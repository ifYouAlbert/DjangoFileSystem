from django.shortcuts import render, redirect
from .models import MyFiles


def page(request):
    all_files = MyFiles.objects.all()

    context = {
        'all_files': all_files
    }

    if request.POST:
        text = request.POST.get('text')
        file = request.FILES.get('file')
        if file:
            if text == '':
                text = file.name
            MyFiles.objects.create(
                text=text,
                file=file
            )

    return render(request, 'files.html', context)


def delete(request):
    all_files = MyFiles.objects.all()
    for file in all_files:
        file.delete()
    return redirect('files')

