from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .forms import CustomUserCreationForm
from jobs.models import Job
from .models import CustomUser
from hitcount.models import HitCountMixin

# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'



class AdminView(DetailView):
    model = CustomUser
    template_name = 'admin.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AdminView, self).get_context_data(*args, **kwargs)
        user = self.request.user
        context["accepted_jobs"] = Job.objects.filter(host=user, accepted=True).order_by('-date')
        context["pending_jobs"] = Job.objects.filter(host=user, accepted=False).order_by('-date')

        #getting total views
        total_job_views = 0
        for job in Job.objects.filter(host=user, accepted=True):
            total_job_views += job.hit_count.hits 
        context["total_job_views"] = total_job_views

        return context

class EmployerAdminView(DetailView):
    model = CustomUser
    slug_field = "username"
    template_name = 'employer_admin.html'

    def get_context_data(self, *args, **kwargs):
        context = super(EmployerAdminView, self).get_context_data(*args, **kwargs)
        user = self.request.user
        context["active_jobs"] = Job.objects.filter(author=user, accepted=True).order_by('-date')
        context["pending_jobs"] = Job.objects.filter(author=user, accepted=False).order_by('-date')
        return context