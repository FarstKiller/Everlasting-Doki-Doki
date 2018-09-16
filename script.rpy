image main_menu_art = "mod_assets/main_menu_art.png"

label edd_input_name:
    if persistent.playername == "":
        $ renpy.jump_out_of_context("edd_input_name2")
    else:
        $ renpy.jump("start")

label edd_input_name2:
    stop music fadeout 3
    scene black
    with Dissolve(2.0, alpha=True)
    $ renpy.pause(2.5, hard=True)
    play music audio.everlast fadein 4
    show main_menu_art
    show noise at bg_alpha(0.15)
    with Dissolve(7, alpha=True)
    $ player = ""
    $ renpy.pause(1.5, hard=True)

label edd_name_main_character:
    $ renpy.call_screen("name_input", "Придумайте имя для протагониста.", ok_action=Jump("finish_user_name"), output_var="player")

label finish_user_name:
    $ renpy.hide_screen("name_input")
    if (not player):
        jump edd_name_main_character
    stop music fadeout 4
    scene black with Dissolve(5, alpha=True)
    $ renpy.jump("start")

label start:


    $ anticheat = persistent.anticheat


    $ chapter = 0

    $ _dismiss_pause = config.developer

    #if hour in [20,21,22,23,24,0,1,2,3,4,5,6]:
        #$ nightmode = "_night"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ allow_skipping = True
    $ config.allow_skipping = True


    if persistent.playthrough == 0:

        $ chapter = 0
        call script_everlast



        return

    elif persistent.playthrough == 1:
        pass

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
label edd_name_cases:
    $ consonants = [u'б', u'в', u'г', u'д', u'ж', u'з', u'й', u'к', u'л', u'м', u'н', u'п', u'р', u'с', u'т', u'ф', u'х', u'ц', u'ч', u'ш', u'щ', u'ь']
    $ combinations = [u'жа', u'ша', u'ща', u'ца']
    $ combinations_special = [u'ка', u'ха']
    $ last_symb = player[-1]
    $ last_symb2 = player[-2:]
    if last_symb in consonants:
        if last_symb == u'й' or last_symb == u'ь':
            $ edd_name_what = player[:len(player)-1]+u'ю'
            $ edd_name_who = player[:len(player)-1]+u'ем'
            $ edd_name_whom = player[:len(player)-1]+u'я'
            $ edd_name_about_someone = player[:len(player)-1]+u'е'
        else:
            $ edd_name_what = player+u'у'
            $ edd_name_who = player+u'ом'
            $ edd_name_whom = player+u'а'
            $ edd_name_about_someone = player+u'е'
    elif last_symb == 'я':
        $ edd_name_what = player[:len(player)-1]+u'и'
        $ edd_name_who = player[:len(player)-1]+u'ей'
        $ edd_name_whom = player[:len(player)-1]+u'ю'
        $ edd_name_about_someone = player[:len(player)-1]+u'е'
    elif last_symb2 in combinations:
        $ edd_name_what = player[:len(player)-1]+u'е'
        $ edd_name_who = player[:len(player)-1]+u'ей'
        $ edd_name_whom = player[:len(player)-1]+u'у'
        $ edd_name_about_someone = player[:len(player)-1]+u'е'
    elif last_symb2 in combinations_special:
        $ edd_name_what = player[:len(player)-1]+u'е'
        $ edd_name_who = player[:len(player)-1]+u'ой'
        $ edd_name_whom = player[:len(player)-1]+u'у'
        $ edd_name_about_someone = player[:len(player)-1]+u'е'
    elif last_symb2 == u'ча':
        $ edd_name_what = player[:len(player)-1]+u'е'
        $ edd_name_who = player[:len(player)-1]+u'ей'
        $ edd_name_whom = player[:len(player)-1]+u'у'
        $ edd_name_about_someone = player[:len(player)-1]+u'е'
    elif last_symb2 == u'иа':
        $ edd_name_what = player[:len(player)-1]+u'е'
        $ edd_name_who = player[:len(player)-1]+u'ой'
        $ edd_name_whom = player[:len(player)-1]+u'у'
        $ edd_name_about_someone = player[:len(player)-1]+u'е'
    elif last_symb == u'а':
        $ edd_name_what = player[:len(player)-1]+u'е'
        $ edd_name_who = player[:len(player)-1]+u'ой'
        $ edd_name_whom = player[:len(player)-1]+u'у'
        $ edd_name_about_someone = player[:len(player)-1]+u'е'
    else:
        $ edd_name_what = player
        $ edd_name_who = player
        $ edd_name_whom = player
        $ edd_name_about_someone = player
        $ edd_name_someone = player

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
