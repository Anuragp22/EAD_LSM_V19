from EAD_LSM import views
from django.urls import path
from .views import city_list, city_detail, LSM_CITY_LIST, LSM_CITY_Detail, city_faqs, city_contact, city_sessions, city_speakers, city_sponsors,City_faqs, City_contact, City_sessions, City_speakers, City_sponsors

app_name = 'EAD_LSM'
urlpatterns = [

    path('', views.index),
    path('cities/', city_list, name='city_list'),
    path('cities/<str:city_name>/', city_detail, name='city_detail'),
    path('Cities/', LSM_CITY_LIST, name='LSM_CITY_LIST'),
    path('Cities/<str:City_name>/', LSM_CITY_Detail, name='LSM_CITY_Detail'),
    path('cities/<str:city_name>/faqs/', city_faqs, name='city_faqs'),
    path('cities/<str:city_name>/contact/', city_contact, name='city_contact'),
    path('cities/<str:city_name>/sessions/', city_sessions, name='city_sessions'),
    path('cities/<str:city_name>/speakers/', city_speakers, name='city_speakers'),
    path('cities/<str:city_name>/sponsors/', city_sponsors, name='city_sponsors'),
    path('Cities/<str:City_name>/LSM_faqs/', City_faqs, name='City_faqs'),
    path('Cities/<str:City_name>/LSM_contact/', City_contact, name='City_contact'),
    path('Cities/<str:City_name>/LSM_sessions/', City_sessions, name='City_sessions'),
    path('Cities/<str:City_name>/LSM_speakers/', City_speakers, name='City_speakers'),
    path('Cities/<str:City_name>/LSM_sponsors/', City_sponsors, name='City_sponsors'),
]
