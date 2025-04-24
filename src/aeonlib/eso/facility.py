import logging

from aeonlib.conf import settings as default_settings
from aeonlib.exceptions import ServiceNetworkError

from .models import Container, ObservationBlock, Template

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
        try:
            container, version = self.api.createFolder(container_id, name)
            assert container and version
        except Exception as e:
            raise ESONetworkError("Failed to create ESO folder") from e
        logger.debug("<- %s (%s)", container, version)

        return Container.model_validate({**container, "version": version})

    def get_container(self, container_id: int) -> Container:
        try:
            container, version = self.api.getContainer(container_id)
            assert container and version
        except Exception as e:
            raise ESONetworkError("Failed to get ESO container") from e
        logger.debug("<- %s (%s)", container, version)

        return Container.model_validate({**container, "version": version})

    def delete_container(self, container: Container) -> None:
        try:
            self.api.deleteContainer(container.container_id, container.version)
        except Exception as e:
            raise ESONetworkError("Failed to delete ESO container") from e

    def create_ob(self, container: Container, name: str) -> ObservationBlock:
        try:
            ob, version = self.api.createOB(container.container_id, name)
            assert ob and version
        except Exception as e:
            raise ESONetworkError("Failed to create ESO observation block") from e
        logger.debug("<- %s (%s)", ob, version)

        return ObservationBlock.model_validate({**ob, "version": version})

    def get_ob(self, ob_id: int) -> ObservationBlock:
        try:
            ob, version = self.api.getOB(ob_id)
            assert ob and version
        except Exception as e:
            raise ESONetworkError("Failed to get ESO observation block") from e
        logger.debug("<- %s (%s)", ob, version)

        return ObservationBlock.model_validate({**ob, "version": version})

    def save_ob(self, ob: ObservationBlock) -> ObservationBlock:
        ob_dict = ob.model_dump(exclude={"version"})
        logger.debug("-> %s", ob_dict)
        try:
            new_ob_dict, version = self.api.saveOB(ob_dict, ob.version)
            assert new_ob_dict and version
        except Exception as e:
            raise ESONetworkError("Failed to update ESO observation block") from e
        logger.debug("<- %s (%s)", new_ob_dict, version)

        return ObservationBlock.model_validate({**new_ob_dict, "version": version})

    def delete_ob(self, ob: ObservationBlock) -> None:
        try:
            self.api.deleteOB(ob.ob_id, ob.version)
        except Exception as e:
            raise ESONetworkError("Failed to delete ESO observation block") from e

    def create_template(self, ob: ObservationBlock, name: str) -> Template:
        try:
            template, version = self.api.createTemplate(ob.ob_id, name)
            assert template and version
        except Exception as e:
            raise ESONetworkError("Failed to create ESO template") from e
        logger.debug("<- %s (%s)", template, version)

        return Template.model_validate({**template, "version": version})

    def delete_template(self, ob: ObservationBlock, template: Template) -> None:
        try:
            self.api.deleteTemplate(ob.ob_id, template.template_id, template.version)
        except Exception as e:
            raise ESONetworkError("Failed to delete ESO template") from e
