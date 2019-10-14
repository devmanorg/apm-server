from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Play, Event


def show_plays(request):
    return render(request, 'plays_list.html', {
        'plays': Play.objects.order_by('-created')[:50]
    })


def show_play(request, play_id):
    play = get_object_or_404(Play, id=play_id)
    return render(request, 'play.html', {
        'play': play
    })


@csrf_exempt
@require_http_methods(["POST"])
def register_play(request):
    new_play = Play.objects.create()
    return JsonResponse({
        'status': 'ok',
        'play_id': new_play.id,
    })


@csrf_exempt
def track(request, play_id):
    play = get_object_or_404(Play, id=play_id)
    print('Got request', request)
    Event.objects.create(play=play)
    return JsonResponse({
        'status': 'ok'
    })