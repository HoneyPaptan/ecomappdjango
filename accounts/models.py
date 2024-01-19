from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User

#for signals
from django.dispatch import receiver
from django.db.models.signals import post_save
import uuid
from base.emails import send_account_activation_email
# Create your models here.


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    email_token = models.CharField(max_length = 100, null=True, blank = True )
    is_verified = models.BooleanField(default = False)
    image = models.ImageField(upload_to="profile")


@receiver(post_save, sender = User)
def send_verification_email(sender, instance, created, **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())

            Profile.objects.create(user=instance , email_token = email_token)
            email = instance.email
            send_account_activation_email(email, email_token)
    except Exception as e:
        print(e)



