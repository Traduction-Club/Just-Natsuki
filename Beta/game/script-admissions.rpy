default persistent._admission_database = dict()

# Retain the last admission made on quitting the game, so Natsuki can react on boot
default persistent.jn_player_admission_type_on_quit = None

init 0 python in jn_admissions:
    import random
    import store

    ADMISSION_MAP = dict()

    # Admission types
    TYPE_ANGRY = 0
    TYPE_ANXIOUS = 1
    TYPE_ASHAMED = 2
    TYPE_BORED = 3
    TYPE_CONFIDENT = 4
    TYPE_EXCITED = 5
    TYPE_HAPPY = 6
    TYPE_HUNGRY = 7
    TYPE_INSECURE = 8
    TYPE_PROUD = 9
    TYPE_SAD = 10
    TYPE_SICK = 11
    TYPE_TIRED = 12

    # The last admission the player gave to Natsuki
    last_admission_type = None

    def get_all_admissions():
        """
        Gets all admission topics which are available

        OUT:
            List<Topic> of admissions which are unlocked and available at the current affinity
        """
        return store.Topic.filter_topics(
            ADMISSION_MAP.values(),
            affinity=store.Natsuki._getAffinityState(),
            unlocked=True
        )

label player_admissions_start:
    python:
        admission_menu_items = [
            (_admission.prompt, _admission.label)
            for _admission in jn_admissions.get_all_admissions()
        ]
        admission_menu_items.sort()

    call screen scrollable_choice_menu(admission_menu_items, ("No importa.", None))

    if _return:
        $ push(_return)
        jump call_next_topic

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Enfadado",
            label="admission_angry",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_angry:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_ANGRY:
        n 1uwdaj "[player]...{w=0.3} ¿aún estás enfadado?"
        n 1tnmbo "¿Has salido a dar una vuelta{w=0.1} como te sugerí?"
        n 1tllbo "..."
        n 1klrsl "Desearía saber que más hacer por ti..."
        n 1knmss "Simplemente...{w=0.3} intenta relajarte un poquito{w=0.1} e intenta pensar con cabeza fría,{w=0.1} ¿vale?"
        n 1kllca "Yo no quiero que estes enfadado y te acabes haciendo daño, {w=0.1} o algo de lo que te puedas arrepentir."
        n 1knmbo "¿Podrías prometerme que eso no pasará,{w=0.2} [player]?"

        if Natsuki.isEnamored(higher=True):
            n 1kplbol "Es realmente desalentador escuchar que estás así,{w=0.1} ¿sabes?..."
            n 1knmbol "Así que, por favor, [player]. ¿Puedes intentar calmarte?{w=0.1} -{w=0.1} ¿aunque sea por mí?"

    else:
        n 1tnmaj "¿Eh?{w=0.2} ¿Estás enfadado?"
        n 1tnmbo "[player]...{w=0.3} ¿qué ha hecho que te encuentres así? {w=0.2} ¡Eso no es bueno,{w=0.1} [player]!"
        n 1kllem "Se que el hecho de que yo lo diga es algo irónico,{w=0.1} pero vamos a intentar calmarnos, ¿de acuerdo?"
        n 1ncssf "Estar enfadado no va a arreglar nada,{w=0.1} así que centrémonos."
        n 1ulraj "Personalmente si las cosas me superan{w=0.1} me gusta ir a dar una vuelta.{w=0.2} ¡Es increíble lo que un poco de aire fresco puede cambiarte el animo!"
        n 1knmsl "¿Por que no sales un rato también?{w=0.2} Hazlo por mí."
        n 1nnmbg "Te sentirás algo mejor. {w=0.2} ¡Te lo prometo!"

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_ANGRY
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Tenso",
            label="admission_anxious",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_anxious:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_ANXIOUS:
        n 1knmsl "¿Todavía te sientes algo tenso,{w=0.1} [player]?"
        n 1kllsl "..."
        n 1kllaj "Desearía poder ayudarte un poco mas..."
        n 1knmaj "¿Y si pruebas a buscar algo con lo que distraerte y no pensar en lo que sea que te inquieta?"
        n 1unmss "Seguro que tienes alguna serie que no te has terminado,{w=0.1} o alguna afición o algo."
        n 1klran "Nnnn..{w=0.3} que más..."
        n 1unmgs "¡Oh!{w=0.2} Intenta no beber mucha Coca-Cola,{w=0.1} café o bebidas así,{w=0.1} [player]."
        n 1knmsl "Créeme la cafeína es lo peor que podrías tomar ahora mismo."
        n 1klrss "¡La música también alivia mucho! {w=0.2} Es algo relajante, supongo {w=0.1}-{w=0.1} ¿quizás deberías usarla para meditar?"
        n 1knmss "¿Por qué no pruebas a hacer eso,{w=0.1} [player]?"
        n 1kwmsm "¡Te prometo que volverás a sentir como siempre dentro de poco!"

    else:
        n 1tplsf "¿Estás tenso,{w=0.1} [player]?"
        n 1tlrsl "..."
        n 1klraj "Ojalá supiera que decir para aliviarte un poco."
        n 1nnmbo "Pero si puedo decirte una cosa,{w=0.1} [player]."
        n 1knmaj "Todo va a estar bien.{w=0.2} Todo va a ir por el buen camino,{w=0.1} con el tiempo."
        n 1knmbo "Lo prometo."
        n 1klrbo "Hacer pucheros por algo no te va a ayudar en nada,{w=0.1} [player]."
        n 1nllssl "Y sin nada más que decir,{w=0.1} aquí estoy para escucharte."
        n 1knmbo "Así que...{w=0.3} Por que no pruebas a dejar que tu mente descanse,{w=0.1} ¿sí?"
        n 1knmaj "Se que no va a ser fácil...{w=0.3} pero inténtalo,{w=0.1} ¿quieres?"

        if Natsuki.isAffectionate(higher=True):
            n 1kwmsm "Siempre estaré aquí para ti."

        if Natsuki.isLove():
            $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
            n 1kchsml "Te amo, [chosen_endearment]."

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_ANXIOUS
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Avergonzado",
            label="admission_ashamed",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_ashamed:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_ASHAMED:
        n 1knmsl "[player]...{w=0.3} ¿Todavía te avergüenzas de ti mismo?"
        n 1fnmsl "Bueno,{w=0.1} ¡yo no voy a abandonarte {i}tan{/i} fácilmente,{w=0.1} ¿sabes?!"
        n 1fnmss "Just keep trying your best to put things right,{w=0.1} okay?"
        n 1unmbg "¡Puedes con ello!{w=0.2} ¡Se que puedes!"

    else:
        n 1unmbo "¿Eh?{w=0.2} ¿Qué?"
        n 1tnmbo "Que te sientes...{w=0.3} ¿avergonzado?{w=0.2} ¿De ti mismo?"
        n 1kllbo "...¿Por qué,{w=0.1} [player]?{w=0.2} ¿Has hecho algo malo?"
        n 1ncsaj "Bueno...{w=0.3} Sea lo que sea que hayas hecho,{w=0.1} ¡seguro que no es para tanto!"
        n 1fcsbg "Pero lo más importante,{w=0.1} vas a esforzarte para arreglar todo.{w=0.2} ¡Se que lo harás!"
        n 1fnmaj "Así que...{w=0.3} no me decepciones,{w=0.2} ¿vale?"
        n 1fnmbo "Y tampoco vayas a decepcionarte a ti mismo,{w=0.1} ¿entendido?"
        menu:
            "¡Tienes razón!":
                n 1fchbg "¡Exacto!"
                n 1fnmsm "¡Esa es la actitud que yo quería ver!"

            "...":
                n 1fsqpo "..."
                n 1fsqaj "Creo que no me has entendido,{w=0.1} [player]."
                n 1fcsss "Mira,{w=0.1} repite conmigo:{w=0.2} '¡No voy a ser una decepción para mí mismo!'"
                menu:
                    "¡No voy a ser una decepción para mí mismo!":
                        n 1uchgn "¿Ves?{w=0.2} ¡Sabía que podías entenderlo!{w=0.2} Jajaja."

        n 1fchbs "¡Ve a por ello{w=0.1} fiera!"

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_ASHAMED
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Aburrido",
            label="admission_bored",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_bored:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_BORED:
        n 1tnmsm "¿Aun buscas algo con lo que entretenerte,{w=0.1} [player]?"
        n 1nllpo "¿Has intentado hacer lo que te dije?"
        n 1flrpu "Hmm..."
        n 1fnmbg "Bueno,{w=0.1} ¡prueba a llamar a alguien!{w=0.2} Seguro que tienes a algún amigo o familiar al que puedes ir a ver,{w=0.1} ¿cierto?"
        n 1nllbg "O...{w=0.3} Podrías intentar leer un rato,{w=0.1} ¿o tal vez probar algo nuevo?"
        n 1fsqsm "Supongo que lo que intento decir es..."
        n 1fsqbg "No es que sea porque haya poca cosa que hacer,{w=0.1} [player]."
        n 1fchgn "¡Tan solo tienes que rebuscar un poco!"

        if Natsuki.isEnamored(higher=True):
            n 1uchbg "Venga,{w=0.1} ¡vete!{w=0.2} Y que luego no se te olvido contármelo todo,{w=0.1} ¿'tá bien?"

        else:
            n 1usqbg "¿Y bien?{w=0.3} ¿A que estas esperando?"
            n 1nchgn "¡Dalo todo,{w=0.1} [player]!"

    # Unlock Snap if not already unlocked
    elif not persistent.jn_snap_unlocked:
        n 1unmaj "Te aburres,{w=0.1} huh?"
        n 1nlrpo "De hecho,{w=0.1} ahora que lo mencionas...{w=0.3} no es que haya {i}precisamente{/i} mucho por aquí."

        if Natsuki.isEnamored(higher=True):
            n 1fllssl "A parte de mí,{w=0.1} obviamente.{w=0.2} Jejeje."

        n 1flrpo "Hmm...{w=0.3} tiene que haber algo más..."
        n 1fcspo "¡Piensa,{w=0.1} Natsuki!{w=0.2} Piensa..."
        n 1fllpu "..."
        n 1fsgbg "¡Aja!{w=0.2} ¡Creo que he encontrado algo!{w=0.2} Déjame hacer un par de comprobaciones rápidas..."

        play audio drawer
        with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

        n 1fchgn "¡Sí!{w=0.2} ¡Aquí seguía!"
        n 1fsgsg "Apuesto a que no sabias que tenia una baraja de cartas,{w=0.1} ¿no es así?"
        n 1nchgn "¡Por fin los cajones del escritorio {i}son{/i} útiles{w=0.1} para algo!"
        n 1nnmsm "Siempre guardo aquí una baraja para los días lluviosos."
        n 1kllsll "...Ehmm."
        n 1nnmsl "Oye...{w=0.3} ¿[player]?{w=0.2} No me juzgues,{w=0.1} pero..."
        n 1nlrun "Yo...{w=0.3} nunca me llegué a aprender las normas de ningún juego de cartas típico o algo así."
        n 1ullaj "Así que...{w=0.3} Juguemos Snap."
        n 1fllssl "...Hasta que me aprenda las reglas de otro,{w=0.1} al menos."
        $ persistent.jn_snap_unlocked = True
        n 1nnmss "Entonces..."
        n 1uchgn "¿Qué te parece,{w=0.1} [player]?{w=0.2} ¿Echamos una partidita o dos?"
        menu:
            n "Tampoco es que tengas mucho más que hacer,{w=0.1} ¿cierto?"

            "Claro,{w=0.1} ¿por qué no?":
                jump snap_intro

            "Ahora mismo no.":
                n 1fllpo "Oww...{w=0.3} ¡ya había sacado las cartas y todo!"
                n 1unmpo "Bueno...{w=0.3} Da igual."
                n 1nnmsm "Avísame en cuanto se te apetezca echar una partida."

                play audio drawer
                with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    else:
        n 1tnmaj "¿Eh?{w=0.2} ¿Te aburres?"
        n 1fnmaj "¿Qué tratas de decir con eso,{w=0.1} [player]?"
        n 1fsqpo "¿No soy lo suficientemente divertida para ti?"
        n 1fbkwr "¡¿Ya no es divertido pasar el rato conmigo?!"
        n 1flrpo "..."
        n 1fsqsm "..."
        n 1uchgn "¡Relájate! {w=0.2} Relaja,{w=0.1} [player], ¡dios!"
        n 1ullaj "Bueno,{w=0.1} si te aburres..."
        $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
        n 1uchbs "Entonces levanta tu culo de la silla y vete a hacer algo,{w=0.1} [chosen_tease]!"
        n 1tlrbg "Diablos,{w=0.1} [player]...{w=0.3} ¡hay un hay todo un vasto mundo esperándote ahí fuera!"
        n 1tsqbg "Incluso si con eso no estas conforme,{w=0.1} ¡tienes uno aun mas grande al alcance de tu mano!"
        n 1fsqss "O podrías,{w=0.1} ya sabes."

        if Natsuki.isEnamored(higher=True):
            n 1kwmsgl "¿Pasar más tiempo con una servidora?"
            n 1knmpol "No soy aburrida…{w=0.3} ¿cierto?"

        else:
            n 1fchbg "¡Apreciar el hecho de que puedes pasar más tiempo con una servidora!"
            n 1flrpol "N-{w=0.1}no es como si quisiera que lo hagas,{w=0.1} o algo así,{w=0.1} claro.{w=0.2} Jajaja..."

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_BORED
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Confiado",
            label="admission_confident",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_confident:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_CONFIDENT:
        n 1fsgsm "Sigues lleno de confianza,{w=0.1} ¿Ya veo?"
        n 1nchbg "Bueno,{w=0.1} ¡me alegra de oírlo!"

        if Natsuki.isEnamored(higher=True):
            n 1kwlsml "Tienes mucha confianza en ti mismo,{w=0.1} [player]."
            n 1fchsml "¡Será mejor que lo recuerdes!"

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_INSECURE:
        n 1fchbg "¿En serio?{w=0.2} ¡Esto es impresionante,{w=0.1} [player]!"
        n 1kllss "Esperaba que salieras de esos sentimientos más pronto que tarde."
        n 1klrpo "No me gusta cuando hablas así,,{w=0.1} you know..."

        if Natsuki.isAffectionate():
            n 1fcspol "N-{w=0.1}no es que me {i}importe{/i} mucho, ¡p-{w=0.1}por supuesto!"
            n 1fllsll "Pero...{w=0.3} Me alegra saber que estás bien ahora,{w=0.1} [player]. Eso es lo que importa."

        elif Natsuki.isEnamored(higher=True):
            n 1kllsll "Me alegra mucho saber que estás mejor ahora,{w=0.1} [player]."

        if Natsuki.isLove():
            $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
            n 1knmssf "Te amo, [chosen_endearment].{w=0.2} Por favor, no lo olvides,{w=0.1} ¿de acuerdo?"
            n 1klrpof "Me enfadaré si lo haces.{w=0.2} Jajaja..."

    else:
        n 1nchgn "¡Jajaja!{w=0.2} ¡Me alegra de oírlo{w=0.1} [player]!"
        n 1unmaj "Tener confianza en ti mismo y en tus habilidades puede ser realmente difícil a veces."
        n 1ullbo "Especialmente si te equivocas, o si no te sientes bien."
        n 1fchbg "Pero si te sientes así contigo mismo,{w=0.1} ¡no te lo voy a quitar!"

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_CONFIDENT
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Emocionado",
            label="admission_excited",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_excited:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_EXCITED:
        n 1fnmsm "Seguimos con el ánimo por las nubes,{w=0.1} ¿verdad [player]?"
        n 1fsqsm "Apuesto a que no puedes esperar,{w=0.1} ¿eh?{w=0.2} Jejeje."

    else:
        n 1fsptr "¿Oh?{w=0.2} ¿Ha pasado algo?{w=0.2} ¿Va a {i}pasar{/i} algo?"
        n 1fchbg "Sea lo que sea,{w=0.1} ¡es bueno saber que te hace ilusión!"
        n 1unmsm "Siempre es genial tener algo con lo que emocionarse,{w=0.1} ¿verdad?"

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_EXCITED
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Feliz",
            label="admission_happy",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_happy:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_HAPPY:
        n 1ksqsg "Guau...{w=0.3} Todo es sol y arcoíris para ti hoy,{w=0.1} ¿no es así?"
        n 1fchbg "¡Jajaja!"
        n 1fchbg "¡Bien por ti,{w=0.1} [player]!"

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_ANGRY or jn_admissions.last_admission_type == jn_admissions.TYPE_SAD:
        n 1kwmss "¿Te sientes mejor ahora,{w=0.1} [player]?"
        n 1kllbg "Eso es...{w=0.3} un alivio,{w=0.1} ajaja..."

        if Natsuki.isAffectionate(higher=True):
            n 1kllunl "..."
            n 1klrbgl "A-{w=0.1}así que...{w=0.3} ¿dónde estábamos?"

        else:
            n 1fllunl "..."
            n 1fcswrl "Dios...{w=0.3} si estás bien,{w=0.1} ¡volvamos a ello ya!"
            n 1klrpol "Tonto..."

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_HUNGRY:
        n 1fsqbg "¿Te sientes mejor,{w=0.1} [player]?{w=0.2} ¡No me sorprende!"
        n 1fchbg "No eres tú mismo cuando tienes hambre.{w=0.2} Jejeje."
        n 1kllsl "Créeme...{w=0.3} Lo se."

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_SICK:
        n 1nnmsm "¿Te sientes mejor,{w=0.1} [player]?{w=0.2} Me alegra oírlo."
        n 1nchbg "Nada te hace apreciar más la sensación de normalidad que estar enfermo,{w=0.1} ¿verdad?"

    else:
        n 1usqbg "¿Oh?{w=0.1} ¡Alguien está de buen humor hoy!"
        n 1fchbg "¡Eso es bueno,{w=0.1} [player]!"

        if Natsuki.isAffectionate(higher=True):
            n 1uchsm "Si tú eres feliz,{w=0.1} yo también."

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_HAPPY
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Hambriento",
            label="admission_hungry",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_hungry:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_HUNGRY:
        n 1tnmpu "¿Que?{w=0.1} ¿Todavía tienes hambre?"
        n 1fnmpo "¿O es que no has entendido nada cuando te lo dije antes?"
        n 1fchgn "Bueno...{w=0.3} de cualquier manera,{w=0.1} ¡mueve el culo y ve a buscar algo entonces!"
        n 1fllpol "Dios,{w=0.1} [player]...{w=0.3} ¡No soy tu niñera!"

        if Natsuki.isEnamored(higher=True):
            n 1fsqsml "P-{w=0.1}por mucho que probablemente desees que lo sea,{w=0.1} ¿verdad?{w=0.2} ¡Jajaja!"
            n 1uchbs "¡Ahora vete ya!{w=0.2} ¡Bon appetit,{w=0.1} [player]!"

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_SAD:
        n 1knmsl "[player]...{w=0.3} me dijiste que estabas triste antes."
        n 1klrsl "No me importa si tienes hambre,{w=0.1} pero trata de no comer cómodamente,{w=0.1} ¿de acuerdo?"
        n 1knmpu "Puede que te sientas un poco mejor...{w=0.3} pero eso no arreglará lo que te entristeció."
        n 1knmsm "Intenta disfrutar de tu comida,{w=0.1} ¿de acuerdo?"

        if Natsuki.isAffectionate(higher=True):
            n 1kwmsml "Estoy aquí para ti si me necesitas,{w=0.1} [player]."

    else:
        n 1unmpu "¿Eh?{w=0.1} ¿Tienes hambre?"
        $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
        n 1kchbg "Entonces, ¿para qué me lo cuentas?{w=0.2} ¡Ve a comer algo,{w=0.1} [chosen_tease]!"
        n 1fcspo "Sinceramente...{w=0.3} ¿Qué voy a hacer contigo,{w=0.1} [player]?"
        n 1fchbg "¡Ahora vete a hacer algo ya!{w=0.2} ¡Pero no te llenes de basura!"

        if Natsuki.isEnamored(higher=True):
            n 1fsqbg "Quiero que estés en forma para cuando salgamos,{w=0.1} ¿ok?"
            n 1uchgn "vamos a tener mucho que hacer juntos,{w=0.1} ¡después de todo!"

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_HUNGRY
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Inseguro",
            label="admission_insecure",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_insecure:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_INSECURE:
        n 1knmsl "¿Todavía te sientes inseguro de ti mismo,{w=0.1} [player]?"
        n 1kllsl "Tú...{w=0.3} recuerdas lo que dije,{w=0.1} ¿verdad?"
        n 1ncssl "Cada uno tiene su propio ritmo.{w=0.2} No me importa cuál sea el tuyo.{w=0.2} Lo haremos juntos."
        n 1fchgn "...Guau{w=0.1}, eso en serio sonó súper cursi."
        n 1kllnv "Pero en serio,{w=0.1} [player]...{w=0.3} intenta no preocuparte,{w=0.1} ¿ok?"
        n 1fchbgl "La gran Natsuki te cubre la espalda,{w=0.1} ¡después de todo!"

    else:
        n 1knmsl "¿Eh?{w=0.2} ¿Te sientes inseguro?{w=0.2} ¿De dónde viene eso,{w=0.1} [player]?"
        n 1kllsl "..."
        n 1knmpu "Yo...{w=0.3} realmente no puedo decir algo sobre lo que te hizo sentir así..."
        n 1fnmpu "Pero será mejor que escuches,{w=0.1} y que escuches bien,{w=0.1} [player]."
        n 1fcspu "No me importa si no le gustas a la gente.{w=0.2} A mí me gustas."
        n 1fcsbo "No me importa que la gente piense que no tienes talento.{w=0.2} Sé que los tienes."
        n 1fnmbo "No me importa que la gente piense que te estás quedando atrás.{w=0.2} Sé que te pondrás al día."
        n 1kllsl "Sólo...{w=0.3} date tiempo y espacio,{w=0.1} [player]."
        n 1kwmsl "Estos pensamientos que tienes...{w=0.3} pueden llevarte a lugares realmente malos.{w=0.2} Confía en mí."
        n 1fwmsl "No voy a dejar que eso ocurra sin luchar,{w=0.1} -{w=0.1} pero tú también tienes que luchar,{w=0.1} [player].{w=0.2} ¿Entendido?"
        menu:
            "Ok.":
                n 1fnmsl "...Bien.{w=0.2} O tendrás que lidiar conmigo también."
                n 1kllsm "..."
                if Natsuki.isAffectionate(lower=True):
                    n 1flrajl "¿Mensaje recibido?{w=0.2} ¡E{w=0.1}-entonces volvamos a ello ya!"
                    n 1flrpol "Dios..."

                else:
                    n 1kwmpul "...Sabes que quise decir cada palabra que dije{w=0.1} ¿verdad?"
                    n 1kcssll "Así que por favor...{w=0.3} no te rindas.{w=0.2} Ambos necesitamos que ganes,{w=0.1} [player]."

                    if Natsuki.isLove():
                        $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
                        n 1kwmsmf "Realmente te amo, [chosen_endearment]."
                        n 1kchbgf "Sabes que siempre te cubriré la espalda,{w=0.1} tonto..."

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_INSECURE
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Orgulloso",
            label="admission_proud",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_proud:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_PROUD:
        n 1fsqbg "¿En serio,{w=0.1} [player]?{w=0.1} Solo quieres presumir,{w=0.1} ¿eh?"
        n 1tsqbg "{i}Sabes{/i} lo que se dice sobre el orgullo,{w=0.1} ¿cierto?"
        n 1fsqsm "..."
        n 1kchlg "¡Solo estoy de broma,{w=0.1} [player]!{w=0.2} ¡Dios!"
        n 1kchgn "¡Deberías haber visto tu cara!"
        n 1nnmsm "Bien,{w=0.1} ¡es bueno ver que te sientes tan bien contigo mismo!"

    else:
        n 1tsgbg "Oh?{w=0.2} You're feeling proud,{w=0.1} huh?"
        n 1fsqsm "Debes estar muy satisfecho contigo mismo para presumir de ello."
        n 1fchbg "Bueno...{w=0.3} sea por lo que haya sido -{w=0.1} ¡buen trabajo,{w=0.1} [player]!"

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_PROUD
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Triste",
            label="admission_sad",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_sad:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_SAD:
        n 1knmsl "Oh...{w=0.3} Realmente siento escuchar que sigas así,{w=0.1} [player]."
        n 1kllsl "Yo...{w=0.3} no estoy segura de estar en la posición adecuada para preguntar esto,{w=0.1} pero..."
        n 1knmpu "¿Tienes a alguien más con quien hablar de ello?{w=0.2} ¿Amigos{w=0.1} o familia?"
        menu:
            "Si tengo.":
                n 1kllss "Entonces deberías hablarles de como te sientes."
                n 1kchbg "¡Las penas compartidas son menos penas,{w=0.1} como se suele decir!"
                n 1knmsl "Pero en serio,{w=0.1} [player].{w=0.2} No tengas miedo de preguntar por ayuda,{w=0.1} ¿vale?"
                n 1klrsl "Todo el mundo necesita ayuda algunas veces."

            "No tengo.":
                n 1ncssf "No es...{w=0.3} lo que esperaba escuchar,{w=0.1} la verdad."
                n 1kllsr "Siento escuchar eso,{w=0.1} [player].{w=0.2} De verdad."
                n 1nnmpu "Pero recuerda esto."
                n 1knmsr "Siempre tendrás todo mi apoyo,{w=0.1} ¿vale?"
                n 1klrpol "S-si es que puedo ser de ayuda,{w=0.1} quiero decir."

            "Ellos ya lo saben.":
                n 1kcspu "¡Bien! Eso es bueno..."
                n 1knmpo "Solo espero que ellos te estén apoyando,{w=0.1} [player].{w=0.2} Al menos eso te lo mereces."

        if Natsuki.isLove():
            $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
            n 1kchnvf "Te amo,{w=0.1} [chosen_endearment]."

        n 1kllpu "¡Espero que empieces a sentirte mejor pronto!"

    else:
        n 1knmpo "Oh...{w=0.3} Es una pena escuchar eso,{w=0.1} [player]."
        n 1knmpu "¿Te ha pasado algo?{w=0.2} Puedes contármelo,{w=0.1} [player].{w=0.2} no te voy a juzgar."
        n 1ncssr "..."
        n 1nwmpu "Está...{w=0.3} bien,{w=0.1} [player].{w=0.2} Todo va a salir bien."

        if Natsuki.isEnamored(higher=True):
            n 1knmpu "Ahora,{w=0.1} respira hondo y relájate,{w=0.1} ¿está bien?"
            n 1uchsm "Eso es,{w=0.1} [player].{w=0.2} Sigue así."

        n 1kllpu "Pasará lo que haya pasado,{w=0.1} estoy seguro de que todo se resolverá."
        n 1ucssl "Lo que importa es que estés bien,{w=0.1} [player].{w=0.2} Así que deberías enfocarte en resolver eso, ¿está bien?"
        n 1kwmsm "Podemos trabajar en eso aquí,{w=0.1} ¿sabes?"

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_SAD
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Enfermo",
            label="admission_sick",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_sick:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_SICK:
        n 1knmsl "[player]...{w=0.3} ¿todavía te sientes enfermo?"
        n 1knmbo "¿Desde hace cuánto te sientes así?"
        menu:
            "Un par de horas.":
                n 1kllsr "Eso no es...{w=0.3} algo bueno que escuchar,{w=0.1} [player]."
                n 1tnmsr "Tal vez deberías irte a descansar pronto{w=0.1} -{w=0.1} con suerte te sentirás mejor."

                if Natsuki.isEnamored(higher=True):
                    n 1knmsl "Hazme saber si te sigues sintiendo así,{w=0.1} ¿vale?"

            "Un par de días.":
                n 1fcssl "[player]."
                n 1fnmca "Tienes que asegurarte de visitar al doctor pronto."
                n 1knmaj "Especialmente si te empieza a doler algo,{w=0.1} o si te sientes más enfermo,{w=0.1} o algo así..."
                n 1knmsl "Inténtalo y descansa mucho,{w=0.1} ¿vale?"

            "Una semana o así.":
                n 1fnmsl "[player]..."
                n 1knmsl "¿Has ido a ver al doctor ya?"

                menu:
                    "Si, lo he hecho.":
                        n 1kllbo "Bueno...{w=0.3} Está bien."
                        n 1knmbo "Yo...{w=0.3} realmente desearía poder ayudarte,{w=0.1} [player]."
                        n 1knmpu "Asegúrate de descansar mucho,{w=0.1} ¿vale?"

                    "No, no lo he hecho.":
                        n 1fnmpu "[player]...{w=0.3} eso no es bueno."
                        n 1knmpo "Confío en que conozcas tus limites...{w=0.3} pero por favor,{w=0.1} cuídate bien a ti mismo."
                        n 1klrpol "Tu salud...{w=0.3} me importa, ¿sabes?"

                        # Add pending apology
                        $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_UNHEALTHY)

            "Mas de una semana.":
                n 1knmpo "..."
                n 1kllpo "Yo...{w=0.3} ya no se que más decirte,{w=0.1} [player]."
                n 1knmpu "Espero que te mejores pronto."
                n 1knmsl "Tómatelo con calma,{w=0.1} ¿está bien?"

                if Natsuki.isAffectionate():
                    n 1kllcal "Odio verte tan mal..."

                elif Natsuki.isEnamored(higher=True):
                    n 1kllsfl "De verdad, me duele verte tan mal..."

                if Natsuki.isLove():
                    n 1kcssff "Te amo,{w=0.1} [player].{w=0.2} Por favor, recupérate pronto."

                # Add pending apology
                $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_UNHEALTHY)


    elif jn_admissions.last_admission_type == jn_admissions.TYPE_HUNGRY:
        n 1ulrsf "Sabes,{w=0.1} puede que te sientas mal por no haber comido en un tiempo,{w=0.1} [player]."
        n 1nnmsf "¿Has comido algo hoy?{w=0.2} ¿Algo con sustancia?"
        menu:
            "Si, he comido.":
                n 1tllsl "Eh...{w=0.3} ¿entonces puede ser que lo que hayas comido te haya sentido mal?"
                n 1tnmsl "Vete a descansar si lo necesitas,{w=0.1} [player].{w=0.2} ¿Está bien?"

            "No, no lo he hecho.":
                n 1fskem "¡E-entonces deberías comer algo ahora mismo,{w=0.1} [player]!"
                n 1fllpo "No tiene que ser una gran comida lujosa ni nada,{w=0.1} ¿sabes?"
                n 1knmsl "Incluso algo pequeño como un caramelo o algo.{w=0.2} Solo necesitas algo que te de energía."
                n 1kllpo "No es mucho pedir,{w=0.1} ¿cierto?"

                if Natsuki.isEnamored(higher=True):
                    n 1kllss "¡Ahora vete a por algo para comer, tontín!  Jajaja..."

    else:
        n 1knmsl "¿Te sientes mal,{w=0.1} [player]?"

        if Natsuki.isEnamored(higher=True):
            n 1kllsl "Ojalá haya algo que pudiera hacer para ayudar..."

        n 1fwmsl "No te estás forzando a estar aquí,{w=0.1} ¿no?"
        n 1klrsl "No quiero ser un impedimento a que te sientas mejor."

        if Natsuki.isEnamored(higher=True):
            n 1kwmsll "Tu salud es lo primero, mas allá de nuestro tiempo juntos."

        else:
            n 1flrpul "No soy tan egoísta."

        n 1knmpo "No soy tan egoísta....{w=0.3} prométeme que te irás a descansar si tienes que hacerlo,{w=0.1} ¿está bien?"

        if Natsuki.isLove():
            $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
            n 1knmssl "Te amo,{w=0.1} [chosen_endearment].{w=0.2} Yo...{w=0.3} realmente espero que te mejores pronto..."

        elif Natsuki.isAffectionate(higher=True):
            n 1knmbol "Espero que te sientas mejor pronto,{w=0.1} [player]..."

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_SICK
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._admission_database,
            prompt="Tired",
            label="admission_tired",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_ADMISSION
    )

label admission_tired:
    # Calculate how long the player has been here so far
    $ total_hours_in_session = jn_utils.get_current_session_length().total_seconds() / 3600

    if jn_admissions.last_admission_type == jn_admissions.TYPE_TIRED:
        n 1unmpu "¿Eh?{w=0.2} ¿Todavía estas cansado?"
        n 1fnmpo "¿No estás descansando nada,{w=0.1} [player]?"
        n 1fllpo "No quiero verte todo cascarrabias..."
        n 1klrsm "Así que...{w=0.3} vete a la cama, ¿vale?"
        n 1nchbg "¡Te veré después,{w=0.1} [player]!"

        if Natsuki.isLove():
            $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
            n 1nchsml "¡Te amo,{w=0.1} [chosen_endearment]!"

        elif Natsuki.isAffectionate(higher=True):
            n 1fsqsml "¡No dejes que los ácaros te muerdan!{w=0.2} Jejeje."

        $ persistent.jn_player_admission_type_on_quit = jn_admissions.TYPE_TIRED
        return { "quit": None }

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_ANGRY or jn_admissions.last_admission_type == jn_admissions.TYPE_SAD:
        n 1tllpu "Bueno,{w=0.1} antes me dijiste que no estabas muy feliz,{w=0.1} [player]."
        n 1unmca "Si ya estás cansado,{w=0.1} creo que deberías irte a dormir."
        n 1unmsr "¿Vas a intentarlo,{w=0.1} [player]?"
        menu:
            "Si, a ello voy.":
                n 1fcssm "Bien...{w=0.3} Pronto te sentirás mejor,{w=0.1} ¿de acuerdo?"

                if Natsuki.isAffectionate(higher=True):
                    n 1nwmsm "Te lo prometo."

                n 1nchbg "¡Dulces sueños,{w=0.1} [player]!"

                $ persistent.jn_player_admission_type_on_quit = jn_admissions.TYPE_TIRED
                return { "quit": None }

            "No, todavía no.":
                n 1ulrpo "Bueno...{w=0.3} si tu lo dices,{w=0.1} [player]."
                n 1fsgsm "Ahora,{w=0.1} veamos si no empeoro ese humor tuyo,{w=0.1} ¿eh?"

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_SICK:
        n 1ulrpo "No me sorprende, estás enfermo,{w=0.1} [player]."
        n 1fnmpo "Deberías descansar."
        n 1kllss "Podemos hablar más tarde,{w=0.1} ¿te parece?"
        n 1knmsm "¡Tómatelo con calma,{w=0.1} [player]!"

        # Add pending apology
        $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_UNHEALTHY)

        $ persistent.jn_player_admission_type_on_quit = jn_admissions.TYPE_SICK
        return { "quit": None }

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_HUNGRY:
        n 1fskem "¡No me sorprende que estés cansado si tienes hambre!"
        n 1kchgn "¡Levanta ese culo de la silla y vete a comer algo,{w=0.1} [player]!"
        n 1tnmsl "Y tampoco te sobre esfuerces,{w=0.1} ¿vale?{w=0.2} No vaya a ser que te desmayes aquí."
        n 1klrsf "Y créeme,{w=0.1} dudo que quieras tampoco..."

    elif total_hours_in_session >= 24:
        n 1fbkwrl "¡[player]!"
        n 1kskem "Llevas aquí un día entero o más{w=0.1} -{w=0.1} ¡cómo no vas a estar cansado!"
        n 1fnmpo "You better get some sleep right now!{w=0.2} And I don't wanna see you come back until you've slept!"
        n 1fcspo "Por dios..."
        n 1knmpo "¡Ahora vete,{w=0.1} [player]!{w=0.2} Te veo más tarde,{w=0.1} ¿'tá bien?"
        $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
        n 1unmbg "¡Que duermas bien,{w=0.1} [chosen_tease]!"

        if Natsuki.isLove():
            n 1uchsml "¡Te amo~!"

        elif Natsuki.isAffectionate(higher=True):
            n 1nllsml "¡Dulces sueños! Jejeje."

        # Add pending apology
        $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_UNHEALTHY)

        $ persistent.jn_player_admission_type_on_quit = jn_admissions.TYPE_TIRED
        return { "quit": None }

    elif total_hours_in_session >= 12:
        n 1fbkwr "¡[player]!"
        $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
        n 1fnmpo "No me sorprende que te sientas cansado{w=0.1} -{w=0.1} ¡has estado aquí muchísimo rato,{w=0.1} [chosen_tease]!"
        n 1fllpo "Necesitas dormir un poco...{w=0.3} ¡sino vas a ser un cascarrabias dentro de poco!"
        n 1kllpo "Aprecio tu compañía, pero deberías irte a dormir pronto,{w=0.1} ¿entendido?"

        if 1knmpul Natsuki.isLove():
            n 1klrpul "Ya sabes que no me gusta cuando no te cuidas, como ahora estás haciendo..."

        elif Natsuki.isAffectionate(higher=True):
            n 1fcspol "Deberías aprender a cuidarte mejor, esto no puede ser,{w=0.1} [player]..."

        n 1fllsfl "No me falles,{w=0.1} ¿entendido?"

        # Add pending apology
        $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_UNHEALTHY)

    elif jn_get_current_hour() > 21 or jn_get_current_hour() < 3:
        n 1fskem "¡[player]!"
        n 1fnmem "¡No me sorprende que estes cansado!{w=0.2} ¡¿Has visto la hora que es?!"
        $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
        n 1knmpu "¡Es medianoche,{w=0.1} [chosen_tease]!"
        n 1fcsanl "Nnnn...{w=0.3} Deberías irte a dormir pronto,{w=0.1} sabes..."
        n 1fnmpol "No quiero verte siendo un cascarrabias por que el niño no quiere dormir suficiente."
        n 1flrpol "Y tú tampoco,{w=0.1} créeme."
        n 1kcspo "Simplemente...{w=0.3} vete a dormir cuanto antes,{w=0.1} ¿vale? {w=0.2} {i}Antes{/i} de que tu teclado sea tu almohada."

        if Natsuki.isLove():
            n 1ksqpol "Además...{w=0.3} ya sabes que yo no tengo suficiente fuerza como para cargarte a la cama...{w=0.3} ¿no es así?"

        n 1kllssl "Jajaja..."

        # Add pending apology
        $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_UNHEALTHY)

    else:
        n 1knmsl "¿Estás cansado,{w=0.1} [player]?"
        n 1kllbo "Deberías pensar en irte a descansar pronto{w=0.1} -{w=0.1} aunque sea a echarte una siesta."
        n 1fcseml "¡No te preocupes por mi si necesitas descansar!{w=0.2} ¡Estaré bien!"
        n 1knmpo "Pero asegúrate de decírmelo si es que decides irte,{w=0.1} [player]."

    $ jn_admissions.last_admission_type = jn_admissions.TYPE_TIRED
    return
