from django.urls import path
from . import views

urlpatterns = [
  path ('',views.index, name='posts'),
  path ('storage/<str:nombre>/<str:apellido>/<str:cargo>/<str:funcion>/<str:rol>',views.storage, name ="storage"),
  path ('storage_empresa/<str:nit>/<str:nombre_emp>/<str:direccion>',views.storage_empresa, name ="storage_empresa")
 ## path ('consultar/<int:id>',views.consultar,name='consultar'),
  ##path ('modificar/<str:titulo>/int:id',views.modificar, name="modificar"),
  ##path ('eliminar/<int:id>',views.eliminar,name='eliminar'),
]