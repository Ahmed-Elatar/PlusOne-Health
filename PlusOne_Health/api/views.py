from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate,login,logout,get_user
from django.contrib.auth.models import User, Group
from .forms import *
from .models import *
from .serializers import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.






def index(request):
    post_list = Post.objects.all()    
    paginator = Paginator(post_list,3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)
    form=SearchPostForm()
  
    if request.method=='POST':
        form=SearchPostForm(request.POST)
  
        if form.is_valid():
            return render(request,"search_result.html",{"posts":search_fun(request,form.cleaned_data['search'])[0] ,"searched_for":search_fun(request,form.cleaned_data['search'])[1] },status=200)


    return render(request,"list.html",{"form":form,"posts":posts},status=200)




def profile(request,id):

    
    user=get_object_or_404(User,id=id)
    user_profile=UserProfile.objects.filter(user=id).first()
    
    post_list = Post.objects.filter(auth_id =id)    
    paginator = Paginator(post_list,3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)

    form=UserProfileForm()

    if request.method=='POST':
        form=UserProfileForm(request.POST,request.FILES)
        items=UserProfile.objects.filter(user_id=request.user.id).first()

        if items == None:
            UserProfile.objects.create(user_id=request.user.id)
        items=UserProfile.objects.filter(user_id=request.user.id).first()

        if form.is_valid():

            if form.cleaned_data['bio']:
                items.bio=form.cleaned_data['bio']
                print(form.cleaned_data['bio'])
            if form.cleaned_data.get('image'):
                items.image=form.cleaned_data['image']
                print(form.cleaned_data['image'])

        items.save()        

        return redirect('profile',request.user.id)
    else:
        
        form = UserProfileForm()

        return render(request,"profile.html",{"form":form,"id":id,"posts":posts,"user":user,"user_profile":user_profile},status=200)






# showing Post details and comments and adding comment --
def post_detail(request, id):
   
    post = get_object_or_404(Post,id=id)
    comments=PostComment.objects.filter(post_id=id)
    form=PostCommentsForm()
   
    if request.method =='POST':
        form=PostCommentsForm(request.POST)
        comment=None
   
        if form.is_valid():
            comment = form.save(commit=False)
            # Assign the post to the comment
            comment.post = post
            # Save the comment to the database
            comment.user= request.user
            comment.save()
   
        return redirect('post_detail',id)
        
    else:
        # print("-----",post.image.url)
        return render(request,'details.html',{'post': post ,"form":form, "comments":comments })



def add_post(request):
   
    user_profile=UserProfile.objects.filter(user=request.user.id).first()
    form=PostForm()
   
    if request.method == 'POST':
        post=None
        form=PostForm(request.POST,request.FILES)
   
        if form.is_valid():
            post=form.save(commit=False)
            post.auth =request.user
            # print(post.image)
            post.save()
   
            return redirect('index')
    
    return render(request,"add_post.html",{"form":form,"user_profile":user_profile})




def post_delete(request,id):

    post=get_object_or_404(Post,id=id)

    if request.user.id == post.auth.id:
        post.delete()

    else:
        return redirect('profile')

    return redirect('index')


def comment_delete(request,id):

    comment=get_object_or_404(PostComment,id=id)

    if request.user.id == comment.user.id:
        post_id= comment.post.id
        comment.delete()
        
        return redirect('post_detail' ,post_id )

    else:
        return redirect('profile')
    







def search_fun(request, slugg):

    post_list = Post.objects.filter(slug__icontains=slugg) | Post.objects.filter( title__icontains=slugg)
    paginator = Paginator(post_list,3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)
    
    return [posts,slugg]












####################################################################################################
##################                  Authentication

#sign-up 
def user_signup(request):
  
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
  
        if form.is_valid():
            form.instance.is_staff = True
            user = form.save()
            group = Group.objects.get(name='Normal_Users')
            user.groups.add(group)

            
            return redirect('login')
  
    else:
        form = UserCreationForm()
  
    return render(request, 'signup.html', {'form': form})



# login
def user_login(request):

    if request.user.is_authenticated:
        return redirect ('logout')
  
    if request.method == 'POST':
        

        form = LoginForm(request.POST)
    
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
    
            if user:
                login(request, user)    
                return redirect('index')
    
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})


# logout page
def user_logout(request):
    
    logout(request)
    return redirect('login')