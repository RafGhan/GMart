from django.forms import ModelForm
from main.models import Item
from django import forms   # NEW!
from django.contrib.auth.models import User   

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description", "type"]
    
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True)  # NEW