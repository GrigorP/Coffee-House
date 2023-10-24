from django.db import models


class Home(models.Model):
    title = models.CharField('Home Title', max_length=254)
    text = models.TextField('Home Text')
    img = models.ImageField('Home Image', upload_to='media')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home'

class Category(models.Model):
    name = models.CharField('Category name', max_length=245)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Coffee(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField('Coffee Name', max_length=254)
    about = models.TextField('About Coffee')
    price = models.PositiveIntegerField('Price')
    img = models.ImageField('Coffee img', upload_to='media')

    def __str__(self) -> str:
        return self.name

class Popular_Items(models.Model):

    coffee = models.ManyToManyField(Coffee)

    def __str__(self) -> str:
        return self.coffee.__str__()
    
    class Meta:
        verbose_name = 'Popular_Items'
        verbose_name_plural = 'Popular_Items'

class Todays_special(models.Model): 


    coffee = models.ManyToManyField(Coffee)

    def __str__(self) -> str:
        return self.coffee.__str__()
    
    class Meta:
        verbose_name = 'Todays_special'
        verbose_name_plural = 'Todays_special'

class Daily_Menu(models.Model):
    img = models.ImageField('IMG', upload_to='media')
    text = models.TextField('Text')
    about1 = models.CharField('about1', max_length=254)
    about2 = models.CharField('about2', max_length=254)
    about3 = models.CharField('about3', max_length=254)
    about4 = models.CharField('about4', max_length=254)
    about5 = models.CharField('about5', max_length=254)
    about6 = models.CharField('about6', max_length=254)

    def __str__(self) -> str:
        return 'Daily Menu'
    
    class Meta:
        verbose_name = 'Daily_Menu'
        verbose_name_plural = 'Daily_Menu'

class Menu(models.Model):
    name = models.CharField('Name', max_length=254)
    text = models.TextField('Text')
    img = models.ImageField('IMG', upload_to='media')


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'

class Our_menus(models.Model):
    coffee = models.ManyToManyField(Coffee)

    def __str__(self) -> str:
        return self.coffee.__str__()

    class Meta:
        verbose_name = 'Our_menus'
        verbose_name_plural = 'Our_menus'























