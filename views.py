#E:\DGP\DD\myVEN\myproject_root\HMS\
from django.shortcuts import render
from .forms import frmOpdRegister
from .forms import frmIpdRegister
from .forms import seedsData
from . models import OpdRegister # to fetch db data

def fnIndex(request):
    myObject = ''
    return render(request, 'index.html', {'form': myObject})

def fnIpdRegister(request):
    myObject=frmIpdRegister()
    context={'form':myObject}
    return render(request, 'IpdRegister.html',context)

def fnOpdRegister(request):
    
    if request.method == "POST":
        form = frmOpdRegister(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save(commit=True)
                #print.form.photo
                return redirect('/')  
            except:  
                pass  
    else:  
        form = frmOpdRegister()  
    return render(request,'OpdRegister.html',{'form':form})  

def fnViewData(request):
    context=OpdRegister.objects.all()
    return render(request, 'ViewData.html',{'myData':context})



def fnViewOpdProfile(request):
    context = OpdRegister.objects.order_by('-first_name')
    #context=list(OpdRegister.objects.all())
    return render(request, 'ViewOpdProfile.html',{'myData':context})



