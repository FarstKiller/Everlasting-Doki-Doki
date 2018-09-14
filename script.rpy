


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
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
