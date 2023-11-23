from django.db import models
from django.contrib.auth.models import User

NEWS_OR_ARTICLE = [
    ('article', 'Статья'),
    ('news', 'Новость'),
]


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Author_rating = models.IntegerField(default=0)
 
    def update_rating(self):
        self.Author_rating = 0
        post,comment = 1, 1

        for post in Post.objects.filter(author=self):
            self.Author_rating += post.post_rating*3

        for comment in Comment.objects.filter(user=self):
            self.Author_rating += comment.comment_rating

        for comment in Comment.objects.filter(post__author=self):
            self.Author_rating += comment.comment_rating
        Author.objects.filter(id=self.id).update(Author_rating=self.Author_rating)


class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=100)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_of_post = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('category', through='PostCategory')
    title_of_post = models.CharField(max_length=255)
    post_text = models.TextField()
    news_or_article = models.CharField(max_length=8, choices=NEWS_OR_ARTICLE, default='article')
    post_rating = models.IntegerField(default=0)

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        return self.post_text[:124] + '...' if len(self.post_text) > 124 else self.post_text
    

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    comment_text = models.TextField()
    date_of_comment = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()

