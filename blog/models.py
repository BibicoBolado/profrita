from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    autor=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    slug=models.SlugField('Atalho')
    numReads = models.IntegerField('Numero Leituras',default=0)
    image=models.ImageField(
        upload_to='blog/imagens',verbose_name='Imagem',
        null=True,blank=True
    )

    capa=models.ImageField(
        upload_to='blog/imagens',verbose_name='Capa',
        null=True,blank=True
    )

    text=models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    
    def time_read(self):
        t_read=round(len(self.text.split(" "))/133)
        return t_read
    def addNumRead(self):
        self.numReads+=1
        self.save()
    
    def query_posts(self):
        return Post.objects.order_by('-created_date').all()

    def __str__(self):
        return self.title
    
