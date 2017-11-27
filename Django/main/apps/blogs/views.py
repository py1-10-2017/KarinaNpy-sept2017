from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = {
        "email" : "blog@mail.com",
        "name" : "mike"
    }
    return render(request, "blogs/index.html", context)

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"
        print "*"*50
        return redirect("/")
    else:
        return redirect("/")

def show(request,blog_id):
    return HttpResponse("placeholder to display blog{}".format(blog_id))

def edit(request, blog_id):
    return HttpResponse("placeholder to edit blog {}".format(blog_id))

def delete(request, blog_id):
    return redirect('/')

# Create your views here.
