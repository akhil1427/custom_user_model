from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.
class UserProfileManager(BaseUserManager):
    def create_user(self,Email,First_name,Last_name,password=None):
        if not Email:
            raise ValueError('provide proper email')
        N_E=self.normalize_email(Email)
        UO=self.model(Email=N_E,First_name=First_name,Last_name=Last_name)
        UO.set_password(password)
        UO.save()
        return UO
    def create_superuser(self,Email,First_name,Last_name,password):
        UP=self.create_user(Email,First_name,Last_name,password)
        UP.is_superuser=True
        UP.is_staff=True
        UP.save()
        return UP
    


class UserProfile(AbstractBaseUser,PermissionsMixin):
    Email=models.EmailField(primary_key=True)
    First_name=models.CharField(max_length=150)
    Last_name=models.CharField(max_length=150)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    objects=UserProfileManager()
    USERNAME_FIELD='Email'
    REQUIRED_FIELDS=['First_name','Last_name']

