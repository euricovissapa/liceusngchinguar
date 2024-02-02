from django.urls import path
from . import views
urlpatterns = [
    #session
    path('bloquear', views.bloquear, name='bloquear'),
    path('terminar', views.terminar, name='terminar'),
    #dd
    path('add_user', views.UserCreate.as_view(), name='add_user'),
    path('add_f', views.Add_Funcionario.as_view(), name='add_f'),
    path('add_f2', views.Add_Funcionario2.as_view(), name='add_f2'),
    path('AddCurso', views.Add_Curso.as_view(), name='AddCurso'),
    path('AddNoticia', views.Add_noticias.as_view(), name='AddNoticia'),
    path('Addfoto', views.Add_foto.as_view(), name='Addfoto'),
    path('AddquadroHonra', views.quadroHonra.as_view(), name='AddquadroHonra'),
    #edit
    path('edit_f/<int:fun_id>', views.edit_Funcionario.as_view(), name='edit_f'),
    path('edit_f2/<int:fun_id>', views.edit_Funcionario2.as_view(), name='edit_f2'),
    path('edit_curso/<int:curso_id>', views.edit_curso.as_view(), name='edit_curso'),
    path('edit_user/<int:user_id>', views.EditUser.as_view(), name='edit_user'),
    path('edit_noticia/<int:noti_id>', views.edit_noticia.as_view(), name='edit_noticia'),
    path('edit_foto/<int:foto_id>', views.edit_foto.as_view(), name='edit_foto'),
    path('edit_alunod/<int:alunod_id>', views.EditquadroHonra.as_view(), name='edit_alunod'),
    path('alterar_pass/', views.AlterarPassword.as_view(), name='alterar_pass'),
    #view
    path('dashboard', views.dashboard, name='dashboard'),
    path('q_cursos', views.q_cursos, name='q_cursos'),
    path('q_funcionarios', views.q_funcionarios, name='q_funcionarios'),
    path('q_utilizadores', views.q_utilizador, name='q_utilizadores'),
    path('q_noticias', views.q_noticia, name='q_noticias'),
    path('q_galeria', views.q_galeria, name='q_galeria'),
    path('q_quadroH', views.Q_QuadroH, name='q_quadroH'),
    path('q_aniversariantes', views.Aniversariantes, name='q_aniversariantes'),
    path('d_funcionario_admin/<int:fun_id>', views.d_funcionario_admin, name='d_funcionario_admin'),
    path('perfil', views.perfil.as_view(), name='perfil'),
    #delete
    path('elim_curso/<int:curso_id>', views.elim_curso, name='elim_curso'),
    path('elim_f/<int:fun_id>', views.elim_f, name='elim_f'),
    path('elim_user/<int:user_id>', views.elim_user, name='elim_user'),
    path('elim_noti/<int:noti_id>', views.elim_noti, name='elim_noti'),
    path('elim_foto/<int:foto_id>', views.elim_foto, name='elim_foto'),
    path('elim_alunod/<int:alunod_id>', views.elim_alunod, name='elim_alunod'),
    ]