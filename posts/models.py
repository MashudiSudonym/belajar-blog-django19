from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	# for python 3
	def __unicode__(self):
		return self.title

	# for python 2
	def __str__(self):
		return self.title
