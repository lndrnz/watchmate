from django.urls import path, include
from .views import WatchListAV, WatchDetailAV, StreamingPlatformAV, StreamDetailAV, ReviewList
urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watchlist'), 
    path('list/<int:pk>/', WatchDetailAV.as_view(), name='watch_detail'),
    path('stream/', StreamingPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>/', StreamDetailAV.as_view(), name='stream_detail'),
    path('review', ReviewList.as_view(), name='review_list',
         
         )
    
    
]
