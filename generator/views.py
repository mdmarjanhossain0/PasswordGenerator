from django.shortcuts import render
from django.core.files.storage import default_storage

def upload_image_view(request):

    if request.method == "POST":
        file = request.FILES['image']
        print(file)
       
        file_name = default_storage.save(file.name, file)
        file = default_storage.open(file_name)
        file_url = default_storage.url(file_name)
        print(file_url)

    
    return render(request, 'upload.html', {})

    data['name'] = password