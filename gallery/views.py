import requests
import base64
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Image
from .forms import ImageForm, ImageUploadForm

def gallery_list(request):
    images = Image.objects.all()
    return render(request, 'gallery_list.html', {'images': images})

def add_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gallery_list')
    else:
        form = ImageForm()
    return render(request, 'add_image.html', {'form': form})

def upload_to_imgur(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Lire le fichier image
            image_file = request.FILES['image']
            image_data = image_file.read()
            
            # Encoder en base64
            image_b64 = base64.b64encode(image_data).decode('utf-8')
            
            # Préparer la requête à l'API ImgBB
            url = "https://api.imgbb.com/1/upload"
            data = {
                'key': settings.IMGBB_API_KEY,
                'image': image_b64
            }
            
            # Envoyer la requête
            response = requests.post(url, data=data)
            
            if response.status_code == 200:
                result = response.json()
                img_url = result['data']['url']
                
                # Créer l'objet Image avec l'URL d'ImgBB
                Image.objects.create(
                    title=form.cleaned_data['title'],
                    url=img_url
                )
                return redirect('gallery_list')
            else:
                return render(request, 'upload_image.html', {
                    'form': form,
                    'error': 'Erreur lors de l\'upload'
                })
    else:
        form = ImageUploadForm()
    
    return render(request, 'upload_image.html', {'form': form})
