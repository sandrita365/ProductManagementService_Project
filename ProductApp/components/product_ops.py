import abc

from django.db.models import QuerySet

from ProductApp.models import product
from ProductManagementService.logger import logger


class ProductOps(abc.ABC):
    """
    The interface encompasses all the operations of the product model.
    """

    @abc.abstractmethod
    def create(self, data: dict) -> product:
        raise NotImplementedError

    @abc.abstractmethod
    def query_all(self, data: dict) -> QuerySet[product]:
        """
        This method queries all unit measures.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def query_by_id(self, id: str) -> product:
        """
        This method queries a product by ID
        """
        raise NotImplementedError

    @abc.abstractmethod
    def query_by_department_id(self, id: str) -> QuerySet[product]:
        """
        This method queries a product by ID
        """
        raise NotImplementedError

    @abc.abstractmethod
    def query_by_unit_measure_id(self, id: str) -> QuerySet[product]:
        """
        This method queries a product by ID
        """
        raise NotImplementedError

    @abc.abstractmethod
    def query_by_name(self, name: str) -> QuerySet[product]:
        """
        This method queries a product by name
        """
        raise NotImplementedError

    @abc.abstractmethod
    def query_by_description(self, description: str) -> QuerySet[product]:
        """
        This method queries a product by description
        """
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, id: str) -> bool:
        """
        This method deletes a record by ID.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, product_object: product) -> product:
        """
        This method update a record by ID.
        """
        raise NotImplementedError


class ProductOpsMongo(ProductOps):

    def query_all(self) -> QuerySet[product]:
        logger.info("Adapter Layer - query_all method:::")
        return product.objects.all()

    def query_by_id(self, id: str) -> product:
        return product.objects.get(_id=id)

    def query_by_department_id(self, id: str) -> QuerySet[product]:
        return product.objects.filter(department_id=id)

    def query_by_unit_measure_id(self, id: str) -> QuerySet[product]:
        return product.objects.filter(unit_measure_id=id)

    def query_by_name(self, name: str) -> QuerySet[product]:
        return product.objects.filter(name__icontains=name)

    def query_by_description(self, description: str) -> QuerySet[product]:
        return product.objects.filter(description__icontains=description)

    def create(self, data: dict) -> product:
        logger.info("Adapter Layer -create method ::: ")
        name = data.get("name")
        description = data.get("description")
        quantity = data.get("quantity")
        url_picture = data.get("url_picture")
        location = data.get("location")
        lot_flag = data.get("lot_flag")
        price_lot_flag = data.get("price_lot_flag")
        alert_minimum_stock_flag = data.get("alert_minimum_stock_flag")
        alert_expiration_date_flag = data.get("alert_expiration_date_flag")
        comments = data.get("comments")
        date = data.get("date")
        last_update = data.get("last_update")
        department_id = data.get("department_id")
        unit_measure_id = data.get("unit_measure_id")
        new_product = product.objects.create(
            name=name,
            description=description,
            quantity=quantity,
            url_picture=url_picture,
            location=location,
            lot_flag=lot_flag,
            price_lot_flag=price_lot_flag,
            alert_minimum_stock_flag=alert_minimum_stock_flag,
            alert_expiration_date_flag=alert_expiration_date_flag,
            comments=comments,
            date=date,
            last_update=last_update,
            department_id=department_id,
            unit_measure_id=unit_measure_id,
        )
        return new_product

    def delete(self, id: str) -> bool:
        get_product = product.objects.get(_id=id)
        delete_count, delete_dict = get_product.delete()
        if delete_count > 0:
            return True
        else:
            return False

    def update(self, product_object: product) -> product:
        logger.info("Adapter layer -update method:::")
        product_object.save()
        return product_object
