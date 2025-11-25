from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomerManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email,  **extra_fields)
        user.set_password(password)

        # print(user.last_login)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, username, password, **extra_fields)


class Customer(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    
    email = models.EmailField(unique=True, max_length=200)
   
    phone_number = models.CharField(max_length=10, unique=True)
    city = models.CharField(max_length=200)
    dob = models.DateField(blank=True, null=True)

    #profile image
    profile_image = models.ImageField(
        # upload_to="profile_images/",
        # default="profile_images/default.png"
        upload_to= "",
        default='images/profile1.jpg',
        blank=True,
    null=True
     )


    # Required Django fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    objects = CustomerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
