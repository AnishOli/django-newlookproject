# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import Customer

# class CustomerRegistrationForm(UserCreationForm):
#     class Meta:
#         model = Customer
#         fields = [
#             'first_name',
#             'last_name',
#             'email',
#             'phone_number',
#             'city',
#             'dob',
#             'username',
#             'password1',
#             'password2',
#         ]



from django import forms
from .models import Customer

class CustomerRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "email", "phone_number", "city", "dob"]

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("password1") != cleaned.get("password2"):
            raise forms.ValidationError("Passwords do not match")
        return cleaned


