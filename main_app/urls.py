from django.urls import path
from . import views

urlpatterns =[
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('animals/', views.animals_index, name='index'),
path('animals/<int:animal_id>', views.animals_details, name='detail'),


#Express
# Get The Form
# Post The Form
path('animals/create',views.AnimalCreate.as_view(),name="animals_create"),

path('animals/<int:pk>/update/', views.AnimalUpdate.as_view(), name='animals_update' ),
path('animals/<int:pk>/delete/', views.AnimalDelete.as_view(), name='animals_delete' ),

path('animals/<int:animal_id>/add_Feeding/', views.add_feeding , name='add_feeding' ),

#Urls for Country Crud Operations
path('countries/', views.CountryList.as_view(), name="countries_index"),
path('countries/<int:pk>/', views.CountryDetail.as_view(),name='countries_detail'),
path('countries/create/',views.CountryCreate.as_view(),name='countries_create'),
path('countries/<int:pk>/update/',views.CountryUpdate.as_view(),name='countries_update'),
path('countries/<int:pk>/delete/',views.CountryDelete.as_view(),name='countries_delete'),




#associate a country with a animal (M:M)

path ('animals/<int:animal_id>/assoc_country/<int:country_id>/', views.assoc_country, name="assoc_country"),


#UN- associate a country with a animal (M:M)

path ('animals/<int:animal_id>/unassoc_country/<int:country_id>/', views.unassoc_country, name="unassoc_country"),

#Sign Up URl

path('accounts/signup/',views.signup,name='signup')
]