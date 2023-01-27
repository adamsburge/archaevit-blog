from django.db import models
from django.contrib.auth.models import User, AbstractUser
from cloudinary.models import CloudinaryField
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))


# Model 1: Extends default user model and adds extras fields
class NewUser(AbstractUser):
    institution = models.CharField(max_length=100)
    role = models.CharField(max_length=100)


# Model 2: Model for archaeological site posts
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name="blog_post")
    updated_on = models.DateTimeField(auto_now=True)
    country = models.CharField(max_length=50)
    dates = models.CharField(max_length=50)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    interesting_likes = models.ManyToManyField(NewUser, related_name='blog_interesting_likes', blank=True)
    important_likes = models.ManyToManyField(NewUser, related_name='blog_important_likes', blank=True)
    underrated_likes = models.ManyToManyField(NewUser, related_name='blog_underrated_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def number_of_interesting_likes(self):
        return self.interesting_likes.count()

    def number_of_important_likes(self):
        return self.important_likes.count()

    def number_of_underrated_likes(self):
        return self.underrated_likes.count()


# Model 3: Model for Comments
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
