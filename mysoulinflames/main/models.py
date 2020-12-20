import self as self
from django.contrib.auth.models import User
from django.db import models

# class Article(models.Model):
#     class Meta:
#         verbose_name = 'article'
#         verbose_name_plural = 'articles'

    # title = models.CharField(
    #     max_length=5000,
    #     verbose_name='Название',
    #     help_text='название статьи')

    # date = models.DateTimeField(auto_now_add=True, null=True)
    # text = models.TextField()
    # authors = models.ManyToManyField(User, related_name='article')
    # likes = models.PositiveIntegerField(default=0)
    # users_like = models.ManyToManyField(User, through='mysoulinflames.LikeArticleUser', related_name='liked_article')
    #
    # def __str__(self):
    #     return f'{self.title}{self.id}'


# class LikeArticleUser(models.Model):
#     class Meta:
#         unique_together = ('user', 'article')
#
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_article_table')
#     article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='liked_user_table')

        # def save(self, **kwargs):
        #     try:
        #         super().save(**kwargs)
        #     except:
        #         LikeArticleUser.objects.get(user=self.user, article=self.article).delete()


class Task(models.Model):
    title = models.CharField('Название', max_length=5000)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
