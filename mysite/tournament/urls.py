from django.urls import path
from . import views
app_name = 'tournament'
urlpatterns = [
    path('', views.base_view, name='base_view'),
    path('login_view', views.login_view, name='login_view'),
    path('home_view', views.home_view, name='home_view'),
    path('register_view', views.register_view, name='register_view'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('create_tournament', views.create_tournament, name='create_tournament'),
    path('create_player', views.create_player, name='create_player'),
    path('my_tournaments', views.tournament_my_table_view, name='my_tournaments'),
    path('tournaments', views.tournament_table_view, name='tournaments'),
    path('tournament/<int:id>', views.tournament_view, name='tournament'),
    path('tournament/<int:id>/delete', views.delete_tournament_view, name='delete'),
    path('tournament/<int:pk>/update', views.update_tournament_view, name='update'),
    path('tournament/<int:id>/<int:pk>/add_player', views.add_player, name='add_player'),
    path('tournament/<int:id>/<int:pk>/delete_player_from_tournament', views.delete_player_from_tournament, name='delete_player_from_tournament'),
]
