"""
URL configuration for modelserial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from modelserial_app import views as v1
from api_view_app import views as v2
from generic import views as v3
from concrete import views as v4
from viewset_app import views as v5
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('studentapi',v5.StudentReadOnlyModelViewSet,basename='student')
# router.register('studentapi',v5.StudentModelViewSet,basename='student')
# router.register('studentapi',v5.StudentViewset,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/',v1.StudentAPI.as_view()),
    # path('student_view_api/',v2.hello_world),
    # path('student_view_api/<int:pk>',v2.hello_world),
    # path('studentapi/',v2.StudentApi.as_view()),
    # path('studentapi/<int:pk>',v2.StudentApi.as_view()),
    # path('genericstudentapi/',v3.StudentList.as_view()),
    path('genericstudentapi/',v3.StudentCreate.as_view()),
    path('genericstudentretrieve/<int:pk>/',v3.StudentRetrieve.as_view()),
    path('genericstudentupdate/<int:pk>/',v3.StudentUpdate.as_view()),
    path('genericstudentdestroy/<int:pk>/',v3.StudentDestroy.as_view()),
    path('concretestudentlist/',v4.StudentList.as_view()),
    path('concretestudentcreate/',v4.StudentCreate.as_view()),
    path('concretestudentretrieve/<int:pk>',v4.StudentRetrieve.as_view()),
    path('concretestudentupdate/<int:pk>',v4.StudentUpdate.as_view()),
    path('concretestudentdestroy/<int:pk>',v4.StudentDestroy.as_view()),
    path('concretestudentrud/<int:pk>',v4.StudentRetrieveUpdateDestroy.as_view()),
    path('',include(router.urls)),
]
