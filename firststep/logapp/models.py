from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.contrib.auth.models import User

class MyAccount(BaseUserManager):
    def create_user(self, first_name, last_name, address, email, contact, city, state, pincode, password=None):
        if not email:
            raise ValueError('User must have an email address')

    

        user = self.model(
            email = self.normalize_email(email),
            # username = username,
            first_name = first_name,
            last_name = last_name,
            address = address,
            contact = contact,
            city = city,
            state = state,
            pincode = pincode

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_superuser(self,password,email,**extra_feilds):
        user = self.create_user(
            email = self.normalize_email(email),
            # username = username,
            **extra_feilds,
            password = password,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


 
class Account(AbstractBaseUser, PermissionsMixin):
    id              = models.AutoField(primary_key=True)
    first_name      = models.CharField(max_length=50, default='')
    last_name       = models.CharField(max_length=50, default='') 
    address         = models.CharField(max_length=100) 
    email           = models.CharField(max_length=200,unique=True)
    contact         = models.BigIntegerField(default=0)
    city            = models.CharField(max_length=50, default='')
    state           = models.CharField(max_length=50, default='')
    pincode         = models.BigIntegerField(default=0)
    password        = models.CharField(max_length=200)


    # required
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_user         = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_superadmin   = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','address','contact','city','state','pincode','password']
    # REQUIRED_FIELDS = ['password']




    objects = MyAccount()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True




















































# class user_reg(models.Model):


#     first_name      = models.CharField(max_length=50, default='')
#     last_name       = models.CharField(max_length=50, default='') 
#     address         = models.CharField(max_length=100) 
#     email           = models.CharField(max_length=200,unique=True)
#     contact         = models.BigIntegerField(default=0)
#     city            = models.CharField(max_length=50, default='')
#     district        = models.CharField(max_length=50, default='')
#     pincode         = models.BigIntegerField(default=0)
#     password        = models.CharField(max_length=200)


#     def __str__(self):
#          return self.email


# #Login Table
# class user_log(models.Model):
#      email    = models.CharField(max_length=200,primary_key=True,unique=True)
#      password = models.CharField(max_length=200)











































































































































