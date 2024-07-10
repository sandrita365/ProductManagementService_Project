import abc

import requests

from ProductManagementService.logger import logger


class UnitMeasureRequest(abc.ABC):
    """
    This interface encompasses all the operations of the unit measure api rest.
    """

    @abc.abstractmethod
    def query_by_id(self, url: str) -> requests.Response:
        raise NotImplementedError


class UnitMeasureApiRest(UnitMeasureRequest):
    def query_by_id(self, url: str) -> requests.Response:
        logger.info("Adapter Layer - query_by_id method ::: ")
        return requests.get(url)
