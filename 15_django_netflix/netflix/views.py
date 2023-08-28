from django.shortcuts import render, redirect
from django.views import View

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import ProfileForm
from .models import Profile, Movie

# Create your views here.
# def home(request):
#     return render(request, 'index.html')


class Home(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('profile-list')
        return render(request, 'index.html')
    

@method_decorator(login_required, name='dispatch')
class ProfileList(View):
    def get(self, request, *args, **kwargs):
        profiles = request.user.profile.all()
        context = {
            'profiles': profiles
        }
        return render(request, 'profilelist.html', context)
    
@method_decorator(login_required, name='dispatch')
class ProfileCreate(View):
    def get(self, request, *args, **kwargs):
        form = ProfileForm()
        context = {
            'form':form
        }
        return render(request, "profilecreate.html", context)
    

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("profile-list")
        context = {
            'form':form
        }
        return render(request, "profilecreate.html", context)
    

@method_decorator(login_required, name='dispatch')
class MovieList(View):
    def get(self, request,profile_id,*args, **kwargs):
        profile = Profile.objects.get(id = profile_id)
        movies = Movie.objects.filter(age_limit = profile.age_limit)
        context = {
            "profile": profile,
            "movies": movies
        }
        return render(request, 'movielist.html', context)