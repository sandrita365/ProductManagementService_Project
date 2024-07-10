import abc

import requests

from ProductManagementService.logger import logger


class DepartmentRequest(abc.ABC):
    """
       The interface encompasses all the operations of the department api
       rest.
    """

    @abc.abstractmethod
    def query_by_id(self, url: str) -> requests.Response:
        raise NotImplementedError


class DepartmentApiRequest(DepartmentRequest):

    def query_by_id(self, url: str) -> requests.Response:
        logger.info("Adapter Layer - query_by_id method ::: ")
        return requests.get(url)
