from rest_framework.viewsets import ModelViewSet

from .models import Contact, OurPage, FAQ
from .serializers import ContactSerializer, OurPageSerializer, FAQSerializer


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class OurPageViewSet(ModelViewSet):
    queryset = OurPage.objects.all()
    serializer_class = OurPageSerializer


class FAQViewSet(ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
