from django.utils.translation import ugettext_lazy as _
from django.db import models
from main.models import Timestamp, Person
from condos.models import Condo

class Property(Timestamp):
	"""
	Property Information.
	"""
	condo = models.ForeignKey(Condo,on_delete=models.CASCADE,verbose_name=_('condominium'))
	identifier = models.CharField(verbose_name=_('property identifier'),max_length=50,blank=True)
	zone = models.CharField(verbose_name=_('property zone'),max_length=100,blank=True)
	area = models.CharField(verbose_name=_('property area'),max_length=100,blank=True)
	number = models.CharField(verbose_name=_('property number'),max_length=100)
	property_type = models.CharField(verbose_name=_('property type'),max_length=100) # Tipo Estudio, Duplex, Apareada, Marbella
	proration = models.DecimalField(verbose_name=_('property proration'),max_digits=6,decimal_places=4)
	extras = models.TextField(verbose_name=_('aditional information'),blank=True) # Other Info - Free
	
	# from main.models.Timestamp
	# created = models.DateTimeField(auto_now_add=True) # Date & Time of object creation
	# updated = models.DateTimeField(auto_now=True) # Date & Time of object last modification

	class Meta:
		ordering = ['zone','area','number']
		verbose_name = _('property')
		verbose_name_plural = _('properties')

	def __str__(self):
		return self.zone + ' ' + self.area + ' ' + self.number

class Contact(Person):
	"""
	Property Contact Information.
	"""
	proper = models.ForeignKey(Property,on_delete=models.CASCADE,verbose_name=_('property'))
	first_name = models.CharField(verbose_name=_('first name'),max_length=30,blank=True) 
	last_name = models.CharField(verbose_name=_('last name'),max_length=30,blank=True)
	contact_type = models.CharField(verbose_name=_('contact type'),max_length=20) # Owner, Resident, Rented, Temporal

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
		ordering = ['contact_type','first_name','last_name']
		verbose_name = _('property contact')
		verbose_name_plural = _('property contacts')

	def __str__(self):
		return self.last_name.upper() + ', ' + self.first_name + ' - ' + self.contact_type

class Owner(Timestamp):
	"""
	Property Owner Information.
	"""
	proper = models.ForeignKey(Property, on_delete=models.CASCADE,verbose_name=_('property'))
	name = models.CharField(verbose_name=_('property'),max_length=200)
	identifier = models.CharField(verbose_name=_('identifier'),max_length=20)
	owner_type = models.CharField(verbose_name=_('owner type'),max_length=20) # Natural o Juridica
	
	# from main.models.Timestamp
	# created = models.DateTimeField(auto_now_add=True) # Date & Time of object creation
	# updated = models.DateTimeField(auto_now=True) # Date & Time of object last modification

	class Meta:
		verbose_name = _('property owner')
		verbose_name_plural = _('property owners')

	def __str__(self):
		return self.last_name.upper() + ' (' + self.owner_type + ')'
