import logging

from aeonlib.conf import settings as default_settings
from aeonlib.exceptions import ServiceNetworkError

from .models import AbsoluteTimeConstraints, Container, ObservationBlock, Template

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

    def get_template(self, ob: ObservationBlock, template_id: str) -> Template:
        try:
            template_dict, version = self.api.getTemplate(ob.ob_id, template_id)
            assert template_dict and version
        except Exception as e:
            raise ESONetworkError("Failed to get ESO template") from e
        logger.debug("<- %s", template_dict)

        return Template.model_validate({**template_dict, "version": version})

    def update_template_params(
        self, ob: ObservationBlock, template: Template, params: dict
    ) -> Template:
        """
        This method simply updates the parameter dictionary in the template object and saves it.
        Alternatively, one can simply update the Template object directly and use
        `save_template` to save the changes.
        This method is included for consistency with the ESO client library.
        """
        template_dict = template.model_dump(exclude={"version"})
        logger.debug("-> %s (params: %s)", template_dict, params)
        try:
            new_template, version = self.api.setTemplateParams(
                ob.ob_id, template_dict, params, template.version
            )
            assert new_template and version
        except Exception as e:
            raise ESONetworkError("Failed to update ESO template parameters") from e
        logger.debug("<- %s (%s)", template, version)

        return Template.model_validate({**new_template, "version": version})

    def save_template(self, ob: ObservationBlock, template: Template) -> Template:
        template_dict = template.model_dump(exclude={"version"})
        logger.debug("-> %s", template_dict)
        try:
            new_template, version = self.api.saveTemplate(
                ob.ob_id, template_dict, template.version
            )
            assert new_template and version
        except Exception as e:
            raise ESONetworkError("Failed to save ESO template") from e
        logger.debug("<- %s", template)

        return Template.model_validate({**new_template, "version": version})

    def get_absolute_time_constraints(
        self, ob: ObservationBlock
    ) -> AbsoluteTimeConstraints:
        try:
            constraints, version = self.api.getAbsoluteTimeConstraints(ob.ob_id)
            print("Constraints:", constraints)
            assert constraints is not None and version is not None
        except Exception as e:
            raise ESONetworkError("Failed to get ESO absolute time constraints") from e
        logger.debug("<- %s (%s)", constraints, version)

        return AbsoluteTimeConstraints.model_validate(
            {"constraints": constraints, "version": version}
        )

    def save_absolute_time_constraints(
        self, ob: ObservationBlock, constraints: AbsoluteTimeConstraints
    ) -> AbsoluteTimeConstraints:
        constraints_dict = constraints.model_dump(mode="json", exclude={"version"})
        logger.debug("-> %s", constraints_dict)
        try:
            new_constraints, version = self.api.saveAbsoluteTimeConstraints(
                ob.ob_id, constraints_dict["constraints"], constraints.version
            )
            assert new_constraints and version
        except Exception as e:
            raise ESONetworkError("Failed to set ESO absolute time constraints") from e
        logger.debug("<- %s (%s)", constraints, version)

        return AbsoluteTimeConstraints.model_validate(
            {"constraints": new_constraints, "version": version}
        )
