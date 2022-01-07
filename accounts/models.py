from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.text import slugify 
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin, HitCount


# Create your models here.
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    is_host = models.BooleanField(
        ('Hosting a Job Board'),
        default=False, 
        help_text= ('Check only if you intend on hosting a job board'),
    )
    slug = models.SlugField(null=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse('job_board', kwargs={'slug': self.slug})

