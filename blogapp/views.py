from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blogapp.forms import UserSignUp, UploadBlog
from blogapp.models import Upload
from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime

base = {'url':'http://127.0.0.1:8000/'}
# Create your views here.
def landing(request):
    return redirect(base['url']+'landing/')

def welcome(request):
    return render(request, 'blogapp/welcome.html')

@login_required
def home(request):
    return render(request, 'blogapp/home.html')

@login_required
def post_blog(request):
    uploadform=UploadBlog()
    if request.method=='POST':
        uploadform = UploadBlog(request.POST, request.FILES)
        if uploadform.is_valid():
            data = uploadform.save(commit = False)
            data.author = request.user
            data.save()
            base.update({'msg1':'Data Uploaded'})
    base.update({'uploadform':uploadform})
    return render(request, 'blogapp/post_blog.html', context = base)

#@login_required
def view_all_blogs(request):
    images = Upload.objects.all().order_by('-upload_date')
    #print(request.GET)
    try:
        if request.GET['id'] !='':
            image = Upload.objects.get(id=request.GET['id'])
            image.delete()
        else: print('Not Allowed')
    except Exception as e:print(e)
    return render(request, 'blogapp/view_all_blogs.html', {'images':images, 'time': datetime.now})

@login_required
def detailview(request):
    #select * from product where id='1'
    #print(request.GET['id'])

    image=Upload.objects.get(id=request.GET['id'])
    #images.delete();  delete records
    return render(request,'blogapp/displaypost.html',{'image':image})

def signupform(request):
    signupform = UserSignUp()
    mydict=dict()
    if request.method=='POST':
        #DB insert code goes here
        signupform=UserSignUp(request.POST);
        if signupform.is_valid():
            user=signupform.save();#insert query
            user.set_password(user.password)
            user.save()# this object save finally
            subject="Blogging Welcome Mail"
            message="Welcome "+user.email+". \nYou are register"
            recipient_list=[user.email]
            email_from=settings.EMAIL_HOST_USER
            send_mail(subject,message,email_from,recipient_list)
            mydict.update({'msg':'Employee Registered Successfully'})
    mydict.update({'signupform':signupform})
    return render(request, 'blogapp/sign_up.html', context = mydict)
