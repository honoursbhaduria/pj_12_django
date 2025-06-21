from django.db import models


class UrlData(models.Model): 
    url = models.CharField(max_length=2000)   # Original long URL
    slug = models.CharField(max_length=20)    # Short slug

    def __str__(self):  
        return f"short URL for: {self.url} is {self.slug}"
