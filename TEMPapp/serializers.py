from rest_framework import serializers
from .models import T_Vs_t

class Temp_serializer(serializers.ModelSerializer):# POST

    class Meta:
        model = T_Vs_t
        fields =["TEMPERATURA"]

class Temp_serializer2(serializers.ModelSerializer):# GET

    class Meta:
        model = T_Vs_t
        fields =["TEMPERATURA", "FECHA"]



        # cd /
        #python3 manage.py shell
        #from INPUT.models import T_Vs_t
        #from INPUT.serializers import Temp_serializer
        #from rest_framework.renderers import JSONRenderer
        #from rest_framework.parsers import JSONParser
        #escribir = T_Vs_t(TEMPERATURA= "20")
        #escribir.save()
        #serializer = Temp_serializer(escribir)
        #serializer.data

        #content = JSONRenderer().render(serializer.data)
        #content


        #serializer = Temp_serializer(T_Vs_t.objects.all(), many=True)
