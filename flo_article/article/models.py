from django.db import models
from datetime import datetime

# Create your models here.
class Blogpost(models.Model):
	post_id=models.AutoField(primary_key=True)
	author_name=models.CharField(max_length=50)
	headline=models.CharField(max_length=500,default='')
	sub_heading=models.CharField(max_length=500,default='')
	chead1=models.CharField(max_length=5000,default='')
	pub_date=models.DateTimeField(default=datetime.now)
	#thumbnail=models.ImageField(upload_to='article/images',default="")

	class Meta:
		ordering=['-pub_date']

	def __str__(self):
		return self.author_name