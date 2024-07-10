import abc
from typing import List

from bson import ObjectId
from django.db.models import QuerySet
from injector import inject

from DepartmentApp.components.department_ops import DepartmentOps
from DepartmentApp.models import Department
from ProductManagementService.logger import logger


class DepartmentsService(abc.ABC):
    """
    This interface defines the methods of the business logic.
    """

    @abc.abstractmethod
    def query_all(self) -> QuerySet[Department]:
        """
        The  method retrieves all departments from the concrete class
        'DepartmentOpsMongo'.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def query_by_id(self, department_id: str) -> Department:
        """
        The method retrieves a department by ID from the
        'DepartmentOpsMongo' concrete class.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def query_by_name(self, name: str) -> List[dict]:
        """
        The method retrieves a department by name from the
        'DepartmentOpsMongo' concrete class.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def create(self, data: dict) -> dict:
        """
        This method allows to create a new department.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, department: Department, id: str) -> dict:
        """
        This method allows to update a record by ID.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, department_id: str) -> bool:
        """
        This method allows to delete a record by ID.
        """
        raise NotImplementedError


class DepartmentsMongoService(DepartmentsService):
    """
    Concrete class implements the methods of the 'DepartmentsService'
    interface.
    """

    @inject
    def __init__(self, department_ops: DepartmentOps):
        self.department_ops = department_ops

    def query_all(self) -> List[dict]:
        logger.info("Service Layer - query_all method ::: ")
        departments = self.department_ops.query_all()
        department_list = [
            self.convert_to_dict(department) for department in departments

        ]
        return department_list

    def query_by_id(self, department_id: str) -> Department:
        logger.info("Service Layer - query_by_id method :: ")
        oid = ObjectId(department_id)
        department = self.convert_to_dict(self.department_ops.query_by_id(oid))
        return department

    def query_by_name(self, name: str) -> List[dict]:
        logger.info("Service Layer - query_by_name method :: ")
        departments = self.department_ops.query_by_name(name)
        department_list = [
            self.convert_to_dict(department) for department in departments

        ]
        return department_list

    def create(self, data: dict) -> dict:
        logger.info("Service Layer - create method :: ")
        department = self.convert_to_dict(self.department_ops.create(data))
        return department

    def update(self, validated_data: dict, id: str) -> dict:
        logger.info(
            "Service Layer - update method ::",
        )
        oid = ObjectId(id)
        department = self.department_ops.query_by_id(oid)
        name = validated_data.get("name")
        if name is not None:
            department.name = name
        description = validated_data.get("description")
        if description is not None:
            department.description = description
        department._id = oid
        department_update = self.department_ops.update(department)
        department_update._id = str(department_update._id)
        return self.convert_to_dict(department_update)

    def delete(self, department_id: str) -> bool:
        logger.info("Service Layer - delete method :: ")
        department_oid = ObjectId(department_id)
        return self.department_ops.delete(department_oid)

    def convert_to_dict(self, object_model):
        object_dict = {
            '_id': str(object_model._id),
            'name': object_model.name,
            'description': object_model.description,
            'date': object_model.formatted_date(),
            'last_update_date': object_model.formatted_last_update_date()
        }
        return object_dict
