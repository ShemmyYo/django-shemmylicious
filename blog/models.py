from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    # recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100, unique=True, null=False, blank=False)

    class Meta:
        ordering = ['category_name']

    def __str__(self):
        return self.category_name


class Recipe(models.Model):
    recipe_title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    featured_image = CloudinaryField('image', default='recipe')
    recipe_ingridients = models.TextField()
    recipe_instructions = models.TextField()
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
