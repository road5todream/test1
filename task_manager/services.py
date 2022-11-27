import task_manager as tm


class UserChangeAccessMixin:

    redirect_field_name = None

    def has_permission(self) -> bool:
        return self.get_object().pk == self.request.user.pk

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            tm.messages.error(
                request,
                tm.FlashMessages.NO_AUTHENTICATION.value,
            )

            return self.handle_no_permission()

        elif not self.has_permission():
            tm.messages.error(
                request,
                tm.FlashMessages.NO_PERMIT_TO_CHANGE_USER.value,
            )
            return tm.redirect('users')
        return super().dispatch(request, *args, **kwargs)


class UserDeleteAccessMixin(UserChangeAccessMixin):

    def form_valid(self, form):
        try:
            self.object.delete()
            tm.messages.success(
                self.request, tm.FlashMessages.USER_SUCCESSFULLY_DELETE.value
            )
            return tm.redirect('users')

        except tm.ProtectedError:
            tm.messages.error(self.request,
                              tm.FlashMessages.USER_IS_USING.value)
            return tm.redirect('users')


class PermissionMixin:
    redirect_field_name = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            tm.messages.error(
                self.request, tm.FlashMessages.NO_AUTHENTICATION.value
            )
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
