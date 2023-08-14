from django import forms
from .models import Contact
from .models import Club
from .models import Activity
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = "__all__"

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = "__all__"


