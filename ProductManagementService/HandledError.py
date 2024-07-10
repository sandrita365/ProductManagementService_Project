from .messages import ApiMessages as msg


class HandledError:
    """
    This class handled different types of errors along with their associated code and message.
    """

    def __init__(self):
        self.__value_error = {
            "Code": msg.CODE_400,
            "Message": msg.BAD_REQUEST_MESSAGE,
        }
        self.__exception = {
            "Code": msg.CODE_500,
            "Message": msg.INTERNAL_SERVER_ERROR,
        }
        self.__object_does_not_exist = {
            "Code": msg.CODE_404,
            "Message": msg.NOT_FOUND,
        }

    def get_value_error(self):
        return self.__value_error

    def get_exception(self):
        return self.__exception

    def get_object_doesnot_exist(self):
        return self.__object_does_not_exist
