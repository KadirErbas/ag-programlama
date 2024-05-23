from django.urls import path
from . import views
from .views import get_road_risk_data
from .views import get_bus_ticket


app_name = 'ag_programlama'


urlpatterns = [
    path("", views.home_view, name="home"),
        path('api/road-risk/', get_road_risk_data, name='get_road_risk_data'),
    path('api/get_bus_ticket/', get_bus_ticket, name='get_bus_ticket'),
    


]