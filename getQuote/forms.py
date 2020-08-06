from django import forms
from .models import GetAQuote

class QuoteFormForAdmin(forms.ModelForm):
    """A form to give custom appearance to the registration table.
    """
    class Meta:
        model = GetAQuote
        fields = ('name', 'phone_number', 'email', 'project_type', 'description')


class QuoteFormForFrontend(forms.ModelForm):
    """A form to give custom appearance to the registration table.
    """

    PROJECT_CHOICES = [
        ('Cloud Services','Cloud Services'),
        ('Web and App Design','Web and App Design'),
        ('Microsoft 365','Microsoft 365'),
        ('IT Consulting','IT Consulting'),
        ('Cyber Security', 'Cyber Security'),
        ('IT Training', 'IT Training'),
        ('CCTV Installation', 'CCTV Installation'),
        ('Inverter Installation', 'Inverter Installation'),
        ('Solar Installation', 'solar Installation'),
        ('UPS Installation', 'UPS Installation'),
        ('IT Equipments', 'IT Equipments'),
        ('Computer Accessories', 'Computer Accessories'),
        ]


    name = forms.CharField(
        max_length=100, label='Enter your full name:', widget=forms.TextInput(
            attrs={
                'class': 'text-input error-handler first_name home-address col-12',
                'placeholder': 'Full name',
                'name': 'name'
            }
        ))

    phone_number = forms.CharField(
        max_length=100, label='Enter your phone number:', widget=forms.TextInput(
            attrs={
                'class': 'text-input error-handler phone-number col-12',
                'name': 'phone_number',
                'placeholder': 'E.g 080XXXXXXXX',
                'pattern': r'^[0][8]\d{9}$|^[0][7]\d{9}$|^[0][9]\d{9}$|^[\+][2][3][4][7]\d{9}$|^[\+][2][3][4][8]\d{9}$|^[\+][2][3][4][9]\d{9}$|^[2][3][4][7]\d{9}$|^[2][3][4][8]\d{9}$|^[2][3][4][9]\d{9}$'
            }
        ))

    email = forms.EmailField(
        max_length=100, label='Enter your email:', widget=forms.TextInput(
            attrs={
                'class': 'text-input error-handler email col-12',
                'placeholder': 'example@mymail.com',
                'name': 'email',
            }
        ))
    
    project_type = forms.CharField(
        required=True,
        label="Select A Project",
        widget=forms.Select (choices=PROJECT_CHOICES,
        attrs={
            'name': 'course',
            "class" : 'select-error-handler custom-select',
        }),
    )

    description = forms.CharField(
        max_length=100, label='Describe your project:', widget=forms.Textarea(
            attrs={
                'class': 'text-input error-handler home-address col-12 rounded-lg py-3',
                'placeholder': 'Describe what your project is all about briefly',
                'name': 'description'
            }
        ))

    class Meta:
        model = GetAQuote
        fields = ('name', 'phone_number', 'email', 'project_type', 'description')

    def clean_name(self):
        # Clean name
        first_name = self.cleaned_data.get("name")
        return first_name

    def clean_phone_number(self):
        # Clean phone_number
        phone_number = self.cleaned_data.get("phone_number")
        return phone_number

    def clean_email(self):
         # Clean email
        email = self.cleaned_data.get('email')
        return email

    def clean_project_type(self):
        # Clean project_type
        project_type = self.cleaned_data.get("project_type")
        return project_type

    def clean_description(self):
        # Clean description
        description = self.cleaned_data.get("description")
        return description