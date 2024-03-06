from .models import Certificate, CertifyingInstitution, Profile, Project
from django.contrib import admin


admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(CertifyingInstitution)
admin.site.register(Certificate)
