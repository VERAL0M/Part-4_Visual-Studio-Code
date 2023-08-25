from django.db import models
from django.contrib import admin
from django.utils.html import format_html

# Create your models here.

class Advertisement(models.Model):
    title = models.CharField('заголовок', max_length=128) 
    description = models.TextField('Описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    auction = models.BooleanField('Торг', help_text='Отметьте, если уместен торг')



class Advertisemen(models.Model):
    title = models.CharField('заголовок', max_length=128) 
    description = models.TextField('Описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    auction = models.BooleanField('Торг', help_text='Отметьте, если уместен торг')

    # def __str__(self): 
    #     return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price},)>'

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.create_at.date()==timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>',created_time
            )
        return self.create_at.strftime('%d.%m.%y')





    class Meta:
        db_table ='advertisement' 
