import abc
from typing import List

from bson import ObjectId
from injector import inject

from MeasureApp.components.unitmeasure_ops import UnitMeasureOps
from ProductManagementService.logger import logger


class UnitMeasureService(abc.ABC):
    """
    This interface defines the methods of the business logic.
    """

    @inject
    def __init__(self, unit_measure_ops: UnitMeasureOps):
        self.unit_measure_ops = unit_measure_ops

    @abc.abstractmethod
    def query_all(self) -> dict:
        """
        This method retrieves all unit measures from
        the UnitMeasureOpsMongo concrete class
        """
        raise NotImplementedError

    @abc.abstractmethod
    def query_by_id(self, unit_measure_id: str) -> dict:
        """
        This method retrieves a unit measure by ID from the
        UnitMeasureOpsMongo concrete class.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def query_by_name(self, name: str) -> List[dict]:
        """
        This method retrieves unit measures by name from
        the UnitMeasureOpsMongo concrete class.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def create(self, data: dict) -> dict:
        """
        This method executes the business logic to create a new unit
        measure record using the UnitMeasureOpsMongo concrete class.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, unit_measure_id: str) -> bool:
        """
        This method execute the business logic to delete a record by ID using
        the UnitMeasureOpsMongo concrete class
        """
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, data: dict, id: str) -> dict:
        """
        This method execute the business logic to update a record by ID
        using the UnitMeasureOpsMongo concrete class

        """
        raise NotImplementedError


class UnitMeasureMongoService(UnitMeasureService):
    def query_all(self) -> List[dict]:
        logger.info("Service Layer - querry_all method:::")
        unit_measures = self.unit_measure_ops.query_all()
        unit_measure_list = [
            self.convert_to_dict(unit_measure) for unit_measure in
            unit_measures
        ]
        return unit_measure_list

    def query_by_id(self, unit_measure_id: str) -> dict:
        logger.info("Service Layer - query_by_id method:::")
        unit_measure_oid = ObjectId(unit_measure_id)
        unit_measure = self.unit_measure_ops.query_by_id(
            unit_measure_oid)
        return self.convert_to_dict(unit_measure)

    def query_by_name(self, name: str) -> List[dict]:
        logger.info("Service Layer - query_by_name method:::")
        unit_measures = list(self.unit_measure_ops.query_by_name(name))
        unit_measure_list = [
            self.convert_to_dict(unit_measure) for unit_measure in
            unit_measures
        ]
        return unit_measure_list

    def create(self, data: dict) -> dict:
        logger.info("Service Layer - create method:::")
        new_object = self.convert_to_dict(self.unit_measure_ops.create(data))
        return new_object

    def delete(self, unit_measure_id: str) -> bool:
        logger.info("Service Layer - delete method:::")
        unit_measure_oid = ObjectId(unit_measure_id)
        self.unit_measure_ops.delete(unit_measure_oid)
        return True

    def update(self, data: dict, id: str) -> dict:
        logger.info("Service Layer - update method:::")
        unit_measure_oid = ObjectId(id)
        unit_measure = self.unit_measure_ops.query_by_id(unit_measure_oid)
        name = data.get("name")
        if name is not None:
            unit_measure.name = name
        abbreviation = data.get("abbreviation")
        if abbreviation is not None:
            unit_measure.abbreviation = abbreviation
        description = data.get("description")
        if description is not None:
            unit_measure.description = data.get("description")
        unit_measure_update = self.unit_measure_ops.update(unit_measure)
        return self.convert_to_dict(unit_measure_update)

    def convert_to_dict(self, object_model):

        object_dict = {
            '_id': str(object_model._id),
            'name': object_model.name,
            'abbreviation': object_model.abbreviation,
            'description': object_model.description,
            'date': object_model.formatted_date(),
            'last_update_date': object_model.formatted_last_update_date()
        }
        return object_dict
