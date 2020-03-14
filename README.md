# Django-TEMP
Recibe informacion desde un sensor de temperatura via WiFi

Este proyecto esta pensado para ser usado en conjunto con 
https://github.com/Krim10000/ESP32-TEMP-WIFI


para usar el proyecto modificar el archivo settings en TEMProject
moficiar la siguiente linea:
ALLOWED_HOSTS = ['127.0.0.1', 'localhost','192.168.0.20']# cambiar la ultima ip por la de tu computador esto se obtine con
en terminal :
///
ifconfig
///
usar la ip despues de inet
luego abrir una terminal en la ubicacion del archivo manage.py (.../Django-TEMP-master/TEMProject):

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
sudo python3 runserver ip:puerto

yo use el puerto 80 abriendolo con  la interfaz grafica de ubunutu 

#sudo apt-get install gufw # interfaz grafica
#Sistema > Administración > Configuración del cortafuegos.
#add the port used






