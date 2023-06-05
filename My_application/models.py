from django.db import models
import datetime
import os


# Create your models here.
def getfilename(request,filename):
    nowtime=datetime.datetime.now().strftime("%d%m%y%H:%M:%S")
    newfilename="%s%s"%(nowtime,filename)
    return os.path.join('uploads/',newfilename)

class product(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    vender=models.CharField(max_length=500,null=False,blank=False)
    product_img=models.ImageField(upload_to=getfilename,null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    discription=models.CharField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    trending=models.BooleanField(default=False,help_text="0-defalt,1-trending")
    created_at=models.DateTimeField(auto_now_add=True)