from django.contrib import admin
from .models import ContactPage, VolunteerApplication
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class ContactPageResource(resources.ModelResource):
    class Meta:
        model = ContactPage
        fields = ('full_name', 'email', 'subject', 'message', 'date_sent')

class ContactPageAdmin(ImportExportModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'message', 'date_sent')
    resource_classes = [ContactPageResource]


class VolunteerApplicationResource(resources.ModelResource):
    class Meta:
        model = VolunteerApplication
        fields = (
            'first_name', 'last_name', 'preferred_name', 'email', 
            'street_address', 'city', 'state_or_province', 'country_of_origin', 
            'home_phone', 'mobile_phone', 'office_tel', 'gender', 'date_of_birth', 
            'nationality', 'preferred_program', 'education_or_experience',
            'health_conditions_disabilities', 'personalized_preferrences', 'travel_pack',
            'preferred_package', 'duration_of_stay', 'preferred_city', 'date_of_travel',
            'do_you_require_further_information', 'how_did_you_hear_about_us', 'any_other_comments',
            'emergency_contact_full_name', 'emergency_contact_telephone_no', 'emergency_contact_residential_address',
            'emergency_contact_relationship', 'referee_contact_full_name', 'referee_contact_organization',
            'referee_contact_telephone_no', 'referee_contact_work_address', 'date_of_application'
            )

class VolunteerApplicationAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'preferred_name', 'email', 'mobile_phone', 'date_of_application')
    resource_classes = [VolunteerApplicationResource]

admin.site.site_header = "ELAN Dome Consultants Administration"
admin.site.site_title = "ELAN Dome Consultants"
admin.site.register(ContactPage, ContactPageAdmin)
admin.site.register(VolunteerApplication, VolunteerApplicationAdmin)
