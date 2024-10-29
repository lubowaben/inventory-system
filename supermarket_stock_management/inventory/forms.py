from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import Product, Supplier, Profile,Notification,Cashier,StockTransaction

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'sku', 'category', 'price', 'quantity', 'supplier', 'expiry_date']
        quantity = forms.IntegerField(min_value=0, required=True)
        product = forms.ModelChoiceField(queryset=Product.objects.all())



class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_info']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'address', 'phone_number']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class PasswordChangeCustomForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput, label='Old Password')
    new_password1 = forms.CharField(widget=forms.PasswordInput, label='New Password')
    new_password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm New Password')

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

class CashierRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=[('cashier', 'Cashier')], widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter notification message'}),
        }
class CashierForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True)

    class Meta:
        model = Cashier
        fields = ['name', 'contact_info', 'user','employee_id','email','address']
    def clean_employee_id(self):
        employee_id = self.cleaned_data.get('employee_id')
        if Cashier.objects.filter(employee_id=employee_id).exists():
            raise forms.ValidationError('A cashier with this employee ID already exists.')
        return employee_id
    
        
class StockTransactionForm(forms.ModelForm):
    class Meta:
        model = StockTransaction
        fields = ['product', 'quantity', 'transaction_type', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }