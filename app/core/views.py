from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Images
import os
  # Assuming Images is the model you want to use

class Add(CreateView):
    """
    View to handle the addition of new items.
    This view can be extended to handle specific models or forms.
    """
    template_name = 'add.html'
    model = Images
    fields = ['image', 'description']
    success_url = '/core/add_image/'

def gallery(request):
    alias = os.environ.get('ALIAS', 'images_db')
    images = Images.objects.using("remote_db").all()
    return render(request, "gallery.html", {"images": images})
