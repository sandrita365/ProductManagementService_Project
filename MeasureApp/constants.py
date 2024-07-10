class AppConstants:
    LOGGER_NAME: str = "app_logger"

    class Api:
        """
        Contains all constants variables.
        """
        QUERY_UNITMEASURE: str = "unitmeasure/"
        QUERY_UNITMEASURE_NAME: str = "query_all_unitmeasure"
        QUERY_BY_ID_UNITMEASURE: str = "unitmeasure/"
        QUERY_BY_ID_UNITMEASURE_NAME: str = "query_BY_ID_unitmeasure"
        CREATE_UNITMEASURE: str = "unitmeasure/create/"
        CREATE_UNITMEASURE_NAME: str = "create_unitmeasure"
        DELETE_UNITMEASURE: str = "unitmeasure/delete/"
        DELETE_UNITMEASURE_NAME: str = "delete_unit_measure"
        UPDATE_UNITMEASURE: str = "unitmeasure/update/"
        UPDATE_UNITMEASURE_NAME: str = "update_unit_measure"
