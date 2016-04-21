from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Vault(models.Model):

	class Meta:
		db_table = 'vault'
		verbose_name = 'Credential'

	account = models.CharField(max_length=100,primary_key=True)
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=255)



	@classmethod
	def store(self,account,username,password):
		newacc = self(account=account,username=username,password=password)
		return newacc

	def __unicode__(self):
		return self.account


