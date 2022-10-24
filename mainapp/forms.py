from django import forms
from crispy_forms.helper import FormHelper
from .models import ContactPage, VolunteerApplication, COUNTRIES, GENDER, TRAVEL_PAX, HOW_DID_YOU_HEAR_ABOUT_US, PROGRAMS, PACKAGES

class ContactPageForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Full name", "class":"form-control", "aria-label":"Full name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email", "class":"form-control", "aria-label":"Email"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Subject", "class":"form-control", "aria-label":"Subject"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"placholder":"Message", "class":"form-control", "rows": "5"}))
    
    def __init__(self, *args, **kwargs):
        super(ContactPageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 

    class Meta:
        model = ContactPage
        fields = '__all__'

class VolunteerApplicationForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"First Name", "class":"form-control", "aria-label":"First Name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Last Name", "class":"form-control", "aria-label":"Last Name"}))
    preferred_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Preferred Name", "class":"form-control", "aria-label":"Preferred Name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email", "class":"form-control", "aria-label":"Email"}))
    street_address = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Street Address","class":"form-control", "aria-label":"Street Address"}))
    city = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"City", "class":"form-control"}))
    state_or_province = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"State or Province", "class":"form-control"}))
    country_of_origin = forms.ChoiceField(choices=COUNTRIES, widget=forms.Select(attrs={"class":"form-control"}))
    home_phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Home Phone", "class":"form-control"}))
    mobile_phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Mobile Phone", "class":"form-control"}))
    office_tel = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Office Tel.", "class":"form-control"}))
    gender = forms.ChoiceField(choices=GENDER, widget=forms.Select(attrs={"class":"form-control", "class":"form-control"}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control", "id":"datepicker", "placeholder":"mm/dd/yyyy"}))
    nationality = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Nationality"}))
    preferred_program = forms.ChoiceField(choices=PROGRAMS, widget=forms.Select(attrs={"class":"form-control", "placeholder":"Preferred Program"}))


    education_or_experience = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder":"Add your resume here. 700 words max.", "rows":"7"}), required=False)
    health_conditions_disabilities = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "rows":"3", "placeholder":"Health conditions, disabilities etc."}), required=False)
    personalized_preferrences = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Type here...", "rows":"3"}), required=False)
    travel_pack = forms.ChoiceField(choices=TRAVEL_PAX, widget=forms.Select(attrs={"class":"form-control"}), required=False)
    preferred_package = forms.ChoiceField(choices=PACKAGES, widget=forms.Select(attrs={"class":"form-control"}), required=False)
    duration_of_stay = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Duration of stay", "class":"form-control"}), required=False)
    preferred_city =forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Preferred city"}), required=False)
    date_of_travel = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control", "id":"datepicker2", "placeholder":"mm/dd/yyyy"}), required=False)
    do_you_require_further_information = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder":"Type here...", "rows":"3"}), required=False)
    how_did_you_hear_about_us = forms.ChoiceField(choices=HOW_DID_YOU_HEAR_ABOUT_US, widget=forms.Select(attrs={"class":"form-control"}), required=False)
    any_other_comments = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder":"Type here...", "rows":"3"}), required=False)

    emergency_contact_full_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Full Name", "class":"form-control"}), required=False)
    emergency_contact_telephone_no = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Telephone No.", "class":"form-control"}), required=False)
    emergency_contact_residential_address = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Residential Address", "class":"form-control"}), required=False)
    emergency_contact_relationship = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Relationship", "class":"form-control"}), required=False)

    referee_contact_full_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Full Name", "class":"form-control"}), required=False)
    referee_contact_organization = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Organization", "class":"form-control"}), required=False)
    referee_contact_telephone_no = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Telephone No.", "class":"form-control"}), required=False)
    referee_contact_work_address = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Work Address", "class":"form-control"}), required=False)


    def __init__(self, *args, **kwargs):
        super(VolunteerApplicationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = VolunteerApplication
        fields = '__all__'