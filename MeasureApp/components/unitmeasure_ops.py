import abc

from django.db.models import QuerySet

from MeasureApp.models import UnitMeasure
from ProductManagementService.logger import logger


class UnitMeasureOps(abc.ABC):
    """
    This interface encompasses all the operations of the unitmeasure model.
    """

    @abc.abstractmethod
    def query_all(self) -> QuerySet[UnitMeasure]:
        """
        This method queries all unit measures.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def query_by_id(self, unit_measure_id: str) -> UnitMeasure:
        """
        This method queries a unit measure by Id.
        """

        raise NotImplementedError

    @abc.abstractmethod
    def query_by_name(self, name: str) -> QuerySet[UnitMeasure]:
        """
        This method queries unit measures by name.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def create(self, data: dict) -> UnitMeasure:
        """
        This method creates a new record in the database..
        """
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, unitmeasure_id: str) -> bool:
        """
        This method deletes a record by ID.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, unit_measure: UnitMeasure) -> UnitMeasure:
        """
        This method updates a record by ID.
        """
        raise NotImplementedError


class UnitMeasureOpsMongo(UnitMeasureOps):
    """
    The concrete class implements the operations of the UnitMeasureOps
    interface by connecting to a Mongo database.
    """

    def query_all(self) -> QuerySet[UnitMeasure]:
        return UnitMeasure.objects.all()

    def query_by_id(self, unit_measure_id: str) -> UnitMeasure:
        return UnitMeasure.objects.get(_id=unit_measure_id)

    def query_by_name(self, name: str) -> QuerySet[UnitMeasure]:
        return UnitMeasure.objects.filter(name__icontains=name)

    def create(self, data: dict) -> UnitMeasure:
        logger.info("Adapter layer - create method :::")
        name = data.get("name")
        abbreviation = data.get("abbreviation")
        description = data.get("description")
        new_measure = UnitMeasure.objects.create(name=name,
                                                 abbreviation=abbreviation,
                                                 description=description)
        return new_measure

    def delete(self, unit_measure_id: str) -> bool:
        logger.info("Adapter layer - delete method :::")
        unit_measure = UnitMeasure.objects.get(_id=unit_measure_id)
        unit_measure.delete()
        return True

    def update(self, unit_measure: UnitMeasure) -> UnitMeasure:
        logger.info("Adapter layer - update method :::")
        unit_measure.save()
        return unit_measure
