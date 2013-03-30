from django.db import models
from customauth.models import MyUser

class Contact(models.Model):
    user = models.ForeignKey(MyUser)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    contact_user = models.ForeignKey(MyUser, related_name='contacted_me', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.contact_user:
            matches = MyUser.objects.filter(full_number=self.phone_number)

            if matches:
                self.contact_user = matches[0]
        
        return super(Contact, self).save(*args, **kwargs)
