from .models import Certificate, CertifyingInstitution, Profile, Project
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = CertificateSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        fields = "__all__"

    def create(self, validated_data):
        certificates_data = validated_data.pop('certificate_set')
        print(certificates_data)
        institution = CertifyingInstitution.objects.create(**validated_data)
        for certificate_data in certificates_data:
            Certificate.objects.create(
                certifying_institution=institution, **certificate_data)
        return institution
