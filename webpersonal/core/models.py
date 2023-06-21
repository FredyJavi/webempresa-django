from django.db import models

# Create your models here.
class redsocial(models.Model):
    title=models.CharField(max_length=50,verbose_name='Titulo')
    descripcion=models.TextField(verbose_name='Descripcion')
    link=models.URLField(verbose_name='Direccion Web',null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True,verbose_name='Fecha Creacion') #añade la hora de forma automatica
    updated=models.DateTimeField(auto_now=True,verbose_name='Fecha Actualizacion')
    

    class Meta:
        verbose_name="url"
        verbose_name_plural="urls"
        ordering=["-created"] #ordena del nuevo al antiguo

    def __str__(self):
        return self.title


