from django.contrib import admin
from django.urls import path
from smsapp.views import home, create, login_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path("home",home,name="home"),
    path("create",create,name="create"),
    path('', login_view, name='login'),
]
