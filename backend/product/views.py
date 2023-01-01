from rest_framework import status
from rest_framework import generics, mixins
from rest_framework import permissions
from rest_framework import authentication
from rest_framework.response import Response

from .models import Product
from . serializers import ProductSerializer
from .permissions import IsStaffProductPermission 

class ProductCreateAPIView(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser,IsStaffProductPermission]

class ProductDetailAPIView(generics.RetrieveAPIView,
                           generics.UpdateAPIView,
                           generics.DestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser,IsStaffProductPermission]
    permission_classes = [IsStaffProductPermission]
    lookup_field = 'pk'


    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
        

