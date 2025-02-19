from rest_framework import serializers
from .models import SpyCat, Mission, Target
import requests

class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = '__all__'  #Include all fields of the SpyCat model

    def validate_breed(self, value):
        response = requests.get("https://api.thecatapi.com/v1/breeds")
        if response.status_code == 200:
            valid_breeds = [breed["name"] for breed in response.json()]
            if value not in valid_breeds:
                raise serializers.ValidationError("Invalid breed.")
        return value

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['name', 'country', 'notes', 'is_complete']  #Specify fields for serialization
        read_only_fields = ['is_complete']  #Prevent updates to is_complete

class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)  #Handle multiple targets

    class Meta:
        model = Mission
        fields = ['id', 'spy_cat', 'is_complete', 'targets']

    def create(self, validated_data):
        targets_data = validated_data.pop('targets')  #Extract target data
        mission = Mission.objects.create(**validated_data)  #Create mission instance
        for target_data in targets_data:
            Target.objects.create(mission=mission, **target_data)  #Create associated targets
        return mission  #Return the created mission instance
