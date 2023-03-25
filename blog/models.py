from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify

STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    featured_image = CloudinaryField('image', default='featured-recipe')

    class Meta:
        ordering = ['category_name']

    def __str__(self):
        return self.category_name


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return str(self.user)


class Recipe(models.Model):
    recipe_title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, null=False)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    featured_image = CloudinaryField('image', default='recipe')
    # models.FileField(null=True, blank=True, upload_to='Shemmylicious/', default="media/Shemmylicious/shemmylicious-logo_szrask")
    featured_comment = models.TextField(null=False, default="Shemmylicious Food")
    recipe_ingridients = models.TextField(blank=True)
    recipe_instructions = models.TextField(blank=True)
    excerpt = models.TextField(blank=True)
    likes = models.ManyToManyField(User, related_name="blog_likes", blank=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.recipe_title

    def number_of_likes(self):
        return self.likes.count() 


class Comment(models.Model):
    recipe_name = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    comment_title = models.CharField(max_length=80)
    comment_body = models.TextField()
    email = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return f"Comment {self.comment_body} by {self.comment_title}, posted: {self.created_date}"
