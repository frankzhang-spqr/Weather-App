from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('weather/', views.WeatherView.as_view(), name='weather'),
    path('forecast/', views.ForecastView.as_view(), name='forecast'),
    path('get-location-weather/', views.LocationWeatherView.as_view(), name='location_weather'),
    path('toggle-favorite/', views.ToggleFavoriteView.as_view(), name='toggle_favorite'),
    path('set-units/', views.SetUnitsView.as_view(), name='set_units'),
]
