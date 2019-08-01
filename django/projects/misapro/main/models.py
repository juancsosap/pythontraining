from django.utils.translation import ugettext_lazy as _
from django.db import models
from .validators import PhoneValidator

"""
-----------------
ABSTRACTS CLASSES
-----------------
"""
class Timestamp(models.Model):
	# Date & Time of object creation
	created = models.DateTimeField(verbose_name=_('creation time'),auto_now_add=True)
	# Date & Time of object last modification
	updated = models.DateTimeField(verbose_name=_('last update time'),auto_now=True)

	class Meta:
		abstract = True

"""
-----------------------
ADDRESS RELATED CLASSES
-----------------------
"""
class Continent(models.Model):
	"""
	Continent code list
	"""

	name = models.CharField(verbose_name=_('continent name'),max_length=20)
	code = models.CharField(verbose_name=_('continent code'),max_length=2,unique=True)

	class Meta:
		ordering = ['code']
		verbose_name = _('continent')
		verbose_name_plural = _('continents')

	def __str__(self):
		return self.code + ': ' + self.name

class Country(models.Model):
	"""
	ISO 3166-1: Codes for the representation of names of countries and their subdivisions
	"""

	continent = models.ForeignKey(Continent,on_delete=models.CASCADE,verbose_name=_('continent'))
	name = models.CharField(verbose_name=_('country name'),max_length=50)
	alpha2 = models.CharField(verbose_name=_('alpha-2 country code'),max_length=2,unique=True)
	alpha3 = models.CharField(verbose_name=_('alpha-3 country code'),max_length=3,unique=True)
	numeric = models.IntegerField(verbose_name=_('numeric country code'),unique=True)

	class Meta:
		ordering = ['alpha2']
		verbose_name = _('country')
		verbose_name_plural = _('countries')

	def __str__(self):
		return self.alpha2 + '/' + self.alpha3 + ': ' + self.name

class Region(models.Model):
	"""
	Region or Estate List
	"""

	country = models.ForeignKey(Country,on_delete=models.CASCADE,verbose_name=_('country'))
	name = models.CharField(verbose_name=_('county name'),max_length=100)
	division = models.CharField(verbose_name=_('division'),max_length=20) # North, East, North-Weast
	code = models.CharField(verbose_name=_('county code'),max_length=10)
	
	class Meta:
		ordering = ['code']
		verbose_name = _('region')
		verbose_name_plural = _('regions')

	def __str__(self):
		return self.code + ': ' + self.name

class County(models.Model):
	"""
	County or Municipality List
	"""

	region = models.ForeignKey(Region,on_delete=models.CASCADE,verbose_name=_('region'))
	name = models.CharField(verbose_name=_('county name'),max_length=100)
	code = models.CharField(verbose_name=_('county code'),max_length=10)
	
	class Meta:
		ordering = ['code']
		verbose_name = _('county')
		verbose_name_plural = _('counties')

	def __str__(self):
		return self.code + ': ' + self.name

class Address(Timestamp):
	"""
	Address class used to refer to any class that require it.
	"""
	county = models.ForeignKey(County,on_delete=models.CASCADE,verbose_name=_('county'))
	city = models.CharField(verbose_name=_('city'),max_length=100)
	zone = models.CharField(verbose_name=_('zone'),max_length=100,blank=True) # Barrio
	zip_code = models.CharField(verbose_name=_('zip code'),max_length=15,blank=True)
	street = models.CharField(verbose_name=_('street'),max_length=100)
	number = models.CharField(verbose_name=_('number'),max_length=100)
	reference = models.TextField(verbose_name=_('reference'))
	
	class Meta:
		ordering = ['county','city']
		verbose_name = _('address')
		verbose_name_plural = _('addresses')

	def __str__(self):
		return self.street + ' ' + self.number + '. ' + self.county

"""
-----------------
PERSON CLASS
-----------------
"""
class Person(Timestamp):
	"""
	An abstract base class implementing all the basic parameters for natural or legal people. Some of them could be overwrite by other classes.
	"""
	GENDERS = (
		('M','Male'),
		('F','Female'),
		('I','Not specified'),
		('N','Not Aplly'),	
	)

	identifier = models.CharField(verbose_name=_('id number'),max_length=20,blank=True,unique=True)
	identifier_type = models.CharField(verbose_name=_('id type'),max_length=20,blank=True)
	nationality = models.ForeignKey(Country,on_delete=models.CASCADE,verbose_name=_('nationality'))
	gender = models.CharField(verbose_name=_('gender'),max_length=1,choices=GENDERS,default='N')
	phone = models.CharField(verbose_name=_('fixed phones'),max_length=20,blank=True,validators=[PhoneValidator])
	celphone = models.CharField(verbose_name=_('mobile phones'),max_length=20,blank=True,validators=[PhoneValidator])
	email = models.EmailField(verbose_name=_('email'),blank=True)
	address = models.ForeignKey(Address,verbose_name=_('address'),blank=True)
	is_active = models.BooleanField(verbose_name=_('active'),default=True)

	class Meta:
		abstract = True
		ordering = ['identifier']

	def __str__(self):
		return self.identifier_type + ':' + self.identifier

"""
-----------------------
UTILITARY CLASSES
-----------------------
"""
class Dictionary(models.Model):
	"""
	Dictionary for all App objects
	"""

	app = models.CharField(verbose_name=_('aplication'),max_length=50) # main
	ttype =  models.CharField(verbose_name=_('object type'),max_length=50) # menu
	code = models.CharField(verbose_name=_('object code'),max_length=50) # logout
	lang = models.CharField(verbose_name=_('languaje'),max_length=10) # es
	value = models.TextField(verbose_name=_('text')) # Salir
	
	class Meta:
		ordering = ['app','ttype','code','lang']
		verbose_name = _('dictionary')
		verbose_name_plural = _('dictionaries')

	def __str__(self):
		text = self.app + '.' + self.ttype + '.' + self.code + '.' + self.lang + ' -> "' + self.value + '"'
		return text 
