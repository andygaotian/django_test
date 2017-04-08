from django.conf.urls import url
from django.contrib import admin
from gao import views as gao_views  # new
 
urlpatterns = [
    url(r'^$', gao_views.index),  # new
	url(r'^test/', gao_views.test),
    url(r'^admin/', admin.site.urls),
]