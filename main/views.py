from django.shortcuts import render
from django.views import generic
from .models import *

class HomeListView(generic.ListView):
    template_name = 'index.html'

    def get(self, reuquest):

        home = Home.objects.get()
        popular_items = Popular_Items.objects.get().coffee.all()
        todays_special = Todays_special.objects.get().coffee.all()
        daily_menu = Daily_Menu.objects.get()

        context = {
            'home': home,
            'popular_items': popular_items,
            'todays_special': todays_special,
            'daily_menu': daily_menu,
        }

        return render(reuquest, self.template_name, context=context)
    
class ContactListView(generic.ListView):
    template_name = 'contact.html'

    def get(self, reuquest):

        context = {

        }

        return render(reuquest, self.template_name, context=context)
    
class MenuListView(generic.ListView):
    template_name = 'menu.html'

    def get(self, reuquest):

        coffees = Coffee.objects.all()
        menu = Menu.objects.get()
        our_menus = Our_menus.objects.get().coffee.all()
        categories = Category.objects.all()

        context = {
            'menu': menu,
            'our_menus': our_menus,
            'categories': categories,
            'coffees': coffees,
        }

        return render(reuquest, self.template_name, context=context)
    
class TodayListView(generic.ListView):
    template_name = 'today-special.html'

    def get(self, reuquest):

        popular_items = Popular_Items.objects.get().coffee.all()
        daily_menu = Daily_Menu.objects.get()

        context = {
            'popular_items': popular_items,
            'daily_menu': daily_menu,
        }

        return render(reuquest, self.template_name, context=context)