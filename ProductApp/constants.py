class AppConstants:
    LOGGER_NAME: str = "app_logger"

    class Api:
        """
        Contains all constants variables.
        """
        CREATE_PRODUCT: str = "product/create/"
        CREATE_PRODUCT_NAME: str = "create_product"
        QUERY_PRODUCTS: str = "products/"
        QUERY_PRODUCTS_NAME: str = "query_all_products/"
        DELETE_PRODUCT_BY_ID: str = "product/delete/"
        DELETE_PRODUCT_BY_ID_NAME: str = "delete_product"
        UPDATE_PRODUCT_BY_ID: str = "product/update/"
        UPDATE_PRODUCT_BY_ID_NAME: str = "update_product"
