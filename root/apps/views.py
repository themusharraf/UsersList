from django.views.generic import TemplateView, ListView
from .models import People


class Home(TemplateView):
    template_name = 'home.html'


class UserList(ListView):
    model = People
    context_object_name = 'users'
    template_name = 'user_list.html'
