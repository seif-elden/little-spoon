from django.shortcuts import render, redirect , get_object_or_404 , HttpResponse
from django.contrib.auth import authenticate, login, logout 
from .forms import *
from django.contrib.auth.decorators import login_required

from .models import *



# Create your views here.
@login_required
def mybookmarks(request):
    me = Profile.objects.get(user=request.user)
    return render(request, 'mybookmarks.html',{"recipes":me.bookmarks.all})

@login_required
def explore(request):
    recipes = Recipe.objects.all()
    return render(request, 'explore.html' , {"recipes":recipes})



# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def myprofile(request):
    me = Profile.objects.get(user=request.user)
    myr = Recipe.objects.filter(author=request.user)

    return render(request, 'profile.html' ,{"me":me , "myr":myr})


@login_required
def addrecipe(request):
    if request.method =='POST':
        form = Recipeform(request.POST , request.FILES)
        if form.is_valid():
            Recipe = form.save(commit=False)
            Recipe.author = request.user
            Recipe.save()
        return redirect("myprofile")


    form = Recipeform()
    return render(request,"add_recipe.html" ,{"form":form})



@login_required
def deleterecipe(request,pk):
    obj = get_object_or_404( Recipe ,pk = pk)
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to 
        # home page
        return redirect("myprofile")

    return render(request, "delete_recipe.html" )

@login_required
def viewrecipe(request,pk):
    r = get_object_or_404( Recipe ,pk=pk)
    u = get_object_or_404( Profile ,user = request.user)
    booked =  u.bookmarks.contains(r)    
    liked =  r.likes.contains(request.user)  

    return render(request, "view_recipe.html" , {"recipe":r , "booked":booked , "liked":liked})

@login_required
def addbockmark(request,pk):
    r = get_object_or_404( Recipe ,pk=pk)
    u = get_object_or_404( Profile ,user = request.user)
    u.bookmarks.add(r)
    
    return redirect("viewrecipe",pk=pk)

@login_required
def removebockmark(request,pk):
    r = get_object_or_404( Recipe ,pk=pk)
    u = get_object_or_404( Profile ,user = request.user)
    u.bookmarks.remove(r)
    
    return redirect("viewrecipe",pk=pk)

@login_required
def likerecipe(request,pk):
    r = get_object_or_404( Recipe ,pk=pk)
    r.likes.add(request.user)
    
    return redirect("viewrecipe",pk=pk)

@login_required
def unlikerecipe(request,pk):
    r = get_object_or_404( Recipe ,pk=pk)
    r.likes.remove(request.user)
    
    return redirect("viewrecipe",pk=pk)


# update view for details
def updaterecipe(request, pk):

    obj = get_object_or_404(Recipe, pk = pk)
    form = Recipeform(request.POST or None, instance = obj)
 
  
    if form.is_valid():
        form.save()
        return redirect("myprofile")
 
    # add form dictionary to context
 
    return render(request, "editrecipe.html", {"form":form})

def editprofile(request, pk):

    obj = get_object_or_404(Profile, user = request.user)
    form = profileform(request.POST or None, instance = obj)
 
  
    if form.is_valid():
        form.save()
        return redirect("myprofile")
 
    # add form dictionary to context
 
    return render(request, "editprofile.html", {"form":form})






