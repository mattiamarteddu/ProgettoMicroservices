from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer
# Create your views here.
from django.http import HttpResponse


## TEST KAFKA ##
from kafka import KafkaProducer
from kafka import KafkaConsumer





def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class CustomerList(APIView):
    def get(self, request):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

class CustomerGet(APIView):
    def get(self, request, customer_id):
        queryset = Customer.objects.filter(id=customer_id)
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

class CustomerCreate(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerUpdate(UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDelete(DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer