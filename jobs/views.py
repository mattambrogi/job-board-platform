from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from .models import Job
from accounts.models import CustomUser
from hitcount.views import HitCountDetailView
from django.contrib.messages.views import SuccessMessageMixin




class JobListView(ListView):
    model = Job
    template_name = 'job_list.html'

class JobDetailView(HitCountDetailView): 
    model = Job
    template_name = 'job_detail.html'
    count_hit = True


class JobUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView): 
    model = Job
    fields = ('accepted',)
    template_name = 'job_edit.html'
 
    def test_func(self): # new
        obj = self.get_object()
        return (obj.host == self.request.user)

    def get_success_url(self):
        return reverse('admin', kwargs={'slug': self.request.user.slug})

class EmployerUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView): 
    model = Job
    fields = ('title', 'body',)
    template_name = 'job_edit.html'
 
    def test_func(self): # new
        obj = self.get_object()
        return (obj.author == self.request.user)


class JobDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView): 
    model = Job
    template_name = 'job_delete.html'
    #success_url = reverse_lazy('job_list')

    def test_func(self): 
        obj = self.get_object()
        return (obj.host == self.request.user or obj.author == self.request.user)

    def get_success_url(self):
        obj = self.get_object()
        if obj.host == self.request.user:
            return reverse('admin', kwargs={'slug': self.request.user.slug})
        else:
            return reverse('employer_admin', kwargs={'slug': self.request.user.slug})


class JobCreateView(LoginRequiredMixin,SuccessMessageMixin, CreateView):
    model = Job
    template_name = 'new_job.html'
    fields = ('company', 'title', 'url', 'body',)
    success_message = ""

    def get_context_data(self, **kwargs):
        users = CustomUser.objects.all()
        context = super(JobCreateView, self).get_context_data(**kwargs)
        page_user = get_object_or_404(CustomUser, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.host=get_object_or_404(CustomUser, id=self.kwargs['pk'])
        return super().form_valid(form)
    
    def get_success_message(self, cleaned_data):
        author = self.request.user
        host = get_object_or_404(CustomUser, id=self.kwargs['pk'])
        if author == host:
            return "Your job was successfully submitted. Right now it is pending, you can accept below or via the admin. "
        return "Your job was successfully submitted. We will give the host a chance to take a look and let you know if they accept. "

class JobBoardView(HitCountDetailView):
    model = CustomUser
    template_name = 'job_board.html'
    count_hit = True

    def get_context_data(self, *args, **kwargs):
        users = CustomUser.objects.all()
        context = super(JobBoardView, self).get_context_data(*args, **kwargs)
        page_user =  get_object_or_404(CustomUser, slug=self.kwargs['slug'])
        context["page_user"] = page_user
        context["jobs"] = Job.objects.filter(host=page_user, accepted=True).order_by('-date')
        return context

  

class JobBoardListView(ListView):
    model = CustomUser
    template_name = 'job_board_list.html'

    



