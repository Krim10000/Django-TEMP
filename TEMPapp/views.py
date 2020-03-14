from django.shortcuts import render
from django.http import HttpResponse
from .models import T_Vs_t
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Avg, Max, Min, Count


###############################
def grafico_mes(request):

    ahora= datetime.now()
    data = []
    labels =[]
    titulo= "Mes"

    queryset = T_Vs_t.objects.filter(FECHA__year=ahora.year, FECHA__month=ahora.month)

    for maumau in queryset:
        data.append(maumau.TEMPERATURA)
        labels.append(str(maumau.FECHA.strftime("%Y-%m-%d %H:%M")))
        min= queryset.aggregate(Min("TEMPERATURA"))
        min = str(min)
        min = min[21:25]
        avg= queryset.aggregate(Avg("TEMPERATURA"))
        avg = str(avg)
        avg = avg[21:25]
        max= queryset.aggregate(Max("TEMPERATURA"))
        max = str(max)
        max = max[21:25]
        count= queryset.count()
        dia = str(ahora.strftime("%d"))
        hora = str(ahora.strftime("%H"))
        minuto = str(ahora.strftime("%M"))
        opcount = int(dia)*24*60 + int(hora)*60 +int(minuto)#dia *24+60 + HORA*60 + MIN


    return render(request, 'grafico.html', {'labels': labels,'data': data, "min":min, "avg": avg, "max":max, "titulo":titulo, "count": count, "opcount": opcount})




###############################FUNCIONA
def grafico24h(request):

    #Step 1: Create a DataPool with the data we want to retrieve.
    ahora= datetime.now()
    data = []
    labels =[]
    titulo= "Ultimas 24 Hrs"

    ultimas24h = ahora-timedelta(hours=24)
    queryset = T_Vs_t.objects.filter(FECHA__range=(ultimas24h,ahora))
    #queryset = T_Vs_t.objects.all()[:1440] #1440 pts son las ultimas 24 hrs, considerando que la info se registra cada un min

    for maumau in queryset:
        data.append(maumau.TEMPERATURA)
        labels.append(str(maumau.FECHA.strftime("%Y-%m-%d %H:%M")))
        min= queryset.aggregate(Min("TEMPERATURA"))
        min = str(min)
        min = min[21:25]
        avg= queryset.aggregate(Avg("TEMPERATURA"))
        avg = str(avg)
        avg = avg[21:25]
        max= queryset.aggregate(Max("TEMPERATURA"))
        max = str(max)
        max = max[21:25]
        count= queryset.count()
        opcount = 1440


    return render(request, 'grafico.html', {'labels': labels,'data': data, "min":min, "avg": avg, "max":max, "titulo":titulo, "count": count, "opcount": opcount})

################################

###############################
def grafico_hora(request):

    ahora= datetime.now()
    data = []
    labels =[]
    titulo= "Ultimos 60 minutos"
    #min = []
    #max = []
    #avg = []
    ultima_hora = ahora-timedelta(hours=1)
    queryset = T_Vs_t.objects.filter(FECHA__range=(ultima_hora,ahora))
    #queryset = T_Vs_t.objects.all()[:1440] #1440 pts son las ultimas 24 hrs, considerando que la info se registra cada un min

    for maumau in queryset:
        data.append(maumau.TEMPERATURA)
        labels.append(str(maumau.FECHA.strftime("%Y-%m-%d %H:%M")))
        min= queryset.aggregate(Min("TEMPERATURA"))
        min = str(min)
        min = min[21:25]
        avg= queryset.aggregate(Avg("TEMPERATURA"))
        avg = str(avg)
        avg = avg[21:25]
        max= queryset.aggregate(Max("TEMPERATURA"))
        max = str(max)
        max = max[21:25]
        count= queryset.count()
        opcount = 60




    return render(request, 'grafico.html', {'labels': labels,'data': data, "min":min, "avg": avg, "max":max, "titulo":titulo, "count": count, "opcount": opcount})


################################

################################FUNCIONA

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from TEMPapp.models import T_Vs_t
from TEMPapp.serializers import Temp_serializer
from TEMPapp.serializers import Temp_serializer2


@csrf_exempt
def Temp_serializer_agregar_data(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = T_Vs_t.objects.all()
        serializer = Temp_serializer2(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Temp_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
##################################################################


def menu(request):
    return render(request, 'menu.html')
