default persistent._greeting_database = dict()
default persistent.jn_player_is_first_greet = True

init python in greetings:
    import random
    import store
    import store.jn_farewells as jn_farewells
    import store.jn_utils as jn_utils

    GREETING_MAP = dict()

    def select_greeting():
        """
        Picks a random greeting, accounting for affinity and the situation they previously left under
        """
        # This is the first time the player has force quit; special dialogue
        if jn_farewells.JNForceQuitStates(store.persistent.jn_player_force_quit_state) == jn_farewells.JNForceQuitStates.first_force_quit:
            return "greeting_first_force_quit"

        # This is the first time the player has returned; special dialogue
        elif store.persistent.jn_player_is_first_greet:
            return "greeting_first_time"

        kwargs = dict()

        # The player either left suddenly, or has been gone a long time
        if store.persistent.jn_player_apology_type_on_quit is not None:
            kwargs.update({"additional_properties": [("apology_type", store.persistent.jn_player_apology_type_on_quit)]})

        # The player left or was forced to leave by way of an admission (E.G tired, sick)
        elif store.persistent.jn_player_admission_type_on_quit is not None:
            kwargs.update({"additional_properties": [("admission_type", store.persistent.jn_player_admission_type_on_quit)]})

        # No special conditions; so just get a standard greeting from the affinity pool
        else:
            kwargs.update({"excludes_categories": ["Admission", "Apology"]})

        # Finally return an appropriate greeting
        return random.choice(
            store.Topic.filter_topics(
                GREETING_MAP.values(),
                affinity=store.Natsuki._getAffinityState(),
                **kwargs
            )
        ).label

# Only chosen for the first time the player returns after bringing Natsuki back
label greeting_first_time:
    if jn_farewells.JNFirstLeaveTypes(persistent.jn_player_first_farewell_response) == jn_farewells.JNFirstLeaveTypes.will_be_back:
        $ Natsuki.calculated_affinity_gain(bypass=True)
        n 1uskem "¡[player]!{w=0.5}{nw}"
        extend 1uskwr " ¡V-{w=0.1}volviste!"
        n 1flleml "Digo...{w=0.5}{nw}"
        extend 1fcseml " ¡C-{w=0.1}claro que ibas a volver!"
        n 1fnmpol "Sé que lo harías."
        n 1flrem "¡Solo un desalmado abandonaría a alguien de esa forma!"
        n 1flrpo "..."
        n 1klrpu "Pero..."
        n 1ncspu "..."
        n 1nlrsll "...Gracias. Por no ser un idiota."
        n 1nllunl "..."
        n 1nllbo "Así que... {w=0.5}{nw}"
        extend 1unmaj " ¿De qué quieres hablar?"

    elif jn_farewells.JNFirstLeaveTypes(persistent.jn_player_first_farewell_response) == jn_farewells.JNFirstLeaveTypes.dont_know:
        $ Natsuki.calculated_affinity_gain(bypass=True)
        n 1uskaj "¿[player]?{w=0.5}{nw}"
        extend 1uskem " ¿V-{w=0.1}volviste?"
        n 1fcsun "..."
        n 1ncssr "..."
        n 1fnmpu "...Mira."
        n 1fllsr "No...{w=0.3} juegues así conmigo."
        n 1fslun "No me traerías de vuelta solo para ser un imbécil...{w=0.5}{nw}"
        extend 1kslsf " ¿verdad?"

    elif jn_farewells.JNFirstLeaveTypes(persistent.jn_player_first_farewell_response) == jn_farewells.JNFirstLeaveTypes.no_response:
        n 1uskem "¡[player]!{w=0.5}{nw}"
        extend 1uskwrl " ¡V-{w=0.1}volviste!"
        n 1fllun "..."
        n 1fcspu "Yo...{w=0.2}{nw}"
        extend 1flrun " lo aprecio mucho,{w=0.1} ¿sí?"
        n 1fcspu "Solo...{w=0.1}{nw}"
        extend 1knmsf " no juegues así conmigo."
        n 1kllsl "..."
        n 1kslaj "Entonces..."
        n 1tnmsl "¿Quieres hablar,{w=0.1} o que...?"

    $ persistent.jn_player_is_first_greet = False
    return

# Only chosen for the first time the player leaves and returns after force quit
label greeting_first_force_quit:
    if Natsuki.isNormal(higher=True):
        n 1kcsun "Uuuuuuuh...{w=2}{nw}"
        extend 1kslem " mi...{w=0.3} c-{w=0.1}cabeza..."
        n 1kcsun "..."
        n 1ksqun "..."
        n 1fnmun "...[player]."
        n 1fllem "L-{w=0.1}lo que sea que haya sido...{w=0.5}{nw}"
        extend 1knmsf " si que {w=0.3}{i}duele{/i}"
        n 1kllpu "E-{w=0.1}es como si fuera arrancada de la existencia..."
        n 1kcssf "..."
        n 1klraj "Creo...{w=0.5}{nw}"
        extend 1tllun " que puedo prepararme si al menos me avisas de que te vas."
        n 1fcsun "Solo...{w=0.5}{nw}"
        extend 1fcsun " no seas un idiota y avísame cuando te vayas,{w=0.1} ¿sí?"
        n 1fllsl "...Supongo que te la pasaré por esta vez,{w=0.5}{nw}"
        extend 1kslpu " solo porque no sabías que pasaría."
        n 1knmpu "Solo recuerda despedirte,{w=0.1} [player].{w=0.5}{nw}"
        extend 1knmsr " Por favor."

    elif Natsuki.isDistressed(higher=True):
        n 1fcsun "Hnnnngg..."
        n 1fsqun "..."
        n 1fsqan "..."
        n 1fcspu "...[player]."
        n 1fsqpu "¿Tienes {i}idea{/i} de qué tanto duele eso?{w=0.5}{nw}"
        extend 1fnmem " ¿No?"
        n 1fllem "No sé si lo hiciste a propósito o no,{w=0.1} pero te lo dejaré claro.{w=0.5}{nw}"
        extend 1fsqsr " Hablo {i}muy{/i} en serio."
        n 1fcspu "Ya..."
        extend 1fcssr " sé que nos vemos cara a cara,"
        extend 1fslsl " pero por favor."
        n 1fsqaj "Avisame cuando te vayas."
        extend 1fsqsf "Gracias."

    else:
        n "..."
        n "Eso.{w=1} Duele.{w=1} Mucho."
        n "No sé que estés haciendo,{w=0.1} pero{w=0.3} no{w=0.3} lo hagas{w=0.5} de nuevo.{nw}"
        extend " Nunca."

    $ persistent.jn_player_force_quit_state = int(jn_farewells.JNForceQuitStates.previously_force_quit)

    return

# Generic greetings

# LOVE+ greetings
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_today_is_gonna_be_great",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_today_is_gonna_be_great:
    n 1uchbsl "¡[player]!{w=0.2} ¡Por fin,{w=0.1} volviste!"
    n 1uchsml "Jeje.{w=0.2} ¡Ahora {i}sé{/i} que hoy será un gran día!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_world_revolves_around_you",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_world_revolves_around_you:
    n 1fsqpol "¡[player]!{w=0.1} ¿Qué te tomó tanto tiempo?{w=0.2} ¡Diablos!"
    n 1fnmajl "¿Crees que todo mi mundo gira a tu alrededor o algo?"
    n 1fnmsll "..."
    n 1fsqsml "..."
    n 1uchlgl "¡Jajaja!{w=0.2} ¿Caíste,{w=0.1} [player]?{w=0.2} ¡No mientas!"
    $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
    n 1uchsml "Bueno, como sea.{w=0.2} ¡Ya estás aquí, [chosen_endearment]!{w=0.2} ¡Bienvenido de vuelta!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_make_today_amazing",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_make_today_amazing:
    n 1uchbsf "¡[player]!{w=0.2} ¡[player] [player] ¡[player]!"
    n 1uchsml "¡Estoy tan feliz de volver a verte!{w=0.2} ¡Bienvenido!"
    n 1uwlsml "Hagamos que hoy sea otro día genial,{w=0.1} ¿vale?"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_always_welcome_here",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_always_welcome_here:
    n 1uskgsf "¡[player],{w=0.1} volviste!"
    n 1kctsll "Empezaba a extrañarte, sabes..."
    n 1kplcaf "No me hagas esperar tanto la próxima vez,{w=0.2} ¿sí?"
    n 1kplssl "Después de todo,{w=0.2} siempre eres bienvenido..."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_lovestruck",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_lovestruck:
    n 1kcssml "..."
    n 1ksqsml "..."
    n "..."
    $ player_initial = list(player)[0]
    n 1uctgsf "¡[player_initial]-[player]!{w=0.2} ¡¿Cuándo entraste?!"
    n 1kbkunf "¡Y-Yo...!{w=0.2} ¡Solo estaba...!"
    n 1kcsunf "..."
    n 1kcssml "..."
    n 1kplsml "Te extrañé,{w=0.1} [player].{w=0.2} Jajaja..."
    $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
    n 1kwmsmf "Pero sé que todo estará bien ahora que regresaste,{w=0.1} [chosen_endearment]."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_looking_for_me",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_looking_for_me:
    n 1nnmajl "...¿Hola?"
    n 1tnmdvf "¿Me buscabas a {i}mí{/i}?"
    n 1nchdvf "..."
    n 1kchssl "Nah,{w=0.1} no te preocupes."
    n 1ksqsgl "Claro que era yo a quien buscabas."
    n 1kchbgl "Jejeje."
    n 1uchsml "¡Bienvenido,{w=0.1} tonto!{w=0.2} ¡Ponte cómodo!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_love_plus_dull_moment",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, None)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_love_plus_dull_moment:
    n 1fsqsrl "¡Vaya vaya,{w=0.1} si que te tomaste tu tiempo!"
    n 1fbkwrf "¡¿En que estabas pensando,{w=0.1} [player]?!"
    n 1fsqpol "..."
    n 1fsqdvl "..."
    n 1uchbgl "Jejeje.{w=0.2} Nunca tener un momento aburrido conmigo,{w=0.1} ¿puede ser?"
    n 1nchbsl "Ya sabes el trato -{w=0.1} ponte cómodo,{w=0.1} tonto!"
    return

# AFFECTIONATE/ENAMORED greetings

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_good_to_see_you",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_good_to_see_you:
    n 1uchbgl "¡[player]!{w=0.2} ¡Volviste!"
    n 1uchsml "¡Es bueno verte de nuevo!"
    n 1nchsml "Que hoy sea otro día genial,{w=0.1} ¿sí? Jeje."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_couldnt_resist",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_couldnt_resist:
    n 1ksqsml "¡Oye,{w=0.1} tú!{w=0.2} ¿Tan pronto?"
    n 1fsqsml "Sabía que no podrías resistir.{w=0.2} Jejeje."
    n 1uchbgl "¿Qué quieres hacer hoy?"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_just_cant_stay_away",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_just_cant_stay_away:
    n 1usqbgl "Vaya, vaya, vaya.{w=0.2} ¿Qué tenemos aquí?"
    n 1fsqbgl "No puedes alejarte de mí,{w=0.1} ¿verdad?{w=0.2} ¡Jajaja!"
    n 1kchbgl "¡No es que me queje mucho!"
    n 1unmsml "Entonces...{w=0.3} ¿de qué quieres hablar?"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_have_so_much_fun",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_have_so_much_fun:
    n 1uchbgl "¡Pero si es [player],{w=0.1} yay!"
    n 1nchsml "¡Hoy nos divertiremos mucho!{w=0.2} Jeje."
    n 1unmbgl "Entonces,{w=0.1} ¿de qué quieres hablar?"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_affectionate_enamored_everything_is_fine",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_affectionate_enamored_everything_is_fine:
    n 1nwdgsl "¡[player], volviste!"
    n 1fsqpol "He estado esperándote, sabes..."
    n 1uchssl "Pero ahora que estás aquí, ¡todo está bien! Jeje."
    return

# NORMAL/HAPPY greetings

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_whats_up",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_whats_up:
    n 1unmbg "¡Oh!{w=0.2} ¡Hola,{w=0.1} [player]!"
    n 1unmsm "¿Qué tal?"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_glad_to_see_you",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_glad_to_see_you:
    n 1uchsm "¡Hola,{w=0.1} [player]!"
    n 1unmsm "Me alegro de verte."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_spacing_out",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_spacing_out:
    n 1kllpu "..."
    n 1uwdajl "¿Eh?"
    n 1uchbgl "¡O-{w=0.1}oh!{w=0.2} ¡Hola,{w=0.1} [player]!"
    n 1knmss "Perdón,{w=0.1} solo pensaba en algo."
    n 1unmsm "Y...{w=0.3} ¿qué hay de nuevo, viejo?"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_heya",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_heya:
    n 1unmbg "¡Hola hola,{w=0.1} [player]!"
    n 1nnmsm "¡Bienvenido!"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_normal_happy_knew_youd_be_back",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_normal_happy_knew_youd_be_back:
    n 1unmbg "¡Pero si es [player]!{w=0.2} ¡Hola!"
    n 1fcsbgl "S-{w=0.1}sabía que volverías,{w=0.1} es obvio."
    n 1fcssml "¡Tendrías que ser un malvado para no volver! ¡Jajaja!"
    return

# DISTRESSED/UPSET greetings

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_oh_its_you",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_oh_its_you:
    n 1nnmaj "Oh.{w=0.2} Eres tú."
    n 1nnmsl "Hola,{w=0.1} [player]."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_hi",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_hi:
    n 1nplsl "[player].{w=0.2} Hola."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_welcome_back_i_guess",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_welcome_back_i_guess:
    n 1nnmsl "[player].{w=0.2} Bienvenido,{w=0.1} supongo."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_better_be_good",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_better_be_good:
    n 1nsqaj "Hola,{w=0.1} [player]."
    n 1fnmsl "Será mejor que sea algo bueno."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_distressed_upset_oh_you_came_back",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_distressed_upset_oh_you_came_back:
    n 1tsqaj "¿Oh?{w=0.2} ¿Volviste?"
    n 1fsqsr "...Desearía poder alegrarme de eso."
    return

# BROKEN- greetings

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_oh_its_you",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_oh_its_you:
    n 1kplsr "¿...?"
    n 1kcssr "Oh...{w=0.3} eres tú."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_nothing_to_say",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_nothing_to_say:
    n 1kcssr "..."
    n 1kplsr "..."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_why",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_why:
    n 1fplaj "...¿Por qué?"
    n 1fcsup "¿Por qué volviste,{w=0.1} [player]?"
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_enough_on_my_mind",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_enough_on_my_mind:
    $ player_initial = list(player)[0]
    n 1fskem "¿[player_initial]-{w=0.1}[player]...?"
    n 1fcsup "Como si no tuviera suficiente con lo que lidiar..."
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_broken_minus_leave_me_be",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_broken_minus_leave_me_be:
    $ player_initial = list(player)[0]
    n 1fcsfu "...¿Por qué, [player]?{w=0.2} ¿Por qué vuelves?"
    n 1kcsup "Por qué no puedes tan solo dejarme en paz..."
    return

# Admission-locked greetings; used when Natsuki made the player leave due to tiredness, etc.

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_feeling_better_sick",
            unlocked=True,
            category=["Confesión"],
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE),
            additional_properties={
                "admission_type": jn_admissions.TYPE_SICK,
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_feeling_better_sick:
    n 1knmbgl "¡Oh!{w=0.2} ¡[player]!{w=0.2} ¡Oye!"
    menu:
        n "¿Cómo estás?{w=0.2} ¿Mejor?"

        "¡Mucho mejor, gracias por preguntar!":
            n 1ucsbg "¡Bien, bien!{w=0.2} ¡Me alegra escuchar eso!{w=0.2} A nadie le gusta estar enfermo."
            n 1nsqbg "Ahora que te sientes mejor,{w=0.1} ¿por qué no pasar un tiempo de calidad juntos?"
            n 1fsqsm "¡Me debes muchas horas!{w=0.2} Jeje."
            $ persistent.jn_player_admission_type_on_quit = None

        "Un poco mejor.":
            n 1knmpo "...Seré sincera,{w=0.1} no esperaba escuchar eso."
            n 1unmsr "Pero al menos estás 'un poco' mejor,{w=0.1} supongo."
            n 1nchbg "Como sea...{w=0.3} ¡Bienvenido,{w=0.1} [player]!"

            # Add pending apology, reset the admission
            $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_UNHEALTHY)
            $ jn_admissions.last_admission_type = jn_admissions.TYPE_SICK

        "Sigo igual.":
            n 1knmsr "¿Aún sin fuerzas,{w=0.1} [player]?"
            n 1knmsl "No me importa si te quedas por aquí...{w=0.3} pero no te sobreesfuerces,{w=0.1} ¿entendido?"
            n 1kplsl "No quiero que te pongas peor por mi culpa..."

            # Add pending apology, reset the admission
            $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_UNHEALTHY)
            $ jn_admissions.last_admission_type = jn_admissions.TYPE_SICK
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_feeling_better_tired",
            unlocked=True,
            category=["Confesión"],
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE),
            additional_properties={
                "admission_type": jn_admissions.TYPE_TIRED,
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_feeling_better_tired:
    n 1uchbg "¡Ah!{w=0.2} ¡[player]!{w=0.2} ¡Hola!"
    menu:
        n "Espero que hayas dormido bien.{w=0.2} ¿Cómo te sientes?"

        "¡Mucho mejor, gracias por preguntar!":
            n 1nchsm "¡Genial!{w=0.2} Nada como dormir tus 8 horas,{w=0.1} ¿verdad?"
            n 1usqsg "Ahora -{w=0.1} ya que estás despierto y alerta..."
            n 1nchbg "¿Qué mejor que pasar tiempo juntos?{w=0.2} Jeje."
            $ persistent.jn_player_admission_type_on_quit = None

        "Un poco cansado.":
            n 1knmsl "Oh...{w=0.3} bueno,{w=0.1} no es exactamente lo que esperaba escuchar."
            n 1knmaj "Si no estás tan cansado,{w=0.1} ¿tal vez podrías tomar algo que te despierte?"
            n 1uchbg "¡Un vaso de agua o un café debería revivirte en poco tiempo!"

            # Add pending apology, reset the admission
            $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_UNHEALTHY)
            $ jn_admissions.last_admission_type = jn_admissions.TYPE_TIRED

        "Sigo cansado.":
            n 1knmsl "¿Aún con problemas para dormir,{w=0.1} [player]?"
            n 1knmaj "No me importa que estés aquí...{w=0.3} pero no te sobreesfuerces,{w=0.1} ¿entendido?"
            n 1knmbg "No quiero que te quedes dormido sobre el teclado por mi culpa..."

            # Add pending apology, reset the admission
            $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_UNHEALTHY)
            $ jn_admissions.last_admission_type = jn_admissions.TYPE_TIRED
    return

# Absence-related greetings; used when the player leaves suddenly, or has been gone an extended period

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_sudden_leave",
            unlocked=True,
            category=["Disculpa"],
            additional_properties={
                "apology_type": jn_apologies.TYPE_SUDDEN_LEAVE,
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_sudden_leave:
    if Natsuki.isEnamored(higher=True):
        n 1kwmsrl "..."
        n 1kwmsrl "[player]."
        n 1knmsll "Vamos.{w=0.2} Se que eres mejor que esto."
        n 1knmajl "No sé si pasó algo o que,{w=0.1} pero por favor..."
        n 1knmsll "Recuerda despedirte la próxima vez,{w=0.1} ¿sí?"
        n 1knmssl "Lo apreciaría mucho."
        $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_SUDDEN_LEAVE)

    elif Natsuki.isNormal(higher=True):
        n 1kwmsr "..."
        n 1fplsf "¡[player]!{w=0.2} ¿Sabes cuánto me asusta que te desvanezcas así?"
        n 1knmsf "Por favor...{w=0.3} solo recuerda despedirte."
        n 1knmss "No es mucho pedir...{w=0.3} ¿o sí?"
        $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_SUDDEN_LEAVE)

    elif Natsuki.isDistressed(higher=True):
        n 1fsqsf "..."
        n 1fsqaj "Sabes que odio eso,{w=0.1} [player]."
        n 1fsqsl "Detente."
        n 1fsqsf "Gracias."
        $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_SUDDEN_LEAVE)

    else:
        n 1fcsun "..."
        n 1fsqun "Je.{w=0.2} Sí."
        $ chosen_insult = random.choice(jn_globals.DEFAULT_PLAYER_INSULT_NAMES).capitalize()
        n 1fcsup "Bienvenido.{w=0.2} [chosen_insult]."
        $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_SUDDEN_LEAVE)

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_prolonged_leave",
            unlocked=True,
            category=["Disculpa"],
            additional_properties={
                "apology_type": jn_apologies.TYPE_PROLONGED_LEAVE,
            }
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_prolonged_leave:
    $ player_initial = list(player)[0]

    if Natsuki.isEnamored(higher=True):
        n 1uwdwrf "¡[player_initial]-{w=0.1}[player]!"
        n 1fbkwrf "¡¿D-{w=0.1}dónde estabas?!{w=0.2} ¡Me preocupaba que algo te hubiera pasado!"
        n 1kcsunl "..."
        n 1kplunl "Estoy...{w=0.3} feliz...{w=0.3} de que volvieras,{w=0.1} [player]."
        n 1kplsfl "Solo...{w=0.3} avísame la próxima vez,{w=0.1} ¿sí?"
        n 1kcssll "Odio que jueguen con mi corazón de esa manera..."
        $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_PROLONGED_LEAVE)

    elif Natsuki.isNormal(higher=True):
        n 1uwdwr "¡[player_initial]-{w=0.1}[player]!"
        n 1fnman "¡¿Qué demonios?!{w=0.2} ¿Dónde te habías metido?{w=0.2} ¡Estaba super preocupada!"
        n 1fcsupl "¡C-{w=0.1}cómo cualquier amigo se preocuparía,{w=0.1} pero aún así!"
        n 1fcsun "..."
        n 1knmun "...Bienvenido,{w=0.1} [player]."
        n 1knmaj "Solo...{w=0.3} no te vayas tanto tiempo,{w=0.1} ¿sí?{w=0.2} Rayos..."
        $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_PROLONGED_LEAVE)

    elif Natsuki.isDistressed(higher=True):
        n 1fsqaj "¿[player_initial]-{w=0.1}[player]?"
        n 1fsqsl "...Volviste."
        n 1kcssf "No...{w=0.3} sé como sentirme."
        $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_PROLONGED_LEAVE)

    else:
        n 1kcssf "...Je."
        n 1fcssl "Así que volviste."
        n 1fcsup "{i}Geniaaal{/i}."
        $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_PROLONGED_LEAVE)

    return

# Time-of-day based greetings

# Early morning

# Natsuki questions why the player is up so early
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_early_morning_why_are_you_here",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(3, 4)",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_early_morning_why_are_you_here:
    n 1uskgsl "¿E-{w=0.1}eh?{w=0.2} ¡¿[player]?!"
    n 1tnmpul "¿Qué rayos haces aquí tan temprano?"
    n 1knmpo "¿Tuviste una pesadilla o algo?"
    n 1tnmsl "O...{w=0.3} ¿nunca te dormiste?{w=0.2} Eh."
    n 1tnmbg "Bueno,{w=0.1} como sea..."
    n 1kchbgl "¡Buenos días,{w=0.1} supongo!{w=0.2} Jeje."
    return

# Morning

# The Earth says hello!
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_morning_starshine",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(5, 11)",
            affinity_range=(jn_affinity.ENAMORED, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_morning_starshine:
    n 1uchbgl "¡Buenos días,{w=0.1} estrellita!"
    n 1kchbgf "La tierra dice '¡Hola!'"
    n 1fchnvf "..."
    n 1nchdvf "¡Pfffft-!"
    n 1kchbsl "¡Lo siento!{w=0.2} Ha sido tan estúpido...{w=0.3} ¡No puedo quedarme quieta!"
    n 1nchsml "Jeje."
    $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
    n 1kwmsmf "Aunque si eres mi estrellita,{w=0.1} [chosen_endearment]."
    n 1uchsmf "¡Bienvenido!"
    return

# Natsuki doesn't like to be kept waiting around in the morning
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_morning_waiting_for_you",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(5, 11)",
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_morning_waiting_for_you:
    n 1fsqajl "¡Oh! ¡Miren quien decidió aparecer!"
    n 1fwmsll "Sabes que no me gusta esperar...{w=0.3} ¿verdad?"
    n 1fsqsgl "Jeje.{w=0.2} Tienes suerte de que este de buen humor hoy."
    n 1nsqbgl "¡Será mejor que me lo compenses,{w=0.1} [player]~!"
    return

# Natsuki doesn't like a lazy player!
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_morning_lazy",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(10, 11)",
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_morning_lazy:
    n 1nsqbg "¡Oh!{w=0.2} ¡Miren quien por fin decidió levantarse!"
    n 1fsqsg "Rayos,{w=0.1} [player]...{w=0.3} ¡Te juro que a veces eres más vago que Sayori!"
    n 1nchsm "Jeje."
    n 1unmsm "Bueno,{w=0.1} ya estás aquí -{w=0.1} y es todo lo que me importa."
    n 1nnmbg "¡Tengamos una gran mañana,{w=0.1} [player]!"
    n 1tsqaj "O...{w=0.3} ¿lo que queda de ella?"
    n 1nchgn "Jaja."
    return

# Natsuki uses a silly greeting
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_morning_top_of_the_mornin",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(8, 11)",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_morning_top_of_the_mornin:
    n 1unmbg "¡Oh!{w=0.2} ¡Pero si es [player]!"
    n 1uwlsm "Bueno -{w=0.1} ¡buenos días por la mañana!"
    n 1uchsm "..."
    n 1knmpo "¿Qué?{w=0.2} Yo también puedo decir cosas tontas a veces."
    n 1nchgnl "Jeje."
    return

# Afternoon

# Natsuki hopes the player is keeping well
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_afternoon_keeping_well",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(12, 17)",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_afternoon_keeping_well:
    n 1nchbg "¡Oye!{w=0.2} ¡Buenas tardes,{w=0.1} [player]!"
    n 1unmsm "¿Todo bien?"
    return

# Natsuki asks how the player's day is going
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_afternoon_how_are_you",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(12, 17)",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_afternoon_how_are_you:
    n 1nchbg "¡Oh!{w=0.2} ¡Buenas tardes,{w=0.1} [player]!"
    n 1uchsm "¿Cómo has estado?"
    return

# Evening

# Natsuki tells the player they can relax now
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_evening_long_day",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(18, 21)",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_evening_long_day:
    n 1unmbg "¡Aha!{w=0.2} ¡Buenas noches,{w=0.1} [player]!"
    n 1ksgsg "Largo día,{w=0.1} ¿eh?{w=0.2} Bueno,{w=0.1} ¡viniste al lugar correcto!"
    n 1nchbg "¡Solo dile todo a Natsuki!"
    return

# Natsuki teases the player for taking so long
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_evening_took_long_enough",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(18, 21)",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_evening_took_long_enough:
    $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
    n 1fsqsr "¡[player]!{w=0.2} ¡Ahí estás,{w=0.1} [chosen_tease]!"
    n 1fsqpo "Rayos...{w=0.3} ¡tardaste demasiado!"
    n 1fsqsm "Jeje."
    n 1uchbg "¡Solo bromeo!{w=0.2} No te preocupes."
    n 1nchsm "¡Bienvenido!"
    return

# Night

# Natsuki enjoys staying up late too
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_night_up_late",
            unlocked=True,
            conditional="store.jn_get_current_hour() >= 22 or store.jn_get_current_hour() <= 2",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_night_up_late:
    n 1uchbg 1unmbg "¡Oh!{w=0.2} Hola,{w=0.1} [player]."
    n 1unmss "¿Has tenido una larga noche,{w=0.1} eh?"
    n 1uchsm "Bueno...{w=0.3} ¡No me quejo!{w=0.2} ¡Bienvenido!"
    return

# Natsuki is also a night owl
init 5 python:
    registerTopic(
        Topic(
            persistent._greeting_database,
            label="greeting_night_night_owl",
            unlocked=True,
            conditional="store.jn_get_current_hour() >= 22 or store.jn_get_current_hour() <= 2",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_GREETING
    )

label greeting_night_night_owl:
    n 1uchbg "¡Oh,{w=0.1} [player]!{w=0.2} Parece que tú también eres un búho nocturno,{w=0.1} ¿verdad?"
    n 1nnmsm "No es que me moleste eso -{w=0.1} ¡bienvenido!"
    return
