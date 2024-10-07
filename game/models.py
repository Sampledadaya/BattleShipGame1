# models.py
from django.db import models

class Game(models.Model):
    player_field = models.JSONField(default=list)
    computer_field = models.JSONField(default=list)
    player_shots = models.JSONField(default=list)
    computer_shots = models.JSONField(default=list)
    hits = models.JSONField(default=list)  # Хранит список попаданий
    is_player_turn = models.BooleanField(default=True)
    game_over = models.BooleanField(default=False)
    winner = models.CharField(max_length=20, blank=True, null=True)
