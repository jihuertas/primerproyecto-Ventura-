from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Autor
from .forms import post_form, post_form_model

# Create your views here.
def post_new(request):
    if request.method =='POST':
        form = post_form_model(request.POST)
        if form.is_valid():
            form.save()
            # ftitulo = form.cleaned_data['titulo']
            # fcuerpo = form.cleaned_data['cuerpo']
            # ffpublicado = form.cleaned_data['fpublicado']
            # autor = Autor.objects.get(id=1)
            # Post.objects.create(titulo=ftitulo,autor=autor, cuerpo=fcuerpo, fpublicado=ffpublicado)
            return render(request, 'blog/post_added.html')
    
    else:
        form = post_form_model()
    
    return render(request, 'blog/post_new.html', {"form":form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method =='POST':
        form = post_form_model(request.POST)
        if form.is_valid():
            # post.titulo = form.cleaned_data['titulo']
            # post.cuerpo = form.cleaned_data['cuerpo']
            # post.fpublicado = form.cleaned_data['fpublicado']
            # #post.autor = Autor.objects.get(id=1)
            # post.save()
            form.save()
            return redirect('principal')
            #return render(request, 'blog/post_added.html')
    
    else:
        #form = post_form(initial=post.__dict__)
        form = post_form_model(instance=post)
    
    return render(request, 'blog/post_new.html', {"form":form})




def principal(request):
    posts= Post.objects.all()
    autores = Post.objects.values_list('autor', flat=True).distinct()
    return render(request, 'blog/principal.html', {"posts": posts, "autores":autores})

def autores(request):
    autores = Post.objects.values_list('autor', flat=True).distinct()
    return render(request, 'blog/autores.html', {"autores":autores})

def ji(request):
    if request.method == 'POST':
        nombre = request.POST['nombre1']
        #Post.objects.create()
        print (nombre)
        print (request.POST)

    return render(request, 'blog/ji.html')


def detalle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle.html', {"post":post})


