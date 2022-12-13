default persistent._event_database = dict()

image poetry_attempt = "mod_assets/props/poetry_attempt.png"
image parfait_manga_held = "mod_assets/props/parfait_manga_held.png"

init python in jn_events:
    import random
    import store
    import store.jn_atmosphere as jn_atmosphere
    import store.jn_affinity as jn_affinity

    JN_EVENT_PROP_ZORDER = 4

    EVENT_MAP = dict()

    def select_event():
        """
        Picks and returns a random event, or None if no events are left.
        """
        kwargs = dict()
        event_list = store.Topic.filter_topics(
            EVENT_MAP.values(),
            unlocked=True,
            affinity=store.Natsuki._getAffinityState(),
            is_seen=False,
            **kwargs
        )

        # Events are one-time only, so we sanity check here
        if len(event_list) > 0:
            return random.choice(event_list).label

        else:
            return None

    def display_visuals(natsuki_sprite_code):
        """
        Sets up the visuals/audio for an instant "pop-in" effect after a black scene opening.
        Note that we start off from ch30_autoload with a black scene by default.

        IN:
            - natsuki_sprite_code - The sprite code to show Natsuki displaying before dialogue
        """
        # Draw background, with Natsuki using the given sprite code
        store.main_background.appear(natsuki_sprite_code)

        if store.persistent.jn_random_weather and 6 < store.jn_get_current_hour() <= 18:
            jn_atmosphere.show_random_sky()

        elif (
            store.jn_get_current_hour() > 6 and store.jn_get_current_hour() <= 18
            and not jn_atmosphere.is_current_weather_sunny()
        ):
            jn_atmosphere.show_sky(jn_atmosphere.WEATHER_SUNNY)

        # UI, music
        renpy.show_screen("hkb_overlay")
        renpy.play(filename="mod_assets/bgm/just_natsuki.ogg", channel="music")

# Natsuki is walked in on reading a new volume of Parfait Girls. She isn't impressed.
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_caught_reading_manga",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 86400 >= 2",
            affinity_range=(jn_affinity.NORMAL, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_caught_reading_manga:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "..."
    play audio page_turn
    $ renpy.pause(2)
    n "E-{w=0.1}espera...{w=0.3} ¡¿Qué?!"
    n "¡M-{w=0.1}Minori!{w=0.5}{nw}"
    extend " ¡{i}Idiota{/i}!"
    n "¡En serio, no me lo creo...!"
    n "Agh...{w=0.5}{nw}"
    extend " ¿{i}esto{/i} era lo que se suponía que debía esperarme?"
    n "Vamos...{w=0.5}{nw}"
    extend " dame un respiro..."

    play audio page_turn
    $ renpy.pause(5)
    play audio page_turn
    $ renpy.pause(7)

    menu:
        "Entrar...":
            pass

    $ jn_events.display_visuals("1fsrpo")
    show parfait_manga_held zorder jn_events.JN_EVENT_PROP_ZORDER
    $ jn_globals.force_quit_enabled = True

    n 1uskem "¡...!"
    n 1uskeml "¡[player]!{w=0.5}{nw}"
    extend 1fcsan " ¿P-{w=0.1}puedes {i}creerte{/i} esto?"
    n 1fllfu "Parfait Girls ahora tiene una nueva editorial,{w=0.3}{nw}"
    extend 1fbkwr " ¡y no tengo la menor {i}idea{/i} de que creen que hacen!"
    n 1flrwr "Quiero decir,{w=0.1} ¡¿has {i}visto{/i} esta basura?!{w=0.5}{nw}"
    extend 1fcsfu " ¡¿Siquiera se han leído los originales?!"
    n 1fcsan "¡{i}Como{/i} si Minori fuera a caer tan bajo como para-!"
    n 1unmem "¡...!"
    n 1fllpol "..."
    n 1fcspo "De hecho,{w=0.1} ¿sabes qué?{w=0.2} No pasa nada."
    n 1fsrss "No quiero hacerte ningún spoiler."
    n 1flldv "Jejeje..."
    n 1nllpol "Simplemente...{w=0.5}{nw}"
    extend 1nlrss " lo dejare a un lado."

    play audio drawer
    hide parfait_manga_held
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    n 1ulraj "Así que..."
    n 1fchbg "¿Qué te cuentas,{w=0.1} [player]?"

    return

# Natsuki is walked in on getting frustrated with her poetry, and gets flustered.
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_caught_writing_poetry",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 86400 >= 7",
            affinity_range=(jn_affinity.AFFECTIONATE, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_caught_writing_poetry:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "Mmmm...{w=0.5}{nw}"
    extend " ¡agh!"

    play audio paper_crumple
    $ renpy.pause(7)

    n "..."
    n "¡Nnnnnn-!"
    n "¡No soy capaz de {i}concentrarme{/i}!{w=0.5}{nw}"
    extend " ¿Por qué me cuesta {i}tanto{/i} ahora?"

    play audio paper_crumple
    $ renpy.pause(7)

    n "¡Rrrrr...!"
    n "Oh,{w=0.1} {i}¡que le den!{/i}"

    play audio paper_crumple
    $ renpy.pause(3)
    play audio paper_throw
    $ renpy.pause(7)

    menu:
        "Entrar...":
            pass

    $ jn_events.display_visuals("1fsrpo")
    show poetry_attempt zorder jn_events.JN_EVENT_PROP_ZORDER
    $ jn_globals.force_quit_enabled = True

    n 1uskupl "¡...!"
    $ player_initial = jn_utils.get_player_initial()
    n 1uskgsf "¡¿[player_initial]-[player]?!{w=0.5}{nw}"
    extend 1fbkwrl " ¡¿Desde hace cuánto que estás ahí?!"
    n 1fllpol "..."
    n 1uskeml "¿E-{w=0.1}eh? ¿Esto?{w=0.5}{nw}"
    extend 1fcswrl " ¡N-{w=0.1}no es nada!{w=0.5}{nw}"
    extend 1flrpol " ¡Nada de nada!"

    play audio drawer
    hide poetry_attempt
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    n 1nslpol "..."
    n 1kslss "A-{w=0.1}así que...{w=0.5}{nw}"
    extend 1flldv " ¿Cómo estás,{w=0.1} [player]?"

    return

# Natsuki is disillusioned with the relationship, and can't suppress her anger and frustration.
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_relationship_doubts",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 86400 >= 5",
            affinity_range=(None, jn_affinity.DISTRESSED)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_relationship_doubts:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "..."
    n "Donde está el {i}punto{/i} en todo esto..."
    n "Simplemente..."
    n "..."

    if Natsuki.isDistressed(higher=True):
        n "{w=2}{i}Odio{/i}{w=2} esto."

    else:
        n "{w=2}{i}ODIO{/i}{w=2} esto."

    n "Lo odio.{w=1} Lo odio.{w=1} Lo odio.{w=1} Lo odio.{w=1} Yo {w=2}{i}lo{/i}{w=2} odio."
    $ renpy.pause(5)

    if Natsuki.isRuined() and random.randint(0, 10) == 1:
        play audio glitch_a
        show glitch_garbled_red zorder 99 with vpunch
        n "¡¡LO {i}DETESTO{/i}!!{w=0.5}{nw}"
        hide glitch_garbled_red
        $ renpy.pause(5)

    menu:
        "Entrar.":
            pass

    $ jn_events.display_visuals("1fcsupl")
    $ jn_globals.force_quit_enabled = True

    n 1fsqunl "..."
    n 1fsqem "...Oh.{w=1}{nw}"
    extend 1fsrsr " {i}You're{/i} here."
    n 1ncsem "{i}Genial{/i}..."
    n 1fcsan "Claro, eso es {i}justamente{/i} lo que necesitaba en este momento."

    return

# Natsuki tries fiddling with the game, it doesn't go well.
init 5 python:
    registerTopic(
        Topic(
            persistent._event_database,
            label="event_code_fiddling",
            unlocked=True,
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 86400 >= 3",
            affinity_range=(jn_affinity.NORMAL, None)
        ),
        topic_group=TOPIC_TYPE_EVENT
    )

label event_code_fiddling:
    $ jn_globals.force_quit_enabled = False
    n "..."
    n "Mmm..."
    n "¡Aja!{w=0.5}{nw}"
    extend " Ya veo,{w=0.1} ya veo."
    n "Así que,{w=0.3} como pensaba...{w=1}{nw}"
    extend " si hago esto...{w=1.5}{nw}"
    extend " con mucho...{w=2}{nw}"
    extend " mucho cuidado...{w=0.5}{nw}"

    play audio static
    show glitch_garbled_a zorder 99 with vpunch
    hide glitch_garbled_a

    n "¡Ugh-!{w=2}{nw}"
    extend " Carajo,{w=0.3} ¡eso {i}duele{/i}!"
    n "Agh..."
    n "¿Como demonios hizo Monika para jugar con esto todo este tiempo?"
    extend " ¡Este código es {i}horrible{/i}!"
    n "..."
    n "..."
    n "Pero...{w=1} que pasaría si yo-{w=0.5}{nw}"

    play audio static
    show glitch_garbled_c zorder 99 with hpunch
    hide glitch_garbled_c

    n "¡Auch!"
    n "..."
    n "...Estaba claro,{w=0.3} no.{w=0.5} Creo que tengo suficiente por ahora.{w=1}{nw}"
    extend " Estoy exhausta..."
    $ renpy.pause(7)

    menu:
        "Entrar...":
            pass

    $ jn_events.display_visuals("1fslpo")
    $ jn_globals.force_quit_enabled = True

    $ player_initial = jn_utils.get_player_initial()
    n 1uskeml "¡Ahh-!"
    n 1fbkwrl "¡[player_initial]-{w=0.1}[player]!"
    extend 1fcseml " ¡¿{i}Tratas{/i} ¡¿Tratas que me dé un ataque al corazón o qué?!"
    n 1fllpol "Dios..."
    n 1fsrpo "Hola a ti también,{w=0.1} idiota..."

    return
