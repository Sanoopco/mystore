from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import math
# Create your views here.

class MyViews(APIView):
  def get(self,request,*args,**kwargs):
    return Response({"msg":"hello world"})


class GoodMornnigView(APIView):
  def get(self, request, *args, **kwargs):
    return Response({"msg":"good morning"})


class WakeUpView(APIView):
  def get(self, request, *args, **kwargs):
    return Response({"msg":"wake up its morning already"})

class GoToWorkView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"msg":"its morning go to work "})


class AddView(APIView):
  def post(self, request, *args, **kwargs):
      num1=int(request.data.get("num1"))
      num2=int(request.data.get("num2"))
      res=num1+num2
      return Response({"sum":res})


class SubtractionView(APIView):
    def post(self, request, *args, **kwargs):
        n1=int(request.data.get("num1"))
        n2 = int(request.data.get("num2"))
        if (n1<n2):
            n1,n2=n2,n1
            sub = n1-n2
            return Response({"substraction":sub})



class MultiplicationView(APIView):
    def post(self, request, *args, **kwargs):
        n1 = int(request.data.get("num1"))
        n2 = int(request.data.get("num2"))
        mul = n1*n2
        return Response({"multiplication":mul})



class PrimeNoCheckView(APIView):
    def post(self, request, *args, **kwargs):
        num=int(request.data.get("num"))
        flag=0
        for i in range(2,num):
            if (num%i==0):
                flag=1
                break
        if flag==1:
            return Response({"result":"is not a prime number"})
        else:
            return Response({"result":"is a prime number"})


class FacorialView(APIView):
    def post(self, request, *args, **kwargs):
        num=int(request.data.get("num"))
        # fact = math.factorial(num)
        # return Response({"factorial:":fact})
        fact=1
        for i in range(1,num+1):
            fact=fact*i
        return Response({"factorial":fact})


class MultipleOfTWO(APIView):
    def post(self, request, *args, **kwargs):
        num=int(request.data.get("num"))
        if (num%2==0):
            return Response({"result":"its a multiple of 2"})











