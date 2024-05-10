from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'home.html'


class UserList(TemplateView):
    template_name = 'user_list.html'
