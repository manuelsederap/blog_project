from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Post(models.Model):
    """Database Post Model for a blog project"""
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        """When call set the published date"""
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        """Return only approved comments from comments"""
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        """Back to post detail url after this intances"""
        return reverse("post_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    """Database Comment Model for a blog project"""
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        """When call update approved comment to True"""
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        """Back to post list url after this intances"""
        return reverse("post_list")

    def __str__(self):
        return self.text
