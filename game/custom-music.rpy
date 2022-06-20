# General tracking; the player unlocks Snap by admitting boredom to Natsuki at least once
default persistent.jn_custom_music_unlocked = False
default persistent.jn_custom_music_explanation_given = False

init python in jn_custom_music:
    import os
    import store

    # Tracks must be placed here for Natsuki to find them
    CUSTOM_MUSIC_DIRECTORY = os.path.join(renpy.config.basedir, "custom_music/").replace("\\", "/")

    # The file extensions we (Ren'Py) support
    _VALID_FILE_EXTENSIONS = [".mp3", ".ogg", ".wav"]

    # Variety in dialogue :)
    _CHOOSE_PLAY_MUSIC_QUIPS = [
        "¡Ooh!{w=0.2} ¿Quieres poner algo más?{w=0.2} ¡Está bien!",
        "¡Mas te vale poner una buena,{w=0.1} [player]!{w=0.2} Jajaja.",
        "¿Quieres poner algo de música?{w=0.2} ¡Claro!",
        "¡Ooh!{w=0.2} ¿Una canción diferente?{w=0.2} ¡Por fin estamos en las mismas!",
        "¿Eh?{w=0.2} ¿Otra canción?{w=0.2} Venga, ¡dale{w=0.1} [player]!",
        "¿Quieres poner algo más?{w=0.2} ¡Venga cámbiala!",
        "Ooh,{w=0.1} ¿quieres una música diferente?{w=0.2} ¿Qué tienes en mente?"
    ]

    _NATSUKI_PICK_MUSIC_QUESTION_QUIPS = [
        "¿Ojo?{w=0.2} ¿Quieres que elija yo?",
        "¿Eh?{w=0.2} ¿Quieres que sea yo la que elija?",
        "¿Hmm?{w=0.2} ¿Quieres que elija yo por ti?",
        "¿Oh?{w=0.2} ¿Quieres que yo elija cual poner?",
        "¿Mmm?{w=0.2} ¿Es mi turno de elegir?"
    ]

    _NATSUKI_PICK_MUSIC_ANSWER_QUIPS = [
        "Jejeje.{w=0.1} ¡Por supuesto!",
        "Claro,{w=0.1} ¡por qué no!",
        "¡Puedo con ello!",
        "Jejeje.{w=0.2} ¡Dejamelo a mi,{w=0.1} [player]!",
        "¡Pensé que nunca me lo preguntarías,{w=0.1} [player]!",
        "¡Oki-doki,{w=0.1} [player]!",
        "¡Por fin!{w=0.2} Jajaja.",
        "¡Ahora sí que sí!"
    ]

    _NATSUKI_PICK_MUSIC_SEARCH_QUIPS = [
        "Ahora,{w=0.1} vamos a ver...",
        "Déjame echar un vistazo...",
        "Muy bien,{w=0.1} que tenemos aquí...",
        "¡Ooh!{w=0.2} ¿Y esta?",
        "A ver esta de aquí...",
        "A ver..."
    ]

    _NATSUKI_NO_MUSIC_QUIPS = [
        "¿Quieres un poquito de silencio?{w=0.2} ¡Venga!",
        "¿No estas de humor para escuchar música,{w=0.1} [player]?{w=0.2} ¡No te preocupes!",
        "¡Vale!{w=0.2} Tan solo déjame apagarla...",
        "¡Muy bien!{w=0.2} Voy a pararla por ahora...",
        "¡Por supuesto!{w=0.2} Déjame que la pare por ahora...",
        "¡No hay problema!{w=0.2} Tan solo dame un segundo...",
    ]

    # Tracks what is currently playing to avoid repetition with random music picks
    _now_playing = None

    def get_directory_exists():
        """
        Checks to see if the custom_music directory exists, and creates it if not
        Returns True/False based on whether the directory already existed

        OUT:
            - True/False based on if directory was existing (True) or had to be created (False)
        """
        if not os.path.exists(CUSTOM_MUSIC_DIRECTORY):
            os.makedirs(CUSTOM_MUSIC_DIRECTORY)
            return False

        return True

    def get_all_custom_music():
        """
        Runs through the files in the custom_music directory, identifying supported music files via extension check
        Returns a tuple representing (file_name, file_path_for_renpy_playback)

        OUT:
            - Tuple representing (file_name, file_path_for_renpy_playback)
        """
        global CUSTOM_MUSIC_DIRECTORY
        return_file_items = []

        for file in os.listdir(CUSTOM_MUSIC_DIRECTORY):
            if any(file_extension in file for file_extension in _VALID_FILE_EXTENSIONS):

                # Valid audio track - return displayed prompt and file name
                return_file_items.append((file, os.path.join(CUSTOM_MUSIC_DIRECTORY, file)))

        return return_file_items

label music_menu:

    $ jn_globals.player_is_in_conversation = True
    $ music_title = "Error, esto debería haber cambiado"

    # Attempt to get the music in the custom_music directory to present as menu options
    python:
        success = False

        if jn_custom_music.get_directory_exists():

            # Get the user's music, then sort the options for presentation
            custom_music_options = jn_custom_music.get_all_custom_music()
            custom_music_options.sort()

            # Add the default music as the first option
            custom_music_options.insert(0, ("Predeterminada", "mod_assets/bgm/just_natsuki.ogg"))

            # Add random option if we have more than one potential track for Nat to pick
            if len(custom_music_options) > 1:
                custom_music_options.insert(1, ("¡Elige tú!", "random"))

            custom_music_options.append(("Quitar música", "no_music"))
            success = True

    # We failed to get the custom music, prompt player to correct
    if not success:
        show natsuki at jn_center
        n 1kllunl "Ehmm..."
        n 1knmunl "Oye...{w=0.3} ¿[player]?"
        n 1klrbgl "Algo ha salido mal cuando intentaba encontrar tu música..."
        n 1kchbgl "¿Puedes hacerme el favor y darle una revisadita rápida?"
        $ folder = jn_custom_music.CUSTOM_MUSIC_DIRECTORY
        n 1knmbgl "Por si te has olvidado -{w=0.1} cualquier canción que quieras que yo ponga debe estar en la carpeta {a=[folder]}custom_music{/a}."
        n 1uwdaj "¡Oh!{w=0.2} Right!{w=0.2} Y también debe estar en formato {i}.mp3,{w=0.1} .ogg o .wav{/i} -{w=0.1} ¡tan solo fíjate en las letras después del punto en el nombre del archivo!"
        jump ch30_loop

    elif preferences.get_volume("music") == 0:
        show natsuki at jn_center
        n 1tsqaj "Eh...{w=0.5}{nw}"
        extend 1tslaj " ahm."
        n 1tsgsg "¿Y exactamente {i}como{/i} planeabas escuchar nada con el volumen a cero?"
        n 1fchbg "Dios, [player].{w=0.5}{nw}" 
        extend 1uchgn " ¡¿Cómo haces para salir vestido a la calle con una memoria como esa?!"
        n 1ullss "Bueno, como sea.{w=0.5}{nw}"
        extend 1unmaj " Así que..."
        menu:
            n "¿Quieres que suba la música por ti para que puedas poner algo?"

            "Sí.":
                n 1nchsm "¡Oki-{w=0.1}doki!{w=0.2} Dame un segundito..."
                $ preferences.set_volume("music", 0.75)
                n 1fcsbg "¡Y ya está!"
                n 1ullss "Entonces...{w=0.5}{nw}"
                extend 1unmaj " ¿Qué quieres escuchar?"

            "No.":
                n 1fcsbg "¡Pongamos 'the sound of silence'{w=0.1} entonces!{w=0.5}{nw}"
                extend 1fchsm " Jejeje."
                jump ch30_loop

    else:
        $ chosen_quip = renpy.substitute(random.choice(jn_custom_music._CHOOSE_PLAY_MUSIC_QUIPS))
        n 1unmbgl "[chosen_quip]"
        show natsuki idle at jn_left

    # We have custom music options, present the choices
    call screen scrollable_choice_menu(custom_music_options, ("No importa.", False))
    show natsuki idle at jn_center

    if not _return:
        jump ch30_loop

    if _return == "no_music":
        $ chosen_no_music_quip = renpy.substitute(random.choice(jn_custom_music._NATSUKI_NO_MUSIC_QUIPS))
        n 1knmsm "[chosen_no_music_quip]"
        $ music_title = "Música quitada"

        stop music fadeout 3
        n 1uchsm "¡Ahí va, [player]!"
        
        if persistent.jn_random_music_enabled:
            # Stop playing random music, if enabled
            $ persistent.jn_random_music_enabled = False
            n 1unmaj "Oh{w=0.1} -{w=0.1} y ahora ya no cambiare más de canción."

    elif _return == "random":

        $ available_custom_music = jn_custom_music.get_all_custom_music()

        # Play a random track
        $ chosen_question_quip = renpy.substitute(random.choice(jn_custom_music._NATSUKI_PICK_MUSIC_QUESTION_QUIPS))
        n 1unmajl "[chosen_question_quip]"

        show natsuki 1uchbg zorder JN_NATSUKI_ZORDER

        $ chosen_answer_quip = renpy.substitute(random.choice(jn_custom_music._NATSUKI_PICK_MUSIC_ANSWER_QUIPS))
        n 1uchbsl "[chosen_answer_quip]"

        $ chosen_search_quip = renpy.substitute(random.choice(jn_custom_music._NATSUKI_PICK_MUSIC_SEARCH_QUIPS))
        n 1ullbgl "[chosen_search_quip]"

        # If we have more than one track, we can make sure the new chosen track isn't the same as the current one
        python:
            if len(available_custom_music) > 1:
                music_title_and_file = random.choice(filter(lambda track: (jn_custom_music._now_playing not in track), available_custom_music))
                music_title = music_title_and_file[0]
                renpy.play(filename=music_title_and_file[1], channel="music")

    elif _return is not None:
        # Play the selected specific track
        $ music_title = _return.split('/')[-1]
        $ renpy.play(filename=_return, channel="music")

    # Pop a cheeky notify with the Nat for visual confirmation :)
    $ jn_custom_music._now_playing = music_title
    $ renpy.notify("Sonando ahora: {0}".format(jn_custom_music._now_playing))

    jump ch30_loop
