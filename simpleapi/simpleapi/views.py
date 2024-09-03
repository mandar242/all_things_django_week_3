from django.http import JsonResponse
from .models import Item
from .serializer import ItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def item_list(request):
    seriializer = ItemSerializer(Item.objects.all(), many=True)
    return JsonResponse(seriializer.data, safe=False)
