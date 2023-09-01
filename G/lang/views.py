from django.shortcuts import render ,redirect
from django.utils.translation import gettext as _
from django.utils.translation import get_language , activate , gettext

# Create your views here.


def home(request):
    trans = translate(language=request.session.get('language', 'tr'))
    return render(request, 'home.html', {'trans': trans})


def switch_language(request, language):
    request.session['language'] = language
    return redirect('lang:home')

def item(request):

    return render(request , 'item.html')

def translate(language):
    cur_language = get_language()
    try :
        activate(language)
        text = gettext('hello')
    finally:
        activate(cur_language)
    return text
