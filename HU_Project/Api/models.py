from django.db import models
#from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

# Create your models here.
class Issues(models.Model):
    IssueId = models.AutoField(primary_key=True)
    IssueTitle = models.CharField(max_length=250)
    IssueDescription = models.CharField(max_length=350)
    IssueAssignee = models.CharField(max_length=150)
    IssueReporter = models.CharField(max_length=150)

class Project(models.Model):
    ProjectId = models.AutoField(primary_key=True)
    ProjectName = models.CharField(max_length=250)
    ProjectDescription = models.CharField(max_length=350)
    ProjectAssignee = models.CharField(max_length=150)
    ProjectReporter = models.CharField(max_length=150)



