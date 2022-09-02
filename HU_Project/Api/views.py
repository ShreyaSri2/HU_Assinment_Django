from logging import raiseExceptions
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Api.models import Issues,Project
from Api.serializers import IssuesSerializer,ProjectsSerializer

from rest_framework.permissions import IsAuthenticated,BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

@csrf_exempt
def issuesApi(request,id=0):
    if request.method=='GET':
        issues = Issues.objects.all()

        title=request.GET.get('title', None)
        reporter=request.GET.get('reporter', None)
        if title is not None and reporter is not None:
            issues = issues.filter(IssuesTitle=title) & issues.filter(IssueReporter=reporter)
        elif title is not None or reporter is not None:
            issues = issues.filter(IssuesTitle=title) | issues.filter(IssueReporter=reporter)
        elif title is not None:
            #issues = issues.filter(name__icontains=name)
            issues = issues.filter(IssueTitle=title)
        elif reporter is not None:
            issues = issues.filter(IssueReporter=reporter)

        issues_serializer=IssuesSerializer(issues,many=True)
        return JsonResponse(issues_serializer.data,safe=False)
    elif request.method=='POST':
        issues_data=JSONParser().parse(request)
        issues_serializer=IssuesSerializer(data=issues_data)
        if issues_serializer.is_valid():
            issues_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        issues_data=JSONParser().parse(request)
        issue=Issues.objects.get(IssueId=issues_data['IssueId'])
        issues_serializer=IssuesSerializer(issue,data=issues_data)
        if issues_serializer.is_valid():
            issues_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")


@csrf_exempt
def issues_detail(request, id):
    if request.method=='GET':
        issues=Issues.objects.get(IssueId=id)
        issues_serializer=IssuesSerializer(issues)
        return JsonResponse(issues_serializer.data,safe=False)
    elif request.method=='DELETE':
        issue=Issues.objects.get(IssueId=id)
        issue.delete()
        return JsonResponse("Deleted Successfully",safe=False)



@csrf_exempt
def projectsApi(request,id=0):
    if request.method=='GET':
        projects = Project.objects.all()

        dd=request.GET.get('dd', None)
        name=request.GET.get('name', None)
        assignee=request.GET.get('assignee', None)
        if name is not None and assignee is not None:
            projects = projects.filter(ProjectName=name) & projects.filter(ProjectAssignee=assignee)
        elif name is not None or assignee is not None:
            projects = projects.filter(ProjectName=name) | projects.filter(ProjectAssignee=assignee)
        elif name is not None:
            #projects = projects.filter(title__icontains=title)
            projects = projects.filter(ProjectName=name)
        elif assignee is not None:
            projects = projects.filter(ProjectAssignee=assignee)
        elif dd is not None:
            return dd

        projects_serializer=ProjectsSerializer(projects,many=True)
        return JsonResponse(projects_serializer.data,safe=False)
    elif request.method=='POST':
        projects_data=JSONParser().parse(request)
        projects_serializer=ProjectsSerializer(data=projects_data)
        if projects_serializer.is_valid():
            projects_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        projects_data=JSONParser().parse(request)
        project=Project.objects.get(ProjectId=projects_data['ProjectId'])
        projects_serializer=ProjectsSerializer(project,data=projects_data)
        if projects_serializer.is_valid():
            projects_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    


@csrf_exempt
def projects_detail(request, id):
    if request.method=='GET':
        project=Project.objects.get(ProjectId=id)
        projects_serializer=ProjectsSerializer(project)
        return JsonResponse(projects_serializer.data,safe=False)
    elif request.method=='DELETE':
        project=Project.objects.get(ProjectId=id)
        project.delete()
        return JsonResponse("Deleted Successfully",safe=False)



class HelloView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request):
		content = {'message': 'Hello, World'}
		return Response(content)


class DemoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print(request.user)
        return Response({"message": "Your are authenticated!"})


class Register(APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "status":"success",
                "user_id": user.id,
                "refresh": str(refresh),
                "access": str(refresh.access_token)

            }
        )


