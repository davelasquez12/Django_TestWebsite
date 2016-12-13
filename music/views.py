from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Album


# Create your views here.
def index(request):
    # if not request.user.is_authenticated():
    #     return redirect('music:login')
    # else:
        albums = Album.objects.all()
        context = {'albums': albums}
        return render(request, 'music/index.html', context)


def detail(request, album_id):
    if not request.user.is_authenticated():
        return redirect('music:login')

    album = get_object_or_404(Album, id=album_id)
    return render(request, 'music/detail.html', {'album': album})


def login_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('music:index')
        else:
            context = {'error_message': 'Username or password are incorrect', 'username': username}
            return render(request, 'music/login_form.html', context)

    return render(request, 'music/login_form.html')


def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        errors = is_valid(username, email, password)
        if errors is None:
            user = User.objects.create_user(username, email, password)
            user.save()
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                albums = Album.object.all()
                return render(request, 'music/index.html', {'albums': albums})
        else:
            errors['username'] = username
            errors['email'] = email
            return render(request, 'music/registration_form.html', errors)

    return render(request, 'music/registration_form.html')


def is_valid(username, email, password):
    errors = {'username_error': None, 'email_error': None, 'password_error': None}
    if not username:
        errors['username_error'] = 'Username field cannot be blank'

    if not email:
        errors['email_error'] = 'Email field cannot be blank'

    if not password:
        errors['password_error'] = 'Password field cannot be blank'

    for value in errors:
        if value is None:
            continue
        else:
            return errors

    return None


# def favorite(request, album_id):
#     album = get_object_or_404(Album, id=album_id)
#     try:
#         selected_song = album.song_set.get(id=request.POST['song'])
#     except(KeyError, Song.DoesNotExist):
#         return render(request, 'music/detail.html', {
#             'album': album,
#             'error_message': "You did not select a valid song",
#         })
#     else:
#         selected_song.is_favorite = True
#         selected_song.save()
#         return render(request, 'music/detail.html', {'album': album})


# class CreateAlbum(CreateView):
#     model = Album
#     fields = ['artist', 'title', 'genre', 'logo']
#     # No template_name is needed here because the template "album_form.html" is the
#     # default template these view classes use. It automatically looks up what model
#     # it is using (Album in this case) and then looks for "album_form" in the templates folder.
#     # The template must be in this form to work: <model>_form.html
#
#
# class UserFormView(View):
#     form_class = UserForm
#     template_name = 'music/registration_form.html'
#
#     # display blank form
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {'form': form})
#
#     # process form data
#     def post(self, request):
#         form = self.form_class(request.POST)
#
#         if form.is_valid():
#             user = form.save(commit=False)
#
#             # cleaned (normalized) data
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user.set_password(password)
#             user.save()
#
#             # returns User objects if credentials are correct
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)    # attaches a session automatically
#                     return redirect('music:index')
#
#         return render(request, self.template_name, {'form': form})




