from django.shortcuts import render

# Create your views here.
import  random
import string 
from django.shortcuts import render , redirect
from .models import UrlData
from .forms import Url

def urlShort(request):
    if request.method == 'POST':
        form = Url(request.POST)
        if form.is_valid():
           # generate random 10-charcter slug 
           slug = ''.join(random.choice(string.ascii_letters) for _ in range(10))
           url = form.cleaned_data["url"]   # get the orirginal url from the form 
           new_url = UrlData(url =url , slug= slug)  #save the url and slug 
           new_url.save()

           return redirect("/") # redirect to the home[page] after saving 
    else:
        form = Url() # empty form if it's a GET request

    data = UrlData.objects.all()
    context = {
        'form': form,
        'data':data ,
    }
    return render(request , 'index.html',context)




from django.shortcuts import redirect 
from .models import UrlData

def urlRedirect(request, slugs):
    # Find the original URL by the slug
    data = UrlData.objects.get(slug=slugs)
    return redirect(data.url)   # Redirect to the original URL


