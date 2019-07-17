from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
# Create your views here.
#def articlespage(request):
#	return render(request,'article/home.html')
def posts(request):
	myposts=Blogpost.objects.all()
	return render(request,'article/art.html',{'myposts':myposts})
def blogpost(request,id):
	post=Blogpost.objects.filter(post_id=id)[0]
	return render(request,'article/blogpost.html',{'post':post})
def newposts(request):
	return render(request,'article/newposts.html')

def newerposts(request):
	print('DOne')
	author_name=request.POST.get("author_name",' ')
	head_line=request.POST.get("head_line",' ')
	sub_heading=request.POST.get("sub_heading",' ')
	content=request.POST.get("content",'')
	#image=request.POST.get("image",' ')
	blogposts=Blogpost(author_name=author_name,headline=head_line,sub_heading=sub_heading,chead1=content,)
	blogposts.save()
	return render(request,'article/newposts.html')
