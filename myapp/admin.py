from django.contrib import admin
from.models import registration

# Register your models here.
@admin.register(registration)
class regadmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'dob', 'gender', 'state', 'city', 'pin', 'mobile', 'email', 'job_location', 'image', 'file']