from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


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
                "interesting_liked": interesting_liked,
                "important_liked": important_liked,
                "underrated_liked": underrated_liked
            }
        )
