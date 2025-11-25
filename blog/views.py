from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import get_user_model
from blog.models import Blog
from blog.forms import BlogForm
from django.http import HttpResponse
from accounts.views import user_login
from django.contrib.auth import login


# for creating blog
@login_required
def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            return redirect("my_blogs")
    else:
        form = BlogForm()
    
    return render(request, "blog/create_blog.html", {"form": form})


#Edit blog
@login_required
def edit_blog(request, pk):
    blog = Blog.objects.get(id=pk)

    if blog.user != request.user:
        return HttpResponse("Unauthorized", status=401)

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect("my_blogs")
    else:
        form = BlogForm(instance=blog)

    return render(request, "blog/edit_blog.html", {"form": form})



#for delete Blog
@login_required(login_url=user_login)
def delete_blog(request, pk):
    blog = Blog.objects.get(id=pk)

    if blog.user != request.user:
        return HttpResponse("Unauthorized", status=401)

    blog.delete()
    return redirect("my_blogs")

# Users  blog list
@login_required(login_url=user_login)
def my_blogs(request):
    blogs = Blog.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "blog/my_blogs.html", {"blogs": blogs})


#Blog detail page

def blog_detail(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request, "blog/detail.html", {"blog": blog})


# def home(request):
#     blogs = Blog.objects.all().order_by("-created_at")
#     return render(request, "users/home.html", {"blogs": blogs})
