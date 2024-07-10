import injector
from injector import Binder, singleton

from .components.department_ops import DepartmentOps, DepartmentOpsMongo
from .services.departments import DepartmentsService, DepartmentsMongoService


class DepartmentInjector(injector.Module):
    """
    This class contains the injector dependency module.
    """

    def configure(self, binder: Binder):
        """
        This method defines the relationship between an interface
        and its implementation class.
        :param binder:Allows linking the interface to a concrete
        implementation class.
        :return:None
        """
        binder.bind(
            DepartmentOps,
            to=DepartmentOpsMongo,
            scope=singleton,
        )
        binder.bind(
            DepartmentsService,
            to=DepartmentsMongoService,
            scope=singleton,
        )
