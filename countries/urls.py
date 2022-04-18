from django.urls import path
from countries import views

urlpatterns=[
    path("all",views.ListAllCountryNames.as_view(),name="allcountries"),
    path("details/<str:cname>",views.CountryDetailView.as_view(),name="countrydetail"),
]