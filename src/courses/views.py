from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.detail import DetailView
from django.db.models import Count
from .models import Language, Course
from students.forms import CourseEnrollForm

class CourseListView(TemplateResponseMixin, View):
    model = Course
    template_name = 'course/list.html'

    def get(self, request, language=None):
        languages = Language.objects.annotate(total_courses=Count('courses'))
        courses = Course.objects.annotate(total_modules=Count('modules'))
        if language:
            language = get_object_or_404(Language, slug=language)
            courses = courses.filter(language=language)
        return self.render_to_response({'languages': languages,
                                        'language': language,
                                        'courses': courses})

class CourseDetailView(DetailView):
    model = Course
    template_name = 'course/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['enroll_form'] = CourseEnrollForm(initial={'course':self.object})
        return context
