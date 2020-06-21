from django.shortcuts import render
from .models import Player, Game, PlayerGameInfo
from .forms import FormGuessNumber
from django.http import HttpResponse

import random

MAX_GUESS_NUM = 100

def show_home(request):

    form = FormGuessNumber(request.POST or None)
    context = {}

    player_id = request.session.get('player_id')
    game_id = request.session.get('game_id')

    if player_id and game_id:
        cur_game = Game.objects.get(game_id=game_id)

        if cur_game.is_game_complete:
            game = Game.objects.create(game_id=random.randint(0, 1000), guess_number=random.randint(1, MAX_GUESS_NUM+1),
                                           is_game_complete=False)
            player = Player.objects.get(player_id=player_id)
            PlayerGameInfo.objects.create(player=player, game=game, try_count=0, is_current_player_gameauthor=True)
            request.session['game_id'] = str(game.game_id)
        else:
            exists_player = Player.objects.get(player_id=player_id)
            cur_game.players.add(exists_player,through_defaults={'try_count': 0, 'is_current_player_gameauthor': False})
            request.session['game_id'] = str(cur_game.game_id)
    else:

        if Game.objects.filter(is_game_complete=False).count() == 0:
            game = Game.objects.create(game_id=random.randint(0, 1000), guess_number=random.randint(1, MAX_GUESS_NUM+1),
                                           is_game_complete=False)
            player = Player.objects.create(player_id=f'{random.randint(0, 1000)}')
            PlayerGameInfo.objects.create(player=player, game=game, try_count=0, is_current_player_gameauthor=True)
            request.session['game_id'] = str(game.game_id)
            request.session['player_id'] = str(player.player_id)

        else:
            cur_game = Game.objects.get(is_game_complete=False)
            player = Player.objects.create(player_id=f'{random.randint(0, 1000)}')
            cur_game.players.add(player, through_defaults={'try_count': 0, 'is_current_player_gameauthor': False})
            request.session['game_id'] = str(cur_game.game_id)
            request.session['player_id'] = str(player.player_id)

    game = Game.objects.get(game_id=request.session.get('game_id'))
    player = Player.objects.get(player_id=request.session.get('player_id'))
    game_info = PlayerGameInfo.objects.filter(game_id=game).get(player_id=player)

    if form.is_valid():
        number = int(request.POST.get('number'))
        if number == game.guess_number:
            game.is_finished = True
            game.save()
            context['text'] = f'Вы угадали число! c {game_info.try_count} попыток'
        elif number < game.guess_number:
            context['text'] = f'Загаданное число больше числа {number}'
        elif number > game.guess_number:
            context['text'] = f'Загаданное число меньше числа {number}'
        game_info.try_count += 1
        game_info.save()
        context['form'] = form
        return render(request, 'home.html', context)
    else:
        context['form'] = form

    return render(request, 'home.html', context)
