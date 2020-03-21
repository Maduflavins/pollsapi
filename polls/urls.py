from django.urls import path
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote, PollViewSet, UserCreate, LonginView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_swagger.views import get_swagger_view


router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

schema_view = get_swagger_view(title="Polls API")

urlpatterns = [
    path("login/", views.obtain_auth_token, name="login"),
    path("polls/", PollList.as_view(), name="polls_list"),
    
    path("/polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("/polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("/polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path(r'swagger-docs/', schema_view),
]

urlpatterns += router.urls

