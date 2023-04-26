import io
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .utils import create_user
from .forms import postForm
from .models import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

from django.db import IntegrityError

# Create your views here.


def home(request):
    if (request.method == 'GET'):
        images = Image.objects.all()
        context_dict = {
            'images': images,
        }
        # TODO
    return render(request, 'index.html', context_dict)


def sign_up(request):
    if (request.method) == 'GET':
        context_dict = {
            'signup_form': UserCreationForm
        }
        return render(request, 'signup.html', context_dict)
    else:
        try:
            form = UserCreationForm(request.POST)
            print(form.is_valid())
            if form.is_valid():
                user = User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password1'),
                    # email= request.POST['email']
                    # legal_age = request.POST['legal']
                    # ADD SOME OTHER FIELDS LIKE +18 AND EMAIL
                )
                user.save()
                login(request, user)
                return redirect('home')
            else:
                context_dict = {
                'signup_form': UserCreationForm,
                'errors': form.errors.as_ul
                }
            return render(request, 'signup.html', context_dict)
        
        except IntegrityError:
            return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error': 'Username already existe'
            }) 

            



def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('post')
            else:
                print("invalid algo")
                form.add_error(None, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect('home')

def about_us(request):
    return render(request, 'about.html')

def post(request):
    context_dict = {
            'post_form': postForm(),
        }
    if(request.method == 'GET'):
        return render(request, 'postPage.html', context_dict)
    else:
        form = postForm(request.POST, request.FILES)
        print(form.errors)
        print("files: " , request.FILES)
        if form.is_valid():
            image_name = form.cleaned_data['image_name']
            description = form.cleaned_data['description']
            # image = form.cleaned_data['image']
            image = request.FILES['image']
            
            new_image = Image(name=image_name, description=description, image=image)
            new_image.save()
        
            return redirect('post')
        else: 
            print("Invalid form")
            return render(request, 'postPage.html', context_dict)
        
def show_profile(request):
    if(request.method == 'GET'):
        return render(request, 'myprofile.html')