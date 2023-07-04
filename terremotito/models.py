from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Intensidad(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    magnitud = models.FloatField()

    def __str__(self):
        return f'Terremoto {self.fecha} - Magnitud: {self.magnitud}'

class Zona(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='zonas')

    def __str__(self):
        return self.nombre

class Sensor(models.Model):
    nombre = models.CharField(max_length=100)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE, related_name='sensores')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    usuario = models.CharField(max_length=100)
    correo = models.EmailField()
    clave = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario