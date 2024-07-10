import json
import logging

import requests
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from injector import inject
from rest_framework import request, status
from rest_framework.views import APIView

from ProductApp.services.products import ProductService
from ProductManagementService.logger import logger
from ProductManagementService.messages import ApiMessages as msg
from .serializer import OutSerializerAllFields, InSerializer


# Create your views here.

class ProductAPIView(APIView):
    """
    vv
    """

    @inject
    def __init__(self, product_service: ProductService):
        super().__init__()
        self.product_service = product_service

    def post(self, request: request.Request):
        logger.info("View - post method ")
        try:
            data = json.loads(request.body)
            serialized_request = InSerializer(
                data=data,
                many=False,
            )
            if not serialized_request.is_valid():
                logging.critical(f"Error ::{serialized_request.errors}",
                                 exc_info=True)
                return JsonResponse(
                    {"error": serialized_request.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
            response_message = self.product_service.create(
                serialized_request.validated_data)
            if response_message["code"] != 201:
                return JsonResponse(
                    {
                        "message": response_message["message"]
                    }, status=response_message["code"]
                )
            new_product = response_message["product"]
            out_serializer = OutSerializerAllFields(
                data=new_product,
                many=False
            )
            if not out_serializer.is_valid():
                return JsonResponse({"error": out_serializer.errors},
                                    status=status.HTTP_400_BAD_REQUEST)
            return JsonResponse(
                out_serializer.validated_data,
                status=status.HTTP_201_CREATED
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

    def get(self, request: requests.Request):
        logger.info("View - get method:::")
        try:
            id: str = request.query_params.get("id")
            name: str = request.query_params.get("name")
            description: str = request.query_params.get("description")
            department_id: str = request.query_params.get("department_id")
            unit_measure_id: str = request.query_params.get("unit_measure_id")

            if id is not None:
                product = self.product_service.query_by_id(id)
                serializer = OutSerializerAllFields(
                    data=product,
                    many=False
                )

            elif name is not None:
                products = self.product_service.query_by_name(name)
                if not products:
                    return JsonResponse({
                        "error": "There is no records "
                                 "that show."},
                        status=status.HTTP_404_NOT_FOUND)
                serializer = OutSerializerAllFields(
                    data=products,
                    many=True
                )
            elif description is not None:
                products = self.product_service.query_by_description(
                    description)
                if not products:
                    return JsonResponse({
                        "error": "There is no records "
                                 "that show."},
                        status=status.HTTP_404_NOT_FOUND)
                serializer = OutSerializerAllFields(
                    data=products,
                    many=True
                )
            elif department_id is not None:
                products = self.product_service.query_by_department_id(
                    department_id)
                if not products:
                    return JsonResponse({
                        "error": "There is no records "
                                 "that show."},
                        status=status.HTTP_404_NOT_FOUND)
                serializer = OutSerializerAllFields(
                    data=products,
                    many=True
                )
            elif unit_measure_id is not None:
                products = self.product_service.query_by_unit_measure_id(
                    unit_measure_id)
                if not products:
                    return JsonResponse({
                        "error": "There is no records "
                                 "that show."},
                        status=status.HTTP_404_NOT_FOUND)
                serializer = OutSerializerAllFields(
                    data=products,
                    many=True
                )
            else:
                products = self.product_service.query_all()
                serializer = OutSerializerAllFields(
                    data=products,
                    many=True
                )
            if not serializer.is_valid():
                return JsonResponse(
                    {"error": serializer.errors},
                    status=status.HTTP_404_NOT_FOUND
                )
            return JsonResponse(
                serializer.data,
                status=status.HTTP_200_OK,
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
            logging.error(f"Validate error:{str(e)}", exc_info=True)
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

    def delete(self, request: requests.Request):
        logger.info("View -delete method::")
        try:
            id: str = request.query_params.get("id")
            result = self.product_service.delete(id)
            if not result:
                return JsonResponse(
                    {"error": "INTERNAL SERVER"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
            return JsonResponse(
                {"message": msg.SUCCESSFUL_DELETION_MESSAGE},
                status=status.HTTP_200_OK,
                safe=False
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

    def put(self, request: request.Request):
        logger.info("View - put method ::: ")
        try:
            id = request.query_params.get("id")
            data = request.data
            serializer = InSerializer(
                data=data,
                many=False
            )
            if not serializer.is_valid():
                return JsonResponse(
                    {"error": str(serializer.errors)},
                    status=status.HTTP_400_BAD_REQUEST,
                    safe=False

                )
            update_product = self.product_service.update(
                serializer.validated_data, id)
            serializer_out = OutSerializerAllFields(
                data=update_product,
                many=False
            )
            if not serializer_out.is_valid():
                return JsonResponse(
                    {"error": str(serializer_out.errors)},
                    status=status.HTTP_400_BAD_REQUEST
                )
            return JsonResponse(
                update_product,
                status=status.HTTP_201_CREATED,
                safe=False
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
                {"Error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            logging.critical(f"A critical error occurred:{str(e)}",
                             exc_info=True)
            return JsonResponse(
                {"Error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
