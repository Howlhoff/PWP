from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

# Create your models here.
class perfil(models.Model):
    n_usuario=models.OneToOneField(User,on_delete=models.CASCADE)
    imagen=models.ImageField(default = 'logo.png',upload_to='images/', height_field=None, width_field=None, null = True,blank = True)
    ciudad=models.CharField(max_length=255,verbose_name="Ciudad",blank=False,null=True)
    pais=models.CharField(max_length=255,verbose_name="Pais",blank=False,null=True)
    descripcion=models.CharField(max_length=255,verbose_name="Descripcion",blank=False,null=True)

    def save(self,*args,**kwargs):
        super().save()
        img = Image.open(self.imagen.path)
        if img.height > 500 or img.width > 500:
            new_img = (500,500)
            img.thumbnail(new_img)
            img.save(self.imagen.path)

    def image_url(self):
        if self.imagen and hasattr(self.imagen, 'url'):
            return self.imagen.url
        else:
            return '/static/img/logo.png'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        perfil.objects.create(n_usuario=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.perfil.save()
