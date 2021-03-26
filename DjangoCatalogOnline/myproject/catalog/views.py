from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from catalog.models import Catalog
from catalog.serializers import CatalogSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET','POST'])
def catalog_list(request):
    if request.method == 'GET':
        catalog = Catalog.objects.all()

        name = request.GET.get('name',None)
        if name is not None:
            catalog = catalog.filter(name__icontains=name)

        catalog_serializer = CatalogSerializer(catalog, many=True)
        return JsonResponse(catalog_serializer.data, safe=False)

    elif request.method == 'POST':
        catalog_data = JSONParser().parse(request)
        catalog_serializer = CatalogSerializer(data = catalog_data)
        if catalog_serializer.is_valid():
            catalog_serializer.save()
            return JsonResponse(catalog_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(catalog_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def catalog_detail(request, pk):
    try:
        catalog = Catalog.objects.get(pk=pk)
    except Catalog.DoesNotExist:
        return JsonResponse({'message':'The note does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        catalog_serializer = CatalogSerializer(catalog)
        return JsonResponse(catalog_serializer.data)

    elif request.method == 'PUT':
        catalog_data = JSONParser().parse(request)
        catalog_serializer = CatalogSerializer(catalog, data=catalog_data)
        if catalog_serializer.is_valid():
            catalog_serializer.save()
            return JsonResponse(catalog_serializer.data)
        return JsonResponse(catalog_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        catalog.delete()
        return JsonResponse({'message':'Catalog was deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
