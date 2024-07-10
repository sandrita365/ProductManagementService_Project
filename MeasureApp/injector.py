import injector
from injector import Binder, singleton

from .components.unitmeasure_ops import UnitMeasureOps, UnitMeasureOpsMongo
from .services.unitmeasure import UnitMeasureService, UnitMeasureMongoService


class UnitMeasureInjector(injector.Module):
    """
        This class contains the injector dependency module.
    """

    def configure(self, binder: Binder):
        """
            This method defines the relationship between an interface and
            its implementation class.
        """
        binder.bind(UnitMeasureOps, to=UnitMeasureOpsMongo, scope=singleton, )
        binder.bind(UnitMeasureService, to=UnitMeasureMongoService,
                    scope=singleton, )
