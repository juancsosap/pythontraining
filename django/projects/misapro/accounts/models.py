from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth import get_backends
from django.contrib.auth.models import PermissionsMixin, Group, Permission, _user_has_perm, _user_get_all_permissions, _user_has_module_perms
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.mail import send_mail
from main.models import Person


# Django Libraries
from django.contrib.auth.models import User
# Custom Libraries
from main.models import Person

class FullUser(User,Person):

	nick = models.CharField(verbose_name=_('nick'), max_length=30)
	
	# from django.contrib.auth.models.AbstractUser
	# username = models.CharField(_('username'),max_length=150,unique=True,validators=[username_validator])
    # first_name = models.CharField(_('first name'), max_length=30, blank=True)
    # last_name = models.CharField(_('last name'), max_length=30, blank=True)
    # email = models.EmailField(_('email address'), blank=True)
    # is_staff = models.BooleanField(_('staff status'),default=False)
    # is_active = models.BooleanField(_('active'),default=True)
    # date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

	# from django.contrib.auth.models.AbstractBaseUser
	# password = models.CharField(max_length=128)
	# last_login = models.DateTimeField(blank=True, null=True)
	# is_active = True
	# def is_authenticated(self):
	# def set_password(self, raw_password):
	# def check_password(self, raw_password):

	# from django.contrib.auth.models.PermissionsMixin
	# is_superuser = models.BooleanField(default=False)
	# groups = models.ManyToManyField(Group,blank=True)
	# user_permissions = models.ManyToManyField(Permission,blank=True)

	# from main.models.Person
	# identifier = models.CharField(max_length=20, blank=True)
	# identifier_type = models.CharField(max_length=20, blank=True)
	# nationality = models.ForeignKey(Country,on_delete=models.CASCADE)
	# gender = models.CharField(max_length=1,choices=GENDERS)
	# phone = models.CharField(,max_length=20,blank=True,validators=[PhoneValidator])
	# celphone = models.CharField(max_length=20,blank=True,validators=[PhoneValidator])
	# email = models.EmailField(verbose_name=_('email'),blank=True)
	# address = models.ForeignKey(Address,blank=True)
	# is_active = models.BooleanField(default=True)

	class Meta:
		ordering = ['username']
		verbose_name = _('user')
		verbose_name_plural = _('users')






class Tenant(models.Model):
	"""
	Tenants are a generic way of separate users and restextources. A user o resourse only could belong to one tenant. The name of a specific resource could be repited between tenants.
	"""
	name = models.CharField(verbose_name=_('name'), max_length=80, unique=True)
	is_active = models.BooleanField(verbose_name=_('active'),default=True)

	class Meta:
		verbose_name = _('tenant')
		verbose_name_plural = _('tenants')

	def __str__(self):
		return self.name


class Log(models.Model):
	"""
	User Log information for Tenants.
	"""
	user = models.ForeignKey(FullUser,verbose_name=_('user'))
	element = models.CharField(max_length=100,verbose_name=_('object affected'))
	action = models.CharField(max_length=50,verbose_name=_('action'))
	detail = models.TextField(verbose_name=_('detail'),blank=True)
	time = models.DateTimeField(verbose_name=_('time'),auto_now_add=True)
	
	class Meta:
		verbose_name = _('log')
		verbose_name_plural = _('logs')

	def __str__(self):
		return self.time + ' - ' + self.element + ' : ' + self.action 
