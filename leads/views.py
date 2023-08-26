from  django.core.mail import send_mail
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Lead, Agent
from .forms import Leadform, LeadModelForm, CustomUserCreationForm

class SignupView(generic.CreateView):
    template_name="registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(request):
        return "/login"

class LandingPageView(generic.TemplateView):
    template_name="landing.html"

def landing_page(request):
    return render(request,"landing.html")

class LeadListVeiw(LoginRequiredMixin,generic.ListView):
    template_name="lead_list.html"
    queryset=Lead.objects.all()

def lead_list(request):
    # return HttpResponse("Hello World")
    # return render(request, 'home_page.html')
    leads=Lead.objects.all()

    context={
        "leads":leads
    }
    return render(request, 'lead_list.html',context)
class LeadDetailVeiw(LoginRequiredMixin,generic.DetailView):
    template_name="lead_detail.html"
    queryset=Lead.objects.all()


def lead_detail(request, pmk):
    lead=Lead.objects.get(id=pmk)
    context={
        "lead":lead
    }
    return render(request, 'lead_detail.html',context)

class LeadCreateVeiw(LoginRequiredMixin,generic.CreateView):
    template_name="lead_create.html"
    form_class = LeadModelForm

    def get_success_url(request):
        return "/leads"
    def form_valid(self, form):
        #to send emails
        send_mail(
            subject="new lead created",
            message="go to crm and check your new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]

        )
        return super(LeadCreateVeiw, self).form_valid(form)

def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # age = form.cleaned_data['age']
            # agent= form.cleaned_data['agent']
            # Lead.objects.create(
            #     first_name=first_name,
            #     last_name=last_name,
            #     age=age,
            #     agent=agent,
            # )

            form.save()
            return redirect("/leads")
    context = {
        "form": form
    }
    return render(request, "lead_create.html",context)

class LeadUpdateVeiw(LoginRequiredMixin,generic.UpdateView):
    template_name="lead_update.html"
    queryset=Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(request):
        return "/leads"

def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form,
        "lead": lead
    }
    return render(request, "lead_update.html", context)

class LeadDeleteVeiw(LoginRequiredMixin,generic.DeleteView):
    template_name="lead_delete.html"
    queryset=Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(request):
        return "/leads"

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")