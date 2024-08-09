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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField('Coffee Name', max_length=254)
    about = models.TextField('About Coffee')
    price = models.PositiveIntegerField('Price')
    img = models.ImageField('Coffee img', upload_to='media')

    def __str__(self) -> str:
        return self.name

class PopularItems(models.Model):

    coffee = models.ManyToManyField(Coffee)

    def __str__(self) -> str:
        return self.coffee.__str__()
    
    class Meta:
        verbose_name = 'Popular_Items'
        verbose_name_plural = 'Popular_Items'

class TodaysSpecial(models.Model): 

    coffee = models.ManyToManyField(Coffee)

    def __str__(self) -> str:
        return self.coffee.__str__()
    
    class Meta:
        verbose_name = 'Todays_special'
        verbose_name_plural = 'Todays_special'

class Text(models.Model):
    name = models.CharField('Text Name', max_length=254)
    text = models.TextField('Text')

    def __str__(self) -> str:
        return self.text

    class Meta:
        verbose_name = 'Text'
        verbose_name_plural = 'Textes'

class DailyMenu(models.Model):
    text = models.TextField('Text')
    about = models.ManyToManyField(Text)
    img = models.ImageField('IMG', upload_to='media')

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

class OurMenus(models.Model):
    coffee = models.ManyToManyField(Coffee)

    def __str__(self) -> str:
        return self.coffee.__str__()

    class Meta:
        verbose_name = 'Our_menus'
        verbose_name_plural = 'Our_menus'

class Contact(models.Model):
    name = models.CharField('Name', max_length=254)
    email = models.EmailField('Email')
    subject = models.CharField('Subject', max_length=254)
    message = models.TextField('Message')

    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'




















