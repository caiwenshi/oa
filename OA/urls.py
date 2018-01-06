from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'getemployeeinfo/(.+)', views.process_get_employee_info, name='process_get_employee_info'),
    url(r'getprojectinfo/(.+)', views.process_get_project_info, name='process_get_project_info'),


    url(r'^loginapp$', views.loginapp, name='loginapp'),
]
