from django.shortcuts import render , redirect
from django.contrib import messages
from dicto.models import Words

# Create your views here.
def base(request):
    return render(request, 'home.html')

def index(request,w):
    if request.method =="POST":
        w = request.POST.get("word").lower()
        l = Words.objects.filter(eword=w).exists()
        if l:
            word = Words.objects.get(eword=w)
            return render(request,'index.html',{"word":word})
        else:
            messages.success(request,"Word is not Present in Dictionary ! ")
            return redirect('/')

    else:
        l = Words.objects.filter(eword=w).exists()
        if l:
            word = Words.objects.get(eword=w)
            return render(request,'index.html',{"word":word})
        else:
            messages.success(request,"Word is not Present in Dictionary ! ")
            return redirect('/')



def edit(request , eword):
    word = Words.objects.get(eword=eword)
    if request.method == "POST":
        hword = request.POST.get("hword").lower()
        uses = request.POST.get("use").lower()
        category = request.POST.get("category")
        rword = request.POST.get("rword").lower()
        word.hword = hword
        word.uses = uses
        word.category = category
        word.rword = rword
        word.save()
        messages.success(request , "Word Edit Successfully !")
        return redirect("/" )
    return render(request, 'edit.html' , {"word":word})
    
def add(request):
    if request.method == "POST":
        eword = request.POST.get("word").lower()
        l = Words.objects.filter(eword=eword).exists()
        if l:
            messages.success(request ,"Word already in Dictionary !")
            return redirect("/")
        
        else:
            w = Words()
            w.eword = request.POST.get("word").lower()
            w.hword = request.POST.get("hword").lower()
            w.uses = request.POST.get("use").lower()
            w.category = request.POST.get("category")
            w.image = request.FILES.get('image')
            w.rword = request.POST.get("rword").lower()
            w.save()
            messages.success(request,"Word Added Succesfully ! ")
            return render(request,'add.html')
    return render(request, 'add.html')


def show(request):
    word = Words.objects.all()
    return render(request,'show.html',{"word":word})

def delete(request,eword):
    word = Words.objects.get(eword=eword)
    word.delete()
    messages.success(request,"Word Delete Successfully ! ")
    return redirect("/")