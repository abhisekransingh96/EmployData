from django.db import models
import uuid
from django.db.models.signals import post_save
from django.dispatch import  receiver
from django.contrib.auth.models import User
from .utils import send_email_client,send_email_with_attachemt
# Create your models here.



class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=70)
    salary=models.IntegerField()
    email=models.EmailField()
    pasword=models.CharField(max_length=8)
    con_password=models.CharField(max_length=8)

    def __str__(self):
        return  self.first_name

@receiver(post_save,sender=Employee)
def post_Emplyee_Save(sender,instance,**kwargs):
    data=User(first_name=instance.first_name,last_name=instance.last_name,username=str(instance.first_name)+str(instance.last_name),
              email=instance.email
              )
    data.save()
    # send_email_client(instance.first_name,str(instance.email))  #for normal emal function
    send_email_with_attachemt(instance.first_name,str(instance.email))


