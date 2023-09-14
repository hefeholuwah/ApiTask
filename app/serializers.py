from rest_framework import serializers
from .models import Person  # Import your Person model or the relevant model

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'age']  # Or specify the fields you want to include/exclude
