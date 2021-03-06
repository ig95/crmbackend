from .models import Driver, ScheduledDate, Images, Vehicles, Invoice, managers, VehicleDamages, DeductionType, SupportType 
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
            'Signed',
            'vehicle_name'
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
            'driver_id',
            'vehicle_id',
            'registration',
            'make',
            'model',
            'year',
            'companyOwned',
            'vtype',
            'quotePrice',
            'invoice'
        ]

class VehicleDamagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleDamages
        fields = [
            'VehicleDamages_id',
            'driver_id',
            'vehicle_id',
            'statmentOfDamage',
            'dateOfIncident',
            'picturesOfIncident',
            'quotePrice',
            'invoice'
        ]

class ImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Images
        fields = [
            'driver_id',
            'vehicle_id',
            'image_id',
            'name',
            'countryOfIssue',
            'expiryDate', 
            'dueDate',
            'datePassed',
            'photo',
            'managerApprovedName',
            'managerApprovedDate',
            'imagesLink',
            'verified',
            'driverSigned',
            'points',
            'nextDVLAScreenshot',
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
            'TORH'
            # 'LateWavePayment',
            # 'LVP',
            # 'CRT',
            # 'RL',
            # 'FDDS',
            # 'PHR',
            # 'CALL',
            # 'POD',
            # 'CONS',
            # 'DPMO',
            # 'fuel',
            'support',
            # 'vans',
            'deductions'
        ]



class DeductionTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeductionType
        fields = [  
            'driver_id',
            'deduction',
            'hiVis',
            'keyChain',
            'fuelCard',
            'otherDeduction'
        ]

class SupprtTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SupportType
        fields = [  
            'driver_id',
            'lateWavePayment',
            'additionalSupport',
            'seasonalIncentive',
            'dpmoIncentive',
            'otherSupport'
        ]

 