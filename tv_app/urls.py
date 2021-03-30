from django.urls import path
from . import views

urlpatterns = [
    path('', views.rendercreate),
    path('create/', views.create),
    path('<int:show_id>/edit', views.edit),
    path('read', views.read),
    path('<int:show_id>/renderupdate', views.renderupdate),
    path('<int:show_id>/update', views.update),
    path('<int:show_id>/delete', views.delete),
]
