# Create your views here.
# Create your views here.
import json
import logging

import requests
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from injector import inject
from rest_framework import request, status
from rest_framework.views import APIView

from MeasureApp.serializer import (InUnitMeasureSerializer,
                                   OutInitMeasureWithIdSerializer)
from MeasureApp.services.unitmeasure import UnitMeasureService
from ProductManagementService.logger import logger
from ProductManagementService.messages import ApiMessages as msg


class UnitMeasureAPIView(APIView):
    """
        A view class that handles HTTP requests for various methods such as
        GET, POST,PUT, DELETE, etc. related to 'UnitMeasure' operations.
    """

    @inject
    def __init__(self, unit_measure_service: UnitMeasureService, *arg,
                 **kwargs):
        super().__init__()
        self.unit_measure_service = unit_measure_service

    def get(self, request: request.Request):
        logger.info("View - get method :::")
        name: str = request.query_params.get("name")
        id: str = request.query_params.get("id")
        try:
            if id is not None:
                response_message = self.unit_measure_service.query_by_id(id)
                if not response_message:
                    return JsonResponse({
                        "error": "No unit measures found with the given id."},
                        status=status.HTTP_404_NOT_FOUND)
                serializer_class = OutInitMeasureWithIdSerializer(
                    data=response_message,
                    many=False
                )
            elif name is not None:
                response_message = self.unit_measure_service.query_by_name(
                    name)
                if not response_message:
                    return JsonResponse({
                        "error":
                            "No unit measures found with the given name."},
                        status=status.HTTP_404_NOT_FOUND)
                serializer_class = OutInitMeasureWithIdSerializer(
                    data=response_message,
                    many=True

                )
            else:
                response_message = self.unit_measure_service.query_all()
                if not response_message:
                    return JsonResponse({
                        "error": "No records founds"},
                        status=status.HTTP_404_NOT_FOUND)
                serializer_class = OutInitMeasureWithIdSerializer(
                    data=response_message,
                    many=True

                )
            if not serializer_class.is_valid():
                return JsonResponse({"error": str(
                    serializer_class.errors)},
                    status=status.HTTP_400_BAD_REQUEST)
            return JsonResponse(
                serializer_class.data,
                status=status.HTTP_200_OK,
                safe=False
            )
        except ObjectDoesNotExist as e:
            logging.critical(f"A critical error occurred:  {str(e)}",
                             exc_info=True)
            return JsonResponse({"error": str(e)},
                                status=status.HTTP_404_NOT_FOUND)
        except ValueError as e:
            logging.error(f"Validation error:  {str(e)}")
            return JsonResponse({"error": str(e)},
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.critical(f"A critical error occurred: {str(e)}",
                             exc_info=True)
            return JsonResponse({"error": str(e)},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request: request.Request):
        logger.info("View: post method::: ")
        try:
            data = json.loads(request.body)
            serialized_unitmeasue = InUnitMeasureSerializer(
                data=data,
                many=False
            )
            if not serialized_unitmeasue.is_valid():
                return JsonResponse({"error": str(
                    serialized_unitmeasue.errors)},
                    status=status.HTTP_400_BAD_REQUEST)
            new_object = self.unit_measure_service.create(
                serialized_unitmeasue.validated_data)
            if not new_object:
                return JsonResponse({
                    "error": "INTERNAL SERVICE ERROR"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            serializer_class = OutInitMeasureWithIdSerializer(
                data=new_object,
                many=False
            )
            if not serializer_class.is_valid():
                self.unit_measure_service.delete(str(new_object['_id']))
                return JsonResponse({"error": str(
                    serializer_class.errors)},
                    status=status.HTTP_400_BAD_REQUEST)

            return JsonResponse(serializer_class.data,
                                status=status.HTTP_201_CREATED
                                )
        except ValueError as e:
            logging.error(f"Validation error:  {str(e)}")
            return JsonResponse({"error": str(e)},
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.critical(f"A critical error occurred: {str(e)}",
                             exc_info=True)
            return JsonResponse({"error": str(e)},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request: requests.Request):
        logger.info("View - delete method ::: ")
        try:
            unit_measure_id = request.query_params.get("id")
            result = self.unit_measure_service.delete(unit_measure_id)
            if result is True:
                return JsonResponse(
                    {"message": msg.SUCCESSFUL_DELETION_MESSAGE},
                    status=status.HTTP_200_OK,
                    safe=False

                )
        except ObjectDoesNotExist as e:
            logging.critical(f"A critical error occurred: {str(e)}",
                             exc_info=True)
            return JsonResponse({"error": str(e)},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logging.critical(f"A critical error occurred:{str(e)}",
                             exc_info=True)
            return JsonResponse({"error": str(e)},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request: request.Request):
        logger.info("View - put method")
        try:
            unit_measure_id = request.query_params.get("id")
            request_data = request.data
            serialized_unit_measure = InUnitMeasureSerializer(
                data=request_data,
                many=False,
            )
            if serialized_unit_measure.is_valid():
                unit_measure = self.unit_measure_service.update(
                    serialized_unit_measure.validated_data, unit_measure_id)
                return JsonResponse(
                    unit_measure,
                    status=status.HTTP_201_CREATED,
                    safe=False

                )
            else:
                self.unit_measure_service.delete(unit_measure_id)
                return JsonResponse({"error": str(
                    serialized_unit_measure.errors)},
                    status=status.HTTP_400_BAD_REQUEST,
                    safe=False
                )
        except ObjectDoesNotExist as e:
            logging.critical(f"A critical error occurred: {str(e)}",
                             exc_info=True)
            return JsonResponse({"error": str(e)},
                                status=status.HTTP_404_NOT_FOUND)
        except ValueError as e:
            logging.critical(f"A critical error occurred: {str(e)}",
                             exc_info=True)
            return JsonResponse({"error": str(e)},
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.critical(f"A critical error occurred: {str(e)}",
                             exc_info=True)
            return JsonResponse({"error": str(e)},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
