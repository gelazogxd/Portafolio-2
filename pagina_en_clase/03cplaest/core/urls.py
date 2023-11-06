from django.urls import path
from core import views



app_name = "core"


urlpatterns = [
    path('list/grantgoal/', views.ListGrantGoal.as_view(), name="gg_list"),
    path('create/grantgoal/', views.CreateGrantGoal.as_view(), name="gg_create"),
    path('detail/grantgoal/<int:pk>/', views.DetailGrantGoal.as_view(), name="gg_detail"),
    path('update/grantgoal/<int:pk>/', views.UpdateGrantGoal.as_view(), name="gg_update"),
    path('delete/grantgoal/<int:pk>/', views.DeleteGrantGoal.as_view(), name="gg_delete"),
]