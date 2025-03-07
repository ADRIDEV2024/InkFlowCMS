from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import MediaFile, MediaCategory
from .forms import MediaUploadForm

class MediaListView(ListView):
    model = MediaFile
    template_name = 'media/media_list.html'
    context_object_name = 'media_files'
    paginate_by = 12

@login_required
def upload_media(request):
    if request.method == 'POST':
        form = MediaUploadForm(request.POST, request.FILES)
        if form.is_valid():
            media = form.save(commit=False)
            media.uploaded_by = request.user
            media.save()
            return redirect('media_list')
    else:
        form = MediaUploadForm()
    return render(request, 'media/upload_media.html', {'form': form})

def media_by_category(request, category_id):
    category = get_object_or_404(MediaCategory, id=category_id)
    media_files = MediaFile.objects.filter(category=category)
    return render(request, 'media/media_by_category.html', {'category': category, 'media_files': media_files})
