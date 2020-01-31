from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django_extensions.db.fields import AutoSlugField
from django import forms
import datetime

class BlogEntry(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(('slug'), max_length=50, unique=True, populate_from=('title',))
    body = models.TextField()
    posted = models.DateField(default=datetime.date.today)
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    category = models.ForeignKey('blogentry.BlogCategory', on_delete=models.CASCADE)
    
    def __unicode__(self):
        return '%s' % self.title
    
    def __str__(self):
        return '%s' % self.title

    def url(self):
        return reverse('view_blog_item', args=[self.slug])

def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    server_filename = "media/images/%s-%s" % (slug, filename)
    return server_filename

class BlogImage(models.Model):
    post = models.ForeignKey(BlogEntry, related_name = 'Image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename)
    caption = models.CharField(max_length=200)
    anchor = models.CharField(max_length = 20)

class BlogCodeSnippet(models.Model):
    post = models.ForeignKey(BlogEntry, related_name = 'CodeSnippet', on_delete=models.CASCADE)
    CodeSnippet = models.TextField()
    caption = models.CharField(max_length=200, blank=True)
    anchor = models.CharField(max_length = 20)
    
class BlogCategory(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    
    def __unicode__(self):
        return '%s' % self.title
    
    def __str__(self):
        return '%s' % self.title

    def url(self):
        return reverse('view_blog_category', args=[self.slug])
