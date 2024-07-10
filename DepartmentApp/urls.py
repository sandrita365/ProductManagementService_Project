from django.urls import path

from .constants import AppConstants
from .views import DepartmentsAPIView

urlpatterns = [
    path(
        AppConstants.Api.QUERY_DEPARTMENTS,
        DepartmentsAPIView.as_view(),
        name=AppConstants.Api.QUERY_DEPARTMENT_NAME,
    ),
    path(
        AppConstants.Api.QUERY_DEPARTMENTS_ID,
        DepartmentsAPIView.as_view(),
        name=AppConstants.Api.QUERY_DEPARTMENTS_ID_NAME,
    ),
    path(
        AppConstants.Api.DELETE_DEPARTMENT_ID,
        DepartmentsAPIView.as_view(),
        name=AppConstants.Api.DELETE_DEPARTMENT_ID_NAME,
    ),
    path(
        AppConstants.Api.UPDATE_DEPARTMENT,
        DepartmentsAPIView.as_view(),
        name=AppConstants.Api.UPDATE_DEPARTMENT_NAME,
    ),
    path(
        AppConstants.Api.CREATE_DEPARTMENT,
        DepartmentsAPIView.as_view(),
        name=AppConstants.Api.CREATE_DEPARTMENT_NAME,
    ),
]
