from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Autor
from .forms import post_form, post_form_model, autor_form_model

# POSTs
def principal(request):
    posts= Post.objects.all()
    autores = Post.objects.values_list('autor', flat=True).distinct()
    return render(request, 'blog/principal.html', {"posts": posts, "autores":autores})

def post_detalle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detalle.html', {"post":post})

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
            return redirect('posts')
    
    else:
        form = post_form_model()
    
    return render(request, 'blog/post_new.html', {"form":form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method =='POST':
        form = post_form_model(request.POST, instance=post)
        if form.is_valid():
            # post.titulo = form.cleaned_data['titulo']
            # post.cuerpo = form.cleaned_data['cuerpo']
            # post.fpublicado = form.cleaned_data['fpublicado']
            # #post.autor = Autor.objects.get(id=1)
            # post.save()
            form.save()
            return redirect('posts')
    
    else:
        #form = post_form(initial=post.__dict__)
        form = post_form_model(instance=post)
    
    return render(request, 'blog/post_new.html', {"form":form})


#### CRUD AUTORES 

def autores(request):
    autores = Autor.objects.all()
    return render(request, 'blog/autores.html', {"autores":autores})

def autor_detalle(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    return render(request, 'blog/autor_detalle.html', {"autor":autor})

def autor_new(request):
    if request.method == 'POST':
        form = autor_form_model(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autores')
    else:

        form = autor_form_model()

    return render(request, 'blog/autor_new.html', {"form":form})

def autor_del(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method=="POST":
        autor.delete()
        return redirect('autores')
    else:
        return render(request, 'blog/autor_del.html', {"autor":autor})

def autor_edit(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == "POST":
        form = autor_form_model(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('autores')
    else:
        form = autor_form_model(instance=autor)
    return render(request, 'blog/autor_edit.html', {"form":form})