from fcm.models import FcmNotification, FcmTokenModel
from rest_framework import serializers


class FcmNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FcmNotification
        fields = [
            'id',
            'user',
            'title',
            'body',
            'data',
            "to_user",
            'created_at',
            'updated_at'    
        ]
        read_only_fields = ('created_at', 'updated_at', 'id') 
        extra_kwargs = {
            'title': {'required': True},
            'body': {'required': True},
            'data': {'required': True},
            "to_user": {'required': True}
        }  

    def validate(self, data):
        # Custom validation logic
        if not data.get('title'):
            raise serializers.ValidationError({"title": "This field is required."})
        if not data.get('body'):
            raise serializers.ValidationError({"body": "This field is required."})
        if not data.get('data'):
            raise serializers.ValidationError({"data": "This field is required."})
        if not data.get('to_user'):
            raise serializers.ValidationError({"to_user": "This field is required."})
        
        # Return the validated data
        return data 



class FcmTokenModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FcmTokenModel
        fields = [
           
            'user',
            'fcm_token',
            'time_stamp',   
            'is_stale',
            'stale_time',
       
        ]
        read_only_fields = ('time_stamp', 'stale_time', )
        extra_kwargs = {

            'fcm_token': {'required': True},
            'stale_time': {'required': True},
            'time_stamp': {'required': False},
            'is_stale': {'required': False} 
     }
#
        
        
   