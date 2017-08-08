from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'sign_in/$', views.sign_in, name='sign_in'),
    url(r'sign_up/$', views.sign_up, name='sign_up'),
    url(r'sign_out/$', views.sign_out, name='sign_out'),
    url(r'profile/$', views.profile, name='profile'),
    url(r'profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'profile/change_avatar/$', views.edit_avatar, name='edit_avatar'),
    url(r'profile/change_avatar/rotate', views.rotate_image, name='rotate_image'),
    url(r'profile/change_avatar/crop', views.crop_image, name='crop_image'),
    url(r'profile/change_avatar/flip', views.flip_image, name='flip_image'),
    url(r'profile/change_password/$', views.edit_password, name='edit_password'),

]