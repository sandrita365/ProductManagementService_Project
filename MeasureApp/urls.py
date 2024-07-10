from django.urls import path

from .constants import AppConstants
from .views import UnitMeasureAPIView

urlpatterns = [
    path(
        AppConstants.Api.QUERY_UNITMEASURE,
        UnitMeasureAPIView.as_view(),
        name=AppConstants.Api.QUERY_UNITMEASURE_NAME,
    ),
    path(
        AppConstants.Api.QUERY_BY_ID_UNITMEASURE,
        UnitMeasureAPIView.as_view(),
        name=AppConstants.Api.QUERY_BY_ID_UNITMEASURE_NAME
    ),
    path(
        AppConstants.Api.CREATE_UNITMEASURE,
        UnitMeasureAPIView.as_view(),
        name=AppConstants.Api.CREATE_UNITMEASURE_NAME
    ),
    path(
        AppConstants.Api.DELETE_UNITMEASURE,
        UnitMeasureAPIView.as_view(),
        name=AppConstants.Api.DELETE_UNITMEASURE_NAME
    ),
    path(
        AppConstants.Api.UPDATE_UNITMEASURE,
        UnitMeasureAPIView.as_view(),
        name=AppConstants.Api.UPDATE_UNITMEASURE_NAME
    )

]
