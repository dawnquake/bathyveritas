from django.db import models
from django.contrib.auth.models import User

class SubmittedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who submitted the file
    filename = models.CharField(max_length=255)  # Filename
    submitted_file = models.FileField(upload_to='submitted_files/')  # File submission
    time_submitted = models.DateTimeField(auto_now_add=True)  # Time of submission
    benchmark_ready = models.CharField(max_length=255, default='Not Ready')  # If Benchmark is ready
    benchmark_date = models.DateField(null=True, blank=True, default=None)  # Nullable result date
    benchmark_version = models.CharField(max_length=50, null=True, blank=True, default=None)  # Nullable benchmark version
    plot1 = models.ImageField(upload_to='plots/', null=True, blank=True, default=None)  # Nullable plot1
    plot2 = models.ImageField(upload_to='plots/', null=True, blank=True, default=None)  # Nullable plot2
    plot3 = models.ImageField(upload_to='plots/', null=True, blank=True, default=None)  # Nullable plot3
    plot4 = models.ImageField(upload_to='plots/', null=True, blank=True, default=None)  # Nullable plot4

    def __str__(self):
        return f"{self.user.username} - {self.filename}"
