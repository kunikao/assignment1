from rest_framework import serializers
from .models import User, MainForm

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']  # Add more fields as needed for registration

    def create(self, validated_data):
        # Override create method if additional logic is needed
        user = User.objects.create_user(**validated_data)
        return user

class MainFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainForm
        fields = '__all__'  # Include all fields from MainForm model

    def validate(self, data):
        # Implement any custom validation logic here
        return data

    def create(self, validated_data):
        # Override create method if needed
        main_form = MainForm.objects.create(**validated_data)
        return main_form

