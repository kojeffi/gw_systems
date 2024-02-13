from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def faqs(request):
    return render(request, 'faqs.html')


def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def techstack(request):
    return render(request, 'techstack.html')

def testimonial(request):
    return render(request, 'testimonials.html')

def blog(request):
    return render(request, 'blog.html')

def partner(request):
    return render(request, 'partnership.html')

def contact(request):
    return render(request, 'contact.html')