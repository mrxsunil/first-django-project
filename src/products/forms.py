from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title       = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Your Title "}))
    description = forms.CharField(required=False,
                                         widget=forms.Textarea(attrs={
                                             "class":"new-class-name two",
                                             "rows": 15
                                         }))
    price       = forms.DecimalField(initial=199.99)
    # email       = forms.EmailField()
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    # def clean_<my_field_name>
    # def clean_title(self, *args, **kwargs):
    #     title  = self.cleaned_data.get("title")
    #     if not "CFE" in title:
    #         raise forms.ValidationError("THis is not valid")
    #     return title
    
    # def clean_email(self, *args, **kwargs):
    #     email  = self.cleaned_data.get("email")
    #     if not email.endswith(".edu"):
    #         raise forms.ValidationError("THis is not valid")
    #     return email



class RawProductForm(forms.Form):
    title       = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Your Title "}))
    description = forms.CharField(required=False,
                                         widget=forms.Textarea(attrs={
                                             "class":"new-class-name two",
                                             "rows": 10
                                         }))
    price       = forms.DecimalField(initial=199.99)
