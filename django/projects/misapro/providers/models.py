from django.utils.translation import ugettext_lazy as _
from django.db import models
from main.models import Person
from accounts.models import Tenant
from condos.models import Condo

class Provider(Person):
	"""
	Provider Information.
	"""
	tenant = models.ForeignKey(Tenant,verbose_name=_('tenant')) 
	name = models.CharField(verbose_name=_('name'),max_length=200)
	services = models.CharField(verbose_name=_('services'),max_length=200)
	is_company = models.BooleanField(verbose_name=_('is company'),default=True) 

	# from main.models.Person
	# identifier = models.CharField(max_length=20,blank=True,unique=True)
	# identifier_type = models.CharField(max_length=20,blank=True)
	# nationality = models.ForeignKey(Country,on_delete=models.CASCADE)
	# gender = models.CharField(max_length=1,choices=GENDERS,default='N')
	# phone = models.CharField(max_length=20,blank=True,validators=[PhoneValidator])
	# celphone = models.CharField(max_length=20,blank=True,validators=[PhoneValidator])
	# email = models.EmailField(blank=True)
	# address = models.ForeignKey(Address,blank=True)
	# is_active = models.BooleanField(default=True)

	# from main.models.Timestamp
	# created = models.DateTimeField(auto_now_add=True) # Date & Time of object creation
	# updated = models.DateTimeField(auto_now=True) # Date & Time of object last modification

	class Meta:
		ordering = ['name','services']
		verbose_name = _('provider')
		verbose_name_plural = _('providers')

	def __str__(self):
		return self.name

class ProviderContact(Person):
	"""
	Provider Contact Information.
	"""
	provider = models.ForeignKey(Provider,on_delete=models.CASCADE,verbose_name=_('provider'))
	first_name = models.CharField(verbose_name=_('first name'),max_length=30,blank=True) 
	last_name = models.CharField(verbose_name=_('last name'),max_length=30,blank=True)
	job_function = models.CharField(verbose_name=_('job function title'),max_length=100) # Cargo
	job_function_desc = models.TextField(verbose_name=_('job function description'),blank=True)

	# from main.models.Person
	# identifier = models.CharField(max_length=20,blank=True,unique=True)
	# identifier_type = models.CharField(max_length=20,blank=True)
	# nationality = models.ForeignKey(Country,on_delete=models.CASCADE)
	# gender = models.CharField(max_length=1,choices=GENDERS,default='N')
	# phone = models.CharField(max_length=20,blank=True,validators=[PhoneValidator])
	# celphone = models.CharField(max_length=20,blank=True,validators=[PhoneValidator])
	# email = models.EmailField(blank=True)
	# address = models.ForeignKey(Address,blank=True)
	# is_active = models.BooleanField(default=True)

	# from main.models.Timestamp
	# created = models.DateTimeField(auto_now_add=True) # Date & Time of object creation
	# updated = models.DateTimeField(auto_now=True) # Date & Time of object last modification

	class Meta:
		ordering = ['first_name','last_name']
		verbose_name = _('provider contact')
		verbose_name_plural = _('provider contacts')

	def __str__(self):
		return self.last_name.upper() + ', ' + self.first_name + ' - ' + self.job_function

class CondoProvider(models.Model):
	"""
	Providers used on each Condominium.
	"""
	condo = models.ForeignKey(Condo, on_delete=models.CASCADE,verbose_name=_('condominium'))
	provider = models.ForeignKey(Provider,on_delete=models.CASCADE,verbose_name=_('provider'))
	service = models.CharField(verbose_name=_('service'),max_length=100)

	class Meta:
		verbose_name = _('provider')
		verbose_name_plural = _('providers')
