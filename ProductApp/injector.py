import injector
from injector import Binder, singleton

from .components.department_api_request import DepartmentRequest, \
    DepartmentApiRequest
from .components.product_ops import ProductOps, ProductOpsMongo
from .components.unitmeasure_api_request import UnitMeasureRequest, \
    UnitMeasureApiRest
from .services.products import ProductService, ProductMongoService


class ProductInjector(injector.Module):
    """
    This class contains the injector dependency module
    """

    def configure(self, binder: Binder):
        """
         This method defines the relationship between an interface and its
         implementation class
        """
        binder.bind(
            ProductOps,
            to=ProductOpsMongo,
            scope=singleton,

        )
        binder.bind(
            ProductService,
            to=ProductMongoService,
            scope=singleton
        )
        binder.bind(
            UnitMeasureRequest,
            to=UnitMeasureApiRest,
            scope=singleton,
        )
        binder.bind(
            DepartmentRequest,
            to=DepartmentApiRequest,
            scope=singleton,
        )
