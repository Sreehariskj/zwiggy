from django.db import models

# Create your models here.
class Hotel(models.Model):
    hotel_name = models.CharField(max_length=200,null=False,blank=False)
    hotel_image = models.ImageField(upload_to='hotel_img',null=False,blank=False)
    hotel_cuisenes = models.CharField(max_length=200,null=False,blank=False)
    hotel_area = models.CharField(max_length=200,null=False,blank=False)
    hotel_distance = models.DecimalField(max_digits=3,decimal_places=1,null=False,blank=False)
    hotel_time = models.IntegerField(null=False,blank=False)
    hotel_rate = models.DecimalField(max_digits=3,decimal_places=1,null=False,blank=False)
    hotel_offer = models.IntegerField()
    
    def __str__(self):
        return self.hotel_name
       
         