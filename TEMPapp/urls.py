from django.contrib import admin
from django.urls import path, include
from .views import grafico24h, grafico_hora, grafico_mes, menu
from .views import  Temp_serializer_agregar_data

urlpatterns = [
    #path("", Listado_Estudiantes),
    path("grafico", grafico24h, name= "DÍA" ),
    path('snippets/',Temp_serializer_agregar_data,name ="Listado"),
    path("grafico_mes",grafico_mes, name = "MES"),
    path("grafico_hora",grafico_hora, name ="HORA"),
    path("menu",menu, name="menu"),# asigana la url menu, llama a la vista menu, y le da el nombre de menu

]
