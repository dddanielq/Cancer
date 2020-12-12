from django.db import models

# Create your models here.


class Tejidos(models.Model):
    partes = models.IntegerField()
    temperatura = models.FloatField()
    color = models.FloatField()
    inflamacion = models.FloatField()
    
    def Tejidos(self):
        cadena = "{0}, {1}, {2}, {3}"
        return cadena.format(self.id, self.temperatura, self.color, self.inflamacion)
    
    def __str__(self):
        return self.Tejidos()

class grafo(models.Model):
    origen = models.ForeignKey(Tejidos, on_delete=models.CASCADE, related_name='origen')
    destino = models.ForeignKey(Tejidos, on_delete=models.CASCADE, related_name='destino')
    conectado = models.BooleanField()

    def __str__(self):
        return self.origen + ' - ' + self.destino + ': ' + self.conectado
