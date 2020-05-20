from .models import Driver, ScheduledDate, Images, TrainingDate, Vehicles, Invoice, managers
from rest_framework import serializers


class managersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = managers
        fields = [
            'user_id',
            'email',
            'name',
            'station',
            'creationDate'
        ]        
  
class DriverSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta:
        model = Driver
        fields =[
            'driver_id',
            'name',
            'location',
            'email',
            'phone',
            'address',
            'datesList',
            'status',
            'DriverUniqueId',
            'SigningUrlNumber',
            'Signed'
        ]
        
class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = [
            'invoice_id',
            'driver_id',
            'day',
            'routeType',
            'LWP',
            'LVP',
            'SUP',
            'deductions',
            'fuel'
        ]


class VehiclesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicles
        fields = [
            'Vehicle_id',
            'VehiclesRegistration',
            'VehiclesDVLANumber',
            'VehicleOwned',
            'driver_id'
        ]


       

class ImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Images
        fields = [
            'image_id',
            'ImagesLink',
            'Verified',
            'ImageName',
            'driver_id',
            'ManagerSigned',
            'DriverSigned',
            'ExpiryDate', 
            'SignitureToken',
            'SignitureManagerEmail',
            'Points',
            'NextDVLAScreenshot',
            'LicenseOrigin'
        ]

class ScheduledDatesSerializer(serializers.HyperlinkedModelSerializer):  
    logIn_time = serializers.TimeField(input_formats= ['%H:%M'])
    logOut_time = serializers.TimeField(input_formats= ['%H:%M'])  
    class Meta:
        model = ScheduledDate
        fields = [
            'date_id',
            'name',
            'inOff',
            'route',
            'routeNumber',
            'logIn_time',
            'logOut_time',   
            'location',
            'date',
            'driver_id',
            'mileage',
            'start_mileage',
            'finish_mileage',
            'parcel',
            'parcelNotDelivered',
            'TORH',
            'LateWavePayment',
            'LVP',
            'CRT',
            'RL',
            'FDDS',
            'PHR',
            'CALL',
            'POD',
            'CONS',
            'DPMO',
            'fuel',
            'support',
            'vans',
            'deductions'
        ]




class TrainingDateSerializer(serializers.HyperlinkedModelSerializer):  
    class Meta:
        model = TrainingDate
        fields = [
            'date_id',
            'name',
            'location',
            'date',
            'driver_id',
            'CRT',
            'RL',
            'deductions',
            'support'
        ]


