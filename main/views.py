from django.shortcuts import render
from django.views import generic
from .models import *
from .forms import ContactForm

class HomeListView(generic.ListView):
    template_name = 'index.html'

    def get(self, reuquest):

        home = Home.objects.get()
        popular_items = PopularItems.objects.get().coffee.all()
        todays_special_left = TodaysSpecial.objects.get().coffee.all()[0]
        todays_special_right = TodaysSpecial.objects.get().coffee.all()[1]
        todays_special_lower = TodaysSpecial.objects.get().coffee.all()[2:]
        daily_menu = DailyMenu.objects.get()
        daily_menu_about = DailyMenu.objects.get().about.all()

        context = {
            'navbar': 'home',
            'home': home,
            'popular_items': popular_items,
            'todays_special_left': todays_special_left,
            'todays_special_right': todays_special_right,
            'todays_special_lower': todays_special_lower,
            'daily_menu': daily_menu,
            'daily_menu_about': daily_menu_about,
        }

        return render(reuquest, self.template_name, context=context)
    
class ContactListView(generic.ListView):
    template_name = 'contact.html'

    def get(self, request):

        context = {
            'navbar': 'contact',
        }

        return render(request, self.template_name, context=context)
    
    def post(self, request):

        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
        else:
            form = ContactForm()

        context = {
            'navbar': 'contact',
            'form': form,
        }

        return render(request, self.template_name, context=context)
    
class MenuListView(generic.ListView):
    template_name = 'menu.html'

    def get(self, reuquest):

        coffees = Coffee.objects.all()
        menu = Menu.objects.get()
        our_menus = OurMenus.objects.get().coffee.all()
        categories = Category.objects.all()

        context = {
            'navbar': 'menu',
            'menu': menu,
            'our_menus': our_menus,
            'categories': categories,
            'coffees': coffees,
        }

        return render(reuquest, self.template_name, context=context)
    
class TodayListView(generic.ListView):
    template_name = 'today-special.html'

    def get(self, reuquest):

        popular_items = PopularItems.objects.get().coffee.all()
        daily_menu = DailyMenu.objects.get()

        context = {
            'navbar': 'today',
            'popular_items': popular_items,
            'daily_menu': daily_menu,
        }

        return render(reuquest, self.template_name, context=context)