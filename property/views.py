from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from property.models import Comment, CommentForm


def index(request):
    response = "You're looking at the Propery Page."
    setting = Setting.objects.get(pk=1)
    context = {'setting':setting,'text': response}
    return render(request, 'index.html', context)


@login_required(login_url='/login') #Check Login
def addcomment(request,id):
    url = request.META.get('HTTP_REFERER') # get last url
    if request.method == 'POST': # form post edildiyse
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user = request.user # Access User Session information
            data = Comment() # model ile baglanti kur
            data.user_id = current_user.id
            data.property_id = id
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR') # Client computer ip address
            data.save() # veritabanina kaydet
            messages.success(request,"Yorumunuz basari ile gonderilmistir. Tesekkur Ederiz")
            return HttpResponseRedirect(url)

    messages.error(request,"Yorumunuz Kaydedilmedi. Lutfen Kontrol Ediniz")  
    return HttpResponseRedirect(url)