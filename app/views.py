from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Person
from .serializers import PersonSerializer

def create_person(request):
    # Handle creating a new person
    if request.method == 'POST':
        data = request.POST
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def get_update_delete_person(request, user_id):
    # Handle reading, updating, or deleting a person
    person = get_object_or_404(Person, pk=user_id)
    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = request.POST
        serializer = PersonSerializer(person, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        person.delete()
        return JsonResponse({'message': 'Person deleted'}, status=204)

def get_person_by_name(request, name):
    persons = Person.objects.filter(name=name)
    if not persons:
        return JsonResponse({'message': 'Person not found'}, status=404)
    serializer = PersonSerializer(persons, many=True)
    return JsonResponse(serializer.data)

# Create your views here.
