from django.contrib import admin
from django.urls import path
from app.views import all_teams_view, procurement_team_view, management_team_view, community_team_view, documentation_team_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", all_teams_view, name='home'),
    path("team/Procurement", procurement_team_view, name='procurement'),
    path("team/Management", management_team_view, name='management'),
    path("team/Community", community_team_view, name='community'),
    path("team/Documentation", documentation_team_view, name='documentation'),
]
