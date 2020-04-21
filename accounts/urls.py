from django.urls import path
from accounts.views import *

app_name = 'accounts'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('login/submit/', login_submit, name='login_submit'),
    path('create/creator/', CreateUserView.as_view(), name="create_creator"),
    path('admins/', AdminListView.as_view(), name="admin_list"),
    path('admins/<int:pk>/update/', AdminUpdateView.as_view(), name="admin_update"),
    path('', dashboard, name='dashboard'),
]
