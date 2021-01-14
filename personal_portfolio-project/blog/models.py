from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=100)
	preview = models.TextField()
	image = models.ImageField(upload_to='blogs/images')
	date = models.DateField()

	def __str__(self):
		return self.title