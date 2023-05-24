from rest_framework import serializers
from watchlist_app.models import WatchList, StreamingPlatform

class WatchListSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()
    class Meta:
        model = WatchList
        fields = "__all__" #Defines all fields in the model
        # fields = ['id', 'name', 'description']
        # exclude = ['active']
        
class StreamingPlatformSerializer(serializers.ModelSerializer):
    # watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.StringRelatedField(many=True) #specifies the string name to be shown
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True) #specifies primarykey only
    watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="watch_detail"
        )#specifies URL only
    
    class Meta:
        model = StreamingPlatform
        fields = "__all__"
        
    
    # def get_len_name(self, object):
    #     length = len(object.name)
    #     return length
    
    
    # def validate(self, data):
    #     if data["name"] == data["description"]:
    #         raise serializers.ValidationError("Title and description should not be the same!")
    #     else:
    #         return data
        
    
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value
    
# def name_length(self, value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")
#     else:
#         return value
        

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validator=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
    
#     def validate(self, data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("Title and description should not be the same!")
#         else:
#             return data
        
    
#     def validate_name(self, value):
        
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short!")
#         else:
#             return value
        