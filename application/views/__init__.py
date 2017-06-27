from .user import CheckUserAuthenticatedMixin, Base, Index, Login, Logout, MyInfo, ChangePassword
from .info import InstituteInfoView, MajorInfoView, ClassInfoView, TeacherInfoView, StudentInfoView

__all__ = [
    CheckUserAuthenticatedMixin,
    Base,
    Index,
    Login,
    Logout,
    MyInfo,
    ChangePassword,
    InstituteInfoView,
    MajorInfoView,
    ClassInfoView,
    TeacherInfoView,
    StudentInfoView
]
