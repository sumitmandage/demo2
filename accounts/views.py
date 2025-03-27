from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, ServiceCenter, Booking
from .serializers import UserSerializer, ServiceCenterSerializer, BookingSerializer
from rest_framework import status

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"})
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')
        try:
            user = User.objects.get(phone_number=phone_number, password=password)
            return Response({"message": "Login successful"})
        except User.DoesNotExist:
            return Response({"message": "Invalid credentials"}, status=400)
        
class ServiceCenterView(APIView):
    def get(self, request):
        service_centers = ServiceCenter.objects.all()
        serializer = ServiceCenterSerializer(service_centers, many=True)
        return Response(serializer.data)        
    
class ServiceCenterListView(APIView):
    # GET /api/service-centers/
    def get(self, request):
        service_centers = ServiceCenter.objects.all()
        serializer = ServiceCenterSerializer(service_centers, many=True)
        return Response(serializer.data)

    # POST /api/service-centers/
    def post(self, request):
        serializer = ServiceCenterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceCenterDetailView(APIView):
    # DELETE /api/service-centers/{id}/
    def delete(self, request, pk):
        service_center = get_object_or_404(ServiceCenter, pk=pk)
        service_center.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
    
class BookingListView(APIView):
    # GET /api/bookings/ - Fetch all bookings
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    # POST /api/bookings/ - Create a new booking
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      