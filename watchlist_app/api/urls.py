from django.urls import path, include
# from .views import movie_list, movie_details
from .views import WatchListAV, WatchDetailAV, StreamingPlatformAV
urlpatterns = [
    path('list/',WatchListAV.as_view(), name='watchlist'), 
    path('<int:pk>/', WatchDetailAV.as_view(), name='watch_detail'),
    path('stream/', StreamingPlatformAV.as_view(), name='stream'),
]
