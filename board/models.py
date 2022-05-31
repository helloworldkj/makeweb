#장고는 모델을 이용하여 DB를 처리한다.
from django.db import models
from django.conf import settings
class Post(models.Model):
    subject= models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #사용자가 삭제되면 글도 삭제
    content=models.TextField()
    create_date=models.DateTimeField()

    def __str__(self):
        return self.subject