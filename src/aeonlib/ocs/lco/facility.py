import logging
import os
from typing import Any, Callable, Literal

import httpx
from astropy.table import Table

from aeonlib.ocs.request_models import RequestGroup, SubmittedRequestGroup

logger = logging.getLogger(__name__)


def lco_token() -> str:
    token = os.getenv("AEONLIB_LCO_TOKEN", "")
    if not token:
        logger.error(
            "AEONLIB_LCO_TOKEN environment variable not set, request will be unauthenticated"
        )
    return token


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
    def __init__(self, *args, api_root="https://api.lco.global", **kwargs):
        self.api_key = lco_token()
        self.headers = {"Authorization": f"Token {self.api_key}"}
        self.client = httpx.Client(base_url=api_root, headers=self.headers)

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

    def validate_request_group(
        self, request_group: RequestGroup
    ) -> tuple[bool, list[Any]]:
        payload = request_group.model_dump(mode="json", exclude_none=True)
        response = self.client.post("/requestgroups/validate/", json=payload)
        response = response.json()
        if response["request_durations"]:
            return True, []
        else:
            return False, response["errors"]

    def submit_request_group(
        self, request_group: RequestGroup
    ) -> SubmittedRequestGroup:
        payload = request_group.model_dump(mode="json", exclude_none=True)
        response = self.client.post("/requestgroups/", json=payload)
        response.raise_for_status()
        return SubmittedRequestGroup.model_validate_json(response.content)
