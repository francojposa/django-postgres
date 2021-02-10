from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request: HttpRequest, question_id: str) -> HttpResponse:
    response = f"You're looking at question {question_id}"
    return HttpResponse(response)


def results(request: HttpRequest, question_id: str) -> HttpResponse:
    response = f"You're looking at results for question {question_id}"
    return HttpResponse(response)


def vote(request: HttpRequest, question_id: str) -> HttpResponse:
    response = f"You're voting on question {question_id}"
    return HttpResponse(response)
