from django import forms
from django.forms import widgets
from webapp.models import CATEGORY_CHOICES


class GoodForm(forms.Form):
    description = forms.CharField(max_length=100, required=True, label="Description")
    detailed_description = forms.CharField(max_length=2000, required=True, label="Detailed description",
                                           widget=widgets.Textarea(attrs={"rows":5 , "cols":50}))
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label="Category", required=True,  initial=CATEGORY_CHOICES[0][1])
    remainder = forms.IntegerField(min_value=0, required=True, label="Remainder",)
    price = forms.DecimalField(required=True, label="Price", decimal_places=2)