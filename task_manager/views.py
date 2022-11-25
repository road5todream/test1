import task_manager as tm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


def main_page(request: tm.HttpRequest) -> tm.HttpResponse:
    return tm.render(request, 'base.html')


class Login(tm.SuccessMessageMixin,
            LoginView,
            ):

    form_class = AuthenticationForm
    template_name = 'login.html'
    success_message = tm.FlashMessages.LOGIN_SUCCESS.value

    def get_success_url(self):
        return tm.reverse_lazy('main_page')


def logout_user(request):
    logout(request)
    tm.messages.success(request, tm.FlashMessages.LOGOUT_SUCCESS.value)
    return tm.redirect('main_page')
