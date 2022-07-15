from django.shortcuts import render
from .models import MazzaQilingYayrang
from django.core.mail import send_mail
from django.views.generic import DetailView, ListView
from .models import News

# Create your views here.

class Index(ListView):
    model = MazzaQilingYayrang
    template_name = 'index.html'
    context_object_name = 'Object'
    slug_url_kwarg = 'newSlug'


# def Index(request):

    # context = MazzaQilingYayrang.objects.all()
    # return render(request, 'index.html', {'Object': context})


def Contact(request):
    if request.method == 'POST':
        ism = request.POST['name']
        email = request.POST['email']
        xabar = request.POST['mess']
        subject = request.POST['subject']
        title=ism
        msg='Sizga '+familya+' '+ism+'dan xabar bor'+'\nTelefon nomeri: '+tel+'\nXabari:\n'+xabar

        print(ism, xabar, tel)
        send_mail(
            ism,
            msg,
            tel,
            ['quchqorovismat@gmail.com'],
            fail_silently=False,
        )

    return render(request, 'contact.html')

class new_detail(DetailView):
    model = MazzaQilingYayrang
    template_name = 'new_detail.html'
    context_object_name = 'more'
    slug_url_kwarg = 'newSlug'


class NewsCreateView(ListView):
    model = News
    template_name = "news.html"
    context_object_name = "Yangiliklar"
