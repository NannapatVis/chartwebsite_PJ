from django.db import models

class Student1(models.Model):
    Order = models.IntegerField()
    Course = models.CharField(max_length=10) 
    Std_no = models.IntegerField()
    Std_name = models.CharField(max_length=30) 
    Std_state = models.CharField(max_length=15) 
    End_year = models.PositiveIntegerField(blank=True)
    Std_plan = models.CharField(max_length=20,blank=True)
    Prof_main = models.CharField(max_length=30,blank=True)
    Prof_Sec = models.CharField(max_length=30,blank=True) 
    Work_name = models.CharField(max_length=200,blank=True)
    Publish_type = models.CharField(max_length=30,blank=True)
    Journal_db = models.CharField(max_length=50,blank=True)
    Implementation = models.CharField(max_length=400,blank=True)
    Journal_name = models.CharField(max_length=300,blank=True)
    Date_start = models.DateField(blank=True)
    Date_End = models.DateField(blank=True)
    Cal_year = models.PositiveIntegerField(blank=True)

   



