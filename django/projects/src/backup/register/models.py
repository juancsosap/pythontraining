from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=200)
	surname = models.CharField(max_length=200)
	email = models.EmailField()
	gender = models.CharField(max_length=1)
	photo = models.FilePathField(path=None)
	passwd = models.CharField(max_length=64) # Password Hash

	def __str__(self):
		return '%s, %s (%s)' % (self.surname.upper(), self.name, self.gender)

class Register(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	message = models.TextField()
	reference = models.CharField(max_length=50)

	def __str__(self):
		return 'User %s' % (str(self.user))