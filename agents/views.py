from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from django.shortcuts import reverse
from .forms import AgentModelForm
# from .mixins import OrganisorAndLoginRequiredMixin


class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = "agent_list.html"
    
    def get_queryset(self):
        # organisation = self.request.user.userprofile
        return Agent.objects.all()


class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")

    def form_valid(self, form):
        agent= form.save(commit=False)
        agent.organisation=self.request.user.userprofile
        agent.save()
        return super(AgentCreateView,self).form_valid(form)
#         user = form.save(commit=False)
#         user.is_agent = True
#         user.is_organisor = False
#         user.set_password(f"{random.randint(0, 1000000)}")
#         user.save()
#         Agent.objects.create(
#             user=user,
#             organisation=self.request.user.userprofile
#         )
#         send_mail(
#             subject="You are invited to be an agent",
#             message="You were added as an agent on DJCRM. Please come login to start working.",
#             from_email="admin@test.com",
#             recipient_list=[user.email]
#         )
#         return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "agent_detail.html"
    context_object_name = "agent"

    def get_queryset(self):
        return Agent.objects.all()


class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "agent_update.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")

    def get_queryset(self):
        return Agent.objects.all()


# class AgentDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
#     template_name = "agents/agent_delete.html"
#     context_object_name = "agent"

#     def get_success_url(self):
#         return reverse("agents:agent-list")

#     def get_queryset(self):
#         organisation = self.request.user.userprofile
#         return Agent.objects.filter(organisation=organisation)