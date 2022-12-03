import json
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict


from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializer



@api_view(['GET'])
def myresponse(request, *args, **kwargs):

    model_data = Product.objects.all().order_by('?').first()


    serializer = ProductSerializer(model_data)


    


    return Response(serializer.data)

    return JsonResponse(
        data
    )

