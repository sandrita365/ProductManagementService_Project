# Create your views here.
import json
import logging

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from injector import inject
from rest_framework import request, status
from rest_framework.views import APIView

from DepartmentApp.serializers import (
    InDepartmentSerializer,
    OutSerializer,
)
from DepartmentApp.services.departments import DepartmentsService
from ProductManagementService.logger import logger
from ProductManagementService.messages import ApiMessages as msg


class DepartmentsAPIView(APIView):
    """
    A view class that handles HTTP requests for various methods such as GET, POST,
    PUT, DELETE, etc. related to 'Department' operations.
    """

    @inject
    def __init__(self, department_service: DepartmentsService, *args,
                 **kwargs):
        """
        Constructor adds an instance of the DepartmentsService implementation in
        the container.
        :param department_service: Interface contains the 'DepartmentsService' operations.
        """
        super().__init__()
        self.department_service = department_service

    def post(self, request: request.Request):
        logger.info("View - post method :::")
        try:
            data = json.loads(request.body)
            serialized_department = InDepartmentSerializer(
                data=data,
                many=False,
            )
            if not serialized_department.is_valid():
                return JsonResponse(
                    {"error": str(serialized_department.errors)},
                    status=status.HTTP_400_BAD_REQUEST
                )
            new_department = self.department_service.create(
                serialized_department.validated_data)
            serializer = OutSerializer(
                data=new_department,
                many=False
            )
            if not serializer.is_valid():
                return JsonResponse(
                    {"error": str(serializer.errors)},
                    status=status.HTTP_400_BAD_REQUEST,
                    safe=False
                )
            return JsonResponse(
                serializer.validated_data,
                status=status.HTTP_200_OK
            )
        except ValueError as e:
            logging.critical(f"A critical error occurred: {str(e)}",
                             exc_info=True)
            return JsonResponse(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            logging.critical(f"A critical error occurred: {str(e)}",
                             exc_info=True)
            return JsonResponse(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request: request.Request):
        logger.info("View - put method :::")
        try:
            request_data = request.data
            department_id = request.query_params.get("id")
            serialized_department = InDepartmentSerializer(
                data=request_data,
                many=False,
            )
            if not serialized_department.is_valid():
                return JsonResponse(
                    {"error": str(serialized_department.errors)},
                    status=status.HTTP_400_BAD_REQUEST,
                    safe=False
                )
            department = self.department_service.update(
                serialized_department.validated_data, department_id
            )
            serializer_out = OutSerializer(
                data=department,
                many=False,
            )
            if not serializer_out.is_valid():
                return JsonResponse(
                    {"error": str(serializer_out.errors)},
                    status=status.HTTP_400_BAD_REQUEST,
                    safe=False
                )
            return JsonResponse(
                serializer_out.validated_data,
                status=status.HTTP_200_OK
            )

        except ObjectDoesNotExist as e:
            logging.critical(f"A critical error occurred:{str(e)}",
                             exc_info=True)
            return JsonResponse(
                {"error": str(e)},
                status=status.HTTP_404_NOT_FOUND
            )
        except ValueError as e:
            logging.critical(f"A critical error occurred:{str(e)}",
                             exc_info=True)
            return JsonResponse(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            logging.critical(f"A critical error occurred:{str(e)}",
                             exc_info=True)
            return JsonResponse(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def get(self, request: request.Request):
        """
        This method handles GET requests to retrieve department data.
        :param request:Contains information about the request sent by the
        client.
        :param department_id:(Optional) ID of the department to retrieve. If
        the ID is not provided, retrieves all departments.
        :return: JSON response with department data.
        """
        logger.info("View - get method :::")
        try:
            id: str = request.query_params.get("id")
            name: str = request.query_params.get("name")
            if id is not None:
                department = self.department_service.query_by_id(id)
                serializer = OutSerializer(
                    data=department,
                    many=False
                )
            elif name is not None:
                department_list = self.department_service.query_by_name(name)
                if department_list:
                    serializer = OutSerializer(
                        data=department_list,
                        many=True,
                    )
                else:
                    return JsonResponse(
                        {"error": "There are no records that show."},
                        status=status.HTTP_404_NOT_FOUND
                    )
            else:
                department_list = self.department_service.query_all()
                if department_list:
                    serializer = OutSerializer(
                        data=department_list,
                        many=True
                    )
                else:
                    return JsonResponse(
                        {"error": "There are no records that show."},
                        status=status.HTTP_404_NOT_FOUND
                    )
            if not serializer.is_valid():
                logging.critical("A critical error occurred",
                                 serializer.errors)
                return JsonResponse({"error": str(serializer.errors)},
                                    status=status.HTTP_400_BAD_REQUEST)

            return JsonResponse(serializer.validated_data,
                                status=status.HTTP_201_CREATED,
                                safe=False
                                )
        except ObjectDoesNotExist as e:
            logging.critical(f"A critical error occurred: {str(e)}",
                             exc_info=True)
            return JsonResponse(
                {"error": str(e)},
                status=status.HTTP_404_NOT_FOUND
            )
        except ValueError as e:
            logging.critical(f"A critical error occurred: {str(e)}",
                             exc_info=True)
            return JsonResponse(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            logging.critical(f"A critical error occurred: {str(e)}",
                             exc_info=True)
            return JsonResponse({"error": str(e)},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        logger.info("View - delete method :::")
        try:
            id: str = request.query_params.get("id")
            result = self.department_service.delete(id)
            if result is True:
                return JsonResponse(
                    {
                        "Message": msg.SUCCESSFUL_DELETION_MESSAGE,
                    },
                    status=status.HTTP_200_OK
                )
        except ObjectDoesNotExist as e:
            logging.critical(f"A critical error occurred:{str(e)}",
                             exc_info=True)
            return JsonResponse(
                {"error": str(e)},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            logging.critical(f"A critical error occurred:{str(e)}",
                             exc_info=True)
            return JsonResponse(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR

            )
