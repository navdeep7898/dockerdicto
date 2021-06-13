from dictionary.settings import MEDIA_URL
from django.db import models

# Create your models here.
class Words(models.Model):
    eword = models.CharField(max_length=30 )
    hword = models.CharField(max_length=30)
    uses = models.TextField()
    category = models.CharField(max_length=80,null=True, blank=True,default=None)
    image = models.ImageField(upload_to="media/")
    rword = models.TextField()

    def __str__(self):
        return self.eword    
    
    class Meta:
        db_table = "Words"


    
    