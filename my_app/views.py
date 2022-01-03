from django.shortcuts import render,redirect
from .forms import *
from .models import *
# from .mysql_connection import *
from datetime import date

# Create your views here.

# cursor = mydb.cursor()
currentDate = date.today().strftime("%B %d, %Y")

#function to display home page with 9 posts only
def home(request):
    tags = Category.objects.all().order_by('-id')
    posts = Post.objects.all().order_by('-id')[:9]
    return render(request,'index.html',{'posts':posts,'date':currentDate,'tags':tags})


#function to display all post in descending order
def allPost(request):
    tags = Category.objects.all().order_by('-id')
    posts = Post.objects.all().order_by('-id')
    return render(request,'index.html',{'posts':posts,'date':currentDate,'tags':tags})


#function to add a post
def post(request):
    tags = Category.objects.all().order_by('-id')
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = PostForm()
            return render(request,'makePost.html',{'form':form,'success':'Post added with success','tags':tags})

    else:   
        form = PostForm()
    return render(request,'makePost.html',{'form':form,'tags':tags})

#function to list all the post of a category
def single(request,id=0,data=0):
    tags = Category.objects.all().order_by('-id')
    if id> 0 and data > 0:
        currentPost = Post.objects.get(id=data)
        currentPost.views = currentPost.views + 1
    
        currentPost.save()
            
        posts = Post.objects.filter(category=id)
        return render(request,'index.html',{'posts':posts,'date':currentDate,'tags':tags})
    
    if id>0 and data==0 :
        posts = Post.objects.filter(category=id).order_by('-id')
        return render(request,'index.html',{'posts':posts,'date':currentDate,'tags':tags})
    
    if id<=0 and data<=0:
        return redirect('home')


#function to display the details of post
def details(request,id=0):
    tags = Category.objects.all().order_by('-id')
    post = Post.objects.get(id=id)
    return render(request,'details.html',{'post':post,'date':currentDate,'tags':tags})

#function to update number of likes of a post
def updatePost(request,id=0):
    tags = Category.objects.all().order_by('-id')
    if id > 0:
        post = Post.objects.get(id=id)
        post.likes = post.likes + 1
    
        post.save()
        
        return render(request,'details.html',{'post':post,'date':currentDate,'tags':tags})
    else:
        return redirect('home')
    
#function to add categories
def addCategory(request):
    tags = Category.objects.all().order_by('-id')
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            
            form = CategoryForm()
            return render(request,'addCategory.html',{'form':form,'success':'Category added with success','tags':tags})
    
    form = CategoryForm()
    return render(request,'addCategory.html',{'form':form,'tags':tags})


#display small dashboard
def displayDashboard(request):
    posts = Post.objects.all().order_by('-id')
    return render(request,'deletePost.html',{'posts':posts})

#blog of code to delete blog
def deletePost(request,id=0):
    post = Post.objects.get(id=id)
    post.delete()
    posts = Post.objects.all().order_by('-id')
    return render(request,'deletePost.html',{'posts':posts,'success':'Post Delete Successfully '})

    
    
            