import base64
import hashlib
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Family
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .forms import UploadFileForm
from django.core.files import File
from django.core.files.storage import FileSystemStorage
    
# Create your views here.
def main(request):
    return render(request, "morae/main.html")
    
def writing(request):
    return render(request, "morae/writing.html")

def details(request):
    addressValue = '모든'
    countryValue = '모든'
    context = {
        'address' : addressValue,
        'country' : countryValue,
        'family' : Family.objects.all()
    }
    
    if request.GET.get('address') != "":
        addressValue = request.GET.get('address')
        context = {              
            'address' : addressValue,
            'country' : countryValue,
            'family' : Family.objects.filter(address__icontains = request.GET.get('address'))
        }
        
        
    if request.GET.get('country') != "":
        countryValue = request.GET.get('country')
        context = {
            'address' : addressValue,
            'country' : countryValue,
            'family' : Family.objects.filter(country__icontains = request.GET.get('country'))
        }
    
    if request.GET.get('country') != "" and request.GET.get('country') != "":
        context = {
            'address' : addressValue,
            'country' : countryValue,
            'family' : Family.objects.filter(country__icontains = request.GET.get('country') , address__icontains = request.GET.get('address'))
        }
        
    return render(request, "morae/details.html", context)

@csrf_exempt
def create(request):
    if request.method=="POST":
        kakao = request.POST.get('kakao')
        state= request.POST.get('state')
        address = request.POST.get('address')
        gmoney = request.POST.get('gmoney')
        kmoney = request.POST.get('kmoney')
        country = request.POST.get('country')
        detail = request.POST.get('detail')
        writepw = request.POST.get('writepw')
    
        tphoto = __create_file__(request.FILES['tphoto'])
        gphoto = __create_file__(request.FILES['gphoto'])
        
        Family.objects.create(state=state, address=address, gmoney=gmoney, kmoney=kmoney, country=country,
                              gphoto=gphoto, tphoto=tphoto, kakao=kakao, detail=detail, writepw=writepw)
        
        return redirect('/')

    
def __create_file__(myfile):
	fs = FileSystemStorage()
	filename = fs.save(myfile.name, myfile)
	uploaded_file_url = fs.url(filename)
	return myfile.name

    
    
@csrf_exempt
def delete(request):
    temppw = request.POST.get('userpw')
    tempkakao = request.POST.get('kakao2')
    
    realpw = Family.objects.filter(kakao=tempkakao, writepw = temppw)
    
    if realpw.exists():
        realpw.delete()
    
    return redirect('/')
    