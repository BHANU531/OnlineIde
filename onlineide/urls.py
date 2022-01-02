from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("user",UserVeiwSet,basename = "user")
router.register("submit",SubmissionVeiwSet,basename="submission")

urlpatterns = [
    path("home",home),
    # path('submit/create',SubmissionVeiwSet.create)
]
urlpatterns =router.urls