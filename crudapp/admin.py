from django.contrib import admin
from .models import Contact
from .models import Club
from .models import Activity


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
     list_display=['firstName','lastName','email','phone','address','display_pictur']
     list_per_page = 2
     


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
     list_display=['name','typeClub']

@admin.register(Activity)
class ClubAdmin(admin.ModelAdmin):
     list_display=['name','typeActivity']
