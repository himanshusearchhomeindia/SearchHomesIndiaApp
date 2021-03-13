from django.shortcuts import render, HttpResponse
from rest_framework import serializers  # This is used to render the pages and return the json response.
from .serializers import PropertyListSerializer, HotPropertyListSerializer  # This is used to get the PropertyListSerializer class to convert it into python obj to json obj.
from .models import (PropertyList, PropertyImages, UserContactData, PropertyImages, Amenities, Builder, UserResumeData, PropertyContact, HotPropertyList, HotPropertyImages) # these are the models that we will be using for filteration, storing the data into the database.
from rest_framework.response import Response # this is used to send the response into the API request.
from rest_framework.decorators import api_view # we are using the function based views in RESTapi for this we need this decorator class.
from django.http import JsonResponse #this is used in compare property page to send the json response to the API call.
import json #imported the json to work with the HttpResponse for contact related queries.

# Create your views here.
def home(request):
    """
    This will return the home page once the user open the website with url("") its empty but in server it will come like(searchhomesindia.com).
    """
    return render(request, 'index.html')


def about(request):
    """
    This will return the about us page once the user click on the About us navigation option.
    """
    return render(request,'about.html')


# def gallery(request):
#     """
#     This will return the gallery page.
#     """
#     return render(request, 'gallery.html')

def blog(request):
    """
    This will return the blog page.
    """
    PropImages = PropertyList.objects.all()   #Filter all the Property List objects and insert into PropImages variable.


    return render(request, 'blog.html', {'featured_images':PropImages})

def faq(request):
    """
    This will return the faq page.
    """
    return render(request, 'faq.html')

def testimonials(request):
    """
    This will return the testimonials page.
    """
    return render(request, 'testimonials.html')
    
def terms(request):
    """
    This will return the terms page.
    """
    return render(request, 'terms.html')

def loan_calculator(request):
    """
    This will return the loan calculator page.
    """
    return render(request, 'loan_calculator.html')

def contact_us(request):
    """
    This will return the contact us page.
    """
    return render(request, 'contact_us.html')

def ContactData(request):
    """
    This function will handle the data coming from the contact page and store it in the database.
    """
    if request.method == 'POST':  #if request is post it will fetch the details from the frontend and store them into the backend.
        try:
            #it will try to do the operation if it fails the except block will get executed.
            success = True #setting the variable as true and if everything went right it will get send to the frontend as response to show the success alert message in the contact form.

            Data = json.loads(request.body.decode(
                "utf-8"))  #loading the json from the fetch API request.
            Name = Data['Name']  #user name.
            Email = Data['Email']  #user email.
            Phone = Data['Phone']  #user phone number.
            Message = Data['Message']  #user message.
            if (Name and Email and Phone and Message != 0):
                #when all the values will have the data then only it will store the data into the database.
                userData = UserContactData(
                    name=Name, email=Email, phone=Phone,
                    message=Message)  #creatig a variable and passing the values into the database fields.
                userData.save()  #saving the data into database.
                params = {
                    'success': success
                }  #making a dictionary for converting it into json.(it will get sent to the frontend as success message).
                successData = json.dumps(
                    params)  #converting dictionary into json.
                return HttpResponse(successData)  #sending the reply in the json format.
            else:
                #if any one of the value will be empty it will send the error as a response.
                success = False #converting the value into false to show the error message in the front end.
            params = {
                'success': success
            }  #making a dictionary for converting it into json.
            successData = json.dumps(params)  #converting dictionary into json.
            return HttpResponse(successData)  #sending the reply.
        except Exception:
            #if any error happens it will send the error response to the frontend.
            success = False  #converting the value into false to show the error message in the front end.
            params = {
                'success': success
            }  #making a dictionary for converting it into json.
            successData = json.dumps(params)  #converting dictionary into json.
            return HttpResponse(successData)  #sending the reply in the json format.


def CarrierData(request):
    """
    This function will handle the data coming from the carrier page.
    """
    if request.method == 'POST':  #if request is post it will fetch the details from the frontend and store them into the backend.
        try:
            #it will try to do the operation if it fails the except block will get executed.
            success = True #setting the variable as true and if everything went right it will get send to the frontend as response to show the success alert message in the carrier form.
            Data = json.loads(request.body.decode(
                "utf-8"))  #loading the json from the fetch API request.
            Name = Data['Name']  #user name.
            Email = Data['Email']  #user email.
            Phone = Data['Phone']  #user phone number.
            Vacancy = Data['Vacancy'] #Vacancy details.
            Message = Data['Message']  #user message.
            if (Name and Email and Phone and Message and Vacancy != 0):
                #when all the values will have the data then only it will store the data into the database.
                resumeData = UserResumeData(
                    name=Name, email=Email, phone=Phone,
                    message=Message, vacancy=Vacancy) #creatig a variable and passing the values into the database fields.
                resumeData.save()  #saving the data into database.
                params = {
                    'success': success
                }  #making a dictionary for converting it into json.(it will get sent to the frontend as success message).
                successData = json.dumps(
                    params)  #converting dictionary into json.
                return HttpResponse(successData)  #sending the reply.
            else:
                #if any one of the value will be empty it will send the error as a response.
                success = False  #converting the value into false to show the error message in the front end.
            params = {
                'success': success
            }  #making a dictionary for converting it into json.
            successData = json.dumps(params)  #converting dictionary into json.
            return HttpResponse(successData)  #sending the reply.
        except Exception:
            #if any error happens it will send the error response to the frontend.
            success = False  #converting the value into false to show the error message in the front end.
            params = {
                'success': success
            }  #making a dictionary for converting it into json.
            successData = json.dumps(params)  #converting dictionary into json.
            return HttpResponse(successData)  #sending the reply.


def carriers(request):
    """
    This will return the carriers page.
    """
    return render(request, 'carriers.html')


def PropertyListing(request):
    """
    This page will show the property listing page to the user.
    """
    return render(request, 'listing.html')

def SmartSearch(request):
    """
    This page will show the smartsearch page to the user.
    """
    return render(request, 'smartsearch.html')

def TimeLine(request):
    """
    This page will show the TimeLine page to the user.
    """
    return render(request, 'timelinenew.html')


@api_view(['POST'])  # decorator with POST request permission we will use this when working with REST API for the general search.
def PropertyView(request):
    try:
        """
        This function will access the SearchQuery + BuilderQuery + PropertyTypeQuery + SubPropertyTypeQuery + LocationQuery from the API request and do the filteration with the database and in the end return the response.
        """

        SearchQuery = request.data['SearchQuery']  # accessing the searchquery form the API request.
        
        BuilderQuery = request.data['BuilderQuery']  # accessing the builderquery form the API request.

        PropertyTypeQuery = request.data['PropertyTypeQuery'] # accessing the PropertyTypeQuery form the API request.

        SubPropertyTypeQuery = request.data['SubPropertyTypeQuery'] # accessing the SubPropertyTypeQuery form the API request.

        LocationQuery = request.data['LocationQuery'] # accessing the LocationQuery form the API request.
        


        if SearchQuery != 0 and "Select+Builder" not in BuilderQuery and "Select+Location" not in LocationQuery and "Select+Property+Type" not in PropertyTypeQuery and "Select+Sub+Property+Type" not in SubPropertyTypeQuery:
            #This block will get execute when searchquery and builder and location and propertytype and subproptype.
            print("1")
            SearchName = 0 #creating a variable for storing the filtered properties based on the searchName
            
            if "+" in SearchQuery:
                #If there is space present in the SearchQuery then this block will replace the query by removing the + sign to space.
                SearchName = SearchQuery.replace("+", " ") # replacing the SearchQuery + sign with space to get the exact query.
                
                BuilderQuery = BuilderQuery.replace("+", " ") # replacing the BuilderQuery + sign with space to get the exact query.
                
                builder = Builder.objects.get(BuilderName = BuilderQuery) #fetching the buildername from (models.py -> Builder model) for using in it the PropertyFiltered.
                
                PropertyFiltered = PropertyList.objects.filter(Location__icontains=LocationQuery, Property_Type__icontains=PropertyTypeQuery, SubPropType__icontains=SubPropertyTypeQuery,PropertyName__icontains=SearchName, BuilderName=builder)#Here we are filtering the data with (PropertyName, Property_Type, Location,SubPropertyType, BuilderName) from (models.py) by using the PropertyList model. 
                
                FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            
            elif "+" not in SearchQuery:
                #else, if there is no space present then it will send the search query into the SearchName field to get the results.
                
                SearchName = SearchQuery #here the SearchQuery will get saved when there is no space(+) is present in the query.
                
                BuilderQuery = BuilderQuery.replace("+", " ") # replacing the BuilderQuery + sign with space to get the exact query.
                
                builder = Builder.objects.get(BuilderName = BuilderQuery) #filtering the builder name by using the BuilderQuery to check whether the builder is present in the database from (models.py -> Builder model).

                PropertyFiltered = PropertyList.objects.filter(Location__icontains=LocationQuery, Property_Type__icontains=PropertyTypeQuery, SubPropType__icontains=SubPropertyTypeQuery,SearchName__icontains=SearchName, BuilderName=builder)#Here we are filtering the data with (PropertyName, Property_Type, Location,SubPropertyType, BuilderName) from (models.py) by using the PropertyList model.
                
                FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.

            if len(FinalResult) != 0:
                #if there is data present in the FinalResults then it will get sent to the API call as result.
                # serializing the data into json format.
                serializer = PropertyListSerializer(FinalResult, many=True)
                # sending the results back to the API request.
                return Response(serializer.data)
            else:
                #if there is no-data present in the FinalResults then it will send 0 as a response to the API call for showing the "no results found" block.
                FinalResult = 0
                # sending the results back to the API request.
                return Response(FinalResult)

        elif "Select+Builder" not in BuilderQuery and "Select+Location" not in LocationQuery and "Select+Property+Type" not in PropertyTypeQuery and "Select+Sub+Property+Type" not in SubPropertyTypeQuery and SearchQuery == 0:
            #This block will execute when Builder and Location and PropertyType and SubPropertyType will present and search query will be empty.
            print("2")

            #It will check whether the BuilderQuery is empty or not if it is not empty then this block will get executed and the BuilderQuery (+) will get replaced with (" ") to get the exact builder name.
            
            BuilderQuery = BuilderQuery.replace("+", " ") # replacing the BuilderQuery + sign with space to get the exact query.
            
            builder = Builder.objects.get(BuilderName = BuilderQuery) #filtering the builder name by using the BuilderQuery to check whether the builder is present in the database from (models.py -> Builder model).
            
            PropertyFiltered = PropertyList.objects.filter(BuilderName=builder, Location__icontains=LocationQuery, Property_Type__icontains=PropertyTypeQuery, SubPropType__icontains=SubPropertyTypeQuery)#Here we are filtering the data with (BuilderName) from (models.py) by using the PropertyList model.
            
            FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.

            serializer = PropertyListSerializer(FinalResult, many=True)
                # sending the results back to the API request.
            
            return Response(serializer.data)
        
        elif "Select+Location" not in LocationQuery and "Select+Property+Type" not in PropertyTypeQuery and "Select+Sub+Property+Type" not in SubPropertyTypeQuery and SearchQuery == 0:
            #This block will execute when Location and PropertyType and SubPropertyType will present and search query will be empty.
            print("3")

            #It will check whether the BuilderQuery is empty or not if it is not empty then this block will get executed and the BuilderQuery (+) will get replaced with (" ") to get the exact builder name.
            PropertyFiltered = PropertyList.objects.filter(Location__icontains=LocationQuery, Property_Type__icontains=PropertyTypeQuery, SubPropType__icontains=SubPropertyTypeQuery)#Here we are filtering the data with (BuilderName) from (models.py) by using the PropertyList model.
            
            FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            serializer = PropertyListSerializer(FinalResult, many=True)
                # sending the results back to the API request.
            
            return Response(serializer.data)
        
        elif "Select+Property+Type" not in PropertyTypeQuery and "Select+Sub+Property+Type" not in SubPropertyTypeQuery  and SearchQuery == 0:
            #This block will execute when PropertyType and SubPropertyType will present and search query will be empty.
            print("4")
            #It will check whether the BuilderQuery is empty or not if it is not empty then this block will get executed and the BuilderQuery (+) will get replaced with (" ") to get the exact builder name.
            
            PropertyFiltered = PropertyList.objects.filter(Property_Type__icontains=PropertyTypeQuery, SubPropType__icontains=SubPropertyTypeQuery)#Here we are filtering the data with (BuilderName) from (models.py) by using the PropertyList model.
            
            FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            serializer = PropertyListSerializer(FinalResult, many=True)
                # sending the results back to the API request.

            return Response(serializer.data)
        
        elif "Select+Builder" not in BuilderQuery and "Select+Location" not in LocationQuery and "Select+Property+Type" not in PropertyTypeQuery  and SearchQuery == 0:
            #This block will execute when Builder and Location and PropertyType and SubPropertyType will present and search query will be empty.
            print("5")
            #It will check whether the BuilderQuery is empty or not if it is not empty then this block will get executed and the BuilderQuery (+) will get replaced with (" ") to get the exact builder name.
            
            BuilderQuery = BuilderQuery.replace("+", " ") # replacing the BuilderQuery + sign with space to get the exact query.
            
            builder = Builder.objects.get(BuilderName = BuilderQuery) #filtering the builder name by using the BuilderQuery to check whether the builder is present in the database from (models.py -> Builder model).
            
            PropertyFiltered = PropertyList.objects.filter(BuilderName=builder, Location__icontains=LocationQuery, Property_Type__icontains=PropertyTypeQuery)#Here we are filtering the data with (BuilderName) from (models.py) by using the PropertyList model.
            
            FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            serializer = PropertyListSerializer(FinalResult, many=True)
                # sending the results back to the API request.
            
            return Response(serializer.data)
        
        elif "Select+Builder" not in BuilderQuery and "Select+Property+Type" not in PropertyTypeQuery  and SearchQuery == 0:
            #This block will execute when Builder and SubPropertyType will present and search query will be empty.
            print("6")
            #It will check whether the BuilderQuery is empty or not if it is not empty then this block will get executed and the BuilderQuery (+) will get replaced with (" ") to get the exact builder name.
            
            BuilderQuery = BuilderQuery.replace("+", " ") # replacing the BuilderQuery + sign with space to get the exact query.
            
            builder = Builder.objects.get(BuilderName = BuilderQuery) #filtering the builder name by using the BuilderQuery to check whether the builder is present in the database from (models.py -> Builder model).
            
            PropertyFiltered = PropertyList.objects.filter(BuilderName=builder, Property_Type__icontains=PropertyTypeQuery)#Here we are filtering the data with (BuilderName) from (models.py) by using the PropertyList model.
            
            FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            serializer = PropertyListSerializer(FinalResult, many=True)
                # sending the results back to the API request.
            
            return Response(serializer.data)
        
        elif "Select+Builder" not in BuilderQuery and "Select+Sub+Property+Type" not in SubPropertyTypeQuery  and SearchQuery == 0:
            #This block will execute when Builder and SubPropertyType will present and search query will be empty.
            print("7")
            #It will check whether the BuilderQuery is empty or not if it is not empty then this block will get executed and the BuilderQuery (+) will get replaced with (" ") to get the exact builder name.
            
            BuilderQuery = BuilderQuery.replace("+", " ") # replacing the BuilderQuery + sign with space to get the exact query.
            
            builder = Builder.objects.get(BuilderName = BuilderQuery) #filtering the builder name by using the BuilderQuery to check whether the builder is present in the database from (models.py -> Builder model).
            
            PropertyFiltered = PropertyList.objects.filter(BuilderName=builder, SubPropType__icontains=SubPropertyTypeQuery)#Here we are filtering the data with (BuilderName) from (models.py) by using the PropertyList model.
            
            FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            serializer = PropertyListSerializer(FinalResult, many=True)
                # sending the results back to the API request.
            
            return Response(serializer.data)
        
        elif "Select+Builder" not in BuilderQuery and "Select+Location" not in LocationQuery and SearchQuery == 0:
            #This block will execute when Builder and Location and PropertyType will present and search query will be empty.
            print("8")
            #It will check whether the BuilderQuery is empty or not if it is not empty then this block will get executed and the BuilderQuery (+) will get replaced with (" ") to get the exact builder name.
            
            BuilderQuery = BuilderQuery.replace("+", " ") # replacing the BuilderQuery + sign with space to get the exact query.
            
            builder = Builder.objects.get(BuilderName = BuilderQuery) #filtering the builder name by using the BuilderQuery to check whether the builder is present in the database from (models.py -> Builder model).
            
            PropertyFiltered = PropertyList.objects.filter(BuilderName=builder, Location__icontains=LocationQuery)#Here we are filtering the data with (BuilderName) from (models.py) by using the PropertyList model.
            
            FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            serializer = PropertyListSerializer(FinalResult, many=True)
                # sending the results back to the API request.

            return Response(serializer.data)
        
        elif "Select+Builder" not in BuilderQuery and SearchQuery != 0:
            #This block will execute when Builder and search query will be empty.
            print("9")
            #It will check whether the BuilderQuery is empty or not if it is not empty then this block will get executed and the BuilderQuery (+) will get replaced with (" ") to get the exact builder name.
            if "+" in SearchQuery:
                #If there is space present in the SearchQuery then this block will replace the query by removing the + sign to space.
                SearchName = SearchQuery.replace("+", " ") # replacing the SearchQuery + sign with space to get the exact query.
                
                BuilderQuery = BuilderQuery.replace("+", " ") # replacing the BuilderQuery + sign with space to get the exact query.
                
                builder = Builder.objects.get(BuilderName = BuilderQuery) #fetching the buildername from (models.py -> Builder model) for using in it the PropertyFiltered.
                
                PropertyFiltered = PropertyList.objects.filter(PropertyName__icontains=SearchName, BuilderName=builder)#Here we are filtering the data with (PropertyName, Property_Type, Location,SubPropertyType, BuilderName) from (models.py) by using the PropertyList model. 
                
                FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            elif "+" not in SearchQuery:
                #else, if there is no space present then it will send the search query into the SearchName field to get the results.
                
                SearchName = SearchQuery #here the SearchQuery will get saved when there is no space(+) is present in the query.
                
                BuilderQuery = BuilderQuery.replace("+", " ") # replacing the BuilderQuery + sign with space to get the exact query.
                
                builder = Builder.objects.get(BuilderName = BuilderQuery) #filtering the builder name by using the BuilderQuery to check whether the builder is present in the database from (models.py -> Builder model).

                PropertyFiltered = PropertyList.objects.filter(SearchName__icontains=SearchName, BuilderName=builder)#Here we are filtering the data with (PropertyName, Property_Type, Location,SubPropertyType, BuilderName) from (models.py) by using the PropertyList model.
                
                FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.

            FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            serializer = PropertyListSerializer(FinalResult, many=True)
                # sending the results back to the API request.
            
            return Response(serializer.data)
        
        elif "Select+Location" not in LocationQuery and SearchQuery != 0:
            #This block will execute when Location and search query will be empty.
            print("10")
            #It will check whether the BuilderQuery is empty or not if it is not empty then this block will get executed and the BuilderQuery (+) will get replaced with (" ") to get the exact builder name.

            if "+" in SearchQuery:
                #If there is space present in the SearchQuery then this block will replace the query by removing the + sign to space.
                SearchName = SearchQuery.replace("+", " ") # replacing the SearchQuery + sign with space to get the exact query.
            
                
                PropertyFiltered = PropertyList.objects.filter(PropertyName__icontains=SearchName, Location__icontains=LocationQuery)#Here we are filtering the data with (PropertyName, Property_Type, Location,SubPropertyType, BuilderName) from (models.py) by using the PropertyList model. 
                
                FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            elif "+" not in SearchQuery:
                #else, if there is no space present then it will send the search query into the SearchName field to get the results.
                
                SearchName = SearchQuery #here the SearchQuery will get saved when there is no space(+) is present in the query.

                PropertyFiltered = PropertyList.objects.filter(SearchName__icontains=SearchName, Location__icontains=LocationQuery)#Here we are filtering the data with (PropertyName, Property_Type, Location,SubPropertyType, BuilderName) from (models.py) by using the PropertyList model.
                
                FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.

            FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            serializer = PropertyListSerializer(FinalResult, many=True)
                # sending the results back to the API request.
            
            return Response(serializer.data)
        
        elif "Select+Property+Type" not in PropertyTypeQuery and SearchQuery != 0:
            #This block will execute when SubPropertyType will present and search query will not be empty.
            print("11")
            #It will check whether the BuilderQuery is empty or not if it is not empty then this block will get executed and the BuilderQuery (+) will get replaced with (" ") to get the exact builder name.
            if "+" in SearchQuery:
                #If there is space present in the SearchQuery then this block will replace the query by removing the + sign to space.
                SearchName = SearchQuery.replace("+", " ") # replacing the SearchQuery + sign with space to get the exact query.
                            
                PropertyFiltered = PropertyList.objects.filter(PropertyName__icontains=SearchName, Property_Type__icontains=PropertyTypeQuery)#Here we are filtering the data with (PropertyName, Property_Type, Location,SubPropertyType, BuilderName) from (models.py) by using the PropertyList model. 
                
                FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            elif "+" not in SearchQuery:
                #else, if there is no space present then it will send the search query into the SearchName field to get the results.
                
                SearchName = SearchQuery #here the SearchQuery will get saved when there is no space(+) is present in the query.

                PropertyFiltered = PropertyList.objects.filter(SearchName__icontains=SearchName, Property_Type__icontains=PropertyTypeQuery)#Here we are filtering the data with (PropertyName, Property_Type, Location,SubPropertyType, BuilderName) from (models.py) by using the PropertyList model.
                
                FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.

            FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            serializer = PropertyListSerializer(FinalResult, many=True)
                # sending the results back to the API request.
            
            return Response(serializer.data)
        
        elif "Select+Sub+Property+Type" not in SubPropertyTypeQuery and SearchQuery != 0:
            #This block will execute when SubPropertyType will present and search query will be empty.
            print("12")
            #It will check whether the BuilderQuery is empty or not if it is not empty then this block will get executed and the BuilderQuery (+) will get replaced with (" ") to get the exact builder name.
            if "+" in SearchQuery:
                #If there is space present in the SearchQuery then this block will replace the query by removing the + sign to space.
                SearchName = SearchQuery.replace("+", " ") # replacing the SearchQuery + sign with space to get the exact query.
            
                
                PropertyFiltered = PropertyList.objects.filter(PropertyName__icontains=SearchName,SubPropType__icontains=SubPropertyTypeQuery)#Here we are filtering the data with (PropertyName, Property_Type, Location,SubPropertyType, BuilderName) from (models.py) by using the PropertyList model. 
                
                FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            elif "+" not in SearchQuery:
                #else, if there is no space present then it will send the search query into the SearchName field to get the results.
                
                SearchName = SearchQuery #here the SearchQuery will get saved when there is no space(+) is present in the query.

                PropertyFiltered = PropertyList.objects.filter(SearchName__icontains=SearchName, SubPropType__icontains=SubPropertyTypeQuery)#Here we are filtering the data with (PropertyName, Property_Type, Location,SubPropertyType, BuilderName) from (models.py) by using the PropertyList model.
                
                FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.

            FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            serializer = PropertyListSerializer(FinalResult, many=True)
                # sending the results back to the API request.
            
            return Response(serializer.data)
        
        elif "Select+Sub+Property+Type" not in SubPropertyTypeQuery and SearchQuery != 0 and "Select+Property+Type" not in PropertyTypeQuery and "Select+Location" not in LocationQuery:
            #This block will execute when Location and PropertyType and SubPropertyType will present and search query will not be empty.
            print("13")

            #It will check whether the BuilderQuery is empty or not if it is not empty then this block will get executed and the BuilderQuery (+) will get replaced with (" ") to get the exact builder name.
            if "+" in SearchQuery:
                #If there is space present in the SearchQuery then this block will replace the query by removing the + sign to space.
                SearchName = SearchQuery.replace("+", " ") # replacing the SearchQuery + sign with space to get the exact query.
            
                
                PropertyFiltered = PropertyList.objects.filter(PropertyName__icontains=SearchName, SubPropType__icontains=SubPropertyTypeQuery,  Property_Type__icontains=PropertyTypeQuery, Location__icontains=LocationQuery,)#Here we are filtering the data with (PropertyName, Property_Type, Location,SubPropertyType) from (models.py) by using the PropertyList model. 
                
                FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            elif "+" not in SearchQuery:
                #else, if there is no space present then it will send the search query into the SearchName field to get the results.
                
                SearchName = SearchQuery #here the SearchQuery will get saved when there is no space(+) is present in the query.

                PropertyFiltered = PropertyList.objects.filter(SearchName__icontains=SearchName, SubPropType__icontains=SubPropertyTypeQuery,  Property_Type__icontains=PropertyTypeQuery, Location__icontains=LocationQuery,)#Here we are filtering the data with (PropertyName, Property_Type, Location,SubPropertyType) from (models.py) by using the PropertyList model.
                
                FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.

            FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            serializer = PropertyListSerializer(FinalResult, many=True)
                # sending the results back to the API request.
            
            return Response(serializer.data)
        elif "Select+Sub+Property+Type" in SubPropertyTypeQuery and SearchQuery != 0 and "Select+Property+Type" in PropertyTypeQuery and "Select+Location" in LocationQuery:
            #This block will execute when Location and PropertyType and SubPropertyType will present and search query will not be empty.
            print("14")

            #It will check whether the BuilderQuery is empty or not if it is not empty then this block will get executed and the BuilderQuery (+) will get replaced with (" ") to get the exact builder name.
            if "+" in SearchQuery:
                #If there is space present in the SearchQuery then this block will replace the query by removing the + sign to space.
                SearchName = SearchQuery.replace("+", " ") # replacing the SearchQuery + sign with space to get the exact query.
            
                
                PropertyFiltered = PropertyList.objects.filter(PropertyName__icontains=SearchName)#Here we are filtering the data with (PropertyName, Property_Type, Location,SubPropertyType, BuilderName) from (models.py) by using the PropertyList model. 
                
                FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            elif "+" not in SearchQuery:
                #else, if there is no space present then it will send the search query into the SearchName field to get the results.
                print("14")
                
                SearchName = SearchQuery #here the SearchQuery will get saved when there is no space(+) is present in the query.

                PropertyFiltered = PropertyList.objects.filter(SearchName__icontains=SearchName)#Here we are filtering the data with (PropertyName, Property_Type, Location,SubPropertyType, BuilderName) from (models.py) by using the PropertyList model.
                
                FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.

            FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            serializer = PropertyListSerializer(FinalResult, many=True)
                # sending the results back to the API request.

            return Response(serializer.data)

        elif "Select+Builder" not in BuilderQuery:
            #This block will execute when only BuilderName will be there.
            print("15")
            #It will check whether the BuilderQuery is empty or not if it is not empty then this block will get executed and the BuilderQuery (+) will get replaced with (" ") to get the exact builder name.
            
            BuilderQuery = BuilderQuery.replace("+", " ") # replacing the BuilderQuery + sign with space to get the exact query.
            
            builder = Builder.objects.get(BuilderName = BuilderQuery) #filtering the builder name by using the BuilderQuery to check whether the builder is present in the database from (models.py -> Builder model).
            
            PropertyFiltered = PropertyList.objects.filter(BuilderName=builder)#Here we are filtering the data with (BuilderName) from (models.py) by using the PropertyList model.
            
            FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            serializer = PropertyListSerializer(FinalResult, many=True)
                # sending the results back to the API request.
            
            return Response(serializer.data)
        
        elif "Select+Location" not in LocationQuery:
            #This block will execute when only Location will be there.
            print("16")
            #else this block will check whether the user has selected only the builder name and, if the user has selected the BuilderName then this block will get executed.
            PropertyFiltered = PropertyList.objects.filter(Location__icontains=LocationQuery)#Here we are filtering the data with (Location) from (models.py) by using the PropertyList model.
            FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            serializer = PropertyListSerializer(FinalResult, many=True)
            # sending the results back to the API request.

            return Response(serializer.data)
        
        elif "Select+Property+Type" not in PropertyTypeQuery:
            #This block will execute when only PropertyTypeQuery will be there.
            print("17")
            #else this block will check whether the user has selected only the builder name and, if the user has selected the BuilderName then this block will get executed.
            PropertyFiltered = PropertyList.objects.filter(Property_Type__icontains=PropertyTypeQuery)#Here we are filtering the data with (PropertyType) from (models.py) by using the PropertyList model.
            FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            serializer = PropertyListSerializer(FinalResult, many=True)
            # sending the results back to the API request.
            
            return Response(serializer.data)
        
        elif "Select+Sub+Property+Type" not in SubPropertyTypeQuery:
            #This block will execute when only SubPropertyType will be there.
            print("18")
            #else this block will check whether the user has selected only the builder name and, if the user has selected the BuilderName then this block will get executed.
            PropertyFiltered = PropertyList.objects.filter(SubPropType__icontains=SubPropertyTypeQuery)#Here we are filtering the data with (BuilderName) from (models.py) by using the PropertyList model.
            FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            serializer = PropertyListSerializer(FinalResult, many=True)
            # sending the results back to the API request.
            
            return Response(serializer.data)

        else:
            #if there is no-data present in the SearchQuery and PropertyTypeQuery and LocationQuery then it will send 0 as a response to the API call for showing the "no results found" block.
            FinalResult = 0
            return Response(FinalResult)

    except:
        #if any error occured in the above operation it will send all the properties details into the front end.
        FinalResult = 0
        # sending the results back to the API request.
        return Response(FinalResult)

@api_view(['GET']) #decorator with GET request permission we will use this when working with REST API for the Hot property section in home page.
def HotPropertyView(request):
    #This function will access the GET request from HotPropertyindex.js and in response it will return the json of all the related data.
    try:
        #This block will try to execute the data and then return the response.
        HotPropertiesData = HotPropertyList.objects.all() #get all the Hotproperties from HotPropertiesList model.
        serializer = HotPropertyListSerializer(HotPropertiesData, many=True) #by using HotPropertyListSerializer it will convert the data into json format, many=True means all the Fields would send from the model.
        return Response(serializer.data)
    except Exception:
        HotPropertiesData = HotPropertyList.objects.all()
        serializer = HotPropertyListSerializer(HotPropertiesData, many=True)
        return Response(serializer.data)

def HotIndividualProp(request, name, loc):
    """
    This function access the Prop_ID form the url and with the help 
    of that Prop_ID it will filter out the individual HotProperty details as well as the multiple images of the particular Hotproperty from the HotPropertyList model.
    """
    Propertyname = name.replace("-", " ")
    Ind_PropData = HotPropertyList.objects.get(PropertyName__icontains=Propertyname)  # Filtering the individual prop data by using the Prop_ID.
    Ind_Prop_Images = HotPropertyImages.objects.filter(Image_ID= Ind_PropData)  #Filter the images according to the Ind_PropData.
    Amenity = Ind_PropData.Property_Amenities.all()   #Filter  all the amenities details insert to Amenity
    PropImages = PropertyList.objects.all()   #Filter all the Property List objects and insert into PropImages variable.
    Recent_Property = PropertyList.objects.all().order_by('-Prop_ID')[:4] #Filtering the last 4 element of the PropertyList objects by firtly ordering by Prop_id

    Ind_PropDataDict = {
        'Prop_Data': Ind_PropData,  #property details.
        'Prop_Img': Ind_Prop_Images, #property images.
        'amenities' : Amenity,     #property amenities.
        'featured_images' : PropImages, #property Images.
        'recent_properties' :Recent_Property, #recent property details.
    }  # Creating the Prop_Data dictionary to send it in the front end template.
    return render(request, 'details.html', Ind_PropDataDict)

def IndividualProp(request, name, loc):
    """
    This function access the Prop_ID form the url and with the help 
    of that Prop_ID it will filter out the individual property details as well as the multiple images of the particular property from the PropertyList model.
    """
    Propertyname = name.replace("-", " ")
    Ind_PropData = PropertyList.objects.get(PropertyName__icontains=Propertyname)  # Filtering the individual prop data by using the Prop_ID.
    Ind_Prop_Images = PropertyImages.objects.filter(Image_ID= Ind_PropData)  #Filter the images according to the Ind_PropData.
    Amenity = Ind_PropData.Property_Amenities.all()   #Filter  all the amenities details insert to Amenity
    PropImages = PropertyList.objects.all()   #Filter all the Property List objects and insert into PropImages variable.
    Recent_Property = PropertyList.objects.all().order_by('-Prop_ID')[:4] #Filtering the last 4 element of the PropertyList objects by firtly ordering by Prop_id

    Ind_PropDataDict = {
        'Prop_Data': Ind_PropData,  #property details.
        'Prop_Img': Ind_Prop_Images, #property images.
        'amenities' : Amenity,     #property amenities.
        'featured_images' : PropImages, #property Images.
        'recent_properties' :Recent_Property, #recent property details.
    }  # Creating the Prop_Data dictionary to send it in the front end template.
    return render(request, 'details.html', Ind_PropDataDict)


@api_view(['POST'])  # decorator with POST request permission we will use this when working with REST API.
def advfilt_properties(request):
    try:
        """
        This function will access the searchquery + propertytypequery + locationquery from the API request and do the filteration with the database and in the end return the response.
        """

        SearchQuery = request.data['SearchQuery']  # accessing the SearchQuery form the API request.
        
        BuilderQuery = request.data['BuilderQuery']  # accessing the BuilderQuery form the API request.

        LocationQuery = request.data['LocationQuery'] # accessing the LocationQuery form the API request.
        
        PropertyTypeQuery = request.data['PropertyTypeQuery'] # accessing the PropertyTypeQuery form the API request.

        SubPropertyTypeQuery = request.data['SubPropertyTypeQuery'] # accessing the SubPropertyTypeQuery form the API request.
        
        PropertyStatusQuery = request.data['PropertyStatusQuery'] # accessing the PropertyStatusQuery form the API request.
        
        PriceQuery = request.data['PriceRange'] # accessing the PriceRange form the API request.
        
        PriceQueryInt = int(PriceQuery) #converting the range into integer to get the range values.
        PriceQueryArr = [] #here we will store the PriceRange in the form of array.
        for numRange in range(0, PriceQueryInt):
            #This for loop will iterate over all the values from 0 to PriceQueryInt and append it inside the PriceQueryArr
            PriceQueryArr.append(numRange)

        if SearchQuery and PropertyTypeQuery and LocationQuery and BuilderQuery and SubPropertyTypeQuery and PropertyStatusQuery and PriceQuery != 0:
            #if there is data present inside of SearchQuery, PropertyTypeQuery, LocationQuery, then this block perform the operations.
            SearchName = 0 #creating a variable for storing the filtered properties based on the searchName
            
            if "+" in SearchQuery:
                #If there is space present in the SearchQuery then this block will replace the SearchQuery by removing the + sign to space.
                SearchName = SearchQuery.replace("+", " ") # replacing the SearchQuery + sign with space to get the exact query.
                BuilderQuery = BuilderQuery.replace("+", " ") # replacing the BuilderQuery + sign with space to get the exact Builder Name.
                builder = Builder.objects.get(BuilderName = BuilderQuery) #fetching the buildername from (models.py -> Builder model) for using in it the PropertyFiltered filter.

                PropertyFiltered = PropertyList.objects.filter(Location__icontains=LocationQuery, Property_Type__icontains=PropertyTypeQuery, SubPropType__icontains=SubPropertyTypeQuery,PropertyName__icontains=SearchName, BuilderName=builder, PropertyStatus__icontains=PropertyStatusQuery, Property_Price__icontains=PriceQueryArr)#Here we are filtering the data with (PropertyName, Property_Type, Location,SubPropertyType, BuilderName, PropertyStatus and Property_Price) from (models.py) by using the PropertyList model. 
                
                FinalResult = PropertyFiltered #here we are storing the PropertyFiltered results in the FinalResult variable that will go with the Response.
            else:
                #else, if there is no space present in the SearchQuery then it will send the SearchQuery into the SearchName field to get the results.

                SearchName = SearchQuery #here the SearchQuery will get saved when there is no space(+) is present in the query.
                BuilderQuery = BuilderQuery.replace("+", " ") # replacing the BuilderQuery + sign with space to get the exact Builder Name.
                builder = Builder.objects.get(BuilderName = BuilderQuery) #fetching the buildername from (models.py -> Builder model) for using in it the PropertyFiltered filter.

                PropertyFiltered = PropertyList.objects.filter(Location__icontains=LocationQuery, Property_Type__icontains=PropertyTypeQuery, SubPropType__icontains=SubPropertyTypeQuery,PropertyName__icontains=SearchName, BuilderName=builder, PropertyStatus__icontains=PropertyStatusQuery, Property_Price__icontains=PriceQueryArr)#Here we are filtering the data with (PropertyName, Property_Type, Location,SubPropertyType, BuilderName, PropertyStatus and Property_Price) from (models.py) by using the PropertyList model. 
                
                FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
                
            
            if len(FinalResult) != 0:
                #if there is data present in the FinalResults then it will get sent to the API call as result.
                # serializing the data into json format.
                serializer = PropertyListSerializer(FinalResult, many=True)
                # sending the results back to the API request.
                return Response(serializer.data)
            else:
                #if there is no-data present in the FinalResults then it will send 0 as a response to the API call for showing the "no results found" block.
                FinalResult = 0
                # sending the results back to the API request.
                return Response(FinalResult)

        elif BuilderQuery and LocationQuery !=0:
            #else this block will check whether the user has selected only the builder name and location, if the user has selected the BuilderName and location then this block will get executed.
            
            BuilderQuery = BuilderQuery.replace("+", " ")  # replacing the BuilderQuery + sign with space to get the exact Builder Name.
            builder = Builder.objects.get(BuilderName = BuilderQuery) #fetching the buildername from (models.py -> Builder model) for using in it the PropertyFiltered filter.
            PropertyFiltered = PropertyList.objects.filter(BuilderName=builder, Location__icontains=LocationQuery)#Here we are filtering the data with (BuilderName and location) from (models.py) by using the PropertyList model.
            
            FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            serializer = PropertyListSerializer(FinalResult, many=True)
                # sending the results back to the API request.
            return Response(serializer.data)
        
        elif LocationQuery != 0:
            #else this block will check whether the user has selected only the Location, if the user has selected the BuilderName then this block will get executed.
            
            PropertyFiltered = PropertyList.objects.filter(Location__icontains=LocationQuery)#Here we are filtering the data with (Location) from (models.py) by using the PropertyList model.
            
            FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            serializer = PropertyListSerializer(FinalResult, many=True)
                # sending the results back to the API request.
            return Response(serializer.data)
        
        elif BuilderQuery !=0:
            #else this block will check whether the user has selected only the builder name and, if the user has selected the BuilderName then this block will get executed.
            
            BuilderQuery = BuilderQuery.replace("+", " ")  # replacing the BuilderQuery + sign with space to get the exact Builder Name.
            builder = Builder.objects.get(BuilderName = BuilderQuery) #fetching the buildername from (models.py -> Builder model) for using in it the PropertyFiltered filter.
            PropertyFiltered = PropertyList.objects.filter(BuilderName=builder)#Here we are filtering the data with (BuilderName) from (models.py) by using the PropertyList model.
            
            FinalResult = PropertyFiltered #here we are storing the PropertyFiltered in the FinalResult variable that will go with the Response.
            serializer = PropertyListSerializer(FinalResult, many=True)
                # sending the results back to the API request.
            return Response(serializer.data)
        
        else:
            #if there is no-data present in the SearchQuery and PropertyTypeQuery and LocationQuery then it will send 0 as a response to the API call for showing the "no results found" block.
            FinalResult = 0
            return Response(FinalResult)

    except:
        #if any error occured in the above operation it will send all the properties details into the front end.
        FinalResult = 0
        # sending the results back to the API request.
        return Response(FinalResult)


def PropertyContactData(request):
    """
    This function will handle the data coming from the modal contact page and store the details in the PropertyContact database.
    """
    if request.method == 'POST':  #if request is post it will fetch the details.
        try:
            #it will try to do the operation if it fails the except block will get executed.
            success = True #setting the variable as true and if everything went right it will get send to the frontend as response to show the success alert message in the carrier form.
            Data = json.loads(request.body.decode(
                "utf-8"))  #loading the json from the fetch API request.
            Name = Data['Name']  #user name.
            Email = Data['Email']  #user email.
            Phone = Data['Phone']  #user phone number.
            PropertyData = Data['Propdetail'] #user address.
            Message = Data['Message']  #user message.
            if (Name and Email and Phone and Message and PropertyData != 0):
                #when all the values will have the data then only it will store the data into the database.
                userData = PropertyContact(
                    name=Name, email=Email, phone=Phone,
                    message=Message, property_Name = PropertyData)  #saving the data into the database.
                userData.save()  #saving the data into database.
                params = {
                    'success': success 
                }  #making a dictionary for converting it into json.
                successData = json.dumps(
                    params)  #converting dictionary into json.
                return HttpResponse(successData)  #sending the reply.
            else:
                #if any one of the value will be empty it will send the error as a response.
                success = False #converting the value into false to show the error message in the front end.
            params = {
                'success': success
            }  #making a dictionary for converting it into json.
            successData = json.dumps(params)  #converting dictionary into json.
            return HttpResponse(successData)  #sending the reply.
        except Exception:
            #if any error happens it will send the error response to the frontend.
            success = False #converting the value into false to show the error message in the front end.
            params = {
                'success': success
            }  #making a dictionary for converting it into json.
            successData = json.dumps(params)  #converting dictionary into json.
            return HttpResponse(successData)  #sending the reply.

def ExclusiveProperty(request, Tag):
    if Tag == "mjr":
        return render(request, 'Exclusive-1.html')
    elif Tag == "neel":
        return render(request, 'Exclusive-2.html')
    elif Tag == "kk":
        return render(request, 'Exclusive-3.html')
    elif Tag == "sr":
        return render(request, 'Exclusive-4.html')
    elif Tag == "gp":
        return render(request, 'Exclusive-5.html')
    elif Tag == "sp":
        return render(request, 'Exclusive-6.html')

def compare_property(request):
    """
    This function will handle the data coming from the compare property page.
    """
    print("called ajax")
    if request.method == 'GET':  #if request is get it will fetch the details.
        try:
            #it will try to do the operation if it fails the except block will get executed.
            success = True  # it will check for successfully Provided of the data.
            name = request.GET['val1']  #get the value which is stored in val1

            property_details = PropertyList.objects.filter(PropertyName=name)  #Get the PropertyList by its Name   
         
            details = PropertyListSerializer(property_details, many=True) #it will dumps the data in the List  serializer.
            return JsonResponse(details.data, safe=False)  #sending the reply with details in JsonResponse
          #this will try when try block gets fail
        except Exception as e:
            #if any error happens it will send the error response to the frontend.
            fail = False
            params = {
                'fail': fail
            }  #making a dictionary for converting it into json.
            # successData = json.dumps(params)  #converting dictionary into json.
            return JsonResponse(params)  #sending the reply with details in JsonResponse

def compare(request):
    """ 
    This will return the compare page.
    """
    property_details = PropertyList.objects.all()
    return render(request, 'compare.html', {'property_details':property_details})