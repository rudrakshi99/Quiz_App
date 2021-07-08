from rest_framework import serializers
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email','firstname', 'lastname','password']

        # make password field
        extra_kwargs = {
            'password' : {
                # make password write only
                'write_only' : True,
                # set input style password
                'style' : {'input_type' : 'password'}
            }
        }

    def create(self, validated_data):

        retailer = User.objects.create_user(
            **validated_data
        )

        return retailer

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data) 
