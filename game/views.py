# views.py
from django.shortcuts import render, redirect
from .models import Game
from .utils import generate_field, create_empty_field  # Импортируем create_empty_field
import random

def index(request):
    if request.method == 'POST':
        player_field = generate_field()
        computer_field = generate_field()
        game = Game.objects.create(
            player_field=player_field,
            computer_field=computer_field,
            player_shots=create_empty_field(),  # Создаем пустое поле для выстрелов игрока
            computer_shots=create_empty_field(),  # Пустое поле для выстрелов компьютера
            hits=[],  # Инициализируем пустой список попаданий
            is_player_turn=True,
            game_over=False
        )
        return redirect('game', game_id=game.id)

    return render(request, 'index.html')

def game_view(request, game_id):
    game = Game.objects.get(id=game_id)

    if request.method == 'POST':
        # Если игра уже окончена, больше ничего не делаем
        if game.game_over:
            return redirect('game', game_id=game_id)

        # Получение данных о выстреле игрока
        row = int(request.POST.get('row'))
        col = int(request.POST.get('col'))

        # Выстрел игрока по полю компьютера
        if game.player_shots[row][col] == 0:  # Если это первый выстрел в эту клетку
            game.player_shots[row][col] = 1  # Указываем, что выстрел был сделан

            if game.computer_field[row][col] == 1:  # Проверяем, попал ли игрок
                game.computer_field[row][col] = 2  # Попадание
                game.player_shots[row][col] = 2  # Указываем на попадание в выстрелах
            else:
                game.player_shots[row][col] = 3  # Указываем на промах (например, 3)

            game.is_player_turn = False  # Ход компьютера
            game.save()

            # Ход компьютера
            if not game.game_over:
                computer_shot(game)

        return redirect('game', game_id=game_id)

    return render(request, 'game.html', {'game': game})


def computer_shot(game):
    # Компьютер делает ход с шансом 50% на победу
    while not game.is_player_turn and not game.game_over:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if game.computer_shots[row][col] == 0:
            game.computer_shots[row][col] = 1
            if game.player_field[row][col] == 1:
                game.player_field[row][col] = 2  # Попадание
            else:
                game.is_player_turn = True  # Возвращаем ход игроку

        # Проверка победы
        check_winner(game)

    game.save()

def check_winner(game):
    if all(cell != 1 for row in game.computer_field for cell in row):
        game.game_over = True
        game.winner = 'Player'
    elif all(cell != 1 for row in game.player_field for cell in row):
        game.game_over = True
        game.winner = 'Computer'
