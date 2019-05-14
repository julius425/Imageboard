from django.shortcuts import render, redirect, reverse, get_object_or_404
from . models import ThreadModel, PostModel
from .forms import ThreadModelForm, PostModelForm


def index_view(request):
    """
    Shows list of threads, allows to post a thread
    """

    threads = ThreadModel.objects.all()

    if request.method == 'POST':
        form = ThreadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = PostModelForm()

    context = {
        'threads': threads,
        'form': form
    }
    return render(request, 'core/index.html', context)


def thread_view(request, thread_id):
    """
    Shows all posts related to thread, allows to add a post with an image
    """
    # why thread=id?
    posts = PostModel.objects.filter(thread=thread_id)
    thread = ThreadModel.objects.get(pk=thread_id)

    # diff between cleaned data
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.thread = get_object_or_404(ThreadModel, pk=thread_id)
            post_item.save()
            return redirect('core:thread_view', thread_id)

    else:
        form = PostModelForm()

    context = {
        'posts': posts,
        'thread': thread,
        'form': form
    }
    return render(request, 'core/thread.html', context)