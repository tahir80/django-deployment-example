from basic_app import views
from django.urls import path
from django.contrib import admin


# Template Tagging

app_name = 'basic_app'


urlpatterns = [
path('admin/', admin.site.urls),
path('relative/', views.relative, name = "relative"),
path('other/', views.other, name = "other")
]
