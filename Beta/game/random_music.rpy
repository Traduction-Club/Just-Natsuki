default persistent.jn_random_music_enabled = False

init python in jn_random_music:
    import random
    import store
    import store.jn_affinity as jn_affinity
    import store.jn_custom_music as jn_custom_music
    import store.jn_plugins as jn_plugins
    import store.jn_utils as jn_utils

    _NEW_TRACK_QUIPS = [
        "¡Muy bien!{w=0.2} ¡Es hora de cambiar esta canción,{w=0.1} creo yo!",
        "¡Venga!{w=0.2} ¡Hora de otra canción!",
        "Creo que ya me harté de esta canción.",
        "Ya es suficiente de esta canción por ahora,{w=0.1} al menos por mi parte.",
        "¡Hora de una nueva canción!",
        "¡Ya me harté de esta canción!",
        "Quiero escuchar algo más...",
        "¡Hora de un cambio de aires!"
    ]

    _NEW_TRACK_FOLLOWUPS = [
        "Bien, vamos a ver...",
        "Y ahora, a ver que tenemos...",
        "Veamos que hay por aquí..."
        "Que mas tenemos por aquí...",
        "¡Aja!{w=0.2} ¡Tengo que probar esta otra!",
        "Déjame ver..."
    ]

    def random_music_change_check():
        """
        Determines if Natsuki should pick a new song to play in the background.
        """

        if (store.persistent.jn_custom_music_unlocked
            and store.persistent.jn_random_music_enabled
            and store.Natsuki.isAffectionate(higher=True)
            and store.preferences.get_volume("music") > 0
            and len(jn_custom_music.get_all_custom_music()) >= 2):

            store.push("random_music_change")
            renpy.jump("call_next_topic")

label random_music_change:
    $ track_quip = random.choice(jn_random_music._NEW_TRACK_QUIPS)
    n 1nchbg "[track_quip]{w=2}{nw}"
    $ track_followup = random.choice(jn_random_music._NEW_TRACK_FOLLOWUPS)
    n 1unmbgl "[track_followup]{w=2}{nw}"
    stop music fadeout 3

    python:
        music_title_and_file = random.choice(filter(lambda track: (jn_custom_music._now_playing not in track), jn_custom_music.get_all_custom_music()))
        music_title = music_title_and_file[0]
        renpy.play(filename=music_title_and_file[1], channel="music", fadein=3)
        jn_custom_music._now_playing = music_title
        renpy.notify("Sonando ahora: {0}".format(jn_custom_music._now_playing))

    jump ch30_loop

# Enable random music
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="random_music_enable",
            unlocked=True,
            prompt="¿Podrías cambiar la música personalizada por mí?",
            conditional="persistent.jn_custom_music_unlocked and not persistent.jn_random_music_enabled",
            category=["Música"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label random_music_enable:
    n 1unmbg "¡Ooh!{w=0.5}{nw}"
    extend 1fchbg " Claro,{w=0.1} ¡déjamelo a mí!"
    n 1unmss "Pondré una nueva mas o menos cada cincuenta minutos,{w=0.1} ¿'tá bien?"
    n 1uwdaj "¡Oh!{w=0.5}{nw}"
    extend 1fllbg " Casi me olvido {w=0.1}-{w=0.1} primero déjame comprobar si hay suficiente música para hacer esto."
    n 1ncsbo "..."

    if len(jn_custom_music.get_all_custom_music()) >= 2:
        # Proceed if we have at least two tracks
        n 1uchgn "¡Muuuy bien!{w=0.2} ¡Creo que aquí hay suficiente con lo que trabajar!{w=0.5}{nw}"
        extend 1nchsm " Jejeje."
        n 1nsqsm "No te preocupes,{w=0.1} [player].{w=0.5}{nw}"
        extend 1fcsbg " ¡Escogeré las mejores para ti!"
        $ persistent.jn_random_music_enabled = True

    elif preferences.get_volume("music") == 0:
        # Cancel if the player has music volume set to zero
        n 1nsqem "Uh...{w=0.5} ahm."
        n 1tsqca "¿Y exactamente {i}como{/i} planeabas escuchar nada con el volumen a cero?"
        n 1uchbg "Diooos...{w=0.3} a veces eres realmente idiota,{w=0.1} [player].{w=0.5}{nw}"
        extend 1nchsm " Jejeje."
        n 1fwlsm "Venga, vuelve a subirla{w=0.1} y entonces ya hablaremos.{w=0.2} ¿Entendido?"

    else:
        # Cancel if the player doesn't have a selection of custom music
        n 1tllaj "Ehmm...{w=0.3} [player]?{w=0.5}{nw}"
        extend 1tnmca " Pues no es que me hayas dado mucho con lo que poder trabajar."
        n 1unmaj "¿Podrías al menos darme un par de canciones?{w=0.5}{nw}"
        extend 1tnmpo " Todavía te {i}acuerdas{/i} de como se hacía,{w=0.1} ¿cierto?"
        $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
        n 1uchbg "¡Tan solo tienes que añadirlas a la carpeta de música personalizada,{w=0.1} [chosen_tease]!"

    jump ch30_loop

# Disable random music
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="random_music_disable",
            unlocked=True,
            prompt="¿Puedes dejar de reproducir mi música personalizada aleatoriamente?",
            conditional="persistent.jn_custom_music_unlocked and persistent.jn_random_music_enabled",
            category=["Música"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label random_music_disable:
    n 1unmaj "¿Ah?{w=0.2} Guau.{w=0.5}{nw}"
    extend 1nsqsf " ¿Las canciones que elijo son {i}tan{/i} malas,{w=0.1} [player]?"
    n 1fsrsm "...Jejeje."
    n 1uchbg "Solo te estoy molestando.{w=0.2} ¡Por supuesto!{w=0.5}{nw}"
    extend 1nchsm " Déjame que ponga la música predeterminada."

    stop music fadeout 3
    play music audio.just_natsuki_bgm fadein 3

    n 1nwlbg "...¡Y ya estaría!"

    $ persistent.jn_random_music_enabled = False
    jump ch30_loop
