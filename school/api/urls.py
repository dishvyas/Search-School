from django.urls import path
from school.api.views import ApiSchoolListView, json_data 

app_name = 'school'

urlpatterns = [
	path('list', ApiSchoolListView.as_view(), name="list"),
	path('table', json_data, name="list")
]