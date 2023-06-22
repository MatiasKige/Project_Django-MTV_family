from django.contrib import admin
from django.urls import path
from app.views import agregar_familiar, mostrar_familiar

urlpatterns = [
    path('admin/', admin.site.urls),
    path("agregar-familiar/",agregar_familiar,name="agregar_familiar"),
    path("mostrar-familiar/",mostrar_familiar,name="mostrar_familiar")
]
