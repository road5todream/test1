import task_manager.services as svs
from .forms import LoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


def main_page(request: svs.HttpRequest) -> svs.HttpResponse:
    return svs.render(request, 'index.html')


class Login(svs.SuccessMessageMixin,
            LoginView,
            ):

    form_class = LoginForm
    template_name = 'login.html'
    success_message = 'Success'
    success_url = 'users'
    redirect_authenticated_user = '/'


def logout_user(request):
    logout(request)
    return svs.redirect('main_page')
