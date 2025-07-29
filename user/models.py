from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from .choices import MyUserRoleEnum
from django.db import models

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        user=self.model(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,email,password):
        user=self.create_user(username,email,password)
        user.is_admin=True
        user.set_password(password)
        user.save(using=self._db)

class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=150,verbose_name="Имя пользователя")
    email = models.EmailField(unique=True,verbose_name="Адрес электронной почты")
    avatar = models.ImageField(upload_to='media/avatars',null=True,blank=True)
    role = models.CharField(
        max_length=20,
        choices=(MyUserRoleEnum.choices),
        default=MyUserRoleEnum.STANDART_USER,
        verbose_name="Роль"
    )
    balance = models.DecimalField(max_digits=12, decimal_places=2,verbose_name="Баланс",default=0)
    is_admin = models.BooleanField(
        default=False
    )
    created_date = models.DateTimeField(auto_now_add=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.email} "

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin

class OTP(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    code = models.CharField(
        max_length=20,
    )
    created_date = models.DateTimeField(auto_now_add=True)