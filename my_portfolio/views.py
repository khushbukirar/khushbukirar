from django.shortcuts import render
from datetime import datetime
# Create your views here.
def home(request):
    return render(request, 'home.html', {'now': datetime.now()})