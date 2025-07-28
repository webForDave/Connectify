from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateCommentForm
from django.contrib.auth.decorators import login_required
from topics.models import Topic

@login_required
def create_comment_view(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    if request.method == "POST":
        form = CreateCommentForm(request.POST)
        if form.is_valid(): 
            comment_instance = form.save(commit=False)
            comment_instance.author = request.user
            comment_instance.topic = topic
            comment_instance.save()
            return redirect("topic_detail", slug=topic.slug)
    else:
        form = CreateCommentForm()
    print(slug)
    context = {
        "form": form
    }
    return render(request, "comments/create_comment.html", context)