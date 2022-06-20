default persistent._compliment_database = dict()

init 0 python in jn_compliments:
    import random
    import store

    COMPLIMENT_MAP = dict()

    # Compliment types
    TYPE_AMAZING = 0
    TYPE_BEAUTIFUL = 1
    TYPE_CONFIDENT = 2
    TYPE_CUTE = 3
    TYPE_HILARIOUS = 4
    TYPE_INSPIRATIONAL = 5
    TYPE_STYLE = 6
    TYPE_THOUGHTFUL = 7

    # The last compliment the player gave to Natsuki
    last_compliment_type = None

    def get_all_compliments():
        """
        Gets all compliment topics which are available

        OUT:
            List<Topic> of compliments which are unlocked and available at the current affinity
        """
        return store.Topic.filter_topics(
            COMPLIMENT_MAP.values(),
            affinity=store.Natsuki._getAffinityState(),
            unlocked=True
        )

label player_compliments_start:
    python:
        compliment_menu_items = [
            (_compliment.prompt, _compliment.label)
            for _compliment in jn_compliments.get_all_compliments()
        ]
        compliment_menu_items.sort()

    call screen scrollable_choice_menu(compliment_menu_items, ("No importa.", None))

    if _return:
        $ push(_return)
        jump call_next_topic

    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="¡Creo que eres increíble!",
            label="compliment_amazing",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_amazing:
    $ Natsuki.calculated_affinity_gain(bypass=get_topic("compliment_amazing").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.TYPE_AMAZING:
        if Natsuki.isEnamored(higher=True):
            n 1uskemf "[player]...{w=0.3} ¡honestamente!{w=0.2} Cielos..."
            n 1kllssl "Pero...{w=0.3} gracias.{w=0.2} Realmente significa mucho para mí."
            n 1fchbgl "Tú también eres increíble, {w=0.1} sin embargo, {w=0.2} ¡Recuerda eso!"

        else:
            n 1kchbgl "Cielos,{w=0.1} [player]...{w=0.3} hoy sí que estás repartiendo cumplidos,{w=0.2} ¿no?"
            n 1kllbgl "No me malinterpretes{w=0.1} -{w=0.1} ¡No me estoy quejando!"
            n 1ksqsm "Asegúrate de no quedarte al margen, sin embargo, {w=0.1} ¿De acuerdo?"
            n 1kchsml "Jejeje."

    else:
        if Natsuki.isEnamored(higher=True):
            n 1kwmpul "¿D-{w=0.1}de verdad lo crees,{w=0.1} [player]?"
            n 1kllsrl "..."
            n 1fcssrl "N-{w=0.1}no me gusta admitirlo,{w=0.1} ¿sabes?"
            n 1klrssl "Pero... {w=0.3} eso significa... {w=0.3} mucho para mí,{w=0.1} [player]."
            $ chosen_descriptor = random.choice(jn_globals.DEFAULT_PLAYER_DESCRIPTORS)
            n 1kwmnvl "De verdad.{w=0.2} Gracias.{w=0.2} Eres sincero [chosen_descriptor]."
            n 1klrnvl "..."

            if Natsuki.isLove():
                n 1kwmsmf "Te amo,{w=0.1} [player]..."

        else:
            n 1flrbsl "¡O-{w=0.1}oh!{w=0.2} ¡Aja!{w=0.2} ¡Sabía que al final lo admitirías!"
            n 1nchgnl "B-{w=0.1}bueno,{w=0.1} Me alegro de que ambos estemos de acuerdo en eso."
            n 1flrbgl "Gracias,{w=0.1} [player]!"

            if Natsuki.isAffectionate(higher=True):
                n 1fwmpul "Pero... {w=0.3} ¡no creas que eso significa que no tienes algo a tu favor también!"
                n 1fllssl "Eres...{w=0.3} bastante asombroso también,{w=0.1} [player].{w=0.2} Será mejor que lo recuerdes, {w=0.1} ¿De acuerdo?"
                n 1klrbgl "Jajaja..."

    $ jn_compliments.last_compliment_type = jn_compliments.TYPE_AMAZING
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="¡Creo que eres hermosa!",
            label="compliment_beautiful",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_beautiful:
    $ Natsuki.calculated_affinity_gain(bypass=get_topic("compliment_beautiful").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.TYPE_BEAUTIFUL:
        if Natsuki.isEnamored(higher=True):
            n 1uskwrf "C-{w=0.1}cielos,{w=0.1} ¡[player]...!"
            n 1fcsanf "¡Uuuuuu-!"
            n 1fbkwrf "¡¿Intentas ponerme en un aprieto o qué?!{w=0.2} ¡Ya me lo has dicho!"
            n 1flrpof "..."
            n 1klrpol "..."
            n 1klrpul "...lo tomaré, {w=0.1} sin embargo."
            n 1fllsll "El cumplido, {w=0.1} Quiero decir."
            $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
            n 1kllssl "G-{w=0.1}gracias de nuevo,{w=0.1} [chosen_tease]."

        else:
            n 1fskwrf "¡¿D-{w=0.1}disculpame?!"
            n 1fbkwrf "¡[player]!{w=0.2} ¡¿Qué te he dicho?!"
            $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
            n 1fcsanf "En serio... {w=0.3} ¡¿estás intentando provocarme un ataque al corazón o algo así{w=0.1} [chosen_tease]?!"
            n 1fllpof "..."

            if Natsuki.isAffectionate(higher=True):
                n 1fcspuf "Sólo... {w=0.3} guárdalo hasta que esté seguro de que lo dices en serio, {w=0.1} ¿de acuerdo?"
                n 1kllpol "Cielos..."

    else:
        if Natsuki.isEnamored(higher=True):
            n 1uskpuf "¡¿E-{w=0.1}ehh?!"
            n 1uskajf "Espera..."
            n 1uskpuf "T-{w=0.1}tú realmente piensas que yo..."
            n 1uscunf "Y-{w=0.3}yo soy..."
            n 1fcsunf "..."
            n 1fnmunf "[player]..."
            n 1knmpuf "Sabes que no debes decir cosas así..."
            n 1kllpuf "¿A menos que lo digas en serio?"
            n 1kcsunf "..."
            n 1klrssf "...Yo...{w=0.3} te creo,{w=0.1} aunque.{w=0.2} No hagas que me arrepienta de haber dicho eso,{w=0.1} ¿de acuerdo?"
            n 1klrbgl "G-{w=0.1}gracias,{w=0.1} [player]."

            if Natsuki.isLove():
                n 1kwmsmf "...Te amo,{w=0.1} [player]...{w=0.3} Jajaja..."

        else:
            n 1uscemf "¿Q{w=0.1}-q{w=0.1}-qué?"
            n 1fskwrf "¡¿Q-{w=0.1}que dijiste?!"
            n 1fcsanf "¡Nnnnnnnnnn-!"
            n 1fbkwrf "N-{w=0.1}no puedes decir cosas así de repente, {w=0.1} ¡tonto!"
            n 1fllemf "Dios..."

            if Natsuki.isAffectionate(higher=True):
                n 1kllunl "..."
                n 1flrajl "Quiero decir, {w=0.1} Me siento halagada, {w=0.1} pero..."
                n 1fcsanl "Uuuuuu...{w=0.3} Sólo detente por ahora, {w=0.1} ¿vale?"
                n 1fllpof "Estás haciendo todo esto súper incómodo..."

    $ jn_compliments.last_compliment_type = jn_compliments.TYPE_BEAUTIFUL
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="¡Me encanta la confianza que tienes en ti misma!",
            label="compliment_confident",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_confident:
    $ Natsuki.calculated_affinity_gain(bypass=get_topic("compliment_confident").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.TYPE_CONFIDENT:
        if Natsuki.isEnamored(higher=True):
            n 1fchbg "Jejeje.{w=0.2} ¡Me alegro de que sigas pensando así,{w=0.1} [player]!"
            n 1uchsm "Eso es lo que significa ser una pro, {w=0.1} ¿verdad?"
            n 1kllss "Jajaja..."

        else:
            n 1fchbg "Jajaja.{w=0.2} ¡Me alegro de que sigas pensando así, [player]!"
            n 1uchsm "Hago lo que puedo, {w=0.1} después de todo."

    else:
        if Natsuki.isEnamored(higher=True):
            n 1fchbg "Jejeje.{w=0.2} Irradio confianza, {w=0.1} ¿no?"
            n 1kllss "..."
            n 1kllsl "Bueno...{w=0.3} a decir verdad,{w=0.1} [player]."
            n 1fcssr "Yo...{w=0.3} realmente...{w=0.3} desearía poder decir que es {i}todo{/i} auténtico."
            n 1kllsr "Pero tenerte aquí conmigo...{w=0.3} me ayuda,{w=0.1} ya sabes.{w=0.2} Mucho."
            n 1klrss "Entonces,{w=0.3} gracias,{w=0.1} [player].{w=0.2} De verdad."

        else:
            n 1uskajl "¿E-{w=0.1}ehh?"
            n 1fchbgl "¡O-{w=0.1}oh!{w=0.2} ¡Pues claro que sí!"
            n 1fcsbgl "Después de todo,{w=0.1} tengo mucho que confiar."
            n 1flrssl "¿No estás de acuerdo?"

            if Natsuki.isEnamored(higher=True):
                n 1uchgnl "Oh,{w=0.1} a quién estoy engañando.{w=0.2} Por supuesto que sí."
                n 1uchbsl "¡Jajaja!"

    $ jn_compliments.last_compliment_type = jn_compliments.TYPE_CONFIDENT
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="¡Creo que eres muy linda!",
            label="compliment_cute",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_cute:
    $ Natsuki.calculated_affinity_gain(bypass=get_topic("compliment_cute").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.TYPE_CUTE:
        if Natsuki.isEnamored(higher=True):
            n 1fskwrl "..."
            n 1fcsanl "..."
            n 1fcsful "..."
            n 1fcsfuf "¡Uh!"
            n 1fbkwrf "Esta bien,{w=0.1} ¡vale!{w=0.2} ¡vale!{w=0.2} Tú ganas,{w=0.1} ¡¿de acuerdo?!"
            n 1fcsemf  "Soy un poco...{w=0.3} quizás...{w=0.3} un poco...{w=0.3} de alguna manera..."
            n 1fsqemf "De una manera abstracta..."
            n 1fsqpuf "...{w=0.3}'linda.'"
            n 1fsqslf "..."
            n 1fcsemf "Listo.{w=0.3} Lo dije, [player].{w=0.3} Lo dije.{w=0.3} {i}Hurra{/i} por tí."
            n 1fsqpof "¿Ya está?{w=0.3} ¿Estás contento?{w=0.3} ¿Estás {i}contento{/i} contigo mismo ahora?"
            n 1flrpof "Dios..."
            n 1fnmpof "Te juro, {w=0.1} que a veces eres tan bobo..."

            if Natsuki.isLove():
                n 1fcsbgf "Además, {w=0.1} Ni siquiera soy la más linda aquí, {w=0.1} d-{w=0.1} de todos modos..."
                $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
                n 1fcssmf "Supongo que dejaré que descubras el resto,{w=0.1} [chosen_tease].{w=0.2} Jejeje."

        else:
            n 1fcsanf "¡Nnnnnnn-!"
            n 1fcsfuf "¡¿Cuántas veces tengo que decir esto,{w=0.1} [player]?!"
            n 1fbkwrf "{i}¡¡No soy linda!!{/i}"
            n 1flremf "Dios..."
            n 1fsqemf "Ahora {i}sé{/i} que querías que dijera eso,{w=0.1} ¿no?"
            n 1flrpof "Realmente ahora...{w=0.3} eres un idiota a veces,{w=0.1} [player]."

            if Natsuki.isAffectionate(higher=True):
                n 1fsqpol "Tienes suerte de estar en mis buenos tiempos."
                n 1fsqbgl "O-{w=0.1} o no sería casi tan paciente.{w=0.2} Jejeje."

    else:
        if Natsuki.isEnamored(higher=True):
            n 1fsqbsl "¡Ja-{w=0.1}jaja!{w=0.2} ¡Nope!"
            n 1fcsbgl "¡Buen intento,{w=0.1} [player]!"
            n 1fchgnl "¡No vas a conseguir que lo diga tan fácilmente!{w=0.2} Jejeje."

        else:
            n 1uskemf "¿Q-{w=0.1}que?{w=0.2} ¡¿Qué acabas de decir?!"
            n 1nllemf "..."
            n 1nlrpuf "..."
            n 1flrbgl "Yo...{w=0.3} debo haberte escuchado mal."
            n 1fcsbgl "S-{w=0.1}sí.{w=0.2} ¡Sí! Te escuché totalmente mal. Al cien porciento."

    $ jn_compliments.last_compliment_type = jn_compliments.TYPE_CUTE
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="Me encanta tu sentido del humor.",
            label="compliment_hilarious",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_hilarious:
    $ Natsuki.calculated_affinity_gain(bypass=get_topic("compliment_hilarious").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.TYPE_HILARIOUS:
        if Natsuki.isEnamored(higher=True):
            n 1uchgn "Jejeje. ¡Gracias, [player]!{w=0.2} Me enorgullezco de eso, {w=0.1} ya sabes."
            n 1fnmbg "Tú tampoco estás mal, {w=0.1} ¿sabes?"
            n 1fwlts "Pero de todos modos{w=0.1} -{w=0.1} Voy a seguir así, {w=0.1} Sólo para ti. Jejeje."

        else:
            n 1uchgn "Jejeje.{w=0.2} Me alegro de que sigas divirtiéndote al escucharme,{w=0.1} [player]."
            n 1fwlts "¡Gracias!{w=0.2} ¡Seguiré así!"

    else:
        if Natsuki.isEnamored(higher=True):
            n 1unmpu "¿Eh?{w=0.2} ¿Tu crees?"
            n 1nllpu "...{w=0.3}¿A decir verdad,{w=0.1} [player]?"
            n 1kllaj "Sinceramente...{w=0.3} me alegra mucho oír eso."
            n 1kllsl "Probablemente sea una tontería, {w=0.1} pero siempre me preocupa que te diviertas aquí."
            n 1klrsl "Yo...{w=0.3} no quiero que te aburras..."
            n 1flrssl "Eso sería súper lamentable."
            n 1kllbol "Así que... {w=0.3} gracias por decírmelo,{w=0.1} [player].{w=0.2} De verdad."
            n 1klrssl "Significa mucho."

        else:
            n 1fcsbgl "¿O-{w=0.1}Oh?{w=0.2} ¡Ah! Bueno, {w=0.1} ¡Me alegro de oírlo!"
            n 1fsqsm "Sabes lo que significa, {w=0.1} ¿verdad?"
            n 1fchgn "¡Significa que tienes buen gusto,{w=0.1} [player]!"
            n 1uchbs "¡Jajaja!"

    $ jn_compliments.last_compliment_type = jn_compliments.TYPE_HILARIOUS
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="¡Eres una inspiración para mí!",
            label="compliment_inspirational",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_inspirational:
    $ Natsuki.calculated_affinity_gain(bypass=get_topic("compliment_inspirational").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.TYPE_INSPIRATIONAL:
        if Natsuki.isEnamored(higher=True):
            n 1fchbg "Jajaja.{w=0.2} Gracias de nuevo por eso,{w=0.1} [player]."
            n 1nllss "Tú tampoco eres una mala inspiración, {w=0.1} ¿sabes?"

        else:
            n 1nchgn "Jejeje.{w=0.2} ¿Qué puedo decir?{w=0.2} ¡Soy una pro,{w=0.1} después de todo!"
            n 1nnmbg "¡Pero gracias,{w=0.1} [player]!"
            n 1fchsm "Me alegro de que sigas encontrando inspiración en ti."

    else:
        if Natsuki.isEnamored(higher=True):
            n 1fskeml "¿E-{w=0.1}eh?{w=0.2} ¿Soy una inspiración para ti?"
            n 1fllbgl "Jajaja...{w=0.3} bueno...{w=0.3} ¡claro que lo soy!"
            n 1kllsr "..."
            n 1kllssl "Aunque me alegro de oírlo, {w=0.1} de todos modos."

        else:
            n 1fskeml "¿E-{w=0.1}eh?{w=0.2} ¿Soy una inspiración para ti?"
            n 1fcsbgl "Bueno...{w=0.3} ¡c-{w=0.1}claro que lo pensarías!"
            n 1fllbgl "Quiero decir, {w=0.1} los modelos a seguir no son mucho mejores que yo, {w=0.1} después de todo."
            n 1uchgn "¿Por qué?{w=0.1} Soy prácticamente una ídolo,,{w=0.1} ¿verdad?{w=0.2} ¡Jajaja!"
            n 1nllss "..."
            n 1knmss "...¿verdad?"

    $ jn_compliments.last_compliment_type = jn_compliments.TYPE_INSPIRATIONAL
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="¡Me encanta tu sentido de la moda!",
            label="compliment_style",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_style:
    $ Natsuki.calculated_affinity_gain(bypass=get_topic("compliment_style").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.TYPE_STYLE:
        if jn_outfits.current_outfit_name != "School uniform":

            # Non-uniform dialogue
            if Natsuki.isEnamored(higher=True):
                n 1fchgn "Jejeje.{w=0.2} ¿Todavía sorprendido por mi sentido de la moda,{w=0.1} [player]?"
                n 1fwlbg "¡No puedes negar que soy una persona elegante!"

                if Natsuki.isLove():
                    $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
                    n 1fllbgl "S-{w=0.1}sin embargo, no creo que sólo me vista para mí,{w=0.1} [chosen_tease]~."
                    n 1nchsml "¡Jajaja!"

            else:
                n 1tsgssl "¿Oh?{w=0.2} Alguien podría tomar algunos puntos, {w=0.1} ¿eh?"
                n 1fsgsm "Jejeje."
                n 1fchbg "¡Relájate,{w=0.1} relájate!{w=0.2} Estoy bromeando,{w=0.1} [player].{w=0.2} No te preocupes."
                n 1fwrsm "¡Pero gracias de nuevo!"

        else:
            # Uniform dialogue
            if Natsuki.isEnamored(higher=True):
                n 1flleml "Quiero decir... {w=0.3} gracias de nuevo,{w=0.1} [player]..."
                n 1fllpol "Pero no es que haya escogido esta ropa yo mismo, {w=0.1} ¿sabes?"
                n 1flrsml "Aunque supongo que una dosis de confianza siempre es bienvenida..."

            else:
                n 1tlrpul "Uh...{w=0.3} bueno...{w=0.3} gracias de nuevo,{w=0.1} ...¿creo?..."
                $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
                n 1fllpol "Aunque al menos podrías guardar los cumplidos para mi propia ropa,{w=0.1} [chosen_tease]..."
                n 1nlrbg "Pero...{w=0.3} Supongo que aprecio el sentimiento.{w=0.2} Jajaja."

    else:

        if jn_outfits.current_outfit_name != "School uniform":
            # Non-uniform dialogue
            if Natsuki.isEnamored(higher=True):
                n 1nchsml "Jejeje.{w=0.2} Estoy feliz de que te guste este atuendo,{w=0.1} [player]!"
                n 1usqsml "Pero entonces... {w=0.3} ¿debería sorprenderme realmente?"
                n 1fllssl "¡Y-{w=0.1}yo {i}soy{/i} quien lo lleva puesto,{w=0.1} d-{w=0.1}después de todo!"

            else:
                n 1fchbgl "¡Ja-{w=0.1}ja!{w=0.2} ¡Me alegro que te guste!"
                n 1fcsbgl "Aunque es natural,{w=0.1} ¿no?{w=0.2} ¡Me gusta enorgullecerme de mi sentido de la moda!"
                n 1fchbg "¡Buen trabajo por notarlo,{w=0.1} [player]!"

        else:
            # Uniform dialogue
            if Natsuki.isEnamored(higher=True):
                n 1tskeml "¿E-{w=0.1}eh?{w=0.2} ¿Te gusta mi sentido de la moda?"
                n 1fllpol "Quiero decir, {w=0.1} no es que pueda hacer mucho estilismo con este tipo de atuendo..."
                n 1flrpol "Pero gracias,{w=0.1} [player]."

            else:
                n 1tskeml "¿Q-{w=0.1}que?{w=0.2} ¿Mi sentido de la moda?"
                n 1fbkeml "¡Pero [player]!{w=0.2} No es que se me haya ocurrido este look a mí."
                n 1fsqpol "..."
                n 1fllpul "A menos que..."
                n 1tnmaj "¿E-{w=0. 1}Estás diciendo que me veo bien con {i}uniforme{/i}?"
                n 1fskemf "..."
                n 1fbkwrf "¡A-{w=0.1}ah!{w=0.2} ¡Asqueroso!{w=0.2} ¡No me gusta en absoluto a dónde va esto!{w=0.2} ¡Es suficiente!"
                $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
                n 1flremf "Dios,{w=0.1} [chosen_tease]..."

    $ jn_compliments.last_compliment_type = jn_compliments.TYPE_STYLE
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._compliment_database,
            prompt="¡Me encanta lo atenta que eres!",
            label="compliment_thoughtful",
            unlocked=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE)
        ),
        topic_group=TOPIC_TYPE_COMPLIMENT
    )

label compliment_thoughtful:
    $ Natsuki.calculated_affinity_gain(bypass=get_topic("compliment_thoughtful").shown_count == 0)

    if jn_compliments.last_compliment_type == jn_compliments.TYPE_THOUGHTFUL:
        if Natsuki.isEnamored(higher=True):
            n 1fcsanl "¡Nnnnn-!{w=0.2} ¿Qué te he dicho,{w=0.1} [player]?"
            n 1kllpol "Yo sólo... {w=0.3} doy lo mejor que tengo, {w=0.1} ¿de acuerdo?"
            n 1knmpol "Dios...{w=0.3} ¿Intentas ponerme en un aprieto o qué?"
            $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES).capitalize()
            n 1klrpo "[chosen_tease]..."
            n 1klrpu "Pero...{w=0.3} Estoy muy contenta de que lo aprecies,{w=0.1} [player]."

            if Natsuki.isLove():
                n 1knmsml "Merece la pena el esfuerzo."

        else:
            n 1fcsanl "Uuuuuh...{w=0.3} Dios,{w=0.1} [player]..."
            n 1fbkeml "¡Ya dije que no era nada! {w=0.2} ¿Intentas ponerme en un aprieto?"
            n 1fllpol "Está bien,{w=0.1} así que...{w=0.3} no te preocupes,{w=0.1} ¿de acuerdo?"
            $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES).capitalize()
            n 1flrpol "[chosen_tease]..."

    else:
        if Natsuki.isEnamored(higher=True):
            n 1klrpol "Honestamente,{w=0.1} [player]...{w=0.2} No te preocupes por eso. ¿De acuerdo?"
            n 1knmpol "Ya has hecho...{w=0.3} mucho por mí..."
            n 1klrnvl "Así que...{w=0.3} Sólo estoy devolviendo el favor,{w=0.1} eso es todo."
            n 1klrssl "Jajaja..."

        else:
            n 1fcsssl "Ah,{w=0.1} cielos,{w=0.1} [player]..."
            n 1fllssl "No es nada, {w=0.1} ¡honestamente!"
            n 1knmpol "Yo-{w=0.1}sólo estoy tratando de ser amigable, {w=0.1}¿sabes?"
            n 1fcsbgl "¡Sí!{w=0.2} No hay ningún tratamiento especial aquí.{w=0.2} ¡Nope!"

    $ jn_compliments.last_compliment_type = jn_compliments.TYPE_THOUGHTFUL
    return
