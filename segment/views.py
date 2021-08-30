from django.shortcuts import render
from .models import EnterpriseSegment, Sector, Branch

# Create your views here.
def mainindex(request):
    #scripts = Notebook.objects.order_by('-fieldDate')
    scripts = EnterpriseSegment.objects.all()
    return render(request, 'mainindex/mainindex.html', { 'scripts':scripts,})