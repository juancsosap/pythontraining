from django.utils.translation import ugettext_lazy as _
from django.db import models
from main.models import Timestamp, Person, Address
from administrations.models import Administration, AdminEmployee

class Condo(Timestamp):
	"""
	Condominium Information.
	"""
	admin = models.ForeignKey(Administration,on_delete=models.CASCADE,verbose_name=_('administration'))
	manager = models.ForeignKey(AdminEmployee,on_delete=models.CASCADE,verbose_name=_('account manager'))
	name = models.CharField(verbose_name=_('name'),max_length=250)
	identifier = models.CharField(verbose_name=_('identifier'),max_length=20, blank=True)
	clasification = models.CharField(verbose_name=_('identifier'),max_length=50) # Building, Houses, Plots   
	photo = models.FilePathField(verbose_name=_('photo path'),path=None,blank=True)
	address = models.ForeignKey(Address,verbose_name=_('address'),blank=True)
	is_active = models.BooleanField(default=True)

	# from main.models.Timestamp
	# created = models.DateTimeField(auto_now_add=True) # Date & Time of object creation
	# updated = models.DateTimeField(auto_now=True) # Date & Time of object last modification

	class Meta:
		verbose_name = _('condominium')
		verbose_name_plural = _('condos')

	def __str__(self):
		return self.name + '-' + selft.clasification	

class Employee(Person):
	"""
	Condominium Information.
	"""
	condo = models.ForeignKey(Condo,on_delete=models.CASCADE,verbose_name=_('condominium'))
	first_name = models.CharField(verbose_name=_('first name'),max_length=30,blank=True) 
	last_name = models.CharField(verbose_name=_('last name'),max_length=30,blank=True)
	employee_type = models.CharField(verbose_name=_('employee type'),max_length=20) # Fixed, Outsourcing
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
		verbose_name = _('condominium employee')
		verbose_name_plural = _('condominium employees')

	def __str__(self):
		return self.last_name.upper() + ', ' + self.first_name + ' - ' + self.job_function
