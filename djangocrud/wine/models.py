from django.db import models

# Create your models here.
class Wine(models.Model):
    wi_id = models.AutoField(primary_key=True)
    wi_name = models.CharField(max_length=100, verbose_name='Name')
    wi_image = models.ImageField(upload_to='images/', verbose_name='Image', null=True)
    wi_descrip = models.TextField(verbose_name='Description', null=True)

    def __str__(self):
        retstr = "Name: "+ self.wi_name +" - " + "Description: " +self.wi_descrip 
        return retstr
    
    def delete(self, using=None, keep_parents=False):
        self.wi_image.storage.delete(self.wi_image.name)
        super().delete()