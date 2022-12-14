from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, name="home"), #home url
    path('findProfessors/', views.find_professors, name="findProfessors"),
    path('aboutUs/', views.aboutUs, name="aboutUs"),
    path('allProfessors/', views.all_professors, name="allProfessors"),
    path('myReviews/', views.my_reviews, name="myReviews"),
    path('profile/', views.profile, name="profile"),
    path('testForm/', views.test_form, name="testForm"),
    path('jasonHome/', views.jason_home, name="jasonHome"),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('search/', views.search, name='search'),
    path('profpage/<int:professor_id>', views.professor_view, name='professorview'),
    path('add_review/<int:professor_id>/<int:user_id>', views.add_review, name='addreview'),
    path('update/<int:review_id>/<int:professor_id>', views.update, name='update'),
    path('delete/<int:review_id>', views.delete, name='delete'),
    path('departments/', views.departments, name='departments'),
    path('departmentProfessors/<int:department_id>', views.department_professors, name='departmentpr'),


]


