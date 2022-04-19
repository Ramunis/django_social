from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import RegForm, SettForm, ComForm, EvenForm, ConfForm, ChatForm, MesForm
from .models import Theme, Community, Post, Comment, Pcom, Ecom, Pli, Eli, Like, Member, Event, Advert, Participant, Student, Subscribe, Board, Fac, Spec, Group
from django.contrib.auth.models import User
import datetime


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/accounts/profile')
    else:
        return render(request, "main/index.html")


def hello(request):
    return render(request, "main/hello.html")


def reg(request):
    if request.method == "POST":
        f = request.POST.get("F")
        i = request.POST.get("I")
        o = request.POST.get("O")
        un = request.POST.get("UN")
        pw = request.POST.get("PW")
        pw2 = request.POST.get("PW2")
        em = request.POST.get("EM")
        ph = request.POST.get("PH")
        dr = request.POST.get("DR")
        g = request.POST.get("G")
        fp = request.POST.get("FP")
        pic = request.POST.get("Pic")
        c = request.POST.get("C")
        de = request.POST.get("DE")
        fac = 1
        spe = 1
        grou = 1
        if fp == 1:
            fp = "Женат/Жената"
        else:
            fp = "Не женат/Не жената"
        ##output = "<h2>User</h2><h3>F - {0}, I - {1}, O - {2}, Login - {3}, PW - {4}, PW2 - {5}, Email - {6}, Phone - {7}, DR - {8}, Gender - {9}, Family - {10}, City - {11}, Enjoy - {12}, Facult - {13}, Spec - {14}, Grup - {15}, Pic - {16}</h3>".format(f, i, o, un, pw, pw2, em, ph, dr, g, fp, c, de, fac, spe, grou, pic)
        user = User.objects.create_user(un, em, pw)
        user.first_name = f+" "+i+" "+o
        user.last_name = pic
        user.save()
        stud = Student.objects.create(un=un, ey=de, f=f, i=i, o=o, dr=dr, male=g, family=fp, city=c, pic=pic, phone=ph, skype='Нет данных', telegram='Нет данных', discord='Нет данных', google='Нет данных', lang='Нет данных', about='Нет данных', activity='Нет данных', interest='Нет данных', music='Нет данных',  films='Нет данных', books='Нет данных', games='Нет данных', fac_id=fac, group_id=grou, spec_id=spe)
        stud.save()
        return HttpResponseRedirect('/reg1')
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect('/accounts/profile')
        else:
            rf = RegForm()
            return render(request, "registration/reg.html", {"form": rf})


def reg1(request):
    if request.method == "POST":
        fac = request.POST.get("area")
        spec = request.POST.get("area1")
        group = request.POST.get("area2")
        output = "<h2>User</h2><h3>F - {0}, S - {1}, G - {2}</h3>".format(fac, spec, group)
        obj = Student.objects.all().order_by('-pk')[0]
        stud = Student.objects.get(id=obj.pk)
        stud.fac_id = fac
        stud.spec_id = spec
        stud.group_id = group
        stud.save()
        return HttpResponseRedirect('/accounts/login')
    else:
        fac = Fac.objects.all()
        spec = Spec.objects.all()
        group = Group.objects.all()
        return render(request, "registration/reg1.html", {"fac": fac, "spec": spec, "group": group})


def settings(request):
    if request.method == "POST":
        f = request.POST.get("F")
        i = request.POST.get("I")
        o = request.POST.get("O")
        ##un = request.POST.get("UN")
        ##pw = request.POST.get("PW")
        ##pw2 = request.POST.get("PW2")
        ##em = request.POST.get("EM")
        ph = request.POST.get("PH")
        dr = request.POST.get("DR")
        ##g = request.POST.get("G")
        fp = request.POST.get("FP")
        c = request.POST.get("C")
        ##de = request.POST.get("DE")
        ##fac = request.POST.get("Fac")
        ##spe = request.POST.get("Spec")
        ##grou = request.POST.get("Group")
        pic = request.POST.get("Pic")
        skype = request.POST.get("Skype")
        telegram = request.POST.get("Telegram")
        discord = request.POST.get("Discord")
        google = request.POST.get("Google")
        about = request.POST.get("About")
        lang = request.POST.get("Lang")
        activ = request.POST.get("Activ")
        hobby = request.POST.get("Hobby")
        music = request.POST.get("Music")
        film = request.POST.get("Film")
        book = request.POST.get("Book")
        games = request.POST.get("Games")

        stud = Student.objects.get(un=request.user.username)
        stud.f = f
        stud.i = i
        stud.o = o
        stud.dr = dr
        stud.phone = ph
        stud.family = fp
        stud.city = c
        stud.pic = pic
        stud.skype = skype
        stud.telegram = telegram
        stud.discord = discord
        stud.google = google
        stud.lang = lang
        stud.about = about
        stud.activity = activ
        stud.interest = hobby
        stud.music = music
        stud.films = film
        stud.books = book
        stud.games = games
        stud.save()
        mainuser = User.objects.get(username=request.user.username)
        mainuser.first_name = f + " " + i + " " + o
        mainuser.last_name = pic
        mainuser.save()
        return HttpResponseRedirect('/accounts/profile')
    else:
        if request.user.is_authenticated:
            my = Student.objects.get(un=request.user.username)
            sf = SettForm(initial={'F': my.f, 'I': my.i, 'O': my.o, 'PH': my.phone, 'DR': my.dr,
    'FP': my.family, 'C': my.city, 'Pic': my.pic, 'Skype': my.skype, 'Telegram': my.telegram, 'Discord': my.discord, 'Google': my.google,
                                   'About': my.about, 'Lang': my.lang, 'Activ': my.activity, 'Hobby': my.interest,
                                   'Music': my.music, 'Film': my.films, 'Book': my.books, 'Games': my.games})
            return render(request, "main/setting.html", {"form": sf})
        else:
            return HttpResponseRedirect('/accounts/profile')


def profile(request):
    if request.user.is_authenticated:
        my = Student.objects.select_related('spec', 'group').filter(un=request.user.username)
        post = Board.objects.select_related('student').filter(student_id=request.user.id)
        com = Member.objects.select_related('community').filter(student_id=request.user.id)
        evs = Participant.objects.select_related('event').filter(student_id=request.user.id)
        mysubs = Subscribe.objects.filter(student_id=request.user.id)
        subs = Subscribe.objects.select_related('student').filter(slave=request.user.username)
        allsub = Subscribe.objects.filter(slave=request.user.username).count()
        allsubs = Subscribe.objects.filter(student_id=request.user.id).count()
        cominfo = {"allsub": allsub, "allsubs": allsubs}

        return render(request, "registration/profile.html", {"my": my, "post": post, "com": com, "evs": evs, "subs": subs, "mysubs": mysubs, "cominfo": cominfo})
    else:
        return render(request, "main/index.html")


def user(request, un):
    my = Student.objects.select_related('spec', 'group').filter(un=un)
    studid = Student.objects.get(un=un).id
    post = Board.objects.select_related('student').filter(student_id=studid)
    com = Member.objects.select_related('community').filter(student_id=studid)
    evs = Participant.objects.select_related('event').filter(student_id=studid)
    mysubs = Subscribe.objects.filter(student_id=studid)
    subs = Subscribe.objects.select_related('student').filter(slave=un)
    allsub = Subscribe.objects.filter(slave=un).count()
    allsubs = Subscribe.objects.filter(student_id=studid).count()

    member = Subscribe.objects.filter(student_id=studid, slave=request.user.username).count()
    if member > 0:
        header = "Вы подписаны"
        head = "Отписаться"
    else:
        header = "Вы не подписаны"
        head = "Подписаться"

    cominfo = {"header": header, "head": head, "sid": studid, "allsub": allsub, "allsubs": allsubs}
    return render(request, "main/user.html", {"my": my, "post": post, "com": com, "evs": evs, "subs": subs, "mysubs": mysubs, "cominfo": cominfo})


def post(request, pid):
    if request.method == "POST":
        text = request.POST.get("comment")
        now = datetime.date.today()
        dc = str(now)
        com = Comment.objects.create(com=text, dl=dc, board_id=pid, student_id=request.user.id)
        com.save()
        return HttpResponseRedirect('/accounts/profile')
    else:
        pos = Board.objects.select_related('student').filter(id=pid)
        com = Comment.objects.select_related('student', 'board').filter(board_id=pid)
        allcom = Comment.objects.filter(board_id=pid).count()
        alllike = Like.objects.filter(board_id=pid).count()
        cominfo = {"allcom": allcom, "alllike": alllike}
        return render(request, "main/post.html", {"pos": pos, "com": com, "cominfo": cominfo})


def like(request, lid):
    member = Like.objects.filter(student_id=request.user.id, board_id=lid).count()
    if member > 0:
        header = "Вы поставили лайк"
        head = "Убрать лайк"
        com = Like.objects.select_related('student', 'board').filter(board_id=lid)
        cominfo = {"header": header, "head": head, "lid": lid}
        return render(request, "main/like.html", {"com": com, "cominfo": cominfo})
    else:
        header = "Вы не ставили лайк"
        head = "Поставить лайк"
        com = Like.objects.select_related('student', 'board').filter(board_id=lid)
        cominfo = {"header": header, "head": head, "lid": lid}
        return render(request, "main/like.html", {"com": com, "cominfo": cominfo})


def nl(request, lid):
    member = Like.objects.filter(student_id=request.user.id, board_id=lid).count()
    if member > 0:
        header = "Вы поставили лайк"
        head = "Убрать лайк"
        lik = Like.objects.get(board_id=lid, student_id=request.user.id)
        lik.delete()
        return HttpResponseRedirect('/accounts/students')
    else:
        header = "Вы не ставили лайк"
        head = "Поставить лайк"
        now = datetime.date.today()
        dc = str(now)
        lik = Like.objects.create(dl=dc, board_id=lid, student_id=request.user.id)
        lik.save()
        return HttpResponseRedirect('/accounts/profile')


def comlike(request, lid):
    member = Pli.objects.filter(student_id=request.user.id, post_id=lid).count()
    if member > 0:
        header = "Вы поставили лайк"
        head = "Убрать лайк"
        com = Pli.objects.select_related('student', 'post').filter(post_id=lid)
        cominfo = {"header": header, "head": head, "lid": lid}
        return render(request, "main/comlike.html", {"com": com, "cominfo": cominfo})
    else:
        header = "Вы не ставили лайк"
        head = "Поставить лайк"
        com = Pli.objects.select_related('student', 'post').filter(post_id=lid)
        cominfo = {"header": header, "head": head, "lid": lid}
        return render(request, "main/comlike.html", {"com": com, "cominfo": cominfo})


def comnl(request, lid):
    member = Pli.objects.filter(student_id=request.user.id, post_id=lid).count()
    if member > 0:
        header = "Вы поставили лайк"
        head = "Убрать лайк"
        lik = Pli.objects.get(post_id=lid, student_id=request.user.id)
        lik.delete()
        return HttpResponseRedirect('/coms')
    else:
        header = "Вы не ставили лайк"
        head = "Поставить лайк"
        now = datetime.date.today()
        dc = str(now)
        lik = Pli.objects.create(dl=dc, post_id=lid, student_id=request.user.id)
        lik.save()
        return HttpResponseRedirect('/accounts/profile')


def evenlike(request, lid):
    member = Eli.objects.filter(student_id=request.user.id, advert_id=lid).count()
    if member > 0:
        header = "Вы поставили лайк"
        head = "Убрать лайк"
        com = Eli.objects.select_related('student', 'advert').filter(advert_id=lid)
        cominfo = {"header": header, "head": head, "lid": lid}
        return render(request, "main/eventlike.html", {"com": com, "cominfo": cominfo})
    else:
        header = "Вы не ставили лайк"
        head = "Поставить лайк"
        com = Eli.objects.select_related('student', 'advert').filter(advert_id=lid)
        cominfo = {"header": header, "head": head, "lid": lid}
        return render(request, "main/eventlike.html", {"com": com, "cominfo": cominfo})


def evennl(request, lid):
    member = Eli.objects.filter(student_id=request.user.id, advert_id=lid).count()
    if member > 0:
        header = "Вы поставили лайк"
        head = "Убрать лайк"
        lik = Eli.objects.get(advert_id=lid, student_id=request.user.id)
        lik.delete()
        return HttpResponseRedirect('/eves')
    else:
        header = "Вы не ставили лайк"
        head = "Поставить лайк"
        now = datetime.date.today()
        dc = str(now)
        lik = Eli.objects.create(dl=dc, advert_id=lid, student_id=request.user.id)
        lik.save()
        return HttpResponseRedirect('/accounts/profile')


def ns(request, sid):
    member = Subscribe.objects.filter(student_id=sid, slave=request.user.username).count()
    if member > 0:
        header = "Вы подписаны"
        head = "Отписаться"
        com = Subscribe.objects.get(student_id=sid, slave=request.user.username)
        com.delete()

    else:
        header = "Вы не подписаны"
        head = "Подписаться"
        now = datetime.date.today()
        dc = str(now)
        com = Subscribe.objects.create(slave=request.user.username, ds=dc, student_id=sid)
        com.save()

    ##return HttpResponse(cid)
    return HttpResponseRedirect('/accounts/profile')


def lent(request):
    if request.method == "POST":
        title = request.POST.get("title")
        text = request.POST.get("comment")
        img = request.POST.get("img")
        now = datetime.date.today()
        dc = str(now)
        com = Board.objects.create(title=title, text=text, img=img, dp=dc, student_id=request.user.id)
        com.save()
        return HttpResponseRedirect('/accounts/profile')
    else:
        if request.user.is_authenticated:
            return render(request, "main/lent.html")
        else:
            return HttpResponseRedirect('/accounts/login')


def search(request):
    return render(request, "main/search.html")


def students(request):
    if request.user.is_authenticated:
        fac = Fac.objects.all()
        student = Student.objects.select_related('spec', 'group')
        return render(request, "main/students.html", {"fac": fac, "student": student})
    else:
        return HttpResponseRedirect('/accounts/login')


def coms(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        tem = request.POST.get("Tem")
        stud = request.user.id
        about = request.POST.get("About")
        now = datetime.date.today()
        dc = str(now)
        site = request.POST.get("Site")
        email = request.POST.get("Email")
        telegram = request.POST.get("Telegram")
        pic = request.POST.get("Pic")
        ##output = "<h2>Community</h2><h3>Name - {0}, Theme - {1}, User - {2}, Site - {3}, Email - {4}, Telegram - {5},
        # Picture - {6}</h3>".format(name, tem, stud, site, email, telegram, pic)
        com = Community.objects.create(name=name, about=about, dc=dc, site=site, mail=email, telegram=telegram,
                                       pic=pic, student_id=stud, theme_id=tem)
        com.save()
        obj = Community.objects.all().order_by('-pk')[0]
        mem = Member.objects.create(dm=dc, community_id=obj.pk, student_id=stud)
        mem.save()
        return HttpResponseRedirect('/coms')
    else:
        if request.user.is_authenticated:
            cf = ComForm()
            themes = Theme.objects.all()
            communes = Community.objects.select_related('theme')
            return render(request, "main/coms.html", {"form": cf, "themes": themes, "communes": communes})
        else:
            return HttpResponseRedirect('/accounts/login')


def compost(request, pid):
    if request.method == "POST":
        text = request.POST.get("comment")
        now = datetime.date.today()
        dc = str(now)
        com = Pcom.objects.create(com=text, dl=dc, post_id=pid, student_id=request.user.id)
        com.save()
        return HttpResponseRedirect('/accounts/profile')
    else:
        pos = Post.objects.select_related('student').filter(id=pid)
        com = Pcom.objects.select_related('student', 'post').filter(post_id=pid)
        allcom = Pcom.objects.filter(post_id=pid).count()
        alllike = Pli.objects.filter(post_id=pid).count()
        cominfo = {"allcom": allcom, "alllike": alllike}
        return render(request, "main/compost.html", {"pos": pos, "com": com, "cominfo": cominfo})


def eves(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        tem = request.POST.get("Tem")
        stud = request.user.id
        now = datetime.date.today()
        dc = str(now)
        adr = request.POST.get("Adr")
        dt = request.POST.get("DT")
        sp = request.POST.get("Sp")
        about = request.POST.get("About")
        site = request.POST.get("Site")
        email = request.POST.get("Email")
        telegram = request.POST.get("Telegram")
        pic = request.POST.get("Pic")
        ##output = "<h2>Event</h2><h3>Name - {0}, Theme - {1}, Adres - {2}, Date - {3}, Sponsor - {4}, About - {5}, Site - {6}, Email - {7}, Telegram - {8}, Picture - {9}</h3>".format(name, tem, adr, dt, sp, about, site, email, telegram, pic)
        even = Event.objects.create(name=name, about=about, de=dc, adr=adr, sp=sp, dc=dt, site=site,
                                    mail=email, telegram=telegram, pic=pic, student_id=stud, theme_id=tem)
        even.save()
        obj = Event.objects.all().order_by('-pk')[0]
        par = Participant.objects.create(dp=dc, event_id=obj.pk, student_id=stud)
        par.save()
        return HttpResponseRedirect('/eves')
    else:
        if request.user.is_authenticated:
            ef = EvenForm()
            themes = Theme.objects.all()
            evs = Event.objects.select_related('theme')
            return render(request, "main/eves.html", {"form": ef, "themes": themes, "evs": evs})
        else:
            return HttpResponseRedirect('/accounts/login')


def filtre(request, fid):
    if request.user.is_authenticated:
        ef = EvenForm()
        themes = Theme.objects.all()
        evs = Event.objects.select_related('theme').filter(theme_id=fid)
        return render(request, "main/eves.html", {"form": ef, "themes": themes, "evs": evs})
    else:
        return HttpResponseRedirect('/accounts/login')


def filtrc(request, fid):
        if request.user.is_authenticated:
            cf = ComForm()
            themes = Theme.objects.all()
            communes = Community.objects.select_related('theme').filter(theme_id=fid)
            return render(request, "main/coms.html", {"form": cf, "themes": themes, "communes": communes})
        else:
            return HttpResponseRedirect('/accounts/login')


def filtrs(request, fid):
    if request.user.is_authenticated:
        fac = Fac.objects.all()
        student = Student.objects.select_related('spec', 'group').filter(fac_id=fid)
        return render(request, "main/students.html", {"fac": fac, "student": student})
    else:
        return HttpResponseRedirect('/accounts/login')


def finds(request):
    if request.method == "POST":
        q = request.POST.get("s")
        student = Student.objects.select_related('spec', 'group').filter(f__contains=q)
        coms = Community.objects.select_related('theme').filter(name__contains=q)
        eves = Event.objects.select_related('theme').filter(name__contains=q)
        return render(request, "main/search.html", {"student": student, "coms": coms, "eves": eves})
    else:
        return HttpResponseRedirect('/accounts/login')


def epost(request, pid):
    if request.method == "POST":
        text = request.POST.get("comment")
        now = datetime.date.today()
        dc = str(now)
        com = Ecom.objects.create(com=text, dl=dc, advert_id=pid, student_id=request.user.id)
        com.save()
        return HttpResponseRedirect('/accounts/profile')
    else:
        pos = Advert.objects.select_related('student').filter(id=pid)
        com = Ecom.objects.select_related('student', 'advert').filter(advert_id=pid)
        allcom = Ecom.objects.filter(advert_id=pid).count()
        alllike = Eli.objects.filter(advert_id=pid).count()
        cominfo = {"allcom": allcom, "alllike": alllike}
        return render(request, "main/epost.html", {"pos": pos, "com": com, "cominfo": cominfo})


def spec(request):
    if request.user.is_authenticated:
        studid = Student.objects.get(un=request.user.username).spec_id
        special = Spec.objects.select_related('fac').filter(id=studid)
        groups = Group.objects.select_related('spec').filter(spec_id=studid)
        facid = Student.objects.get(un=request.user.username).fac_id
        student = Student.objects.select_related('spec', 'group').filter(fac_id=facid)
        return render(request, "main/spec.html", {"special": special, "groups": groups, "student": student})
    else:
        return HttpResponseRedirect('/accounts/login')


def group(request):
    if request.user.is_authenticated:
        studid = Student.objects.get(un=request.user.username).group_id
        groups = Group.objects.select_related('spec').filter(id=studid)
        groupid = Group.objects.get(id=studid).id
        student = Student.objects.select_related('spec', 'group').filter(group_id=groupid)
        return render(request, "main/group.html", {"groups": groups, "student": student})
    else:
        return HttpResponseRedirect('/accounts/login')


def community(request, cid):
    if request.method == "POST":
        title = request.POST.get("title")
        text = request.POST.get("comment")
        img = request.POST.get("img")
        now = datetime.date.today()
        dc = str(now)
        member = Member.objects.filter(student_id=request.user.id, community_id=cid).count()
        if member > 0:
            header = "Вы состоите в сообществе"
            head = "Выйти"
            com = Post.objects.create(title=title, text=text, img=img, dp=dc, community_id=cid, student_id=request.user.id)
            com.save()
            return HttpResponseRedirect('/lent')
        else:
            header = "Вы не состоите в сообществе"
            head = "Вступить"
            return HttpResponseRedirect('/coms')
    else:
        communes = Community.objects.select_related('theme', 'student').filter(id=cid)
        post = Post.objects.select_related('student').filter(community_id=cid)
        mem = Member.objects.select_related('student').filter(community_id=cid)
        memfour = Member.objects.select_related('student').filter(community_id=cid)[:4]

        allmemb = Member.objects.filter(community_id=cid).count()
        allpost = Post.objects.filter(community_id=cid).count()
        member = Member.objects.filter(student_id=request.user.id, community_id=cid).count()
        if member > 0:
            header = "Вы состоите в сообществе"
            head = "Выйти"
        else:
            header = "Вы не состоите в сообществе"
            head = "Вступить"

        cominfo = {"header": header, "head": head, "cid": cid, "allmemb": allmemb, "allpost": allpost}
        return render(request, "main/community.html",
                      {"communes": communes, "mem": mem, "memfour": memfour, "post": post, "cominfo": cominfo})


def am(request, cid):
    member = Member.objects.filter(student_id=request.user.id, community_id=cid).count()
    if member > 0:
        header = "Вы состоите в сообществе"
        head = "Выйти"
        com = Member.objects.get(community_id=cid, student_id=request.user.id)
        com.delete()

    else:
        header = "Вы не состоите в сообществе"
        head = "Вступить"
        now = datetime.date.today()
        dc = str(now)
        com = Member.objects.create(dm=dc, community_id=cid, student_id=request.user.id)
        com.save()

    ##return HttpResponse(cid)
    return HttpResponseRedirect('/accounts/profile')


def event(request, eid):
    if request.method == "POST":
        title = request.POST.get("title")
        text = request.POST.get("comment")
        img = request.POST.get("img")
        now = datetime.date.today()
        dc = str(now)
        member = Participant.objects.filter(student_id=request.user.id, event_id=eid).count()
        if member > 0:
            header = "Вы состоите в сообществе"
            head = "Выйти"
            com = Advert.objects.create(title=title, text=text, img=img, dp=dc, event_id=eid, student_id=request.user.id)
            com.save()
            return HttpResponseRedirect('/lent')
        else:
            header = "Вы не состоите в сообществе"
            head = "Вступить"
            return HttpResponseRedirect('/eves')
    else:
        communes = Event.objects.select_related('theme', 'student').filter(id=eid)
        post = Advert.objects.select_related('student').filter(event_id=eid)
        mem = Participant.objects.select_related('student').filter(event_id=eid)
        memfour = Participant.objects.select_related('student').filter(event_id=eid)[:4]

        allmemb = Participant.objects.filter(event_id=eid).count()
        allpost = Advert.objects.filter(event_id=eid).count()
        member = Participant.objects.filter(student_id=request.user.id, event_id=eid).count()
        if member > 0:
            header = "Вы учавствуйте в мероприятии"
            head = "Уйти"
        else:
            header = "Вы не учавствуйте в мероприятии"
            head = "Вступить"

        cominfo = {"header": header, "head": head, "eid": eid, "allmemb": allmemb, "allpost": allpost}
        return render(request, "main/event.html",
                      {"communes": communes, "mem": mem, "memfour": memfour, "post": post, "cominfo": cominfo})


def ap(request, eid):
    member = Participant.objects.filter(student_id=request.user.id, event_id=eid).count()
    if member > 0:
        header = "Вы состоите в сообществе"
        head = "Выйти"
        com = Participant.objects.get(event_id=eid, student_id=request.user.id)
        com.delete()

    else:
        header = "Вы не состоите в сообществе"
        head = "Вступить"
        now = datetime.date.today()
        dc = str(now)
        com = Participant.objects.create(dp=dc, event_id=eid, student_id=request.user.id)
        com.save()

    ##return HttpResponse(cid)
    return HttpResponseRedirect('/accounts/profile')


