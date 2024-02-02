from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('home2', views.home2, name='home2'),
    path('detalhes_curso/<int:pk>', views.detalhes_curso, name='detalhes_curso'),
    path('detalhes_funcionario/<int:pk>/<int:disc>/<int:direccao>', views.detalhes_funcionario, name='detalhes_funcionario'),
    path('noticia/<int:pk>', views.noticia, name='noticia'),
    path('instituicao', views.instituicao, name='instituicao'),
    path('direccao', views.direccao, name='direccao'),
    path('docentes', views.docentes, name='docentes'),
    path('quadro_de_honra', views.Quadro_de_honra, name='quadro_de_honra'),
    path('quadro_de_honra2/<int:pk>', views.Quadro_de_honra2, name='quadro_de_honra2'),
    path('entrar', views.entrar, name='entrar'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/password_reset', auth_views.PasswordResetView.as_view(
        template_name = 'password_reset_form.html',
        email_template_name='password_reset_email.html'
    ), name="password_reset"),
    path('accounts/password_reset_done', auth_views.PasswordResetDoneView.as_view(
        template_name = 'password_reset_done.html'
    ), name="password_reset_done"),
    path('accounts/password_reset_confirm/<slug:uidb64>/<slug:token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name = 'password_reset_confirm.html'
    ), name="password_reset_confirm"),
    path('accounts/password_reset_complete', auth_views.PasswordResetCompleteView.as_view(
        template_name = 'password_reset_complete.html'
    ), name="password_reset_complete"),
    ]