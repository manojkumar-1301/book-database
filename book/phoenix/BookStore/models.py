from django.db import models
from django.utils.timezone import now


# Create your models here.
class UserModel(models.Model):
    username=models.CharField(max_length=300)
    userid=models.CharField(max_length=200)
    password=models.IntegerField()
    mobilenumber=models.IntegerField()
    email=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)


class BookDetail(models.Model):
    Book_Name=models.CharField(max_length=300)
    Book_Code=models.CharField(max_length=300)
    Author_Name=models.CharField(max_length=300)
    Date=models.DateTimeField(default=now)
    Status=models.CharField(max_length=300)
    Created_By=models.IntegerField(null=True,blank=True)
    Created_Date=models.DateTimeField(default=now)



class OrderDetail(models.Model):
    Book_Id=models.ForeignKey(BookDetail,on_delete=models.SET_NULL,null=True)
    Total_Count=models.IntegerField(null=True,blank=True)
    Total_Price=models.DecimalField(max_digits=20,decimal_places=2,default=0.00)
    Delivery_Date=models.DateTimeField(null=True,blank=True)
    Status=models.CharField(max_length=200)
    Created_By=models.IntegerField(null=True,blank=True)
    Created_Date=models.DateTimeField(default=now)

