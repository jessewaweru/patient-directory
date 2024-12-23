from rest_framework import serializers
from .models import Patient
from .validators import (
    validate_email,
    validate_password,
    validate_phone_number,
    validate_username,
)


class PatientSerializer(serializers.ModelSerializer):
    username = serializers.CharField(validators=[validate_username])
    email = serializers.EmailField(validators=[validate_email])
    phone_number = serializers.CharField(validators=[validate_phone_number])
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = Patient
        fields = [
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "phone_number",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"read_only": True},  # email is now read-only, it can't be updated
        }

    def create(self, validated_data):
        # Hashing the password before saving the user
        user = Patient.objects.create_user(**validated_data)
        return user
