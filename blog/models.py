from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(null=True, max_length=150, db_index=True)
    slug = models.SlugField(null=True, unique=True)
    class Meta:
        ordering = ('-name',)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('posts:posts_by_category', args=[self.slug])

class Post(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=350)
    slug = models.SlugField(max_length=450, null=True, unique_for_date='publish')
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    content = models.TextField(null=True)
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='all_posts')
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager

    def get_absolute_url(self):
       return reverse('posts:post_detail',args=[self.id,])

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title

class Mysociallinks(models.Model):
    email = models.CharField(null=True, max_length=150)
    github = models.CharField(null=True, max_length=150)
    instagram = models.CharField(null=True, max_length=150)
    myportfolio = models.CharField(null=True, max_length=150)
    facebook = models.CharField(null=True, max_length=150)
    youtube = models.CharField(null=True, max_length=150)
    telegram = models.CharField(null=True, max_length=150)
    aboutmyself = models.TextField(null=True)

    def __str__(self):
        return self.email