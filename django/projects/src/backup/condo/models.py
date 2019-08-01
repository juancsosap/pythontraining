from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/1.11/ref/models/fields/

# Tenant Administrator
class Administration(models.Model):
	name = models.CharField(max_length=200)
	identifier = models.CharField(max_length=20)
	phone = models.CommaSeparatedIntegerField()
	celphone = models.CommaSeparatedIntegerField()
	email = models.EmailField()
	logo = models.FilePathField(path=None)
	is_active = models.BooleanField(default=True)
	
	created = models.DateTimeField(auto_now_add=True) # Date & Time of object creation
	updated = models.DateTimeField(auto_now=True) # Date & Time of object last modification

	def __str__(self):
		return self.name

class EmployeeAdmin(models.Model):
	admin = models.ForeignKey(Administration, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	identifier = models.CharField(max_length=20)
	phone = models.CommaSeparatedIntegerField()
	celphone = models.CommaSeparatedIntegerField()
	email = models.EmailField()
	employee_type = models.CharField(max_length=20) # Fixed, Outsourcing
	job_function = models.CharField(max_length=100) # Cargo : Ejecutivo de Cuenta
	job_function_desc = models.TextField()
	is_active = models.BooleanField(default=True)
	
	created = models.DateTimeField(auto_now_add=True) # Date & Time of object creation
	updated = models.DateTimeField(auto_now=True) # Date & Time of object last modification

	def __str__(self):
		return self.name + ' - ' + self.job_function

class User(models.Model):
	admin = models.ForeignKey(Administration, on_delete=models.CASCADE)
	user = models.CharField(max_length=100)
	email = models.EmailField()
	passwd = models.CharField(max_length=100)
	user_profile = models.CharField(max_length=50)
	person = models.IntegerField() # ID Administration Employee or Contact
	person_type = models.CharField(max_length=20) # Employee or Contact
	is_active = models.BooleanField(default=True)
	
	created = models.DateTimeField(auto_now_add=True) # Date & Time of object creation
	updated = models.DateTimeField(auto_now=True) # Date & Time of object last modification

	def __str__(self):
		return self.user

# Condo Objects
class Condo(models.Model):
	admin = models.ForeignKey(Administration, on_delete=models.CASCADE)
	name = models.CharField(max_length=250)
	identifier = models.CharField(max_length=20)
	clasification = models.CharField(max_length=50) # Building, Houses, Plots   
	photo = models.FilePathField(path=None)
	account_manager = models.IntegerField() # ID Administration Employee
	is_active = models.BooleanField(default=True)

	created = models.DateTimeField(auto_now_add=True) # Date & Time of object creation
	updated = models.DateTimeField(auto_now=True) # Date & Time of object last modification

	def __str__(self):
		return self.name
	
class Address(models.Model):
	condo = models.ForeignKey(Condo, default=1, on_delete=models.CASCADE)
	country = models.CharField(max_length=100)
	region = models.CharField(max_length=10) # Estado o Region
	city = models.CharField(max_length=100)
	county = models.CharField(max_length=100) # Comuna o Municipio
	zone = models.CharField(max_length=100) # Barrio
	zip_code = models.CharField(max_length=15)
	street = models.CharField(max_length=100)
	number = models.CharField(max_length=100)
	reference = models.TextField()
	
	created = models.DateTimeField(auto_now_add=True) # Date & Time of object creation
	updated = models.DateTimeField(auto_now=True) # Date & Time of object last modification

	def __str__(self):
		return self.street + ' ' + self.number + '. ' + self.county

class Property(models.Model):
	condo = models.ForeignKey(Condo, on_delete=models.CASCADE)
	zone = models.CharField(max_length=100)
	area = models.CharField(max_length=100)
	number = models.CharField(max_length=100)
	property_type = models.CharField(max_length=100) # Tipo Estudio, Duplex, Apareada, Marbella
	proration = models.DecimalField(max_digits=6, decimal_places=4)
	identifier = models.CharField(max_length=50)
	reference = models.TextField() # Other Info - Free
	
	created = models.DateTimeField(auto_now_add=True) # Date & Time of object creation
	updated = models.DateTimeField(auto_now=True) # Date & Time of object last modification

	def __str__(self):
		return self.zone + ' ' + self.area + ' ' + self.number

class Contact(models.Model):
	proper = models.ForeignKey(Property, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	identifier = models.CharField(max_length=20)
	phone = models.CommaSeparatedIntegerField()
	celphone = models.CommaSeparatedIntegerField()
	email = models.EmailField()
	contact_type = models.CharField(max_length=20) # Owner, Resident, Rented, Temporal
	
	created = models.DateTimeField(auto_now_add=True) # Date & Time of object creation
	updated = models.DateTimeField(auto_now=True) # Date & Time of object last modification

	def __str__(self):
		return self.name + '(' + self.status + ')'

class Owner(models.Model):
	proper = models.ForeignKey(Property, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	identifier = models.CharField(max_length=20)
	owner_type = models.CharField(max_length=20) # Natural o Juridica
	
	created = models.DateTimeField(auto_now_add=True) # Date & Time of object creation
	updated = models.DateTimeField(auto_now=True) # Date & Time of object last modification

	def __str__(self):
		return self.name

class Employee(models.Model):
	condo = models.ForeignKey(Condo, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	identifier = models.CharField(max_length=20)
	phone = models.CommaSeparatedIntegerField()
	celphone = models.CommaSeparatedIntegerField()
	email = models.EmailField()
	employee_type = models.CharField(max_length=20) # Fixed, Outsourcing
	job_function = models.CharField(max_length=100) # Cargo
	job_function_desc = models.TextField()
	is_active = models.BooleanField(default=True)
	
	created = models.DateTimeField(auto_now_add=True) # Date & Time of object creation
	updated = models.DateTimeField(auto_now=True) # Date & Time of object last modification

	def __str__(self):
		return self.name + ' - ' + self.job_function
"""
class salary(models.Model):
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	isapre = models.CharField(max_length=200)
	afp = models.CharField(max_length=20)
	
	created = models.DateTimeField(auto_now_add=True) # Date & Time of object creation
	updated = models.DateTimeField(auto_now=True) # Date & Time of object last modification

	def __str__(self):
		return self.name + ' - ' + self.job_function
"""
# Admin Provider
class Provider(models.Model):
	admin = models.ForeignKey(Administration, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	identifier = models.CharField(max_length=20)
	services = models.TextField() #----> pasar a lista
	phone = models.CommaSeparatedIntegerField()
	celphone = models.CommaSeparatedIntegerField()
	email = models.EmailField()
	is_company = models.BooleanField(default=True) 
	is_active = models.BooleanField(default=True)
	
	created = models.DateTimeField(auto_now_add=True) # Date & Time of object creation
	updated = models.DateTimeField(auto_now=True) # Date & Time of object last modification

	def __str__(self):
		return self.name

class ProviderContact(models.Model):
	provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	function = models.CharField(max_length=100)
	function_desc = models.TextField()
	phone = models.CommaSeparatedIntegerField()
	celphone = models.CommaSeparatedIntegerField()
	email = models.EmailField()
	is_active = models.BooleanField(default=True)
	
	created = models.DateTimeField(auto_now_add=True) # Date & Time of object creation
	updated = models.DateTimeField(auto_now=True) # Date & Time of object last modification

	def __str__(self):
		return self.name + ' - ' + self.function

class Provider(models.Model):
	condo = models.ForeignKey(Condo, on_delete=models.CASCADE)
	provider = models.ForeignKey(ProviderAdmin, on_delete=models.CASCADE)
	
	



# Finantial Objects
class Expense(models.Model):
	condo = models.ForeignKey(Condo, on_delete=models.CASCADE)
	provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
	service = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	amount = models.DecimalField(max_digits=15, decimal_places=2)
	date = models.DateField()
	was_paid = models.BooleanField(default=True)

	created = models.DateTimeField(auto_now_add=True) # Date & Time of object creation
	updated = models.DateTimeField(auto_now=True) # Date & Time of object last modification

	def __str__(self):
		return self.date + ' - ' + self.service

class Fund(models.Model):
	condo = models.ForeignKey(Condo, on_delete=models.CASCADE)
	mission = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	amount = models.DecimalField(max_digits=15, decimal_places=2)
	date = models.DateField()

	created = models.DateTimeField(auto_now_add=True) # Date & Time of object creation
	updated = models.DateTimeField(auto_now=True) # Date & Time of object last modification

	def __str__(self):
		return self.date + ' - ' + self.service

class FinesPolicy(models.Model):
	condo = models.ForeignKey(Condo, on_delete=models.CASCADE)
	percentage = models.DecimalField(max_digits=4, decimal_places=2)
	date = models.DateField()

	created = models.DateTimeField(auto_now_add=True) # Date & Time of object creation
	updated = models.DateTimeField(auto_now=True) # Date & Time of object last modification

	def __str__(self):
		return self.percentage + ' - ' + self.date    

class Report(models.Model):
	condo = models.ForeignKey(Condo, on_delete=models.CASCADE)
	date = models.DateField()

	created = models.DateTimeField(auto_now_add=True) # Date & Time of object creation
	updated = models.DateTimeField(auto_now=True) # Date & Time of object last modification

	def __str__(self):
		return self.date + ' - ' + self.service

class ReportItem(models.Model):
	report = models.ForeignKey(Report, on_delete=models.CASCADE)
	date = models.DateField()
	amount = models.DecimalField(max_digits=15, decimal_places=2)
	item_type = models.CharField(max_length=50) # Expenditure, Fund, 

	created = models.DateTimeField(auto_now_add=True) # Date & Time of object creation
	updated = models.DateTimeField(auto_now=True) # Date & Time of object last modification

	def __str__(self):
		return self.date + ' - ' + self.service

# System Objects
class Log(models.Model):
	user = models.ForeignKey(User)
	element = models.CharField(max_length=100)
	action = models.CharField(max_length=50)
	detail = models.TextField()
	time = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.time + ' - ' + self.element + ' : ' + self.action 
