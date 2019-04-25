from django.db import models
from django.db.models.signals import post_save, pre_save, post_delete
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title



def on_post_delete(sender, instance, **kwargs):
    print(f'instance {instance.id}')

def save_post(sender, instance, **kwargs):
    for i in range(0,4):
        cmnt = Comment.objects.create(comm=f"I am the comment{i}",post_id=instance.id)

def just_post_check(sender, instance, **kwargs):
    print("Posts count", Post.objects.all().count())
    print("Posts count", Comment.objects.all().count())

def just_comment_check(sender, instance, **kwargs):
    print("Posts count", Post.objects.all().count())
    print("Posts count", Comment.objects.all().count())


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comm = models.TextField()


def comment_save(sender, instance, **kwargs):
    print(instance.id)

post_save.connect(save_post, sender=Post)
post_save.connect(just_post_check, sender=Post)
post_delete.connect(on_post_delete, sender=Post)


post_save.connect(comment_save, sender=Comment)
post_save.connect(just_comment_check, sender=Comment)
post_delete.connect(on_post_delete, sender=Comment)
