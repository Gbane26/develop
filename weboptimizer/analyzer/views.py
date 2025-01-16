from django.shortcuts import render
from .forms import FileUploadForm
from .models import Analysis

# Create your views here.

def analyze_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            analysis = form.save(commit=False)  
            
            analysis.selectors_removed = 10  
            analysis.size_saved = 5.2 
            analysis.save() 
            return render(request, 'analyzer/result.html', {'analysis': analysis})
    else:
        form = FileUploadForm()
    return render(request, 'analyzer/upload.html', {'form': form})