from rest_framework import serializers

from .models import FAQ, Contact, OurPage


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class OurPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurPage
        fields = '__all__'
