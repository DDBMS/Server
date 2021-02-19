from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm


def my_view(request):
    print(f"Great!")
    message = 'Upload files you want'
    # 處理上傳的資料
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # 上傳資料後重整
            return redirect('my-view')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  #空白的form

    # 
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'list.html', context)
