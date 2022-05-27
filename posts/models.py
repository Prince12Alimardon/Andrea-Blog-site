from django.db import models

# Create your models here.

TYPE = (
    (0, 'FASHION'),
    (1, 'TRAVEL'),
)


class Tag(models.Model):
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.tag


class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


# get_<file_name>_display
def post_image_path(instance, filename):
    return f'posts/{instance.get_type_display()}/{filename}'


class Post(models.Model):
    title = models.CharField(max_length=255)
    type = models.IntegerField(choices=TYPE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField()
    image = models.ImageField(upload_to=post_image_path)
    content = models.TextField()
    tag = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='comments')
    website = models.URLField(null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
