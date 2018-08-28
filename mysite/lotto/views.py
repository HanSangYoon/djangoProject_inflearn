from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm
# Create your views here.

def index(request):
    #return HttpResponse("<H1>HAHAHAHA</H1>")

    lottos = GuessNumbers.objects.all()
    return render(request, "lotto/default.html", {"lottos":lottos})

def post(request):

    if request.method == "POST":
        #save Data
        #return HttpResponse("POST mothod") # POST method라는 문구가 출력
        form =  PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit = False)
            lotto.generate()

            #return HttpResponse("Saved OK")
            return redirect('index') #urls.py 의 지정된 url의 name을 쓰면 된다.
    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {"form":form})

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk=lottokey)
    return render(request, "lotto/detail.html", {"lotto":lotto})
