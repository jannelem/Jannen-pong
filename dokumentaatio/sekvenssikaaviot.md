# Sekvenssikaavioiden tekstit

Tähän tiedostoon on tallennettu websequencediagramilla tehtyjen sekvenssikaavioiden tekstit.

## Pistelistan tarkastelu

actor käyttäjä

main->*menu_view: MenuView(screen, bkg_color, object_color, screen_size, object_width
menu_view->*hi_scores: HiScoreService()
hi_scores->*_scores: HiScoreList()
main->+menu_view: run()

käyttäjä->menu_view: painaa H

menu_view->*hi_score_view: HiScoreView(screen, bkg_color, object_color, hi_scores)
menu_view->+hi_score_view: run()
hi_score_view->+hi_scores: get_lines()
hi_scores->+_scores: lines()
_scores-->-hi_scores: lines
hi_scores-->-hi_score_view: lines

käyttäjä->hi_score_view: painaa Esc

hi_score_view-->-menu_view:

käyttäjä->menu_view: painaa Esc

menu_view-->-main:

## Pelaaminen

actor käyttäjä

main->*menu_view: MenuView(screen, bkg_color, object_color, screen_size, object_width
menu_view->*hi_scores: HiScoreService()
hi_scores->*_scores: HiScoreList()
main->+menu_view: run()

käyttäjä->menu_view: painaa Enter

menu_view->*game_view: GameView(screen, bkg_color, object_color, screen_size, object_width, hi_scores)
menu_view->+game_view: run()
game_view->*pong_service: PongService(bkg_color, object_color, screen_size, object_width, hi_scores)
pong_service->*pong: Pong(bkg_color, object_color, screen_size, object_width, hi_scores)
pong->*player_paddle:
pong->*computer_paddle:
pong->*ball:
game_view->+pong_service: running()
pong_service->+pong: running()
pong-->-pong_service: True
pong_service-->-game_view: True


käyttäjä->game_view: painaa ylänuolta
game_view->+pong_service: player_move_up()
pong_service->+pong: player_paddle_move_up(object_width)
pong->+player_paddle: move_up(object_width)
player_paddle-->-pong:
pong-->-pong_service:
pong_service-->-game_view:
game_view->+pong_service: handle_game_events()
pong_service->pong_service: _computer_move()
pong_service->pong_service: _handle_wall_collisions()
pong_service->pong_service: _handle_paddle_collisions()
pong_service->pong_service: _check_scores()

## Pisteiden tallentaminen pelin päättyessä

actor käyttäjä

pong_service->pong_service: _player_scores
pong_service->pong_service: _check_scores
pong_service->+pong: scores()
pong-->-pong_service: [18, 2]
pong_service->+pong: runnning(False)
pong-->-pong_service:
game_view->+pong_service: running()
pong_service->+pong: running()
pong-->-pong_service: False
pong_service-->-game_view: False

game_view->*game_over_view: GameOverView(screen, bkg_color, object_color, hi_scores, pong_service)
game_view->+game_over_view: run()
game_over_view->+pong_service: scores()
pong_service-->-game_over_view: [18, 2]
game_over_view->+pong_service: check_new_hi_score()
pong_service->+hi_scores: lowest_score()
hi_scores-->-pong_service: 3
pong_service-->-game_over_view: True

käyttäjä->game_over_view: kirjoittaa "Irmeli" ja painaa Enter

game_over_view->+hi_scores: add_new_score("Irmeli", 18)
hi_scores->_scores: add_score("Irmeli", 18)
_scores->_scores: sort_list()
_scores-->hi_scores:
hi_scores-->game_over_view:
game_over_view-->menu_view:

