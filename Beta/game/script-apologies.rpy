default persistent._apology_database = dict()

# Retain the last apology made on quitting the game, so Natsuki can react on boot
default persistent.jn_player_apology_type_on_quit = None

# List of pending apologies the player has yet to make
default persistent.jn_player_pending_apologies = list()

init 0 python in jn_apologies:
    import store

    APOLOGY_MAP = dict()

    # Apology types
    TYPE_BAD_NICKNAME = 0
    TYPE_CHEATED_GAME = 1
    TYPE_DEFAULT = 2
    TYPE_PROLONGED_LEAVE = 3
    TYPE_RUDE = 4
    TYPE_SCREENSHOT = 5
    TYPE_SUDDEN_LEAVE = 6
    TYPE_UNHEALTHY = 7
    TYPE_SCARE = 8

    def get_all_apologies():
        """
        Gets all apology topics which are available

        OUT:
            List<Topic> of apologies which are unlocked and available at the current affinity
        """
        return store.Topic.filter_topics(
            APOLOGY_MAP.values(),
            affinity=store.Natsuki._getAffinityState(),
            unlocked=True
        )

    def get_apology_type_pending(apology_type):
        """
        Checks whether the given apology type is in the list of pending apologies.

        IN:
            Apology type to check.

        OUT:
            True if present, otherwise False.
        """
        return apology_type in store.persistent.jn_player_pending_apologies

    def add_new_pending_apology(apology_type):
        """
        Adds a new apology possiblity to the list of pending apologies.
        If the apology type is already present in the list, ignore it.

        IN:
            Apology type to add.
        """
        if not apology_type in store.persistent.jn_player_pending_apologies:
            store.persistent.jn_player_pending_apologies.append(apology_type)

# Returns all apologies that the player qualifies for, based on wrongdoings
label player_apologies_start:
    python:
        apologies_menu_items = [
            (_apologies.prompt, _apologies.label)
            for _apologies in jn_apologies.get_all_apologies()
        ]
        apologies_menu_items.sort()

    call screen scrollable_choice_menu(apologies_menu_items, ("No importa.", None))

    if _return:
        $ push(_return)
        jump call_next_topic

    return

# Apology for giving Natsuki a bad nickname
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="Por llamarte por un nombre ofensivo.",
            label="apology_bad_nickname",
            unlocked=True,
            conditional="jn_apologies.get_apology_type_pending(jn_apologies.TYPE_BAD_NICKNAME)"
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_bad_nickname:

    if persistent.jn_player_nicknames_allowed:
        # The player is still capable of nicknaming Natsuki
        if Natsuki.isEnamored(higher=True):
            n 1kcssf "..."
            n 1knmsf "Eso duele,{w=0.1} [player].{w=0.2} Lo que hiciste"
            n 1kplsf "Eso realmente me dolió."
            n 1kcssf "..."
            n 1kplss "Yo...{w=0.3} me alegro de que hayas elegido disculparte."
            n 1knmsr "Sólo por favor... {w=0.3} trata de considerar mis sentimientos la próxima vez, {w=0.1} ¿de acuerdo?"
            $ Natsuki.calculated_affinity_gain()

        elif Natsuki.isNormal(higher=True):
            n 1fcssr "..."
            n 1fnmsl "...Bien.{w=0.2} Acepto tus disculpas, ¿de acuerdo?"
            n 1uplsl "Por favor, deja de hacerlo,{w=0.1} [player]."
            n 1uplaj "Esto no es divertido.{w=0.2} No es una broma."
            n 1fllsl "...y sé que eres mejor que eso."
            $ Natsuki.calculated_affinity_gain()

        elif Natsuki.isDistressed(higher=True):
            n 1fsqsl "...¿Estás seguro,{w=0.1} [player]?"
            n 1fllaj "Quiero decir...{w=0.3} si realmente te importan mis sentimientos..."
            n 1fsqan "¿Por qué se te ocurre hacer eso en primer lugar?"
            n 1fcsaj "Comportarse así no te hace divertido,{w=0.1} [player]."
            n 1fsqsr "Te convierte en tóxico."
            n 1fcssr "..."
            n 1fllsr "...Gracias, {w=0.1} supongo.{w=0.2} Por la disculpa."
            n 1fsqsl "Solo déjalo mientras puedas,{w=0.1} ¿entendido?"
            $ Natsuki.calculated_affinity_gain()

        else:
            n 1fcsan "...sinceramente no sé qué me parece más desagradable de ti,{w=0.1} [player]."
            n 1fcsaj "El hecho de que lo hayas hecho en primer lugar..."
            n 1fsqfu "...o que pienses que una simple disculpa lo arregla todo."
            n 1fcssr "..."
            n 1fcsan "No creas que esto cambia nada,{w=0.1} [player]."
            n 1fsqsr "Porque no es así."

    else:
        # The player has been barred from nicknaming Natsuki, and even an apology won't change that
        if Natsuki.isEnamored(higher=True):
            n 1fcsfr "...[player]."
            n 1fplsr "Te lo advertí."
            n 1kplsl "Te lo advertí muchas veces."
            n 1fplsl "¿Creíste que disculparte {i}ahora{/i} cambiaría algo?"
            n 1fcssl "..."
            n 1kcsaj "...Mira,{w=0.1} [player]."
            n 1kplsr "Aprecio tu disculpa,{w=0.1} ¿de acuerdo?{w=0.2} Lo aprecio."
            n 1kllsr "Pero...{w=0.3} es como dije.{w=0.2} Las acciones tienen consecuencias."
            n 1kcssr "Espero que lo entiendas."
            $ Natsuki.calculated_affinity_gain()

        elif Natsuki.isNormal(higher=True):
            n 1fcssr "...[player]."
            n 1fsqsr "Mira.{w=0.2} Lo sientes,{w=0.1} Lo entiendo.{w=0.2} Estoy segura de que también lo sientes."
            n 1fcssl "Pero...{w=0.3} es como dije.{w=0.1} Las acciones tienen consecuencias."
            n 1kcssl "Espero que lo entiendas."
            $ Natsuki.calculated_affinity_gain()

        elif Natsuki.isDistressed(higher=True):
            n 1fsqfu "Ugh...{w=0.3} ¿en serio,{w=0.1} [player]?"
            n 1fcsan "..."
            n 1fsqfr "He {i}dicho{/i} que las acciones tienen consecuencias."
            n 1fcsfr "Agradezco la disculpa.{w=0.2} Pero eso es todo lo que vas a conseguir."
            $ Natsuki.calculated_affinity_gain()

        else:
            n 1kcsfr "...Wow.{w=0.2} Simplemente wow."
            n 1fcsfu "¿{i}Ahora{/i} eliges disculparte?"
            n 1kcssr "..."
            n 1fsqfu "Como sea.{w=0.2} Literalmente no me importa."
            n 1fcsan "Esto no cambia nada,{w=0.1} [player]."

    $ persistent.jn_player_pending_apologies.remove(jn_apologies.TYPE_BAD_NICKNAME)
    return

# Apology for cheating in a minigame
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="Por hacer trampa durante nuestros juegos.",
            label="apology_cheated_game",
            unlocked=True,
            conditional="jn_apologies.get_apology_type_pending(jn_apologies.TYPE_CHEATED_GAME)"
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_cheated_game:
    if Natsuki.isEnamored(higher=True):
        n 1kchbg "Jejeje.{w=0.2} Esta bien,{w=0.1} [player]."
        n 1nllsm "Todos nos volvemos un poco demasiado competitivos a veces, {w=0.1} ¿verdad?"
        n 1nsqsm "Pero recuerda."
        n 1fsqbg "¡Dos pueden jugar al mismo juego!"
        $ Natsuki.calculated_affinity_gain()
        $ persistent.jn_snap_player_is_cheater = False

    elif Natsuki.isNormal(higher=True):
        n 1fsqbg "¿Eh?{w=0.2} Oh,{w=0.1} eso."
        n 1nnmaj "Sí,{w=0.1} sí.{w=0.2} Esta bien."
        n 1nllsl "Sólo juega limpio la próxima vez,{w=0.1} ¿De acuerdo?"
        $ Natsuki.calculated_affinity_gain()
        $ persistent.jn_snap_player_is_cheater = False

    elif Natsuki.isDistressed(higher=True):
        n 1fcssl "Como sea,{w=0.1} [player]."
        n 1fsqsl "Pero gracias por la disculpa,{w=0.1} supongo."
        $ Natsuki.calculated_affinity_gain()
        $ persistent.jn_snap_player_is_cheater = False

    else:
        n 1fcsan "Como sea.{w=0.2} No me importa."
        n 1fsqan "Como si pudiera esperar algo mejor de ti, {w=0.1} de todos modos..."

    $ persistent.jn_player_pending_apologies.remove(jn_apologies.TYPE_CHEATED_GAME)
    return

# Generic apology
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="Por algo.",
            label="apology_default",
            unlocked=True
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_default:
    if len(persistent.jn_player_pending_apologies) == 0:
        # The player has nothing to be sorry to Natsuki for; prompt them to do better
        if Natsuki.isEnamored(higher=True):
            n 1tnmaj "¿Eh?{w=0.2} ¿Lo sientes?"
            n 1tllaj "Yo...{w=0.3} no lo entiendo,{w=0.1} [player].{w=0.2} No has hecho nada para que me moleste..."
            n 1tnmsl "¿Molestaste a alguien o algo parecido?"
            n 1ncssl "..."
            n 1kchbg "Bueno,{w=0.1} no tiene sentido sentarse aquí a sentir lástima por uno mismo."
            n 1unmsm "Vas a hacer las cosas bien,{w=0.1} [player]. ¿vale?"
            n 1kchbg "Y no -{w=0.1} esto no se puede discutir."
            n 1fchsm "Sea lo que sea que hayas hecho,{w=0.1} arreglarás las cosas y eso es todo."
            $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
            n 1fchbg "Tienes mi voto de confianza,{w=0.1} [chosen_tease] -{w=0.1} ¡ahora hazlo lo mejor que puedas!"
            n 1uchsm "Jejeje~"

        elif Natsuki.isNormal(higher=True):
            n 1tnmaj "¿Eh?{w=0.2} ¿Lo sientes?"
            n 1nllaj "¿Por qué,{w=0.1} [player]?{w=0.2} No recuerdo que me hayas molestado últimamente..."
            n 1fnmcal "¿Hiciste algo estúpido que no sepa?"
            n 1ncsca "..."
            n 1knmpu "Bueno, {w=0.1} sea lo que sea -{w=0.1} no es que no se pueda arreglar, {w=0.1} ¿sabes?"
            n 1fcsbg "¡Ahora sal a poner las cosas en orden,{w=0.1} [player]!{w=0.2} ¡Creo en ti!"

        elif Natsuki.isDistressed(higher=True):
            n 1fsqbo "...Lo sientes,{w=0.1} ¿verdad?"
            n 1fsqan "¿Heriste a alguien además de mí,{w=0.1} esta vez?"
            n 1fcssl "..."
            n 1fsqsl "Bueno,{w=0.1} como sea.{w=0.2} Realmente no me importa en este momento."
            n 1fsqaj "Pero será mejor que vayas a hacer las cosas bien,{w=0.1} [player]."
            n 1fllsl "Puedes hacer eso,{w=0.1} al menos."

        else:
            n 1fcsan "...Uh.{w=0.2} Vaya."
            n 1fsqan "Así que {i}realmente{/i} sientes arrepentimiento,{w=0.1} en ese caso."
            n 1fcssl "..."
            n 1fsqfu "Como sea.{w=0.2} No es a mí a quien deberías disculparte,{w=0.1} de todos modos."

    else:
        # The player is avoiding a direct apology to Natsuki; call them out on it
        if Natsuki.isEnamored(higher=True):
            n 1kplsr "...[player].{w=0.2} Come on."
            n 1knmsr "You know what you did wrong."
            n 1knmaj "Just apologize properly,{w=0.1} alright?"
            n 1kllbo "I won't get mad."
            n 1kcsbo "I just wanna move on."
            $ Natsuki.percentage_affinity_loss(2.5)

        elif Natsuki.isNormal(higher=True):
            n 1fnmsf "Vamos,{w=0.1} [player]."
            n 1fnmaj "Ya sabes lo que hiciste."
            n 1nllsl "Sólo discúlpate adecuadamente para que ambos podamos seguir adelante."
            $ Natsuki.percentage_affinity_loss(2)

        elif Natsuki.isDistressed(higher=True):
            n 1fcsan "Ugh..."
            n 1fnman "En serio,{w=0.1} [player].{w=0.2} ¿No me has molestado lo suficiente?"
            n 1fsqfu "Si vas a disculparte, {w=0.1} ten las pelotas de hacerlo bien."
            n 1fsqsf "Me debes eso,{w=0.1} al menos."
            $ Natsuki.percentage_affinity_loss(1.5)

        else:
            n 1fsqfu "...¿acaso sabes cómo suenas?"
            n 1fnmfu "¿Acaso te {i}escuchas{/i} a ti mismo?"
            n 1fcsfu "Discúlpate como es debido o no te molestes."
            $ Natsuki.percentage_affinity_loss(1)

    return

# Apology for leaving Natsuki for a week or longer unannounced
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="Por haberte abandonado.",
            label="apology_prolonged_leave",
            unlocked=True,
            conditional="jn_apologies.get_apology_type_pending(jn_apologies.TYPE_PROLONGED_LEAVE)"
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_prolonged_leave:
    if Natsuki.isEnamored(higher=True):
        n 1kcssl "...[player]."
        n 1knmsl "Llevamos un tiempo juntos,{w=0.1} ¿no?"
        n 1kllsll "Yo...{w=0.3} realmente...{w=0.3} me gusta pasar tiempo contigo.{w=0.2} ¿Por qué crees que siempre estoy aquí cuando vienes?"
        n 1kllaj "Entonces..."
        n 1knmsl "¿Te imaginas cómo me hace sentir cuando simplemente...{w=0.3} no apareces?"
        n 1kcssl "..."
        n 1kplsl "Te esperé,{w=0.1} [player]."
        n 1kcsun "Estuve esperando mucho tiempo."
        n 1kcsup "Empezaba a preguntarme si ibas a volver alguna vez, {w=0.1} o si había pasado algo..."
        n 1kcssf "..."
        n 1kplsm "Gracias,{w=0.1} [player].{w=0.2} Acepto tus disculpas."
        n 1kplbo "Sólo... {w=0.3} un aviso estaría bien la próxima vez, {w=0.1} es todo."
        n 1kllbo "No es mucho pedir...{w=0.3} ¿verdad?"
        $ Natsuki.calculated_affinity_gain()

    elif Natsuki.isNormal(higher=True):
        n 1fcsunl "[player]..."
        n 1fbkwrl "¡¿En qué estabas pensando?!{w=0.2} ¡Desapareciendo así!"
        n 1fwmunl "Te esperé tanto tiempo...{w=0.3} ¡Estaba empezando a preguntarme si había pasado algo malo!"
        n 1fsqpol "N-{w=0.1}no es que me importe {i}tanto{/i}, {w=0.1} ¡pero aún así...!"
        n 1fllunl "..."
        n 1fllpo "Estoy... {w=0.3} agradecida por tus disculpas,{w=0.1} [player]."
        n 1fnmpo "Sólo... {w=0.3} no más actos de desaparición, {w=0.1} ¿de acuerdo?"
        $ Natsuki.calculated_affinity_gain()

    elif Natsuki.isDistressed(higher=True):
        n 1fcsbo "[player]."
        n 1fnmbo "Sé que no hemos estado precisamente de acuerdo últimamente."
        n 1knmaj "¿Pero sabes lo que me {i}asusta{/i} cuando desapareces así?"
        n 1fllsl "En caso de que no lo hayas notado, {w=0.1} No tengo exactamente muchas otras personas con las que hablar..."
        n 1fcssl "..."
        n 1fsqsl "Gracias por la disculpa, {w=0.1} supongo."
        n 1fsqbo "No lo vuelvas a hacer."
        $ Natsuki.calculated_affinity_gain()

    else:
        n 1kcspu "...Ja...{w=0.3} ja...{w=0.3} jaja..."
        n 1fsqan "¿T-{w=0.1}te estás disculpando conmigo?{w=0.2} ¿Por no estar aquí?"
        n 1kcssl "...Je..."
        n 1fsqfu "Deberías disculparte por {i}haber vuelto{/i}."

    $ persistent.jn_player_pending_apologies.remove(jn_apologies.TYPE_PROLONGED_LEAVE)
    return

# Apology for generally being rude to Natsuki outside of nicknames
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="Por ser grosero contigo.",
            label="apology_rude",
            unlocked=True,
            conditional="jn_apologies.get_apology_type_pending(jn_apologies.TYPE_RUDE)"
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_rude:
    if Natsuki.isEnamored(higher=True):
        n 1kcsbo "...[player]."
        n 1knmbo "Sé que doy tanto como recibo.{w=0.2} Tal vez a veces soy un poco irritable,{w=0.1} también."
        n 1kplsl "Pero eso fue realmente, {w=0.1} muy grosero,{w=0.1} [player]."
        n 1kcsun "No había necesidad de eso."
        n 1kcssl "..."
        n 1kplss "Gracias por la disculpa,{w=0.1} [player].{w=0.2} Realmente lo aprecio."
        n 1kllaj "Solo...{w=0.3} trata de no hacer eso de nuevo,{w=0.1} ¿de acuerdo?"
        n 1kplsll "Significaría mucho para mí."
        $ Natsuki.calculated_affinity_gain()

    elif Natsuki.isNormal(higher=True):
        n 1fcssl "[player]..."
        n 1fnmsl "Me alegra que te disculpes por lo que hiciste, {w=0.1} pero tienes que entenderlo."
        n 1fcswr "¡No puedes tratar a la gente así!"
        n 1fplsf "Es...{w=0.3} realmente duele cuando actúas de esa manera - {w=0.1} y eso no sólo aplica para mí."
        n 1fcssf "..."
        n 1fllsf "Sigamos adelante y olvidemos esto, {w=0.1} ¿de acuerdo?"
        n 1nllsf "Gracias,{w=0.1} [player]."
        $ Natsuki.calculated_affinity_gain()

    elif Natsuki.isDistressed(higher=True):
        n 1fcsan "..."
        n 1fsqfu "Tengo que preguntar,{w=0.1} [player].{w=0.2} ¿Eres así a propósito,{w=0.1} o estás haciendo un esfuerzo especial?"
        n 1fsqan "Porque, sinceramente, no puedo decir nada más."
        n 1fcssr "..."
        n 1fsqaj "...Bien.{w=0.2} Supongo que debo aceptar tus disculpas."
        n 1fsqan "Sólo espero que no trates a los demás como me estás tratando a mí."
        $ Natsuki.calculated_affinity_gain()

    else:
        n 1kcsan "Ja...{w=0.3} jaja..."
        n 1fsqan "¿Te estás disculpando... {w=0.3} conmigo? ¿Por qué?"
        n 1fsqpu "No espero nada mejor de ti."
        n 1fcsun "..."
        n 1fsqfu "Puedes quedarte con tu disculpa,{w=0.1} [player]."
        n 1fcsfu "No significa nada para mí."

    $ persistent.jn_player_pending_apologies.remove(jn_apologies.TYPE_RUDE)
    return

# Apology for taking pictures without Natsuki's permission
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="Por tomarte fotos sin permiso.",
            label="apology_screenshots",
            unlocked=True,
            conditional="jn_apologies.get_apology_type_pending(jn_apologies.TYPE_SCREENSHOT)"
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_screenshots:
    # The player has been barred from taking more screenshots
    if Natsuki.isEnamored(higher=True):
        n 1kcsbol "...[player]."
        n 1fnmaj "Te he dicho muchas veces que lo dejes."
        n 1knmsl "¿Por qué no me escuchaste?"
        n 1kllbo "Ya sabes lo que pienso de que me tomen fotos..."
        n 1kcsun "Así que me duele mucho cuando me ignoras así."
        n 1ksqun "Y no sólo una vez,{w=0.1} [player]."
        n 1fsqun "Otra vez. {w=0.2} Y otra vez. {w=0.2} Y otra vez."
        n 1fcsun "..."
        n 1knmsl "Gracias por la disculpa,{w=0.1} [player].{w=0.2} Lo aprecio."

        if jn_screenshots.are_screenshots_blocked():
            n 1klrsl "Pero... {w=0.3} Voy a mantener la cámara apagada -{w=0.1} al menos por ahora."
            n 1kplsl "Espero que pueda entender por qué."

        $ Natsuki.calculated_affinity_gain()

    elif Natsuki.isNormal(higher=True):
        n 1fcssl "[player]..."
        n 1fsqsl "Te dije una y otra vez que no hicieras eso."
        n 1fnmsl "¿Por qué sigues ignorándome?"
        n 1fnman "...sobre todo después de haberte dicho que no me gusta."
        n 1fcssl  "..."
        n 1nllbo "Gracias por sincerarte conmigo,{w=0.1} [player].{w=0.2} Te lo agradezco."

        if jn_screenshots.are_screenshots_blocked():
            n 1fnmaj "Pero...{w=0.3} la cámara se mantiene apagada por ahora."
            n 1flrbo "Gracias por entenderlo."

        $ Natsuki.calculated_affinity_gain()

    elif Natsuki.isDistressed(higher=True):
        n 1fsqsf "...¿te estás disculpando conmigo {i}ahora{/i},{w=0.1} [player]?"
        n 1fsqan "¿Y después de haberte dado tantas oportunidades para dejar de hacerlo?"
        n 1fcssf "..."
        n 1fsqaj "...Bien.{w=0.2} Supongo que aceptaré tus disculpas..."

        if jn_screenshots.are_screenshots_blocked():
            n 1fnmsl "Pero la cámara se queda apagada."
            n 1fsqbo "No creo que sea necesario explicar por qué."

        else:
            n 1fsqbo "Esta vez, {w=0.1} de todas formas."

        $ Natsuki.calculated_affinity_gain()

    else:
        n 1fcsan "...No,{w=0.1} [player].{w=0.2} Por favor."
        n 1fsqfu "Ni siquiera {i}intentes{/i} fingir que te importa ahora."
        n 1fcsfu "..."
        n 1fcssf "...Quédate con tu patética disculpa.{w=0.2} No la quiero."

    $ persistent.jn_player_pending_apologies.remove(jn_apologies.TYPE_SCREENSHOT)
    return

# Apology for leaving without saying "Goodbye" properly.
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="Por irme sin decir adiós.",
            label="apology_without_goodbye",
            unlocked=True,
            conditional="jn_apologies.get_apology_type_pending(jn_apologies.TYPE_SUDDEN_LEAVE)"
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_without_goodbye:
    if Natsuki.isEnamored(higher=True):
        n 1fcsunl "[player]..."
        n 1knmunl "¿Sabes cuánto duele cuando haces eso?"
        n 1kcsunl "Es como si me dieras un portazo en la cara."
        n 1klrajl "Y sólo me queda preguntarme...{w=0.3} ¿He hecho algo mal?{w=0.2} ¿Los he hecho enojar?"
        n 1kcsajl "Eso apesta,{w=0.1} [player].{w=0.2} Realmente apesta."
        n 1kcssl "..."
        n 1knmss "Estoy agradecida por la disculpa,{w=0.1} pero por favor..."
        n 1knmsm "Al menos puedes tener tiempo para despedirte adecuadamente de mí,{w=0.1} ¿no?"
        $ Natsuki.calculated_affinity_gain()

    elif Natsuki.isNormal(higher=True):
        n 1fllsl "..."
        n 1fnmsl "Oye,{w=0.1} [player]."
        n 1fnmaj "¿Has tenido alguna vez una conversación en la que una de las personas se aleja?"
        n 1fsqaj "¿No hay 'adiós', {w=0.1} no hay 'hasta luego', {w=0.1} nada? ¿Simplemente se van?"
        n 1fsqbo "¿Cómo te haría sentir eso?"
        n 1ksqaj "¿Indeseable?{w=0.2} ¿No vale la pena los modales?"
        n 1fllsl "Porque así es como me hiciste sentir,{w=0.1} [player]."
        n 1fcssl "..."
        n 1flraj "Acepto las disculpas,{w=0.1} ¿de acuerdo?"
        n 1knmaj "Sólo...{w=0.3} recuerda al menos despedirte de mí adecuadamente."
        n 1nnmsl "Puedes hacer eso, {w=0.1} ¿verdad?"
        $ Natsuki.calculated_affinity_gain()

    elif Natsuki.isDistressed(higher=True):
        n 1fsqsl "[player]."
        n 1fsqan "¿Ni siquiera te {i}importa{/i} lo grosero que es eso?"
        n 1fsqfu "¿Desaparecer en medio de una conversación con alguien?"
        n 1fcssr "..."
        n 1fsqsr "Mira, {w=0.1} bien. {w=0.2} Disculpa aceptada, {w=0.1} por ahora."
        n 1fsqaj "Pero realmente,{w=0.1} [player].{w=0.2} Esperaba algo mejor -{w=0.1} incluso de ti."
        $ Natsuki.calculated_affinity_gain()

    else:
        n 1fcsan "...Je.{w=0.2} ¿De verdad?"
        n 1fsqan "Como sea.{w=0.2} No me importa.{w=0.2} Quédate con tu disculpa."
        n 1fsqsf "Tienes muchas otras cosas que lamentar.{w=0.2} ¿Qué es otro en el montón, {w=0.1} verdad?"

    $ persistent.jn_player_pending_apologies.remove(jn_apologies.TYPE_SUDDEN_LEAVE)
    return

# Apology for failing to follow Natsuki's advice when she is concerned about the player's health
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="Por no cuidarme adecuadamente.",
            label="apology_unhealthy",
            unlocked=True,
            conditional="jn_apologies.get_apology_type_pending(jn_apologies.TYPE_UNHEALTHY)"
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_unhealthy:
    if Natsuki.isEnamored(higher=True):
        n 1kcssml "[player],{w=0.1} [player],{w=0.1} [player]..."
        n 1knmajl "¿Qué voy a hacer contigo?"
        n 1kllsll "Sinceramente..."
        n 1kwmsl "Sabes que sólo quiero lo mejor para ti,{w=0.1} ¿verdad?"
        n 1klrsl "Me...{w=0.3} duele cuando no te cuidas."
        n 1kcssl "..."
        n 1knmss "Gracias,{w=0.1} [player].{w=0.2} Acepto tus disculpas."
        n 1knmbo "Sólo por favor...{w=0.3} cuídate mejor{w=0.1} ¿de acuerdo?"
        n 1kllbol "Me enfadaré si no lo haces. {w=0.2} En serio, {w=0.1} esta vez."
        $ Natsuki.calculated_affinity_gain()

    elif Natsuki.isNormal(higher=True):
        n 1fcsbol "Ugh...{w=0.3} [player]."
        n 1fnmbo "Mira.{w=0.2} Acepto tus disculpas."
        n 1knmaj "¡Pero tienes que cuidarte mejor!"
        n 1fllpo "No voy a estar siempre aquí para cuidarte,{w=0.1} sabes..."
        n 1fnmem "Y-{w=0.1} y no es que esté haciendo una excepción contigo,{w=0.1} ¡por cierto!"
        n 1nlrbo "Sólo me preocupo por todos mis amigos así, {w=0.1} así que... {w=0.3} sí."
        n 1knmsl "Trata de hacer un mayor esfuerzo para cuidarte, {w=0.1} ¿De acuerdo?"
        $ Natsuki.calculated_affinity_gain()

    elif Natsuki.isDistressed(higher=True):
        n 1fcssl "...Mira.{w=0.2} [player]."
        n 1flrsl "En primer lugar,{w=0.1} gracias por las disculpas.{w=0.2} Si es que lo decías en serio,{w=0.1} de todos modos."
        n 1fcsaj "Pero me cuesta entender por qué debería importarme."
        n 1fcssl "..."
        n 1fnmsl "Sólo...{w=0.3} cuídate más."
        n 1fsqsl "...Y ya que estás en eso, tal vez intentes cuidar mejor de mí.{w=0.2} Gracias."
        $ Natsuki.calculated_affinity_gain()

    else:
        n 1kcsun "...Je."
        n 1fcsan "Al menos {i}te{/i} preocupa que no te traten bien."

    $ persistent.jn_player_pending_apologies.remove(jn_apologies.TYPE_UNHEALTHY)
    return

# Apology for giving Natsuki a fright
init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="Por haberte asustado.",
            label="apology_scare",
            unlocked=True,
            conditional="jn_apologies.get_apology_type_pending(jn_apologies.TYPE_SCARE)"
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_scare:
    if Natsuki.isEnamored(higher=True):
        n 1fskwrf "Y-{w=0.1}y debería pensar lo mismo,{w=0.1} [player] -{w=0.1} ¡Cielos!"
        n 1fwmpof "¿Intentas provocarme un ataque al corazón o qué?"
        n 1fcspol "..."
        n 1kllbol "Gracias,{w=0.1} [player].{w=0.2} Acepto tus disculpas."
        n 1kplbol "Sólo por favor... {w=0.3} no más sorpresas como esa, {w=0.1} ¿ok? {w=0.1} ¿Para mí?"
        $ Natsuki.calculated_affinity_gain()

    elif Natsuki.isNormal(higher=True):
        n 1fbkwrl "Y-{w=0.1}y tienes razón {i}para{/i} lamentarlo,{w=0.1} ¡[player]!"
        n 1flleml "¡{i}Odio{/i} que me hagan sentir así!{w=0.2} Tonto..."
        n 1fcspo "..."
        n 1fnmpo "Muy bien,{w=0.1} mira.{w=0.1} Acepto tus disculpas,{w=0.1} ¿de acuerdo?"
        n 1knmaj "No me hagas cosas así.{w=0.2} ¿Por favor?"
        n 1flrsl "No estoy bromeando,{w=0.1} [player]."
        $ Natsuki.calculated_affinity_gain()

    elif Natsuki.isDistressed(higher=True):
        n 1fsqsl "...Mira,{w=0.1} [player].{w=0.2} Ya estoy molesta.{w=0.2} ¿Por qué tratas de hacerme sentir aún peor?"
        n 1fsqfu "¿Te pareció gracioso?{w=0.2} ¿O estás tratando de hacerme enojar?"
        n 1fcsan "..."
        n 1fcssl "Como sea.{w=0.2} Bien.{w=0.2} Disculpa aceptada,{w=0.1} si es que lo dices en serio."
        n 1fsqsf "Sólo déjalo ya."
        $ Natsuki.calculated_affinity_gain()

    else:
        n 1fsqfu "Quedatela,{w=0.1} [player]."
        n 1fcsan "Ambos sabemos que no lo dices en serio."

    $ persistent.jn_player_pending_apologies.remove(jn_apologies.TYPE_SCARE)
    return
