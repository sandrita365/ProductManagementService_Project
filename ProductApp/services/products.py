import abc
from typing import Any
from typing import List

from bson import ObjectId
from django.db.models import QuerySet
from injector import inject

from ProductApp.components.department_api_request import DepartmentRequest
from ProductApp.components.product_ops import ProductOps
from ProductApp.components.unitmeasure_api_request import UnitMeasureRequest
from ProductApp.models import product
from ProductManagementService.env import AppEnv
from ProductManagementService.logger import logger


class ProductService(abc.ABC):
    """
    This interface defines the methods of the business logic.
    """
    @abc.abstractmethod
    def create(self, data: dict) -> dict:
        """
        This method allows to create a new product.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def query_all(self) -> QuerySet[product]:
        """
        This method retrieves a unit measure by ID from the ProductOpsMongo
        concrete class.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def query_by_id(self, id: str) -> product:
        """
        This method retrieves a product by ID from the ProductOpsMongo
        concrete class.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def query_by_department_id(self, id: str) -> List[product]:
        """
        This method retrieves a product by department ID from the
        ProductOpsMongo concrete class.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def query_by_unit_measure_id(self, id: str) -> List[product]:
        """
        This method retrieves a product by Unit measure ID from the
        ProductOpsMongo concrete class.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def query_by_name(self, name: str) -> List[product]:
        """
        This method retrieves a product by name from the ProductOpsMongo
        concrete class.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def query_by_description(self, description: str) -> List[product]:
        """
        This method retrieves a product by description from the
        ProductOpsMongo concrete class.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, id: str) -> bool:
        """
        This method execute the business logic to delete a record by ID using
        the ProductOpsMongo concrete class

        """
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, data: dict, id: str) -> dict:
        """
        This method execute the business logic to update a record by ID
        using the ProductOpsMongo concrete class.
        """
        raise NotImplementedError


class ProductMongoService(ProductService):

    @inject
    def __init__(self, product_ops: ProductOps,
                 unitmeasure_ops: UnitMeasureRequest,
                 department_ops: DepartmentRequest):
        self.product_ops = product_ops
        self.unitmeasure_ops = unitmeasure_ops
        self.department_ops = department_ops

    def create(self, data: dict) -> dict[str, Any]:
        logger.info("Service Layer -create method")

        unit_measure_id = data.get("unit_measure_id")
        department_id = data.get("department_id")
        if unit_measure_id is not None:

            url_measure = f"{AppEnv.QUERY_UNIT_MEASURE_BY_ID}?id={str(
                unit_measure_id)}"
            unit_measure = self.unitmeasure_ops.query_by_id(url_measure)

            if unit_measure.status_code != 200:
                return {
                    "code": unit_measure.status_code,
                    "message": unit_measure.text
                }
        if department_id is not None:
            url_department = \
                f"{AppEnv.QUERY_DEPARTMENT_BY_ID}?id={str(department_id)}"
            department = self.department_ops.query_by_id(url_department)
            status_code = department.status_code
            if department.status_code != 201:
                if status_code == 404:
                    return {
                        "code": status_code,
                        "message": department.text
                    }
                else:
                    return {
                        "code": status_code,
                        "message": department.text
                    }

        product = self.convert_to_dict(self.product_ops.create(data))
        return {
            "code": 201,
            "product": product
        }

    def query_all(self) -> dict:
        logger.info("Service Layer -query_all method")
        departments = self.product_ops.query_all()
        departments_list = [
            self.convert_to_dict(department) for department in departments
        ]
        return departments_list

    def query_by_id(self, id: str) -> dict:
        logger.info("Service layer - query_by_id method")
        oid = ObjectId(id)
        product = self.product_ops.query_by_id(oid)
        return self.convert_to_dict(product)

    def query_by_department_id(self, id: str) -> List[product]:
        logger.info("Service layer - query_by_department_id method")
        oid = ObjectId(id)
        products = self.product_ops.query_by_department_id(oid)
        products_list = [
            self.convert_to_dict(product) for product in products
        ]
        return products_list

    def query_by_unit_measure_id(self, id: str) -> List[product]:
        logger.info("Service layer - query_by_unit_measure_id method")
        oid = ObjectId(id)
        products = self.product_ops.query_by_unit_measure_id(oid)
        products_list = [
            self.convert_to_dict(product) for product in products
        ]
        return products_list

    def query_by_name(self, name: str) -> List[dict]:
        logger.info("Service layer - query_by_name method")
        departments = self.product_ops.query_by_name(name)
        department_list = [
            self.convert_to_dict(department) for department in departments
        ]
        return department_list

    def query_by_description(self, description: str) -> List[dict]:
        logger.info("Service layer - query_by_description method")
        departments = self.product_ops.query_by_description(description)
        department_list = [
            self.convert_to_dict(department) for department in departments
        ]
        return department_list

    def delete(self, id: str) -> bool:
        logger.info("Services layer -delete method:::")
        oid = ObjectId(id)
        return self.product_ops.delete(oid)

    def update(self, data: dict, id: str) -> dict:
        logger.info("Serice Layer -update method:::")
        oid = ObjectId(id)
        get_product = self.product_ops.query_by_id(oid)
        name = data.get("name")
        if name is not None:
            get_product.name = name
        description = data.get("description")
        if description is not None:
            get_product.description = description
        quantity = data.get("quantity")
        if quantity is not None:
            get_product.quantity = quantity
        url_picture = data.get("url_picture")
        if url_picture is not None:
            get_product.url_picture = url_picture
        location = data.get("location")
        if location is not None:
            get_product.location = location
        lot_flag = data.get("lot_flag")
        if lot_flag is not None:
            get_product.lot_flag = lot_flag
        price_lot_flag = data.get("price_lot_flag")
        if price_lot_flag is not None:
            get_product.price_lot_flag = price_lot_flag
        alert_minimum_stock_flag = data.get("alert_minimum_stock_flag")
        if alert_minimum_stock_flag is not None:
            get_product.alert_minimum_stock_flag = alert_minimum_stock_flag
        alert_expiration_date_flag = data.get("alert_expiration_date_flag")
        if alert_expiration_date_flag is not None:
            get_product.alert_expiration_date_flag = alert_expiration_date_flag
        comments = data.get("comments")
        if comments is not None:
            get_product.comments = comments
        department_id = data.get("department_id")
        if department_id is not None:
            get_product.department_id = department_id
        unit_measure_id = data.get("unit_measure_id")
        if unit_measure_id is not None:
            get_product.unit_measure_id = unit_measure_id
        update_product = self.product_ops.update(get_product)
        return self.convert_to_dict(update_product)

    def convert_to_dict(self, object_model: product):

        object_dict = {
            '_id': str(object_model._id),
            'name': object_model.name,
            'description': object_model.description,
            'quantity': object_model.quantity,
            'url_picture': object_model.url_picture,
            'location': object_model.location,
            'lot_flag': object_model.lot_flag,
            'price_lot_flag': object_model.price_lot_flag,
            'alert_minimum_stock_flag': object_model.alert_minimum_stock_flag,
            'alert_expiration_date_flag':
                object_model.alert_expiration_date_flag,
            'comments': object_model.comments,
            'date': object_model.formatted_date(),
            'last_update': object_model.formatted_last_update(),
            'department_id': object_model.department_id,
            'unit_measure_id': object_model.unit_measure_id
        }
        return object_dict
