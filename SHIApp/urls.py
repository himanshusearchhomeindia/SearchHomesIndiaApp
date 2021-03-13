from django.urls import path #we use path to make the urls endpoints.
from .views import (home, PropertyListing, PropertyView, IndividualProp, advfilt_properties, about,
                      blog, faq, testimonials, terms, loan_calculator, contact_us, carriers, ContactData, CarrierData, PropertyContactData, ExclusiveProperty, SmartSearch, TimeLine, compare_property, compare, HotPropertyView, HotIndividualProp) #these are the view function's that we are using to perform the operations.


urlpatterns = [
    path('', home, name='home'), #this will show the homepage of the website.
    path('propertylist/', PropertyListing, name='PropertyListing'), #this will show the property listing page.
    path('exclusiveproperty/<str:Tag>', ExclusiveProperty, name='ExclusiveProperty'), #this will show the exclusive property page.
    path('properties/', PropertyView, name='PropertyView'), #This is the API call url(coming from index.js file) from where the user will get the filtered properties based on his query.
    path('hotproperties/', HotPropertyView, name='HotPropertyView'), #This is the API call url(coming from HotPropertyindex.js file) from where the user will get the Hot properties in the home page.
    path('HotProperty/<str:name>/<str:loc>', HotIndividualProp, name='HotIndividualProp'), #This is the end point from where the user will get the individual Hotproperty details.
    path('<str:name>/<str:loc>', IndividualProp, name='IndividualProp'), #This is the end point from where the user will get the individual property details.
    # path('adv_filter/', adv_Filter, name='adv_Filter'), #This will show the advance property listing page.(prashant) 
    path('advfilt_properties/', advfilt_properties, name='advfilt_properties'), #This will show the selected advance property listing page.(prashant) 
    path('about/', about , name='about'),  #this will show the about us page (prashant). 
    # path('gallery/', gallery , name='gallery'),  #this will show the gallery page (prashant). 
    path('blog/', blog , name='blog'),  #this will show the blog page (prashant).
    path('faq/', faq , name='faq'),  #this will show the faq page (prashant).
    path('testimonials/', testimonials , name='testimonials'),  #this will show the testimonials page (prashant). 
    path('terms/', terms , name='terms'),  #this will show the terms and conditions page (prashant).
    path('loan_calculator/', loan_calculator , name='loan_calculator'),  #this will show loan_calculator page (prashant). 
    path('contact_us/', contact_us , name='contact_us'),  #this will show the contactus page. 
    path('carriers/', carriers , name='carriers'),  #this will show the carriers page.
    path('contactdata/', ContactData, name='contactdata'), #This url will work for the ContactData API to get the details of the user and store it in the database.
    path('carrierdata/', CarrierData, name='carrierdata'), #This will work for the Carrier Data Api to store the details of the user and store it into Database. 
    path('propertycontactdata/', PropertyContactData, name='propertycontactdata'), #This url will work for the ContactData with property name, API to get the details of the user and store it in the database.
    path('smartsearch/', SmartSearch, name='smartsearch'), #This url will show the SmartSearch page by using SmartSearch function from views.py file.
    path('timeline/', TimeLine, name='timeline'), #This url will show the timeline page by using TimeLine function from views.py file.
    path('compare_property/', compare_property , name='compare_property'),  #this will show the compare property page 
    path('compare/', compare , name='compare'),  #this will show the compare page 
]