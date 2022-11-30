from django.urls import path
from .views import person_list, person_new, people_update, people_delete


urlpatterns = [
    path('list/', person_list, name="person_list"),
    path('new/', person_new, name="person_new"),
    path('update/<int:id>/', people_update, name="people_update"),
    path('delete/<int:id>/', people_delete, name="people_delete"),
]

