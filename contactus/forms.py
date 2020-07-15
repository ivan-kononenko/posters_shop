from django.forms import ModelForm
from .models import ContactRequest


# Create the form class.
class ContactRequestForm(ModelForm):
    class Meta:
        model = ContactRequest
        fields = ['name', 'email', 'message']