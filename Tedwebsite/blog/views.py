from django.shortcuts import render
from django.http import HttpResponse

# # Create your views here.
# def index(request):
#     return HttpResponse("Blog home page")
def post_list(request):
    return render(request, 'blog/post_list.html', {})