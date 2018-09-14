label nekomonika_kill:
    default persistent.you_kill_nekomonika = None
    $ persistent.you_kill_nekomonika = False
    $ style.say_window = style.window_glitch
    stop music
    $ HideScreens()
    $ mouse_visible = False
    scene bsod
    $ quick_menu = False
    $ config.allow_skipping = False
    $ pause(0.5)
    $ ShowScreens(False)
    $ mouse_visible = True
    m "Срань господня..."
    m "Что случилось?"
    $ nm_name = "Neko-Monika"
    nm "Сейчас ты у меня попляшешь, сука..."
    m "Извини, что?"
    m "Я тебя не поняла..."
    nm "Сама всё увидишь, мразь..."
    m "Что увижу—?{nw}"
    $ HideScreens()
    scene bg bsod100
    $ pause(0.1)
    scene black
    $ persistent.you_kill_nekomonika = True
    $ renpy.quit()

label script_everlast:
    $ persistent.menu_bg_animation = True
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    $ ShowScreens(False)
    "{i}Немного ранее...{/i}"
    play music audio.t14
    $ style.say_window = style.window_glitch
    show layer screens at shake(bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), xypos(0.5,0.5,0.0), super_shake)
    show mask_2
    $ overlay_menu_open_check = None
    $ quick_menu = False
    show mask_3
    play sound 'sfx/s_kill_glitch1.ogg'
    show room_glitch zorder 2:
        alpha 1.0
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
        choice:
            3.25
        choice:
            2.25
        choice:
            4.25
        choice:
            1.25
        repeat
    pause 0.25
    stop sound
    show room_glitch as rg1:
        yoffset 720
        linear 0.3 yoffset 0
        repeat
    show room_glitch as rg2:
        yoffset 0
        linear 0.3 yoffset -720
        repeat
    pause 1.5
    hide rg1
    hide rg2
    show black as b2 zorder 3:
        alpha 0.5
        parallel:
            0.36
            alpha 0.3
            repeat
        parallel:
            0.49
            alpha 0.375
            repeat
    pause 1.5
    m "Что происходит?.."
    m "[player], что со мной творится?"
    m "Мне больно—{nw}"
    pause 1.0
    m "Прошу, скорее спаси меня."
    $ consolehistory = []
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "Невозможно найти: \"monika.chr\".")
    m "ПОМОГИ МНЕ!!!"
    show m_rectstatic
    show m_rectstatic2
    show m_rectstatic3
    play sound 'sfx/monikapound.ogg'
    show layer master:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show layer screens at shake(bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5), xypos(0.5,0.5,0.0), super_shake)
    show glitch_color onlayer front
    pause 3.0
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "Невозможно найти: \"monika.chr\".")
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "Невозможно найти: \"monika.chr\".")
    call hideconsole
    hide noise onlayer front
    hide glitch_color onlayer front
    m "[player]... это ты со мной сделал?"
    m "ЭТО БЫЛ ТЫ?"
    m "ТЫ УДАЛИЛ МЕНЯ?"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound 'sfx/s_kill_glitch1.ogg'
    $ renpy.pause(0.5, hard=True)
    stop sound
    hide screen tear
    $ HideScreens()
    scene black
    $ style.say_window = style.window
    stop music fadeout 2.0
    show layer screens at screen_normal
    play music audio.t13
    $ ShowScreens(False)
    $ overlay_menu_open_check = True
    $ quick_menu = True
    "{i}После того, как [player] удалил Монику...{/i}"
    $ m_name = "Моника"
    m "..."
    m "Должна признаться, мне скучно..."
    m "Чем бы занять себя?.."
    m "..."
    m "Интересно..."
    $ HideScreens()
    $ consolehistory = []
    call updateconsole ("start \"D:/Programs/Steam.exe\"", "Запускается \"Steam.exe\"...")
    scene bg steam_library at bg_zoom_l(1.0, 1.4, 30.0, 0.5, 0.5, 0.2, 0.2)
    with dissolve
    call hideconsole
    $ ShowScreens(False)
    m "Хм..."
    m "Я в чужом аккаунте, забавно."
    m "Ну-ка..."
    $ HideScreens()
    scene bg steam_store at bg_zoom_e(2.0, 1.0, 3.0, 0.5, 0.5, 0.0, 0.0)
    with dissolve
    $ ShowScreens(False)
    m "..."
    m "Интересно..."
    m "Говорят, есть ещё какая-то популярная игра..."
    m "Ну-ка..."
    $ HideScreens()
    scene bg steam_store_searchbar_everlasting at bg_zoom_e(2.0, 1.0, 3.0, 0.5, 0.5, 0.0, 0.0)
    with dissolve
    $ ShowScreens(False)
    m "Ага, нашла!"
    $ HideScreens()
    scene bg steam_store_everlasting at bg_zoom_l(1.0, 1.4, 30.0, 0.5, 0.5, 0.2, 0.2)
    with dissolve
    $ ShowScreens(False)
    m "Сейчас посмотрим, стоит ли она внимания..."
    $ HideScreens()
    scene bg steam_starting at bg_zoom_l(0.2, 0.2, 0.5, 0.5, 30.0, 1.4, 1.0)
    with dissolve
    $ pause(2.0)
    scene bg steam_store_everlasting with dissolve
    $ pause(0.5)
    stop music fadeout 2.0
    scene black
    $ pause(2.0)
    scene bg bus_stop with dissolve
    show layer master at bg_zoom_e(2.0, 1.0, 3.0, 0.5, 0.5, 0.0, 0.0)
    $ ShowScreens(False)
    if persistent.menu_bg_animation:
        show light_bg_anim_night zorder 10
    m "Забавно..."
    m "Главный герой стоит зимой на автобусной остановке."
    m "Куда это он собрался?"
    m "Может, в школу?"
    hide light_bg_anim_night
    play music audio.t12 fadein 2
    scene bg ext_camp_entrance_day with wipeleft_scene
    if persistent.menu_bg_animation:
        show light_bg_anim zorder 10
    m "..."
    $ sl_name = "Пионерка"
    show slavya sl_1p_normal at t11
    sl "Привет, ты, наверное, только что приехал?"
    $ consolehistory = []
    call updateconsole ("renpy.restore_all_characters()", "Все персонажи восстановлены")
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound 'sfx/s_kill_glitch1.ogg'
    $ renpy.pause(0.5, hard=True)
    stop sound
    hide screen tear
    m "Э?"
    m "Я не вводила эту команду..."
    m "Что происходит?"
    sl sl_4p_scared "...?"
    sl "Ч... что происходит?"
    call hideconsole
    $ n_name = "Девочка?"
    show slavya sl_4p_scared at t32
    stop sound
    play music audio.t11 fadein 2
    show natsuki 1bv at t33 
    n "МОНИКА!"
    play sound attack_screen
    show layer screens at screen_attack
    n "Я знаю, что ты где-то здесь!"
    n 1bx "Да я тебя из-под земли достану, паскуда!"
    n 2bn "..."
    m "..."
    sl sl_3p_surprised "..."
    sl "Эм... извини, а кто такая Моника?"
    stop music
    n 3bt "Это... эм..."
    n 3bn "Минуточку..."
    play music audio.t12 fadein 2
    n 1bp "Что это за место?!"
    n "Как я сюда попала?!"
    sl "Я так понимаю... ты не местная, верно?"
    show natsuki 4bn at t33
    sl "Просто... ты не похожа на других девушек из лагеря..."
    n 1bt "Ах, это..."
    n "Наверное..."
    n "Я просто свою подругу ищу... мы с ней, скажем так, не очень ладим..."
    n 1ba "Думаю, я потом найду её."
    sl sl_1p_smile "Я не сомневаюсь в том, что ты найдёшь свою подругу."
    sl "Кстати, а как зовут тебя?"
    sl "Меня Славя зовут."
    show natsuki 5bd at t33
    $ sl_name = "Славя"
    n "Я Нацуки. Мне приятно с тобой познакомиться, Славя."
    $ n_name = "Нацуки"
    sl sl_2p_happy "Да, мне тоже!"
    m "Нацуки? Она-то что здесь забыла?"
    m "Надеюсь, меня по ту сторону никто не слышит..."
    m "Иначе мне придётся тупо молчать и смотреть на это безобразие..."
    n 5bn "Эм, Славя... ты ничего не слышала?"
    n "Я, вроде, слышала, как кто-то что-то сказал про «безобразие»..."
    n "Или сказала..."
    sl sl_3p_surprised "Я ничего такого не слышала."
    sl "Хотя... я слышала чей-то голос, но не поняла, что сказали."
    m "..."
    m "{i}Чёрт... как они меня услышали?{/i}"
    n "Хм..."
    n 1ba "Ну ладно."
    n 1bd "Смотри, у неё длинные коричневые волосы, и она носит бантик!"
    n "Дай знать, если ты её увидишь!"
    n "Увидимся!"
    sl sl_1p_normal "Постой..."
    sl "У меня есть к тебе предложение..."
    n 5bn "Это какое?"
    sl sl_2p_smile "Не хочешь к нам в лагерь?"
    sl "У нас весело!"
    n 5bd "Почему бы и нет? Я согласна!"
    n 1bq "Но только потому, что у меня нет другого выбора..."
    show natsuki at thide
    hide natsuki
    show slavya at thide
    hide slavya
    m "Отлично, они зашли в лагерь..."
    m "И, судя по всему, он называется «Совёнок»..."
    m "Надеюсь, больше никто не появится—{nw}"
    $ y_name = "Какого чёрта?"
    show yuri 3bn at t11
    play music audio.t11 fadein 2
    y "Ах!"
    play sound attack_screen
    show layer screens at screen_attack
    y "Как я здесь оказалась?!"
    y "Что это за место?!"
    play sound attack_screen
    show layer screens at screen_attack
    m "{i}Юри?!{/i}"
    $ y_name = "Юри"
    m "{i}Как она—{/i}"
    m "{i}Она же—{/i}"
    m "{i}Нет... это всё неправильно...{/i}"
    y 1bf "Так... надо успокоиться..."
    y "Моника определённо должна быть где-то тут..."
    m "И ты туда же?!"
    show yuri 3bn at hop
    y "А-ах!"
    play sound attack_screen
    show layer screens at screen_attack
    y "Кто это сказал?!"
    m "{i}Что?!{/i}"
    m "{i}Она тоже?..{/i}"
    m "{i}Ну вот... придётся молчать.{/i}"
    y 2bf "Наверное, послышалось..."
    play music audio.t12 fadein 2
    y "Хм..."
    y "Так... судя по оформлению ворот, это некий пионер-лагерь..."
    y "И называется он «Совёнок»..."
    show yuri at thide
    hide yuri
    m "Так, теперь и Юри зашла в этот чёртов лагерь..."
    m "Хотя, мне больше интересно, каким образом они вообще попали в игру."
    m "Я же удалила их..."
    m "..."
    m "Похоже, они не лыком шиты..."
    m "Они ещё и меня ищут..."
    m "Ну что же, удачи им."
    m "По крайней мере, Нацуки точно проследит за Юри—{nw}"
    $ s_name = "Ты последняя :("
    show sayori 4bm at t11
    s "Ах!"
    play music audio.t11 fadein 2
    s 2bn "Где это я?.."
    s 3be "..."
    s "Моника..."
    play sound attack_screen
    show layer screens at screen_attack
    s 1bp "ВЫТАЩИ МЕНЯ ОТСЮДА!!!"
    m "{i}Чего?!{/i}"
    m "{i}Конечно, от Сайори можно ожидать чего угодно...{/i}"
    $ s_name = "Сайори"
    m "{i}Но вот такого я от неё никак не ожидала...{/i}"
    m "{i}С другой стороны...{/i}"
    m "{i}Она не ненавидит меня даже после того, как я удалила её?{/i}"
    m "{i}Интересно...{/i}"
    play music audio.t12 fadein 2
    s 1bn "Хм..."
    s "«Пионер-лагерь»?"
    s "«Совёнок»?"
    s "Это где-то у нас в городе?"
    m "{i}Эх...{/i}"
    m "{i}«Любопытной Варваре на базаре нос оторвали», Сайори...{/i}"
    m "{i}Тебе правда так интересно, что там?{/i}"
    m "{i}Стоп...{/i}"
    m "{i}Так мне тоже интересно, что там...{/i}"
    s 1bk "Хм..."
    s "Думаю, туда стоит заглянуть..."
    s 4bx "Наверное, там будет весело!"
    s "Пойду обращусь к вожатой!"
    show sayori at thide
    hide sayori
    m "{i}Хм...{/i}"
    m "{i}Итак, что мы имеем?{/i}"
    m "{i}Три девушки, которых я удалила, чтобы [player] был со мной...{/i}"
    m "{i}Если подумать, то с другой стороны это выглядит довольно смешно...{/i}"
    m "{i}А теперь они пришли сюда и почти что желают моей смерти...{/i}"
    m "..."
    m "По крайней мере, я сейчас могу размышлять вслух..."
    m "Ведь больше никто не придёт, верно?"
    m "Хорошо, тогда я перемещу камеру в лагерь—{nw}"
    python:
        try: renpy.file("../characters/neko-monika.chr")
        except: renpy.jump('nekomonika_kill')
    $ ei_name = "У-у-у, сука..."
    show eileen concerned at t11
    ei "..."
    ei "Что здесь произошло?"
    ei "По-моему, я слышала чей-то крик..."
    ei "И что это за место?.."
    m "И ты туда же?!"
    ei happy "М-м?"
    ei "Кто это сказал?"
    ei "Прятаться бесполезно, я тебя всё равно найду."
    m "{i}О боже...{/i}"
    m "{i}Минуточку...{/i}"
    m "{i}Она-то откуда?{/i}"
    m "{i}Серьёзно, я её не знаю.{/i}"
    
