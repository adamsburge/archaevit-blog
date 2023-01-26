from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import CommentForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        interesting_liked = False
        if post.interesting_likes.filter(id=self.request.user.id).exists():
            interesting_liked = True
        important_liked = False
        if post.important_likes.filter(id=self.request.user.id).exists():
            important_liked = True
        underrated_liked = False
        if post.underrated_likes.filter(id=self.request.user.id).exists():
            underrated_liked = True     
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "interesting_liked": interesting_liked,
                "important_liked": important_liked,
                "underrated_liked": underrated_liked,
                "comment_form": CommentForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        interesting_liked = False
        if post.interesting_likes.filter(id=self.request.user.id).exists():
            interesting_liked = True
        important_liked = False
        if post.important_likes.filter(id=self.request.user.id).exists():
            important_liked = True
        underrated_liked = False
        if post.underrated_likes.filter(id=self.request.user.id).exists():
            underrated_liked = True     

        comment_form = CommentForm(data=request.POST)
        if request.user.institution == '':
            comment_name = request.user.first_name + ' ' + request.user.last_name + ' – ' + request.user.role 
        else:
            comment_name = request.user.first_name + ' ' + request.user.last_name + ' – ' + request.user.role + ' – ' + request.user.institution

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = comment_name
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "interesting_liked": interesting_liked,
                "important_liked": important_liked,
                "underrated_liked": underrated_liked,
            },
        )
