actor käyttäjä

main->*menu_view: MenuView(screen, bkg_color, object_color, screen_size, object_width
menu_view->*hi_scores: HiScoreService()
main->+menu_view: run()

käyttäjä->menu_view: painaa H

menu_view->*hi_score_view: HiScoreView(screen, bkg_color, object_color, hi_scores)
menu_view->+hi_score_view: run()
hi_score_view->+hi_scores: get_lines()
hi_scores-->-hi_score_view: lines

käyttäjä->hi_score_view: painaa Esc

hi_score_view-->-menu_view:

käyttäjä->menu_view: painaa Esc

menu_view-->-main: