init -100 python:
    import os
    import platform
    import random
    #from time import localtime, strftime
    #t = strftime("%H:%M:%S", localtime())
    #hour, min, sec = t.split(":")
    #hour = int(hour)
    os.name
    platform.system()
    platform.release()
    if platform.release() == "XP":
        renpy.error("Ты неудачник! :D")
    if platform.release() == "Vista":
        renpy.error("Увы, Windows 7 признали лучше Vista.")
    if platform.release() == "2000":
        renpy.error("Молодец, молодой энтузиаст, только вот зачем всё это нужно было? Ты хвастаешься точно так же, как и любители «конструкторов» для Apple Mac II?")
    if platform.release() == "7":
        pass
    if platform.release() == "8":
        pass
    if os.name == "posix":
        pass
    if os.name == "posix" and platform.system() == "Darwin":
        pass
    if not renpy.version_only == "7.1.0.882":
        renpy.error("Так-так-так... что это тут у нас? Пытаемся не использовать порт на новую версию движка? Совсем умом тронулся??? :D")
    if persistent.you_kill_neko-monika = True:
        renpy.error("Ты... ты очень-очень нехороший человек... ВЕРНИ ЕЁ!!!")
        persistent.you_kill_neko-monika = False
    if persistent.you_kill_neko-monika = False:
        try: renpy.file("../characters/neko-monika.chr")
        except: persistent.you_kill_neko-monika = True

init python:
    menu_trans_time = 1
    splash_message_default = "Эта игра является лишь плодом воображения самого разработчика, и она\nне имеет никакого отношения ни к Team Salvato, ни к Soviet Games."
    #splash_message_night = "{color=#ffffff}Эта игра является лишь плодом воображения самого разработчика, и она\nне имеет никакого отношения ни к Team Salvato, ни к Soviet Games.{/color}"
    splash_messages = [
    "Пожалуйста, поддержите «Литературный клуб \"Тук-тук!\"»."
    "Моника следит за вашим кодом."
    ]

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

image menu_bg:
    truecenter
    "bg/ext_camp_entrance_day.jpg"

#image menu_bg_night:
#    truecenter
#    "bg/ext_camp_entrance_night.jpg"

image game_menu_bg:
    truecenter
    "bg/ext_camp_entrance_day.jpg"

#image game_menu_bg_night:
#    truecenter
#    "bg/ext_camp_entrance_night.jpg"

image menu_fade:
    "white"
    menu_fadeout

image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

#image menu_nav_night:
#    "gui/overlay/main_menu_night.png"
#    menu_nav_move

image menu_logo:
    "gui/logo.png"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

#image menu_logo_night:
#    "gui/logo_night.png"
#    subpixel True
#    xcenter 240
#    ycenter 120
#    zoom 0.60
#    menu_logo_move

image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=40, particleTime=2.0, particleXSpeed=3, particleYSpeed=3).sm
    particle_fadeout

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0


image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image intro_ru:
    truecenter
    "white"
    0.5
    "mod_assets/msr-logo.png" with Dissolve(0.5, alpha=True)
    1.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image tos = "mod_assets/warning.png"
image tos2 = "mod_assets/warning2.png"


label splashscreen:

    python:
        process_list = []
        currentuser = ""
        if renpy.windows:
            try:
                process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                pass
            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        currentuser = user
            except:
                pass


    python:
        firstrun = ""
        try:
            firstrun = renpy.file("firstrun").read(1)
        except:
            with open(config.basedir + "/game/firstrun", "wb") as f:
                pass
    if not firstrun:
        if persistent.first_run and (config.version == persistent.oldversion or persistent.autoload == "postcredits_loop"):
            $ quick_menu = False
            scene black
            menu:
                "Обнаружены файлы сохранений. Вы действительно хотите удалить их и начать игру заново?"
                "Да, удалить существующие сохранения.":
                    "Файлы сохранений удаляются...{nw}"
                    python:
                        delete_all_saves()
                        renpy.loadsave.location.unlink_persistent()
                        renpy.persistent.should_save_persistent = False
                        renpy.utter_restart()
                "Нет, продолжить оттуда, где я остановился.":
                    $ restore_relevant_characters()

        python:
            if not firstrun:
                try:
                    with open(config.basedir + "/game/firstrun", "w") as f:
                        f.write("1")
                except:
                    renpy.jump("readonly")

    if config.version != persistent.oldversion:
        $ restore_relevant_characters()
        $ persistent.oldversion = config.version
        $ renpy.save_persistent()

    if not persistent.first_run:
        python:
            restore_all_characters()
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0
        "Эта игра целиком и полностью является плодом воображения её разработчиков."
        "И я очень надеюсь, что вам понравится моя задумка, ведь я делал всё это с душой. :3"
        "А если вы думаете иначе, являетесь БубСракой, или просто настроены против визуальных новелл..."
        "То я советую вам немедленно закрыть игру и проконсультироваться с врачом. :D"
        menu:
            "Нажимая на кнопку «Я согласен», вы соглашаетесь с тем, что с вашей головой всё хорошо и не станете ничего высказывать против Курильни Маунти. :3"
            "Я согласен.":
                pass
            "Я не согласен.":
                $ renpy.quit()
        $ persistent.first_run = True
        scene tos2
        with Dissolve(1.5)
        pause 1.0
        scene black


    python:
        s_kill_early = None
        if persistent.playthrough == 0:
            try: renpy.file("../characters/sayori.chr")
            except: s_kill_early = True
        if not s_kill_early:
            if persistent.playthrough <= 2 and persistent.playthrough != 0:
                try: renpy.file("../characters/monika.chr")
                except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
            if persistent.playthrough <= 1 or persistent.playthrough == 4:
                try: renpy.file("../characters/natsuki.chr")
                except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
                try: renpy.file("../characters/yuri.chr")
                except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
            if persistent.playthrough == 4:
                try: renpy.file("../characters/sayori.chr")
                except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())

    $ basedir = config.basedir.replace('\\', '/')



    if persistent.autoload:
        jump autoload



    $ config.allow_skipping = False

    #if hour in [20,21,22,23,24,0,1,2,3,4,5,6]:
        #$ renpy.movie_cutscene("mod_assets/splash-everlast2.m2t")
    #else:    
    $ renpy.movie_cutscene("mod_assets/splash-everlast.m2t")
    #if hour in [20,21,22,23,24,0,1,2,3,4,5,6]:
        #show black
    #else:
    show white
    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default
    #$ config.main_menu_music = audio.everlast
    #if not hour in [20,21,22,23,24,0,1,2,3,4,5,6] and renpy.random.randint(0, 3) == 0:
    if renpy.random.randint(0, 3) == 0:
        $ config.main_menu_music = audio.eurobeatreality
    else:
        $ config.main_menu_music = audio.everlast
    #if hour in [20,21,22,23,24,0,1,2,3,4,5,6]:
        #$ config.main_menu_music = audio.night
    $ renpy.music.play(config.main_menu_music)
    #if hour in [20,21,22,23,24,0,1,2,3,4,5,6]:
        #$ splash_message = splash_message_night
    show splash_warning "[splash_message]" with Dissolve(1.0, alpha=True)
    pause 5.0
    hide splash_warning with Dissolve(1.0, alpha=True)
    $ config.allow_skipping = True
    return

label after_load:
    if persistent.playthrough == 0:
        $ restore_all_characters()
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ style.say_dialogue = style.normal

    if persistent.playthrough == 0 and not persistent.first_load and not config.developer:
        $ persistent.first_load = True
        call screen dialog("Подсказка: используйте кнопку «Пропуск» для\nбыстрой прокрутки уже прочитанного текста.", ok_action=Return()) 
    return



label autoload:
    python:

        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()


        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
        $ persistent.yuri_kill += 200


    if renpy.get_return_stack():
        $ renpy.pop_call()
    jump expression persistent.autoload

label before_main_menu:
    $ renpy.music.play(config.main_menu_music)
    return

label quit:
    if persistent.ghost_menu:
        hide screen main_menu
        scene white
        show expression "gui/menu_art_m_ghost.png":
            xpos -100 ypos -100 zoom 3.5
        pause 0.01
    return

label readonly:
    scene black
    "Игра не может быть запущена, потому что вы пытаетесь запустить её в защищённой от записи директории (%(firstrun_path)s)."
    "Скопируйте, пожалуйста, игру на рабочий стол или в любое другое место и попробуйте запустить заново."
    $ renpy.quit()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
