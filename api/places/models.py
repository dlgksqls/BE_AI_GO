from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Place(models.Model):
    name = models.CharField(verbose_name="장소명", max_length=150)
    image = models.ImageField(verbose_name="장소이미지", null=True, blank=True)
    branch = models.CharField(verbose_name="지점명", max_length=150)
    classification = models.CharField(verbose_name="상권업종대분류명", max_length=150)
    industry_classification = models.CharField(verbose_name="상권업종소분류명", max_length=300)
    city_county = models.CharField(verbose_name="시군구명", max_length=150)
    Administrative = models.CharField(verbose_name="행정동명", max_length=150)
    legal = models.CharField(verbose_name="법정동명", max_length=150)
    adress = models.TextField(verbose_name="지번주소")
    building = models.CharField(verbose_name="건물명", max_length=150)
    street_name_address = models.TextField(verbose_name="도로명주소", max_length=150)
    zip_code = models.CharField(verbose_name="우편번호", max_length=150)
    floor = models.IntegerField(verbose_name="층정보")
    hardnesss = models.FloatField(verbose_name="경도")
    latitude = models.FloatField(verbose_name="위도")

    info = models.TextField(verbose_name="장소정보")
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
