from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import BucketlistSerializer,CreatelistSerializer
from .models import Bucketlist,Createlist
import datetime, requests 

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer


class DDetailsView(generics.ListCreateAPIView):
    """This class handles the http GET, PUT and DELETE requests."""   
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    def perform_create(self,serializer):         
        print("NOW HERE")
        # Send Message Device to IoTHub over HTTPS via Rest
        # IoT DeviceID
        deviceID = "myThing886"
        # Iot Hub Name
        IoTHubName = "myGTVIotHub"
        # RestAPI Version
        iotHubAPIVer = "2018-06-30"
        iotHubRestURI = "https://" + IoTHubName + ".azure-devices.net/devices/" + deviceID + "?api-version=" + iotHubAPIVer
        # SAS Token Generated via Azure CLI or Device Explorer
        SASToken = 'SharedAccessSignature sr=myGTVIotHub.azure-devices.net&sig=4gwDPneY4rVqn0ZsAhnk893mrdziBoZ6fHVDV6cmFXk%3D&skn=iothubowner&se=1576001315'

        # Headers
        Headers = {}
        Headers['Authorization'] = SASToken
        Headers['Content-Type'] = "application/json"

        # Message Payload
        body = {} 
        body['deviceid'] = deviceID

        # Send Message
        resp = requests.put(iotHubRestURI, json=body, headers=Headers)
        print(iotHubRestURI)
        print(resp)   

    
    
 

         
        