from django.contrib import admin
from django.urls import path
from app.views import all_teams_view, team_detail_view

urlpatterns = [
    path("", all_teams_view, name='home'),
    path("team/<str:name>/", team_detail_view, name='team'), 
]