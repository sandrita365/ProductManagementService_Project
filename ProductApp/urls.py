from django.urls import path

from ProductApp.views import ProductAPIView
from .constants import AppConstants

urlpatterns = [
    path(
        AppConstants.Api.CREATE_PRODUCT,
        ProductAPIView.as_view(),
        name=AppConstants.Api.CREATE_PRODUCT_NAME
    ),
    path(
        AppConstants.Api.QUERY_PRODUCTS,
        ProductAPIView.as_view(),
        name=AppConstants.Api.QUERY_PRODUCTS_NAME
    ),
    path(
        AppConstants.Api.DELETE_PRODUCT_BY_ID,
        ProductAPIView.as_view(),
        name=AppConstants.Api.DELETE_PRODUCT_BY_ID_NAME
    ),
    path(
        AppConstants.Api.UPDATE_PRODUCT_BY_ID,
        ProductAPIView.as_view(),
        name=AppConstants.Api.UPDATE_PRODUCT_BY_ID_NAME

    )
]
