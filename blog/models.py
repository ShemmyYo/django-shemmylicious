from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from django.dispatch import receiver
from django.db import models
from django.db.models.signals import pre_save
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    category_name = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False
        )
    featured_image = CloudinaryField('cat image', default='cat_recipe')
    featured_comment = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        unique=False
        )
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['category_name']

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('recipe-mylist',)


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = CloudinaryField('profile image', default='profile_img')
    website_url = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        unique=True
        )
    facebook_url = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        unique=True
        )
    twitter_url = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        unique=True
        )
    instagram_url = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        unique=True
        )
    pintrest_url = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        unique=True
        )

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('recipes',)


class Recipe(models.Model):
    recipe_title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, null=False)
    status = models.IntegerField(choices=STATUS, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    featured_image = CloudinaryField('recipe image', default='recipe')
    featured_comment = models.TextField(null=False)
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
    
    def get_absolute_url(self):
        return reverse('recipe-mylist',)


@receiver(pre_save, sender=Recipe)
def store_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.recipe_title)


class Comment(models.Model):
    recipe_name = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments'
        )
    comment_title = models.CharField(max_length=80)
    comment_body = models.TextField()
    post_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_author = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return f"Comment {self.comment_body} by {self.post_author}, posted: {self.created_date}"
