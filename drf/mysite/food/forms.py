from django import forms
from .models import Item
from django.core import validators

def must_start_with_capital(value):
    if value[0] != value[0].capitalize():
        raise forms.ValidationError("Does not start with a capital letter")

def must_have_at_least_three_characters(value):
    if len(value) < 3:
        raise forms.ValidationError("Must be at least 3 characters long")

def must_be_at_least_length_10(value):
    n = len(value.replace(' ', ''))
    if n < 10:
        raise forms.ValidationError(f"Minimum description should be 10 characters, but it is only {n}")

class ItemForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'
    
    item_name = forms.CharField(
        validators=[must_start_with_capital, must_have_at_least_three_characters],
        label='Name',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Name'}
        )
    )

    item_desc = forms.CharField(
        validators=[must_be_at_least_length_10],
        label='Description',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'maxlength': 2000})
    ) 

    class Meta:
        model = Item
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']
        # fields = '__all__'
        
        labels = {
            # 'item_name': 'Name',
            # 'item_desc': 'Description',
            'item_price': 'Price',
            'item_image': 'Upload a photo',
        }

        widgets = {
            # 'item_desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'item_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 0.00}),
            'item_image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class ItemDeleteForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ['id']

        widgets = {
            'id': forms.HiddenInput()
        }
