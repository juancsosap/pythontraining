from django.db import models

# Create your models here.
class Join(models.Model):
	email = models.EmailField(max_length=250)
	full_name = models.CharField(max_length=250, null=True, blank=True)
	zip_code = models.IntegerField(default=0)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return self.email	