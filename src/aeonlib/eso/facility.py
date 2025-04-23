import logging

from aeonlib.conf import settings as default_settings

from .models import Container

logger = logging.getLogger(__name__)

try:
    import p2api
except ImportError as e:
    logger.critical("p2api not found. Install the 'eso' dependency group for Aeonlib.")
    raise e


class EsoFacility:
    def __init__(self, settings=default_settings):
        self.api = p2api.ApiConnection(
            settings.eso_environment,
            settings.eso_username,
            settings.eso_password,
            debug=True,
        )

    def create_folder(self, container_id: int, name: str) -> Container:
        container, tx_id = self.api.createFolder(container_id, name)
        logger.debug("EsoFacility.create_folder <- %s (%s)", container, tx_id)
        return Container.model_validate(container)
