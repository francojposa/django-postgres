from django.urls import path

from . import views

urlpatterns = [
    # Ex. /polls/
    path("", views.index, name="index"),
    # Ex./polls/6722b747-f497-4095-95bf-7ba4402ba3b8/
    path("<str:question_id>/", views.detail, name="detail"),
    # Ex./polls/6722b747-f497-4095-95bf-7ba4402ba3b8/results
    path("<str:question_id>/results/", views.results, name="results"),
    # Ex./polls/6722b747-f497-4095-95bf-7ba4402ba3b8/vote
    path("<str:question_id>/vote/", views.vote, name="vote"),
]
