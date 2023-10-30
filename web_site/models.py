from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy


User._meta.get_field('email')._unique = True


class Category(models.Model):
    title = models.CharField(max_length=150)

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
    
class Ip(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_posts', blank=True)
    views = models.ManyToManyField(Ip, related_name='post_views', blank=True)

    def __str__(self):
        return self.title
    
    def photo_url(self):
        try:
            url = self.photo.url
        except:
            url = 'https://i5.walmartimages.com/asr/9da1bfb1-6e4c-41bc-b28f-c20a19b78452.6274ced12951e94c262c39218dde8a05.png'
        return url
    
    def views_count(self):
        return self.views.count()
    
    def like_count(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse_lazy('post', kwargs={'pk': self.pk})
    

    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, null=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='''Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Maecenas tortor mauris, maximus nec ipsum euismod, auctor vehicula ipsum.
''', max_length=135)
    phone = models.CharField(max_length=20, default='---------', blank=True)
    mobile = models.CharField(max_length=20, default='---------', blank=True)
    address = models.CharField(max_length=120, default='Uzbekistan', blank=True)
    profile_pic = models.ImageField(blank=True, upload_to='images/profile')
    website_url = models.CharField(max_length=255, default='#', blank=True)
    github_url = models.CharField(max_length=255, default='#', blank=True)
    instagram_url = models.CharField(max_length=255, default='#', blank=True)
    facebook_url = models.CharField(max_length=255, default='#', blank=True)
    telegram_url = models.CharField(max_length=255, default='#', blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def image_url(self):
        try:
            url = self.profile_pic.url
        except:
            url = 'https://us.123rf.com/450wm/tuktukdesign/tuktukdesign1608/tuktukdesign160800043/61010830-user-icon-man-profile-businessman-avatar-person-glyph-vector-illustration.jpg?ver=6'
        return url

    
     

