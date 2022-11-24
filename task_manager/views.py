import task_manager.services as svs
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


def main_page(request: svs.HttpRequest) -> svs.HttpResponse:
    return svs.render(request, 'base.html')


class Login(svs.SuccessMessageMixin,
            LoginView,
            ):

    form_class = AuthenticationForm
    template_name = 'login.html'
    success_message = svs.FlashMessages.LOGIN_SUCCESS.value
    success_url = 'users'
    redirect_authenticated_user = '/'


def logout_user(request):
    logout(request)
    svs.messages.success(request, svs.FlashMessages.LOGOUT_SUCCESS.value)
    return svs.redirect('main_page')
