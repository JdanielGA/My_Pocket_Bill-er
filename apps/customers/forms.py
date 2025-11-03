# apps/customers/forms.py
from django import forms
from .models import Customer

# Form for creating and updating Customer instances.
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'customer_type',
            'customer_id',
            'email',
            'country',
            'city',
            'phone_number',
            'address',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_type': forms.Select(attrs={'class': 'form-select'}),
            'customer_id': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean_customer_id(self):
        customer_id = self.cleaned_data.get('customer_id')
        if not customer_id:
            return customer_id
        
        query = Customer.objects.filter(customer_id=customer_id)
        if self.instance and self.instance.pk:
            query = query.exclude(pk=self.instance.pk)
        
        if query.exists():
            raise forms.ValidationError("Customer ID already exists. Please choose a different one.")
        return customer_id