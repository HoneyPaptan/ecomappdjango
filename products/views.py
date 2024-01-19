from django.shortcuts import render
from .models import Product
# Create your views here.
def productsPage(request):
    products = Product.objects.all()
    

    return render(request, "products/products.html", {'prod': products})


def productView(request,slug):
    prodview = Product.objects.get(slug = slug)
    main_image_url = prodview.main_image.url if prodview.main_image else ''
    secondary_images_urls = [image.image.url for image in prodview.images.all()]

    return render(request,"products/proddetail.html", {'prodview': prodview, 'main_image_url': main_image_url,
            'secondary_images_urls': secondary_images_urls})