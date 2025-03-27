from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=128)
    vehicle_model = models.CharField(max_length=100)
    vehicle_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class ServiceCenter(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='service_centers/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Booking(models.Model):
    service_center = models.ForeignKey(ServiceCenter, on_delete=models.CASCADE)
    car_type = models.CharField(max_length=50)
    service_type = models.CharField(max_length=50)
    selected_date = models.DateField()
    time_slot = models.CharField(max_length=50)

    def __str__(self):
        return f"Booking for {self.service_center.name} on {self.selected_date} at {self.time_slot}"    