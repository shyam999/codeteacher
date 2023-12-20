from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from .fields import OrderField
from ckeditor.fields import RichTextField

class Language(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Language, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Course(models.Model):
    owner = models.ForeignKey(User, related_name='courses_created', on_delete=models.CASCADE)
    students = models.ManyToManyField(User, related_name='courses_joined', blank=True)
    language = models.ForeignKey(Language, related_name='courses', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = RichTextField(verbose_name='ModuleContent',null=True,blank=True)
    order = OrderField(blank=True, for_fields=['course'])

    class Meta:
        ordering = ['order']

    def __str__(self):
        return '{}. {}'.format(self.order, self.title)
