from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from chatbot.views import (
    chatbot,
    chatbot_response,
)
from account.views import (
    registration_view,
    logout_view,
    login_view,
    account_update_view,
    account,
)

urlpatterns = [
    path('', views.home, name='website-home'),
    path('about/', views.about, name='website-about'),
    path('faqs/', views.faqs, name='website-faqs'),
    path('login/', login_view, name='website-login'),
    path('signup/', registration_view, name='website-signup'),
    path('logout/', logout_view, name='website-logout'),
    path('account/', account, name='website-account'),
    path('account/update/', account_update_view, name='website-account-update'),
    path('chatbot/', chatbot, name='website-chatbot'),
    path('chatbot/response/', chatbot_response, name='website-chatbot-response'),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('account/password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='chatbot_website/pages/changepass-done.html'), 
        name='password_change_done'),
    path('account/password-change/', auth_views.PasswordChangeView.as_view(template_name='chatbot_website/pages/changepass.html'), 
        name='password_change'),
    # path('account/password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
    #  name='password_reset_done'),
    # path('account/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('account/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('account/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
    #  name='password_reset_complete'),
]
