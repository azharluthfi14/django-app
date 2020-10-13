from django.urls import path, include
from . import views

app_name = "app"

urlpatterns = [
    path('', views.index, name='index'),
    path('predict/dashboard/', views.dashboard, name='dashboard'),
    path('predict/form', views.predict, name='predict'),
    path('predict/', views.predict_chances, name='submit_prediction'),
    path('user/signin/', views.sign_in_user, name='signin'),
    path('user/signup/', views.sign_up_user, name='signup'),
    # path('predict/chart/', views.data_chart, name='chart'),
    path('predict/profile/', views.profile, name='profile'),
    path('logout_user/', views.logout_user, name="logout"),
    # path('user_settings/', views.user_theme, name='user_settings'),
    # path('update_theme/', views.update_theme, name='update_theme')

]