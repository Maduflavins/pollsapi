from rest_framework import serializers

from .models import Poll, Choice, Vote
from django.contrib.auth.models import User




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        
    
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


#create serializer class for vote
class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'
        

#Create serializer class for choice
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
    
    


class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)
    
    class Meta:
        model = Poll
        fields = '__all__'
    
    