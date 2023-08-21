from django.db import models

class Advertis(models.Model):
    title = models.CharField('заголовок', max_length=128) 
    description = models.TextField('Описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    auction = models.BooleanField('Торг', help_text='Отметьте, если уместен торг')

    def __str__(self): 
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price},)>'

    class Meta:
        db_table ='advertisements'

