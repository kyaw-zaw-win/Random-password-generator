from django.urls import path
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('yourpassword/',views.password,name='password'),
    path('about/',views.about,name='about')
]