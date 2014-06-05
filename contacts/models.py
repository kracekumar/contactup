from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default=u'')
    phone_no = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField(default=u'')

    def __unicode__(self):
        return u"{}: {}".format(self.id, self.first_name)


class ExtraDetail(models.Model):
    person = models.OneToOneField(Person)
    website = models.URLField(default=u'')
    notes = models.TextField()
    birthday = models.DateField(null=True)
    relationship = models.CharField(max_length=100, default=u'')

    def __unicode__(self):
        return u"{}: {}".format(self.id, self.person)
