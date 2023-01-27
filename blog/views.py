from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, UpdatePostForm
from django.contrib import messages
from django.db.models import Count


# Delete post instance
def delete_post(request, slug):
	post = Post.objects.get(slug=slug)
	if request.user.is_superuser:
		post.delete()
		messages.success(request, ("Event Deleted!"))
		return redirect('home')
	else:
		messages.success(request, ("You Aren't Authorized To Delete This Post!"))
		return redirect('home')


# Add post instance
def add_post(request):
	submitted = False
	if request.method == "POST":
		form = UpdatePostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user  # logged in user
			post.save()
			# form.save()
			return redirect('home')
	else:
		form = UpdatePostForm
		if 'submitted' in request.GET:
			submitted = True

	return render(request, 'add_post.html', {'form': form, 'submitted': submitted})


# update a post
def update_post(request, slug):
	post = Post.objects.get(slug=slug)
	if request.user.is_superuser:
		form = UpdatePostForm(request.POST or None, request.FILES or None, instance=post)
	else:
		form = UpdatePostForm(request.POST or None, request.FILES or None, instance=post)

	if form.is_valid():
		form.save()
		return redirect('home')

	return render(request, 'update_post.html', {'post': post, 'form': form})


# Display the homepage with a listview
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


# Display the an alternate version of the homepage with a filtered listview (see html page for filter)
class PostListInteresting(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'filter_interesting.html'
    paginate_by = 6


# Display the an alternate version of the homepage with a filtered listview (see html page for filter)
class PostListImportant(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'filter_important.html'
    paginate_by = 6


# Display the an alternate version of the homepage with a filtered listview (see html page for filter)
class PostListUnderrated(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'filter_underrated.html'
    paginate_by = 6


# Display the Post webpage
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


# Add functionality for users to like posts
class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if self.request.POST.get('interesting'):
            if post.interesting_likes.filter(id=request.user.id).exists():
                post.interesting_likes.remove(request.user)
            else:
                post.interesting_likes.add(request.user)
        elif self.request.POST.get('important'):
            if post.important_likes.filter(id=request.user.id).exists():
                post.important_likes.remove(request.user)
            else:
                post.important_likes.add(request.user)
        elif self.request.POST.get('underrated'):
            if post.underrated_likes.filter(id=request.user.id).exists():
                post.underrated_likes.remove(request.user)
            else:
                post.underrated_likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
