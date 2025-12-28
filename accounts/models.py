import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save
from django.utils import timezone
from django.dispatch import receiver
from username_generator import get_uname

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('An email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user must have is_superuser=True')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super user must have is_staff=True')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Super user must have is_active=True')
        
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(unique=True)
    bio = models.CharField(max_length=70, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def user_joined_recently(self):
        return (timezone.now() - self.date_joined).days < 30

@receiver(post_save, sender=CustomUser)
def generate_username(sender, instance, created, **kwargs):
    if created:
        generated_username = get_uname(min_size=10, max_size=25, underscores=True)
        user = CustomUser.objects.filter(username=instance.username).first()

        if user.username == None:
            user.username = generated_username
            user.save()
        elif user.username != None:
            if 'user' in user.username:
                user.username = generated_username
                user.save()
        else:
            user.username = generated_username
            user.save()
            
