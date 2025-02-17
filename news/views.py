from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm
from django.views.generic import DeleteView


def news_home(request):
    news = Artiles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DeleteView):
    model = Artiles
    template_name = 'news/datails_view.html'
    context_object_name = 'article'
    
def create(request):
    error =''
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'

    form = ArtilesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)