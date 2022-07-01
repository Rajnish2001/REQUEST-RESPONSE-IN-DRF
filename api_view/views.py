from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
# @api_view()
# def index(request):
#     return Response({'msg':'Data is created'})

# @api_view(['POST'])
# def index(request):
#     if request.method == 'POST':
#         print(request.data) # request.data is return the parsed data content of request body.
#         return Response({'msg':'Your Data is POST'})


@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        return Response({'msg':'Your data is Safe'})
    
    if request.method == 'POST':
        print(request.data)
        return Response({'msg':'Your Data is Created','data':request.data})