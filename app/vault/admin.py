from django.contrib import admin
from .models import Vault 
# Register your models here.

class VaultAdmin(admin.ModelAdmin):
    list_display = ('account','account_type', 'username' , 'password')

admin.site.register(Vault,VaultAdmin)
