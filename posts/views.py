from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def posts(request):
    return render(request,"posts/footer.html")

def post_detail(request):
    return HttpResponse("Hello post detail page!")