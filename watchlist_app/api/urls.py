from django.urls import path, include
from .views import WatchListAV, WatchDetailAV, StreamingPlatformAV, StreamDetailAV, ReviewList, ReviewDetail
urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watchlist'), 
    path('list/<int:pk>/', WatchDetailAV.as_view(), name='watch_detail'),
    path('stream/', StreamingPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>/', StreamDetailAV.as_view(), name='stream_detail'),
    
    path('stream/1/review/', StreamDetailAV.as_view(), name='stream_details'),
    path('review/', ReviewList.as_view(), name='review_list'),
    path('stream/1/review/<int:pk>/', ReviewDetail.as_view(), name='review_detail'),

    
    
]
