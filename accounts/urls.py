from django.urls import path
from .views import RegisterView, LoginView, ServiceCenterListView, ServiceCenterDetailView, BookingListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Register endpoint
    path('login/', LoginView.as_view(), name='login'),
    path('service-centers/', ServiceCenterListView.as_view(), name='service-center-list'),
    path('service-centers/<int:pk>/', ServiceCenterDetailView.as_view(), name='service-center-detail'),
    path('bookings/', BookingListView.as_view(), name='booking-list'),
]