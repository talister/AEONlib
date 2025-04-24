import logging

from aeonlib.conf import settings as default_settings
from aeonlib.exceptions import ServiceNetworkError

from .models import Container, ObservationBlock

logger = logging.getLogger(__name__)

try:
    import p2api
except ImportError as e:
    logger.critical("p2api not found. Install the 'eso' dependency group for Aeonlib.")
    raise e


class ESONetworkError(ServiceNetworkError):
    pass


class EsoFacility:
    def __init__(self, settings=default_settings):
        self.api = p2api.ApiConnection(
            settings.eso_environment,
            settings.eso_username,
            settings.eso_password,
            debug=True,
        )

    def create_folder(self, container_id: int, name: str) -> Container:
        container, version = self.api.createFolder(container_id, name)
        if not container or not version:
            raise ESONetworkError("Failed to create ESO folder")
        logger.debug("EsoFacility.create_folder <- %s (%s)", container, version)
        return Container.model_validate({**container, "version": version})

    def get_container(self, container_id: int) -> Container:
        container, version = self.api.getContainer(container_id)
        if not container or not version:
            raise ESONetworkError("Failed to get ESO container")
        logger.debug("EsoFacility.get_container <- %s (%s)", container, version)
        return Container.model_validate({**container, "version": version})

    def delete_container(self, container: Container) -> None:
        self.api.deleteContainer(container.container_id, container.version)

    def create_ob(self, container: Container, name: str) -> ObservationBlock:
        ob, version = self.api.createOB(container.container_id, name)
        if not ob or not version:
            raise ESONetworkError("Failed to create ESO observation block")
        logger.debug("EsoFacility.create_observation_block <- %s (%s)", ob, version)
        ob = ObservationBlock.model_validate({**ob, "version": version})
        return ob

    def get_ob(self, ob_id: int) -> ObservationBlock:
        ob, version = self.api.getOB(ob_id)
        if not ob or not version:
            raise ESONetworkError("Failed to get ESO observation block")
        logger.debug("EsoFacility.get_observation_block <- %s (%s)", ob, version)
        return ObservationBlock.model_validate({**ob, "version": version})

    def save_ob(self, ob: ObservationBlock) -> ObservationBlock:
        ob_dict = ob.model_dump(exclude={"version"})
        logger.debug("EsoFacility.save_ob -> %s", ob_dict)
        new_ob_dict, version = self.api.saveOB(ob_dict, ob.version)
        if not new_ob_dict or not version:
            raise ESONetworkError("Failed to update ESO observation block")
        logger.debug("EsoFacility.save_ob <- %s (%s)", new_ob_dict, version)
        return ObservationBlock.model_validate({**new_ob_dict, "version": version})

    def delete_ob(self, ob: ObservationBlock) -> None:
        self.api.deleteOB(ob.ob_id, ob.version)
