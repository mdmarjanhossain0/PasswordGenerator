from django.shortcuts import render

def upload_image_view(request):
    image = request.FILES['image']
    print(image)

    
    return render(request, 'upload.html', {})