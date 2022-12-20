from django.shortcuts import render
from .serializers import studSerial
from .models import studinfo
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.

@api_view(['GET'])
def getall(request):
    if request.method=='GET':
        stdata=studinfo.objects.all()
        stserial=studSerial(stdata,many=True)
        return Response(stserial.data)

@api_view(['GET'])
def getstid(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    stserial=studSerial(stid)
    return Response(stserial.data)

@api_view(['GET','DELETE'])
def deletestid(request,id):
    try:
        stid=studinfo.objects.get(id=id)
    except studinfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        stserial=studSerial(stid)
        return Response(stserial.data)
    studinfo.delete(stid)
    return Response(status=status.HTTP_202_ACCEPTED)



