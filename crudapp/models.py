from django.db import models
"""from django.utils.deconstruct import deconstructible"""

"""@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)

path_and_rename = PathAndRename("/media")"""


class Contact(models.Model):
    firstName = models.CharField("First name", max_length=255, blank = True, null = True)
    lastName = models.CharField("Last name", max_length=255, blank = True, null = True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank = True, null = True)
    address = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    membre = models.ManyToManyField("Club", blank = True)
    display_pictur = models.ImageField(blank=True, upload_to="crudapp/templates/media/", default="crudapp/templates/media/static/telechargement.jpg")
    def __str__(self):
        return self.firstName

class Club(models.Model):
    name=models.CharField("name", max_length=255, blank = True, null = True)
    typeClub=models.CharField("Type Club",max_length=255, blank = True, null = True)
    #clubMembers=models.ManyToManyField("Contact", blank = True) 
    clubActivity=models.ManyToManyField("Activity", blank = True)   

class Activity(models.Model):
    name=models.CharField("name", max_length=255, blank = True, null = True)
    typeActivity=models.CharField("Type Activity",max_length=255, blank = True, null = True)  
    #club=models.ManyToManyField("ClubActivity", blank = True)
   

def __str__(self):
    return self.firstName   