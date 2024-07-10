class AppConstants:
    LOGGER_NAME: str = "app_logger"

    class Api:
        """
        Contains all constants variables.
        """

        CREATE_DEPARTMENT: str = "department/create/"
        CREATE_DEPARTMENT_NAME: str = "create_department"
        QUERY_DEPARTMENTS: str = "departments/"
        QUERY_DEPARTMENT_NAME: str = "query_all_departments_view"
        QUERY_DEPARTMENTS_ID: str = "departments/<str:department_id>"
        QUERY_DEPARTMENTS_ID_NAME: str = "department_details"
        DELETE_DEPARTMENT_ID: str = "departments/delete/"
        DELETE_DEPARTMENT_ID_NAME: str = "delete_department"
        UPDATE_DEPARTMENT: str = "departments/update/"
        UPDATE_DEPARTMENT_NAME: str = "update_department"
