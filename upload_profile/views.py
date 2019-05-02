from django.shortcuts import render
from .models import User  # 新增的程式碼
from .facedect import Facedect


def index(request):
    return render(request, 'upload_profile/index.html')


def addmyface(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        user_img = request.FILES.get('user_image')
        introduce = request.POST.get('introduce')
        user = User(user_name=user_name,
                    user_image=user_img, introduce=introduce)
        user.save()
        return render(request, 'upload_profile/addmyface.html', locals())

    return render(request, 'upload_profile/addmyface.html', locals())


def facelist(request):
    users = User.objects.all()
    return render(request, 'upload_profile/facelist.html', locals())


def whoami(request):
    whosface = Facedect(User).face_names  # return a name list
    print("whosface" + str(whosface))

    if len(whosface) != 0:
        for user in User.objects.all():
            print("user:" + str(user))
            print("whosface[0]" + whosface[0])
            if whosface[0] == user.user_name:
                themen = user
    else:
        themen = None

    print(themen)
    return render(request, 'upload_profile/whoami.html', locals())
