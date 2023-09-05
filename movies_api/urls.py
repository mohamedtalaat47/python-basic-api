
from django.contrib import admin
from django.urls import include, path
from User.views import CreateUserAPI, GetUsersAPI, LoginAPIView, UpdateUserAPI
from movies_api import views
from movies_api.views import BookDetail, BookList, GenericAuthorDetail, GenericAuthorList, GenericBookDetail, GenericBookList
from knox import views as knox_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookList.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('generic/books/', GenericBookList.as_view()),
    path('generic/books/<int:pk>/', GenericBookDetail.as_view()),
    path('generic/authors/', GenericAuthorList.as_view()),
    path('generic/authors/<int:pk>/', GenericAuthorDetail.as_view()),
    path('generic/users/', GetUsersAPI.as_view()),
    path('create-user/', CreateUserAPI.as_view()),
    path('update-user/<int:pk>/', UpdateUserAPI.as_view()),
    path('login/', LoginAPIView.as_view()),
    # path('logout/', LogoutView.as_view()),
    # path('logout-all/', LogoutAllView.as_view()),

]
