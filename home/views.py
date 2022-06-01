from django.shortcuts import render,HttpResponse

# Create your views here.
#def index(request):
  #  return HttpResponse("this is home page")
def index(request):
    return render(request,'clock.html')
def stop_watch(request):
    return render(request,'stop_watch.html')
def timer(request):
    return render(request,'timer.html')
   