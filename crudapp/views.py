from django.contrib.auth.decorators import login_required
from django.http import request,HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from .models import Club
from .forms import ClubForm
from .models import Activity
from .forms import ActivityForm
from django.views.generic import ListView, DetailView
from django.contrib.auth import views

class IndexView(ListView):
    template_name = 'crudapp/index.html'
    context_object_name = 'contact_list'

    def get_queryset(self):
        return Contact.objects.all()


class IndexClub(ListView):
    template_name = 'crudapp/index_club.html'
    context_object_name = 'club_list'
    
    def get_queryset(self):
        return Club.objects.all()


class IndexAct(ListView):
    template_name = 'crudapp/index_act.html'
    context_object_name = 'act_list'
    
    def get_queryset(self):
        return Activity.objects.all()


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'crudapp/contact-detail.html'
    
        
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.display_pictur =request.POST['display_pictur'] 
            
            fs = FileSystemStorage()
            filename = fs.save(user_pr.display_pictur.name,user_pr.display_pictur )
            uploaded_file_url = fs.url(filename)
            file_type = user_pr.display_pictur.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return render(request, 'crudapp/index.html')
            user_pr.save()
            redirect('contacts/<user_pr>')#.args(user_pr)
            #return render(request, 'crudapp/contact_detail.html', {'user_pr': user_pr})

    form = ContactForm()
    return render(request,'crudapp/create.html',{'form': form})


def edit(request, pk, template_name='crudapp/edit.html'):
    contact = get_object_or_404(Contact, pk=pk)
    form = ContactForm(request.POST or None , instance=contact)
    if form.is_valid(): #or request.method=='POST':
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})
    
    

def delete(request, pk, template_name='crudapp/confirm_delete.html'):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method=='POST':
        contact.delete()
        return redirect('index')
    return render(request, template_name, {'object':contact})

def createClub(request):
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = ClubForm()

    return render(request,'crudapp/create_club.html',{'form': form})


def editClub(request, pk, template_name='crudapp/edit_club.html'):
    club = get_object_or_404(Club, pk=pk)
    form = ClubForm(request.POST or None , instance=club)
    if form.is_valid(): #or request.method=='POST':
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})
    
    

def deleteClub(request, pk, template_name='crudapp/confirm_delclub.html'):
    club = get_object_or_404(Activity, pk=pk)
    if request.method=='POST':
        club.delete()
        return redirect('index')
    return render(request, template_name, {'object':club})

def createAct(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = ActivityForm()

    return render(request,'crudapp/create_act.html',{'form': form})


def editAct(request, pk, template_name='crudapp/edit_club.html'):
    act = get_object_or_404(Activity, pk=pk)
    form = ActivityForm(request.POST or None , instance=act)
    if form.is_valid(): #or request.method=='POST':
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})
    
    

def deleteAct(request, pk, template_name='crudapp/confirm_delact.html'):
    act = get_object_or_404(Activity, pk=pk)
    if request.method=='POST':
        act.delete()
        return redirect('index')
    return render(request, template_name, {'object':act})



