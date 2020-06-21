from django.db import models


class Player(models.Model):
    player_id = models.CharField(max_length=10, verbose_name='id игрока')

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'

    def __str__(self):
        return self.player_id


class Game(models.Model):
    game_id = models.CharField(max_length=10, verbose_name='id игры')
    is_game_complete = models.BooleanField(verbose_name='Закончена ли игра', default=True)
    guess_number = models.IntegerField(verbose_name='Загаданное число')
    players = models.ManyToManyField(Player, through='PlayerGameInfo')

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

    def __str__(self):
        return str(self.game_id)


class PlayerGameInfo(models.Model):
    player = models.ForeignKey(Player, verbose_name='id игрока', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, verbose_name='id игры', on_delete=models.CASCADE)
    try_count = models.IntegerField(verbose_name='Число попыток')
    is_current_player_gameauthor = models.BooleanField(verbose_name='Автор ли игры', default=False)

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информация'
