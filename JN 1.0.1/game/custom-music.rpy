
default persistent.jn_custom_music_unlocked = False
default persistent.jn_custom_music_explanation_given = False

init python in jn_custom_music:
    import os
    import store
    import store.jn_utils as jn_utils


    CUSTOM_MUSIC_DIRECTORY = os.path.join(renpy.config.basedir, "custom_music/").replace("\\", "/")


    _VALID_FILE_EXTENSIONS = ["mp3", "ogg", "wav"]


    _CHOOSE_PLAY_MUSIC_QUIPS = [
        "Ooh!{w=0.2} You wanna put something else on?{w=0.2} Okay!",
        "You better play something good,{w=0.1} [player]!{w=0.2} Ahaha.",
        "You wanna play something?{w=0.2} Sure!",
        "Ooh!{w=0.2} Some different music?{w=0.2} Now we're talking!",
        "Eh?{w=0.2} Another track?{w=0.2} Go for it,{w=0.1} [player]!",
        "You wanna play something else?{w=0.2} Go for it!",
        "Ooh,{w=0.1} some different music?{w=0.2} What did you have in mind?"
    ]

    _NATSUKI_PICK_MUSIC_QUESTION_QUIPS = [
        "Oho?{w=0.2} You want me to pick?",
        "Huh?{w=0.2} You want me to choose something?",
        "Hmm?{w=0.2} You want me to pick?",
        "Oh?{w=0.2} You want me to choose something to play?",
        "Mmm?{w=0.2} Is it my turn to pick?"
    ]

    _NATSUKI_PICK_MUSIC_ANSWER_QUIPS = [
        "Ehehe.{w=0.1} Sure!",
        "Sure,{w=0.1} why not!",
        "Can do!",
        "Ehehe.{w=0.2} Leave it to me,{w=0.1} [player]!",
        "I thought you'd never ask,{w=0.1} [player]!",
        "Okie-dokie,{w=0.1} [player]!",
        "Finally!{w=0.2} Ahaha.",
        "Now we're talking!"
    ]

    _NATSUKI_PICK_MUSIC_SEARCH_QUIPS = [
        "Now,{w=0.1} let's see...",
        "Let me take a look...",
        "Alright,{w=0.1} what have we got...",
        "Ooh!{w=0.2} How about this?",
        "Let's see here...",
        "Let's see..."
    ]

    _NATSUKI_NO_MUSIC_QUIPS = [
        "Just quiet for now?{w=0.2} Sure!",
        "Not in the mood for music,{w=0.1} [player]?{w=0.2} No worries!",
        "Okay!{w=0.2} Let me just turn that off...",
        "Alright!{w=0.2} I'll turn that off for now...",
        "Sure thing!{w=0.2} Let me just get that for you...",
        "No worries!{w=0.2} Just give me a sec...",
    ]


    _now_playing = None

label music_menu:
    $ Natsuki.setInConversation(True)
    $ music_title = "Error, this should have changed"


    python:
        success = False

        if not jn_utils.createDirectoryIfNotExists(jn_custom_music.CUSTOM_MUSIC_DIRECTORY):
            
            
            custom_music_options = jn_utils.getAllDirectoryFiles(
                path=jn_custom_music.CUSTOM_MUSIC_DIRECTORY,
                extension_list=jn_custom_music._VALID_FILE_EXTENSIONS
            )
            custom_music_options.sort()
            
            
            custom_music_options.insert(0, ("Default", "mod_assets/bgm/just_natsuki.ogg"))
            
            
            if len(custom_music_options) > 1:
                custom_music_options.insert(1, ("You pick!", "random"))
            
            custom_music_options.append(("No music", "no_music"))
            success = True


    if not success:
        show natsuki at jn_center
        n 1kllunl "Uhmm..."
        n 1knmunl "Hey...{w=0.3} [player]?"
        n 1klrbgl "Something went wrong when I was trying look for your music..."
        n 1kchbgl "Can you do me a favour and just check everything out real quick?"
        $ folder = jn_custom_music.CUSTOM_MUSIC_DIRECTORY
        n 1knmbgl "If you forgot -{w=0.1} anything you want me to play needs to be in the {a=[folder]}custom_music{/a} folder."
        n 1uwdaj "Oh!{w=0.2} Right!{w=0.2} And it also needs to be in {i}.mp3,{w=0.1} .ogg or .wav{/i} format -{w=0.1} just look for the letters after the period in the file name!"
        jump ch30_loop

    elif preferences.get_volume("music") == 0:
        show natsuki at jn_center
        n 1tsqaj "Uh...{w=0.5}{nw}"
        extend 1tslaj " huh."
        n 1tsgsg "And {i}how{/i} exactly do you plan to hear any music with the volume at zero?"
        n 1fchbg "Jeez, [player].{w=0.5}{nw}"
        extend 1uchgn " How do you even get dressed in the morning with memory like that?!"
        n 1ullss "Well, whatever.{w=0.5}{nw}"
        extend 1unmaj " So..."
        menu:
            n "Did you want me to turn the music back up so you can pick something?"
            "Yes.":

                n 1nchsm "Okey-{w=0.1}dokey!{w=0.2} Just a second..."
                $ preferences.set_volume("music", 0.75)
                n 1fcsbg "And there we are!"
                n 1ullss "So...{w=0.5}{nw}"
                extend 1unmaj " What did you wanna listen to?"
                show natsuki idle at jn_left
            "No.":

                n 1fcsbg "The sound of silence it is,{w=0.1} then!{w=0.5}{nw}"
                extend 1fchsm " Ehehe."
                jump ch30_loop
    else:

        $ chosen_quip = renpy.substitute(random.choice(jn_custom_music._CHOOSE_PLAY_MUSIC_QUIPS))
        n 1unmbgl "[chosen_quip]"
        show natsuki idle at jn_left


    call screen scrollable_choice_menu(custom_music_options, ("Nevermind.", False))
    show natsuki idle at jn_center

    if not _return:
        jump ch30_loop

    if _return == "no_music":
        $ chosen_no_music_quip = renpy.substitute(random.choice(jn_custom_music._NATSUKI_NO_MUSIC_QUIPS))
        n 1knmsm "[chosen_no_music_quip]"
        $ music_title = "No music"

        stop music fadeout 3
        n 1uchsm "There you go, [player]!"

        if persistent.jn_random_music_enabled:

            $ persistent.jn_random_music_enabled = False
            n 1unmaj "Oh{w=0.1} -{w=0.1} and I'll stop switching around the music too."

    elif _return == "random":

        $ available_custom_music = jn_utils.getAllDirectoryFiles(
            path=jn_custom_music.CUSTOM_MUSIC_DIRECTORY,
            extension_list=jn_custom_music._VALID_FILE_EXTENSIONS
        )


        $ chosen_question_quip = renpy.substitute(random.choice(jn_custom_music._NATSUKI_PICK_MUSIC_QUESTION_QUIPS))
        n 1unmajl "[chosen_question_quip]"

        show natsuki 1uchbg

        $ chosen_answer_quip = renpy.substitute(random.choice(jn_custom_music._NATSUKI_PICK_MUSIC_ANSWER_QUIPS))
        n 1uchbsl "[chosen_answer_quip]"

        $ chosen_search_quip = renpy.substitute(random.choice(jn_custom_music._NATSUKI_PICK_MUSIC_SEARCH_QUIPS))
        n 1ullbgl "[chosen_search_quip]"


        python:
            if len(available_custom_music) > 1:
                music_title_and_file = random.choice(filter(lambda track: (jn_custom_music._now_playing not in track), available_custom_music))
                music_title = music_title_and_file[0]
                renpy.play(filename=music_title_and_file[1], channel="music")

    elif _return is not None:

        $ music_title = store.jn_utils.escapeRenpySubstitutionString(_return.split('/')[-1])
        $ renpy.play(filename=_return, channel="music")


    $ jn_custom_music._now_playing = music_title
    $ renpy.notify("Now playing: {0}".format(jn_custom_music._now_playing))

    jump ch30_loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
