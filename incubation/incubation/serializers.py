from rest_framework import fields, serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token
from api.models import BookingForm

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']

        extra_kwargs = {'password' : {
            'write_only' : True,
            'required' : True
        }}

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingForm
        fields = '__all__'
    

