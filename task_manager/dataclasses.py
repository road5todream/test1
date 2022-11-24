from enum import Enum
from django.utils.translation import gettext as _


class VerboseName(Enum):
    NAME = _('Name')
    STATUS = _('Status')
    PERFORMER = _('Performer')
    LABEL = _('Label')
    DESCRIPTION = _('Description')


class FlashMessages(Enum):
    REGISTER_SUCCESS = _('User is successfully registered')
    LOGIN_SUCCESS = _('You are logged in')
    LOGOUT_SUCCESS = _('You are logged out')
    NO_PERMIT_TO_CHANGE_USER = _('You have no rights to change another user')
    USER_SUCCESSFULLY_CHANGED = _('User successfully changed')