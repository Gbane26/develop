from django.db import models

# Create your models here.

class Analysis(models.Model):
    user = models.CharField(max_length=100)  
    uploaded_file = models.FileField(upload_to='uploads/')  
    created_at = models.DateTimeField(auto_now_add=True)  
    selectors_removed = models.IntegerField(default=0)  
    size_saved = models.FloatField(default=0.0)  