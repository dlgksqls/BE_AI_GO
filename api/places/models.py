from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Place(models.Model):
    name = models.CharField(verbose_name="장소명", max_length=100)
    image = models.ImageField(verbose_name="장소이미지", null=True, blank=True)
    info = models.TextField(verbose_name="장소정보")
    address = models.CharField(verbose_name="장소주소", max_length=100)
    like = models.IntegerField(verbose_name="좋아요수", default=0)
    tag = models.ForeignKey(to="Tag", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(verbose_name="태그명", max_length=50, primary_key=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    content = models.TextField(verbose_name="리뷰내용")
    image = models.ImageField(verbose_name="리뷰이미지", null=True, blank=True)
    score = models.IntegerField(verbose_name="리뷰점수")
    created_at = models.DateTimeField(verbose_name="리뷰작성일", auto_now_add=True)
    place = models.ForeignKey(
        to="Place", on_delete=models.CASCADE
    )  # 1:N 관계일 경우, N이 되는 쪽에 ForeignKey를 해줘야 함. to와 on_delete는 필수고 to에는 1의 클래스 이름을 넣자.cc
    writer = models.ForeignKey(
        to=User, on_delete=models.CASCADE, null=False, blank=False
    )

    def __str__(self):
        return self.content
