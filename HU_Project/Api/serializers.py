#from django.core import serializers as core_serializers
#from django.core import serializers
from rest_framework import serializers
from Api.models import Issues,Project


class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Issues
        fields=('IssueId','IssueTitle','IssueDescription','IssueAssignee','IssueReporter')


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=('ProjectId','ProjectName','ProjectDescription','ProjectAssignee','ProjectReporter')