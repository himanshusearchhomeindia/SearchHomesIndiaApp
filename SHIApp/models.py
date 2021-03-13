from django.db import models
from datetime import datetime #we are using it in timestamp field.
# Create your models here.

class Amenities(models.Model):
    """
    This model will store the information of the Amenities that are associated with the property.
    """
    Title = models.CharField(max_length=100, default=None)  #This will be the name of the amenities that are present in the particuler property.
    Icon = models.FileField(upload_to='static/Icon') #This will store the Amenities icon files inside (SHIProj\static\Icon) folder.
    
    def __str__(self):
        """
        This function will show the amenities name(Title) instead of object in admin panel.
        """
        return f'{self.Title}'

    class Meta:
        """
        This meta class will help functions to fetch the data.(Prashnat)
        """
        verbose_name_plural = "Amenities"

class Builder(models.Model):
    """
    This model will store the information of the builders that are associated with the property.
    """
    BuilderName = models.CharField(max_length=50, default=None) #This will store the builder's name.
    Logo = models.FileField(upload_to='static/BuilderLogo') #This will store the logo images related to the builder inside (SHIProj\static\BuilderLogo) folder..
    SolePartner = models.CharField(max_length=100, default=None) #This will store the partners that are associated with a particular builder.

    def __str__(self):
        """
        This function will show the builder name instead of object in admin panel.
        """
        return f'{self.BuilderName}'


class PropertyList(models.Model):
    """
    This model will store the information about all the properties with their description and other information and we will use this model in general search and advanced search.
    """
    Prop_ID = models.AutoField(
        primary_key=True)  # prop id will be our primary key based on this id the property individual page will work.

    # builder name will get stored here related to a particular property.
    BuilderName = models.ForeignKey(Builder, on_delete=models.SET_NULL, null=True)

    # property name will be stored here.
    PropertyName = models.CharField(max_length=100, unique=True)

    slug = models.CharField(max_length=550, default="", null=True) #This slug is used for showing the property name and location in the url.

    #we are using this for improvement of search functionality if the user will write the query in small letter than with the help of this table the filteration will be done.
    SearchName = models.CharField(max_length=100, default="") #This field will help us to make the general search work better !(always store the values in small letters with no space).

    # property images will get uploaded here, inside the (SHIProj\static\Property_images) folder.
    Property_Image = models.ImageField(upload_to='static/Property_images')

    # Master Plan will get uploaded here, inside the (SHIProj\static\Master_Plans) folder.
    Master_Plan = models.ImageField(upload_to='static/Master_Plans', blank=True, default="")

    # Master Plan will get uploaded here, inside the (SHIProj\static\Floor_Plan_1BHK) folder.
    Floor_Plan_1BHK = models.ImageField(upload_to='static/Floor_Plan_1BHK', blank=True, default="")
    
    # Floor_Plan_2BHK will get uploaded here, inside the (SHIProj\static\Floor_Plan_2BHK) folder.
    Floor_Plan_2BHK = models.ImageField(upload_to='static/Floor_Plan_2BHK', blank=True, default="")
    
    # Floor_Plan_3BHK will get uploaded here, inside the (SHIProj\static\Floor_Plan_3BHK) folder.
    Floor_Plan_3BHK = models.ImageField(upload_to='static/Floor_Plan_3BHK', blank=True, default="")
    
    # Floor_Plan_4BHK will get uploaded here, inside the (SHIProj\static\Floor_Plan_4BHK) folder.
    Floor_Plan_4BHK = models.ImageField(upload_to='static/Floor_Plan_4BHK', blank=True, default="")
    
    #video related to a particular property will get stored here inside the (SHIProj\static\Videos) folder.
    Video = models.FileField(upload_to='static/Videos', blank=True, default="")

    # property price will be stored here.
    Property_Price = models.CharField(max_length=50)

    # property description will be stored here.
    Property_Description = models.TextField(max_length=1000)

    PropertyStat = [
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Ready to move', 'Ready to move'),
    ]  # choices for property status.
    # property status will be stored here.
    PropertyStatus = models.CharField(max_length=50, choices=PropertyStat)

    PropertyType = [
        ('Residential', 'Residentail'),
        ('Commercial', 'Commercial'),
    ]  # choices for propertytype.
    # property type will be stored here.
    Property_Type = models.CharField(
        max_length=20, choices=PropertyType, default='Residential')

    SubProp = [
        ('Plot', 'Plot'),
        ('Villa', 'Villa'),
        ('Apartment', 'Apartment'),
        ('Rowhouse', 'Rowhouse'),
        ('Farmhouse', 'Farmhouse'),
        #this is used to add the sub property dropdown menu in the general search(this will help the user to get the correct result).
    ]
    #subproptype details will get stored here.
    SubPropType = models.CharField(max_length=60, choices=SubProp, default="")
    
    MultipleLocations = [
        ('Bangalore', 'Bangalore'),
        ('Mumbai', 'Mumbai'),
        ('Delhi', 'Delhi'),
        ('Punjab', 'Punjab'),
    ]  # choices for locations.
    # property locations will get stored here.
    Location = models.CharField(max_length=50, choices=MultipleLocations)

    # property address will get stored here.
    PropertyAddress = models.CharField(max_length=100)

    # BHK values will be stored here.
    BHK = models.CharField(max_length=50)  

    # property avaliability will get stored here and the default value will be Sale.
    Avaliable_For = models.CharField(max_length=50, default="Sale")

    #Property_Amenities is the foreign model that we are using here to store the amenities related to the particular property.
    Property_Amenities = models.ManyToManyField(Amenities)
    
    #Project_Area will store the information about in how many acres the project is Build.
    Project_Area = models.CharField(max_length=100, default=None)
    
    #PerSqftPrice will store the information about the cost of per square feet of a property.
    PerSqftPrice = models.CharField(max_length=100, default=None)

    # Google_Map api will get stored here, the google map api key.
    Google_Map = models.CharField(max_length=10000, default="")

    #Time stamp for showing at what time the particular property has been listen in the site.
    timestamp = models.DateTimeField(default=datetime.now)

    def __str__(self):
        """
        This function will show the property name with property id instead of object in admin panel.
        """
        return f"{self.PropertyName, self.Prop_ID}"


class PropertyImages(models.Model):

    """
    This model will store all the images of a particular property with the help of the ForeignKey(PropertyList)
    """
    Image_ID = models.ForeignKey(PropertyList, on_delete=models.CASCADE)  #image id will be based in Foreign key.
    Images = models.ImageField(upload_to='static/IndividualPropImgs')  #here the multiple images will get stored inside the (SHIProj\static\IndividualPropImgs) (!store one image at a time of a single property).

    def __str__(self):
        """
        This function will show the property image id instead of object in admin panel.
        """
        return f"{self.Image_ID}"

class HotPropertyList(models.Model):
    """
    This model will store the information about all the Hot Properties with their description and other information and we will use this model in general search and advanced search.
    """
    Prop_ID = models.AutoField(
        primary_key=True)  # prop id will be our primary key based on this id the property individual page will work.

    # builder name will get stored here related to a particular property.
    BuilderName = models.ForeignKey(Builder, on_delete=models.SET_NULL, null=True)

    # property name will be stored here.
    PropertyName = models.CharField(max_length=100, unique=True)

    slug = models.CharField(max_length=550, default="", null=True) #This slug is used for showing the property name and location in the url.

    #we are using this for improvement of search functionality if the user will write the query in small letter than with the help of this table the filteration will be done.
    SearchName = models.CharField(max_length=100, default="") #This field will help us to make the general search work better !(always store the values in small letters with no space).

    # property images will get uploaded here, inside the (SHIProj\static\HotProperty_images) folder.
    Property_Image = models.ImageField(upload_to='static/HotProperty_images')

    # Master Plan will get uploaded here, inside the (SHIProj\static\HotMaster_Plans) folder.
    Master_Plan = models.ImageField(upload_to='static/HotMaster_Plans', blank=True, default="")

    # Master Plan will get uploaded here, inside the (SHIProj\static\Floor_Plan_1BHK) folder.
    Floor_Plan_1BHK = models.ImageField(upload_to='static/Hot_Prop_Floor_Plan_1BHK', blank=True, default="")
    
    # Floor_Plan_2BHK will get uploaded here, inside the (SHIProj\static\Floor_Plan_2BHK) folder.
    Floor_Plan_2BHK = models.ImageField(upload_to='static/Hot_Prop_Floor_Plan_2BHK', blank=True, default="")
    
    # Floor_Plan_3BHK will get uploaded here, inside the (SHIProj\static\Floor_Plan_3BHK) folder.
    Floor_Plan_3BHK = models.ImageField(upload_to='static/Hot_Prop_Floor_Plan_3BHK', blank=True, default="")
    
    # Floor_Plan_4BHK will get uploaded here, inside the (SHIProj\static\Floor_Plan_4BHK) folder.
    Floor_Plan_4BHK = models.ImageField(upload_to='static/Hot_Prop_Floor_Plan_4BHK', blank=True, default="")
    
    #video related to a particular property will get stored here inside the (SHIProj\static\HotVideos) folder.
    Video = models.FileField(upload_to='static/HotPropVideos', blank=True, default="")

    # property price will be stored here.
    Property_Price = models.CharField(max_length=50)

    # property description will be stored here.
    Property_Description = models.TextField(max_length=1000)

    PropertyStat = [
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Ready to move', 'Ready to move'),
    ]  # choices for property status.
    # property status will be stored here.
    PropertyStatus = models.CharField(max_length=50, choices=PropertyStat)

    PropertyType = [
        ('Residential', 'Residentail'),
        ('Commercial', 'Commercial'),
    ]  # choices for propertytype.
    # property type will be stored here.
    Property_Type = models.CharField(
        max_length=20, choices=PropertyType, default='Residential')

    SubProp = [
        ('Plot', 'Plot'),
        ('Villa', 'Villa'),
        ('Apartment', 'Apartment'),
        ('Rowhouse', 'Rowhouse'),
        ('Farmhouse', 'Farmhouse'),
        #this is used to add the sub property dropdown menu in the general search(this will help the user to get the correct result).
    ]
    #subproptype details will get stored here.
    SubPropType = models.CharField(max_length=60, choices=SubProp, default="")
    
    MultipleLocations = [
        ('Bangalore', 'Bangalore'),
        ('Mumbai', 'Mumbai'),
        ('Delhi', 'Delhi'),
        ('Punjab', 'Punjab'),
    ]  # choices for locations.
    # property locations will get stored here.
    Location = models.CharField(max_length=50, choices=MultipleLocations)

    # property address will get stored here.
    PropertyAddress = models.CharField(max_length=100)

    # BHK values will be stored here.
    BHK = models.CharField(max_length=50)  

    # property avaliability will get stored here and the default value will be Sale.
    Avaliable_For = models.CharField(max_length=50, default="Sale")

    #Property_Amenities is the foreign model that we are using here to store the amenities related to the particular property.
    Property_Amenities = models.ManyToManyField(Amenities)
    
    #Project_Area will store the information about in how many acres the project is Build.
    Project_Area = models.CharField(max_length=100, default=None)
    
    #PerSqftPrice will store the information about the cost of per square feet of a property.
    PerSqftPrice = models.CharField(max_length=100, default=None)

    # Google_Map api will get stored here, the google map api key.
    Google_Map = models.CharField(max_length=10000, default="")

    #Time stamp for showing at what time the particular property has been listen in the site.
    timestamp = models.DateTimeField(default=datetime.now)

    def __str__(self):
        """
        This function will show the property name with property id instead of object in admin panel.
        """
        return f"{self.PropertyName, self.Prop_ID}"


class HotPropertyImages(models.Model):

    """
    This model will store all the images of a particular Hotproperty with the help of the ForeignKey(PropertyList)
    """
    Image_ID = models.ForeignKey(HotPropertyList, on_delete=models.CASCADE)  #image id will be based in Foreign key.
    Images = models.ImageField(upload_to='static/HotIndividualPropImgs')  #here the multiple images will get stored inside the (SHIProj\static\HotIndividualPropImgs) (!store one image at a time of a single property).

    def __str__(self):
        """
        This function will show the property image id instead of object in admin panel.
        """
        return f"{self.Image_ID}"

class UserContactData(models.Model):

    """
    This model is used to store the contact info about the user who has filled the contact form (normal contact from).
    """
    sno = models.AutoField(primary_key=True) #This will be the primary key for the contact data.
    name = models.CharField(max_length=60, default="")  #user name will get stored here.
    email = models.CharField(max_length=60, default="") #user email will get stored here.
    phone = models.CharField(max_length=12, default=None) #user phone number will get stored here.
    contact_time = models.DateTimeField(default=datetime.now)  #user contact time field, at what time the user has submitted the contact from.
    message = models.TextField(default="") #user message will get stored here.

    def __str__(self):
        """
        This function will show the username instead of object in admin panel.
        """
        return f"{self.name}"


class UserResumeData(models.Model):
    """
    This model is used to store the contact info about the user who has submitted the carrirers from.
    """
    sno = models.AutoField(primary_key=True) #This will be the primary key for the userresume data.
    name = models.CharField(max_length=60, default="")  #user name will get stored here.
    email = models.CharField(max_length=60, default="") #user email will get stored here.
    phone = models.CharField(max_length=12, default=None) #user phone number will get stored here.
    resumetime = models.DateTimeField(default=datetime.now)  #user contact time field, at what time the user has filled the carrier from.
    vacancy = models.CharField(max_length=100, default="") #vacancy info will get stored here.
    message = models.TextField(default="") #user message will get stored here.

    def __str__(self):
        """
        This function will show the user name instead of object in admin panel.
        """
        return f"{self.name}"

class PropertyContact(models.Model):

    """
    This model is used to store the contact info about the user and the property name for which he is looking at.
    """
    sno = models.AutoField(primary_key=True) #This will be the primary key for the property contact data.
    name = models.CharField(max_length=60, default="")  #user name will get stored here.
    email = models.CharField(max_length=60, default="") #user email will get stored here.
    phone = models.CharField(max_length=12, default=None) #user phone number will get stored here.
    property_Name = models.CharField(max_length=100, default="")  #property name for which he is looking at.
    message = models.TextField(default="") #user message will get stored here.
    contactTime = models.DateTimeField(default=datetime.now) #this will store the time of the inquiry.

    def __str__(self):
        """
        This function will show the user name + property name instead of object in admin panel.
        """
        return f"{self.name} {self.property_Name}"