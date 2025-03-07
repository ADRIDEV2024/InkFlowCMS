from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from .models import Page, PageView

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    
    # Registrar la vista del usuario
    PageView.objects.create(page=page, ip_address=request.META.get('REMOTE_ADDR'))
    
    return render(request, 'pages/page_detail.html', {'page': page})
