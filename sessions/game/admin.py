from django.contrib import admin

from .models import Player, Game, PlayerGameInfo


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'player_id',)
    list_display_links = ('id', 'player_id',)
    ordering = ('player_id',)

class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'game_id', 'is_game_complete', 'guess_number',)
    list_display_links = ('id', 'game_id',)
    ordering = ('game_id',)

class InfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', 'game', 'try_count', 'is_current_player_gameauthor',)
    list_display_links = ('id',)
    ordering = ('id',)


admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(PlayerGameInfo, InfoAdmin)