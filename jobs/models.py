# jobs/models.py
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin, HitCount


class Job(models.Model, HitCountMixin):
    # Host will not always be the current user. 
    host = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name = 'host'
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name = 'author',
        null=True,
    )
    title = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    company = models.CharField(max_length=255) #change this in the future
    url = models.URLField(blank=True, null=True)
    accepted = models.BooleanField(default=False)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('job_detail', args=[str(self.id)])
        #return reverse('home')

    def get_full_name(self):
        if not self.user.first_name:
            return
        return ' '.join([self.user.first_name, self.user.last_name])
    
    def get_url(self):
        if not self.url:
            return '#'
        return self.url
    