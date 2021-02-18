from django.shortcuts import render

from .models import Ducument
from .forms import FocumentForm
# Create your views here.

def my_view(request):
    print(f"Great! ")
    message = "Upload as many files as you want!"
    #Handle file upload
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES["docfile"])
            newdoc.save()

            return redirect("my-view")
        else:
            message = "The form is not valid. Fix the following error:"
    else:
        form = DocumentForm()
    
    #loadDocument for the list page
    documents = Document.objects.all()
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'list.html', context)
