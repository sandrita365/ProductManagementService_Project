import abc
from abc import abstractmethod

from django.db.models import QuerySet

from DepartmentApp.models import Department
from ProductManagementService.logger import logger


class DepartmentOps(abc.ABC):
    """
    The interface encompasses all the operations of the department model.
    """

    @abstractmethod
    def query_all(self) -> QuerySet[Department]:
        """
        The method retrieves all departments from the database.
        """
        raise NotImplementedError

    @abstractmethod
    def query_by_id(self, department_id: str) -> Department:
        """
        The method retrieves a department by its ID from the
        database.
        """
        raise NotImplementedError

    @abstractmethod
    def query_by_name(self, name: str) -> Department:
        """
        This method defines the structure to query departments by name.
        """
        raise NotImplementedError

    @abstractmethod
    def create(self, data: dict) -> Department:
        """
        This method allows to add a new department.
        """
        raise NotImplementedError

    @abstractmethod
    def update(self, department: Department) -> Department:
        """
        This method allows to update a department by ID.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, department_id: str) -> bool:
        """
        This method allows to delete a record by ID.
        """
        raise NotImplementedError


class DepartmentOpsMongo(DepartmentOps):
    """
    The concrete class implements the operations of the DepartmentOps
    interface by connecting to a Mongo database.
    """

    def query_all(self) -> QuerySet[Department]:
        logger.info(" Adapter Layer - query_all method ::: ")
        departments = Department.objects.all()
        return departments

    def query_by_id(self, department_id: str) -> Department:
        logger.info("Adapter Layer - query_by_id method ::: ")
        department = Department.objects.get(_id=department_id)
        return department

    def query_by_name(self, name: str) -> Department:
        logger.info("Adapter Layer - query_by_name method ::: ")
        department = Department.objects.filter(name__icontains=name)
        return department

    def create(self, data: dict) -> Department:
        logger.info("Adapter Layer - new_department method ::: ")
        name = data.get("name")
        description = data.get("description")
        new_department = Department.objects.create(name=name,
                                                   description=description)
        return new_department

    def update(self, department: Department) -> Department:
        logger.info("Adapter Layer - update method :::")
        department.save()
        return department

    def delete(self, department_id: str) -> bool:
        logger.info("Adapter Layer - delete method ::: ")
        department = Department.objects.get(_id=department_id)
        department.delete()
        return True
