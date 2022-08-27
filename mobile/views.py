from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from mobile.models import mobiles
# Create your views here.

class MobileView(APIView):
    def get(self, request, *args, **kwargs):
        all_mobiles=mobiles
        if "display" in request.query_params:
            disp=request.query_params.get("display")
            all_mobiles = [m for m in all_mobiles if (m.get('display')==disp)]
        if "brand" in request.query_params:
            brand = request.query_params.get("brand")
            all_mobiles = [m for m in all_mobiles if (m.get('brand') == brand)]
        return Response({"data":all_mobiles})


    def post(self,request, *args, **kwargs):
        data=request.data
        print(data)
        mobiles.append(data)
        return Response({"msg":"created"})




class MaxMobile(APIView):
    def get(self, request, *args, **kwargs):
        maxmob=max(mobiles,key=lambda mob:mob.get("price"))
        return Response({"maxmob":maxmob})

class MobileDetailsView(APIView):
    def get(self, request, *args, **kwargs):
        id=kwargs.get("mob_id")
        data=[mob for mob in mobiles if mob.get("id")==id].pop()
        return Response({"mobile":data})
    def put(self, request, *args, **kwargs):
        id=kwargs.get("mob_id")
        instanse = [mob for mob in mobiles if mob.get("id")==id].pop()
        data = request.data
        instanse.update(data)
        return Response(instanse)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("mob_id")
        data = [mob for mob in mobiles if mob.get("id") == id].pop()
        mobiles.remove(data)
        return Response({"msg":"mobile removed"})



