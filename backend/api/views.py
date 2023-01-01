import json
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from product.models import Product
from product.serializers import ProductSerializer



@api_view(['POST'])
def myresponse(request, *args, **kwargs):

    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):

        instance = serializer.save()
        print(instance)

        return Response(serializer.data)

    return Response({
        'message':'Invalid Data'
    }, status=status.HTTP_400_BAD_REQUEST)


