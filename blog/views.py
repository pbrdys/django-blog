from django.shortcuts import render, get_object_or_404, reverse
# from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.
# def index(request):
#     return HttpResponse("Ello, ello, Blog og og og og")

class PostList(generic.ListView):
    # queryset = Post.objects.all()
    queryset = Post.objects.filter(status=1)
    # queryset = Post.objects.all().order_by("created_on")
    # template_name = "post_list.html"
    template_name = "blog/index.html"
    paginate_by = 6
    
def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    
    # Handle the POST request from the comment form
    if request.method == "POST":
        print("Received a POST request")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            # display success message string:
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    
    comment_form = CommentForm()
    
    print("About to render template")
    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )
    

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    
    if request.method == "POST":
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data = request.POST, instance=comment)
        
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
    


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    # HttpResponseRedirect is a Django class that tells the browser to go to a different URL.
    # reverse is a Django function that constructs a URL from the provided URL path name and any relevant URL arguments: args=[slug].
    # Using the slug argument ensures the user is returned to the same blog post on which they edited or deleted a comment.
    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
        