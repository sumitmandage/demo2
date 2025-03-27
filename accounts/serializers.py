from rest_framework import serializers
from .models import User, ServiceCenter, Booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'phone_number', 'password', 'vehicle_model', 'vehicle_number']
        

class ServiceCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCenter
        fields = ['id', 'name', 'description', 'location', 'phone_number', 'image']   
        
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'service_center', 'car_type', 'service_type', 'selected_date', 'time_slot']                    