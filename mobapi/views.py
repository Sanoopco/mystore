from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from mobapi.serializers import MobileSerializer,MobileModelSeializer
from mobapi.models import Mobiles

# Create your views here.

class MobileView(APIView):
    def get(self, request, *args, **kwargs):
        qs=Mobiles.objects.all()
        if "band" in request.query_params:
            qs=qs.filter(band=request.query_params.get("band"))
        if "price" in request.query_params:
            qs=qs.filter(price__gte=request.query_params.get("price"))
        serializer=MobileSerializer(qs,many=True)
        return Response(data=serializer.data)
    def post(self, request, *args, **kwargs):
        serializer=MobileSerializer(data=request.data)
        if serializer.is_valid():
            Mobiles.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.data)

class MobileDetailView(APIView):
    def get(self, request, *args, **kwargs):
        id=kwargs.get("mob_id")
        qs=Mobiles.objects.get(id=id)
        serializer=MobileSerializer(qs,many=False)
        return Response(data=serializer.data)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("mob_id")
        mobile=Mobiles.objects.get(id=id)
        mobile.delete()
        return Response({"msg":"deleted"})
    def put(self, request, *args, **kwargs):
        id=kwargs.get("mob_id")
        qs = Mobiles.objects.filter(id=id)
        serializer=MobileSerializer(instance=qs,data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            qs.update(**serializer.validated_data)
            # qs.name=serializer.validated_data.get("name")
            # qs.brand = serializer.validated_data.get("brand")
            # qs.band = serializer.validated_data.get("band")
            # qs.display = serializer.validated_data.get("display")
            # qs.price = serializer.validated_data.get("price")
            # qs.rating = serializer.validated_data.get("rating")
            # qs.save()
            return Response(data="updated")
        else:
            return Response(data=serializer.errors)

class MobileModelView(APIView):
    def get(self, request, *args, **kwargs):
        qs=Mobiles.objects.all()
        serializer = MobileModelSeializer(qs,many=True)
        return Response(data=serializer.data)
    def post(self, request, *args, **kwargs):
        serializer = MobileModelSeializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
class MobileDetailModelView(APIView):
    def get(self, request, *args, **kwargs):
        id=kwargs.get("mob_id")
        qs = Mobiles.objects.get(id=id)
        serializer=MobileModelSeializer(qs)
        return Response(data=serializer.data)
    def put(self, request, *args, **kwargs):
        id = kwargs.get("mob_id")
        mobile = Mobiles.objects.get(id=id)
        serializer = MobileModelSeializer(instance=mobile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def delete(self, request, *args, **kwargs):
        id = kwargs.get("mob_id")
        qs = Mobiles.objects.get(id=id)
        qs.delete()
        return Response(data="successfuly deleted")

