from django.db import models
from django.forms import forms


# Create your models here.


class Fac(models.Model):
    name = models.CharField(max_length=60)


class Spec(models.Model):
    fac = models.ForeignKey(Fac, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)


class Group(models.Model):
    spec = models.ForeignKey(Spec, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    ey = models.DateField()


class Student(models.Model):
    fac = models.ForeignKey(Fac, on_delete=models.DO_NOTHING)
    spec = models.ForeignKey(Spec, on_delete=models.DO_NOTHING)
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    un = models.CharField(max_length=60)
    ey = models.DateField()
    f = models.CharField(max_length=60)
    i = models.CharField(max_length=60)
    o = models.CharField(max_length=60)
    dr = models.DateField()
    male = models.CharField(max_length=20)
    family = models.CharField(max_length=30)
    city = models.CharField(max_length=60)
    pic = models.CharField(max_length=2000)
    phone = models.CharField(max_length=20)
    skype = models.CharField(max_length=60)
    telegram = models.CharField(max_length=60)
    discord = models.CharField(max_length=60)
    google = models.CharField(max_length=60)
    about = models.TextField()
    lang = models.TextField()
    about = models.TextField()
    activity = models.TextField()
    interest = models.TextField()
    music = models.TextField()
    films = models.TextField()
    books = models.TextField()
    games = models.TextField()


class Subscribe(models.Model):
    student = models.ForeignKey(Student,  on_delete=models.DO_NOTHING)
    slave = models.CharField(max_length=60)
    ds = models.DateField()


class Board(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=60)
    text = models.TextField()
    img = models.CharField(max_length=2000)
    dp = models.DateField()


class Comment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    com = models.TextField()
    dl = models.DateField()


class Like(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    dl = models.DateField()


class Theme(models.Model):
    name = models.CharField(max_length=60)


class Community(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=60)
    about = models.TextField()
    dc = models.DateField()
    site = models.CharField(max_length=60)
    mail = models.CharField(max_length=60)
    telegram = models.CharField(max_length=60)
    pic = models.CharField(max_length=2000)


class Member(models.Model):
    student = models.ForeignKey(Student,  on_delete=models.DO_NOTHING)
    community = models.ForeignKey(Community, on_delete=models.DO_NOTHING)
    dm = models.DateField()


class Post(models.Model):
    community = models.ForeignKey(Community, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=60)
    text = models.TextField()
    img = models.CharField(max_length=2000)
    dp = models.DateField()


class Pcom(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    com = models.TextField()
    dl = models.DateField()


class Pli(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    dl = models.DateField()


class Event(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=60)
    about = models.TextField()
    de = models.DateField()
    adr = models.CharField(max_length=100)
    sp = models.CharField(max_length=100)
    dc = models.DateField()
    site = models.CharField(max_length=60)
    mail = models.CharField(max_length=60)
    telegram = models.CharField(max_length=60)
    pic = models.CharField(max_length=2000)


class Participant(models.Model):
    student = models.ForeignKey(Student,  on_delete=models.DO_NOTHING)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    dp = models.DateField()


class Advert(models.Model):
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=60)
    text = models.TextField()
    img = models.CharField(max_length=2000)
    dp = models.DateField()


class Ecom(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE)
    com = models.TextField()
    dl = models.DateField()


class Eli(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE)
    dl = models.DateField()





