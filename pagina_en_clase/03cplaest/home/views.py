from django.shortcuts import render
from django.views import generic



# Create your views here.

class Index(generic.View):
    template_name = "home/index.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
            "name": "Ray Parra",
            "lista": [1, 2, 3]
        }
        return render(request, self.template_name, self.context)
    

class About(generic.View):
    template_name = "home/about.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
            "name": "Ray Parra"
        }
        return render(request, self.template_name, self.context)


class Identity(generic.View):
    template_name = "home/identity.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
            "name": "Ray Parra"
        }
        return render(request, self.template_name, self.context)


class Contact(generic.View):
    template_name = "home/contact.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context = {
            "name": "Ray Parra"
        }
        return render(request, self.template_name, self.context)