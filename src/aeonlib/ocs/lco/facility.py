import logging
from typing import Any, Callable, Literal

import httpx
from astropy.table import Table

from aeonlib.conf import settings as default_settings
from aeonlib.ocs.request_models import RequestGroup, SubmittedRequestGroup

logger = logging.getLogger(__name__)


def walk_pagination(response: dict, callback: Callable[[dict], None]):
    while response["next"]:
        response = httpx.get(response["next"]).json()
        callback(response)


def dict_table(proposals: list[dict], fields: list[str]) -> Table:
    """Construct an Astropy Table from the given list of dictionaries, containing
    only the specified fields.
    """
    ps = [{field: p[field] for field in fields} for p in proposals]
    return Table(rows=ps)


class LcoFacility:
    """
    Las Cumbres Observatory Facility
    Configuration:
        - AEON_LCO_TOKEN: API token for authentication
        - AEON_LCO_API_ROOT: Root URL of the API
    """

    def __init__(self, settings=default_settings):
        if not settings.lco_token:
            logger.info(
                "AEON_LCO_TOKEN setting is missing, request will be unauthenticated"
            )
            headers = {}
        else:
            headers = {"Authorization": f"Token {settings.lco_token}"}
        self.client = httpx.Client(base_url=settings.lco_api_root, headers=headers)

    def __del__(self):
        self.client.close()

    def proposals(
        self, format: Literal["dict", "table"] = "table"
    ) -> Table | list[dict]:
        response = self.client.get("/proposals/")
        response.raise_for_status()
        proposals = response.json()["results"]
        walk_pagination(response.json(), lambda x: proposals.extend(x["results"]))
        if format == "dict":
            return proposals
        elif format == "table":
            fields = ["id", "active", "title", "requestgroup_count"]
            return dict_table(proposals, fields)

    def serialize_request_group(self, request_group: RequestGroup) -> dict:
        # The LCO api expects certain time fields to be in MJD format instead of datetime.
        # The below mapping is accessed in the Time field to output to MJD.
        output_mapping = {"epochofel": "mjd", "epochofperih": "mjd"}
        return request_group.model_dump(
            mode="json", exclude_none=True, context={"output_mapping": output_mapping}
        )

    def validate_request_group(
        self, request_group: RequestGroup
    ) -> tuple[bool, list[Any]]:
        payload = self.serialize_request_group(request_group)
        logger.debug("LcoFacility.validate_request_group -> %s", payload)
        response = self.client.post("/requestgroups/validate/", json=payload)
        response = response.json()
        logger.debug("<- %s", response)
        if response.get("request_durations"):
            return True, []
        else:
            return False, response.get("errors", [str(response)])

    def submit_request_group(
        self, request_group: RequestGroup
    ) -> SubmittedRequestGroup:
        payload = self.serialize_request_group(request_group)
        logger.debug("-> %s", payload)
        response = self.client.post("/requestgroups/", json=payload)
        response.raise_for_status()
        logger.debug("<- %s", response.content)
        return SubmittedRequestGroup.model_validate_json(response.content)
