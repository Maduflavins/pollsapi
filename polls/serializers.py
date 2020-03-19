from rest_framework import serializers

from .models import Poll, Choice, Vote

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
    
    