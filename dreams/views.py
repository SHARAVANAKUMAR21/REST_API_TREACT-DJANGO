from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Dream
from .serializers import DreamSerializer, DreamUpdateSerializer

@api_view(['GET'])

def view_dream(request):
    if request.method == 'GET':
        dreams = Dream.objects.all()
        serializer = DreamSerializer(dreams, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def add_dream(request):
    if request.method == 'POST':
        serializer = DreamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_dream(request, dream_id):
    try:
        dream = Dream.objects.get(id=dream_id)
    except Dream.DoesNotExist:
        return Response({'error': 'Dream not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        dream.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])

def update_dream(request, dream_id):
    try:
        dream = Dream.objects.get(id=dream_id)
    except Dream.DoesNotExist:
        return Response({'error': 'Dream not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = DreamSerializer(dream, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)