default persistent._farewell_database = dict()
default persistent.jn_player_first_farewell_response = None
default persistent.jn_player_force_quit_state = 1

init python in jn_farewells:
    from Enum import Enum
    import random
    import store
    import store.jn_affinity as jn_affinity
    import store.jn_globals as jn_globals
    import store.jn_utils as jn_utils

    from store import Natsuki
    FAREWELL_MAP = dict()

    class JNFirstLeaveTypes(Enum):
        """
        Ways in which the player may choose to first leave Natsuki; this decides dialogue upon returning.
        """
        will_be_back = 1
        dont_know = 2
        no_response = 3
        force_quit = 4

        def __int__(self):
            return self.value

    class JNForceQuitStates(Enum):
        """
        Tracking for player force quits; this decides dialogue on returning.
        """
        not_force_quit = 1
        first_force_quit = 2
        previously_force_quit = 3

        def __int__(self):
            return self.value

    def get_farewell_options():
        """
        Returns the list of all farewell options when saying Goodbye to Natsuki.
        """
        return [
            ("Me voy a dormir.", "farewell_option_sleep"),
            ("Voy a ir a comer algo.", "farewell_option_eat"),
            ("Voy a salir a alguna parte.", "farewell_option_going_out"),
            ("Voy a trabajar.", "farewell_option_work"),
            ("Voy a ir a la escuela.", "farewell_option_school"),
            ("Voy a jugar a otra cosa.", "farewell_option_play"),
            ("Voy a estudiar un poco.", "farewell_option_studying"),
            ("Voy a hacer otra cosa.", "farewell_option_misc_activity"),
            ("Voy a hacer algunas tareas.", "farewell_option_chores")
        ]

    def select_farewell():
        """
        Picks a random farewell, accounting for affinity
        If the player has already been asked to stay by Natsuki, a farewell without the option
        to stay will be selected
        """
        if store.persistent.jn_player_first_farewell_response is None:
            return "farewell_first_time"

        kwargs = dict()

        farewell_pool = store.Topic.filter_topics(
            FAREWELL_MAP.values(),
            affinity=Natsuki._getAffinityState(),
            excludes_categories=["Failsafe"],
            **kwargs
        )

        return random.choice(farewell_pool).label

label farewell_start:
    $ push(jn_farewells.select_farewell())
    jump call_next_topic

# Only chosen for the first time the player chooses to say Goodbye
label farewell_first_time:
    n 1uskem "E-{w=0.1}espera,{w=0.1} ¿te vas a ir?"
    n 1fskwrl "¡[player]!{w=0.2} ¡E-{w=0.1}espera un segundo!{w=0.5}{nw}"
    extend 1fbkwrl " ¡Solo un momento!"
    n 1fskeml "..."
    n 1klleml "..."
    n 1kplpu "...Tú-{w=0.1} vas a regresar,{w=0.1} ¿verdad?"
    n 1kllun "..."
    n 1kwmem "...¿Verdad?"
    menu:
        "Claro que volveré":
            $ persistent.jn_player_first_farewell_response = int(jn_farewells.JNFirstLeaveTypes.will_be_back)
            $ Natsuki.calculated_affinity_gain(bypass=True)
            n 1unmeml "¡...!{w=0.5}{nw}"
            n 1flleml "¡C-{w=0.1}claro!{w=0.5}{nw}"
            extend 1fsqpol " Más te vale."
            n 1flreml "T-{w=0.1}tú eres responsable de esto,{w=0.1} ya lo sabes{w=0.5}{nw}"
            extend 1flrpol " Así que..."
            n 1kllpol "..."

        "No lo sé..":
            $ persistent.jn_player_first_farewell_response = int(jn_farewells.JNFirstLeaveTypes.unknown)
            n 1kskem "..."
            n 1kskwr "¡N-{w=0.5}no!"
            n 1kcsan "¡No puedes hacerme esto!{w=0.5}{nw}"
            extend 1fcsup " N-{w=0.1}no ahora..."
            n 1kcsun "..."
            n 1ksqun "..."
            n 1kplpu "Por favor,{w=0.1} [player]...{w=0.5}{nw}"
            extend 1kllpu " No es mucho pedir...{w=2}{nw}"
            extend 1kwmem " ¿cierto?"

        "...":
            $ persistent.jn_player_first_farewell_response = int(jn_farewells.JNFirstLeaveTypes.no_response)
            n 1knmem "[player],{w=0.1} v-{w=0.5}vamos..."
            n 1kllpu "Si esto es una broma,{w=0.5}{nw}"
            extend 1fnmpu " ¡realmente no es gracioso!{w=2}{nw}"
            extend 1knmem " ¡L-{w=0.1}lo digo en serio!"
            n 1kllun "..."
            n 1knmaj "Por favor,{w=0.1} [player]...{w=0.5}{nw}"
            extend 1kllpu " No es mucho pedir...{w=2}{nw}"
            extend 1kwmem " ¿cierto?"

    return { "quit": None }

# Only chosen for the first time the player leaves via force quit
label farewell_force_quit:
    $ persistent.jn_player_force_quit_state = int(jn_farewells.JNForceQuitStates.first_force_quit)
    if not persistent.jn_player_first_farewell_response:
        $ persistent.jn_player_first_farewell_response = int(jn_farewells.JNFirstLeaveTypes.force_quit)

    hide screen hkb_overlay
    show glitch_garbled_a zorder 99 with hpunch
    hide glitch_garbled_a
    stop music
    play audio glitch_c

    n 1uskem "¿E-{w=0.3}eh?{w=1}{nw}"
    extend 1uscwr " ¡N-{w=0.3}no!{w=0.2} ¡¡Espera!!{w=0.2} POR FAVOR N-{w=0.3}{nw}"

    play audio static
    show glitch_garbled_b zorder 99 with hpunch
    hide glitch_garbled_b

    return { "quit": None }

# Non-generic farewells - each of these should be registered under FAREWELL_OPTIONS. Affectionate + only.

label farewell_option_sleep:
    if jn_admissions.last_admission_type in (jn_admissions.TYPE_SICK , jn_admissions.TYPE_TIRED):
        # Sick/tired
        n 1kllsl "...[player]."
        n 1knmpu "Yo...{w=0.3} creo que sería una buena idea.{w=0.2} Ya sabes."
        $ feeling_like = "enfermo" if jn_admissions.last_admission_type == jn_admissions.TYPE_SICK else "cansado"
        n 1klrpu "Teniendo en cuenta lo que has dicho antes sobre que te sentias [feeling_like].{w=0.5}{nw}"
        extend 1knmss " Ve a descansar un poco,{w=0.1} ¿de acuerdo?{w=0.2} Siempre podemos hablar más tarde de todos modos."
        n 1kllbg "¿Cierto?"
        n 1kchsm "¡Duerme bien,{w=0.1} [player]!"

    elif jn_get_current_hour() > 22 or jn_get_current_hour() < 6:
        # Late night
        n 1fnmaj "¡E-{w=0.1}espera un momento!{w=0.1} ¡Yo tambien deberia!{w=0.5}{nw}"
        extend 1tnmem " ¿Tanto tardaste en darte cuenta de la hora?"
        n 1fllpo "Cielos...{w=0.5}{nw}"
        extend 1nllpo " pero más vale tarde que nunca,{w=0.1} supongo."
        n 1fllsm "Jejeje.{w=0.5}{nw}"
        extend 1fchsm " ¡Duerme bien,{w=0.1} [player]!"

    elif jn_get_current_hour() >= 21:
        # Standard night
        n 1unmaj "Así que duermes temprano {w=0.1} ¿eh?"
        n 1ullaj "Está bien....{w=0.5}{nw}"
        extend 1fslaj " Supongo."
        n 1fcssm "...Jejeje."
        n 1uchbg "¡No te preocupes!{w=0.2} ¡Duerme bien,{w=0.1} [player]!"

    elif jn_get_current_hour() >= 19:
        # Early night
        n 1unmaj "¿Eh?{w=0.2} ¿Te vas a dormir más temprano hoy?"
        n 1ullaj "Está bien.{w=0.2} Supongo."
        n 1fsqpo "Mas vale que te quedes despierto conmigo luego.{w=0.5}{nw}"
        extend 1fchsg " Jejeje."
        n 1fchbg "¡Buenas noches,{w=0.1} [player]!"

    else:
        # Nap
        n 1tnmpu "¿Eh?{w=0.2} ¿Ahora tomas siestas?{w=0.5}{nw}"
        extend 1tsqca " ...¿En serio?"
        n 1fllca "Cielos...{w=0.3} Juro que a este paso me tocará alimentarte como si fueras un bebe...."
        n 1fsqsm "..."
        n 1fchbg "Jejeje.{w=0.2} ¡Bromeo,{w=0.1} bromeo!{w=0.5}{nw}"
        extend 1ullbg " Crédulo."
        n 1uchbg "¡Te veo después,{w=0.1} [player]~!"

    if Natsuki.isEnamored(higher=True):
        n 1fchbgl "¡Que no te coman las chinches!"

    if Natsuki.isLove():
        n 1uchbgf "¡Te amo~!"

    return { "quit": None }

label farewell_option_eat:
    if jn_admissions.last_admission_type == jn_admissions.TYPE_HUNGRY:
        n 1fcsgs "B-{w=0.1}bueno,{w=0.1} ¡Claro!{w=0.2} Ve a por algo de comer,{w=0.1} ¡tonto!"
        n 1fllpo "Cielos..."
        n 1fnmpo "Asegurate que sea algo sano,{w=0.1} ¿entendido?"
        n 1fllsm "...Jejeje.{w=0.2}{nm}"
        extend 1fchbg "¡Buen provecho,{w=0.1} [player]!"

    elif jn_get_current_hour() in (7, 8):
        n 1fnmaj "¡Mas te vale!{w=0.5}{nw}"
        extend 1fslca " Ya {i}sabes{/i} lo que dicen del desayuno,{w=0.1} ¿verdad?"
        n 1fllsm "...Jejeje.{w=0.2}{nm}"
        n 1fchbg "¡Bon appetit,{w=0.1} [player]!"

    elif jn_get_current_hour() in (12, 13):
        n 1unmaj "¿Almorzarás fuera,{w=0.1} [player]?"
        n 1nlrpu "Suena bien,{w=0.1} suena bien."
        n 1nsqsm "Pero, no olvides...{w=0.3}{nm}"
        extend 1fsqss " Eres lo que comes~."
        n 1fchsm "...Jejeje.{w=0.5}{nw}"
        extend 1uchsm "¡Provecho!"

    elif jn_get_current_hour() in (18, 19):
        n 1unmaj "¿Ah?{w=0.1} ¿ya es hora de cenar?{w=0.5}{nw}"
        extend 1unmbg " ¡No problemo!"
        n 1nlrpu "Solo...{w=0.5}{nw}"
        extend 1flrpo " no comas comida instantánea.{w=0.5}{nw}"
        extend 1fsqpo " ¿Entendido?"
        n 1fsqsm "...Jejeje."
        n 1fchbg "¡Provecho,{w=0.1} [player]~!"

    else:
        n 1unmaj "¿Oh?{w=0.2} ¿Vas a buscar un bocadillo?"
        n 1nllaj "Está bien."
        n 1nsqpo "Más vale que no te llenes con comida chatarra,{w=0.1} [player]."
        n 1fsqsm "...Jejeje.{w=0.5}{nw}"
        extend 1uchbg "¡Provecho~!"

    return { "quit": None }

label farewell_option_going_out:
    if jn_is_new_years_eve():
        n 1tsqbg "¿Ajá?{w=0.2} Conque piensas salir,{w=0.1} ¿eh?{w=0.5}{nw}"
        extend 1fchbg " ¡Lo entiendo!"
        n 1ullaj "Solo...{w=0.5}{nw}"
        extend 1nsqsl " No te comportes como un idiota allá afuera,{w=0.1} ¿entendido?"
        n 1fslsl "No quiero que te excedas con la bebida, los fuegos artificiales como bobo y salgas lastimado."
        n 1ullpu "Pero...{w=0.5}{nw}"
        extend 1uchbg "¡Sí!{w=0.2} ¡Diviertete allá afuera,{w=0.1} [player]!"
        n 1usqbg "Y por si no te veo antes."
        n 1fbkbs "¡Feliz año nuevo!"

    elif jn_is_easter():
        n 1unmaj "¿Oh?{w=0.2} ¿Con que piensas salir eh?"
        n 1unmbg "¿Planeaste una comida para hoy, o algo así?"
        n 1tlrsm " ¡{i}Es{/i} pascua,{w=0.1} despues de todo!{w=0.5}{nw}"
        extend 1uchsm " Jejeje."
        n 1ullss "Bueno,{w=0.1} cómo sea.{w=0.5}{nw}"
        extend 1uchgn " ¡Nos vemos despues,{w=0.1} [player]!"

    elif jn_is_halloween():
        n 1usqss "¿Ooh?{w=0.2} ¿Saldrás a pedir dulces en halloween,{w=0.1} [player]?"
        n 1fsqsm "No lo olvides..."
        n 1fsqbg "¡Debes traer mi ración de dulces!"
        n 1fchgn "Jejeje.{w=0.5}{nw}"
        extend 1uchbg " ¡Diviertete~!"

    elif jn_is_christmas_eve():
        n 1unmbo "¿Oh?{w=0.2} ¿Saldrás por nochebuena?"
        n 1kllsl "Bueno...{w=0.3} está bien."
        n 1kllajl "...Regresarás para festejar la navidad conmigo...{w=0.5}{nw}"
        extend 1knmsll " ¿Verdad?"
        n 1klrbgl "...Jajaja.{w=0.3}"
        extend 1kchbg " ¡Nos vemos despues,{w=0.1} [player]!"

    elif jn_is_christmas_day():
        n 1unmbo "¿Em?{w=0.2} ¿Vas a salir?"
        n 1kllsl "Bueno...{w=0.3} no hay problema."
        n 1kllss "Gracias por pasar a visitarme,{w=0.1} [player]."
        n 1kcsssl "Eso...{w=0.3} significa mucho para mi."
        n 1kchss "¡Nos vemos despues,{w=0.1} [player]!{w=0.5}{nw}"
        extend 1kchbg " ¡Y feliz navidad!"

    else:
        n 1unmaj "¿Ah?{w=0.2} ¿Vas a salir,{w=0.1} [player]?"
        n 1fchbg "¡No problemo!{w=0.2} Te veo despues entonces,{w=0.1} ¿okay?"
        n 1nchbg "¡Adio-{w=0.1}sito,{w=0.1} [player]!"

    if Natsuki.isLove():
        n 1uchbgf "¡Te amo~!"

    return { "quit": None }

label farewell_option_work:
    if jn_get_current_hour() >= 20 or jn_get_current_hour() <= 4:
        n 1knmaj "¿E-{w=0.1}eh?{w=0.2} ¿Vas a ir a trabajar ahora?"
        $ time_concern = "tarde" if jn_get_current_hour() >= 20 else "pronto"
        n 1kllaj "Pero...{w=0.3} es super [time_concern] aunque,{w=0.1} [player]..."
        n 1kllun "..."
        n 1fnmun "Sólo...{w=0.3} ten cuidado,{w=0.1} ¿de acuerdo?"
        extend 1fsqpo " Y {i}será mejor{/i} que vengas a visitarme cuando vuelvas."
        n 1fllsm "...Jejeje."
        n 1fchbg "¡Da tu mejor esfuerzo,{w=0.1} [player]!"

    else:
        n 1unmaj "¿Oh?{w=0.2} ¿Trabajas hoy?"

        if jn_is_easter():
            n 1uskgs "...de todos los días,{w=0.1} ¿en serio en Pascua?{w=0.5}{nw}"
            extend 1fslpo " Madre mía..."

        elif jn_is_christmas_eve():
            n 1fskgsl "...¿Tienes que ir incluso en Nochebuena?{w=0.5}{nw}"
            extend 1fcseml " Tienes que estar bromeando..."

        elif jn_is_christmas_day():
            n 1fskwrl "...¡¿En {i}Navidad{/i}?!{w=0.5}{nw}"
            extend 1fcseml " Agh..."
            n 1fslpol "..."
            n 1fslajl "Está bien..."

        elif jn_is_new_years_eve():
            n 1fskgsl "...En año nuevo,{w=0.1} ¡¿también tienes que ir?!{w=0.5}{nw}"
            extend 1fcseml " Dios..."

        elif not jn_is_weekday():
            n 1uwdaj "I-{w=0.1}incluso en fin de semana,{w=0.1} ¡¿también debes ir?!{w=0.5}{nw}"
            extend 1fslpu " Hombre..."

        n 1nlrpo "Es una mierda que tengas que trabajar,{w=0.1} pero lo entiendo.{w=0.2} Supongo."
        n 1fnmpo "...Sin embargo, será mejor que vengas a visitarme cuando acabes."
        n 1fsqsm "Jejeje."
        n 1fchbg "Tómalo con calma, {w=0.1} [player]{w=0.2} ¡no dejes que nadie te apresure!"

    if Natsuki.isLove():
        $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
        n 1uchbgf "¡Tu puedes,{w=0.1} ¡[chosen_endearment]!{w=0.2} ¡Te amo~!"

    elif Natsuki.isEnamored(higher=True):
        $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
        n 1uchbgl "¡Yo creo en ti,{w=0.1} [chosen_tease]!"

    return { "quit": None }

label farewell_option_school:
    if jn_get_current_hour() >= 20 or jn_get_current_hour() <= 4:
        n 1twdem "...¿Clases?{w=0.2} ¿A esta hora?"

        if jn_is_easter():
            n 1uskgs "...¿Tambien tienes que ir en pascua?"

        elif jn_is_christmas_eve():
            n 1fskgsl "...¿En Nochebuena?"

        elif jn_is_christmas_day():
            n 1fskwrl "...En ¡¿{i}Navidad{/i}?!"

        elif jn_is_new_years_eve():
            n 1fskgsl "...¿En{w=0.1} año nuevo tambien?"

        if not jn_is_weekday():
            extend 1uskwr "P-{w=0.1}pero {i}en fin de semana{/i} ¡¿tambien?!"

        n 1fbkgs "¿Qué clase de escuela es esa?"
        n 1kllpo "Dios.{w=0.5}{nw}"
        extend 1fllpo " Y yo que pensaba que mi experiencia en la escuela era bastante mala."
        n 1kcspu "Solo...{w=0.5}{nw}"
        extend 1knmpu " Ten cuidado,{w=0.1} ¿sí?"
        $ time_concern = "tarde" if jn_get_current_hour() >= 20 else "pronto"
        extend 1fllsr "Es realmente [time_concern],{w=0.1} después de todo."
        n 1kllss "¡Estudia mucho,{w=0.1} [player]!"

    else:
        if jn_is_easter():
            n 1uskgs "...¿Tambien tienes que ir en pascua?,{w=0.1} ¿en serio?{w=0.5}{nw}"
            extend 1fslpo " Hombre..."

        elif jn_is_christmas_eve():
            n 1fskgsl "...¿En Nochebuena?{w=0.5}{nw}"
            extend 1fcseml " Tienes que estar bromeando..."

        elif jn_is_christmas_day():
            n 1fskwrl "...En ¡¿{i}navidad{/i}?!{w=0.5}{nw}"
            extend 1fcseml " Agh..."
            n 1fslpol "..."
            n 1fslajl "Esta bien..."

        elif jn_is_new_years_eve():
            n 1fskgsl "...¡¿En año nuevo,{w=0.1} tambien?!{w=0.5}{nw}"
            extend 1fcseml " Dios..."

        elif jn_is_weekday():
            n 1unmaj "¿Vas a la escuela{w=0.1} [player]?{w=0.5}{nw}"
            extend 1nchsm " ¡No te preocupes!"

        else:
            n 1tnmpu "¿Eh?{w=0.2} ¿Hoy vas a la escuela?{w=0.5}{nw}"
            extend 1nsqpu "En pleno... ¿{i}fin de semana{/i}?"
            n 1fslpu "..."
            n 1fsqpo "¿En serio?..."

        n 1tsqsm "Realmente odiaria estar en tu lugar, {w=0.1} ¿no crees?{w=0.5}{nw}"
        extend 1fchsm " Jejeje."
        n 1fchbg "¡No procastines,{w=0.1} [player]!{w=0.2} ¡Nos vemos luego!"

    if Natsuki.isLove():
        $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
        n 1uchbgf "¡Te amo,{w=0.1} [chosen_endearment]!"

    return { "quit": None }

label farewell_option_misc_activity:
    n 1knmpu "¿E-{w=0.1}eh?{w=0.5}{nw}"
    extend 1kllaj " ¿Y tienes que irte para hacer eso también?"
    n 1fcsun "Nnnnnn...{w=0.5}{nw}"
    extend 1kcsaj " Vale."
    n 1fnmpol "...Pero será mejor que vengas a visitarme cuando hayas terminado."
    extend 1klrpo "{w=0.2} ¿Entendido?"
    n 1kllpo "¡Hasta pronto,{w=0.1} [player]!"

    if Natsuki.isLove():
        n 1kllssf "¡Te amo!"

    return { "quit": None }

label farewell_option_play:
    n 1fsqaj "...¿En serio,{w=0.5} [player]?"
    n 1nslpu "En serio, prefieres más jugar {i}videojuegos{/i}...{w=0.5}{nw}"
    extend 1fsqsf " ¿que pasar tiempo conmigo?"
    n 1fcssl "..."
    n 1uchgn "Bueno,{w=0.1} ¡tú te lo pierdes!{w=0.5}{nw}"
    extend 1uchlg " ¡Jajaja!"
    n 1nllbg "No,{w=0.1} no.{w=0.2} Está bien.{w=0.2} Ve a lo tuyo{w=0.1} [player].{w=0.5}{nw}"
    extend 1nsqbg " Además..."
    n 1usqct "Seguro que te vendría bien la práctica, {w=0.1} ¿eh?{w=0.5}{nw}"
    extend 1fchsm " Jejeje."
    $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
    n 1fchbg "¡Nos vemos luego,{w=0.1} [chosen_tease]!"

    return { "quit": None }

label farewell_option_studying:
    $ player_initial = list(player)[0]
    n 1fskgsl "¡[player_initial]-{w=0.1}[player]!"
    n 1fllanl "¡Si hubiera sabido que estabas a punto de estudiar te habría echado yo misma!{w=0.5}{nw}"
    extend 1fllpo " Demonios..."
    n 1fnmpo "Espero que no tengas exámenes mañana o algo así..."
    n 1flrpo "Pero de cualquier manera,{w=0.1} estarás bien.{w=0.2} ¡Sólo ve!{w=0.5}{nw}"
    extend 1fwdaj " ¡Vamos!"
    n 1fchgn "...¡Adiós adiós,{w=0.1} tonto!{w=0.2} Jejeje.{w=0.5}{nw}"
    extend " ¡Hablamos luego!"

    if Natsuki.isLove():
        n 1uchbgf "¡Te amo~!"

    return { "quit": None }

label farewell_option_chores:
    if store.jn_get_current_hour() >= 20 or store.jn_get_current_hour() <= 4:
        n 1tnmaj "...¿Quehaceres?{w=0.5}{nw}"
        extend 1tsqem " ¿En {i}este{/i} momento?"
        n 1nllbo "Tengo que decir,{w=0.1} [player]."
        n 1nsqdv "O estás dedicado o estás desesperado.{w=0.5}{nw}"
        extend 1nchsm " Jejeje."
        n 1ullss "Bueno,{w=0.1} como sea.{w=0.5}{nw}"
        extend 1tnmss " Sólo apúrate y despues vete a dormir,{w=0.1} ¿de acuerdo?"

        if Natsuki.isLove():
            n 1uchbg "¡Adiós{w=0.1} [player]!"
            extend 1uchbgf " ¡Te amo~!"

        else:
            n 1fchbg "¡Adios,{w=0.1} [player]!"

    else:
        n 1tnmsg "Atorado con los quehaceres,{w=0.1} ¿eh?"
        n 1nchsm "Jejeje.{w=0.2} Sí,{w=0.1} está bien.{w=0.5}{nw}"
        extend 1fchgn " ¡Ve a ocuparte de tu racha de limpieza!"

        if Natsuki.isLove():
            n 1uchbg "¡Hasta pronto,{w=0.1} [player]!{w=0.5}{nw}"
            extend 1uchbgf " ¡Te amo~!"

        else:
            n 1fchbg "Jejeje.{w=0.2} ¡Adiós,{w=0.1} [player]!"

    return { "quit": None }

# Generic farewells

# LOVE+ farewells
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_you_mean_the_world_to_me",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_you_mean_the_world_to_me:
    n 1kplsfl "Aww...{w=0.3} ¿Ya te vas,{w=0.1} [player]?{w=0.2} Hm,{w=0.1} está bien..."
    n 1knmsfl "S-{w=0.2}sabes que te extranaré,{w=0.1} ¿verdad?"
    n 1knmssf "¡Cuídate,{w=0.1} [player]!{w=0.2} ¡Lo eres todo para mí!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_dont_like_saying_goodbye",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_dont_like_saying_goodbye:
    n 1fplpol "Sabes que no me gusta despedirme,{w=0.1} [player]..."
    n 1ncssll "..."
    n 1kplsml "¡Está bien!{w=0.2} Solo vuelve pronto,{w=0.1} ¿si?"
    n 1kchbgf "¡Cuídate,{w=0.1} bobo!{w=0.2} ¡Te amo!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_counting_on_you",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_counting_on_you:
    n 1fllpol "Uuuuh...{w=0.3} No me gusta despedirme..."
    n 1knmsml "Pero supongo que no puedo hacer nada para evitarlo,{w=0.1} [player]."
    $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
    n 1uchbgf "¡Cuídate allá afuera,{w=0.1} [chosen_endearment]!{w=0.2} ¡Cuento contigo!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_do_your_best",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_do_your_best:
    n 1unmajl "¿Eh?{w=0.2} ¿Ya te vas?"
    n 1flrpol "Bien,{w=0.1} supongo..."
    n 1kplsml "Te voy a extrañar mucho,{w=0.1} [player]."
    $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
    n 1uchsmf "¡Da lo mejor de ti,{w=0.1} [chosen_endearment]!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_rooting_for_you",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_rooting_for_you:
    n 1unmajl "¿Eh?{w=0.2} ¿Ya te vas?"
    n 1fcssll "Odio cuando tienes que irte..."
    $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
    n 1kcssml "...Pero sé que regresarás,{w=0.1} [chosen_endearment]."
    n 1unmbgl "Bueno...{w=0.1} ¡Suerte!"
    n 1uchbgf "¡Hazme sentir orgullosa,{w=0.1} [player]!{w=0.2} ¡Te amo!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_me_to_deal_with",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_me_to_deal_with:
    n 1unmajl "¿Te vas,{w=0.1} [player]?"
    n 1fllpol "Awww...{w=0.3} bueno está bien."
    n 1knmssl "Cuídate,{w=0.1} ¿entendido? ¡O te las verás conmigo!"
    n 1uchbgf "¡Adiós!{w=0.2} ¡Te amo!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_love_wish_you_could_stay_forever",
            unlocked=True,
            affinity_range=(jn_affinity.LOVE, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_love_wish_you_could_stay_forever:
    n 1kplsml "¿Hora de irse,{w=0.1} [player]?"
    n 1kllssl "A veces deseo que pudieras quedarte por siempre...{w=0.3} Jejeje."
    n 1knmsml "Pero entiendo que tienes cosas que hacer allá afuera."
    $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
    n 1uchbgf "¡Adiós,{w=0.1} [chosen_endearment]!"

    return { "quit": None }

# AFFECTIONATE/ENAMORED farewells

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_was_having_fun",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_was_having_fun:
    n 1unmajl "¿Hmm?{w=0.2} ¿Ya te vas?"
    n 1knmsll "Aww,{w=0.1} hombre..."
    n 1kllpol "Me estaba divertiendo tanto..."
    n 1unmbgl "Bueno,{w=0.1} si tienes que irte,{w=0.1} ¡tienes que irte!"
    n 1uchbgl "¡Cuídate,{w=0.1} [player]!{w=0.2} ¡Hazme sentir orgullosa!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_waiting_for_you",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_waiting_for_you:
    n 1unmajl "¿Ya te vas,{w=0.1} [player]?"
    n 1kplpol "Uuuuuh...{w=0.3} bien..."
    n 1knmpol "¡Trata de volver pronto,{w=0.1} ¿sí?"
    n 1nnmsml "¡Estaré esperando!"
    n 1nchbgl "¡Adiós,{w=0.1} [player]!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_ill_be_okay",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_ill_be_okay:
    n 1unmajl "¿Eh?{w=0.2} ¿Ya te vas?"
    n 1kcssfl "..."
    n 1kcssll "Bueno...{w=0.3} Estaré bien..."
    n 1fplcaf "Será mejor que vuelvas pronto,{w=0.1} ¿entendido [player]?"
    n 1kchsml "¡Adiós!{w=0.2} ¡Estaré esperando!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_dont_make_me_find_you",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_dont_make_me_find_you:
    n 1unmajl "¿Oh?{w=0.2} ¿Ya te vas,{w=0.1} [player]?"
    n 1kllpol "Yo...{w=0.3} quisiera que no te fueras..."
    n 1knmssl "Pero entiendo que tienes responsabilidades."
    n 1knmajl "Será mejor que vuelvas pronto,{w=0.1} ¿me lo prometes?"
    n 1fchdvl "¡No me obligues salir a buscarte!{w=0.2} Jejeje."

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_take_care_for_both",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_take_care_for_both:
    n 1unmajl "¿Mmm?{w=0.2} ¿Ya te vas,{w=0.1} [player]?"
    n 1fcspol "Esperaba que te quedaras un poco más..."
    n 1nllnvl "Bueno,{w=0.2} ¡está bien!"
    n 1fnmcaf "¡Cuídate,{w=0.1} [player]!{w=0.2} Y-{w=0.1}y no lo hagas solo por mí,{w=0.1} ¿sí?"
    n 1kchbgl "¡Hasta luego!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_enjoy_our_time_together",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_enjoy_our_time_together:
    n 1tnmajl "¿Ya te vas,{w=0.1} [player]?"
    n 1fllcal "Nnnnnn...{w=0.3} bien."
    n 1knmcaf "Será mejor que vuelvas pronto,{w=0.1} ¿entendido?{w=0.2} Yo...{w=0.3} disfruto el tiempo que pasamos juntos."
    n 1kllsmf "¡Hasta luego,{w=0.1} [player]!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_affectionate_enamored_see_me_soon",
            unlocked=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_affectionate_enamored_see_me_soon:
    n 1fllcal "Bueno,{w=0.1} eventualente tendrías que irte."
    n 1fnmpol "No es que me guste..."
    n 1kplpol "Vuelve pronto,{w=0.1} ¿sí?"

    return { "quit": None }

# HAPPY/AFFECTIONATE farewells

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_going_now",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.AFFECTIONATE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_going_now:
    n 1unmsm "¿Ya te vas,{w=0.1} [player]?{w=0.2} ¡Nos vemos luego!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_heading_off",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.AFFECTIONATE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_heading_off:
    n 1unmaj "¿Te vas,{w=0.1} [player]?"
    n 1nnmsm "¡Bien!{w=0.2} ¡Cuídate!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_stay_safe",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.AFFECTIONATE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_stay_safe:
    n 1nchss "¡Okie doki!{w=0.2} ¡Estaré esperando!"
    n 1nnmsm "¡Cuídate,{w=0.1} [player]!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_take_care",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.AFFECTIONATE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_take_care:
    n 1nnmbg "¡Nos vemos luego,{w=0.1} [player]!"
    n 1nchsm "¡Cuídate!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_happy_affectionate_see_me_soon",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.AFFECTIONATE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_happy_affectionate_see_me_soon:
    n 1nchbg "¡Adiós,{w=0.1} [player]!"
    n 1nchsm "Vuelve pronto,{w=0.1} ¿sí?"

    return { "quit": None }

# NORMAL/HAPPY farewells

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_see_you_later",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_see_you_later:
    n 1nchsm "¡Nos vemos luego,{w=0.1} [player]!"
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_later",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_later:
    n 1nnmss "¡Hasta luego,{w=0.1} [player]!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_goodbye",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_goodbye:
    n 1nchsm "¡Adiós,{w=0.1} [player]!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_kay",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_kay:
    n 1nwmss "¡Okie doki!{w=0.2} ¡Hasta pronto!"

    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_normal_happy_see_ya",
            unlocked=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.HAPPY)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_normal_happy_see_ya:
    n 1nchbg "¡Adiosito,{w=0.1} [player]!"

    return { "quit": None }

# UPSET/DISTRESSED farewells
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_bye",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_bye:
    n 1nnmsl "Adiós,{w=0.1} [player]."
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_later",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_later:
    n 1nnmsf "Hasta luego,{w=0.1} [player]."
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_kay",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_kay:
    n 1fllsf "Bueno.{w=0.2} Hasta luego."
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_goodbye",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_goodbye:
    n 1flrsf "Adiós,{w=0.1} [player]."
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_upset_distressed_see_you_around",
            unlocked=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.UPSET)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_upset_distressed_see_you_around:
    n 1fsqsf "Nos vemos luego."
    return { "quit": None }

# DISTRESSED/BROKEN/RUINED farewells

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_yeah",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_yeah:
    n 1fcssf "Eh, sí."
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_yep",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_yep:
    n 1fcsup "Bueno."
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_uh_huh",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_uh_huh:
    n 1fsqsl "Ah ajá."
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_nothing_to_say",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_nothing_to_say:
    n 1fcssf "..."
    n 1kcsup "..."
    return { "quit": None }

init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_broken_ruined_kay",
            unlocked=True,
            affinity_range=(None, jn_affinity.BROKEN)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_broken_ruined_kay:
    n "Ok."
    return { "quit": None }

# Farewells that allow the player to choose to stay

# Natsuki calls the player out on how long they've been here, and asks for more time together
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_short_session_ask",
            unlocked=True,
            conditional="not jn_globals.player_already_stayed_on_farewell and jn_utils.get_current_session_length().total_seconds() / 60 < 30",
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_short_session_ask:
    n 1uskwrl "¿Qué?{w=0.2} ¿Te vas?{w=0.2} ¡Pero si apenas estuviste un rato,{w=0.1} [player]!"
    $ time_in_session_descriptor = jn_utils.get_time_in_session_descriptor()
    n 1fnmpol "¡De hecho,{w=0.1} solo has estado por [time_in_session_descriptor]!"
    menu:
        n "¿Seguro de qué no puedes quedarte un poco más?"

        "Claro que si, puedo quedarme un rato más":
            n 1uchbsl "¡Yay{nw}!"
            n 1uskgsl "¡D-digo...!"
            if Natsuki.isLove():
                n 1kllssl "G-{w=0.1}gracias,{w=0.1} [player]. Significa mucho para mí."
                $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
                n 1kplssl "De verdad.{w=0.2} Gracias,{w=0.1} [chosen_endearment]."
                n 1klrbgl "...¡C-{w=0.1}como sea!"

            else:
                n 1fnmbgl "¡Sí!{w=0.2} ¡Es justo lo que pensaba!"
                n 1fcsbgl "Bueno..."
                n 1fnmunl "..."
                n 1fbkwrf "¡Deja de verme así,{w=0.1} demonios!"
                n 1fllpof "Agh..."

            n 1fllbgl "B-{w=0.1}bueno,{w=0.1} ¿dónde estábamos?"
            $ jn_globals.player_already_stayed_on_farewell = True

        "Si tú lo dices":
            n 1kllpol "[player]..."
            n 1knmpol "No te...{w=0.3} estoy obligando a estar aquí.{w=0.1} Sabes eso,{w=0.1} ¿verdad?"
            menu:
                n "¿Seguro que quieres quedarte?"

                "Si, estoy seguro":
                    n 1knmpol "Bueno,{w=0.1} ya dijiste que si."
                    n 1kllcal "Solo queria asegurarme de que no sueno como una mandona."
                    if Natsuki.isEnamored(higher=True):
                        $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
                        n 1knmssl "Gracias,{w=0.1} [chosen_endearment]. Significa mucho para mí."

                    else:
                        n 1nlrcaf "Gracias,{w=0.1} [player].{w=0.2} Lo aprecio mucho."

                    $ Natsuki.calculated_affinity_gain()
                    $ jn_globals.player_already_stayed_on_farewell = True

                "No, debo irme":
                    n 1knmcal "Bueno...{w=0.3} vale,{w=0.1} [player]."
                    n 1knmpol "Cuídate,{w=0.1} ¿sí?"
                    n 1uchsml "¡Nos vemos luego!"

                    return { "quit": None }

        "Lo siento, [n_name]. De verdad debo irme":
            n 1fllanl "¡Nnnnnn-!"
            n 1kcssll "..."
            n 1klrsll "Bueno...{w=0.3} está bien."
            n 1kllpol "Pero no tardes mucho,{w=0.1} ¿sí?"
            n 1knmsml "¡Nos vemos luego,{w=0.1} [player]!"

            return { "quit": None }

    return

# Natsuki calls the player out on how long they've been here, and asks for more time together (alt)
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_short_session_ask_alt",
            unlocked=True,
            conditional="not jn_globals.player_already_stayed_on_farewell and jn_utils.get_current_session_length().total_seconds() / 60 < 30",
            affinity_range=(jn_affinity.HAPPY, jn_affinity.ENAMORED)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_short_session_ask_alt:
    n 1knmgsl "¡E-{w=0.1}espera un segundo,{w=0.1} [player]!{w=0.2} ¡Esto no es nada justo!"
    $ time_in_session_descriptor = jn_utils.get_time_in_session_descriptor()
    n 1knmpol "Apenas has estado [time_in_session_descriptor],{w=0.1} ¿y ya te quieres ir?"
    menu:
        n "¡Vamos!{w=0.2} Seguro que te quedaras un poco más,{w=0.1} ¿verdad?"

        "Claro que si, puedo quedarme un rato más.":
            n 1fcsbsl "¡J-{w=0.1}ja!{w=0.2} Lo sabia."
            n 1fsqdvl "Jejeje.{w=0.1} ¡Parece que gano de nuevo,{w=0.1} [player]!"
            menu:
                n "¿O-o es que no puedes alejarte de mí ni por un segundo?"

                "Me atrapaste, [n_name]. No podría irme aunque quisiera":
                    $ player_was_snarky = False
                    n 1uscwrf "¿Q-{w=0.2}qué...?"
                    n 1fcsunf "¡Nnnnnnn-!"
                    $ player_initial = list(player)[0]
                    n 1fbkwrf "¡[player_initial]-{w=0.2}[player]!"
                    n 1fllwrf "¡No me salgas con esas cursilerias ahora!"
                    n 1fllpof "Demonios...{w=0.3} eres un grandísimo tonto a veces..."

                "Si, si, lo que digas":
                    $ player_was_snarky = True
                    n 1fsqbgf "Jejeje.{w=0.2} ¿Qué pasa,{w=0.1} [player]?"
                    n 1tsqdvf "¿Muy cerca de la verdad?"
                    n 1uchbsf "¡Jajaja!"

            n 1nllbgl "Bueno,{w=0.1} de cualquier manera,{w=0.1} ¡me alegra que te quedes por un rato más!"

            if player_was_snarky:
                n 1nsqbgf "O...{w=0.3} ¿el que deberia estar agradeciendo serias {i}tú{/i}?{w=0.2} Jejeje."

            n 1nchsml "Bueno...{w=0.3} ¿qué más quieres hacer hoy?"
            $ jn_globals.player_already_stayed_on_farewell = True
            $ Natsuki.calculated_affinity_gain()

        "Si, supongo":
            n 1fbkwrf "¿{i}Supongo{/i}?{w=0.2} ¡¿Qué quieres de decir con{w=0.2} supongo?!"
            n 1fnmpol "Diablos...{w=0.3} ¿Por qué esa actitud hoy,{w=0.1} [player]?"
            n 1fllpof "Bueno,{w=0.1} como sea...{w=0.3} Gracias por acompañarme un rato más."
            n 1fsgsgl "...{i}Supongo{/i}."
            n 1uchgnl "¡Jajaja!{w=0.2} ¡Oh,{w=0.1} alégrate,{w=0.1} [player]!{w=0.2} ¡Solo juego contigo!"
            n 1tllsml "Jejeje.{w=0.2} Ahora,{w=0.1} ¿dónde estábamos?"
            $ jn_globals.player_already_stayed_on_farewell = True
            $ Natsuki.calculated_affinity_gain()

        "Lo siento [n_name], no puedo":
            n 1fcsunf "Uuuuh-"
            n 1kllcaf "Bueno,{w=0.1} supongo que está bien.{w=0.2} No se puede hacer nada al respecto."
            n 1fnmajf "Pero después nos arreglamos,{w=0.1} ¿entendido?"
            n 1kchbgl "¡Cuídate,{w=0.1} [player]!{w=0.2} ¡Nos vemos luego!"

            return { "quit": None }
    return

# Natsuki tries to confidently ask her player to stay
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_fake_confidence_ask",
            unlocked=True,
            conditional="not jn_globals.player_already_stayed_on_farewell",
            affinity_range=(jn_affinity.HAPPY, jn_affinity.AFFECTIONATE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_fake_confidence_ask:
    n 1knmaj "¿Eh?{w=0.2} No tienes que irte tan pronto,{w=0.1} ¿sabes?"
    n 1fllsf "¡Se siente como si apenas hubieras estado aquí!"
    n 1flldv "¡A-{w=0.1}apuesto todo a que puedes quedarte un poco más!{w=0.2} ¿Cierto,{w=0.1} [player]?"
    menu:
        n "{w=0.3}...¿Cierto?"

        "¡Cierto!":
            n 1fcsbgl "¡A-ajá!{w=0.2} ¡Lo sabía!"
            n 1fllbg "¡N-{w=0.1}no es como si te necesitara aquí,{w=0.1} ni nada de eso!"
            n 1flldvl "Debes pasar mucho tiempo solo como para ser {i}tan{/i} dependiente de alguien...{w=0.3} Jajaja..."
            n 1klrsll "..."
            n 1fcswrf "¡D-{w=0.1}demonios!{w=0.2} Olvídalo..."
            n 1fllajf "Ahora,{w=0.1} ¿dónde estábamos?"
            $ jn_globals.player_already_stayed_on_farewell = True
            $ Natsuki.calculated_affinity_gain()

        "Lo siento, en verdad tengo que irme":
            n 1fllbgf "O-{w=0.1}oh...{w=0.3} ajá..."
            n 1fllpol "Está bien,{w=0.1} supongo..."
            n 1fnmbg "¡Te veo luego entonces,{w=0.1} [player]!"
            n 1knmpo "No me hagas esperar mucho,{w=0.1} ¿entendido?"

            return { "quit": None }
    return

# Natuski really doesn't want to be alone today; she pleads for her player to stay
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_pleading_ask",
            unlocked=True,
            conditional="not jn_globals.player_already_stayed_on_farewell",
            affinity_range=(jn_affinity.ENAMORED, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_pleading_ask:
    n 1kskwrf "¡N-no!{w=0.2} ¡Aún no puedes irte!"
    n 1kllupf "..."
    n 1kcssfl "[player]..."
    n 1klrsff "{w=0.3} De...{w=0.3} verdad...{w=0.3} quiero que estés conmigo ahora mismo."
    menu:
        n "Solo un rato más...{w=0.3} ¿sí?"

        "¡Claro!":
            n 1kchbsf "¡Sí!{nw}"
            n 1knmajf "¡D-digo...!"
            n 1kllslf "..."
            $ chosen_descriptor = random.choice(jn_globals.DEFAULT_PLAYER_DESCRIPTORS)
            n 1kllnvf "G-{w=0.1}gracias,{w=0.1} [player].{w=0.1} Eres [chosen_descriptor],{w=0.1} ¿sabías?"
            n 1kplsmf "De verdad.{w=0.1} Gracias."
            n 1kllbgf "A-{w=0.1}ahora,{w=0.1} ¿dónde estábamos? Je..."
            $ jn_globals.player_already_stayed_on_farewell = True
            $ Natsuki.calculated_affinity_gain()

        "No puedo":
            n 1kllsff "Oh..."
            n 1knmajl "Bueno,{w=0.1} si te tienes que ir,{w=0.1} no se puede evitar,{w=0.1} supongo..."
            n 1kplpol "Vuelve pronto,{w=0.1} ¿entendido?"
            n 1klrsmf "O te las tendrás que ver conmigo...{w=0.3} Jajaja..."
            n 1knmsmf "¡Cuídate,{w=0.1} [player]!"

            return { "quit": None }
    return

# Natsuki gently asks her player to stay
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_gentle_ask",
            unlocked=True,
            conditional="not jn_globals.player_already_stayed_on_farewell",
            affinity_range=(jn_affinity.LOVE, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_gentle_ask:
    n 1knmsrf "[player]...{w=0.3} ¿en serio tienes que irte ahora?"
    n 1kplsrf "Sé que tienes cosas que hacer,{w=0.1} pero...{w=0.3} esperaba...{w=0.3} pasar más tiempo contigo."
    menu:
        n "¿Seguro que debes irte ahora?"

        "Bueeeno, puedo quedarme un rato más.":
            n 1kplsmf "[player]..."
            n 1kchsmf "Gracias.{w=0.2} Eso significa mucho para mí."
            $ chosen_descriptor = random.choice(jn_globals.DEFAULT_PLAYER_DESCRIPTORS)
            n 1kwmssf "E-{w=0.1}eres [chosen_descriptor],{w=0.1} [player]."
            n 1kcssmf "En serio.{w=0.1} Gracias..."
            n 1kcssmf "..."
            n 1kllbgf "Jaja...{w=0.3} ¿qué más quieres hacer hoy?"
            $ jn_globals.player_already_stayed_on_farewell = True
            $ Natsuki.calculated_affinity_gain()

        "Lo siento, en verdad tengo que irme.":
            n 1kllsrf "Oh..."
            n 1kplsmf "Mentiría si digo que no estoy molesta,{w=0.1} pero lo entiendo."
            n 1kwmsrf "Solo ten cuidado allá afuera,{w=0.1} ¿sí?"
            n 1kllsrf "..."
            n 1kwmsmf "T-{w=0.1}te amo,{w=0.1} [player]..."
            n 1kchsmf "Nos vemos luego."

            return { "quit": None }
    return

# Time-of-day based farewells

# Early morning

# Natsuki thanks the player for visiting so early
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_early_morning_going_this_early",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(3, 4)",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_early_morning_going_this_early:
    n 1tnmaj "¿E-{w=0.1}eh?{w=0.2} ¿Te vas tan temprano?"
    n 1kllsl "...Oh."

    if Natsuki.isEnamored(higher=True):
        n 1klrssl "Esperaba...{w=0.3} que pudiéramos estar juntos un poco más...{w=0.3} pero si te tienes que ir,{w=0.1} te tienes que ir."
        n 1unmbgl "Gracias por la visita,{w=0.1} [player].{w=0.2} Lo aprecio mucho."
        n 1knmssl "No apresures las cosas por mi culpa,{w=0.1} ¿entendido?"

    else:
        n 1fchbgf "¡D-{w=0.1}digo,{w=0.1} fue genial que te dieras una vuelta por aquí,{w=0.1} [player]!"

    n 1uchgnl "Cuídate allá afuera,{w=0.1} ¿sí?{w=0.2} ¡No hagas nada tonto!"

    if Natsuki.isLove():
        n 1uchbsf "¡Te amo,{w=0.1} [player]~!"

    elif Natsuki.isAffectionate(higher=True):
        $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
        n 1uchbgl "¡Nos vemos luego,{w=0.1} [chosen_tease]!"

    else:
        n 1uchsml "¡Adiosito!"

    return { "quit": None }

# Morning

# Natsuki wishes the player a good day
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_morning_heading_off",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(5, 11)",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_morning_heading_off:
    n 1nnmbg "¿Hora de irse,{w=0.1} [player]?{w=0.2} ¡No hay problema!"

    if Natsuki.isEnamored(higher=True):
        n 1nchbgl "Espero que tengas un gran día, igual que tú."

        if Natsuki.isLove():
            n 1nchsmf "Jejeje.{w=0.2} ¡Te amo,{w=0.1} [player]~!"

        else:
            n 1uchsml "¡Hasta luego!"

    else:
        n 1unmbg "¡Adiosito!"

    return { "quit": None }

# Afternoon

# Natsuki asks that the player visit later
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_afternoon_come_visit_soon",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(12, 17)",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_afternoon_come_visit_soon:
    n 1unmaj "¿Oh?{w=0.2} Como que te vas algo temprano,{w=0.1} ¿no?"
    n 1ullaj "Supongo que está bien...{w=0.3} pero recuerda volver pronto,{w=0.1} ¿entendido?"

    if Natsuki.isAffectionate(higher=True):
        n 1fnmcal "Me enojaré si no lo haces."
        n 1uchbgl "Jejeje.{w=0.2} ¡Cuídate,{w=0.1} [player]!"

    else:
        n 1nnmsm "¡Cuídate!"

    return { "quit": None }

# Evening

# Natsuki wishes the player a good evening
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_evening_good_evening",
            unlocked=True,
            conditional="store.jn_get_current_hour() in range(18, 21)",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_evening_good_evening:
    n 1unmaj "¿Eh?{w=0.2} ¿Ya te vas,{w=0.1} [player]?"
    n 1ullaj "Hmmm...{w=0.3} está bien."
    n 1nchsm "¡Ten una buena noche!"

    if Natsuki.isAffectionate(higher=True):
        n 1kwmsml "Vísitame pronto,{w=0.1} ¿sí?"

    return { "quit": None }

# Night

# Natsuki can't fault the player for turning in
init 5 python:
    registerTopic(
        Topic(
            persistent._farewell_database,
            label="farewell_night_good_night",
            unlocked=True,
            conditional="store.jn_get_current_hour() >= 22 or store.jn_get_current_hour() <= 2",
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
        ),
        topic_group=TOPIC_TYPE_FAREWELL
    )

label farewell_night_good_night:
    n 1unmaj "¿Eh?{w=0.2} ¿Ya te vas?"
    n 1nnmbg "Bueno...{w=0.3} Viendo la hora, no te culpo."
    n 1uchsm "¡Buenas noches,{w=0.1} [player]!"

    if Natsuki.isAffectionate(higher=True):
        n 1uchbgl "¡Dulces sueños!"

    return { "quit": None }
