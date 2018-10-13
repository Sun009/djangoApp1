from django.http import HttpResponse 
from django.shortcuts import render
import ctypes

# Create your views here.
def enhance_home(request):

    return render(request, 'enhance/Web_Site/ImageEnhancer.html')

def PythonCode(request):
    results = "Python Code Worked" 
    return HttpResponse(results)
        
         



      

 
         