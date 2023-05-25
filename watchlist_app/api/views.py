from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from watchlist_app.models import WatchList, StreamingPlatform, Review
from .serializers import WatchListSerializer, StreamingPlatformSerializer, ReviewSerializer


class WatchListAV(APIView):
    
    def get(self, request):
        watchlist = WatchList.objects.all()
        serializer = WatchListSerializer(watchlist, many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
class WatchDetailAV(APIView):
    
    def get(self, request, pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"Error": "Watchlist not found"}, status=status.HTTP_404_NOT_FOUND)
    
        serializer = WatchListSerializer(watchlist)
        return Response(serializer.data)
    
    
    def put(self,request, pk):
        watchlist = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer( watchlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def delete(self,request, pk):
        watchlist = WatchList.objects.get(pk=pk)
        watchlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class StreamingPlatformAV(APIView):
    def get(self, request):
        stream = StreamingPlatform.objects.all()
        serializer = StreamingPlatformSerializer(stream, many=True) #Need to add context={'request': request} for URLSerializer
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = StreamingPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamDetailAV(APIView):
    
    def get(self, request, pk):
        try:
            stream = StreamingPlatform.objects.get(pk=pk)
        except StreamingPlatform.DoesNotExist:
            return Response({"Error": "Streaming Platform not found"}, status=status.HTTP_404_NOT_FOUND)
    
        serializer = StreamingPlatformSerializer(stream)
        return Response(serializer.data)
    
    
    def put(self,request, pk):
        stream = StreamingPlatform.objects.get(pk=pk)
        serializer = StreamingPlatformSerializer(stream, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def delete(self,request, pk):
        stream = StreamingPlatform.objects.get(pk=pk)
        stream.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        
        
# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':  
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET','PUT','DELETE'])
# def movie_details(request, pk):
#     if request.method == "GET":
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({"Error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
    
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method == "PUT":
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer( movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == "DELETE":
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

            
