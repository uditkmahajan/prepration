from django.db import models
from django.db.models.base import Model
from ckeditor.fields import RichTextField, RichTextFormField
from django.contrib.postgres.fields import JSONField


class Jee(models.Model) :
    Name=models.CharField(max_length=200,default="20")
    Year=models.IntegerField(default=0)
    Pdf=models.FileField(upload_to="exercise/previous_papers/Jee")
    def __str__(self) :
        return self.Name+" "+str(self.Year)

class Neet(models.Model) :
    Name=models.CharField(max_length=200,default="20")
    Year=models.IntegerField(default=0)
    Pdf=models.FileField(upload_to="exercise/previous_papers/Neet")
    def __str__(self) :
        return self.Name+" "+str(self.Year)

# class Previous_paper(models.Model) :
#      Name=models.CharField(max_length=20,choices=NAME_CHOICES,default="GATE")
#      Category=models.CharField(max_length=100,choices=CAT_CHOICES)
#      Year=models.IntegerField(default=0)
#      Part=models.IntegerField(default=1)
#      Paper=models.FileField(upload_to='previous_papers/', null=True, blank=True)
#      content=RichTextField(blank=True)

#      def __str__(self) : 
#          return self.Name+" "+self.Category+" "+"Year -"+str(self.Year)+" "+"Part -"+str(self.Part)

# class Question(models.Model) :
#     qid=models.CharField(max_length=20,default="")
#     paper=models.ForeignKey(Previous_paper,on_delete=models.CASCADE)
#     title=RichTextField(blank=True)

# class json(models.Model) :
#     data = JSONField(default={})
