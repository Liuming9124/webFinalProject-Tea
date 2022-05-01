from django.db import models

# Create your models here.

class Drink(models.Model):
    drink_id = models.IntegerField()
    drink_cname = models.CharField(max_length=20)
    drink_Mmoney = models.IntegerField()
    drink_Lmoney = models.IntegerField()

    def __str__(self):
        return self.drink_cname

class Order(models.Model):
    DC = [
        ('00', '挑Tea紅茶'),
        ('01', '蘭香綠茶'),
        ('02', '桂香烏龍茶'),
        ('03', '金萱青茶'),
        ('04', '極品高山茶'),
        ('05', '特級奶綠'),
        ('06', '芝麻奶茶'),
        ('07', '蜂蜜奶茶'),
        ('08', '烏龍奶茶'),
        ('09', '錫蘭奶紅'),
        ('10', '桔茶'),
        ('11', '葡萄柚汁'),
        ('12', '金桔檸檬'),
        ('13', '蘆薈蜂蜜檸檬'),
        ('14', '鳳梨紅茶'),
        ('15', '珍珠/波霸奶茶'),
        ('16', '暗黑水晶奶茶'),
        ('17', '椰果奶茶'),
        ('18', '蘆薈優多綠茶'),
        ('19', '紅茶三兄弟')
    ]
    SC = [
        ('M','中'),
        ('L','大')
    ]
    oid = models.CharField(max_length=15, blank=False)
    name = models.CharField(max_length=10, blank=False)
    size = models.CharField(max_length=2, choices=SC, default='M')
    drink = models.CharField(max_length=10, choices = DC, default='00')

    class Meta:
        ordering = ['-oid']

    def __str__(self):
        return self.oid


