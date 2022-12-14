from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.decorators import login_required
from base.models import Login, Professor, Review, Subject, Courses
from base.forms import ReviewForm
from django.contrib.auth import logout
from django.http import HttpResponseRedirect


# Create your views here.

# @login_required(login_url='login/')
def base(request):
    return render(request, 'base/home.html')


# login Page
def login(request):
    return render(request, 'base/login.html')


# Find Professor Page
def find_professors(request):
    return render(request, 'base/findProfessors.html')

def aboutUs(request):
    return render(request, 'base/aboutUs.html')

# Profile Page
def profile(request):
    return render(request, 'base/profile.html')


# Test Form
def test_form(request):
    return render(request, 'base/testForm.html')


# jasonHome
def jason_home(request):
    return render(request, 'base/jasonHome.html')


def register_view(request):
    form = UserCreationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'base/signUp.html', context)


def login_view(request):
    form = AuthenticationForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # get the user
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def search(request):
    search_term = request.GET.get('searchbar' or '')
    professors = Professor.objects.all().filter(name__contains=search_term).order_by('name')
    context = {'professors': professors, 'search_item': search_term}
    return render(request, 'base/findProfessors.html', context)


def professor_view(request, professor_id):
    professor = Professor.objects.get(id=professor_id)
    reviews = Review.objects.all().filter(professor_id=professor.id)

    context = {'professor': professor, 'reviews': reviews}

    return render(request, 'base/professorPage.html', context)


@login_required(login_url='login')
def add_review(request, professor_id, user_id):
    professor = Professor.objects.get(id=professor_id)
    review = Review.objects.all().filter(professor=professor)
    u = User.objects.get(id=user_id)
    # professor.rating = 5.0
    # professor.save()
    for r in review:
        if r.user.username == u.username:
            return redirect('home')

    professors = Review(user=request.user, professor=professor, review_check=True)
    form = ReviewForm(request.POST, instance=professors or None)

    if request.method == 'POST':
        if form.is_valid():
            rate = form.cleaned_data.get('rating')
            if rate == 1.0 and professor.rating != 0.0 and professor.rating >= 0.4:
                professor.rating = professor.rating - 0.4
                professor.save()
            elif rate == 2.0 and professor.rating != 0.0 and professor.rating >= 0.3:
                professor.rating = professor.rating - 0.3
                professor.save()
            elif rate == 3.0 and professor.rating != 0.0 and professor.rating >= 0.1:
                professor.rating = professor.rating - 0.1
                professor.save()
            elif rate == 4.0 and professor.rating != 5.0 and professor.rating <= 4.9:
                professor.rating = professor.rating + 0.1
                professor.save()
            elif rate == 5.0 and professor.rating != 5.0 and professor.rating <= 4.7:
                professor.rating = professor.rating + 0.3
                professor.save()
            form.save()
            reviews = Review.objects.all()
            # context = {'professor': professor, 'reviews': reviews}
            # return render(request, 'base/professorPage.html', context)
            return redirect('professorview', professor_id=professor.id)

    courses = Courses.objects.all()
    context = {'form': form, 'professor': professor, 'courses': courses}
    return render(request, 'base/reviewForm.html', context)

@login_required(login_url='login')
def update(request, review_id, professor_id):
    # update the product with product_id
    professor = Professor.objects.get(id=professor_id)
    review = Review.objects.get(id=review_id)
    form = ReviewForm(request.POST or None, instance=review)
    if request.user.id != review.user.id:
        return redirect('home')


    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('professorview', professor_id=professor.id)

    courses = Courses.objects.all()
    context = {'form': form, 'review': review, 'professor': professor, 'courses': courses}

    return render(request, 'base/update.html', context)

@login_required(login_url='login')
def delete(request, review_id):
    review = Review.objects.get(id=review_id)
    professor = Professor.objects.get(id=review.professor.id)
    if request.user.id != review.user.id:
        return redirect('home')
    #if review.rating == 1.0 and professor.rating <= 4.6:
        #professor.rating = professor.rating + 0.4
        #professor.save()
    # elif review.rating == 2.0 and professor.rating <= 4.7:
    #     professor.rating = professor.rating + 0.3
    #     professor.save()
    # elif review.rating == 3.0 and professor.rating <= 4.9:
    #     professor.rating = professor.rating + 0.1
    #     professor.save()
    # elif review.rating == 4.0 and professor.rating >= 0.1:
    #     professor.rating = professor.rating - 0.1
    #     professor.save()
    # elif review.rating == 5.0 and professor.rating >= 0.3:
    #     professor.rating = professor.rating - 0.3
    #     professor.save()
    review.review_check = False
    review.save()
    if request.method == 'POST':
        review.delete()
        return redirect('professorview', professor_id=professor.id)

    # context = {'reviews': review}
    # return render(request, 'base/myReviews.html', context)


def all_professors(request):
    professors = Professor.objects.all().order_by('name')
    context = {'professors': professors}
    return render(request, 'base/allProfessors.html', context)


def my_reviews(request):
    reviews = Review.objects.all().filter(user=request.user)
    context = {'reviews': reviews}
    return render(request, 'base/myReviews.html', context)


def departments(request):
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, 'base/departments.html', context)


def department_professors(request, department_id):
    department = Subject.objects.get(id=department_id)
    professors = []
    teachers = Professor.objects.all().order_by('name')
    for t in teachers:
        if department.subject in t.department:
            professors.append(t)
    context = {'professors': professors}
    return render(request, 'base/departmentProfessors.html', context)

def my_view(request):
    logout(request)
    return HttpResponseRedirect('/')