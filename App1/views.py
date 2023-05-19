from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializers
from .models import Product,Product1


# Create your views here.

@api_view(['GET'])
def App1overview(request):
    app_urls = {
        'To show all the Products from db (in table format)--->':'/list',
        'To show all the Products from DB in JSON format ---->':'/list1',
        'To see only one Product(json format)-->': '/detail/<int:id>    ex:/deatil/2',
        'want to create new Product details(json format) as input': '/create/',
        'if you want update specific record(json format)': '/update/<int:id>    ex:/update/3',
        'if you want delete specific record--->': '/delete/<int:id>  ex:/delete/3',
    }

    return Response(app_urls)


@api_view(['GET'])
def showall(request):
    products = Product1.objects.all()
    serializer = ProductSerializers(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def showall1(request):
    products = Product1.objects.all()
    return render(request, "index.html", {'Product': products})


@api_view(['GET'])
def ViewProduct(request, pk):
    products = Product1.objects.get(id=pk)
    serializer = ProductSerializers(products, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateProduct(request):
    serializer = ProductSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateProduct(request, pk):
    products = Product1.objects.get(id=pk)
    serializer = ProductSerializers(instance=products, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def deleteProduct(request, pk):
    products = Product1.objects.get(id=pk)
    products.delete()

    return Response('Items deleted Successfully')
