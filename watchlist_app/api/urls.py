from django.urls import path, include
from rest_framework.routers import DefaultRouter

from watchlist_app.api.views import ReviewDetail, watch_list, watchlist_detail, \
    ReviewList, ReviewCreate, StreamPlatformVS

router = DefaultRouter()

router.register('stream', StreamPlatformVS, basename='streamplatform')


urlpatterns = [
    path('list/', watch_list, name='watch_list'),
    path('<int:pk>/', watchlist_detail, name='watchlist_detail'),
    path('', include(router.urls)),

    # path('stream/', StreamPlatformAV.as_view(), name='StreamPlatformAV'),
    # path('stream/<int:pk>/', StreamDetailAV.as_view(), name='StreamDetailAV'),

    # path('review/', ReviewList.as_view(), name='ReviewList'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='ReviewDetail'),

    path('<int:pk>/review/', ReviewList.as_view(), name='ReviewList'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='ReviewCreate'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='ReviewDetail'),


]
