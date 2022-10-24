from django.db import models
from .countries import COUNTRIES

GENDER = (
    ('- Select -','- Select -'),
    ('Male','Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)

PROGRAMS = (
    ('- Select -','- Select -'),
    ('Volunteer Services','Volunteer Services'),
    ('Investment supervision, coordination and implementation', 'Investment supervision, coordination and implementation'),
    ('Project Management', 'Project Management'),
    ('Workshops & Training', 'Workshops & Training'),
    ('Career Counselling', 'Career Counselling')
)

TRAVEL_PAX = (
    ('- Select -','- Select -'),
    ('Individual', 'Individual'),
    ('Group', 'Group')
)

PACKAGES = (
    ('- Select -','- Select -'),
    ('Families', 'Families'),
    ('Friends', 'Friends'),
    ('Students', 'Students'),
    ('Employees', 'Employees'),
    ('Individuals', 'Individuals'),
    ('Teachers', 'Teachers')
)

HOW_DID_YOU_HEAR_ABOUT_US = (
    ('- Select -','- Select -'),
    ('Through a friend', 'Through a friend'),
    ('LinkedIn', 'LinkedIn'),
    ('Facebook', 'Facebook'),
    ('Instagram', 'Instagram'),
    ('Twitter', 'Twitter'),
    ('Blog Post', 'Blog Post'),
    ('Word of Mouth', 'Word of Mouth'),
    ('Email', 'Email'),
    ('Online Ad', 'Online Ad'),
    ('Other', 'Other')
)
# Create your models here.
class ContactPage(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"

class VolunteerApplication(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    preferred_name = models.CharField(max_length=100)
    email = models.EmailField()
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state_or_province = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=50, choices=COUNTRIES)
    home_phone = models.CharField(max_length=50)
    mobile_phone = models.CharField(max_length=50)
    office_tel = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=50)
    preferred_program = models.CharField(max_length=150, choices=PROGRAMS)


    education_or_experience = models.TextField(blank=True, null=True)
    health_conditions_disabilities = models.TextField(blank=True, null=True)
    personalized_preferrences = models.TextField(blank=True, null=True)
    travel_pack = models.CharField(max_length=50, choices=TRAVEL_PAX,blank=True, null=True)
    preferred_package = models.CharField(max_length=50, choices=PACKAGES,blank=True, null=True)
    duration_of_stay = models.CharField(max_length=100,blank=True, null=True)
    preferred_city = models.CharField(max_length=100,blank=True, null=True)
    date_of_travel = models.DateField(blank=True, null=True)
    do_you_require_further_information = models.TextField(blank=True, null=True)
    how_did_you_hear_about_us = models.CharField(max_length=100, choices=HOW_DID_YOU_HEAR_ABOUT_US, blank=True, null=True)
    any_other_comments = models.TextField(blank=True, null=True)

    # Emergency Contact Details
    emergency_contact_full_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_telephone_no = models.CharField(max_length=50, blank=True, null=True)
    emergency_contact_residential_address = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_relationship = models.CharField(max_length=100, blank=True, null=True)

    # Referee Contact Details
    referee_contact_full_name = models.CharField(max_length=100, blank=True, null=True)
    referee_contact_organization = models.CharField(max_length=100, blank=True, null=True)
    referee_contact_telephone_no = models.CharField(max_length=50, blank=True, null=True)
    referee_contact_work_address = models.CharField(max_length=100, blank=True, null=True)

    date_of_application = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email} - {self.date_of_application}"
