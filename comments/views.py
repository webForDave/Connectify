from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateCommentForm
from django.contrib.auth.decorators import login_required
from topics.models import Topic
from comments.models import Comment

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

def update_comment_view(request, slug):
    comment = get_object_or_404(Comment, slug=slug)
    # topic = get_object_or_404(Topic, slug=topic_slug)
    if request.method == "POST":
        form = CreateCommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("topic_detail", slug=comment.topic.slug)
    else:
        form = CreateCommentForm(instance=comment)
    return render(request, "comments/update_comment.html", {"form": form})

def delete_comment_view(request, slug):
    comment = get_object_or_404(Comment, slug=slug)
    if request.method == "POST":
        comment.delete()
        return redirect("topic_detail", slug=comment.topic.slug)
    return render(request, "comments/delete_comment.html")