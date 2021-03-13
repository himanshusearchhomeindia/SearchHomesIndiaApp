from django.contrib import admin
from .models import (Amenities, Builder, PropertyList, PropertyImages, UserContactData, UserResumeData, PropertyContact, HotPropertyList, HotPropertyImages) #Importing the models from models.py file to register in the admin panel of django.

# Register your models here.
admin.site.register(Amenities)  #Amenities model.
admin.site.register(Builder)  #Builder model.
admin.site.register(PropertyList)  #Property model.
admin.site.register(HotPropertyList)  #HotProperty model.
admin.site.register(HotPropertyImages) #Multiple Hotproperty images model.
admin.site.register(PropertyImages) #Multiple property images model.
admin.site.register(UserContactData) #User contact form model.
admin.site.register(UserResumeData)  #user resume from model.
admin.site.register(PropertyContact) #user  + property data model.
