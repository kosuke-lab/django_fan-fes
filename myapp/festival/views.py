from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Festival
from .models import Area
from .models import Country
from .models import Comment
from .forms import PostForm
from .forms import ContactForm
from .forms import CommentForm
from django.views import generic
from django.db.models import Q 
from django.views.generic import TemplateView
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings
 

class Topview(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['festivals' ] =Festival.objects.all().order_by('-pk')[0:4]
        context['festivals_pv'] = Festival.objects.all().order_by('-views')[0:4]
        return context


def area(request, url_code, pk):
    area = get_object_or_404(Area, url_code = url_code)
    url_code = get_object_or_404(Festival, pk=pk, area = area)
    festival = get_object_or_404(Festival, pk = pk)
    festival.views += 1
    festival.save() 
    template_name = 'festival/festival_detail.html'

    
    article = Festival.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        print(request.POST)
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.article = get_object_or_404(Festival, pk=pk)
            form.save()
            #return redirect('https://google.com')

    context = {
        'area': area, 
        'url_code' : url_code,
        'festival' : festival,
        'form':form,
         }
    return render(request, template_name ,context, )

class AboutView(TemplateView):
    template_name = 'festival/about/index.html'

class AsiaView(TemplateView):
    template_name = 'festival/asia/index.html'

class CreateView(LoginRequiredMixin,generic.edit.CreateView):
    model = Festival
    template_name = 'festival/create/index.html'
    form_class = PostForm
    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super().get_form_kwargs(*args, **kwargs)
        form_kwargs['initial'] = {'author': self.request.user}
        return form_kwargs



class UpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.edit.UpdateView):
    model = Festival
    fields = ['name', 'area', 'country', 'location', 'start_time', 'thumbnail', 'detail']
    raise_exception = True

    def test_func(self):
         post = self.get_object()
         if self.request.user == post.author:
            return True
         return False

class IndexView(generic.ListView):
    model = Festival
    template_name = 'festival/festival_list.html'
    paginate_by = 10

    def get_queryset(self):
        keyword = self.request.GET.get('keyword')
        if keyword:
            object_list =  Festival.objects.filter(name__contains=keyword)
            messages.success(self.request, '「{}」の検索結果'.format(keyword))
        else:
            object_list = Festival.objects.all()
        return object_list

##各カテゴリーページ作成

class CategoryView(generic.ListView):
    model = Festival
    template_name = 'festival/category.html'
    context_object_name = 'category_list'
    paginate_by = 5

    def get_queryset(self):
        category_list = Festival.objects.filter(area__url_code = self.kwargs['url_code']).order_by('-id')
        keyword = self.request.GET.get('keyword')
        if keyword:
            category_list =  category_list.filter(name__contains=keyword)
            messages.success(self.request, '「{}」の検索結果'.format(keyword))
        else:
                category_list = category_list
        return category_list
    
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Area, url_code=self.kwargs['url_code'])
        return context


class PolicyView(TemplateView):
    template_name = 'festival/policy/index.html'

class SitemapView(TemplateView):
    template_name = 'festival/sitemap/index.html'

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        print(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'お問合わせ'
            from_email = form.cleaned_data['email']
            recipient_list = ["support@fan-fes.com","k.12ap.m@gmail.com"]
            message = form.cleaned_data['message']
            send_mail(subject, message, from_email, recipient_list)
            return redirect('festival:complete')
    else:
        form = ContactForm()
        return render(request, 'festival/contact/index.html', {
        'form': form,
    })


def complete(request):
    return render(request, 'festival/contact/complete.html')


class RequirementsView(TemplateView):
    template_name = 'festival/requirements/index.html' 