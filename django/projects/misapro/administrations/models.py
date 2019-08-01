from django.utils.translation import ugettext_lazy as _
from django.db import models
from main.models import Timestamp, Person
from accounts.models import Tenant, MultiTenantUser

class Administration(Person):
	"""
	Administration Organization Details
	"""
	tenant = models.OneToOneField(Tenant,on_delete=models.CASCADE,verbose_name=_('tenant'))
	name = models.CharField(verbose_name=_('name'),max_length=30,blank=True) 
	logo = models.FilePathField(path=None,blank=True,verbose_name=_('logo image path'))

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
		verbose_name = _('administration')
		verbose_name_plural = _('administrations')

class AdminEmployee(Timestamp):
	"""
	Administration Employee Information
	"""
	tenant = models.ForeignKey(Tenant,verbose_name=_('tenant')) 
	user = models.ForeignKey(MultiTenantUser,verbose_name=_('employee user'),blank=True)
	employee_type = models.CharField(verbose_name=_('employee type'),max_length=20) # Fixed, Outsourcing
	job_function = models.CharField(verbose_name=_('job function title'),max_length=100) # Cargo : Ejecutivo de Cuenta
	job_function_desc = models.TextField(verbose_name=_('job function description'),blank=True)

	# from main.models.Timestamp
	# created = models.DateTimeField(auto_now_add=True) # Date & Time of object creation
	# updated = models.DateTimeField(auto_now=True) # Date & Time of object last modification
	
	class Meta:
		verbose_name = _('administration employee')
		verbose_name_plural = _('administration employees')

	def __str__(self):
		return self.user + ' - ' + self.job_function