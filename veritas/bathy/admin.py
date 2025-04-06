from django.contrib import admin
from .models import SubmittedFile

class SubmittedFileAdmin(admin.ModelAdmin):
    list_display = ('filename', 'user', 'time_submitted', 'benchmark_ready', 'benchmark_date', 'benchmark_date')  # Columns to display in the admin list view
    list_filter =  ('filename', 'user', 'time_submitted', 'benchmark_ready', 'benchmark_date', 'benchmark_date')

admin.site.register(SubmittedFile, SubmittedFileAdmin)