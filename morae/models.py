from django.db import models
from django.conf import settings
# Create your models here.

def user_path(instance, filename): #파라미터 instance는 Photo 모델을 의미 filename은 업로드 된 파일의 파일 이름
    from random import choice
    import string # string.ascii_letters : ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr) # 8자리 임의의 문자를 만들어 파일명으로 지정
    extension = filename.split('.')[-1] # 배열로 만들어 마지막 요소를 추출하여 파일확장자로 지정
    # file will be uploaded to MEDIA_ROOT/user_<id>/<random>
    return '%s.%s' % (pid, extension) # 예 : wayhome/abcdefgs.png



class Family (models.Model):
    kakao = models.CharField(max_length=200)
    state = models.CharField(max_length=4)
    address = models.CharField(max_length=200)
    gmoney = models.CharField(max_length=200)
    kmoney = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    gphoto = models.FileField(null=True)
    tphoto = models.FileField(null=True)
    detail = models.CharField(max_length=200)
    writepw = models.CharField(max_length=200)
