from django.test import TestCase

# Create your tests here.
from .models import Person


class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(first_name="krace", phone_no=123)

    def test_phone_no(self):
        p = Person.objects.get(first_name="krace")
        self.assertEquals(p.phone_no, u'123')
