from django.db import models

class Food(models.Model):
    title = models.CharField('Описание', max_length=255)
    text = models.TextField('Рецепты блюд')
    img = models.ImageField('Картинка', upload_to='home/adanov', blank=True)
    price = models.IntegerField('Цена')


class Order(models.Model):
    author = models.CharField('Автор', max_length=255)
    title = models.CharField('описание блюда', max_length=255)
    price = models.IntegerField('Цена')


class Order_detail(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class Apartment(models.Model):
    number = models.CharField(max_length=255)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
