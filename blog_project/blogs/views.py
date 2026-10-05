from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from blogs.models import*
# Create your views here.
@login_required
def Home(req):
    return render(req,'home.html')

def Register_page(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        full_name = req.POST.get('full_name')
        email = req.POST.get('email')
        password = req.POST.get('password')
        password2 = req.POST.get('password2')
        if password == password2:
            UserModel.objects.create_user(
                username = username,
                full_name = full_name,
                email = email,
                password = password2
            )
            return redirect('Login_page')

    return render(req,'register.html')

def Login_page(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        user_info = authenticate(req, username=username, password=password)
        if user_info:
            login(req,user_info)
            return redirect('Home')
    return render(req,'login.html')

@login_required
def Blog_list(req):
    blog_data = BlogModel.objects.all()
    context = {
        'blog_data':blog_data
    }
    return render(req,'blog_list.html',context)

@login_required
def Add_Blog(req):
    if req.method == 'POST':
        title = req.POST.get('title')
        author_name = req.POST.get('author_name')
        content = req.POST.get('content')
        category = req.POST.get('category')
        blog_image = req.FILES.get('blog_image')
        BlogModel.objects.create(
            title = title,
            author_name = author_name,
            content = content,
            category = category,
            blog_image = blog_image
        )
        return redirect('Blog_list')
    
    return render(req,'Add_Blog.html')

@login_required
def Update_Blog(req, id):
    blog_data = BlogModel.objects.get(id=id)

    if req.method == 'POST':
        title = req.POST.get('title')
        author_name = req.POST.get('author_name')
        content = req.POST.get('content')
        category = req.POST.get('category')
        blog_image = req.FILES.get('blog_image')

        blog_data.title = title
        blog_data.author_name = author_name
        blog_data.content = content
        blog_data.category = category

        if blog_image:
            blog_data.blog_image = blog_image

        blog_data.save()

        return redirect('Blog_list')
    context = {
        'blog_data':blog_data
    }

    return render(req, 'Update_Blog.html', context)

def Blog_view(req):
    blog_data = BlogModel.objects.all()
    context = {
        'blog_data':blog_data
    }
    return render(req,'Blog_view.html',context)

@login_required
def Delete_blog(req,id):
    BlogModel.objects.filter(id=id).delete()
    return redirect('Blog_list')

@login_required
def Logout_page(req):
    logout(req)
    return redirect('Login_page')