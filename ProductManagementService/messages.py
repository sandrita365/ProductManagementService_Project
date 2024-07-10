class ApiMessages:
    CODE_SUCCESS: str = "200"
    SUCCESSFUL_CREATION_CODE: str = "201"
    SUCCESSFUL_CREATION_MESSAGE: str = "The record was created successfully"
    SUCCESSFUL_UPDATE_CODE: str = "201"
    SUCCESSFUL_UPDATE_MESSAGE: str = "The record was updated successfully. "
    SUCCESSFUL_DELETION_CODE: str = "200"
    SUCCESSFUL_DELETION_MESSAGE: str = "The record was deleted successfully."
    CODE_400: str = "400"
    BAD_REQUEST_MESSAGE = (
        "Please check the format of the message. It seems " 
        "to be a bad request."
    )
    CODE_500: str = "500"
    INTERNAL_SERVER_ERROR: str = "Internal error, please try again."
    CODE_404: str = "404"
    NOT_FOUND: str = (
        "The record you wish to query is not found in the database, please "
        "review and try again."
    )
    SUCCESSFUL_QUERY_CODE: str = "200"
    SUCCESSFUL_QUERY_MESSAGE: str = "The query was executed successfully."
    SUCCESSFUL_QUERY_NO_RECORDS_FOUND: str = (
        "Sorry! There are no records to show.")
    INTERNAL_SERVER_ERROR_UNIT_MEASURE: str = ("Internal error  from Unit "
                                               "Measure "
                                               "Service, please try again")
