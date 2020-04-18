from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'base.html')


def html_home(request):
    return render(request, 'html_home.html')


def css_home(request):
    return render(request, 'css_home.html')


def tags(request):
    return render(request, 'tags.html')


def html_resources(request):
    return render(request, 'html_resources.html')


def attributes(request):
    return render(request, 'attributes.html')


def forms(request):
    return render(request, 'forms.html')


def meta(request):
    return render(request, 'meta.html')


def css_resources(request):
    return render(request, 'css_resources.html')


def box_model(request):
    return render(request, 'box_model.html')


def margin(request):
    return render(request, 'margin.html')


def display(request):
    return render(request, 'display.html')


def flexbox(request):
    return render(request, 'flexbox.html')

