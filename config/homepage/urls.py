from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='inicio'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', logoutRedirectView.as_view(), name='logout'),

]