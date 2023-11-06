from django.shortcuts import render

from django.views import generic

from django.urls import reverse_lazy
from .models import GrantGoal
from .forms import GrantGoalForm, UpdateGrantGoalForm
# Create your views here.

##### G R A N T G O A L C R U D #####

##Create
class CreateGrantGoal(generic.CreateView):
    template_name = "core/gg_create.html"
    model = GrantGoal
    form_class = GrantGoalForm
    success_url = reverse_lazy("core:gg_list")


## Retrieve
#List GrantGoal
class ListGrantGoal(generic.View):
    template_name = "core/gg_list.html"
    context = {}

    def get(self, request, *args, **kwargs):
        queryset = GrantGoal.objects.filter(status=True)
        self.context = {
            "grant_goals": queryset
        }
        return render(request, self.template_name, self.context)


#Detail
class DetailGrantGoal(generic.DetailView):
    template_name = "core/gg_detail.html"
    model = GrantGoal


#Update
class UpdateGrantGoal(generic.UpdateView):
    template_name = "core/gg_update.html"
    model = GrantGoal
    form_class = UpdateGrantGoalForm
    success_url = reverse_lazy("core:gg_list")


#Delete
class DeleteGrantGoal(generic.DeleteView):
    template_name = "core/gg_delete.html"
    model = GrantGoal
    success_url = reverse_lazy("core:gg_list")