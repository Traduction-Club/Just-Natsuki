default persistent._topic_database = dict()

# Generic
default persistent._jn_out_of_topics_warning_given = False

# Pet data
default persistent.jn_player_pet = None

# Seasonal data
default persistent.jn_player_favourite_season = None

# Appearance data
default persistent.jn_player_appearance_declined_share = False
default persistent.jn_player_appearance_eye_colour = None
default persistent.jn_player_appearance_hair_length = None
default persistent.jn_player_appearance_hair_colour = None
default persistent.jn_player_appearance_height_cm = None

# Hobby data
default persistent.jn_player_gaming_frequency = None
default persistent.jn_player_can_drive = None

# Romance data
default persistent.jn_player_love_you_count = 0

init python in topics:
    import store
    TOPIC_MAP = dict()

# Special dialogue for when out of random topics
label talk_out_of_topics:
    if Natsuki.isNormal(higher=True):
        n 1kllpo "Uhmm..."
        n 1knmaj "Oye...{w=0.5}{nw}"
        extend 1knmss " ¿[player]?"
        n 1fslss "Estoy...{w=0.3} esforzándome por pensar en más cosas de las que quiero hablar."
        n 1ulraj "Así que...{w=0.5}{nw}"
        extend 1nsrss " No creo que vaya a hablar mucho hasta que se me ocurra algo más."
        n 1nsrpo "..."
        n 1tnmem "¿Qué?{w=0.5}{nw}"
        extend 1fllpol " No hablo sólo porque me gusta el sonido de mi propia voz, {w=0.1} ¿sabes?"
        n 1tllpu "Pero...{w=0.5}{nw}"
        extend 1unmbo " Supongo que {i}podría{/i} hablarte de lo que se me ocurra."
        n 1nchbg "Entonces...{w=0.3} ¿Qué te parece esto?"

        menu:
            n "¿Te importa si repito algunos temas?"

            "Claro, no me molesta escucharte.":
                $ persistent.jn_natsuki_repeat_topics = True
                n 1uchgn "¡Muy bien!{w=0.5}{nw}"
                extend 1tcsaj " Ahora,{w=0.1} dejame pensar..."

            "Preferiría esperar.":
                n 1tllaj "Bueno...{w=0.5}{nw}"
                extend 1tnmbo " si estás seguro de ello."

                if Natsuki.isAffectionate(higher=True):
                    n 1kwmpol "Intentaré que se me ocurra algo pronto,{w=0.5}{nw}"
                    extend 1klrssl " ¿vale?"

                else:
                    n 1flrpol "S-{w=0.1}solo no hagas el silencio más incómodo,{w=0.1} ¡¿entendido?!"

    elif Natsuki.isDistressed(higher=True):
        n 1nllsf "..."
        n 1fllaj "Sí, {w=0.1} bueno.{w=0.5}{nw}"
        extend 1fnmsl " No tengo nada más que decir."
        n 1fsqpu "...O cosas que quiera contarte a {i}tí{/i},{w=0.1} de todos modos."
        n 1fslsr "Así que me voy a callar."
        n 1fcsun "Je.{w=0.5}{nw}"
        extend 1fsqun " No es que eso sea un {i}problema{/i} para ti, {w=0.1} ¿eh?"

    else:
        n 1fslun "...{w=2}{nw}"
        extend 1fsqem " ¿Qué?"
        n 1fcsan "Eres la {i}última{/i} persona con la que quiero pensar en más cosas para hablar.{w=1}{nw}"
        extend 1fsrem " Tarado."

    $ persistent._jn_out_of_topics_warning_given = True
    return

# Talk menu topics

# Natsuki's thoughts on having her picture taken via the ingame screenshot system
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_having_pictures_taken",
            unlocked=True,
            prompt="¿Qué te parece que te tomen una foto?",
            category=["Natsuki", "Fotografía", "Vida"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_having_pictures_taken:

    if not persistent.jn_first_screenshot_taken:
        n 1uskwr "E-espera...{w=0.3} ¿Me estás diciendo que hay una cámara aquí?{w=0.2}"
        extend 1fbkwr " ¡¿Estás bromeando?!"
        n 1kbktr "Uuuuh-"
        n 1kslaj "Nunca me ha gustado que me fotografíen sin mi permiso..."
        n 1ksgsl "Sólo...{w=0.3} por favor no me saques fotos a menos que te lo diga,{w=0.1} ¿de acuerdo [player]?{w=0.2}"
        extend 1kllsl " Significaría mucho para mí."
        n 1kllsf "Espero que lo entiendas."

    else:
        if Natsuki.isEnamored(higher=True):
            n 1tnmsf "¿Hmm?{w=0.2} ¿Fotos mías?"
            n 1nllsl "Honestamente,{w=0.1} No creo que nunca me sienta completamente cómoda con ellas..."
            n 1unmss "¡Pero confío en que tomes una buena foto!"
            n 1fcsbg "Mientras preguntes,{w=0.1} ¡no tengo ningún problema con ello!"

        elif Natsuki.isNormal(higher=True):
            if jn_screenshots.are_screenshots_blocked():
                n 1fsqpu "¿Es en serio,{w=0.1} [player]?{w=0.1} ¿Me estás preguntando por esto {i}ahora{/i}?"
                n 1fslaj "Sabes {i}perfectamente{/i} lo que pienso de esto."
                n 1fsgbo "No te odio,{w=0.1} pero por favor, trata de recordar cómo me siento antes de hacer cosas como esa."
                n 1ncssl "Yo... {w=0.3} todavía voy a mantener eso apagado por ahora, {w=0.1} de todos modos."

            else:
                n 1ncuaj "¿E-{w=0.1}Ehh?{w=0.2} ¿Fotos mías?"
                n 1nlrsr "No soy aficionada,{w=0.1} honestamente-{w=0.1} pero eso ya lo sabías,{w=0.1} [player]."
                n 1knmpu "Es sólo que..."
                n 1kcspu "Realmente...{w=0.3} necesito...{w=0.3} mi privacidad.{w=0.1} Me importa mucho."
                n 1kwmpu "Entiendes,{w=0.1} ¿verdad?"
                n 1knmnv "Así que... {w=0.3} si alguna vez quieres tomar una foto, {w=0.1} ¿puedes preguntarme primero?"
                menu:
                    n "¿Lo harías por mí?"

                    "¡Por supuesto!":
                        n 1kcssg "Gracias,{w=0.1} [player]."
                        n 1knmss "Eso realmente...{w=0.3} significa mucho para mí."

                    "Lo pensaré.":
                        n 1fwmsf "[player]...{w=0.3} Por favor.{w=0.1} Estoy hablando en serio."
                        extend 1fllsl " No me molestes de esa manera."
                        n 1nnmaj "Asegúrate de preguntar,{w=0.1} ¿de acuerdo?"

                    "...":
                        n 1nunfr "..."
                        n 1fnmaj "[player].{w=0.2} Esto no es gracioso."
                        n 1fllsl "Sólo asegúrate de preguntar."

        elif Natsuki.isDistressed(higher=True):
            n 1fsqsl "...Fotos,{w=0.1} ¿[player]?{w=0.2} ¿En serio?"
            n 1fsqaj "No creo que quiera que me saques una foto,{w=0.1} [player]."
            n 1fslfr "Hablemos de otra cosa."

        else:
            n 1kplpu "Ni siquiera {i}intentes{/i} fingir que te importa lo que siento por las fotos."
            n 1kcssr "Hemos terminado aquí,{w=0.1} [player]."
    return

# Natsuki discusses her lack of pet with the player, and asks about theirs
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_did_you_have_pets",
            unlocked=True,
            prompt="¿Has tenido alguna vez mascotas?",
            category=["Vida", "Animales", "Familia"],
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_did_you_have_pets:

    # Check to see if the player and Natsuki have already discussed this
    $ already_discussed_pets = get_topic("talk_did_you_have_pets").shown_count > 0

    if already_discussed_pets:
        n 1tnmsl "Espera... {w=0.3}¿no hemos hablado de esto antes?{w=0.1} [player]?"
        n 1unmsl "Bueno, de todos modos,{w=0.1} no ha cambiado mucho."
        n 1ullsl "Todavía no tengo una mascota,{w=0.1} por mucho que lo desee."
        n 1nnmsm "Tal vez debería conseguir una pronto. {w=0.2} Hmm..."

    else:
        n 1tnmsl "¿Eh?{w=0.2} ¿Que si he tenido alguna vez mascotas?"
        n 1fllaj "Ya sabes,{w=0.1} realmente me gustaría tener una. {w=0.1} ¡Pero nunca me permitieron nada!"
        n 1fsgpo "Siempre se hablaba del lío que iba a suponer,{w=0.1} o de lo que iba a costar,{w=0.1} o de literalmente de cualquier otra cosa que se les ocurriera..."
        n 1fnmaj "¡Incluso cuando {i}dije{/i} que me encargaría de todo!"
        n 1fslem "Agh..."
        n 1fslun "Aún me molesta...{w=0.3}{nw}"
        extend 1uchgn " pero entonces, {w=0.1} no es como si no pudiera tener una mascota aquí dentro, {w=0.1} ¿verdad?{w=0.1} Jejeje."

    if persistent.jn_player_pet is None:
        n 1unmbg "Pero, ¿qué hay de ti,{w=0.1} [player]?"
        menu:
            n "¿Tienes mascotas?"

            "Sí, sí tengo.":
                n 1uspaw "¡Oh!{w=0.2} ¡Oh oh oh!{w=0.2} ¡Tienes que decirme,{w=0.1} [player]!"
                n 1uspbs "¿Qué mascota tienes?{w=0.2} ¿Qué mascota tienes?"
                call pet_options_a

            "No, no tengo.":
                n 1usgem "Aww...{w=0.3} Debo admitir,{w=0.1} Estoy un poco decepcionada."
                n 1nchbg "Bueno, {w=0.1} ¡entonces tienes que avisarme si consigues una,{w=0.1} [player]!"
                n 1uchgn "¡Quiero escucharlo todo!"

            "Solía tener":
                n 1kplaj "Oh...{w=0.3} oh por Dios."
                n 1kllbo "Siento mucho oír eso,{w=0.1} [player]."
                n 1knmbo "Espero que lo estés llevando bien ahora."
                n 1kcsbo "..."
                n 1knmbo "Yo...{w=0.3} creo que deberíamos hablar de otra cosa, ¿está bien?"

    else:
        n 1unmbs "¿Que hay de ti,{w=0.1} [player]?"
        menu:
            n "¿Conseguiste una nueva mascota?"

            "Sí, lo hice.":
                n 1uspaw "Ooh...{w=0.3} ¡Tienes que decirme!{w=0.2} ¿Qué conseguiste?"
                call pet_options_a

            "No, no lo he hecho..":
                n 1usgem "Aww...{w=0.3} Debo admitir,{w=0.1} Estoy un poco decepcionada."
                n 1nchbg "Bueno,{w=0.1} ¡entonces tienes que avisarme si consigues una,{w=0.1} [player]!"
                n 1uchgn "¡Quiero escucharlo todo!"

            "Perdí una.":
                n 1knmaj "Oh...{w=0.3} oh Dios..."
                n 1knmfr "Lo siento mucho,{w=0.1} [player].{w=0.2} ¿Estás bien?"
                n 1kllbo "Tal vez deberíamos hablar de otra cosa para mantener tu mente fuera de eso..."
                if Natsuki.isAffectionate(higher=True):
                    n 1knmbo "Estoy aquí para ti,{w=0.1} [player]."

    return

label pet_options_a:
    menu:
        n "¿Qué has conseguido?"

        "Un ave":
            n 1uchgn "¡Oh!{w=0.2} ¡Genial!"
            n 1nnmsm "No creo que yo tenga aves, {w=0.1} ¡pero seguro que alegran las habitaciones!"
            n 1tnmaj "No es demasiado ruidoso para ti,{w=0.1} ¿espero?"
            n 1uchsm "Sin embargo, estoy segura de que los tuyos aprecian tu compañía."
            $ persistent.jn_player_pet = "birds"

        "Un gato":
            n 1uchsm "¡Yay!{w=0.2} ¡Gatos!"
            n 1uchgn "Realmente me gustaría tener uno,{w=0.1} ¡me encanta ver todas las situaciones tontas en las que se meten!"
            n 1unmbs "Espero que no hayas dicho eso porque a {i}mi{/i} me gusten,{w=0.1} sin embargo.{w=0.5}{nw}"
            extend 1uchsm " Jejeje."
            n 1tnmsm "¡Sólo no lo mimes demasiado,{w=0.1} [player]!"
            $ persistent.jn_player_pet = "cats"

        "Un camaleón.":
            n 1unmaj "¡Oh!{w=0.2} ¡Camaleones!"
            n 1uchgn "¡Eso está súper bien,{w=0.1} [player]!"
            n 1unmbg "El cambio de color es suficientemente loco,{w=0.1} pero esos ojos también{w=0.1} -{w=0.1} ¡es como si alguien los hubiera fabricado!"
            n 1uchgn "Sin embargo{w=0.1} -{w=0.1} ¡eso es impresionante!"
            n 1unmbg "Será mejor que lo cuides bien,{w=0.1} ¿de acuerdo?"
            $ persistent.jn_player_pet = "chameleons"

        "Un perro.":
            n 1uwdaj "¡Oh!{w=0.2} ¿Un perro?{w=0.5}{nw}"
            extend 1uchbs " ¡Increíble!"
            n 1nnmsm "No creo que un perro sea mi primera opción,{w=0.1} con todos los paseos y todo eso."
            n 1uchbs "¡Pero no puedo pensar en una mascota más cariñosa!"
            n "¡Espero que el tuyo te cuide tanto como tú lo haces!"
            $ persistent.jn_player_pet = "dogs"

        "Un hurón":
            n 1unmlg "¡Oh!{w=0.2} ¿Un hurón?"
            n 1uchbs "¡Eso es {i}adorable{/i}!"
            n 1tllbg "Pero...{w=0.3} Siempre me he preguntado.{w=0.5}{nw}"
            n 1tchbg " ¿Se parecen más a un gato,{w=0.1} o a un perro?"
            n 1flrss "Bueno,{w=0.1} como sea. {w=0.2}De cualquier manera,{w=0.1} [player]..."
            n 1unmlg "¡Será mejor que cuides bien al pequeño!"
            $ persistent.jn_player_pet = "ferrets"

        "Más...":
            call pet_options_b

    return

label pet_options_b:
    menu:
        n "¿Qué has conseguido?"

        "Un pez":
            n 1unmaj "¡Ooh!{w=0.2} ¡Los peces son interesantes!"
            n 1kllnv "Personalmente no creo que sean súper cariñosos..."
            n 1uchgn "¡Pero creo que son una buena manera de aliviar el estrés!{w=0.2} Deben ser tranquilos para ver en su propio pequeño mundo."
            n 1nsqsm "Apuesto a que sientes que podrías perderte en ese tanque.{w=0.5}{nw}"
            extend 1nchsm " Jejeje."
            $ persistent.jn_player_pet = "fish"

        "Una rana":
            n 1kspaw "¡Ooh!{w=0.2} ¡Ranas!"
            extend 1kspbs " ¡Qué bonito!"
            n 1fsqsm "En serio, no me canso de ver sus caras.{w=0.5}{nw}"
            extend 1fbkbs " ¡Siempre parecen tan confusas!"
            n 1fllbg "Jejeje.{w=0.2} Bueno,{w=0.1} [player]..."
            n 1fchgn "¡Más vale que {i}saltes{/i} a ello y cuides la tuya!"
            $ persistent.jn_player_pet = "frogs"

        "Un jerbo":
            n 1kspaw "¡Awww!{w=0.2} ¡Me gustan los jerbos!"
            n 1uchbs "Es muy bonito cómo viven en pequeños grupos para hacerse compañía."
            n 1unmbs "Son buenos para cavar,{w=0.1} también{w=0.1} -{w=0.1} ¡son muy buenos!"
            n "Cuida bien del tuyo por mí, {w=0.1} ¿vale?"
            $ persistent.jn_player_pet = "gerbils"

        "Una cobaya":
            n 1unmaj "¡Ooh!{w=0.2} ¡Me gustan las cobaya!"
            n 1uchbs "No sé mucho sobre ellos,{w=0.1} pero me encantan los pequeños sonidos que hacen."
            n "¡Es como si siempre estuvieran conversando!"
            n 1unmbs "Cuida bien del tuyo por mí,{w=0.1} ¿vale?"
            $ persistent.jn_player_pet = "guinea pigs"

        "Un hamster":
            n 1uspbs "¡Oh, dios mío!{w=0.2} ¡Hamsters!"
            n 1uchbs "¡Aaaaaah!{w=0.2} ¡Me encantan!"
            n 1uspbs "Me encantan sus colitas,{w=0.1} y sus patitas,{w=0.1} y sus bigotes,{w=0.2} y-"
            n "¡Y!{w=0.2} Y..."
            n 1uwdbol "..."
            n 1uchbsl "¡Ja-{w=0.1}jaja!{w=0.2} Parece que me he dejado llevar un poco..."
            n 1uchgnf "..."
            n 1fllgnf "Será mejor que cuides el tuyo por mí, {w=0.1} ¿de acuerdo?"
            $ persistent.jn_player_pet = "hamsters"

        "Más...":
            call pet_options_c

        "Atrás...":
            call pet_options_a

    return

label pet_options_c:
    menu:
        n "¿Qué has conseguido?"

        "Un caballo":
            n 1uspaw "¡G-{w=0.1}guau!{w=0.2} No estás bromeando conmigo, {w=0.1} ¡¿verdad?!"
            n 1uspbs "¡¿Un caballo?!{w=0.2} ¡Eso es increible,{w=0.1} [player]!"
            n 1uchbs "¡Tienes que enseñarme a montar algún día!"
            n 1uchbs "Asegúrate de visitar el tuyo a menudo, {w=0.1} ¿de acuerdo?"
            n 1unmlg "Oh -{w=0.2} ¡y lleva un casco si vas a montar!"
            $ persistent.jn_player_pet = "horses"

        "Un insecto":
            n 1twmsc "Ack-{nw}"
            n 1kslup "Nnnnn..."
            n 1kwmsg "...Me gustaría poder compartir tu entusiasmo.{w=0.5}{nw}"
            extend 1kllss " Jajaja..."
            n 1ksqun "No creo que yo misma pueda soportar a los bichos raros."
            n 1ksrun "Ciertamente tienes un...{w=0.3} gusto interesante,{w=0.1} [player]."
            n 1kwmss "¡Pero estoy segura de que cuidas mucho el tuyo!"
            $ persistent.jn_player_pet = "insects"

        "Una lagartija":
            n 1uchgn "¡Ooh!{w=0.2} Lagartijas,{w=0.1} ¿eh?"
            n 1fsqss "...Confío en que no tengas la misma sangre fría,{w=0.1} [player]."
            n 1fchgn "...¡Pffffft!{w=0.5}{nw}"
            extend 1uchlg " ¡Estoy bromeando, [player]!{w=0.2} ¡Sólo estoy bromeando!"
            n 1unmbg "Sin embargo, ¡los animales tienen un aspecto genial!{w=0.2}"
            extend 1tllbg " Creo que es difícil encontrar un tipo de mascota más variado."
            n 1uchgn "¡Será mejor que mantengas el tuyo bien calentito,{w=0.1} [player]!"
            $ persistent.jn_player_pet = "lizards"

        "Un ratón":
            n 1uchgn "Jejeje.{w=0.2} ¡Los ratones son adorables!"
            n 1nllaj "Todavía no estoy segura de cómo me siento con la cola..."
            n 1unmbg "¡Pero son tan curiosos y sociables!{w=0.2} Me encanta verlos jugar juntos."
            n 1uchgn  "Asegúrate de cuidar el tuyo por mí,{w=0.1} ¿de acuerdo?"
            $ persistent.jn_player_pet = "mice"

        "Una rata":
            n 1unmbs "Ratas,{w=0.1} ¿eh?"
            n 1fsgsg "¿Esperabas que me diera asco?"
            n 1uchbs "¡Jajaja!"
            n 1unmsm "Las ratas están bien.{w=0.2} ¡Son sorprendentemente inteligentes,{w=0.1} también!"
            n 1uchgn "¿Acaso estás entrenando a la tuya,{w=0.1} [player]?{w=0.2} Jejeje."
            n 1unmbs "Asegúrate de cuidar la tuya por mí,{w=0.1} ¿de acuerdo?"
            $ persistent.jn_player_pet = "rats"

        "Más...":
            call pet_options_d

        "Atrás...":
            call pet_options_b

    return

label pet_options_d:
    menu:
        n "¿Qué has conseguido?"

        "Un conejo":
            n 1kspaw "¡Awwwwww!{w=0.2} ¡Conejitos!"
            n 1kcuaw "¡Son tan lindos!{w=0.2} ¡Me encantan!"
            n 1uchbs "Especialmente los que tienen las orejas caídas,{w=0.1} ¡parecen tan adorables!"
            n 1knmbo "Aunque es una pena{w=0.1} que necesiten tanto espacio."
            n 1uchgn "¡Pero estoy segura de que el tuyo tiene mucho espacio para moverse!{w=0.2} Jejeje."
            $ persistent.jn_player_pet = "rabbits"

        "Una serpiente":
            n 1uskaj "¿E-{w=0.1}Eh?{w=0.5}{nw}"
            extend 1uscem " ¿S-{w=0.1}serpientes?"
            n 1fcsun "Uuuuuuh..."
            n 1kcsaj "...Bien.{w=0.2} Voy a ser sincera contigo, [player].{w=0.5}{nw}"
            extend 1kllsl " Yo... {w=0.3} no soy muy buena con ellas."
            n 1kllaj "S-{w=0.1}serpientes,{w=0.1} quiero decir."
            n 1kllsl "Es que...{w=0.3} no están muy de acuerdo conmigo.{w=0.2} No sé por qué."
            n 1fcsgsl "¡P-{w=0.1}pero eso no quiere decir que {i}no puedan{/i} ser lindas,{w=0.1} obviamente!{w=0.5}{nw}"
            extend  1flrpo " Hacer esa suposición sería simplemente ignorante."
            n 1ksrpo "...Y merecen cuidados como cualquier otra mascota.{w=0.5}{nw}"
            extend 1flraj " Entonces..."
            n 1fnmpo "¡Será mejor que no te dejes engañar por la tuya,{w=0.1} [player]!"
            $ persistent.jn_player_pet = "snakes"

        "Otra mascota.":
            n 1unmaj "¡Ooh!{w=0.2} Un propietario exótico, ¿verdad?"
            n 1tsgsg "Me pregunto si eso dice algo sobre el resto de tus gustos.{w=0.2} Jejeje."
            n 1uchgn "Confío en que cuides bien de la tuya.{w=0.1} ¡Las mascotas poco comunes pueden ser bastante exigentes!"
            $ persistent.jn_player_pet = "something_else"

        "Atrás...":
            call pet_options_c

    return


# Natsuki discusses service animals with the player, in particular emotional support animals
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_service_animals",
            unlocked=True,
            prompt="Animales de apoyo",
            category=["Animales"],
            nat_says=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_service_animals:
    n 1ullbo "Hmm..."
    n 1unmaj "Oye [player],{w=0.1} ¿has oído hablar de los animales de apoyo?"
    n 1unmbg "Son como animales que la gente entrena especialmente para hacer trabajos que los humanos no pueden hacer fácilmente."

    if Natsuki.isNormal(higher=True):
        n 1unmbs "Algunos trabajan en los aeropuertos para mantener la seguridad de la gente, {w=0.1} otros ayudan en los rescates...{w=0.3} ¡es súper genial!"
        n 1uwmsm "Pero hay un tipo que es especialmente impresionante..."
        n 1uchgn "¡Animales de apoyo emocional!"
        n 1ullaj "Son como mascotas muy mansas que se utilizan para consolar a las personas que pasan por un mal momento."
        n 1ulraj "¡También los hay de todas las formas y tamaños!{w=0.5}{nw}"
        n 1nnmpu " Perros y gatos -{w=0.5}{nw}"
        extend 1fslss " {i}obviamente{/i}{w=0.5}{nw}"
        extend 1uwdgs " -{w=0.2} ¡pero incluso los caballos a veces!"
        n 1fchbg "Impresionante, {w=0.1} ¿verdad?"
        n 1kllss "..."
        n 1ulrbo "..."
        n 1uplaj "Sabes,{w=0.1} [player]..."
        n 1kcsaj "A veces me pregunto si uno podría haber ayudado a Sayori..."
        n 1klrfr "...pero intento no pensar demasiado en eso."
        n 1knmem "{i}Son{/i} grandiosos,{w=0.1} pero no hacen milagros."
        n 1kwmem "[player]...{w=0.3} Realmente espero que nunca tengas que buscar su ayuda."
        n 1kwmnv "Y en ese sentido, {w=0.1} si necesitas apoyo..."

        if Natsuki.isAffectionate(higher=True):
            n 1fcssrl "Y-{w=0.2}Yo quiero que sepas que puedes confiar en mí.{w=0.1} ¿de acuerdo?"

            if Natsuki.isLove():
                n 1kwmnv "Te amo,{w=0.1} [player]."
                return

        else:
            n 1fcssrl "Solo...{w=0.5}{nw}"
            extend 1fnmsl " no te hagas el tonto,{w=0.1} [player].{w=0.5}{nw}"
            extend 1kllss " Puedo escucharte si lo necesitas."
            n 1fcsajl "¡N-{w=0.1}no soy una idiota!{w=0.5}{nw}"
            extend 1flrpol " Es lo mínimo que se puede hacer,{w=0.1} eso es todo."

    else:
        n 1unmbo "Trabajan en un montón de lugares.{w=0.2} Aeropuertos, rescates y esas cosas,{w=0.1} normalmente."
        n 1unmss "Pero me gustan mucho los animales de apoyo emocional."
        n 1nnmsl "Son como mascotas especialmente domesticadas que se utilizan para consolar a quienes lo están pasando mal."
        n 1nsgbo "..."
        n 1nsgaj "Y...{w=0.3} para ser totalmente honesta..."
        n 1fcsun "A veces siento que me vendría bien uno."
        return

    n 1ksrfr "..."
    n 1kwmfr "Esto se puso un poco complicado,{w=0.1} ¿no?"
    n 1kwmbg "Bueno, {w=0.1} basta de eso.{w=0.2}"
    extend 1uwmss " ¿De qué más quieres hablar?"

    return

# Natsuki highlights her concern for her player using their computer for long periods of time, and offers her wisdom
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_using_computers_healthily",
            unlocked=True,
            prompt="Utilizar las computadoras de forma saludable",
            conditional="store.jn_utils.get_current_session_length().total_seconds() / 3600 >= 8",
            category=["Vida", "TÚ", "Salud"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_using_computers_healthily:
    n 1unmaj "Eh."
    n 1tnmaj "Oye,{w=0.1} [player].{w=0.2} Se me acaba de ocurrir algo."
    n 1unmsf "Tienes que estar en tu ordenador para hablar conmigo,{w=0.1} ¿verdad?"
    n 1ullsf "Y ya llevas un tiempo aquí..."

    if (jn_activity.has_player_done_activity(jn_activity.JNActivities.work_applications)
        or jn_activity.has_player_done_activity(JNActivities.artwork)
        or jn_activity.has_player_done_activity(JNActivities.coding)):
            n 1knmaj "De hecho, ¡incluso te he {i}visto{/i} trabajar en un montón de cosas!"
            n 1kllsl "..."

    n 1nchgn "Muy bien,{w=0.1} ¡eso es!{w=0.2} Lo he decidido."
    n 1uchgn "Te voy a dar una pequeña lección sobre cómo usar el ordenador de forma correcta."
    n 1nnmss "Número uno:{w=0.2} ¡postura!"
    n 1fwmlg "Siéntese recto,{w=0.1} y con la espalda apoyada en la silla,{w=0.1} [player].{w=0.2}"
    extend 1uchlg " ¡Lo digo en serio!"
    n 1tnmlg "No quieres problemas de espalda,{w=0.1} ¿verdad?"
    n 1nnmsm "Asegúrate de que tus pies todavía pueden tocar el suelo,{w=0.1} sin embargo.{w=0.2}"
    extend 1uchgn " ¡Incluso yo puedo hacerlo!"
    n 1nnmaj "Número dos:{w=0.2} ¡distancia!"
    n 1nsggn "Sé que no te cansas de verme,{w=0.1}"
    extend 1fnmpo " pero no quiero verte presionando tu cara contra la pantalla.{w=0.2} Es raro."
    n 1uchgn "Así que asegúrate de sentarte a un brazo de distancia de la pantalla,{w=0.1} ¿de acuerdo?"
    n 1uwdaj "¡Oh!{w=0.2} Pero no olvides tener tus cosas al alcance de la mano{w=0.1} -{w=0.1}"
    extend 1unmsm " como tu ratón."
    n 1unmbg "Número tres:{w=0.2} ¡descansos!"
    n 1uwmbg "No sé tú, {w=0.1} pero yo me pongo nerviosa si me quedo quieta mucho tiempo..."
    n 1fchgn "¡Así que asegúrate de mover el culo y hacer algunos estiramientos varias veces por hora!"
    n 1fsqsg "Incluso podrías conseguir agua o algo así si {i}realmente{/i} necesitas una excusa para moverte."
    n 1nnmsm "Además, así los ojos descansan de la pantalla."
    n 1uchbs "¡Bien{w=0.1} -{w=0.1} y la última! {w=0.2} Este es importante,{w=0.1}"
    extend 1uchgn " así que ¡escucha bien!"
    n 1unmbo "Si alguna vez te sientes mal{w=0.1} - {w=0.1}como sentir que te duele la espalda,{w=0.1} o te duelen los ojos o algo..."
    n 1nwmbo "Por favor, deja de hacer lo que sea que estés haciendo.{w=0.2} Tu salud es lo primero.{w=0.2} No me importa lo que haya que hacer."
    n 1unmsm "Tómate un tiempo para sentirte mejor, {w=0.1} y luego asegúrate de que todas tus cosas están bien configuradas como he dicho."
    n "No continúes hasta que te sientas lo suficientemente bien.{w=0.1} -{w=0.1} ¡habla con alguien si es necesario!"
    n 1uchgn "¡Okaaay!{w=0.2} ¡Okaaay! ¡La conferencia ha terminado!"
    n 1ullaj "Guau...{w=0.3} He divagado un poco, {w=0.1} ¿no es así?{w=0.2}"
    extend 1klrbgl " ¡Lo siento,{w=0.1} lo siento!{w=0.2} Jejeje."

    if Natsuki.isEnamored(higher=True):
        n 1kwmsml "Pero sabes que sólo hago estas cosas porque realmente me importas,{w=0.1} [player]...{w=0.3} ¿de acuerdo?"
        n 1kwmnvl "Así que por favor...{w=0.3} cuídate, ¿de acuerdo?{w=0.2} No quiero que sufras por mi culpa."

        if Natsuki.isLove():
            $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
            n 1kwmsml "Te amo,{w=0.1} [chosen_endearment]."
            n 1kwmnvl "..."
            return

    else:
        n 1usglg "Pero sabes que sólo digo estas cosas porque me importas."
        n 1nsqpo "...y no quiero que te quejes de que te duele la espalda.{w=0.2}"

    n 1nchgn "Jajaja...{w=0.3} ahora, ¿dónde estábamos?"
    return

# Natsuki highlights the importance of staying active and getting exercise
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_staying_active",
            unlocked=True,
            prompt="Mantenerse activo",
            conditional="persistent.jn_total_visit_count >= 10",
            category=["Vida", "TÚ", "Salud"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_staying_active:
    n 1nnmbo "Oye,{w=0.1} [player]..."
    n 1nllsr "Deberías salir más."
    n 1fsqsm "..."
    n 1fchbg "¡Jajaja!{w=0.2} ¡No,{w=0.1} de verdad!{w=0.2} ¡Te lo digo en serio!"
    n 1ulraj "En la escuela,{w=0.1} era súper fácil hacer ejercicio ya que teníamos que ir andando a todas partes,{w=0.1} y teníamos deportes y tal..."
    n 1nsqsf "Sin embargo, no es tan sencillo cuando tienes un trabajo {w=0.1}y otras cosas de las que preocuparte."
    n 1fllss "No voy a mentir y decir que hice ejercicio o algo así..."
    n 1ullaj "Pero intenté dar algunos paseos cuando pude.{w=0.5}{nw}"
    extend 1uchgn " ¡Cualquier excusa para ir a la librería es motivo suficiente para mí!"
    n 1kslsl "...O {i}era{/i} razón suficiente, al menos."
    n 1fllaj "Pero aún así {w=0.1}-{w=0.5}{nw}"
    extend 1unmbg " ¡también deberías intentarlo,{w=0.1} [player]!"
    n 1nlrss "No tiene que ser una excursión o algo loco{w=0.1} -{w=0.3}{nw}"
    extend 1nnmsm " se trata más bien de mantenerse en ello,{w=0.1} realmente."
    n 1fchsm "Incluso un paseo diario de diez minutos te ayudará a sentirte renovado y despierto."
    n 1ullaj "Así que...{w=0.5}{nw}"
    extend 1fnmss " asegúrate de salir pronto,{w=0.1} [player]."

    if Natsuki.isEnamored(higher=True):
        n 1fchbg "¡Quiero verte poniendote en forma!{w=0.5}{nw}"
        extend 1uchsm " Jejeje."
        return

    n 1fchbg "¡Es lo mínimo que puedes hacer!"
    return

# Natsuki discusses stress and offers ways she finds useful to deal with it
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_relieving_stress",
            unlocked=True,
            prompt="Aliviar el estrés",
            category=["Vida", "TÚ", "Salud"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_relieving_stress:
    n 1ullaj "Sabes, {w=0.1}lo admito,{w=0.1} [player]."
    n 1flrbg "Yo...{w=0.3} como que soy de mecha corta.{w=0.5}{nw}"
    extend 1klrss " Jejeje."
    n 1fnmss "Sin embargo, he intentado trabajar en ello,{w=0.3}{nw}"
    extend 1fchbg " y me encantaría compartir algunas de las formas en las que afronto el estrés."
    n 1unmss "Personalmente, {w=0.1} creo que la mejor manera de lidiar con ello, si se puede, es tratar de crear algo de reposo."
    n 1nslss "Antes de todo... {w=0.3} esto,{w=0.5}{nw}"
    extend 1nllss " si las cosas se ponen un poco difíciles,{w=0.1} salía si podía."
    n 1unmbo "Un poco de aire fresco y un cambio de ambiente pueden poner las cosas en su lugar.{w=0.5}{nw}"
    extend 1fwdaj " ¡Es muy efectivo!"
    n 1ulraj "Pero no sólo crea distancia física,{w=0.1} supngo.{w=0.5}{nw}"
    extend 1fnmpu " ¡Distancia también mental!"
    n 1ncssr "Si hay algo que te estresa, {w=0.1} tienes que dejar de prestarle atención."
    n 1fslpo "Ahora no puedo salir,{w=0.5}{nw}"
    extend 1nllsf " así que solo leo algo, {w=0.1} o veo algunos videos tontos."
    n 1fchbg "Pero haz lo que te funcione; {w=0.1}todos tenemos nuestras propias zonas de confort."
    n 1fslpo "Y-{w=0.1}y por supuesto, {w=0.1} siempre puedes venir a verme, {w=0.1} ya sabes..."
    n 1fchbgl "¡D-{w=0.1}de todos modos!"
    n 1unmpu "La cuestión es intentar volver siempre con la cabeza fria,{w=0.3}{nw}"
    extend 1nnmss " y no te preocupes por las cosas pequeñas."
    n 1tnmss "Puedes manejar eso,{w=0.1} ¿verdad, [player]?"
    n 1uchsm "¡Seguiré trabajando en ello si lo haces!"
    return

# Natsuki muses on how easy it is to waste money, and offers some guidance on spending wisely
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_careful_spending",
            unlocked=True,
            prompt="Gastar con cuidado",
            category=["Vida", "TÚ", "Salud", "Sociedad"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_careful_spending:
    n 1tllsr "..."
    n 1fllsr "..."
    n 1tnmpu "¡Hmm...?"
    n 1uwdgs "¡O-{w=0.1}oh!{w=0.5}{nw} "
    extend 1flrbg " ¡Ja-{w=0.1}jaja!{w=0.5}{nw}"
    extend 1flrdvl " ¡Me he despistado!"
    n 1unmaj "Estaba pensando..."
    n 1flrbo "Hoy en día es muy fácil gastar más de lo que se quiere, {w=0.1} ¿sabes?"
    n 1flrpu "Como...{w=0.3} parece que donde quiera que mires,{w=0.1} hay un descuento,{w=0.1} o ofertas,{w=0.1} o algún tipo de trato especial..."
    n 1unmpu "Y cada lugar acepta todo tipo de formas de pago, {w=0.1} también.{w=0.5}{nw}"
    extend 1fsrpo " ¡Lo hacen súper conveniente!"
    n 1fsrpo "Supongo que lo que quiero decir es... {w=0.3} que intentes tener cuidado con tus hábitos de gasto, {w=0.1} ¿vale?"
    n 1unmss "Trata de no comprar cosas que no necesites{w=0.1} -{w=0.3}{nw}"
    extend 1flrbg " piensa en todo lo que tiraste la última vez que limpiaste."
    n 1uwdajl "¡E-{w=0.1}eso no quiere decir que no debas darte un capricho, {w=0.1} por supuesto!{w=0.5}{nw}"
    extend 1flrssl " ¡Tú también te mereces cosas chulas!"
    n 1flrss "El dinero no puede comprar la felicidad...{w=0.5}{nw}"
    extend 1fchgn " pero seguro que facilita la búsqueda.{w=0.5}{nw}"
    extend 1uchbs " ¡Jajaja!"
    n 1nllss "Bueno,{w=0.1} de todos modos.{w=0.5}{nw}"
    extend 1tnmsg " Intenta pensar un poco antes de gastar,{w=0.1} [player]{w=0.1} -{w=0.3}{nw}"
    extend 1uchbs " ¡es todo lo que digo!"

    if Natsuki.isAffectionate(higher=True):
        n 1nslbg "Además..."
        n 1fsqsm "Tenemos que ahorrar todo lo que podamos para cuando podamos salir,{w=0.1} ¿verdad?{w=0.5}{nw}"
        extend 1uchsm " Jejeje"

        if Natsuki.isLove():
            n 1uchbgl "¡Te amo,{w=0.1} [player]~!"

    return

# Natsuki discusses the importance of not only eating healthily, but regularly too
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_eating_well",
            unlocked=True,
            prompt="Comer bien",
            category=["Vida", "TÚ", "Salud", "Comida"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_eating_well:
    n 1unmaj "Oye,{w=0.1} [player]..."
    menu:
        n "¿Has comido hoy?"

        "Sí":
            n 1fnmbg "¡Aja!{w=0.5}{nw}"
            extend 1fsqbg " Pero, ¿has comido {i}bien{/i},{w=0.1} [player]?"

        "No":
            n 1knmpu "¿Eh?{w=0.2} ¿Qué?{w=0.5}{nw}"
            extend 1knmem " ¡¿Por qué no?!"
            n 1fnmem "No te estás saltando las comidas,{w=0.1} ¿verdad?"
            n 1flrpo "Más te vale que no sea así,{w=0.1} [player]."

    n 1unmpu "Es muy importante asegurarse de que no sólo comes regularmente,{w=0.3}{nw}"
    extend 1fnmpu " ¡sinó también comer decentemente!"
    n 1fnmsr "La dieta adecuada marca la diferencia,{w=0.1} [player]."
    n 1ullaj "Entonces...{w=0.5}{nw}"
    extend 1nnmaj " intenta hacer un esfuerzo con tus comidas, {w=0.1} ¿entendido?"
    n 1fnmaj "¡Y me refiero a un verdadero esfuerzo!{w=0.5}{nw}"
    extend 1ulrss " Intenta prepararlos desde cero si puedes;{w=0.3}{nw}"
    extend 1flrss " de todos modos, suele ser más barato que los platos preparados."
    n 1unmss "Reducir cosas como la sal y el azúcar y otras cosas también...{w=0.5}{nw}"
    extend 1nslpo " así como cualquier cosa realmente procesada."
    n 1unmaj "Oh {w=0.1}-{w=0.3}{nw}"
    extend 1fnmaj " y como he dicho, {w=0.1} ¡también tener comidas regularmente!"
    n 1fchbg "No deberías encontrarte comiendo chatarra si comes adecuadamente a lo largo del día."
    n 1usqsm "Tu saldo bancario y tu cuerpo te lo agradecerán.{w=0.5}{nw}"
    extend 1nchsm " Jejeje."

    if Natsuki.isAffectionate(higher=True):
        n 1fsqsm "Y además..."
        n 1usqss "Tengo que conseguir que adquieras buenos hábitos por ti mismo antes de que yo esté ahí para obligarte."
        n 1fchgn "¡Jajaja!{w=0.2} ¡Estoy bromeando,{w=0.1} [player]!{w=0.2} ¡Estoy bromeando!"
        n 1fsqsm "...La mayor parte."

        if Natsuki.isEnamored(higher=True):
            n 1uchsm "¡Te amo, [player]~!{w=0.2} Jejeje."
            return

    n 1fllss "Ahora...{w=0.3} ¿dónde estábamos?"
    return

# Natsuki discusses her favourite season with the player, and asks the player theirs
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_favourite_season",
            unlocked=True,
            prompt="¿Cuál es tu estación favorita?",
            category=["Clima", "Naturaleza"],
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_favourite_season:
    n 1unmbo "¿Eh?{w=0.2} ¿Mi estación favorita?"
    if not persistent.jn_player_favourite_season:
        n 1tllss "Esa pregunta no me la esperaba, {w=0.1} ¿eh?"
        n 1tnmss "Bueno... {w=0.3} en todo caso.{w=0.3}{nw}"
        extend 1fnmaw " ¡Una pregunta difícil, [player]!"
        n 1fsrsl "Creo que si tuviera que elegir..."
        n 1fchts "¡Sería el verano!{w=0.2} ¡Dah!"
        n 1fsqss "¿Por qué?{w=0.5}{nw}"
        extend 1fchgn " ¡Piénsalo,{w=0.1} [player]!"
        n 1ullbg "Los viajes largos a la playa...{w=0.5}{nw}"
        extend 1ncssm " helado en la sombra...{w=0.5}{nw}"
        extend 1ksrss " paseos nocturnos por las tiendas..."
        n 1flleml "E-{w=0.1}es decir,{w=0.3}{nw}"
        extend 1fllbgl " ¿qué es lo que no te gusta?"
        n 1fchbg "Puedo disfrutar de la vida ahí fuera sin tener que preocuparme por el tiempo."
        n 1usqsg "No creo que tenga que aclarar más mi punto, {w=0.1} ¿verdad?{w=0.5}{nw}"
        extend 1uchsm " Jajaja."
        n 1unmaj "De todos modos...{w=0.3} ¿qué hay de ti,{w=0.1} [player]?"
        menu:
            n "¿Cuál es tu estación favorita?"

            "Primavera.":
                n 1fnmss "¿Oh?{w=0.2} Primavera,{w=0.1} ¿eh?"
                n 1tllsr "Hmmm..."
                n 1unmss "Quiero decir, {w=0.1} de alguna manera lo entiendo.{w=0.2} Es la señal de que el invierno finalmente terminó,{w=0.1} ¿verdad?"
                n 1ulrss "Y supongo que las flores volviendo a florecer son algo genial de ver."
                n 1fsqan "¡Pero la lluvia!{w=0.2} ¡Dios!{w=0.5}{nw}"
                extend 1fcspu " ¡Nunca se detiene!"
                n 1fllpo "Que venga el verano,{w=0.1} por qué yo lo digo."
                $ persistent.jn_player_favourite_season = "la primavera"

            "Verano.":
                n 1fsgbg "¡Aja!{w=0.2} ¡Lo sabía!"
                n 1fsqbg "Nadie puede resistirse a un poco de diversión bajo el sol,{w=0.1} ¿tengo razón?"
                n 1fnmbg "Me alegro de que ambos estemos de acuerdo,{w=0.1} [player].{w=0.5}{nw}"
                extend 1fchsm " Jejeje."
                $ persistent.jn_player_favourite_season = "el verano"

            "Otoño.":
                n 1unmaj "¿Otoño?{w=0.5}{nw}"
                extend 1nllaj " No es una mala elección, {w=0.1} en realidad."
                n 1ullsm "Me gusta cuando todavía hace suficiente calor en el día para salir y hacer cosas..."
                n 1ucsss "Pero también tienes{w=0.1} ese aire fresco de la mañana para despertarte."
                n 1ullaj "Las hojas que caen son súper bonitas también."
                n 1fcsan "Es sólo que...{w=0.5}{nw}"
                extend 1fsrsr " todo se arruina cuando llega la lluvia, {w=0.1} ¿sabes?"
                n 1fsqsr "Caminar entre todas esas hojas podridas es simplemente asqueroso.{w=0.5}{nw}"
                extend 1fcssf " ¡No, gracias!"
                $ persistent.jn_player_favourite_season = "el otoño"

            "Invierno":
                n 1tnmsf "¿Eh?{w=0.2} ¿En serio?"
                n 1tnmaj "¡El invierno es lo último que esperaba que dijeras,{w=0.1} [player]!"
                n 1tlrbo "Aunque...{w=0.3} Lo entiendo, más o menos."
                n 1fcsbg "¡Es la época del año perfecta para ponerse súper cómodo y pasar un rato de lectura de calidad!"
                n 1fslss "Especialmente porque no hay mucho que puedas hacer fuera,{w=0.1} de todos modos."
                $ persistent.jn_player_favourite_season = "el invierno"

    else:
        n 1tllbo "Espera...{w=0.5}{nw}"
        extend 1tnmss " ¿No hemos hablado de esto antes,{w=0.1} [player]?"
        n 1nlrpu "Bueno, {w=0.1} de todos modos..."
        n 1ucsbg "Sigo amando el verano,{w=0.1} como ya sabes{w=0.1} -{w=0.3}{nw}"
        extend 1fcsbg " ¡y nada va a cambiar eso pronto!"
        n 1tsqsg "¿Qué hay de ti,{w=0.1} [player]?"
        menu:
            n "¿Todavía te gusta [persistent.jn_player_favourite_season]?"
            "Sí.":
                n 1fcsbg "Jejeje.{w=0.2} Justo lo que habia pensado,{w=0.1} [player]."
                if persistent.jn_player_favourite_season == "el verano":
                    n 1uchbg "Ya que has elegido la mejor temporada,{w=0.1} ¡después de todo!"
                    return

                n 1fllss "Bueno...{w=0.3} ¡Me temo que no vas a convencerme!{w=0.5}{nw}"
                extend 1uchbg " ¡Jajaja!"

            "No.":
                n 1tsgbg "¿Oh?{w=0.2} Has cambiado de opinión,{w=0.1} ¿verdad?"
                n 1tsqss "¿Bueno?{w=0.5}{nw}"
                extend 1fchbg " ¡Dime entonces,{w=0.1} [player]!"
                menu:
                    n "¿Cuál es tu estación favorita?"

                    "Primavera.":
                        $ new_favourite_season = "la primavera"

                    "Verano.":
                        $ new_favourite_season = "el verano"

                    "Otoño.":
                        $ new_favourite_season = "el otoño"

                    "Invierno.":
                        $ new_favourite_season = "el invierno"

                if persistent.jn_player_favourite_season == new_favourite_season:
                    n 1fnmgs "¡Oye!{w=0.2} ¡[player]!"
                    n 1fsqpo "Creí que habías dicho que habías cambiado de opinión."
                    n 1fllem "¡No has cambiado de opinión en absoluto!{w=0.2} Dijiste [persistent.jn_player_favourite_season] la última vez,{w=0.1} también."
                    $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
                    n 1fcsem "Dios...{w=0.5}{nw}"
                    extend 1fnmpo " ¡a veces eres tan bobo,{w=0.1} [chosen_tease]!"
                    if Natsuki.isAffectionate(higher=True):
                        n 1flrpol "N-{w=0.1}no es que me {i}desagrade{/i} ese lado tuyo,{w=0.1} o-{w=0.1}o algo."

                    else:
                        n 1fsqsm "Pero...{w=0.3} Creo que puedo {i}aclimatarme{/i} a ello."
                        n 1fsrss "Por ahora."

                    return

                else:
                    $ persistent.jn_player_favourite_season = new_favourite_season

                if persistent.jn_player_favourite_season == "la primavera":
                    n 1usqss "¿Ooh?{w=0.2} ¿Favoreciendo la primavera ahora,{w=0.1} [player]?"
                    n 1nlrbo "Podría ser mejor sin toda la lluvia, {w=0.1} pero lo entiendo."
                    n 1flrpu "Hmm...{w=0.3} Primavera..."
                    n 1tlrbo "Me pregunto...{w=0.5}{nw}"
                    extend 1tnmss " ¿cultivaste algo{w=0.1} [player]?"
                    n 1fchsm "Jajaja."

                elif persistent.jn_player_favourite_season == "el verano":
                    n 1fchbs "¡Aja!{w=0.2} ¿Lo ves?"
                    n 1fsqbs "Sabías que tenía razón todo el tiempo, {w=0.1} ¿no?"
                    n 1usqsg "Ni siquiera intentes negarlo,{w=0.1} [player].{w=0.5}{nw}"
                    extend 1fchbg " ¡El verano es lo mejor!"
                    n 1uchsm "Me alegro de que hayas reaccionado.{w=0.2} ¡Eso es lo importante!"

                elif persistent.jn_player_favourite_season == "el otoño":
                    n 1usqsm "¿Oh?{w=0.2} Te ha {i}arrastrado{/i} la lluvia del otoño,{w=0.1} ¿verdad?"
                    n 1fchsm "Jejeje."
                    n 1ullss "Lo admito,{w=0.1} es una bonita estación,{w=0.1} con todas las hojas doradas y demás..."
                    n 1nslss "Mientras el tiempo siga siendo cálido, {w=0.1} de todos modos."

                elif persistent.jn_player_favourite_season == "el invierno":
                    n 1tllss "Invierno,{w=0.1} ¿eh?{w=0.2} No me esperaba eso."
                    n 1tnmbo "¿Ahora prefieres estar dentro de casa o algo así,{w=0.1} [player]?"
                    n 1flrss "Bueno,{w=0.1} si prefieres estar todo el tiempo dentro..."
                    n 1fsqsm "¡Entonces será mejor que no estés descuidando la lectura,{w=0.1} [player]!{w=0.5}{nw}"
                    extend 1fchsm " Jejeje."

    return

# Natsuki discusses the concept of timeboxing
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_time_management",
            unlocked=True,
            prompt="Gestión del tiempo",
            category=["Vida"],
            nat_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_time_management:
    n 1ullaj "Oye,{w=0.1} [player]..."
    n 1unmaj "¿Tienes días libres a veces?{w=0.2} ¿En los que te cuesta hacer algo?"
    n 1flrpo "¿O simplemente te distraes con mucha facilidad?"
    n 1unmbo "¿Te soy honesta?{nw}"
    extend 1fllss "{w=0.2} He luchado con eso durante un tiempo.{nw}"
    extend 1fbkwr "{w=0.2} ¡Especialmente cuando cosas como las tareas son tan aburridas!"
    n 1nllaj "Pero...{w=0.5}{nw}"
    extend 1fllbg " ¡He descubierto una forma de gestionarlo{w=0.1} -{w=0.1} y tú también deberías conocerla,{w=0.1} [player]!"
    n 1fchbg "¡Empaquetar el tiempo!"
    n 1nsqpo "Y no, {w=0.1} no es tan literal como parece."
    n 1nnmaj "La idea es que se reserve un periodo del día en el que se quiera trabajar{w=0.1} -{w=0.1} como la jornada escolar,{w=0.1} o unas horas por la noche."
    n 1fnmbg "Entonces, por cada hora de ese período,{w=0.1} ¡lo divides!"
    n 1ulraj "Así que para una hora cualquiera,{w=0.1} pasas la mayor parte de ella trabajando,{w=0.1} y el resto en algún tipo de descanso."
    n 1unmss "La idea es que resulta mucho más fácil mantenerse concentrado y motivado, ya que siempre tienes un respiro a la vuelta de la esquina."
    n 1uchsm "Personalmente,{w=0.1} me parece que una división 50/10 funciona bien para mí."
    n 1nllbo "Así que paso 50 minutos de cada hora estudiando,{w=0.3}{nw}"
    extend 1uchsm " y 10 minutos haciendo lo que quiera."
    n 1usqbg "¡Te sorprendería saber cuánto tiempo de manga puedo dedicarle!"
    n 1unmaj "Sin embargo, no tomes mi horario como una regla.{w=0.5}{nw}"
    extend 1fchbg " ¡Encuentra un equilibrio que te funcione, [player]!"
    n 1fslbg "Aunque debo recordarte... {w=0.3} La palabra clave aquí es {i}equilibrio{/i}."
    n 1fsqsr "No me sorprendería que trabajes demasiado...{w=0.5}{nw}"
    extend 1fnmpo " ¡O simplemente vagues!"
    if Natsuki.isAffectionate(higher=True):
        n 1ullbo "Aunque... {w=0.3} Ahora que lo pienso..."
        n 1tsqsm "Tal vez debería hacer un paquete de tiempo para nuestro tiempo juntos,{w=0.1} [player]."
        extend 1uchbs " ¡Jajaja!"

    return

# Natsuki discusses her sweet tooth with the player
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_sweet_tooth",
            unlocked=True,
            prompt="¿Te gustan los dulces?",
            category=["Salud", "Comida"],
            player_says=True,
            affinity_range=(jn_affinity.DISTRESSED, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_sweet_tooth:
    n 1unmbo "¿Eh?{w=0.2} ¿Que si me gustan los dulces?"

    # Opening response
    if Natsuki.isAffectionate(higher=True):
        n 1fspbg "¡Claro que sí!"
        n 1nsqts "¿Qué más esperabas,{w=0.1} [player]?"
        extend 1fchsm "{w=0.2} Jejeje."

    elif Natsuki.isNormal(higher=True):
        n 1fllss "Bueno,{w=0.1} sí.{w=0.2} ¡Por supuesto que sí!"

    else:
        n 1nnmsl "Bueno...{w=0.3} sí.{w=0.2} ¿Por qué no lo haría?"

    n 1nllaj "Las cosas horneadas están bien, {w=0.1} pero me parece que se vuelve un poco enfermizo en poco tiempo."
    n 1ullaj "Pero para ser completamente honesta, {w=0.1} si pudiera elegir...{w=0.5}{nw}"
    extend 1unmbo " Sólo dame un montón de caramelos cada vez."

    if Natsuki.isNormal(higher=True):
        n 1uwdaj "¡Hay mucha más variedad!{w=0.2} Como...{w=0.3} ¡siempre hay algo para lo que me apetece!"
        n 1tllss "Sin embargo, creo que si tuviera que elegir un favorito,{w=0.3}{nw}"
        extend 1fllss " serían esos burbujeantes."
        n 1fchbg "Esa mezcla perfecta de dulce y ácido, {w=0.1} ¿sabes?"
        n 1flraj "Dios...{w=0.5}{nw}"
        extend 1fchts " Ya siento un cosquilleo en la lengua sólo de pensar en ellos."
        n 1fsrts "..."
        n 1flleml "¡D-{w=0.1}de todos modos!"
        n 1fcseml "Sin embargo, no es que esté comiendo dulces todo el tiempo."
        n 1fllpo "Tengo cosas mucho mejores en las que gastar mi dinero."
        n 1fnmss "Y... {w=0.3} tampoco es precisamente saludable.{w=0.5}{nw}"
        extend 1fchsm " Jajaja."

    # Closing thoughts
    if Natsuki.isAffectionate(higher=True):
        n 1fsqsm "Aunque tengo que decir,{w=0.1} [player]."
        n 1fsqssl "Estoy segura de que tú también eres muy goloso."
        n 1fsrbgl "Eso explicaría por qué pasas tanto tiempo conmigo,{w=0.1} d-{w=0.1}despues de todo."
        n 1fchbgl "¡Jajaja!"

    elif Natsuki.isNormal(higher=True):
        n 1fllbg "Podría ir por algo dulce ahora mismo, {w=0.1}de hecho.{w=0.5}{nw}"
        extend 1fslss " Pero...{w=0.3} creo que voy a contenerme."
        n 1usqbg "Alguien tiene que ser un modelo a seguir para ti,{w=0.1} [player].{w=0.2} ¿Tengo razón?"
        n 1fchsm "Jejeje."

    else:
        n 1nnmbo "..."
        n 1nlrbo "Dicho esto..."
        n 1flrsr "Me...{w=0.3} vendría muy bien un poco de chocolate ahora mismo."
        n 1fsqsr "Dejaré que {i}tú{/i} descubras por qué,{w=0.1} [player]."

    return

# Natsuki asks about and potentially discovers more about the player's physical appearance
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_player_appearance",
            unlocked=True,
            prompt="Mi aspecto",
            category=["TÚ"],
            player_says=True,
            affinity_range=(jn_affinity.ENAMORED, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_player_appearance:
    # Player was asked before, and declined to share their appearance
    if persistent.jn_player_appearance_declined_share:
        n 1unmaj "¿Eh?{w=0.2} ¿Tu aspecto?"
        n 1ullaj "Si no recuerdo mal,{w=0.1} [player]{w=0.1} -{w=0.3}{nw}"
        extend 1tnmbo " dijiste que no querías compartirlo conmigo antes."
        n 1tlrbo "Eh. Bueno..."
        menu:
            n "¿Has cambiado de opinión,{w=0.1} [player]?"

            "Sí, quiero compartirte mi aspecto.":
                n 1fcsbg "¡A-{w=0.1}aja!{w=0.2} Sabía que al final entrarías en razón,{w=0.1} [player].{nw}"
                extend 1fchgn "{w=0.2} ¡No perdamos el tiempo!"

            "No, todavía no quiero compartir mi aspecto.":
                n 1nllsl "Oh..."
                n 1unmaj "Bueno,{w=0.1} es tu decisión,{w=0.1} [player]."
                n 1unmss "Sólo hazme saber si cambias de opinión de nuevo,{w=0.1} ¿de acuerdo?"
                return

    # Player has already described themselves to Natsuki
    elif persistent.jn_player_appearance_eye_colour is not None:
        n 1unmaj "¿Eh?{w=0.2} ¿Tu aspecto?"
        n 1tllbo "Pero...{w=0.3} Estaba segura de que ya lo habías compartido conmigo,{w=0.1} [player]."
        n 1uspgs "¡Ooh!{w=0.5}{nw}"
        extend 1unmbg " ¿Te has teñido el pelo o algo así?"
        n 1fllbg "O...{w=0.3} ¿quizás te equivocaste la última vez?"
        n 1tslbg "Bueno...{w=0.5}{nw}"
        extend 1unmbg " de cualquier manera."
        menu:
            n "¿Querías compartir tu apariencia de nuevo,{w=0.1} [player]?"

            "Sí, mi apariencia ha cambiado.":
                n 1fcssm "¡Aja!{w=0.2} ¡Ya me lo imaginaba!"
                n 1fchgn "Estoy impaciente por saber cómo."

            "No, mi apariencia no ha cambiado.":
                n 1tnmsr "¿E-{w=0.1}Eh?{w=0.2} Me estás tomando el pelo, {w=0.1}¿verdad?"
                n 1tsrsf "Okaaay..."
                n 1tnmss "Sólo hazme saber si realmente {i}haces{/i} cambiar algo entonces,{w=0.2} ¿De acuerdo?"
                return

    # Player has never described themselves to Natsuki, and this is their first time discussing it
    else:
        n 1tlrbo "Eh..."
        n 1tnmbo "Sabes,{w=0.1} [player].{w=0.2} Me acabo de dar cuenta de algo."
        n 1unmaj "Has visto mucho de mí, {w=0.1} ¿verdad?{w=0.5}{nw}"
        extend 1fslssl " A-{w=0.1}al pasar tiempo conmigo aquí, {w=0.1} quiero decir."
        n 1ullaj "Así que... {w=0.3} sabes exactamente con quién estás hablando."
        n 1uwdgs "¡Pero no tengo ni idea de con quién {i}estoy{/i}  hablando!"
        n 1fsqsm "¿Y honestamente?{w=0.2} Ya deberías conocerme.{w=0.5}{nw}"
        extend 1fsqbg " ¡La verdad es que tengo mucha curiosidad!"
        n 1nchbg "Pero no te preocupes -{w=0.1} cualquier cosa que me digas se queda estrictamente entre nosotros,{w=0.1} ¡obviamente!"
        n 1fllsfl "N-{w=0.1}no es que a nadie {i}le importe{/i} mucho,{w=0.1} de todos modos."
        n 1unmsm "Entonces, {w=0.3} ¿qué te parece, [player]?"
        menu:
            n "¿Quieres compartir tu aspecto conmigo, [player]?"

            "¡Claro!":
                n 1uchbsl "¡Sí!{w=0.5}{nw}"
                extend 1fcsbgl " ¡Q-{w=0.1}quiero decir, bien!{w=0.5}{nw}"
                n 1fchbg "Comencemos entonces,{w=0.1} ¿de acuerdo?"

            "No me siento cómodo compartiendo eso.":
                n 1unmsl "Oh..."
                n 1ullaj "Eso es un poco decepcionante de escuchar,{w=0.1} si te soy honesta."
                n 1nchss "Pero lo entiendo perfectamente,{w=0.1} [player].{w=0.2} Así que no te preocupes, {w=0.1} ¿de acuerdo?"
                n 1fsqss "Sin embargo, ¡más vale que me avises si te apetece decírmelo después!"
                $ persistent.jn_player_appearance_declined_share = True
                return

    n 1uchgn "¡Muy bien!{w=0.2} Empecemos con...{w=0.5}{nw}"
    extend 1fchbg " ¡tus ojos!"
    n 1unmbg "Dicen que los ojos son la ventana del alma,{w=0.1} así que tiene sentido empezar por ahí,{w=0.1} ¿no?"
    n 1flldvl "..."
    n 1fcseml "¡D-{w=0.1}de todos modos...!"

    # Eye colour
    menu:
        n "¿Cómo describirías el color de tus ojos,{w=0.1} [player]?"

        "Ámbar":
            n 1unmaj "¡Ooh!{w=0.2} No creo que haya visto a alguien con ojos ámbar antes."
            n 1fchbg "¡Eso es increible,{w=0.1} [player]!{w=0.2} Apuesto a que eso te ayuda a destacar, {w=0.1} ¿verdad?"
            $ persistent.jn_player_appearance_eye_colour = "ambar"

        "Azules":
            n 1unmbg "Ojos azules,{w=0.1} ¿eh?{w=0.2} ¡Genial!"
            n 1fsgsm "¡Me gusta mucho lo llamativos que son!"
            $ persistent.jn_player_appearance_eye_colour = "azules"

        "Marrones":
            n 1unmaj "Ojos marrones,{w=0.1} ¿eh?{w=0.5}{nw}"
            extend 1fchsm " ¡No me estoy quejando!"
            n 1tsqss "Bonito y natural, {w=0.1} ¿verdad?{w=0.5}{nw}"
            extend 1uchsm " Jajaja."
            $ persistent.jn_player_appearance_eye_colour = "marrones"

        "Grises":
            n 1unmaj "¿Oh?{w=0.2} ¿Ojos grises?{w=0.2} ¡Super genial, [player]!"
            n 1tllss "¡Creo que no he visto a nadie con ojos grises antes!"
            $ persistent.jn_player_appearance_eye_colour = "grises"

        "Verdes":
            n 1fsgbg "¡Aja!{w=0.2} Te imaginaba con ojos verdes,{w=0.1} [player]."
            n 1fsqbg "Apuesto a que estás orgulloso de ellos,{w=0.1} ¿no?{w=0.5}{nw}"
            extend 1uchsm " Jejeje."
            $ persistent.jn_player_appearance_eye_colour = "verdes"

        "Avellana":
            n 1unmaj "¡Ooh!{w=0.2} Avellana,{w=0.1} ¿eh?{w=0.5}{nw}"
            extend 1fsqbg " ¡Qué elegantes!"
            n 1tslsm "Hmm...{w=0.3} ¿Me pregunto si los tuyos están más cerca del verde o del marrón,{w=0.1} [player]?"
            $ persistent.jn_player_appearance_eye_colour = "avellana"

        "Heterocromáticos":
            n 1unmaj "¡Wow!{w=0.2} ¿Tiene dos colores diferentes o algo así,{w=0.1} [player]?"
            n 1fchbg "Ahora, si eso no es único, {w=0.1} ¡No sé lo que es!"
            $ persistent.jn_player_appearance_eye_colour = "heterocromáticos"

        "Otros":
            n 1unmaj "¿Oh?{w=0.2} Algo un poco fuera del lugar, {w=0.1} ¿eh?"
            n 1tlrss "...¿O tal vez usas mucho los lentes de contacto?{w=0.5}{nw}"
            extend 1unmsg " Bueno, {w=0.1} como sea."
            n 1ncsss "Estoy segura de que se ven bien de cualquier manera."
            $ persistent.jn_player_appearance_eye_colour = "otros"

    n 1uchbg "¡Muy bien!{w=0.2} ¡Eso es una menos!"
    n 1ullaj "Así que a continuación,{w=0.1} tenemos...{w=0.5}{nw}"
    extend 1fchsm " ¡tu cabello,{w=0.1} por supuesto!"
    n 1nnmsm "Empezaremos con el largo por ahora."
    n 1ullss "Ahora..."

    # Hair length
    menu:
        n "¿Cómo describirías el largo de tu cabello,{w=0.1} [player]?"

        "Corto":
            n 1ncsss "Ah, {w=0.1} el enfoque de bajo mantenimiento {w=0.1}-{w=0.1} ya veo.{w=0.1} Ya veo.{w=0.5}{nw}"
            extend 1fchbg " ¡De moda!"
            n 1unmaj "Para ser honesta, de hecho,{w=0.1} lo entiendo perfectamente."
            n 1fslpo "No tengo ni idea de cómo se mantiene el cabello largo en buen estado..."
            n 1nslpo "Me parece demasiado esfuerzo."
            $ persistent.jn_player_appearance_hair_length = "corto"

        "De longitud media":
            n 1fcsbg "¡Aja!{w=0.2} El equilibrio perfecto, {w=0.1} ¿verdad?"
            n 1fllss "Lo suficientemente largo para casi cualquier estilo..."
            n 1fchgn "Y, sin embargo, ¡lo suficientemente corto como para adaptarse a un día de pereza!{w=0.5}{nw}"
            extend 1nchsm " Jejeje."
            n 1flrbgl "¡Me alegra que pensemos igual,{w=0.1} [player]!"
            $ persistent.jn_player_appearance_hair_length = "de longitud media"

        "Largo.":
            n 1unmbg "¡Ooh!{w=0.2} Dejándolo libre,{w=0.1} ¿verdad?"
            n 1fcssm "Apuesto a que cuidas muy bien del tuyo."
            n 1fsqsm "Puede que incluso tenga que tomar prestados tus productos,{w=0.1} [player].{w=0.5}{nw}"
            extend 1nchsm " ¡Jejeje!"
            $ persistent.jn_player_appearance_hair_length = "largo"

        "No tengo cabello.":
            n 1fnmaj "Oye{w=0.1} -{w=0.1} ¡no hay nada malo en ello!{nw}"
            extend 1fsqbg "{w=0.2} ¿Quieres saber por qué?"
            n 1fchgn "Porque sólo significa que eres aerodinámico,{w=0.1} [player].{w=0.5}{nw}"
            extend 1uchsm " ¡Jajaja!"
            $ persistent.jn_player_appearance_hair_length = "calvo"

    n 1uchbs "¡Bien!{w=0.5}{nw}"
    extend 1unmbg " Ahora sí que empiezo a hacerme una idea."
    n 1fwdgs "¡Tenemos que mantener la dinámica,{w=0.1} [player]!"

    # Hair colour
    if persistent.jn_player_appearance_hair_length == "calvo":
        n 1fllss "Dijiste que no tenías cabello, {w=0.1} ¿cierto?{w=0.5}{nw}"
        extend 1fllbg " Así que creo que no tiene sentido hablar del color del cabello."
        n 1fslbo "Ahora,{w=0.1} veamos...{w=0.3} qué más..."

    else:
        n 1fchsm "Ahora, ¡el color de tu cabello!"
        n 1unmbg "Entonces,{w=0.1} [player]..."
        menu:
            n "¿Cómo describirías tu color de cabello?"

            "Bermejo":
                n 1unmaw "¡Ooh!{w=0.2} Bermejo,{w=0.1} ¿eh?{w=0.5}{nw}"
                extend 1fwdaw " ¡Eso es increíble,{w=0.1} [player]!"
                n 1fchbg "¡Es un color tan cálido!"
                $ persistent.jn_player_appearance_hair_colour = "bermejo"

            "Negro":
                n 1tsgsm "Negro,{w=0.1} ¿eh?{w=0.5}{nw}"
                extend 1nchgn " ¡Bien!"
                n 1usqsg "Apuesto a que te sientes súper sofisticado,{w=0.1} ¿eh [player]?"
                $ persistent.jn_player_appearance_hair_colour = "negro"

            "Rubio":
                n 1fnmbg "¡Aja!{w=0.2} Un rubio,{w=0.1} ¿verdad?{w=0.5}{nw}"
                extend 1fsqts " {w=0.3}...Eso explica muchas cosas."
                n 1fchgn "¡Jajaja!"
                n 1uchbs "¡Estoy bromeando,{w=0.1} [player]!{w=0.2} ¡Sólo estoy bromeando!"
                n 1fllbg "La verdad es que estoy un poco celosa.{w=0.5}{nw}"
                extend 1fsqsm " Sólo un poco."
                $ persistent.jn_player_appearance_hair_colour = "rubio"

            "Marrón":
                n 1unmaj "¿Cabello marrón,{w=0.1} [player]?{w=0.5}{nw}"
                extend 1nchsm " ¡Estoy a favor!"
                n 1nchsm "Ni demasiado sutil ni demasiado llamativo,{w=0.1} ¿sabes?{w=0.2} ¡Está bien!"
                $ persistent.jn_player_appearance_hair_colour = "marrón"

            "Gris":
                n 1unmaj "Ooh...{w=0.5}{nw}"
                extend 1ullaj " Debo decir que...{w=0.5}{nw}"
                extend 1kllbg " ¡No me lo esperaba!"
                n 1fsqsr "Sólo espero que no sea por el estrés,{w=0.1} [player]..."
                n 1fllbg "...O al menos el estrés por mi parte, {w=0.1} de todas formas.{w=0.5}{nw}"
                extend 1fchsm " Jejeje."
                $ persistent.jn_player_appearance_hair_colour = "gris"

            "Rojo":
                n 1fchsm "Jejeje.{w=0.5}{nw}"
                extend 1usqsm " ¿Así que eres pelirrojo,{w=0.1} [player]?"
                n 1flrajl "No es que haya nada malo en ello, {w=0.1} ¡o-{w=0.1}obviamente!"
                n 1fchbg "Apuesto a que eso consigue llamar la atención,{w=0.1} ¿eh?"
                n 1fsrpo "Pero más vale que sea del{w=0.1} tipo bueno."
                $ persistent.jn_player_appearance_hair_colour = "rojo"

            "Blanco":
                n 1unmbg "Cabello blanco,{w=0.1} ¿eh?{w=0.5}{nw}"
                extend 1uchsm " ¡Genial!"
                $ persistent.jn_player_appearance_hair_colour = "blanco"

            "Otro":
                n 1unmaj "¿Oh?{w=0.5}{nw}"
                extend 1fsqsm " ¡Parece que somos más parecidos en gustos de lo que pensaba!"
                n 1fsrss "Aunque probablemente debería aclarar...{w=0.5}{nw}"
                extend 1uchgn " ¡el mío es totalmente natural,{w=0.1} [player]!{w=0.2} Jajaja."
                $ persistent.jn_player_appearance_hair_colour = "otro"

    # Height
    n 1unmbg "¡Muy bien!{w=0.2} Creo que ya casi he terminado de interrogarte,{w=0.1} [player]."
    n 1fsqsm "Jejeje."
    n 1flrsl "Así que...{w=0.3} no me tomes el pelo cuando pregunto esto,{w=0.1} pero tengo que saberlo."
    n 1ulrbo "Exactamente..."

    $ player_input_valid = False
    while not player_input_valid:
        $ player_input = int(renpy.input(prompt="¿Cuánto mides en {i}centímetros{/i},{w=0.2} [player]?", allow="0123456789"))

        # Valid height
        if player_input > 75 and player_input <= 300:
            $ player_input_valid = True
            $ persistent.jn_player_appearance_height_cm = player_input

            if player_input < 149:
                n 1unmgs "¿E-{w=0.1}eh?{w=0.2} ¿De verdad?"
                n 1unmaj "¿Eres más bajo que yo?"
                n 1flldv "Bueno,{w=0.1} ¡No esperaba eso!"
                n 1fnmbg "No te preocupes,{w=0.1} [player].{w=0.2} Ambos estamos del mismo lado, {w=0.1} ¿cierto?{w=0.5}{nw}"
                extend 1fchbg " Jejeje."

            elif player_input == 149:
                n 1unmgs "¿En serio?{w=0.2} ¿Tenemos la misma altura?"
                n 1uchbg "¡Es increíble,{w=0.1} [player]!"

                if persistent.jn_player_appearance_hair_length = "de longitud media" and persistent.jn_player_appearance_hair_colour = "otro":
                    n 1fllbg "Con el cabello y todo también..."
                    n 1uchgn "¡Es como si fuéramos prácticamente gemelos!"

            elif player_input > 149 and player_input < 166:
                n 1unmaj "¿Oh?{w=0.2} ¿Un poco más bajo,{w=0.1} [player]?"
                n 1fcsss "¡No te preocupes, no te preocupes!{w=0.5}{nw}"
                extend 1fllpo " N-{w=0.1}no soy nadie para juzgar, {w=0.1} después de todo."

            elif player_input >= 166 and player_input < 200:
                n 1unmaj "¿De estatura media,{w=0.1} [player]?"
                n 1nchsm "¡No me quejo!"

            elif player_input >= 200 and player_input < 250:
                n 1unmaj "¿Oh?{w=0.2} En el lado más alto [player],{w=0.1} ¿cierto?"
                n 1fllbg "Supongo que ya sé a quién llevar de compras,{w=0.1} ¿verdad?{w=0.5}{nw}"
                extend 1nchsm " Jejeje."

            else:
                n 1unmgs "¡G-{w=0.1}guau!{w=0.2} ¿Qué demonios,{w=0.1} [player]?{w=0.2} ¿En serio?"
                n 1fbkwr "¡Eso es una locura de altura!"
                n 1tlrem "Aunque... {w=0.3} en realidad...{w=0.5}{nw}"
                extend 1knmpo " Sin embargo, espero que no sea un inconveniente,{w=0.1} para ti."

        else:
            n 1fllpo "[player]...{w=0.3} por favor.{w=0.2} Tómate esto en serio,{w=0.1} ¿de acuerdo?"

    n 1uchsm "¡Muy bien!{w=0.2} Creo que eso es todo."
    n 1unmbg "¡Muchas gracias,{w=0.1} [player]!"
    n 1fllbg "Sé que no era mucho,{w=0.3}{nw}"
    extend 1uchgn " ¡pero siento que te conozco mucho mejor ahora!"

    if Natsuki.isLove():
        n 1flldvl "¿Sabes,{w=0.1} [player]?{w=0.2} Ya me lo puedo imaginar."
        n 1fnmssl "Conocerte en persona en algún lugar por ahí,{w=0.1} por primera vez..."
        python:
            # Get the descriptor for the eye colour
            if persistent.jn_player_appearance_eye_colour == "otros":
                eye_colour_descriptor = "calmados"

            else:
                eye_colour_descriptor = persistent.jn_player_appearance_eye_colour.lower()

            # Get the descriptor for the hair colour
            if persistent.jn_player_appearance_hair_colour == "otro":
                hair_colour_descriptor = "brillante"

            else:
                hair_colour_descriptor = persistent.jn_player_appearance_hair_colour.lower()

        # Comment on hair length and colour, if the player has hair
        if not persistent.jn_player_appearance_hair_length == "calvo":
            $ hair_length_descriptor = persistent.jn_player_appearance_hair_length.lower()
            n 1fsqsml "Veré tu cabello [hair_length_descriptor] [hair_colour_descriptor] en la distancia y te perseguire..."

        else:
            n 1fsqsml "Te ve en la distancia y te persigue..."

        # Comment on height and eye colour
        if persistent.jn_player_appearance_height_cm < 149:
            n 1fllssl "Mirando hacia abajo en tus ojos [eye_colour_descriptor]..."

        elif persistent.jn_player_appearance_height_cm == 149:
            n 1fllssl "Mirando directamente a tus ojos [eye_colour_descriptor]..."

        elif persistent.jn_player_appearance_height_cm > 149:
            n 1fllssl "Mirando hacia arriba a tus ojos [eye_colour_descriptor]..."

        n 1fchunl "Uuuuuuh..."
        n 1fsqunl "...{w=0.5}{nw}"
        extend 1fllajl " ¡E-ejem!{w=0.2} En fin..."
        $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
        n 1kllsml "Realmente.{w=0.2} Gracias,{w=0.1} [chosen_endearment]."
        n 1kcsbgl "Esto significó mucho para mí."

    elif Natsuki.isEnamored():
        n 1fsldvl "...Y ahora sé exactamente a quién debo vigilar."
        n 1fsqssl "Así que será mejor que tengas cuidado,{w=0.1} [player]."
        n 1fcsbgl "Jejeje."

    return

# Natsuki discusses drinking alcohol
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_drinking_alcohol",
            unlocked=True,
            prompt="¿Bebes alchol?",
            category=["Comida", "Salud"],
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_drinking_alcohol:
    n 1tnmss "[player] ¿Qué si bebo alchol?"
    extend 1tllss " Bueno...{w=0.3} No puedo decir que lo haya probado"
    n 1nllsr "No creo que me guste."
    n 1ullpu "Dicho esto,{w=0.1} Conocí a gente que si bebía..."
    n 1kcspu "Pero...{w=0.3} yo...{w=0.3} realmente prefiero no entrar en ese tema{w=0.1} [player]."
    n 1ncssr "Lo siento."
    n 1tlrpu "..."
    n 1unmaj "¡Oh! {w=0.2} ¡Eso me recuerda algo! {w=0.1}"
    n 1fnmbg "Apuesto a que no lo sabías,{w=0.1} pero ¿adivina quién llevo un poco al club?"
    n 1fchgn "...¡Yuri!"
    n 1tnmbg "¿Sorprendido?{w=0.5}{nw}"
    extend 1fcsss " Lo sé,{w=0.1} ¿verdad?"
    n 1tllss "Quiero decir... {w=0.3} ¡fue algo completamente inesperado!"
    n 1uchbs "Lo sacó de su bolso como si fuera alguno de sus libros o algo así."
    n 1unmbo "Ni siquiera era uno cualquiera del supermercado...{w=0.5}{nw}"
    extend 1uwdaj " ¡parecía súper caro!"
    n 1kllss "Honestamente, {w=0.1} No pude evitarlo pero acabe riendome de la situacion."
    n 1ullun "Creo que fue por lo despreocupada que se veia."
    n 1nnmsl "Monika no parecía impresionada,{w=0.1} aunque..."
    n 1klrsl "Sayori...{w=0.3} se puso muy molesta.{w=0.5}{nw}"
    extend 1klrpu " ¡Estaba gritando y todo!"
    n 1kcspu "Parecía que Yuri solo queria compartirnos un poco, {w=0.1} pero sólo le gritaron por ello..."
    n 1kcssr "Quiero decir...{w=0.5}{nw}"
    extend 1kllsr " Sé que no deberíamos haber traido eso a la escuela, {w=0.1} y Yuri debería haberlo sabido."
    n 1fslsr "Pero ella no se merecia que reaccionaran asi...{w=0.5}{nw}"
    extend 1kslsr " aun que."
    n 1kslaj "Creo que sólo trataba de ser amable, ¿sabes?"
    n 1unmsr "Todo está en el pasado ahora, {w=0.1} obviamente.{w=0.5}{nw}"
    extend 1kslsr " Pero...{w=0.3} eso no significa que no me siga sintiendo mal a veces."
    n 1kcssr "..."
    if Natsuki.isAffectionate(higher=True):
        n 1kllsr "Oye...{w=0.5}{nw}"
        extend 1knmpu " ¿[player]?"
        n 1klrsr "¿Puedes prometerme algo?"
        n 1fcssr "Es una tontería,{w=0.1} pero no me importa."
        n 1nnmsl "Realmente no me importa si bebes o no."
        n 1klrpu "Pero... {w=0.3} si lo haces..."
        n 1ksqsr "Por favor, tóma con moderación, {w=0.1} ¿de acuerdo?"
        n 1kllsr "Yo he{w=0.5}{nw}"
        extend 1fcsan " visto...{w=0.5}{nw}"
        extend 1fcssr " lo que le puede hacer a la gente."
        n 1kslsr "...De primera mano."
        n 1ksqsl "Te mereces algo mejor que eso,{w=0.1} [player].{w=0.5}{nw}"
        extend 1kslun " Eres {i}mejor{/i} que eso."
        if Natsuki.isLove():
            n 1kcsun "..."
            n 1ksqsml "Te amo,{w=0.1} [player]."
            n 1fcssrl "{i}Nunca{/i} voy a dejar que ninguna bebida se interponga entre nosotros."

    else:
        n 1unmsr "Oye,{w=0.1} [player]"
        n 1nllaj "Realmente no me importa mucho si bebes o no."
        n 1ncssr "Sólo...{w=0.3} no bebas demasiado."
        n 1flleml "¡P-{w=0.1}pero sólo porque no voy a limpiar todo tu desastre despues!"
        n 1fllss "Jajaja..."
        n 1kllsr "..."

    return

# Natsuki laments her inability to drive and questions the player on if they can
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_driving",
            unlocked=True,
            prompt="¿Sabes conducir?",
            category=["Transporte"],
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_driving:
    # Check to see if the player and Natsuki have already discussed if Nat can drive in this topic, or the "are you into cars?" topic
    $ already_discussed_driving = get_topic("talk_driving").shown_count > 0 or get_topic("talk_are_you_into_cars").shown_count > 0

    n 1fchdv "¡Pffft!{w=0.5}{nw}"
    extend 1uchbs " ¡Jajaja!"
    n 1fchgn "¿Qué clase de pregunta es esa{w=0.1} [player]?"
    $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)

    if already_discussed_driving:
        n 1tllss "¡Ya te dije que no se conducir,{w=0.1} [chosen_tease]!{w=0.5}{nw}"
        extend 1fchgn " ¡Ni siquiera tengo licencia!"
        n 1kllpo "Y aunque quisiera, {w=0.1} No creo que pueda permitírmelo..."

    else:
        n 1tllss "¡Por supuesto que no se conducir,{w=0.1} [chosen_tease]!{w=0.5}{nw}"
        extend 1fchgn " ¡Ni siquiera tengo licencia!"
        n 1kllpo "Quiero decir...{w=0.3} incluso si quisiera aprender, {w=0.1} no creo que pueda permitírmelo."

    n 1uskgs "¡Las clases son súper caras hoy en día!"
    n 1fslem "Y luego hay pruebas,{w=0.1} seguro,{w=0.1} combustible, {w=0.1}aparcarmientos..{w=0.5}{nw}"
    extend 1fsqaj " en realidad me fastidia bastante lo rápido que se acumula todo."
    n 1nlraj "Creo que prefiero el transporte público y mis propios pies."
    n 1unmaj "Pero, ¿qué hay de ti,{w=0.1} [player]?"

    # Player has never confirmed if they can/cannot drive
    if persistent.jn_player_can_drive is None:
        menu:
            n "¿Sabes conducir?"

            "Si, se conducir":
                n 1uwdaj "Guau..."
                extend 1fsraj " ...{w=0.3}que irrelevante."
                n 1fsqpo "..."
                n 1fchbg "Relájate,{w=0.1} ¡[player]!{w=0.2} ¡Dios!{w=0.5}{nw}"
                extend 1nchsm " Sólo te estoy molestando."
                n 1unmbg "Es impresionante,{w=0.1} aunque... -{w=0.1} no se puede superar la comodidad de un coche,{w=0.1} ¿verdad?"

                if Natsuki.isAffectionate(higher=True):
                    n 1fllbg "Pero debo advertirte..."
                    n 1fsgsm "Ya voy eligiendo las canciones para nuestra playlists de viajes."
                    extend 1uchbg " ¡Jajaja!"

                else:
                    n 1fllbg "Sólo recuerda,{w=0.1} [player]..."
                    n 1fsgsm "Yo llevo la escopeta.{w=0.5}{nw}"

                $ persistent.jn_player_can_drive = True
                return

            "Sí, pero ahora mismo no.":
                n 1unmaj "¿Oh?{w=0.2} ¿Hay algo que ande mal en tu coche,{w=0.1} [player]?"
                n 1tllbo "O tal vez...{w=0.3} ¿simplemente no tienes uno en este momento?"
                n 1nnmsm "Bueno, {w=0.1} no soy nadie para juzgar. Estoy seguro de que te las arreglas bien."
                n 1flrss "Además, {w=0.1} asi también estás ayudando al medio ambiente, {w=0.1} ¿verdad?"

                if Natsuki.isAffectionate(higher=True):
                    n 1fsgsm "Tan reflexivo como siempre,{w=0.1} [player]."
                    extend 1nchsm " Jejeje."

                $ persistent.jn_player_can_drive = True
                return

            "No, no se.":
                n 1klrsl "Oh..."
                n 1flrss "Bueno,{w=0.3}{nw}"
                extend 1fchbg " ¡no te desanimes, {w=0.1}[player]! No es el fin del mundo ni nada asi."
                n 1usgsg "No te preocupes -{w=0.3}{nw}"
                extend 1fsgsm " ¡te enseñaré a usar el autobús!"
                n 1uchsm "Jejeje."

                if Natsuki.isEnamored(higher=True):
                    n 1fllsm "Y además..."
                    n 1fllssl "Eso sólo significa que podemos acurrucarnos en el asiento juntos,{w=0.1} [player]."
                    n 1fcsbgl "Un sueño hecho realidad para ti,{w=0.1} ¿verdad?"
                    n 1flldvl "Jejeje."

                else:
                    n 1fchbg "¡Para eso están los amigos, [player]!"

                $ persistent.jn_player_can_drive = False
                return

    # Player stated they can drive previously
    elif persistent.jn_player_can_drive:
        menu:
            n "¿Conduces mucho?"

            "Sí, conduzco con frecuencia.":
                n 1fnmbg "Ah,{w=0.1}  así que vives practicamente en carretera,{w=0.1} ¿eh?"
                n 1ullss "Supongo que esta bien -{w=0.1} ¡solo recuerda conducir con cuidado [player]!"

            "Sólo conduzco a veces.":
                n 1ullss "Bueno, oye, {w=0.1}al menos estás ahorrando combustible, {w=0.1} ¿verdad?{w=0.5}{nw}"
                extend 1ullsm " Eso no me parece mal."
                n 1fchsm "Además,{w=0.1} ¡eso significa que puedes guardar las millas para disfrutarlas!"

            "No, no conduzco mucho.":
                n 1unmaj "¿Oh?{w=0.5}{nw}"
                extend 1tllbg " Eso me parece algo bueno,{w=0.1} ¡sinceramente!"
                n 1tnmbg "Sólo asegúrate de salir aun si no conduces mucho,{w=0.1} ¿De acuerdo?"

            "No, ya no puedo conducir.":
                n 1tnmsl "Oh... {w=0.3} ¿pasó algo?"
                n 1kllsl "Yo...{w=0.3} lamento escuchar eso,{w=0.1} [player]."
                n 1fsgsm "Pero al menos eso significa más tiempo para pasar el rato conmigo, {w=0.1}¿verdad?{w=0.5}{nw}"
                extend 1fchbg " Jajaja."
                $ persistent.jn_player_can_drive = False

        return

    # Player admitted they cannot drive previously
    else:
        menu:
            n "¿Hay alguna novedad en cuanto a conducir"

            "¡Estoy aprendiendo a conducir!":
                n 1fnmss "¡Ooh!{w=0.5}{nw}"
                extend 1fchbg " ¡Muy bien{w=0.1} [player]!"
                n 1fchsm "No te preocupes por el examen,{w=0.1} ¿de acuerdo?{w=0.2} ¡Estoy segura de que lo harás bien!"

                if Natsuki.isAffectionate(higher=True):
                    n 1uchsm "¡Yo creo en ti,{w=0.1} [player]!"

            "¡Pase el examen!":
                n 1uskgs "¿No es una broma?{w=0.5}{nw}"
                extend 1uchbs " ¡Yaaay!{w=0.2} ¡Felicidades,{w=0.1} [player]!"

                if Natsuki.isLove():
                    n 1kwmsm "¡Sabía que podías hacerlo,{w=0.1} enorme imbecil!"
                    extend 1kchsm " Jejeje."

                n 1kwmsm "Sólo asegúrate de mantener los buenos hábitos cuando sigas aprendiendo por tu cuenta,{w=0.1} ¿de acuerdo?{w=0.2} jajaja."
                $ persistent.jn_player_can_drive = True

            "¡Puedo volver a conducir!":
                n 1uchbg "¡Oye!{w=0.2} ¡Buen trabajo,{w=0.1} [player]!"
                n 1uwlsm "¡Conduce con cuidado!"
                $ persistent.jn_player_can_drive = True

            "No, nada nuevo.":
                n 1unmaj "¿Oh?{w=0.5}{nw}"
                extend 1nlrss " Bueno,{w=0.1} ¡No pasa nada!"
                n 1tnmsm "Entonces, estamos en la misma situacion.{w=0.5}{nw}"
                extend 1nchsm " Jajaja."

        return
    return

# Natsuki laments her inability to drive and questions the player on if they can
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_sustainable_fashion",
            unlocked=True,
            prompt="Moda sustentable",
            category=["Medioambiente", "Moda"],
            nat_says=True,
            affinity_range=(jn_affinity.UPSET, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_sustainable_fashion:
    n 1nnmaj "Oye,{w=0.1} [player]..."
    n 1nllaj "Es una pregunta extraña,{w=0.1} pero..."
    extend 1unmpu " ¿te gusta la moda?"
    if Natsuki.isHappy(higher=True):
        n 1fcsbg "¡Se lo que parece!{w=0.2} ¿pero puedes contestar?"
        extend 1nchsm " Jejeje."

    else:
        n 1nnmpu "Se que suena extraño."

    n 1fllpu "Pero me sorprendió la cantidad de residuos que genera."

    if Natsuki.isNormal(higher=True):
        n 1uwdgs "En serio, {w=0.1}[player] {w=0.1}-{w=0.1} ¡es una locura!"
        n 1ullaj "La gente tira {i}mucha{/i} ropa...{w=0.5}{nw}"
        extend 1flrem " Se estima que tiramos alrededor de 90{w=0.3} {i}millones{/i}{w=0.3} de toneladas cada año."
        n 1fnman "¡Eso es un camión lleno cada segundo! ¡Qué desperdicio!"

    else:
        n 1nllbo "Es una locura, sinceramente."
        n 1fnmsl "Recuerdo haber leído en alguna parte que tiramos algo así como 90{w=0.3} {i}millones{/i}{w=0.3} de toneladas cada año."
        n 1fcsan "Eso es literalmente un {i}camión lleno{w=0.3} cada segundo.{/i}."

    n 1fsrem "Y ni siquiera hemos empezado a hablar de la cantidad de agua que se utiliza para lavar y del plástico que se usa para los envases."
    n 1ksrsr "...O las condiciones que tienen que soportar algunos de los trabajadores que fabrican nuestra ropa."

    if Natsuki.isNormal(higher=True):
        n 1fcssm "De hecho, es una de las razones por las que empecé a aprender a coser."
        n 1klrsr "Nunca{w=0.3} he tenido mucho dinero para comprar mucha ropa,{w=0.1} así que intento reutilizar y arreglar lo que puedo."
        n 1fchbg "Pero te sorprendería lo que puedes conseguir con un poco de creatividad."
        extend 1fcssm " Y una pizca de inteligencia también,{w=0.1} obviamente."
        n 1fchgn "Apuesto a que no sabías que mi falda rosa favorita estaba hecha a mano,{w=0.1} ¿verdad?"

    n 1unmaj "Creo que ya te he dado suficientes lecciones,{w=0.1} [player],{w=0.1} así que no seguiré insistiendo en ello."
    n 1nllpu "Pero... {w=0.3} la próxima vez que salgas a comprar ropa,{w=0.1} o a mirar algunos catálogos online..."
    n 1unmpu "Piensa en el medio ambiente,{w=0.1} ¿quieres?"

    if Natsuki.isAffectionate(higher=True):
        n 1kllssl "¿Lo harás por mí?"
        n 1nchbg "Jajaja.{w=0.5}{nw}"
        extend 1uchsm " ¡Gracias,{w=0.1} [player]!"

    elif Natsuki.isNormal(higher=True):
        n 1nchbg "Jajaja.{w=0.5}{nw}"
        extend 1uchsm " ¡Gracias,{w=0.1} [player]!"

    else:
        n 1nllsl "Gracias."

    return

# Natsuki gets a nickname from the player, assuming they aren't blocked from doing so
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_give_nickname",
            unlocked=True,
            prompt="¿Puedo ponerte un apodo?",
            conditional="persistent.jn_player_nicknames_allowed",
            category=["Natsuki"],
            player_says=True,
            affinity_range=(jn_affinity.ENAMORED, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_give_nickname:
    # Natsuki hasn't been nicknamed before, or is rocking her normal name
    if persistent.jn_player_nicknames_allowed and persistent.jn_player_nicknames_current_nickname == "Natsuki":
        n 1unmaj "¿Eh?{w=0.2} ¿Quieres ponerme un apodo?"
        n 1fsqsl "¿Por qué?{w=0.2} ¿Natsuki no es un apodo lo suficientemente bueno para ti? ¿Es eso?"
        extend 1fsqpu " ¿Eh?{w=0.2} ¡Vamos, [player]!{w=0.2} ¡Dilo!"
        n 1fsqsm "..."
        n 1fchbg "Relájate,{w=0.1} ¡[player]! {w=0.2} ¡Cielos! ¡Estoy bromeando!"
        extend 1fchsm " Jejeje."
        n 1ullbg "Bueno...{w=0.3} ¡No veo por qué no!"

    # Another nickname is being assigned
    else:

        # Account for strikes
        if persistent.jn_player_nicknames_bad_given_total == 0:
            n 1unmaj "¿Oh?{w=0.2} ¿Quieres darme otro apodo?"
            n 1uchbg "Claro,{w=0.1} ¡por qué no!"

        elif persistent.jn_player_nicknames_bad_given_total == 1:
            n 1unmaj "¿Quieres darme un nuevo apodo?"
            n 1unmbo "Muy bien,{w=0.1} [player]."

        elif persistent.jn_player_nicknames_bad_given_total == 2:
            n 1nnmsl "¿Quieres darme otro apodo,{w=0.1} [player]?{w=0.5}{nw}"
            extend 1nllsl " Bien."
            n 1ncsaj "Sólo...{w=0.3} piensa un poco en lo que eliges,{w=0.1} ¿De acuerdo?"

        elif persistent.jn_player_nicknames_bad_given_total == 3:
            n 1nnmsl "Muy bien,{w=0.1} [player]."
            n 1fsqpu "Sólo recuerda. Ya te di tu última advertencia sobre esto."
            n 1nsqsl "No me vuelvas a fallar."

    # Validate the nickname, respond appropriately
    $ nickname = renpy.input(prompt="¿Qué tienes en mente{w=0.2} [player]?", allow=jn_globals.DEFAULT_ALPHABETICAL_ALLOW_VALUES, length=10).strip()

    if nickname.lower() == "Olvídalo":
        n 1tnmpu "¿Eh?{w=0.2} ¿Cambiaste de opinión?"
        n 1tllpu "Esta bien."
        n 1nnmaj "Solo hazme saber si quieres llamarme de otra manera entonces, {w=0.1} ¿De acuerdo?"
        return

    else:
        $ nickname_type = jn_nicknames.get_nickname_type(nickname)

    if nickname_type == jn_nicknames.TYPE_INVALID:
        n 1tlraj "Ehmm...{w=0.3} ¿[player]?"
        n 1tnmaj "No creo que eso sea un apodo en absoluto."
        n 1tllss "Yo...{w=0.3} sólo seguiré con el que tengo ahora,{w=0.1} gracias."
        return

    elif nickname_type == jn_nicknames.TYPE_LOVED:
        $ persistent.jn_player_nicknames_current_nickname = nickname
        $ n_name = persistent.jn_player_nicknames_current_nickname
        n 1uskgsl "¡O-{w=0.1}oh!{w=0.2} ¡[player]!"
        n 1ulrunl "..."
        n 1fcsbgl "B-{w=0.1}bueno,{w=0.1} tienes buen gusto,{w=0.1} al menos."
        n 1fcssml "[nickname]. ¡Me gusta!{w=0.5}{nw}"
        extend 1uchsml " Jejeje."
        return

    elif nickname_type == jn_nicknames.TYPE_DISLIKED:
        n 1fsqbo "Vamos,{w=0.1} [player]...{w=0.3} ¿es en serio?"
        n 1fllsl "Sabes que no me va a resultar comodo que me llames así."
        n 1fcssl "..."
        n 1nlraj "Yo...{w=0.3} Voy a fingir que no has dicho eso,{w=0.1} ¿de acuerdo?"
        return

    elif nickname_type == jn_nicknames.TYPE_HATED:
        n 1fskem "¿Q-{w=0.1}qué?{w=0.5}{nw}"
        extend 1fscwr " ¡¿Cómo me llamaste?!"
        n 1fcsan "¡[player]!{w=0.2} ¡No puedo creerlo!"
        n 1fcsfu "¿Por qué me llamaste así?{w=0.5}{nw}"
        extend 1fsqfu " ¡Esto es {i}horrible{/i}!"
        n 1fcspu "..."
        $ persistent.jn_player_nicknames_bad_given_total += 1

    elif nickname_type == jn_nicknames.TYPE_PROFANITY:
        n 1fskpu "¿D-{w=0.1}disculpa?"
        n 1fskfu "¡¿Como demonios acabas de llamarme, {w=0.1} [player]?!"
        n 1fcsan "..."
        n 1fslan "En serio, no puedo creerlo,{w=0.1} [player].{w=0.5}{nw}"
        extend 1fnman " ¿Por qué harías eso? ¡¿Estás {i}intentando{/i} ponerme de mal humor?!"
        n 1fcspu "..."
        $ persistent.jn_player_nicknames_bad_given_total += 1

    elif nickname_type == jn_nicknames.TYPE_FUNNY:
        n 1nbkdv "¡Pffft!"
        n 1uchbs "¡Jajaja!"
        n 1fbkbs "¡¿[nickname]?!{w=0.2} ¿Qué se supone que significa eso?{w=0.1} [player]?"
        n 1fbkbs "Bueno...{w=0.3} tienes suerte de que tenga un buen sentido del humor."
        n 1fsgbg "¡[nickname] esta bien,{w=0.1} supongo!{w=0.5}{nw}"
        extend 1fchgn " Jejeje."

        $ persistent.jn_player_nicknames_current_nickname = nickname
        $ n_name = persistent.jn_player_nicknames_current_nickname
        return

    elif nickname_type == jn_nicknames.TYPE_NOU:
        show natsuki 1uwlgn zorder JN_NATSUKI_ZORDER
        n 1usqsg "No, tu~."
        return

    else:
        $ neutral_nickname_permitted = False

        # Check and respond to easter egg nicknames
        if nickname.lower() == "natsuki":
            n 1fllss "Ehmm...{w=0.5}{nw}"
            extend 1tnmdv " ¿[player]?"
            $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
            n 1fchbg "¡Ese es mi nombre normal,{w=0.1} [chosen_tease]!"
            n 1fcsca "Sinceramente...{w=0.5}{nw}"
            extend 1ksgsg " a veces me pregunto por qué me molesto."
            n 1unmbg "Bueno,{w=0.1} ¡No me quejo! Si no está roto, w=0.1} no lo arregles-{w=0.1} ¿verdad?"
            n 1nchbg "Jajaja."
            $ neutral_nickname_permitted = True

        elif nickname.lower() == "thiccsuki":
            n 1kllunl "..."
            n 1fnmssl "S-{w=0.1}sigue soñando,{w=0.1} [player]"
            n 1klrsrl "Ehmm..."
            n 1klrpol "Yo...{w=0.3} realmente...{w=0.3} no es que me emocione,{w=0.1} pero si es lo que prefieres..."
            $ neutral_nickname_permitted = True

        elif nickname.lower() == persistent.playername.lower():
            n 1fsldv "Yo...{w=0.3} no creo que hayas pensado bien esto,{w=0.1} [player]."
            n 1tnmbg "¿Sabes lo confuso que sería eso?"
            n 1tlrss "Yo...{w=0.3} creo que me quedaré con lo que funciona,{w=0.1} ¿de acuerdo?{w=0.5}{nw}"
            extend 1fsqsm " Jejeje."
            n 1uchbg "¡Pero buen intento!"

        # Fallback for anything not categorised
        else:
            n 1fllsr "Hmm...{w=0.5}{nw}"
            extend 1ullpu " [nickname],{w=0.1} ¿eh?"
            n 1fllss "[nickname]..."
            n 1fnmbg "¿Sabes qué?{w=0.2} ¡Sí!{w=0.2} ¡Me gusta!"
            n 1fchbg "¡Dalo por hecho,{w=0.1} [player]!{w=0.5}{nw}"
            extend 1uchsm " Jejeje."
            $ neutral_nickname_permitted = True

        # Finally, assign the neutral/easter egg nickname if it was permitted by Natsuki
        if (neutral_nickname_permitted):
            $ persistent.jn_player_nicknames_current_nickname = nickname
            $ n_name = persistent.jn_player_nicknames_current_nickname

        return

    # Handle strikes
    if persistent.jn_player_nicknames_bad_given_total == 1:
        n 1kllsf "Dios,{w=0.1} [player]...{w=0.3} ¡eso no es propio de ti en absoluto!{w=0.5}{nw}"
        extend 1knmaj " ¿Qué te pasa hoy?"
        n 1kcssl "..."
        n 1knmsl "Sólo...{w=0.3} no vuelvas a hacer eso,{w=0.1} ¿de acuerdo?"
        n 1fsqsl "Eso realmente dolió,{w=0.1} [player].{w=0.2} No abuses asi de mi confianza."

        # Apply penalty and pending apology
        $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_BAD_NICKNAME)
        $ Natsuki.percentage_affinity_loss(1)

    elif persistent.jn_player_nicknames_bad_given_total == 2:
        n 1fsqsl "No puedo creer que me hayas hecho eso otra vez,{w=0.1} [player]."
        n 1fsqan "Te dije que me dolía,{w=0.1} ¡y seguiste haciendolo de todas formas!"
        n 1fcsan "..."
        n 1fcsun "Yo...{w=0.3} realmente...{w=0.3} no puedo creerlo [player].{w=0.5}{nw}"
        extend 1kllun " Duele más cuando lo haces tu."
        n 1fsqsr "No pongas a prueba mi paciencia así.{w=0.2} Eres mejor que eso."

        # Apply penalty and pending apology
        $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_BAD_NICKNAME)
        $ Natsuki.percentage_affinity_loss(2.5)

    elif persistent.jn_player_nicknames_bad_given_total == 3:
        n 1fsqan "Sinceramente, es increíble,{w=0.1} [player]."
        n 1fnmfu "Ya lo he dicho muchas veces,{w=0.1} y todavía no lo dejas."
        n 1fcspu "..."
        n 1fsqpu "Se acabaron las advertencias,{w=0.1} [player]."
        menu:
            n "¿Entiendes?"

            "Lo entiendo, lo siento [n_name].":
                n 1fsqsr "¿Lo entiendes,{w=0.1} verdad?"
                n 1fsqan "...Entonces empieza a actuar como tal,{w=0.1} [player]."
                n 1fslsl "Gracias."

                $ Natsuki.percentage_affinity_loss(3)

            "...":
                n 1fcssl "Mira.{w=0.2} No estoy bromeando,{w=0.1} [player]."
                n 1fnmpu "Actuar así no es divertido,{w=0.1} ni bonito."
                n 1fsqem "Es dañino y toxico."
                n 1fsqsr "No me importa si estás tratando de tomarme el pelo.{w=0.2} Déjalo."

                $ Natsuki.percentage_affinity_loss(5)

        # Apply penalty and pending apology
        $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_BAD_NICKNAME)

    elif persistent.jn_player_nicknames_bad_given_total == 4:
        # Player is locked out of nicknaming; this is why we can't have nice things
        n 1fcsan "No.{w=0.2} He escuchado suficiente. No necesito escuchar más."
        n 1fnmem "¿Cuándo aprenderás que tus acciones tienen consecuencias?"
        n 1fcspu "..."
        n 1fnmpu "¿Sabes qué?{w=0.5}{nw}"
        extend 1fsqpu " Ni siquiera te molestes en contestar."
        n 1fsqsr "Te lo advertí,{w=0.1} [player].{w=0.2} Recuérdalo."

        # Apply affinity/trust penalties, then revoke nickname priveleges and finally apply pending apology
        $ Natsuki.percentage_affinity_loss(10)
        $ persistent.jn_player_nicknames_allowed = False
        $ persistent.jn_player_nicknames_current_nickname = None
        $ n_name = "Natsuki"
        $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_BAD_NICKNAME)

    return

# Natsuki advises the player on good sleeping habits
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_sleeping_well",
            unlocked=True,
            prompt="Dormir bien",
            conditional="persistent.jn_total_visit_count >= 5",
            category=["Salud", "Tú"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_sleeping_well:
    n 1fllpu "Eh..."
    n 1fllpu "Oye,{w=0.1} [player].{w=0.5}{nw}"
    extend 1nnmaj " Déjame hacerte una pregunta,{w=0.1} ¿de acuerdo?"
    n 1fsqsr "¿Duermes bien por la noche?"
    n 1fsqpu "Sé honesto.{w=0.2} ¿De acuerdo?"
    n 1ksqsm "..."
    n 1fchsm "Jejeje.{w=0.2} ¿Te he atrapado?"
    n 1unmaj "Pero en serio,{w=0.2} [player].{w=0.5}{nw}"
    extend 1tnmaj " ¿Tiene problemas para dormir?"

    # Quip if the player has been around a while, or has admitted they're tired
    if jn_utils.get_current_session_length().total_seconds() / 3600 >= 12:
        n 1fsqpo "Quiero decir,{w=0.1} llevas aqui un {i}buen{/i} rato..."
        n 1ullaj "Así que...{w=0.5}{nw}"
        extend 1nnmaj " De todos modos, me imaginé que tendrías un poco de sueño."

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_TIRED:
        n 1fllpo "Quiero decir, incluso dijiste que estabas cansado antes."
        n 1ullaj "Así que...{w=0.5}{nw}"
        extend 1nnmaj " Tiene sentido que pregunte,{w=0.1} ¿verdad?{w=0.2} De todos modos..."

    n 1nnmaj "Lo admito,{w=0.1} yo también tengo alguna que otra noche de insomnio.{w=0.5}{nw}"
    extend 1fbkwr " ¡Es lo peor!"
    n 1fllem "No hay nada que odie más que dar vueltas en la cama,{w=0.3}{nw}"
    extend 1fcsan " sólo espero que mi cuerpo decida que es hora de que pase al día de mañana."
    n 1ullaj "Pero...{w=0.5}{nw}"
    extend 1fnmss " ya sabes lo que dicen,{w=0.1} [player]."
    n 1fcsss "Con el sufrimiento...{w=0.5}{nw}"
    extend 1uchbg  " ...¡viene la sabiduría!"
    n 1nsqbg "Y por suerte para ti,{w=0.1} no me importa compartirla contigo.{w=0.5}{nw}"
    extend 1nchsm " Jejeje."
    n 1fcsbg "Así que,{w=0.1} escuchen-{w=0.1} ¡es hora de otra lección de su maestra!"
    n 1fnmaj "Muy bien,{w=0.1} primero,{w=0.1} ¡deja las tonterías!{w=0.2} Si estás tratando de dormir,{w=0.1} cualquier cosa con alto contenido de azúcar o cafeína es tu enemigo."
    n 1fllss "Así que antes de nada,{w=0.1} deja los refrescos y el café. Puedes agradecérmelo después."
    n 1fcsaj "Siguiente -{w=0.1} ¡nada de pantallas!{w=0.5}{nw}"
    extend 1fsqpo " Incluyendo esta, [player]."
    n 1unmsl "Nada de pantalla significa que no tengas luces brillantes ni distracciones que te mantengan despierto,{w=0.1} obviamente."
    n 1fnmpu "Si estás cansado, lo último que necesitas es algo que te ilumine."

    if jn_activity.has_player_done_activity(jn_activity.JNActivities.anime_streaming):
        n 1tsqsr "Y no, [player] {w=0.1}-{w=0.3}{nw}"
        extend 1fnmpo " tampoco hay sesiones nocturnas de anime."
        n 1nchgn "¡Lo siento~!"

    n 1fcsbg "Lo siguiente es la temperatura:{w=0.2} Si hace calor,{w=0.1} utiliza sabanas más finas y con el frio al reves."
    n 1fcspu "Nada interrumpe más el sueño que tener que quitar las mantas,{w=0.1} o poner algunas."
    n 1fsgsg "¿Me sigues hasta ahora,{w=0.1} [player]?{w=0.5}{nw}"
    extend 1fchgn " Ya casi termino,{w=0.1} no te preocupes."
    n 1unmaj "Por último...{w=0.5}{nw}"
    extend 1fchbg " ¡ponte cómodo!"
    n 1nnmsm "Asegúrate de tener suficientes almohadas para apoyar la cabeza,{w=0.1} o incluso pon algo de música tranquila si crees que eso te ayuda."
    n 1fcssm "...Y eso es todo."
    n 1nllss "Deberías haber conocido ya al menos algunas de ellas,{w=0.3}{nw}"
    extend 1unmss " pero en cualquier caso..."
    n 1fwlbg "¡Espero que puedas estar mas tranquilo con tus nuevos conocimientos,{w=0.1} [player]!"
    n 1uchsm "Jejeje."

    return

# Natsuki discusses aging, and her carefree attitude towards the age-gap in relationships
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_aging",
            unlocked=True,
            prompt="Envejecer",
            category=["Vida"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_aging:
    n 1unmaj "Ya sabes,{w=0.1} [player]..."
    n 1nllpu "Creo que la mayoría de la gente comparte un montón de miedos."
    n 1unmpu "Entiendes lo que quiero decir,{w=0.1} ¿verdad?{w=0.2} Como presentar cosas a una sala llena de gente, o suspender un examen."
    n 1tlrss "Por supuesto,{w=0.1} es raro encontrar un miedo que tenga {i}todo el mundo{/i}..."
    n 1tnmaj "O al menos algo que haga que la gente se sienta incómoda."
    n 1unmbg "Pero...{w=0.3} ¡Creo que he encontrado uno!"
    n 1usgsm "¿En qué estoy pensando,{w=0.1} te preguntarás?"
    n 1ullaj "Bueno...{w=0.3} en realidad es algo un poco aburrido,{w=0.1} realmente."
    n 1nnmbo "Estaba pensando en envejecer."
    n 1unmpu "¿Has pensado en ello,{w=0.1} [player]?"
    n 1fllbg "Probablemente sea lo último en lo que pienses si eres muy joven."
    n 1nwmpu "Pero creo que a medida que se envejece,{w=0.1} se empieza a notar."
    n 1kllpu "Puede que tengas menos energía,{w=0.1} o que los amigos y la familia empiecen a alejarse..."
    n 1knmem "Los cumpleaños pierden todo su sentido -{w=0.1} ¡incluso puedes tenerles miedo!"
    n 1ullaj "Las señales aparecen de muchas maneras,{w=0.3}{nw}"
    extend 1knmsl " pero eso es lo que lo hace desconcertante."
    n 1kllaj "Cada persona lo experimenta de forma diferente,{w=0.3}{nw}"
    extend 1kskaw " ¡y ni siquiera sabemos qué pasa después del final!"
    n 1klrss "Espeluznante,{w=0.1} ¿eh?"
    n 1ulrpu "Aunque...{w=0.3} Supongo que se podría decir que es más el miedo a lo desconocido que el envejecimiento en sí."
    n 1flraj "Sin embargo, lo que me molesta es lo inmadura que puede ser la gente al respecto."
    n 1fnmaj "¡Especialmente cuando se trata de relaciones entre diferentes edades!"
    n 1fslsf "La gente se vuelve muy habladora..."
    n 1fllaj "Como... {w=0.3} mientras ambos sean felices,{w=0.3}{nw}"
    extend 1fnmem " y nadie se siente herido o incómodo, {w=0.1} ¿a quién le importa?"
    n 1nlrpu "Es como la mayoría de las cosas,{w=0.1} realmente."
    n 1unmaj "Además,{w=0.1} no es que tener cierta edad signifique que {i}tengas{/i} que ser de cierta manera."
    n 1fchbg "Quiero decir...{w=0.3} ¡mira a Yuri!"
    n 1uchgn "Siendo así de anticuada -{w=0.1} ¡cualquiera diría que es una anciana!"
    n 1nllbg "Pero de todos modos...{w=0.3} Creo que nos hemos desviado del tema."
    n 1unmss "No me importa la edad que tengas,{w=0.1} [player]."

    if Natsuki.isLove():
        $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
        n 1klrpol "S-{w=0.1}sabes que te quiero igual,{w=0.1} [chosen_tease]."
        n 1knmpol "Nunca lo olvides,{w=0.1} ¿de acuerdo?"
        n 1flrpol "Me enfadaré si lo haces.{w=0.5}{nw}"
        extend 1klrbgl " Jajaja..."

    elif Natsuki.isEnamored(higher=True):
        n 1fllbgl "De todos modos, te has portado muy bien conmigo."

    elif Natsuki.isHappy(higher=True):
        n 1fchbgl "¡Siempre es divertido pasar el rato contigo!"

    else:
        n 1fllbg "Pero...{w=0.3} por si acaso..."
        n 1fsqsg "Sólo pondre una vela en tu pastel de cumpleaños.{w=0.2} Lo siento.{w=0.5}{nw}"
        extend 1uchbg " ¡Jajaja!"

    return

# Natsuki discusses the concept of work-life balance, and how it can be difficult to disconnect
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_work_life_balance",
            unlocked=True,
            prompt="Equilibrio entre el trabajo y la vida privada",
            category=["Vida", "Sociedad"],
            nat_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_work_life_balance:
    if Natsuki.isUpset(higher=True):
        n 1ullaj "Ya sabes,{w=0.1} [player]..."

    n 1nnmaj "Creo que hoy en día es muy fácil dejar que tu vida académica o laboral se cuele en tu tiempo de ocio."
    n 1nlrsl "Quiero decir...{w=0.3} piensa en ello."
    n 1nnmsl "Con todo el mundo con teléfonos móviles,{w=0.1} además de algún tipo de ordenador en casa -{w=0.1} es difícil no estar conectado de alguna manera."
    n 1flrbo "Y es como...{w=0.3} si ya existe esa conexión,{w=0.1} entonces, ¿qué impide que el trabajo te moleste durante tu tiempo libre?"
    n 1fsrbo "¿O compañeros que piden ayuda en el último momento?"

    if Natsuki.isUpset(higher=True):
        n 1fcsem "Resulta molesto -{w=0.1} como si todo el mundo esperara que estuvieras siempre cerca para aportar un poco más,{w=0.1} o para hacer algo."
        n 1fnmpo "Abrumador,{w=0.1} ¿verdad?"
        n 1fllaj "Eh. {w=0.2} En realidad...{w=0.3} ahora que lo pienso..."
        n 1fnmsf "Tampoco es que ese tipo de intromisión se limite sólo a cuando estás fuera."
        n 1fslpu "He oído {i}demasiadas{/i} historias de gente que hace cantidades estúpidas de horas extras en el trabajo...{w=0.5}{nw}"
        extend 1fnman " ¡a veces ni siquiera se pagan!"
        n 1fsran "O incluso estudiantes que estudian hasta altas horas de la noche hasta que se desploman...{w=0.3} ¡es una locura!"

    else:
        n 1fsqpu "Simplemente resulta molesto -{w=0.1} todo el mundo espera que estés siempre para hacer más."
        n 1fslsl "En realidad,{w=0.1} ahora que lo pienso..."
        n 1fcsaj "Tampoco es que ese tipo de cosas se limiten sólo a cuando estás fuera."
        n 1fsrsr "He oído demasiadas historias de personas que hacen cantidades estúpidas de horas extras en el trabajo.{w=0.5}{nw}"
        extend 1fsqan " A menudo ni siquiera se pagan"
        n 1fslem "O incluso estudiantes que estudian hasta altas horas de la noche hasta que se desploman..."

    if Natsuki.isNormal(higher=True):
        n 1kcsem "Agh...{w=0.3} Sólo deseo que la gente valore más su propio tiempo."
        n 1klrsr "..."
        n 1unmaj "Oye,{w=0.1} [player]..."
        n 1nllaj "No sé si estás trabajando,{w=0.1} o estudiando,{w=0.1} o qué..."
        n 1fnmsf "Pero será mejor que no dejes que se apodere de tu vida. ¿Entiendes?"

        if Natsuki.isEnamored(higher=True):
            n 1knmpu "{i}Tu eres más{/i} que tu carrera,{w=0.1} o tu educación.{w=0.2} Tienes tus propios deseos y necesidades que también importan."
            n 1kllun "No quiero que un trabajo tonto o una tarea estúpida se apoderen de tu vida."
            n 1fcsun "Eres...{w=0.3} mucho más importante que cualquiera de esos,{w=0.1} [player].{w=0.2} Confía en mí."

            if Natsuki.isLove():
                n 1fllun "Además..."
                n 1fllssl "Tú y tu tiempo son míos, [player]."
                n 1flldvl "Ya pague por ellos,{w=0.1} d-{w=0.1}despues de todo.{w=0.5}{nw}"
                extend 1fchsml " Jejeje..."

        else:
            $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
            n 1kllpo "La gente es más que lo que hace para ganarse la vida,{w=0.1} después de todo. ¡Y eso te incluye a ti también, [chosen_tease]!"

    elif Natsuki.isDistressed(higher=True):
        n 1fllsr "Me hace desear que la gente valore más su propio tiempo."
        n 1fnmsr "...Supongo que eso te incluye a ti también,{w=0.1} [player]."
        n 1fllpu "Tienes mejores cosas que hacer."
        n 1fsqsf "...Como ser un amigo decente para los demás, para variar.{w=0.2} ¿Tengo razón?"

    else:
        n 1fslbo "La gente necesita valorar más su propio tiempo."
        n 1fcssl "...Je."
        n 1fcsun "Tal vez debería seguir mi propio consejo..."
        n 1fsqfu "Porque {i}claramente{/i} estar aquí también es una pérdida de tiempo."

    return

# Natsuki warns against the risks of wearing headphones/headsets
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_using_headphones_carefully",
            unlocked=True,
            prompt="Utilizar los auriculares con cuidado",
            category=["Salud", "Música", "Tecnología"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_using_headphones_carefully:
    n 1unmaj "..."
    n 1tnmaj "¿...?"
    n 1fnmaw "¡...!"
    n 1fbkwr "...¡[player]!"
    n 1fnmpo "¡[player]!{w=0.2} ¡Por fin!{w=0.2} ¿Puedes oírme ahora?"
    n 1fllpo "Dios... {w=0.3} ¡te ha llevado bastante tiempo!"
    n 1fslsm "..."
    n 1uchbg "Jejeje."
    n 1fnmbg "¡Admítelo,{w=0.1} [player]! {w=0.2} Te atraparé un día de estos."
    n 1nnmaj "En serio -{w=0.1} ¿usas a menudo auriculares o algo parecido?"
    n 1nlrpo "Lo admito,{w=0.1} probablemente uso los míos más de lo que debería."
    n 1fnmaj "Estaba bromeando con lo de la audición,{w=0.1} pero esto es importante,{w=0.1} [player]."
    n 1nlrss "A mí también me gusta subir el volumen -{w=0.1} sólo que no se me hace un mal hábito."
    n 1unmsl "En algunos países incluso hay advertencias si tienes el volumen demasiado alto..."
    n 1fllem "...¡Y por una buena razón!"
    n 1fnmpo "No sólo para proteger tus oídos -{w=0.1} más vale que tengas cuidado al salir fuera de casa también."
    n 1fcsem "¡No quiero oír hablar de que te han atropellado porque no has oído venir algo!"
    n 1unmbo "Oh -{w=0.1} y una última cosa, {w=0.1} en realidad."
    n 1unmpu "Puede que los lleves para concentrarte en el trabajo o para relajarte en casa -{w=0.1} y eso está bien."
    n 1nnmsr "Pero por favor,{w=0.1} [player]."
    n 1flrsr "...Quítatelos de vez en cuando,{w=0.1} ¿lo harás?{w=0.2} Al menos al estar con otras personas, {w=0.1} sabes..."
    n 1ncsbo "Lo entiendo -{w=0.1} si sólo quieres escuchar algo en paz,{w=0.1} o darte un poco de espacio,{w=0.1} está bien."

    if jn_activity.has_player_done_activity(jn_activity.JNActivities.music_applications):
        n 1kslbg "Sé que te gusta tu música en streaming."

    n 1nsqbo "Pero no los utilices para aislarte de todos y de todo."
    n 1ksrsl "No es...{w=0.3} saludable hacer eso tampoco,{w=0.1} [player]."
    n 1nchsm "...Y eso es todo lo que tenía que decir."
    n 1fchbg "¡Gracias por {i}escucharme{/i}... [player]! {w=0.2} Jejeje."
    return

# Natsuki discusses her dislike of the horror genre
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_thoughts_on_horror",
            unlocked=True,
            prompt="Reflexiones sobre el horror",
            category=["Contenido", "Literatura"],
            nat_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_thoughts_on_horror:

    if Natsuki.isNormal(higher=True):
        n 1unmaj "Sabes...{w=0.1} [player]..."
        n 1tllaj "Creo que nunca he explicado por qué me disgusta tanto el terror."
        n 1tlrss "Sé que lo mencioné antes, {w=0.1} pero me tomo un poco desprevenida en ese momento."
        n 1unmaj "¿Honestamente?"
        n 1nnmsm "Cada uno tiene sus gustos,{w=0.1} ¿verdad? Y puedo entender por qué la gente lo disfruta."

    elif Natsuki.isDistressed(higher=True):
        n 1nllbo "Creo que no he explicado por qué no me gusta el terror."
        n 1nnmsl "Entiendo que cada uno tiene sus gustos,{w=0.1} pero a mí no me gusta."

    else:
        n 1kslsl "..."
        n 1fsqaj "...Estaba a punto de compartir contigo algunos de mis pensamientos sobre el horror."
        n 1fsrsl "O al menos,{w=0.1} estaba pensando en ello."
        n 1fnmaj "...Pero entonces, ¿sabes de qué me di cuenta{w=0.1} [player]?"
        n 1fsqsf "Odio el horror -{w=0.1} no es que te importe -{w=0.1} y honestamente..."
        n 1fcsun "Estar atrapada aquí {i}contigo{/i} ya es un horror."
        return

    if Natsuki.isNormal(higher=True):
        n 1fchbg "¡Como Yuri!"
        n 1fcsss "Ella es fan del suspenso,{w=0.1} y los miedos son un motivador súper poderoso para los personajes."
        n 1ullpu "Así que no me malinterpretes{w=0.1} -{w=0.1} puedo apreciar totalmente el esfuerzo que supone."
        n 1fllpol "...Cuando no se trata de estúpidos jumpscares, {w=0.1} -{w=0.1} de cualquier manera."

    else:
        n 1ullpu "Entiendo el esfuerzo que supone...{w=0.2} En su mayor parte."

    n 1nllpu "Pero..."
    n 1nnmbo "Cuando leo algo -{w=0.1} o veo algo -{w=0.1} lo hago porque para mí,{w=0.1} es como me relajo."
    n 1fllbo "No quiero que me hagan sentir incómoda."
    n 1fllpu "No quiero que me hagan saltar."
    n 1fllsr "No quiero tener que ver cosas asquerosas."
    n 1fcssr "Yo...{w=0.3} sólo quiero sentarme,{w=0.1} sentirme bien y escapar por un rato."
    n 1fnmsl "Ya hay suficientes cosas desagradables por ahí, {w=0.1} ¿sabes?"
    n 1flrpu "Algunas cosas están más cerca de casa que otras."
    n 1fcssl "..."
    n 1nnmaj "Así que...{w=0.3} sí. {w=0.1} Eso es todo lo que tenía que decir al respecto."

    if Natsuki.isAffectionate(higher=True):
        n 1unmss "Aunque...{w=0.3} si quieres poner algo, {w=0.1} {w=0.2} adelante."
        n 1fllssl "Si es contigo, {w=0.1} creo que puedo lidiar con ello."
        n 1flrpol "Pero... {w=0.3} mantengamos el volumen bajo.{w=0.2} ¿Entendido?"

    elif Natsuki.isNormal(higher=True):
        n 1nnmaj "Pero no me hagas caso,{w=0.1} [player].{w=0.2} Si quieres ver algo, {w=0.1} hazlo."
        n 1flrcal "Pero lo estaras viendo solo."

    elif Natsuki.isDistressed(higher=True):
        n 1flrsl "..."
        n 1fnmpu "Yo {i}diria{/i} que si vas a ver algo así,{w=0.1} me avises primero."
        n 1fsqsr "Pero no me escucharías de todos modos, {w=0.1} ¿verdad?"

    return

# Natsuki discusses her gaming habits
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_gaming",
            unlocked=True,
            prompt="¿Te gustan los videojuegos?",
            category=["Videojuegos", "Contenido"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_gaming:
    if Natsuki.isNormal(higher=True):
        n 1unmaj "¿Videojuegos?"
        n 1fcsbg "Bueno...{w=0.3} ¡dah!"
        n 1fnmbg "¡Claro que me gusta los videojuegos,{w=0.1} [player]!"
        n 1ullss "No diría que soy la jugadora más activa...{w=0.2} pero definitivamente hago mi parte en apretar botones."
        n 1nslsg "Hmm..."
        n 1tnmss "Creo que ni siquiera necesito preguntar,{w=0.1} pero..."
        menu:
            n "¿Qué hay de ti,{w=0.1} [player]?{w=0.2} ¿Juegas a menudo?"

            "¡Claro que sí!":
                $ persistent.jn_player_gaming_frequency = "High"
                n 1fcsbg "¡Si!{w=0.2} Tal y como sospechaba..."
                n 1uchgn "[player] es un mega-friki."
                n 1uchbs "¡Jajaja!"
                n 1uchsm "¡Relájate,{w=0.1} [player]!"
                n 1fllssl "No soy mucho mejor,{w=0.1} después de todo."

            "Juego de vez en cuando.":
                $ persistent.jn_player_gaming_frequency = "Medium"
                n 1fsqsm "Sí,{w=0.1} sí.{w=0.2} Cree lo que quieras creer,{w=0.1} [player]."
                n 1usqbg "Aunque{w=0.1} no tengo claro si creerte."

            "Yo no juego en absoluto.":
                $ persistent.jn_player_gaming_frequency = "Low"
                n 1tnmaj "¿Eh?{w=0.2} ¿En serio?"
                n 1tllaj "¿Ni siquiera de vez en cuando?"

                if jn_activity.has_player_done_activity(jn_activity.JNActivities.gaming):
                    n 1fsqts "Mentiroso.{nw}"

                n 1ncsaj "...Bueno entonces."
                n 1fnmbg "¡Parece que tengo mucho que enseñarte,{w=0.1} [player]!"

    elif Natsuki.isDistressed(higher=True):
        n 1nnmsl "¿Eh?{w=0.2} ¿Videojuegos?"
        n 1nslsl "Sí,{w=0.1} supongo.{w=0.2} Por si te sirve de algo."

    else:
        n 1nsqsl "¿Videojuegos...?"
        n 1fsqsl "...Je.{w=0.2} ¿Por qué,{w=0.1} [player]?"
        n 1fcsan "¿No fue suficiente con pisotear mis sentimientos?"
        n 1fsqfu "¿O también querías ver si podías aplastarme en los juegos?"
        n 1fslsl "..."
        n 1fslaj "...No quiero hablar más de esto.{w=0.2} Esta conversación ya terminó."
        return

    if Natsuki.isNormal(higher=True):
        n 1ullaj "De todas formas,{w=0.1} dejando eso de lado..."
        n 1nsgbg "En cuanto a mis preferencias...{w=0.2} ¡Me gustan los desafíos en los juegos!"
        n 1fcsbg "Juego para ganar{w=0.1} -{w=0.1} ¡soy yo contra los desarrolladores,{w=0.1} y ellos no están para detenerme!"
        n 1fchbg "Jajaja."
        n 1ullss "La verdad es que me gustan más los roguelikes,{w=0.1} para serte sincera."
        n 1fnmsm "Je.{w=0.2} ¿Sorprendido,{w=0.1} [player]?"
        n 1fcsbg "Tener que resistir con garras y dientes,{w=0.1} pensar bien en mis movimientos{w=0.1} -{w=0.1} además es súper satisfactorio aprender todo también."
        n 1fchsm "Y con lo aleatorio que es todo,{w=0.1} ¡siempre resultan reconfortantes y divertidas de jugar!"
        n 1fnmbg "Cada vez que echo una partida, {w=0.1} no tengo ni idea de a qué me enfrento...{w=0.3} y eso es lo que los hace adictivos."
        n 1fcssm "Jejeje.{w=0.2} Pero no te preocupes, [player]."
        n 1fcsbg "No sé si a ti también te gustan esas cosas,{w=0.1} pero..."

        if persistent.jn_player_gaming_frequency == "High":
            n 1fchgn "¡Todavía puedo enseñarte muchas cosas!"

            if Natsuki.isEnamored(higher=True):
                n 1ksqsml "Y apuesto a que también te gustaría,{w=0.1} ¿eh?"
                n 1nchbg "Jajaja."

            elif Natsuki.isAffectionate(higher=True):
                n 1fchbg "¡Y no voy a aceptar un 'no' como respuesta!"

        elif persistent.jn_player_gaming_frequency == "Medium":
            n 1fsqsm "No me importa mostrarte cómo se juega."
            n 1fchbg "¡Soy {i}la{/i} pro,{w=0.1} después de todo!"

        else:
            if jn_activity.has_player_done_activity(jn_activity.JNActivities.gaming):
                n 1fsqts "Eres un mentiroso.{nw}"

            n 1ullaj "Bueno, entonces...{w=0.5}{nw}"
            extend 1usqsm " Estoy segura de que puedo hacer que {i}tú{/i}, de entre toda la gente, te metas en esto."

    else:
        n 1nnmsl "Supongo que lo que más busco es un reto en mis juegos."
        n 1nllsl "Es divertido enfrentarse a los desarrolladores y ganarles en su propio juego."
        n 1nsqaj "Supongo que podría decir que me gusta que me pongan a prueba -{w=0.1} siempre que esté todo bajo control, {w=0.1} claro."
        n 1fsqbo "¿Qué significa eso?{w=0.2} Supongo que te lo dejaré clarito,{w=0.1} [player]."
        n 1fsqan "Realmente {i}no{/i} me gusta el tipo de pregunta que estás haciendo."

    return

# Natsuki talks about her trademark fang, and checks the player is keeping their own teeth healthy
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_natsukis_fang",
            unlocked=True,
            prompt="El colmillo de [n_name]",
            category=["Natsuki"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_natsukis_fang:
    n 1nllbo "..."
    n 1unmaj "¿Eh?{w=0.2} ¿Qué sucede,{w=0.1} [player]?"
    n 1unmsl "..."
    n 1tnmaj "¿Qué?{w=0.2} ¿Tengo algo en la cara?"
    n 1tnmca "..."
    n 1uwdaj "Oh.{w=0.2} Ya veo.{w=0.2} Ahora entiendo."
    n 1nsqss "No puedo evitar notar el colmillo,{w=0.1} ¿verdad?{w=0.2} Jejeje."
    n 1nllss "Sabes..."
    n 1nnmaj "No siempre estuve contenta con mis dientes,{w=0.1} [player]."
    n 1flran "Solía ser muy consciente de ellos.{w=0.2} La gente los señalaba todo el tiempo."
    n 1fcsaj "No fue...{w=0.3} {i}malo{/i} ni nada...{w=0.3} un poco molesto al principio,{w=0.1} pero nada exagerado."
    n 1kslsf "...En su mayoría."
    n 1ulrsl "Pero...{w=0.3} ¿Supongo que he llegado a aceptarlos?"
    n 1fchbg "¡Son como una marca registrada o algo así ahora!{w=0.2} Por eso los cuido mucho."
    n 1fnmsf "¡Más vale que no te descuides con los tuyos,{w=0.1} [player]!"
    n 1fnmaj "Y tampoco me refiero{w=0.1} a saltarte el cepillado regular..."
    n 1fsgss "Sí.{w=0.2} Ambos sabemos a lo que viene,{w=0.2} ¿no?"
    n 1fsqbg "¿Cuándo fue la última vez que {i}usaste{/i} el hilo dental{w=0.1} [player]?{w=0.2} Sé honesto."
    n 1tsqsm "..."
    n 1fchbg "¡Jajaja!{w=0.2} ¿Te he llamado la atención?"
    n 1nlrss "Bueno,{w=0.1} como sea.{w=0.2} Voy a suponer que lo harás después."
    n 1fcsaw "Pero en serio.{w=0.2} ¡Será mejor que te asegures de cuidar tus dientes!"
    n 1fnmaj "Es importante cepillarse los dientes y usar el hilo dental con regularidad,{w=0.1} pero vigila también tu dieta."
    n 1fllsl "No usar el hilo dental no es bueno,{w=0.1} ¡pero las bebidas azucaradas constantes son aún peores!"
    n 1fsgsm "Recuerda,{w=0.1} [player] -{w=0.1} si los ignoras,{w=0.1} desaparecerán~."
    n 1nllss "Pero no, en serio."

    if Natsuki.isLove():
        $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
        n 1kllss "Las sonrisas te quedan bien,{w=0.1} [chosen_endearment]."
        n 1fnmsm "Que sigan viéndose así."
        n 1uchsml "Jejeje.{w=0.2} ¡Te amo,{w=0.1} [player]~!"

    elif Natsuki.isEnamored(higher=True):
        n 1fnmsml "Creo sonreir va contigo,{w=0.1} [player]."
        n 1fchbgl "¡Mantengamos ese aspecto!"

    elif Natsuki.isAffectionate(higher=True):
        n 1usqbg "La sonrisa correcta puede marcar la diferencia,{w=0.1} ya sabes.{w=0.2} ¡Sólo mira la mía!"
        n 1uchgn "Jejeje."

    else:
        n 1unmaj "¿Y si no los cuidas?"
        n 1fllajl "¡No te voy a llevar de la mano al dentista!"

    return

# Natsuki responds to the player confessing their love to her
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_i_love_you",
            unlocked=True,
            prompt="¡Te amo, {0}!".format(n_name),
            category=["Natsuki", "Romance"],
            player_says=True,
            location="classroom",
            affinity_range=(jn_affinity.ENAMORED, None)
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_i_love_you:
    # We use these a lot here, so we define them in a higher scope
    $ player_initial = player[0]
    $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
    $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
    $ chosen_descriptor = random.choice(jn_globals.DEFAULT_PLAYER_DESCRIPTORS)

    # We account for the situation where a player may have unlocked the topic, but never selected it
    # and therefore may have any affection level
    if persistent.jn_player_love_you_count == 0:

        if Natsuki.isLove():
            n 1uscemf "O-{w=0.1}o-{w=0.1}oh por Dios..."
            n 1uskemf "[player_initial]-{w=0.2}[player]...{w=0.3} T-{w=0.1}¡tú...!"
            n 1fcsanf "¡Nnnnnnn-!"
            n 1fbkwrf "¡B-{w=0.1}bueno, ya has tardado bastante!{w=0.2} ¡¿Qué creías que estabas esperando?!"
            n 1flrwrf "¡Apuesto a que estabas esperando a que lo dijera yo primero!"
            n 1fllemf "Cielos,{w=0.1} [player]...{w=0.3} [chosen_tease]..."
            n 1kllemf "Pero..."
            n 1fcswrf "¡P-{w=0.1}pero...!"
            n 1flranf "¡Uuuuuuuh-!"
            n 1fchwrf "Oh,{w=0.1} ¡como sea!{w=0.2} ¡No me importa!{w=0.2} ¡Tengo que decirlo!{w=0.2} ¡Tengo que decirlo!"
            n 1kwdemf "¡[player]!{w=0.2} ¡Yo también te amo!"
            n 1kchbsf "Y-{w=0.1}yo tambien...{w=0.3} te amo..."
            n 1kplbgf "Y...{w=0.3} Y..."
            n 1kchsmf "..."
            n 1kwmsmf "Yo te amo,{w=0.1} [player]..."
            n 1kllsml "..."
            n 1kskemf "¡L-{w=0.1}lo siento...!"
            n 1klrunf "Yo...{w=0.3} vreo que me he dejado llevar un poco..."
            n 1kcssmf "..."
            n 1knmajf "..."
            n 1kbkemf "¡C-{w=0.1}cielos!{w=0.2} ¡Deja de mirarme así!"
            n 1fllemf "A-{w=0.1}ahora estamos los dos en la misma página,{w=0.1} entonces..."
            n 1kllbof "...{w=0.3}E-eso es todo lo que tengo."
            n 1kllsmf "..."
            n 1kllssf "E-{w=0.1}entonces..."
            n 1kplssf "¿Dónde estábamos?{w=0.2} Jejeje..."
            $ Natsuki.calculated_affinity_gain(base=3, bypass=True)

        elif Natsuki.isEnamored(higher=True):
            n 1uscgsf "¡[player_initial]-{w=0.2}[player]!"
            n 1fskgsf "¡T-{w=0.1}tú...!"
            n 1fcsanf "¡Nnnnn-!"
            n 1fbkwrf "S-{w=0.1}sé que hemos estado juntos un tiempo, {w=0.1} ¡pero esto es demasiado repentino!"
            n 1fllwrf "¡Ahora ya está hecho y esto es súper incómodo,{w=0.1} [player]!{w=0.2} ¡¿Por qué tuviste que hacer eso?!"
            n 1fcsemf "¡Cielos!"
            n 1fslpof "...Espero que estés feliz."
            n 1fsqunf "..."
            n 1fnmpof "N-{w=0.1}no creas que esto significa que te {i}odio{/i} o algo así,{w=0.1} aunque..."
            n 1flreml "Es que...{w=0.3} Es que..."
            n 1fcsanl "Eeeeeeh..."
            n 1flrbol "N-{w=0.1}no importa..."
            n 1fcseml "Olvida lo que he dicho."
            n 1kllbof "..."
            $ Natsuki.calculated_affinity_gain(base=2, bypass=True)

        elif Natsuki.isAffectionate(higher=True):
            n 1uskwrf "¿Q-{w=0.1}q-{w=0.1}qué?"
            n 1fwdwrf "¿A-{w=0.1}acabas de...?"
            n 1fcsanf "¡Nnnnnnnnn-!"
            n 1fbkwrf "¡[player_initial]-{w=0.2}[player]!"
            n 1fcsemf "¡¿Estás tratando de hacer que me dé ataque al corazón?!{w=0.2} ¡Cielos!"
            n 1fllemf "No puedes decir cosas así tan de repente..."
            n 1kllunf "..."
            n 1fllajf "Q-{w=0.1}quiero decir..."
            n 1flranf "No es que {i}no{/i} me gustes,{w=0.1} o-{w=0.1}o algo así,{w=0.1} pero..."
            n 1fslanf "¡Pero...!"
            n 1fcsanf "Uuuuuh..."
            n 1fcsajf "¡O-{w=0.1}olvídalo!{w=0.2} N-{w=0.1}no es nada..."
            n 1kslslf "..."
            $ Natsuki.calculated_affinity_gain(bypass=True)

        elif Natsuki.isHappy(higher=True):
            n 1fsqdvl "¡Pffffft!"
            n 1uchbsl "¡Jajaja!"
            n 1tllbgl "¡No puedes hablar en serio,{w=0.1} [player]!{w=0.2} ¡Sólo me estás tomando el pelo!{w=0.2} ¿Cierto?"
            n 1knmbgl "¿Verdad,{w=0.1} [player]?"
            n 1knmajf "¿C-{w=0.1}cierto...?"
            n 1fllunf "..."
            n 1fcsgsf "¡C-{w=0.1}cielos!{w=0.2} ¡Basta de esto!"
            n 1fsqajf "¡No deberías meterte con las chicas así,{w=0.1} [player]!"
            n 1fslpul "T-{w=0.1}tienes suerte de que tenga un gran sentido del humor."
            n 1fnmpol "A-{w=0.1}así que está bien...{w=0.3} por esta vez..."
            n 1fcsajl "Sólo...{w=0.3} ¡piensa un poco antes de soltar cosas!{w=0.2} Dios mío."
            n 1fllslf "[chosen_tease.capitalize()]..."

        elif Natsuki.isNormal(higher=True):
            n 1fscgsf "¡Urk-!"
            n 1fskanf "¿Q-{w=0.1}qué es lo que...?"
            n 1fwdanf "¿Acabas de...?"
            n 1fllajl "..."
            n 1fcsbgf "¡Ja-{w=0.1}jaja!{w=0.2} Quiero decir... {w=0.3} ¡S-{w=0.1}sí!{w=0.2} ¿Quién no me querría,{w=0.1} no?"
            n 1fllbgf "Mi ingenio,{w=0.1} mi estilo,{w=0.1} mi sentido del humor...{w=0.3} Lo tengo todo.{w=0.1} Sí..."
            n 1fbkwrf "¡P-{w=0.1}pero no te confundas o a-{w=0.1}algo parecido!"
            n 1fllssf "Q-{w=0.1}quiero decir, {w=0.1} me alegro de que tengas buen gusto."
            n 1fllunf "Sí..."

        elif Natsuki.isUpset(higher=True):
            n 1fcsan "..."
            n 1fnmfu "En serio, {w=0.1} ¿[player]? {w=0.2} ¿De verdad vas a decirme eso {i}ahora{/i}?"
            n 1fsqfu "La primera vez que eliges decirlo...{w=0.3} ¿y lo dices {i}ahora{/i}?"
            n 1fcspu "..."
            n 1fwman "...¿Y realmente crees que voy a aceptar eso {i}ahora{/i},{w=0.1} [player]?"
            n 1fcsfu "..."
            n 1fcssr "..."
            n 1fsqsr "Ya hemos terminado con esto."
            n 1fsqpu "¿Y si {i}realmente{/i} te sientes así?"
            n 1fsqsf "...¿Entonces por qué {i}no{/i} estás tratando de hacer que esto funcione,{w=0.1} [player]?"
            $ Natsuki.percentage_affinity_loss(10)

        else:
            # :(
            n 1fsqpu "..."
            n 1fcsun "T-{w=0.1}tú..."
            n 1fcsan "Tú...{w=0.3} ¡C-{w=0.1}cómo...!"
            n 1fscwr "¡C-{w=0.1}cómo te {i}atreves{/i} a decirme eso ahora!"
            n 1fscfu "{i}Cómo{w=0.3} te{w=0.3} atreves.{/i}"
            n 1fcsfu "..."
            n 1fcssr "..."
            n 1fsqsr "Tú sabías cómo me sentía,{w=0.1} [player]..."
            n 1fcsan "Lo sabías desde hace mucho tiempo..."
            n 1fsqfu "¿Y ahora?{w=0.2} ¿{i}Ahora{/i} es cuando me lo dices?"
            n 1fsqup "¿Por {i}primera vez{/i}?"
            n 1fcsup "..."
            n 1kplan "Yo...{w=0.3} Yo n-{w=0.1}no puedo aceptar esto ahora."
            n 1kcsan "Eso...{w=0.5} eso duele..."
            n 1kcsfu "..."
            n 1fcspu "Fuera de mi vista,{w=0.1} [player]."
            n 1fcsan "..."
            n 1fsqfu "¡Vete!"
            n 1fscsc "{i}¡Déjame sóla!{/i}{nw}"
            $ Natsuki.percentage_affinity_loss(25)
            return { "quit": None }

        $ persistent.jn_player_love_you_count += 1

    # Standard flows
    else:
        $ persistent.jn_player_love_you_count += 1
        if Natsuki.isLove():

            # At this point, Natsuki is super comfortable with her player, so we can be open and vary things!
            $ random_response_index = random.randint(0, 11)

            if random_response_index == 0:
                n 1unmbgf "Jejeje.{w=0.2} ¡Yo tambien te amo,{w=0.1} [chosen_endearment]!"
                n 1uchsmf "Siempre serás [chosen_descriptor] para mi."
                $ Natsuki.calculated_affinity_gain()
                return

            elif random_response_index == 1:
                n 1tsqssl "Aww,{w=0.1} ¿no me digas?"
                n 1uchbsl "¡Jajaja!"
                $ chosen_endearment = chosen_endearment.capitalize()
                n 1kwmbgf "¡[chosen_endearment],{w=0.1} yo también te amo!"
                n 1fcsbgf "Siempre estaré aquí para apoyarte."
                $ Natsuki.calculated_affinity_gain()
                return

            elif random_response_index == 2:
                n 1uchsmf "Aww,{w=0.1} [chosen_endearment]!{w=0.2} ¡Yo también te amo!"
                n 1klrbgf "Eres lo mejor que me ha pasado."
                $ Natsuki.calculated_affinity_gain()
                return

            elif random_response_index == 3:
                n 1ksqbgf "¿Oh?{w=0.2} Alguien está necesitado hoy,{w=0.1} ¿eh?"
                n 1fsqsmf "Bueno,{w=0.1} ¡estaré encantada de complacerte!"
                n 1uchsmf "¡Yo tambien te amo,{w=0.1} [chosen_endearment]!"
                n 1fchbgf "Sigue sonriendo por mí,{w=0.1} ¿de acuerdo?"
                $ Natsuki.calculated_affinity_gain()
                return

            elif random_response_index == 4:
                n 1flrpof "¿Adulándome como siempre,{w=0.1} [player]?"
                n 1usqssf "Jejeje.{w=0.2} No te preocupes,{w=0.1} ¡No me quejo!"
                n 1uchbgf "¡Yo tambien te amo,{w=0.1} [chosen_endearment]!"
                n 1fcssmf "¡Somos nosotros dos contra el mundo!"
                $ Natsuki.calculated_affinity_gain()
                return

            elif random_response_index == 5:
                n 1fllbgf "Bueno, {w=0.1} p-{w=0.1}por supuesto que sí.{w=0.2} ¡Jajaja!"
                n 1fchbgf "Pero...{w=0.3} ambos sabemos que yo te amo más,{w=0.1} [player]."
                menu:
                    "No, yo te amo más.":
                        n 1fnmbgf "No,{w=0.1} Yo-"
                        n 1tllajl "..."
                        n 1fnmawl "O-{w=0.1}oye...{w=0.3} ¡Espera un momento...!"
                        n 1fchgnl "¡Ya sé a dónde vamos con esto!{w=0.2} ¡Buen intento,{w=0.1} [player]!"
                        n 1fsqsml "Tendrás que aceptar que te amo más,{w=0.1} y así es como son las cosas."
                        menu:
                            "Tú me amas más, y así son las cosas.":
                                n 1uchgnf "Jejeje.{w=0.2} ¿Ves?"
                                n 1fwmsmf "No fue tan difícil, {w=0.1} ¿verdad?"
                                n 1nchbgf "¡Te amo tanto,{w=0.1} [player]~!"

                    "Esta bien.":
                        n 1uchgnl "¡Pfffft!{w=0.2} ¡Jajaja!"
                        n 1fwltsf "¡Vamos,{w=0.1} [player]!{w=0.2} ¿Dónde está tu espíritu de lucha?"
                        n 1fchsmf "Bueno,{w=0.1} como sea.{w=0.2} Me alegro de que aceptes la verdad."
                        n 1uchsmf "Jejeje."

                $ Natsuki.calculated_affinity_gain()
                return

            elif random_response_index == 6:
                n 1uchsmf "Jejeje...{w=0.3} Siempre adoro oír eso de ti,{w=0.1} [player]."
                n 1usqsmf "...Y creo que puedo adivinar que a ti también te gusta oírlo."
                n 1uchbgf "¡Yo tambien te amo,{w=0.1} [chosen_endearment]!"
                n 1nchsmf "No necesito a nadie más~."
                $ Natsuki.calculated_affinity_gain()
                return

            elif random_response_index == 7:
                n 1nsqajl "Guau,{w=0.1} [player]..."
                n 1tslajl "Hoy estás realmente hecho un desastre,{w=0.1} ¿no es así?"
                n 1tsldvl "Asco..."
                n 1fchbgf "...Pero justo el tipo de asquerosidad que me gusta.{w=0.2} Jejeje."
                n 1uchbgf "¡Yo tambien te amo,{w=0.1} [chosen_endearment]!"
                n 1unmsmf "Siempre te cubriré la espalda."
                $ Natsuki.calculated_affinity_gain()
                return

            elif random_response_index == 8:
                n 1uchsmf "Jejeje."
                n 1nchssf "Yo..."
                n 1uchbsf "¡tambien te aaaaaaaaaaaamo,{w=0.1} [player]!"
                n 1kwmsmf "Siempre serás mi apoyo."
                $ Natsuki.calculated_affinity_gain()
                return

            elif random_response_index == 9:
                n 1fllsmf "Quiero decir...{w=0.3} que es muy dulce de tu parte y todo,{w=0.1} [player]..."
                n 1fsqsmf "Pero ambos sabemos que te amo más~."
                $ player_is_wrong = True
                $ wrong_response_count = 0

                # Natsuki won't lose!
                while player_is_wrong:
                    menu:
                        "No, ¡yo te {i}amo{/i} más!":

                            if wrong_response_count == 1:
                                n 1fsqbgl "¿Hmm?{w=0.2} ¿Me has escuchado mal{w=0.1} [player]?"
                                n 1fchbgf "He dicho que yo te {i}amo{/i} más,{w=0.2} [chosen_tease]!"

                            elif wrong_response_count == 5:
                                n 1fsqbgl "¿Oh?{w=0.2} Eres competitivo,{w=0.1} ¿verdad?"
                                n 1fslbgl "Jejeje.{w=0.2} Tonto [player].{w=0.1} ¿Nunca te lo dijo nadie?"
                                n 1fchgnl "¡No empieces una pelea que no puedas terminar!"
                                n 1fchbgf "Especialmente esta -{w=0.1} ¡te {i}amo{/i} más~!"

                            elif wrong_response_count == 10:
                                n 1tsqbgl "¿Ooh?{w=0.2} ¡Nada mal,{w=0.1} [player]!"
                                n 1fsqbgl "Casi admiro su terquedad..."
                                n 1uchsmf "¡Pero no tanto como te admiro a ti!{w=0.2} ¡Yo te {i}amo{/i} más!"

                            elif wrong_response_count == 20:
                                n 1fsqbgl "Jejeje.{w=0.2} ¡Eres persistente!{w=0.2} Lo reconozco."
                                n 1fsqsml "Pero si crees que te estoy dando la victoria..."
                                n 1fchgnl "¡Entonces te espera otra cosa!"
                                n 1uchbgl "¡Yo te {i}amo{/i} más,{w=0.1} tonto!"

                            elif wrong_response_count == 50:
                                n 1tnmajl "¡Guau!{w=0.2} Esto es como...{w=0.3} ¡la 50va vez que te equivocas! {w=0.2} ¡De forma consecutiva!"
                                n 1tsqsgl "Me parece que estás en un ciclo de negación,{w=0.1} [player]~."
                                n 1nllssl "No creo que pueda molestarme en contar mucho más a partir aquí..."
                                n 1fsqtsl "Así que, ¿por qué no me haces un favor y aceptas que yo te {i}amo{/i} más de una vez?"
                                n 1uchsml "Jejeje."
                                n 1fchbgl "¡Gracias,{w=0.1} [chosen_endearment]~!"

                            elif wrong_response_count == 100:
                                n 1uwdgsl "...¡Oh!{w=0.2} ¡Y parece que tenemos nuestra 100va respuesta errónea!"
                                n 1fllawl "¡Apaguen las luces! {w=0.2}¡Que suene la música!"
                                n 1flrbgl "Ahora,{w=0.1} miembros del público -{w=0.1} ¿qué obtiene nuestro obstinado participante?"
                                n 1fsqbgl "El ganó..."
                                n 1uchgnl "¡Tenemos una corrección!{w=0.2} ¡Guau!"
                                n 1fsqbgl "Y esa corrección es..."
                                n 1fchbsf "¡[n_name] te {i}ama{/i} mucho más!{w=0.2} ¡Felicidades,{w=0.1} idiota!"
                                n 1fsqdvl "Y ahora, {w=0.1} para ganar el gran premio -{w=0.1} todo lo que nuestro invitado tiene que hacer..."
                                n 1fchbsl "...¡es rendirse y admitir lo equivocado que está~!{w=0.2} Jejeje."

                            else:
                                $ player_is_wrong_responses = [
                                    "¡Nope!{w=0.2} ¡Yo te {i}amo{/i} más!",
                                    "¡Lo siento,{w=0.1} tontito!{w=0.2} ¡Definitivamente yo te {i}amo{/i} más!",
                                    "Jejeje.{w=0.2} ¡Nope~!{w=0.2} Ambos sabemos que te {i}amo{/i} más.",
                                    "Hmm...{w=0.3} nop.{w=0.2} ¡Seguro que te {i}amo{/i} yo más!",
                                    "¡Nooooop~!{w=0.2} ¡Yo te {i}amo{/i} más!",
                                    "Tonto [player]~.{w=0.2} Yo te {i}amo{/i} más,{w=0.1} ¿recuerdas?",
                                    "Mmmmmmmm...{w=0.3} ¡nope!{w=0.2} ¡Yo te amo {i}mucho{/i} más,{w=0.1} [player]~!",
                                    "Vamos, vamos,{w=0.1} [player].{w=0.2}  ¡No seas tonto!{w=0.2} Definitivamente te {i}amo{/i} más.",
                                    "Espera...{w=0.3} ¿puedes oír eso?{w=0.2} ¡Oh!{w=0.2} Es lo equivocado que estás -{w=0.1} ¡yo te amo más,{w=0.1} tonto!"
                                    "Sólo estás perdiendo el tiempo, {w=0.1} [player]~.{w=0.2} ¡Te amo {i}mucho{/i} más!",
                                    "Vaya,{w=0.1} vaya,{w=0.1} [player].{w=0.2} ¿No sabes que yo te amo {i}más{/i} a estas alturas?{w=0.2} Jejeje.",
                                    "Oh oh...{w=0.3} Nat te escucha,{w=0.1} Nat sabe que estás equivocado.{w=0.1} Te amo {i}más{/i},{w=0.1} ¡bobo!",
                                    "Eres adorable cuando te niegas,{w=0.1} [player].{w=0.2} Jejeje.{w=0.2} ¡Yo te {i}amo{/i} más~!",
                                    "Aww,{w=0.1} vamos,{w=0.1} [player].{w=0.2} Si {i}realmente{/i} me amaras,{w=0.2} admitirías que te {i}amo{/i} más."
                                ]
                                $ chosen_random_response = renpy.substitute(random.choice(player_is_wrong_responses))
                                n 1fchbgf "[chosen_random_response]"

                            $ wrong_response_count += 1

                        "Bueno, está bien. Me amas más.":
                            $ player_is_wrong = False
                            n 1tsqbgl "¿Ves?{w=0.2} ¿Era realmente tan difícil?"
                            n 1uchtsl "A veces hay que admitir que uno se equivoca,{w=0.1} [player]~."
                            n 1nchsml "Jejeje."

                            if wrong_response_count >= 10:
                                n 1nsqsml "¡Buen intento,{w=0.1} pese a todo~!"

                            $ Natsuki.calculated_affinity_gain()
                            return

            elif random_response_index == 10:
                n 1ksqsml "Jejeje.{w=0.2} Nunca me cansaré de oír eso de ti,{w=0.1} [player]."
                n 1uchsmf "¡Yo también te amo!"
                n 1uchbgf "Eres mi número uno~."
                $ Natsuki.calculated_affinity_gain()
                return

            else:
                n 1usqbgf "¿Oh?{w=0.2} ¿Tan cariñoso como siempre?"
                n 1uslsmf "Eres tan dulce,{w=0.1} [player].{w=0.2} Jejeje."
                n 1uchbgf "Pero...{w=0.3} ¡No me voy a quejar!{w=0.2} ¡Yo también te amo,{w=0.1} [chosen_endearment]!"
                n 1uchsmf "Siempre me haces sentir bien."
                $ Natsuki.calculated_affinity_gain()
                return

            return

        elif Natsuki.isEnamored(higher=True):
            n 1fbkwrf "¡A-{w=0.1}agh!{w=0.2} ¡[player]!"
            n 1fllwrf "¿Qué dije sobre hacer las cosas incómodas?{w=0.2} ¡Ahora es el doble de incómodo!"
            n 1fcsemf "Cielos..."
            n 1flremf "Vamos a hablar de algo, {w=0.1} ¿de acuerdo?"
            n 1flrpof "¡P-{w=0.1}puedes adularme en el momento {i}apropiado{/i}!"
            n 1klrpof "Tonto..."
            $ Natsuki.calculated_affinity_gain()
            return

        elif Natsuki.isHappy(higher=True):
            n 1fskemf "¡O-{w=0.1}oye! ¡Pensé que te había dicho que no salieras con cosas así!"
            n 1fllemf "Cielos..."
            n 1fcsemf "N-{w=0.1}no sé si estás tratando de ganarme,{w=0.1} o qué..."
            n 1fcspof "¡Pero vas a tener que esforzarte mucho más que eso!"
            return

        elif Natsuki.isNormal(higher=True):
            n 1fskemf "¡A-{w=0.1}agh!"
            n 1fbkwrf "¡[player_initial]-{w=0.1}[player]!"
            n 1fnmanl "¡Deja de ser asqueroso!"
            n 1fcsanl "Cielos..."
            n 1fllajl "No sé si crees que esto es una broma,{w=0.1} o qué..."
            n 1fsqaj "Pero a mí no me hace gracia,{w=0.1} [player]."
            return

        elif Natsuki.isUpset(higher=True):
            n 1fcssr "..."
            n 1fsqsr "Hablar no cuesta nada,{w=0.1} [player]."
            n 1fsqaj "Si {i}realmente{/i} te importo..."
            n 1fsqpu "Entonces {i}pruebalo{/i}."
            $ Natsuki.percentage_affinity_loss(2.5)
            return

        else:
            n 1fsqpu "..."
            n 1fsqan "Eres realmente increíble,{w=0.1} [player]."
            n 1fsqfu "¿Entiendes {i}siquiera{/i} lo que estás diciendo?"
            n 1fcsfu "..."
            n 1fcspu "¿Sabes qué?{w=0.2} Como sea.{w=0.2} Ya no me importa."
            n 1fsqfu "Di lo que quieras,{w=0.1} [player].{w=0.2} Es todo basura,{w=0.1} al igual que todo sobre ti."
            $ Natsuki.percentage_affinity_loss(2)
            return

    return

# Natsuki discusses her trademark hairstyle with the player
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_natsukis_hairstyle",
            unlocked=True,
            prompt="¿Por qué te peinas así?",
            category=["Moda"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_natsukis_hairstyle:
    if Natsuki.isEnamored(higher=True):
        n 1unmaj "¿Hmm?{w=0.2} ¿Mi peinado?"
        n 1fsgsg "¿Por qué lo preguntas{w=0.1} [player]?{w=0.2} ¿Buscas una estilista?"
        n 1fchsm "Jejeje."

    elif Natsuki.isNormal(higher=True):
        n 1unmaj "¿Eh?{w=0.2} ¿Mi peinado?"
        n 1fsqaj "Espera...{w=0.3} ¿Me estás tomando el pelo?{w=0.2} ¿Qué quieres decir?"
        n 1fllpo "Será mejor que no te estés burlando de mí,{w=0.1} [player]..."

    elif Natsuki.isDistressed(higher=True):
        n 1nnmsl "...¿Eh?{w=0.2} Oh.{w=0.2} Mi peinado."
        n 1flrsl "Yo estoy...{w=0.3} sorprendida que te preocupes tanto como para preguntar por eso."

    else:
        n 1fsqsl "Porque me gusta así.{w=0.2} ¿Es suficiente para ti?"
        n 1fsqan "¿Por qué te importaría de todos modos?{w=0.2} No te has preocupado por mí hasta ahora."
        n 1fslpu "Tarado."
        return

    n 1nnmpu "Bueno,{w=0.1} de todas formas."
    n 1ullpu "Nunca lo había pensado tanto,{w=0.1} honestamente."

    if Natsuki.isNormal(higher=True):
        if persistent.jn_natsuki_current_hairstyle == "default":
            n 1ulrpo "Sólo pensé que las coletas dobles me quedarían muy bien."

        else:
            n 1ulrpo "Sé que no las tengo puestas ahora,{w=0.1} pero pensé que las coletas dobles se verían muy bien en mí."

        n 1fsqpo "...Sí, {w=0.1} sí. {w=0.2} Sé lo que estás pensando,{w=0.1} [player]."

        if Natsuki.isEnamored(higher=True):
            n 1ksqsm "¿Me equivoqué...?"
            n 1fchbg "Jejeje.{w=0.2} Yo pensé que no."

    else:
        if persistent.jn_natsuki_current_hairstyle == "default":
            n 1nnmsl "Supongo que me gustaba la idea de las coletas dobles."

        else:
            n 1nnmsl "No es que las lleve ahora,{w=0.1} pero supongo que me gustaba la idea de las coletas dobles."

    n 1ulraj "En cuanto al flequillo,{w=0.1} yo...{w=0.3} siempre encontré difícil cortarme el cabello."

    if Natsuki.isNormal(higher=True):
        n 1flraj "Es que cuesta tanto, {w=0.1} ¿sabes? {w=0.2} ¡Es super tonto!"
        n 1fnman "Como... {w=0.3} ¡No lo entiendo en absoluto!"
        n 1fllan "Y lo más molesto es que si fuera un chico, {w=0.1} ¡sería mucho más barato! {w=0.2} ¿Qué pasa con eso?"
        n 1ncssl "Agh...{w=0.3} pero sí."

    else:
        n 1nlrsl "Siempre fui un poco breve a la hora de cortarlo."
        n 1fsqsl "...Y no, {w=0.1} {i}no{/i} en el sentido físico."

    if persistent.jn_natsuki_current_accessory is not None:
        n 1ullaj "En cuanto a mi pinza para el cabello...{w=0.2} Es sólo para mantener mi cabello fuera de mis ojos."

    else:
        n 1ullaj "Ahora no lo llevo, {w=0.1} pero la pinza de cabello es sólo para mantener mi cabello fuera de mis ojos."

    if Natsuki.isNormal(higher=True):
        n 1fllss "Lucir bien es una ventaja, {w=0.1} pero sobre todo me cansé de quitarme el cabello de la cara."
        n 1nsrca "¡Especialmente con un flequillo tan largo!"
        n 1unmaj "En fin..."

    n 1tllaj "¿Qué si he pensado en otros peinados?{w=0.2} Bueno..."

    if persistent.jn_natsuki_current_hairstyle != "default":
        n 1ullbo "Creo que eso habla por sí mismo, {w=0.1} realmente. {w=0.2} Estoy probando uno diferente..."

    if Natsuki.isEnamored(higher=True):
        $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
        n 1usgss "Sin embargo, do otra forma,{w=0.1} [player]..."
        n 1fcssml "Estoy bastante segura de que ya me he soltado el pelo contigo,{w=0.1} [chosen_tease].{w=0.2} Eso cuenta, ¿verdad?"
        n 1uchgnl "¡Jajaja!"

    elif Natsuki.isNormal(higher=True):
        n 1unmaj "Ya sabes lo que dicen,{w=0.1} [player]."
        n 1fnmbg "Si no está dañado,{w=0.1} no lo arregles."
        n 1uchgn "Jejeje."

    else:
        n 1fslaj "...En este momento,{w=0.1} [player]...{w=0.2} Preferiría que te mantuvieras alejado de mi cabello."
        n 1fsqbo "Gracias."

    return

# Natsuki provides guidance on how to stay true to yourself and your values
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_integrity",
            unlocked=True,
            prompt="Tener integridad",
            category=["Sociedad", "TÚ"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, jn_affinity.LOVE),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_integrity:
    n 1ullaj "Sabes,{w=0.1} [player]..."
    n 1nnmaj "Siento que hoy en día,{w=0.1} todo el mundo está tratando de distinguirse de los demas,{w=0.1} o predicar algo."
    n 1flrem "Especialmente con las redes sociales y todo eso por todas partes -{w=0.1} ¡es una locura!"
    n 1fllem "Como...{w=0.3} hay posts diciendo que esto es malo,{w=0.1} otros preguntando por qué no apoyas otra cosa..."
    n 1fcsan "Y por supuesto, {w=0.1} ¡{i}todo el mundo{/i} está dea acuerdo con eso -{w=0.1} por lo que se filtra en la vida real también!"
    n 1flrsl "Uf... {w=0.3} no puedo ser sólo yo la que lo encuentra todo agotador,{w=0.1} ¿verdad?"
    n 1unmaj "Creo que es un poco fácil perder la noción de lo que realmente te gusta, {w=0.1} o lo que defiendes."
    n 1ullaj "Lo cual... {w=0.3} es algo de lo que realmente quería hablarte,{w=0.1} [player]."
    n 1fllpu "No estoy diciendo que debas ignorar a todos los demás,{w=0.1} o que nunca consideres otros puntos de vista."
    n 1fnmpo "Eso es ser un ignorante."
    n 1knmaj "Pero...{w=0.3} no dejes que las opiniones o concepciones de los demás sobrescriban completamente las tuyas,{w=0.1} ¿vale?"
    n 1fnmbo "No sin poner resistencia, {w=0.1} al menos."
    n 1fnmpu "{i}Tú{/i} eres tu propio maestro,{w=0.1} [player] -{w=0.1} tienes tus propias opiniones,{w=0.1} tus propios valores:{w=0.1} ¡y eso es súper importante!"
    n 1fcsbg "Quiero decir, {w=0.1} ¡mírame!"
    n 1fllaj "¿Y qué pasa si alguien dice que lo que me gusta es una basura?{w=0.2} ¿O si debería seguir algo más popular?"
    n 1fnmsf "No hace daño a nadie, {w=0.1} así que ¿quiénes son ellos para juzgar y decirme lo que debo disfrutar?"
    n 1fcsbg "Es mi vida, {w=0.1} ¡así que pueden seguir adelante!"
    n 1nnmsr "De todos modos...{w=0.3} Supongo que lo que quiero decir es que no tengas miedo de defender lo que te importa,{w=0.1} [player]."
    n 1fcsaj "Habrá veces que te equivocarás, {w=0.1} ¡pero no dejes que te afecte!"
    n 1flrsl "Simplemente no me gusta la idea de que se empuje a la gente a lo que no es correcto para ellos."
    n 1nnmpu "Dicho esto,{w=0.1} [player]..."

    if Natsuki.isEnamored(higher=True):
        n 1ksqsm "Estoy bastante segura de que ambos sabemos lo que es bueno para el otro a estas alturas,{w=0.1} ¿eh?"
        n 1fcsbgl "Jajaja."

        if Natsuki.isLove():
            n 1uchsml "¡Te amo,{w=0.1} [player]~!"

    elif Natsuki.isAffectionate(higher=True):
        n 1ksqsm "Estoy bastante segura de que sé lo que te conviene..."
        n 1fcsbgl "¡Pasando más tiempo conmigo!{w=0.2} Jajaja."

    else:
        n 1unmss "Seguro que puedo ayudarte a encontrar lo que te conviene."
        n 1fllss "Para eso están los amigos,{w=0.1} ¿no?"
        n 1fcsbg "¡Especialmente los que son como yo!{w=0.2} Jejeje."

    return

# Natsuki discusses her favourite animal
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_favourite_animal",
            unlocked=True,
            prompt="¿Cuál es tu animal favorito?",
            category=["Animales", "Naturaleza"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_favourite_animal:
    if Natsuki.isNormal(higher=True):
        n 1fsqsr "El hámster."
        n 1fcssm "Eso no llega ni a pregunta para mí,{w=0.1} [player]."
        n 1uwdaj "A ver...{w=0.3} si alguna vez has visto a alguno,{w=0.1} ¿podrías reprochármelo?"
        n 1fcspu "Son...{w=0.5}{nw}"
        n 1fspgs "¡¡{i}Adorables{/i}!!"
        n 1fbkbsl "Simplemente me encanta todo sobre ellos...{w=0.3} sus pequeñas patitas,{w=0.1} esos ojitos brillantitos, esas mejillas acolchaditas..."
        n 1fspbgl "Y esa colita chiquita...{w=0.3} ¡Oh Dios mío!{w=0.2} ¡Son preciosos!"
        n 1fllan "Me molesta bastante cuando alguien dice que son aburridos,{w=0.1} o que no dan afecto.{w=0.2} Es como...{w=0.3} ¿Qué clase de hámster has visto?"
        n 1fnmaj "Todos ellos tienen sus mini personalidades,{w=0.1} como cualquier otro animal -{w=0.1} ¡pero chiquito!"
        n 1uwdaj "Y si eres bueno con ellos,{w=0.1} no van a tener miedo a enseñártelas -{w=0.1} he visto un montón de videos de ellos siguiendo a sus amos por ahí,{w=0.1} ¡incluso trepando por sus manitas!"
        n 1fchbg "¡Además,{w=0.1} son muy fáciles de cuidar!"
        n 1fchsm "Solo hay que ponerles comida y agua todos los días,{w=0.1} y limpiar su jaula una vez a la semana -{w=0.1} no hace falta esforzarse."
        n 1nllpu "Hmm..."
        n 1unmpu "Sabes,{w=0.1} [player]...{w=0.3} Aquí todo es muy aburrido cuando no estás por aquí,{w=0.1} no sé si ves por donde voy..."
        n 1fnmsm "¿Tal vez un día podríamos tener nuestro propio amiguito peludito?{w=0.1} Jejeje."
        n 1fllss "Y no te preocupes,{w=0.1} [player]..."
        n 1ucssm "Por que no tengo pensado ser quien cuide de él."
        n 1fchgn "...¡Así que tú te quedas encargado de eso!"

        if Natsuki.isEnamored(higher=True):
            n 1fchbg "Oh,{w=0.1} y relájate -{w=0.1} ¡yo me encargaré de que esté bien domesticado!"
            n 1uslbg "O..."
            n 1usqts "Al menos tanto como tú lo estás ,{w=0.1} eh [player]?{w=0.2} ¡Jajaja!"

            if Natsuki.isLove():
                n 1uchbg "¡Te quiero~!"

    elif Natsuki.isDistressed(higher=True):
        n 1fsqpu "El hámster,{w=0.1} si es que siquiera importa."
        n 1fllpu "¿Por qué?{w=0.2} Ni idea.{w=0.2} Creo que simplemente son monos."
        n 1nllbo "Además,{w=0.1} creo que la gente subestima lo expresivos que pueden ser."
        n 1nnmbo "Son como el resto de los animales -{w=0.1} y como tal todos tienen sus pequeñas personalidades."
        n 1nnmaj "Supongo que además son fáciles de cuidar,{w=0.1} así que esa es otra."
        n 1nlrsl "..."
        n 1flrsl "...Te mentiría si te dijera que no he pensado en conseguirme uno para mi..."
        n 1fsqpu "¿Pero siendo honesta,{w=0.1} [player]?{w=0.2} ¿Si has demostrado no poder cuidar de {i}mí{/i}?"
        n 1fcsan "...Entonces no quiero ni pensar en traer uno aquí,{w=0.1} tampoco.{w=0.2} Jeh."

    else:
        n 1fsqpu "Jeh.{w=0.2} ¿En serio?{w=0.2} ¿Qué cuál es mi animal favorito...?"
        n 1fcsan "Tu no,{w=0.1} [player].{w=0.2} Eso por supuesto."

    return

# Natsuki discusses her favourite drink
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_favourite_drink",
            unlocked=True,
            prompt="¿Cuál es tu bebida favorita?",
            category=["Comida"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_favourite_drink:
    if Natsuki.isAffectionate(higher=True):
        n 1unmbg "¡Ooooh!{w=0.2} ¿Mi bebida favorita?"

    elif Natsuki.isNormal(higher=True):
        n 1unmaj "¿Mmm?{w=0.2} ¿Mi bebida favorita?"

    elif Natsuki.isDistressed(higher=True):
        n 1nllbo "¿Eh?{w=0.2} Oh.{w=0.1} Mi bebida favorita."

    else:
        n 1fslsf "...No entiendo por que te importa,{w=0.1} [player]."
        n 1fsqsf "Así que...{w=0.3} ¿Por qué debería decírtelo?"
        n 1fsqan "El agua.{w=0.2} Ahí tienes la respuesta que querías.{w=0.2} ¿Feliz?"
        n 1fcsan "Ahora vete..."
        return

    if Natsuki.isNormal(higher=True):
        n 1ullaj "Si tuviera que decidir...{w=0.3} es que depende del clima mas que nada."
        n 1tnmaj "Quiero decir...{w=0.3} ¡¿Qué clase de idiota pediría un granizado en medio del invierno?!"
        n 1fllss "Pero dicho eso..."
        n 1fcsbg "Si hace frio,{w=0.1} entonces lo mejor es un chocolate caliente.{w=0.2} No tengo pruebas,{w=0.1} pero tampoco dudas.."
        n 1uchgn "En pleno invierno,{w=0.1} ¡definitivamente no vas a encontrar mejor opción que eso!"

        if Natsuki.isAffectionate(higher=True):
            n 1fcsbg "Y por supuesto,{w=0.1} [player] -{w=0.1} nata montada,{w=0.1} malvaviscos -{w=0.1} métele de todo.{w=0.2} Van perfectamente juntos."
            n 1uchgn "...¡No aceptaría nada más!"
            n 1fllbg "Quiero decir,{w=0.1} piénsalo -{w=0.1} si vas a tomar chocolate caliente,{w=0.1} tu salud ya se va un poco al carajo."
            n 1uchgn "¿Así que por que no ir a por todas,{w=0.1} cierto?{w=0.2} Jajaja."

            if Natsuki.isLove():
                n 1fcsdvl "Igualmente,{w=0.2} no me preocupa -{w=0.1} nos dividimos las calorías,{w=0.1} [player]~."

        n 1unmaj "Y para cuando hace calor...{w=0.3} Eso ya está mas complicado,{w=0.1} de hecho."
        n 1fslsr "Déjame pensar..."
        n 1fsrsr "..."
        n 1fchbs "¡Aja!{w=0.2} ¡Ya lo se!"
        n 1unmbg "Serian esos batidos fresquitos,{w=0.1} ¡pero de uno de esos sitios que te dejan elegir que llevan!"
        n 1fsqsm "Y no me refiero a elegir un sabor,{w=0.1} [player]..."
        n 1fchgn "¡Me refiero a elegir los ingredientes con los que se hacen!"
        n 1fllss "Bueno...{w=0.3} hasta que se mezcla,{w=0.1} de todos modos."
        n 1ncssm "Cualquier tipo de dulces,{w=0.1} cualquier tipo de lácteo..."

        if Natsuki.isAffectionate(higher=True):
            n 1ucssm "¿Y si tuviera que elegir uno?"
            n 1fcsbg "Seria de fresa y nata,{w=0.1} obviamente."
            n 1fllbgl "Y...{w=0.3} ¿tal vez con sirope de chocolate también?{w=0.2} Jejeje."

        else:
            n 1fchbg "Si.{w=0.2} ¡Ahí está la cosa!"

        n 1fllpo "Dios...{w=0.3} Tanto hablar de bebidas me ha dado sed,{w=0.1} de hecho.{w=0.2} Así que en ese sentido..."
        n 1fnmbg "Tienes que hidratarte bien,{w=0.1} [player] -{w=0.1} ¡sin importar el tiempo que haga!"

    else:
        n 1flrsl "Supongo que depende de como esté el clima."
        n 1fnmbo "Chocolate caliente si hace frio,{w=0.1} aunque tampoco soy de pedir mucho."
        n 1fllaj "Y para cuando hace calor..."
        n 1fllsl "Realmente no tengo idea.{w=0.2} Cualquier cosa está bien."
        n 1fsqsl "Jeh.{w=0.2} Aunque por como me has tratado,{w=0.1} no podría esperar mas que agua del grifo por tu parte.{w=0.2} ¿Me equivoco,{w=0.1} [player]?"

    return

# Natsuki complains about her school uniform
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_school_uniform",
            unlocked=True,
            prompt="¿Qué opinas de tu uniforme escolar?",
            category=["Moda"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_school_uniform:
    if Natsuki.isLove():
        n 1fsqctl "¿Ojo?{w=0.2} ¿Acaso a [player] le gustan las chicas en uniforme?"
        n 1ksqaj "Guau...{w=0.3} Eres incluso {i}más{/i} guarro de lo que pensaba."
        n 1fsqsm "..."
        $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
        n 1uchgn "¡Oh, vamos,{w=0.1} [chosen_tease]!{w=0.2} ¡Siempre pones mala cara cuando te llamo guarro!{w=0.2} No puedo resistirme."
        n 1fchsm "Jejeje.{w=0.2} Igualmente..."

    elif Natsuki.isAffectionate(higher=True):
        n 1unmaj "¿Eh?{w=0.2} ¿Mi uniforme escolar?"
        n 1fsqsm "...Jejeje."
        n 1fcsbgl "¿Por qué preguntas,{w=0.1} [player]?{w=0.2} ¿Acaso {i}tú{/i} querías probártelo o algo así?"
        n 1fchgn "¡Oh!{w=0.2} ¡Podemos jugar a los disfraces!{w=0.2} ¿No te gustaría hacer eso,{w=0.1} [player]?{w=0.2} ¡Va a ser muy divertido!"
        n 1uchbs "Apuesto a que te puedo convertir en una niñita adorable~.{w=0.1} ¡Jajaja!"
        n 1nllss "Bueno igualmente,{w=0.1} dejándonos de bromas..."

    elif Natsuki.isNormal(higher=True):
        n 1tnmaj "¿Mi uniforme escolar?{w=0.2} Eso es...{w=0.3} algo raro de lo que preguntar,{w=0.1} ¿eh?"
        n 1nslaj "Bueno,{w=0.1} como sea.{w=0.2} Lo dejare pasar...{w=0.3} por esta vez."

    elif Natsuki.isDistressed(higher=True):
        n 1nsraj "...¿Eh?{w=0.2} Oh,{w=0.1} el uniforme escolar."
        n 1nsqsl "Yo...{w=0.3} no se que esperabas que te dijera,{w=0.1} [player]."
        n 1fsqsl "Lo tengo que usar para las clases.{w=0.2} Para eso está hecho el uniforme,{w=0.1} por si aún no te habías dado cuenta."
        n 1fsrsf "No importa si me gusta o no."
        n 1fsqbo "...Y todavía menos que te guste a ti."
        return

    else:
        n 1fsran "Jeh.{w=0.2} Me gusta más que {i}tú{/i}.{w=0.2} Desgraciado."
        return

    n 1unmaj "Esta bien,{w=0.1} supongo.{w=0.2} ¡La verdad me gustan mucho los colores cálidos!"
    n 1nnmss "Entran mejor por los ojos que otros uniformes que he visto por ahí."
    n 1nsqsr "Pero Oh.{w=0.2} Dios.{w=0.2} Mio.{w=0.2} [player]."
    n 1fcsan "Las capas.{w=0.2} Demasiadas capas de ropa."
    n 1fllem "¡¿Quién demonios necesita tanta ropa?!{w=0.2} Para la escuela,{w=0.1} no,{w=0.1} ¡¿para cualquier sitio?!"
    n 1fbkwr "Quiero decir...{w=0.3} ¡¿Siquiera {i}sabes{/i} lo que es vestir todo eso en verano?!{w=0.2} ¡Es un horror!"
    n 1flrpo "Y el jersey...{w=0.3} ¡agh!{w=0.2} Es la peor cosa que han inventado jamás."
    n 1fsqpo "Es como, si,{w=0.1} podría quitarme algo entre clase y clase,{w=0.1} pero tendría que ponérmelo una vez empiece la siguiente clase."
    n 1fllpo "...Eso, o ser regañada.{w=0.2} {i}Otra vez{/i}.{w=0.2} Honestamente, no se como Sayori no sale perjudicada por ir siempre tan descuidada."
    n 1fcsan "¡Hablando de una patada en la boca!{w=0.2} ¡Para colmo es super caro!"
    n 1fslan "Joder."
    n 1fslsr "Agh...{w=0.3} En serio, desearía que los uniformes estuvieran prohibidos o algo por el estilo."
    n 1flrpo "Aunque podría ser peor,{w=0.1} supongo.{w=0.2} Al menos nunca he tenido que aprender como atar una corbata."
    n 1unmaj "¿Y tú qué, [player]?"
    menu:
        n "¿Tenéis un uniforme escolar en tu escuela?"

        "Si, tuve que llevar uniforme.":
            n 1fcsbg "¡Aja!{w=0.2} Entonces sabes el sufrimiento que conlleva,{w=0.1} ¿eh?"

        "No, nunca he llevado uniforme.":
            n 1fslsr "..."
            n 1fsqsr "...Suertudo."

        "Todavía tengo que usarlo.":
            n 1fchgn "¡Entonces acepta mis condolencias,{w=0.1} [player]!{w=0.2} Jajaja."
            n 1fcsbg "Es bueno saber que somos tan parecidos,{w=0.1} supongo."

    n 1ullss "Bueno,{w=0.1} igualmente..."

    if Natsuki.isLove():
        n 1fllss "Todavía no me {i}gusta{/i} precisamente llevarlo..."
        n 1uslbgl "Pero...{w=0.3} Creo que podría aguantarlo.{w=0.2} Solo para ti,{w=0.1} [player]~."
        n 1usrdvl "Jejeje."

    elif Natsuki.isAffectionate(higher=True):
        n 1usrdvl "¿S-{w=0.1}si no te importa,{w=0.1} [player]?"
        n 1fllbgl "Supongo que podría soportar llevarlo un rato,{w=0.1} a-{w=0.1}al menos..."

    elif Natsuki.isNormal(higher=True):
        n 1fchgn "Supongo que al menos estaré calentita y arropada durante el invierno,{w=0.1} ¿cierto?{w=0.2} Jajaja."

    return

# Natsuki laments how she's never travelled abroad by plane
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_flying",
            unlocked=True,
            prompt="¿Has volado alguna vez?",
            category=["Transporte"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_flying:
    if Natsuki.isEnamored(higher=True):
        n 1uwdbg "¡Ooh!{w=0.2} ¿Volar?{w=0.2} ¿Cómo, en avión?"
        n 1fllun "Nnn...{w=0.3} Desearía contestar que si,{w=0.1} [player]..."
        n 1fchbg "¡Pero no me malinterpretes!{w=0.2} ¡Con {i}total{/i} seguridad volaría a algún lugar si pudiera!"
        n 1fslsl "Es solo que...{w=0.3} todo eso es muy caro,{w=0.1} ¿sabes?"
        n 1kllsl "Nunca he tenido un pasaporte,{w=0.1} pero el principal problema son los billetes y esas cosas..."

    elif Natsuki.isHappy(higher=True):
        n 1unmaj "¿Eh?{w=0.2} ¿Volar?{w=0.2} ¿En avión o algo así?"
        n 1kllaj "Yo...{w=0.3} desearía contestar que sí,{w=0.1} [player]."
        n 1fnmbg "¡Pero no me malinterpretes!{w=0.2} Me encantaría volar a algún lado.{w=0.2} ¡Por vacaciones o algo así!"
        n 1flrpo "Solo que lo que cuesta me echa para atrás, ¿sabes?"
        n 1fcspo "Incluso si tuviera pasaporte, hay demasiadas cosas que hay que pagar..."

    elif Natsuki.isNormal(higher=True):
        n 1unmaj "¿Oh?{w=0.2} ¿Volar en avión o algo por el estilo?"
        n 1kllbo "Ehmm..."
        n 1klraj "Yo...{w=0.3} nunca he tenido la oportunidad de volar a algún sitio,{w=0.1} [player]."
        n 1unmaj "Ni siquiera tengo un pasaporte ni nada por el estilo,{w=0.1} ¿y que más daría si lo tuviera?"
        n 1nsraj "No es como si los billetes sean...{w=0.3} baratos,{w=0.1} ¿sabes a lo que me refiero?"
        n 1nslpo "Especialmente para alguien en mi...{w=0.3} posición."

    elif Natsuki.isDistressed(higher=True):
        n 1nnmbo "¿Volar?{w=0.2} Como...{w=0.3} ¿en avión?"
        n 1fnmsf "No,{w=0.1} [player].{w=0.2} Nunca he podido."
        n 1fllsf "Nunca he tenido un pasaporte,{w=0.1} e igualmente es demasiado caro."
        n 1fnmaj "Tampoco me entusiasma la idea del impacto que tiene eso en el medio ambiente."
        n 1fsqaj "...Pero algo me dice que eso ultimo no va contigo,{w=0.2} ¿no es cierto?"
        n 1flrca "Sabes...{w=0.3} lo digo por lo que he experimentado hasta ahora."
        n 1fsqca "...¿O no?"
        return

    else:
        n 1fsqan "No,{w=0.1} [player].{w=0.2} Nunca he volado.{w=0.2} Y probablemente nunca lo haré."
        n 1fcsan "Así que regodéate todo lo que quieras.{w=0.2} No me importa una mierda si tú lo has hecho."
        return

    n 1ullaj "Igualmente,{w=0.1} intento no sentirme mal al respecto.{w=0.2} ¡Es mejor para el medio ambiente si no lo hago,{w=0.1} al menos!"
    n 1nnmbo "Volar a otros lugares contamina mucho.{w=0.2} Me sentiría egoísta si constantemente fuera en avión,{w=0.1} más sabiendo lo malo que es para todos."
    n 1nllss "Pero...{w=0.3} Solo es mi forma de pensar,{w=0.1} supongo."
    n 1unmaj "¿Y qué hay de ti,{w=0.1} [player]?"
    menu:
        n "¿Vas en avión con frecuencia?"

        "Si, tomo vuelos contantemente":
            n 1fcsbg "¿Oh?{w=0.2} ¡Mírate,{w=0.1} [player]!"
            n 1fslpo "¿Se podría decir que es bueno ver como mi pequeñín {i}alza el vuelo{/i}?"
            n 1fchbg "Jejeje."
            n 1fnmaj "Simplemente no vayas a acumular muchos kilómetros,{w=0.1} [player]."
            n 1fllss "También hay que pensar en el planeta,{w=0.1} ya lo sabes..."

            if Natsuki.isEnamored(higher=True):
                n 1fslnvf "E-{w=0.1}especialmente cuando la gente que más nos importa vive en el.{w=0.2} Jajaja..."

            elif Natsuki.isHappy(higher=True):
                n 1fchgn "¡Sin excusas,{w=0.1} [player]! Jejeje."

        "Tomo vuelos a veces":
            n 1unmss "Ooh,{w=0.1} ¡vale!{w=0.2} ¿Así que viajes familiares o vacaciones extravagantes entonces?"
            n 1fslsm "Ya veo,{w=0.1} ya veo..."
            n 1fcsbg "Bueno,{w=0.1} ¡bien por ti,{w=0.1} [player]!{w=0.2} Todo el mundo debería tener la oportunidad de explorar el basto mundo."
            n 1kslss "Con suerte tendré la oportunidad en algún momento."

            if Natsuki.isEnamored(higher=True):
                n 1fsqsg "Espero que tengas tiempo para entonces,{w=0.1} [player]."
                n 1fchgnl "Vas a ser mi guía turístico,{w=0.1} ¡quieras o no!"

            elif Natsuki.isHappy(higher=True):
                n 1fsqsm "Espero que estes por ahí cuando eso pase,{w=0.1} [player]..."
                n 1fchgn "¡Y entonces veremos qué tan buen guía eres!"

        "He ido en avión alguna vez":
            n 1fsqct "¿Oh?{w=0.2} Así que ya has desplegado tus alas,{w=0.1} ¿eh?"
            n 1tllaj "Hmm...{w=0.3} ¿Me pregunto a dónde fuiste?"
            n 1fnmaj "Promete contarme si vuelves a volar otra vez,{w=0.1} ¿'tá bien?"
            n 1fchgn "¡Quiero escuchar todo al respecto!"

        "Nunca he montado en avión":
            n 1fcsbg "¡Entonces es otra cosa que tenemos en común,{w=0.1} [player]!"
            n 1fsqss "Supongo que se podría decir..."
            n 1fsqdv "Que ambos hemos {i}echado raíces{/i},{w=0.1} ¿eh?"
            n 1fchgn "¡Jajaja!"

    return

# Natsuki laments how she's never travelled abroad by plane
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_are_you_into_cars",
            unlocked=True,
            prompt="¿Te gustan los coches?",
            category=["Transporte"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_are_you_into_cars:
    $ already_discussed_driving = False

    # Check to see if the player and Natsuki have already discussed if Nat can drive in this topic, or the "can you drive" topic
    if get_topic("talk_driving"):
        $ already_discussed_driving = get_topic("talk_driving").shown_count > 0

    elif get_topic("talk_are_you_into_cars"):
        $ already_discussed_driving = get_topic("talk_are_you_into_cars").shown_count > 0

    if already_discussed_driving:
        # Natsuki has already established she can't drive at some point
        if Natsuki.isNormal(higher=True):
            n 1unmaj "¿Eh?{w=0.2} ¿Coches?"
            n 1fchgn "Dios,{w=0.1} ya sabes que no se conducir,{w=0.1} ¡idiota!{w=0.2} ¡No tengo ningún motivo para que me gusten!"
            n 1nlrbg "Bueno,{w=0.1} como sea..."

        elif Natsuki.isDistressed(higher=True):
            n 1fcssl 1nnmsl "[player].{w=0.2} Ya sabes que no se conducir.{w=0.2} ¿Entonces por qué pensaste que me gustarían los coches,{w=0.1} entre todas las cosas?"
            n 1fllsl 1nllsl "...Bien.{w=0.2} Como sea."

        else:
            n 1fsqpu "...¿En serio?"
            n 1fsqaj "Sabes que no se conducir.{w=0.2} Así que ni siquiera voy a {i}pretender{/i} que me importa si a ti sí,{w=0.1} [player]."
            n 1fsqan "Por otro lado...{w=0.3} Apuesto a que {i}jamás{/i} vas a tratar al coche de tus sueños como me tratas a mí,{w=0.1} ¿o sí?"
            return

    else:
        # Natsuki hasn't stated she can't drive before
        if Natsuki.isNormal(higher=True):
            n 1unmaj "¿Eh?{w=0.1} ¿Qué si me gustan los coches?"
            n 1fllnv "Bueno...{w=0.3} a decir verdad,{w=0.1} [player]."
            n 1unmaj "...Nunca he dado clases de conducir."
            n 1flrpo "¡Ni siquiera creo que pudiera ahorrar para ello!"
            n 1nnmaj "Así que jamás me han interesado especialmente los coches."

        elif Natsuki.isDistressed(higher=True):
            n 1fnmsr "No se conducir,{w=0.1} [player].{w=0.2} Y tampoco tengo carné;{w=0.1} las clases siempre han sido caras."
            n 1fnmpu "Así que...{w=0.3} ¿Por qué me interesarían los coches?{w=0.1} Literalmente no puedo {i}permitírmelo{/i}."

        else:
            n 1fcsan "Nuevas noticias,{w=0.1} imbécil.{w=0.2} {i}No{/i} se conducir,{w=0.1} y ni siquiera puedo ahorrar para {i}aprender{/i}."
            n 1fsqan "Así que {i}dime{/i} -{w=0.1} ¿por qué deberían gustarme los coches?{w=0.2} Y aun si fuera así,{w=0.1} ¿por qué demonios hablaría {i}contigo{/i} de ello?"
            n 1fcspu "...Jeh.{w=0.2} Claro,{w=0.1} ya decía yo.{w=0.2} Pues ya está,{w=0.1} [player]."
            return

    if Natsuki.isNormal(higher=True):
        n 1unmsm "Puedo notar el talento en su diseño -{w=0.1} ¡de hecho considero que es bastante guay lo expresivos que pueden ser!"
        n 1nllss "Es como...{w=0.3} No sabes todos los lenguajes de diseño de las diferentes marcas,{w=0.1} y la ingeniería que hay detrás de todo eso."
        n 1fchbg "Es una locura la cantidad de trabajo que conlleva;{w=0.1} ¡y definitivamente eso se merece un respeto!"
        n 1fsqsm "¿Y tú qué opinas, [player]?{w=0.2} Tú {i}fuiste{/i} quien preguntó,{w=0.1} pero pienso preguntar igualmente..."
        menu:
            n "¿Te gustan los coches?"

            "¡Sí! Me encantan":

                # The player has never stated if they can drive
                if persistent.jn_player_can_drive is None:
                    n 1tllbo "Eh.{w=0.2} Nunca me has dicho si sabes conducir,{w=0.1} pero supongo que realmente no importa."
                    n 1fsqsm "Supongo que ser un adicto al motor no es tan exclusivo,{w=0.1} ¿eh?"
                    n 1uchbg "Jajaja."

                # The player has confirmed they can drive
                elif persistent.jn_player_can_drive:
                    n 1fsgbg "Bueno,{w=0.1} {i}dame{/i} por sorprendida."
                    n 1fchgn "Jejeje."
                    n 1fcsbg "No te preocupes,{w=0.1} ya había imaginado que eras de esos,{w=0.2} [player]."
                    n 1fchbg "Pero oye -{w=0.1} ¡por algo el bote no se va a pique!"

                # The player has admitted they cannot drive
                else:
                    n 1unmaj "Eso es...{w=0.3} bastante sorprendente de escuchar por tu parte,{w=0.1} la verdad [player]."
                    n 1nllaj "Sabes,{w=0.1} desde que dijiste que no sabes conducir y eso..."
                    n 1fchbg "Pero supongo que es como todo -{w=0.1} no tienes que hacerlo para que te guste,{w=0.1} ¡y eso está bien por mí parte!"

            "No me importan demasiado":
                n 1ullss "Supongo que eso es justo -{w=0.1} y no te preocupes,{w=0.1} lo entiendo."
                n 1nnmsm "Pero si a alguien le gustan esas cosas,{w=0.1} ¿quién somos nosotros para juzgar,{w=0.1} después de todo?"

            "No, no es lo mío":
                n 1ulraj "...Eh.{w=0.2} Eso es bastante raro -{w=0.1} ¿entonces por qué has sacado el tema,{w=0.1} [player]?"

                if persistent.jn_player_can_drive:
                    n 1tlraj "¡Especialmente si sabes conducir!"
                    n 1tllpu "Eh..."

                n 1fchbg "Bueno,{w=0.1} como sea.{w=0.2} ¡Supongo que es justo!"

    else:
        n 1flrsr "Supongo que es merecedor de respeto todo el trabajo y el talento necesario para diseñar y crear uno de esos..."
        n 1fnmbo "Pero es lo mismo que cualquier otra cosa."
        n 1fsqbo "...Supongo que te gustan los coches,{w=0.1} ¿no?"
        n 1fcspu "Jeh."
        n 1fsqpu "Estaría guay si ese respeto lo aplicaras también a las {i}personas{/i},{w=0.1} [player]."
        n 1fsqsr "{i}Yo solo te lo comento.{/i}"

    return

# Natsuki comments on how she feels about the player, based on affinity
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_how_do_you_feel_about_me",
            unlocked=True,
            prompt="¿Qué sientes por mí?",
            category=["Natsuki", "Romance", "TÚ"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_how_do_you_feel_about_me:
    if Natsuki.isLove():

        if persistent.jn_player_love_you_count > 0:
            n 1kwmpof "[player]...{w=0.3} ¿no es obvio? Ya sabes que te amo,{w=0.1} ¿cierto?"
            n 1fllpol "Dios...{w=0.3} a veces creo que eres bobo,{w=0.1} ¿sabes?"
            n 1kllssl "Pero...{w=0.3} me gusta esa parte atontada de ti,{w=0.1} [player]."
            n 1nwmbgl "Nunca cambies,{w=0.1} ¿'tá bien? Jejeje."
            n 1nchbgl "¡Te amo,{w=0.1} [player]~!"

        else:
            n 1fcsanf "¡Nnnnnnn-!"
            n 1fnmanf "¡V-{w=0.1}vamos! ¿No ha quedado claro hasta ahora? Dios...{w=0.5}{nw}"
            n 1fllpof "¿Acaso tengo que deletreártelo,{w=0.1} [player]?"
            n 1fcspol "Agh...{w=0.5}{nw}"
            n 1fsqssl "Jeh.{w=0.2} De hecho,{w=0.1} ¿sabes qué?"
            n 1fsqbgl "Dejare que te des cuenta por ti mismo.."
            n 1fslajl "Y no,{w=0.1} antes de que preguntes -{w=0.1} ya has tenido suficientes pistas."
            n 1fllpol "Bobo..."

        return

    elif Natsuki.isEnamored(higher=True):
        n 1fcsanf "¡Uuuuuuh-!"
        n 1fskwrf "¿E-{w=0.1}estás intentando ponerme entre la espada y la pared o algo,{w=0.1} [player]?"
        n 1fllemf "Dios...{w=0.5}{nw}"
        n 1fcseml "Ya deberías {i}saber{/i} lo que opino de ti...{w=0.5}{nw}"
        n 1fllpol "...{w=0.5}{nw}"
        n 1kcspol "...{w=0.3}Bien."
        n 1fcspol "Tú...{w=0.3} me...{w=0.3} gustas,{w=0.1} [player].{w=0.2} Un montón."
        n 1fbkwrf "¡Y-{w=0.1}ya está!{w=0.2} ¡¿Estas contento?!"
        n 1kllsrl "Dios santo..."
        return

    elif Natsuki.isAffectionate(higher=True):
        n 1fskemf "¿E-{w=0.1}eh? ¿Qué que siento por ti?"
        n 1fbkwrf "¡¿P-{w=0.1}porque me estás preguntando eso ahora?!"
        n 1fllpol "Dios santo,{w=0.1} [player]...{w=0.3} vas a hacer que esto sea incomodo..."
        n 1fcseml "Eres guay,{w=0.1} ¡así que no hace falta que me molestes más al respecto!"
        n 1flrunl "Diablos..."
        return

    elif Natsuki.isHappy(higher=True):
        n 1uskemf "¡¿E-eh?!"
        n 1fllbgl "¡O-oh! Jajaja..."
        n 1nllaj "Bueno,{w=0.1} a ver...{w=0.5}{nw}"
        n 1ullaj "Eres alguien gracioso con el que estar,{w=0.1} todo de ti lo es."
        n 1fllnvl "Así que...{w=0.3} eso...."
        return

    elif Natsuki.isNormal(higher=True):
        n 1uskeml "¡¿E-{w=0.1}eh?!"
        n 1fllbg "¡O-oh!"
        n 1unmaj "A ver...{w=0.3} estás bien...{w=0.3} ¿supongo?"

        if not persistent.jn_player_first_farewell_response:
            n 1flleml "¿Q-{w=0.1}que esperabas qué te dijera?{w=0.5}{nw}"
            extend 1fnmpol " ¡{i}Literalmente{/i} nos acabamos de conocer!"

        n 1nnmpu "Eso es todo lo que puedo decir,{w=0.1} así que...{w=0.3} eso."
        n 1nllca "...{w=0.5}{nw}"
        n 1nlraj "Así que...{w=0.3} ¿Dónde estábamos?"
        return

    elif Natsuki.isUpset(higher=True):
        n 1fsqaj "...{w=0.3}¿Oh? Entonces eso ahora te importa,{w=0.1} ¿no es así?"
        n 1fsqbo "Entonces dime,{w=0.1} [player]."
        n 1fnmun "¿Por qué has seguido dañando mis sentimientos así?"
        n 1fcsun "...{w=0.5}{nw}"
        n 1fllan "No tengo mucha paciencia para los imbéciles,{w=0.1} [player]."
        n 1fnmaj "No se si intentas hacerte el gracioso o que,{w=0.1} pero que te den.{w=0.2} ¿Lo pillas?"
        n 1fsqsr "Muchas gracias."
        return

    elif Natsuki.isDistressed(higher=True):
        n 1fsqsr "...{w=0.3}Dejémonos de tonterías."
        n 1fcsan "Me has hecho daño,{w=0.1} [player].{w=0.2} He has hecho daño una,{w=0.1} y otra vez."
        n 1fnmfu "Lo has hecho tantas veces ya."
        n 1fnman "Así que dime."
        n 1fsqpu "¿Qué demonios sentirías {i}tú{/i} por alguien que hizo lo que me hiciste?"
        n 1fcspu "...{w=0.5}{nw}"
        n 1fsqan "Estás en la cuerda floja,{w=0.1} [player].{w=0.2} ¿Lo pillas?"
        return

    elif Natsuki.isBroken():
        $ already_discussed_relationship = get_topic("talk_how_do_you_feel_about_me").shown_count > 0
        if already_discussed_relationship:
            n 1fsqpu "...Guau.{w=0.2} ¿En serio?"

        else:
            n 1fsqpu "...{w=0.3}No tengo palabras para describir como me siento respecto a {i}ti{/i}."
            n 1fsqfu "No me puto pongas a prueba, {i}[player]{/i}."

        return

    else:
        n 1fcsun "...{w=0.3}...{w=0.5}{nw}"
        n 1fcsan "...{w=0.3}...{w=0.5}{nw}"
        return

    return

# Natsuki pitches her thoughts on cosplaying
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_are_you_into_cosplay",
            unlocked=True,
            prompt="¿Te gusta el cosplay?",
            category=["Moda", "Contenido", "Sociedad"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_are_you_into_cosplay:

    # Check to see if Natsuki has already revealed she can sew/seamstress in this/previous topic(s)
    $ already_mentioned_sewing = get_topic("talk_sustainable_fashion").shown_count > 0 or get_topic("talk_are_you_into_cosplay").shown_count > 0

    if Natsuki.isEnamored(higher=True):
        n 1unmbg "¡Ooh!{w=0.2} Cosplay,{w=0.1} ¿dices?"
        n 1fllbg "Para ser honesta,{w=0.1} nunca he hecho cosplay ni nada parecido..."
        n 1nnmss "¡Pero he estado pensando mucho el ello últimamente desde que estoy metida en el manga y esas cosas!"
        n 1flrbg "Además, quiero decir,{w=0.1} ¿por qué no?{w=0.2} Realmente no hay mucho que me detenga."

        if already_mentioned_sewing:
            n 1fcssm "Como creo que he mencionado antes -{w=0.1} tengo bastante soltura con la aguja y el hilo,{w=0.1} ¡te lo digo yo!"

        else:
            n 1fwlsm "Tengo bastante soltura con la aguja y el hilo,{w=0.1} ¿sabes?"

        n 1ulrss "Y los materiales no son muy caros tampoco -{w=0.1} sin contar los accesorios y las pelucas,{w=0.1} creo."
        n 1nnmsm "Así que me parece una maravillosa forma de mostrar cuanto aprecio a ciertos personajes..."
        n 1fsqbg "...Y así mostrar mi {i}ilimitado{/i} talento mientras lo hago."
        n 1fchgn "¡Jajaja!"
        n 1uchgn "¿Y quién sabe?"
        n 1uchsm "Tal vez puedas ver alguna de mis magnificas obras algún día,{w=0.1} [player]."
        n 1fsqbg "Apuesto a que te encantaría,{w=0.1} ¿eh?{w=0.2} Jejeje."
        n 1fsgsg "No hay necesidad de avergonzarse,{w=0.1} [player] -{w=0.1} eres más fácil de leer que un libro abierto."
        n 1fsqsgl "Un libro asqueroso,{w=0.1} pero un libro, al fin y al cabo~."
        n 1fchgn "¡Jajaja!"
        return

        if Natsuki.isLove():
            n 1uchtsl "¡Te amo,{w=0.1} [player]~!"
            return

    elif Natsuki.isHappy(higher=True):
        n 1tsrpu "...¿Por qué tenía la impresión de que ibas a sacar el tema tarde o temprano,{w=0.1} [player]?"
        n 1fnmpo "¿Qué?{w=0.2} ¿Creíste que iba a estar metida {i}automáticamente{/i} en esas cosas solo porque me gusta el manga desde hace un tiempo?"
        n 1fsqpo "¿Eh?{w=0.2} ¿Es verdad o no?"
        n 1fnmaj "¿Y bien?"
        n 1fsqsg "¡Habla,{w=0.1} [player]!{w=0.2} ¡No te oigo~!"
        n 1fslpo "..."
        n 1fchgn "¡Jajaja!{w=0.2} Nah,{w=0.1} está bien."
        n 1ulraj "He estado pensando en ello mucho,{w=0.1} la verdad -{w=0.1} como desde que me introduje en temas de manga y eso."
        n 1nnmaj "{i}De hecho{/i}, todavía no lo he hecho nunca,{w=0.1} creo."
        n 1fnmaj "Pero no hay mucho que me detenga,{w=0.1} [player]."

        if already_mentioned_sewing:
            n 1ullbo "Como te dije -{w=0.1} ya he hecho y arreglado algunas de mis ropas,{w=0.1} así que un disfraz no debe ser para tanto."

        else:
            n 1flrbg "Se podría decir que soy una pro respecto a la aguja y el hilo,{w=0.1} ¡que es justo lo que se necesita!"

        n 1unmaj "Igualmente,{w=0.1} he estado mirando materiales -{w=0.1} , y de hecho sale bastante rentable,{w=0.1} así que está bien."
        n 1nllaj "Bueno,{w=0.1} sin contar los accesorios y las pelucas.{w=0.2} Esos son algo mas caras,{w=0.1} pero no son particularmente poco rentable -{w=0.1} ¡solo hay que saber dónde comprar!"
        n 1fllsl "Dicho eso...{w=0.3} hmm..."
        n 1fllsm "¿Sabes qué,{w=0.1} [player]?"
        n 1fnmbg "Tal vez le de una oportunidad...{w=0.3} ¡venga!"
        n 1fchgn "Hombre,{w=0.1} ¡no sabes la cantidad de ideas rondando mi cabeza ahora misma!"
        n 1fchsm "Oh -{w=0.1} no te preocupes -{w=0.1} tendrás tu oportunidad de verlos.{w=0.2} Necesitare una segunda opinión."
        n 1uchbg "Para eso están los amigos,{w=0.1} ¿verdad?{w=0.2} Jejeje."

        if Natsuki.isAffectionate(higher=True):
            n 1fsqbg "Igualmente,{w=0.1} [player].{w=0.2} Parece que tienes un buen gusto."
            n 1fsqsml "Creo que puedo confiar en tu juicio..."

        return

    elif Natsuki.isNormal(higher=True):
        n 1unmaj "Cosplay,{w=0.1} ¿eh?"
        n 1ulraj "Bueno...{w=0.3} Quiero decir,{w=0.1} me lo he pensado,{w=0.1} si por eso lo preguntas."
        n 1nnmbo "Nunca me lo había planteado mucho antes de conocer el manga y estas cosas."
        n 1flrbg "¡Siento como que una vez que te metes en ese mundo descubres un montón de cosas a la vez!"
        n 1nnmaj "Pero, aun así,{w=0.1} nunca he salido a hacer cosplay."
        n 1flleml "E-{w=0.1}eso no quiere decir que haya algo deteniéndome,{w=0.1} ¡por supuesto!"

        if already_mentioned_sewing:
            n 1fllss "Ya te dije antes que soy bastante buena con la aguja y el hilo,{w=0.1} así que eso es un-{w=0.1}¡'tá bien!"

        else:
            n 1fcsbg "Básicamente soy una experta de la aguja y el hilo,{w=0.1} ¡así que esa parte ya la tengo dominada!"

        n 1nlrpu "Lo demás es simplemente ir de compras a por materiales,{w=0.1} los cuales son bastante baratos de hecho."
        n 1unmpu "Los accesorios y las pelucas si son algo mas molestas,{w=0.1} pero no son inaccesibles."
        n 1fllsr "Hmm..."
        n 1fllbg "Cuanto más lo pienso,{w=0.1} ¡más me gusta la idea!"
        n 1fnmbg "¿Qué te parece,{w=0.1} [player]?{w=0.2} Apuesto a que te encantaría ver mis habilidades en acción,{w=0.1} ¿cierto?"
        n 1nnmsm "Jajaja."
        n 1flrsml "Bueno...{w=0.3} ya lo veremos,{w=0.1} ¡pero no prometo nada!"
        return

    elif Natsuki.isDistressed(higher=True):
        n 1nnmpu "¿Eh?{w=0.2} ¿Cosplay?"
        n 1fsqsr "...¿Por qué,{w=0.1} [player]?"
        n 1fsqpu "¿Así que también te quieres reír de cómo visto?"
        n 1fslsr "..."
        n 1fsqpu "No,{w=0.1} [player].{w=0.2} Nunca he hecho cosplay.{w=0.2} Podría,{w=0.1} pero no lo he hecho."
        n 1fsqan "¿Eso responde a tu pregunta?"
        return

    else:
        n 1fsqsr "Jeh.{w=0.2} ¿Por qué?"
        n 1fcsan "¿Es que quieres algo más con lo que hacerme sentir mal?"
        n 1kcssr "...Ya.{w=0.2} No, gracias."
        n 1fcsan "Ya no quiero hablar de esto."
        return

    return

# Natsuki describes why she likes the player
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_why_do_you_like_me",
            unlocked=True,
            prompt="¿Por qué te gusto?",
            category=["Natsuki", "Romance", "TÚ"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_why_do_you_like_me:
    if Natsuki.isLove():
        if jn_admissions.last_admission_type == jn_admissions.TYPE_INSECURE:
            n 1kwmsl "[player]..."
            n 1kwmsf "No me estarás preguntando esto por lo que me dijiste anteriormente...{w=0.3} ¿Cierto?"
            n 1kllbo "..."
            n 1ncspu "Mira,{w=0.1} [player].{w=0.2} Voy a ser completamente honesta contigo,{w=0.1} ¿vale?"
            n 1ncssl "Lo que puedas -{w=0.1} o {i}no{/i} hacer -{w=0.1} no me importa."
            n 1nnmpu "Lo que la gente {i}diga{/i} que eres -{w=0.1} o lo que {i}no{/i} puedan decir -{w=0.1} no me importa en absoluto."
            n 1fnmpu "Tampoco lo que opinen de ti."
            n 1knmsr "[player]."
            $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
            n 1klrpu "Yo...{w=0.3} lo que siento por ti es por cómo me has cuidado,{w=0.1} [chosen_endearment].{w=0.2} ¿Acaso no lo ves?"
            n 1klrss "Has pasado mucho tiempo a mi lado,{w=0.1} día tras día..."
            n 1kwmss "Has escuchado mis problemas,{w=0.1} me has contado los tuyos..."
            n 1kllpo "Has sido paciente conmigo cuando mi humor no es el mejor,{w=0.1} también cuando fui una malcriada..."

            if persistent.jn_player_love_you_count >= 10:
                n 1kcsunl "Y...{w=0.3} me has hecho sentir..."
                n 1kcsunf "tan amada..."
                n 1kllunl "..."

            elif persistent.jn_player_love_you_count >= 1:
                n 1kllssl "Eres...{w=0.3} Eres mi primer amor,{w=0.1} [player]..."
                n 1kcussl "¿Eres consciente de {i}cuanto{/i} significa eso para mí?"

            elif persistent.jn_player_love_you_count == 0:
                n 1kwmssl "De verdad,{w=0.1} lo significas todo para mí,{w=0.1} [player]..."

            n 1kllssl "Así que...{w=0.3} Eso."
            n 1klrnvl "¿Te sirve como respuesta?"
            n 1knmsr "Se que no puedo resolver tus problemas con un chasquido,{w=0.1} [player].{w=0.2} No hago milagros."
            n 1kslsl "Créeme -{w=0.1} {i}ya{/i} lo hubiera hecho si pudiera."
            n 1knmsl "Pero..."
            n 1kllss "Espero que puedas creerme cuando digo que las cosas se arreglarán,{w=0.1} ¿puede ser?"
            n 1fwmsm "Tan solo...{w=0.3} sigue luchando..."
            n 1fcssml "...Por que yo lucharé por ti a cambio."
            n 1kplnvf "Te amo,{w=0.1} [player].{w=0.2} Espero que nunca olvides eso."
            return

        else:
            n 1fcspo "[player]..."
            n 1flrpo "¿En serio tengo que explicarte esto?"
            n 1flrsll "Es bastante...{w=0.3} embarazoso...{w=0.3} para mi..."
            n 1kcssll "..."
            n 1ncspu "...Vale,{w=0.1} mira."
            n 1fllssl "Tú has...{w=0.3} hecho más de lo que jamás te podrías imaginar,{w=0.1} [player]."
            n 1fllsll "Por mí,{w=0.1} quería decir."
            n 1knmsll "Ya casi pierdo la cuenta de cuantas horas has pasado hablando conmigo..."
            n 1klrssl "Has escuchado tantos de mis problemas tontos,{w=0.1} una y otra vez..."
            n 1fllunl "...Incluso has sido paciente aun con mis cambios de humor."

            if persistent.jn_player_love_you_count >= 10:
                n 1fcsunl "T-tú me has hecho sentir..."
                n 1kcsunl "Tan apreciada.{w=0.2} Tantas veces que he perdido la cuenta..."

            elif persistent.jn_player_love_you_count >= 1:
                n 1kskajf "Eres...{w=0.3} ¡Eres mi primer amor incluso!"
                n 1kwmpuf "¿Siquiera sabes {i}cuanto{/i} significa eso para mí?"

            elif persistent.jn_player_love_you_count == 0:
                n 1kwmpuf "De verdad, lo significas todo para mí,{w=0.1} [player]..."

            n 1kllssl "Así que...{w=0.3} Eso."
            n 1klrnvl "¿Te sirve esta respuesta?{w=0.2} ¿Ya puedo irme?"
            n 1klrss "Jajaja..."
            n 1kwmpu "Ahora en serio,{w=0.1} [player]."
            n 1kplbo "Ni te atrevas a dudar de lo mucho que significas para mí,{w=0.1} ¿vale?"
            n 1fnmpol "Me enfadaré si te atreves a intentarlo."
            n 1flrpol "Y créeme..."
            n 1klrssl "Dudo que quieras eso."
            return

    elif Natsuki.isEnamored(higher=True):
        if jn_admissions.last_admission_type == jn_admissions.TYPE_INSECURE:
            n 1knmaj "...Oye,{w=0.1} [player]..."
            n 1klrpu "Esto no será por casualidad por lo que me dijiste antes...{w=0.3} ¿cierto?"

        else:
            n 1uskpul "¿Po-{w=0.1}porque me-{w=0.1}...?"
            n 1fcsanl "Uuuuuuuh..."

        n 1fcsajl "...Vale,{w=0.1} mira.{w=0.2} Voy a intentar ayudarte para que lo entiendas lo mejor posible."
        n 1fllaj "No se si alguien te ha hecho tener una mala pasada, pero voy a decirlo igualmente."
        n 1fllsr "No me importa lo que otros esperen de ti."
        n 1fnmsr "No me importa lo que otros piensen o digan de ti."
        n 1knmpu "No me importa si puedes -{w=0.1} o no -{w=0.1} hacer algo."
        n 1fcseml "Yo...{w=0.3} Te {i}quiero{/i},{w=0.1} por cómo me has tratado,{w=0.1} ¡bobo!"
        n 1flleml "Es como,{w=0.1} ¡vamos!"
        n 1flrssl "Me has escuchado chacharear,{w=0.1} una y otra vez..."
        n 1knmssl "Me has oído hablar de tantos problemas tontos que he tenido…..."
        n 1fcsbgl "¡Me has aguantado incluso cuando me comporto como un mono!"
        n 1klrsl "..."
        n 1kcssl "...Nunca había sido tratada tan bien como tu lo hiciste,{w=0.1} [player]."
        n 1fllslf "Así que no es de extrañar...{w=0.3} ¿qué disfrute de pasar tanto tiempo contigo?"
        n 1fcsslf "..."
        n 1flrajl "Muy bien,{w=0.1} ya está.{w=0.2} De verdad que no quiero explicar todo esto otra vez,{w=0.1} así que espero que lo recuerdes."
        n 1fnmssl "Tan solo...{w=0.3} sigue siendo tú,{w=0.1} ¿entendido?"
        n 1kllpul "A mi...{w=0.3} me gusta como eres ahora."
        return

    else:
        if jn_admissions.last_admission_type == jn_admissions.TYPE_INSECURE:
            n 1unmpul "...¿Eh?"
            n 1uskemf "¿P-{w=0.1}porque me...?"
            n 1fcsanf "..."
            n 1tlremf "..."
            n 1flrsll "..."
            n 1fnmpul "Ehmm...{w=0.3} ¿[player]?"
            n 1fllpo "Esto no tiene que ver con lo que hablamos antes,{w=0.1} ¿verdad?"
            n 1knmpo "¿Sobre sentirte inseguro y eso?"
            n 1klrsl "..."
            n 1nnmsl "[player]."
            n 1fnmpuf "Escúchame,{w=0.1} ¿'tá bien?{w=0.2} Yo...{w=0.3} No quiero tener que repetirte esto."

        else:
            n 1uscemf "¡Urk-!"
            n 1uskemf "E-{w=0.1}espera,{w=0.1} ¿q-{w=0.1}qué?"
            n 1fwdemf "P-{w=0.1}porque me...{w=0.3} ¡¿g-{w=0.1}gustas?!"
            n 1fcsanf "¡Nnnnnnnnn-!"
            n 1fllwrf "¡A ver...!{w=0.2} ¡No es {i}como{/i} que me gustes,{w=0.1} o algo tan ridículo como eso!"
            n 1fcsemf "Agh...{w=0.3} Quiero decir,{w=0.1} [player] -{w=0.1} realmente sabes como ponerme incomoda a veces..."
            n 1fllslf "..."
            n 1fllsll "Yo...{w=0.3} supongo que te {i}debo{/i} una respuesta,{w=0.1} como mínimo."

        n 1fcssll "Mira."
        n 1nlrpu "Has sido bastante increíble conmigo,{w=0.1} [player]."
        n 1klrpu "...¿Sabes cuantas personas me han hecho sentir así en toda mi vida?"
        n 1klrsl "Son...{w=0.3} bueno, no son muchas,{w=0.1} en resumen."
        n 1fllpol "Siempre me has escuchado,{w=0.1} no me has dicho que soy molesta,{w=0.1} o pedido que baje el volumen..."
        n 1kwmsrl "También eres super comprensivo."
        n 1kllpul "Yo...{w=0.3} no podría pedir un amigo mejor,{w=0.1} [player]."
        n 1fnmbol "Recuérdalo por siempre,{w=0.1} ¿puedes?{w=0.2} Si no, me enfadare contigo."
        n 1kllbol "..."

    return

# Natsuki actually likes fried squid!
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_fried_squid",
            unlocked=True,
            prompt="Calamares fritos",
            category=["DDLC", "Comida"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_fried_squid:
    n 1fllss "Oye,{w=0.1} [player]..."
    n 1usqsm "¿Sabes a por lo que se me apetecería ir ahora mismo?"
    n 1uchbs "¡Un enorme,{w=0.1} humeante plato recién hecho de Mon-{w=0.1}ika!"
    n 1uchbg "..."
    n 1flrpu "...Eh."
    n 1tnmpu "Sabes,{w=0.1} en retrospectiva...{w=0.2} Esa broma no fue graciosa ni la primera vez."
    n 1tllpo "Mira...{w=0.3} siendo sincera no tengo idea de por qué pensé que sería gracioso esta vez."
    n 1uspgs "¡Oh!"
    n 1fchbg "¡Pero los calamares fritos no son algo con lo que bromear,{w=0.1} [player]!{w=0.2} ¿Los has probado una vez?"
    n 1uchbs "¡Son {i}deliciosos{/i}!{w=0.2} ¡Me encantan!"
    n 1fsqsm "Pero no son simple marisco frito -{w=0.1} ¡rebozarlo antes es muy importante!"
    n 1uspbg "Ese crujiente recubrimiento dorado es lo mejor, en serio.{w=0.2} ¡La comida frita es maravillosa!"
    n 1fllbg "Aunque no es exactamente {i}buena{/i} para ti,{w=0.1} ¿es más bien un capricho?{w=0.2} Aun se puede empeorar..."
    n 1fcssm "¡Especialmente con salsa que le dé algo de picor al asunto!"
    n 1fnmss "Por cierto -{w=0.1} ¿quieres saber cómo reconocer cuando estás comiendo un buen calamar de primera categoría?"
    n 1uchbs "Por la textura,{w=0.1} ¡por supuesto!"
    n 1fllaj "Los calamares demasiado fritos parecen chicle y dan asco,{w=0.1} y lo que es peor -{w=0.1} ¡también pierde todo su sabor!"
    n 1fsqsr "Imagínate mordiendo el rebozado,{w=0.1} solo para encontrarte con un conglomerado de gomas."
    n 1fsqem "¡Agh!{w=0.2} ¡Que asco!{w=0.2} Hablando de desanimarse."
    n 1unmaj "Pero no dejes que eso te desanime,{w=0.1} [player] -{w=0.1} la próxima vez que veas calamares fritos,{w=0.1} ¿por qué no les das una oportunidad?"

    if jn_admissions.last_admission_type == jn_admissions.TYPE_HUNGRY:
        n 1kllss "...Cuanto antes mejor,{w=0.1} si tienes tanta hambre como dices."
        n 1ullaj "Pero igualmente..."

    n 1unmbg "¡Incluso si quieres sonar pedante podrías intentar pedirlo por su nombre culinario!"
    n 1fnmbg "Diez puntos para ti si puedes adivinar cual es.{w=0.2} Jejeje."

    if Natsuki.isLove():
        n 1flrsg "Hmm..."
        n 1fnmbg "De hecho...{w=0.3} ¿Sabes qué?"
        n 1fchbg "Deberíamos pedir calamares para compartir.{w=0.2} Sería justo,{w=0.1} ¿cierto?"
        n 1fsqsm "Pero tengo que advertirte,{w=0.1} [player]..."
        n 1fchgn "¡No voy a darte el ultimo sin pelear!"
        n 1nchsml "Jejeje."

    elif Natsuki.isEnamored(higher=True):
        n 1uchbg "Pero eso -{w=0.1} ¡deberías darle una oportunidad si es que aún no lo has hecho,{w=0.1} [player]!"
        n 1fchbg "¡No me gustaría que nadie se perdiera eso!"
        n 1klrssl "E-{w=0.1}especialmente tú.{w=0.2} Jejeje..."

    else:
        n 1uchbg "Pero eso {w=0.1}-{w=0.1} ¡deberías darle una oportunidad si es que aún no lo has hecho,{w=0.1} [player]!"
        n 1fchbg "¡No me gustaría que nadie se perdiera eso!{w=0.2} Jajaja."

    return

# Natsuki talks about collectibles
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_collectibles",
            unlocked=True,
            prompt="¿Tienes algún objeto de coleccionismo?",
            category=["Contenido"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_collectibles:
    if Natsuki.isAffectionate(higher=True):
        n 1unmpu "¿Coleccionismo?{w=0.2} ¿Te refieres a cosas como figuras, peluches y demás?"
        n 1flrpu "Mmm...{w=0.3} En realidad no.{w=0.2} ¡El coleccionismo es un pasatiempo caro,{w=0.1} [player]!"
        n 1klrpo "Quiero decir,{w=0.1} depende de que sea lo que colecciones,{w=0.1} pero es como que los sitios donde lo venden se aprovechan de ello."
        n 1flraj "Como...{w=0.3} te urge completar una colección -{w=0.1} ¡y mágicamente suben los precios!"
        n 1fcsbo "Agh..."
        n 1kllbo "Y para la gente en mi...{w=0.3} ehmm...{w=0.3} {i}posición{/i},{w=0.1} es una gran barrera para meterte en el mundillo."
        n 1unmaj "Pero bueno..."

    elif Natsuki.isNormal(higher=True):
        n 1tnmpu "¿Eh?{w=0.2} ¿Quieres decir figuras y esas cosas?"
        n 1tlrpu "Bueno...{w=0.3} no,{w=0.1} [player].{w=0.2} No realmente."
        n 1knmsf "¡No podría justificar tanto gasto como requiere un pasatiempo así!"
        n 1flrbo "Especialmente no cuando tengo otras cosas en las que gastar primero,{w=0.1} ya sabes."
        n 1unmaj "Pero bueno,{w=0.1} dejando eso de lado..."

    elif Natsuki.isDistressed(higher=True):
        n 1fsqsf "No,{w=0.1} [player]."
        n 1fsqaj "Los objetos de colección son demasiado caros para mí.{w=0.2} No puedo justificar gastar el dinero que {i}tengo{/i} así."
        n 1fnmsl "{i}Especialmente{/i} con cosas que se van a quedar muertos de risa en una solitaria estantería."
        n 1fsqsr "Claro,{w=0.1} [player] -{w=0.1} lo creas o no,{w=0.1} algunos de nosotros {i}tenemos{/i} que preocuparnos por como gastamos nuestro dinero."
        n 1fsqun "Impactante,{w=0.1} ¿verdad?"
        n 1fcsun "..."
        n 1fnmaj "¿Y bien?{w=0.2} ¿Satisfecho con la respuesta?"
        n 1fsqaj "Ya está."
        return

    else:
        n 1fsqsr "...¿Por qué?{w=0.2} ...Y no me refiero a por que te importa."
        n 1fsqan "¿Pero por qué debería decirte {i}a ti{/i} si lo hago o no?"
        n 1fcsan "Seguramente solo lo tirarías por la borda."
        n 1fcsun "Jeh.{w=0.2} Después de todo."
        n 1fsqup "Has demostrado ser muy bueno en tirar las cosas por la borda hasta ahora,{w=0.1} ¿{i}no es así{/i}?{w=0.2} Desgraciado."
        return

    n 1ullbo "..."
    n 1tllbo "...Eh.{w=0.2} Tiene su punto,{w=0.1} de hecho.{w=0.2} ¿El manga cuenta como un objeto de coleccionismo?"
    n 1tllaj "Yo...{w=0.3} no estoy segura..."
    n 1tnmpu "¿Tú qué opinas,{w=0.1} [player]?"
    menu:
        n "¿Se le podría considerar un objeto de colección?"

        "¡Yo diría que sí!":
            n 1fsqbg "¡Ojo!"
            n 1fchbg "Así que soy una especie de coleccionista,{w=0.1} ¡después de todo!"

            if Natsuki.isLove():
                n 1uchsm "Supongo que todo tiene sentido ahora.{w=0.2} Al final..."
                n 1fllsmf "Me gusta pensar que tu eres parte de mi colección,{w=0.1} [player]~."
                n 1uchsmf "Jejeje."

            else:
                n 1flrsm "Bueno,{w=0.1} en ese caso..."
                n 1nchbg "¡Si quieres, déjame saber si quieres que te haga un tour!"
                n 1nchgn "¡No encontrarás una colección mejor!{w=0.2} Jejeje."

                if jn_activity.has_player_done_activity(jn_activity.JNActivities.manga):
                    n 1fllss "O,{w=0.1} al menos...{w=0.5}{nw}"
                    extend 1fsqss " mejor...{w=0.3} en {i}físico{/i}."
                    n 1fsqsm "¿Verdad,{w=0.5}{nw}"
                    extend 1fsqbg " [player]?"

        "No,{w=0.1} no creo.":
            n 1flrpo "Eh...{w=0.3} supongo que tienes razón."
            n 1tnmpo "Supongo que podrías llamarlo biblioteca,{w=0.1} ¿o algo así?"
            n 1nnmsm "Bueno,{w=0.1} como sea."
            n 1nsqsm "Supongo que será mejor {i}leer{/i} la definición,{w=0.1} ¿no crees?"
            n 1nchsm "Jejeje."

        "Bueno,{w=0.1} lo que definitivamente no es, es literatura.":
            n 1nsqsr "Ja.{w=0.2} Ja.{w=0.2} Ja.{w=0.2} Ja.{w=0.2} ...Ja."
            n 1flrpo "{i}Eres hilarante{/i},{w=0.1} [player]."
            n 1flraj "Repítelo si te atreves,{w=0.1} te haré una reserva."
            n 1fsqsg "...Y no,{w=0.1} no precisamente del próximo tomo."

    return

# Prompt Natsuki to play a game of Snap!
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_play_snap",
            unlocked=True,
            prompt="¿Quieres jugar al Snap?",
            conditional="persistent.jn_snap_unlocked",
            category=["Videojuegos"],
            player_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_play_snap:
    if persistent.jn_snap_player_is_cheater:
        # Unlock Snap if the player somehow is labelled as a cheater with no option to apologize
        if jn_apologies.TYPE_CHEATED_GAME not in persistent.jn_player_pending_apologies:
            $ persistent.jn_snap_player_is_cheater = False

        else:
            n 1fnmem "[player]...{w=0.3} si ni siquiera te vas a disculpar por hacer trampas,{w=0.1} ¿por qué debería jugar siquiera?"
            n 1kllpo "Vamos...{w=0.3} no es tan difícil disculparse,{w=0.1} ¿o no?"
            return

    if Natsuki.isLove():
        n 1uchbg "¡Por supuesto que sí,{w=0.1} bobo!{w=0.2} Jejeje."

    elif Natsuki.isEnamored(higher=True):
        n 1fchbg "¡Claro jugaré un rato contigo,{w=0.1} bobo!"

    elif Natsuki.isAffectionate(higher=True):
        n 1fchsm "Bueno,{w=0.1} ¡dah!{w=0.2} ¡Claro que estoy lista para una partida!"

    else:
        n 1nnmss "¿Quieres jugar Snap?{w=0.2} ¡Pues venga!"

    n 1unmsm "Deja que agarre las cartas en un santiamén,{w=0.1} ¿vale?"
    play audio drawer
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")
    jump snap_intro

# Natsuki goes over the rules of snap again, for if the player has already heard the explanation pre-game
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_remind_snap_rules",
            unlocked=True,
            prompt="¿Me puedes explicar las reglas del Snap otra vez?",
            conditional="persistent.jn_snap_unlocked and persistent.jn_snap_explanation_given",
            category=["Videojuegos"],
            player_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_remind_snap_rules:
    if persistent.jn_snap_player_is_cheater:
        n 1fcsan "Venga,{w=0.1} [player]."
        n 1flrpo "Si tanto te importan las reglas,{w=0.1} ¿entonces por qué hiciste trampas la última vez?"
        n 1fnmpo "Ni siquiera te has disculpado todavía..."
        return

    else:
        if Natsuki.isLove():
            n 1nchbg "Jajaja.{w=0.2} Eres tan olvidadizo a veces,{w=0.1} [player]."
            n 1nsqbg "Claro,{w=0.1} ¡te lo explicaré una y otra vez!{w=0.2} Sooolo para ti~."

        elif Natsuki.isEnamored(higher=True):
            n 1nchbg "¡Por supuesto que puedo!"

        elif Natsuki.isAffectionate(higher=True):
            n 1fchsm "¡Puedes apostar por ello!"

        else:
            n 1nnmss "¡Ni lo dudes!"

        jump snap_explanation

# Natsuki hates people being inconsiderate with chewing gum
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_chewing_gum",
            unlocked=True,
            prompt="Chicle",
            category=["Hábitos"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_chewing_gum:
    n 1fcsan "Agh...{w=0.3} ¿sabes que me pone de los nervios de verdad?"
    n 1fsqsl "Cuando la gente da asco y no sabe se deshace bien de los chicles."
    n 1fbkwr "En serio -{w=0.1} ¡esa mierda me saca de mis casillas!"
    n 1fllem "Es como,{w=0.1} ¿sabes cuando estás andando por el centro de la ciudad y miras al suelo?{w=0.2} ¿A las calles?"
    n 1fcsan "Todos esos chicles resecos por el suelo -{w=0.1} es malditamente desagradable,{w=0.1} ¡y da puñetero asco!"
    n 1fsqan "Y para colmo es un sitio repleto de papeleras,{w=0.1} así que no solo es desagradable..."
    n 1fnmwr "¡También es de ser un vago!{w=0.2} No sé qué es peor."
    n 1fcswr "E incluso peor que eso -{w=0.1} están las personas que van y lo pegan debajo de las mesas,{w=0.1} o en las paredes -{w=0.1} ¡¿a {i}quién{/i} demonios se le ocurrió?!"
    n 1flrpu "Dios...{w=0.3} Me dan ganas de devolvérsela y metérselo de nuevo en sus estúpidas bocas."
    n 1nnmsl "No me importa si mascas chicle,{w=0.1} [player]."

    if Natsuki.isLove():
        n 1kllca "Pero asegúrate de tirarlo adecuadamente,{w=0.1} ¿'tá bien?"
        n 1kllss "De todos modos seguro que lo haces bien,{w=0.1} pero...{w=0.3} por si acaso."
        n 1kchsml "¡Te amo,{w=0.1} [player]~!"

    elif Natsuki.isAffectionate(higher=True):
        n 1nllca "Pero por favor,{w=0.1} simplemente asegúrate de tirarlo apropiadamente."
        n 1nchsm "¡Gracias,{w=0.1} [player]~!"

    else:
        n 1fnmaj "Pero en serio -{w=0.1} tíralo a una papelera cuando acabes,{w=0.1} ¿vale?{w=0.2} O envuélvelo en un pañuelo para deshacerte de el más tarde."
        n 1fsqaj "...¡O no será sólo chicle lo que mascaras!"

    return

# Natsuki hates people smoking/vaping indoors
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_smoking_vaping_indoors",
            unlocked=True,
            prompt="Fumar en interiores",
            category=["Hábitos"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_smoking_vaping_indoors:
    n 1fllaj "¿Sabes que apesta,{w=0.1} [player]?"
    n 1fsqaj "Me refiero a lo que apesta {i}de verdad{/i} -{w=0.1} no solo en sentido figurativo,{w=0.1} literalmente también."
    n 1fcssf "Cuando la gente fuma o vapea en interiores,{w=0.1} o cerca de una entrada -{w=0.1} {i}especialmente{/i} cuando hay más gente alrededor.{w=0.2} ¡No puedo aguantarlo!"
    n 1fcsan "Me refiero...{w=0.3} ¿Cuan desconsiderado puedes ser?{w=0.2} ¡En serio!"
    n 1fsqwr "Para empezar,{w=0.1} y como te iba diciendo  -{w=0.1} ¡{i}apesta{/i} absolutamente!"
    n 1fllem "El tabaco huele horrible,{w=0.1} y todos esos líquidos para el vaper no es que sean mucho mejor."
    n 1ksqup "Y para colmo se impregna en las paredes -{w=0.1} ¡así que sigue oliendo por años!"
    n 1kllan "Hablando de impregnarse,{w=0.1} el humo lo hace también -{w=0.1} ¿alguna vez has {i}visto{/i} la casa de un fumador,{w=0.1} o su coche?"
    n 1ksqup "Todas esas manchas amarillas...{w=0.3} parece que fue pintado o algo.{w=0.2} ¡Ew!"
    n 1fsqan "¿Y sabes qué,{w=0.1} [player]?{w=0.2} Todavía no he llegado a lo peor..."
    n 1fcsan "No he hablado de cuan caras son esas cosas,{w=0.1} o los problemas de salud ya no solo al que fuma..."
    n 1fsqaj "...¡Si no a todos los que tengan cerca!"
    n 1fcsbo "Agh..."
    n 1flrbo "No te confundas -{w=0.1} si alguien quiere fumar o vapear,{w=0.1} es su decisión y su dinero.{w=0.2} No me importa."
    n 1fnmbo "Pero al menos deberían respetar la decisión de los que {i}no{/i} quieren,{w=0.1} ¿sabes?"
    n 1fcssl "..."

    if Natsuki.isLove():
        n 1nnmsl "Te conozco,{w=0.1} [player].{w=0.2} Dudo mucho que seas ese tipo de persona asquerosa."
        n 1klrss "Simplemente...{w=0.3} no me decepciones,{w=0.1} ¿entendido?"
        n 1uchgn "¡Te lo agradecería!{w=0.2} Jajaja."

    elif Natsuki.isAffectionate(higher=True):
        n 1kllpo "Dudo que seas tan mala persona incluso si es que fumas,{w=0.1} [player]."
        n 1fsqpo "Pero...{w=0.3} no puedes decepcionarme,{w=0.1} ¿'tá bien?{w=0.2} Me gustas más así que siendo un asqueroso."
        n 1uchsm "¡Gracias!"

    else:
        n 1ullaj "No creo que seas tan mala persona,{w=0.1} [player]."
        n 1nnmaj "Pero...{w=0.3} solo por si acaso -{w=0.1} tenlo en mente,{w=0.1} ¿puede ser?"
        n 1nchsm "¡Gracias!"

    return

# Natsuki hates people who don't wash their hands after using a restroom
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_unwashed_hands",
            unlocked=True,
            prompt="Lavarse las manos",
            category=["Hábitos"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_unwashed_hands:
    n 1unmaj "Oye,{w=0.1} [player]."
    n 1nnmaj "¿Has trabajado alguna vez en un restaurante,{w=0.1} un hospital, o algo así?"
    n 1fnmaj "Por que entonces apuesto a que algo te esta taladrando el cerebro...{w=0.3} ¡Cuan importante es lavarte bien las manos!"
    n 1flraj "Me pone de los nervios que la gente no se lave las manos después de hacer algo desagradable."
    n 1fsqsl "Es como...{w=0.3} {i}Sabemos{/i} lo importante que es deshacerse de esos gérmenes -{w=0.1} ¡¿así que {i}cuán{/i} difícil es meter tus manos bajo el grifo un maldito minuto?!"
    n 1fsqem "¡Me molesta incluso mas cuando la persona es idiota al respecto!{w=0.2} Como si no tuvieran que lavárselas,{w=0.1} aunque no hagan nada."
    n 1fcsem "Pues aquí tengo una noticia -{w=0.1} si entraste,{w=0.1} has tenido que tocar algo -{w=0.1} ¡así que los gérmenes de esa cosa ahora van contigo!"
    n 1fsqsf "No solo es {i}super{/i} asqueroso y horrible para {i}tu{/i} salud..."
    n 1ksqan "¡También es asqueroso para el resto!{w=0.2} ¿Y si tienes que manejar la comida de alguien,{w=0.1} o visitar a alguien en el hospital?"
    n 1fllan "Podrías hacer que alguien se enferme seriamente..."
    n 1fnmfu "...¡Y todavía se enfadan si les dices algo al respecto!{w=0.2} A ver,{w=0.1} ¡venga {i}ya{/i}!"
    n 1fcssl "Simplemente...{w=0.3} agh."
    n 1ncssl "...[player]."
    n 1nnmpu "Realmente espero que mantengas tus manos impecables.{w=0.2} Y no sólo cuando vayas al baño."
    n 1fnmpu "Antes de preparar comida,{w=0.1} después de sacar la basura...{w=0.3} Solo tienes que pensar donde acabas de estar,{w=0.1} ¿entiendes?"

    if Natsuki.isLove():
        n 1kchbg "¡Pero tampoco me malinterpretes!{w=0.2} ¡Estoy segura de que intentas hacerlo correctamente!"
        n 1nnmbg "Tan solo...{w=0.3} Mantén ese buen trabajo,{w=0.1} ¿entendido?{w=0.2} Por todos."
        n 1nchsm "¡Gracias,{w=0.1} [player]!"

    else:
        n 1tsqpo "No es mucho pedir...{w=0.3} ¿o sí?"

    return

# Natsuki hates people who litter
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_litter",
            unlocked=True,
            prompt="Limpieza",
            category=["Hábitos"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_litter:
    n 1ullpu "Sabes,{w=0.1} [player]..."
    n 1unmaj "¿En la escuela?{w=0.2} En mi escuela,{w=0.1} ¿al menos?"
    n 1unmss "Nosotros -{w=0.1} los estudiantes -{w=0.1} somos responsables de mantener todo limpio."
    n 1fcsbg "Jejeje.{w=0.2} ¿Estás sorprendido?"
    n 1fchgn "¡Sip!{w=0.2} Desde las papeleras,{w=0.1} los escritorios,{w=0.1} hasta el suelo.{w=0.2} ¡Ha sido nuestro esfuerzo el que los mantuvo impecables!"
    n 1flrpol "N-{w=0.1}no es que me {i}gustara{/i},{w=0.1} ¡por supuesto!{w=0.2} Limpiar {i}es{/i} bastante aburrido,{w=0.1} pero es algo que hay que hacer."
    n 1fnmpo "Pero te diré una cosa,{w=0.1} [player]."
    n 1fsqtr "{i}Nada{/i} me enfada más que los desgraciados que dejan tirada toda su basura por ahí."
    n 1fnman "...¡No solo en la escuela!"
    n 1fcsan "A ver...{w=0.3} ¡¿por dónde empiezo?!"
    n 1fnmaj "Primero que todo -{w=0.1} ¿hasta qué punto se puede ser un maldito vago?{w=0.2} ¡¿Esa gente simplemente tira todo por ahí al llegar a sus casas?!"
    n 1flran "¡Me molesta incluso más cuando tienen papeleras justo enfrente!"
    n 1fcsfu "Es como,{w=0.1} guau...{w=0.3} ¿además de vago, desconsiderado?{w=0.2} ¡Que combinación más {i}maravillosa{/i}!"
    n 1fllpu "Incluso si quitásemos el factor de la papelera..."
    n 1fllan "¡Es como si no tuvieran bolsillos,{w=0.1} o no pudieran llevarlo en la mano un par de minutos!"
    n 1fcsan "Agh..."
    n 1flrup "¡Y sin mencionar a los que tiran basura desde el coche en marcha,{w=0.1} o en lagos y estanques!"
    n 1fcssl "Me enfada de solo pensarlo..."
    n 1fllbo "..."
    n 1fnmbo "[player]."

    if Natsuki.isEnamored(higher=True):
        n 1ksqbo "Te conozco.{w=0.2} De hecho,{w=0.1} me atrevería a decir que te conozco {i}mejor{/i} que mucha gente."
        n 1knmbo "Y no creo que seas el tipo de persona que haría eso…..."
        n 1klraj "No me equivoco...{w=0.3} ¿verdad?"
        n 1klrss "No me gustaría estarlo.{w=0.2} Jajaja..."

    elif Natsuki.isAffectionate(higher=True):
        n 1unmaj "No creo que seas así,{w=0.1} [player]."
        n 1ullsl "O...{w=0.3} Al menos {i}intentas{/i} no serlo."

    else:
        n 1fnmsl "De verdad,{w=0.1} realmente espero que no seas uno de esos."

    n 1nllpu "Así que..."
    n 1nnmsl "...Si has ensuciado algo,,{w=0.1} te lo dejaré pasar esta vez."
    n 1klrpo "Simplemente...{w=0.3} asegúrate de limpiarlo,{w=0.1} ¿entendido?"

    if Natsuki.isLove():
        n 1uchsml "Jejeje.{w=0.2} Te amo,{w=0.1} [player]~."

    elif Natsuki.isAffectionate(higher=True):
        n 1nlrpol "Eso...{w=0.3} significaría mucho para mí."

    else:
        n 1fchbg "Gracias,{w=0.1} [player]."

    return

# Natsuki discovers a music player, leading to the unlocking of custom music!
# We assign no categories to this so it isn't selectable via menu, making it a one-time conversation
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_custom_music_introduction",
            unlocked=True,
            prompt="Descubriendo la música personalizada",
            conditional="not persistent.jn_custom_music_unlocked",
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_custom_music_introduction:
    n 1fllpu "Hmm..."
    n 1flrbo "Me pregunto si seguirá aquí..."

    play audio drawer
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    n 1fllpo "¡Vamos!{w=0.2} ¡Tiene que estar por aquí!{w=0.2} ¡Lo se!"

    play audio drawer
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    n 1uspbg "..."
    n 1fchbs "¡Aja!{w=0.2} ¡Si!"
    n 1nchsm "..."
    n 1uwdbg "¡Oh!{w=0.2} ¡[player]!{w=0.2} ¡[player]!"
    n 1uchgn "¡Adivina lo que he encontraaado!{w=0.2} Jejeje."
    n 1nchbs "Es...{w=0.3} ¡un reproductor de música!{w=0.2} Genial,{w=0.1} ¿cierto?"
    n 1tlrbg "Bueno...{w=0.3} Algo es algo.{w=0.2} No es precisamente...{w=0.3} {i}moderno{/i},{w=0.1} ¡pero me sirve!"
    n 1tllpo "Ahora que lo pienso...{w=0.3} Ni siquiera se a quien le pertenece."
    n 1unmpu "La encontramos abandonada en la sala del club un día.{w=0.2} Nadie sabía si le pertenecía a alguien -{w=0.1} y créeme,{w=0.1} ¡le buscamos!"
    n 1tnmsl "Preguntamos en todas las clases,{w=0.1} pusimos carteles...{w=0.3} ¡y nada!"
    n 1tlrbg "Así que...{w=0.3} lo guardamos aquí,{w=0.1} en mi escritorio,{w=0.1} por si acaso quien sea volviese a recogerlo."
    n 1tsqpo "Supongo que ya nadie lo hará,{w=0.1} ¿eh?"
    n 1uchbg "Bueno,{w=0.1} da igual.{w=0.2} ¡El punto es que ahora podemos poner la música que queramos!"
    n 1fchbg "Creo que se me ha ocurrido una idea para que me des lo que quieras poner,{w=0.1} así que escúchame,{w=0.1} ¿'ta bien?"
    jump talk_custom_music_explanation

# Natsuki explains how the custom music functionality works
# Unlocked as a permanent topic once Natsuki has naturally lead into this from talk_custom_music_introduction via random topics
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_custom_music_explanation",
            unlocked=True,
            prompt="¿Puedes repetirme cómo funciona la música personalizada?",
            category=["Música"],
            conditional="persistent.jn_custom_music_unlocked and persistent.jn_custom_music_explanation_given",
            player_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_custom_music_explanation:
    if persistent.jn_custom_music_explanation_given:
        n 1unmaj "¿Eh?{w=0.2} ¿Quieres que te explique cómo funciona la música personalizada otra vez?"
        n 1uchbg "Claro,{w=0.1} ¡puedo hacerlo!"
        n 1nnmsm "Primero lo primero,{w=0.1} déjame comprobar si está la carpeta {i}custom_music{/i}..."

    else:
        n 1unmbg "¡De acuerdo!{w=0.2} A ver...{w=0.3} de hecho es bastante simple,{w=0.1} [player]."
        n 1nnmsm "Debería haber una carpeta llamada {i}custom_music{/i} por ahí..."
        n 1nchbg "Déjame comprobarlo,{w=0.1} un segundo..."
        n 1ncssr "..."

    if jn_custom_music.get_directory_exists():
        n 1tnmbg "Bueno,{w=0.1} ¡mira por dónde!{w=0.2} ¡Ya estaba ahí!{w=0.2} Debí de haberla creado y se me olvidó."
        n 1uchgn "¡Menos complicaciones para mí! No me quejo."

    else:
        n 1uchbg "¡Muuuy bien!{w=0.2} No estaba,{w=0.1} así que la cree para ti."

    $ folder = jn_custom_music.CUSTOM_MUSIC_DIRECTORY
    n 1nnmss "Entonces,{w=0.1} [player] -{w=0.1} si haces clic {a=[folder]}aquí{/a},{w=0.1} te llevara a la carpeta que te dije."
    n 1ullbg "Así que lo único que tienes que hacer es {i}copiar{/i} tu música en esa carpeta,{w=0.1} ¡y ya estaría!"
    n 1uchgn "Facilito,{w=0.1} ¿eh?{w=0.2} Jejeje."
    n 1uwdaj "Oh -{w=0.1} un par de cosas más,{w=0.1} [player]."
    n 1unmpu "Cualquier música que me des tiene que estar en formato {i}.mp3,{w=0.1} .ogg o .wav{/i}."
    n 1ullss "Si no sabes como comprobarlo,{w=0.1} tan solo tienes que mirar las letras que van después del punto, al final del nombre del archivo."
    n 1unmss "También puedes verlo en las {i}propiedades{/i} del archivo si no te aparece en el nombre."
    n 1flrbg "Como dije -{w=0.1} esto no es {i}precisamente{/i} super moderno,{w=0.1} así que no va a funcionar con los estilosos nuevos formatos,{w=0.1} ni con los antiguos raros."
    $ persistent.jn_custom_music_unlocked = True
    $ persistent.jn_custom_music_explanation_given = True
    n 1nnmaj "Una vez hecho eso,{w=0.1} tan solo tienes que pulsar en el botón {i}Música{/i},{w=0.1} y comprobar que todo esté en orden."
    n 1nchbg "...¡Y eso es todo!"
    n 1nsqbg "Aunque he de advertirte,{w=0.1} [player]..."
    n 1usqsg "Espero que tengas buen gusto."
    n 1uchgn "¡Jajaja!"
    return

# Natsuki's thoughts on VTubers
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_vtubers",
            unlocked=True,
            prompt="¿Sigues a algún VTuber?",
            category=["Videojuegos", "Contenido", "Sociedad"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_vtubers:
    if Natsuki.isEnamored(higher=True):
        n 1tllss "VTubers,{w=0.1} ¿eh?{w=0.2} ¿Me lo preguntas a {i}mí{/i}?"
        n 1fnmsm "...Guau,{w=0.1} [player].{w=0.2} Estoy impresionada."
        n 1fsqsm "Una vez más,{w=0.1} ¡has demostrado que eres aún más friki que yo!"
        n 1uchsm "Jejeje."
        n 1klrbg "¡Relájate!{w=0.2} Relájate,{w=0.1} ¡dios!{w=0.2} Ya sabes que nunca juzgaría tus pasatiempos en serio,{w=0.1} idiota."
        n 1unmaj "Pero eso,{w=0.1} igualmente..."

    elif Natsuki.isHappy(higher=True):
        n 1unmbg "¡Claro!{w=0.2} ¡Creo que los conozco!"
        n 1tnmpu "Son esas personas que usan avatares anime para hacer streaming para otros,{w=0.1} ¿cierto?"
        n 1tllpu "Bueno..."

    elif Natsuki.isNormal(higher=True):
        n 1unmpu "¿Eh?{w=0.2} ¿VTubers?{w=0.2} ¿Como esa gente con avatares estilo anime que juegan a juegos y cosas online para que la gente los vea?"
        n 1tnmpu "Eso {i}es{/i} a lo que te refieres,{w=0.1} ¿cierto?"
        n 1tllpu "Bueno..."

    elif Natsuki.isDistressed(higher=True):
        n 1fsqpu "No,{w=0.1} no sigo a ninguno.{w=0.2} Prefiero jugar a los juegos por mi misma en vez de que alguien lo haga por mí."
        n 1fsqbo "Si sigues a alguno,{w=0.1} bien por ti."
        n 1flrbo "{i}Algunos{/i} de nosotros no tenemos tiempo para sentar nuestro culo en el sitio por horas..."
        n 1fsqaj "...O dinero para dárselo a desconocidos."
        n 1fsqpu "[player]."
        n 1fsqsr"Cuanto apostamos a que no estás {i}ni cerca{/i} de ser tan toxico con {i}ellos{/i} como lo eres conmigo, ¿eh?"
        return

    else:
        n 1fsqan "No.{w=0.2} Y no me importa una mierda si tu lo haces,{w=0.1} tampoco."
        n 1fnmpu "...Y oye,{w=0.1} nuevas noticias,{w=0.1} idiota."
        n 1fsqpu "Tirarle dinero a extraños que ocultan su identidad bajo una adorable imagen no te hace más que un imbécil."
        return

    n 1nchsm "¡Me parece una gran idea!{w=0.2} Permite a las personas compartir sus pasiones y experiencias con los demás detrás de un personaje completamente limpio..."
    n 1fllpo "Sin preocuparse de que afecte a su vida personal,{w=0.1} o que la gente sea repugnante,{w=0.1} o cosas así."
    n 1uwdem "Muchos incluso hacen carreras completas en base a ello: Merchandising,{w=0.1} canciones y de todo -{w=0.1} ¡como si fueran idols!{w=0.2} ¡Es una locura!"
    n 1tllem "Dicho esto..."
    n 1tnmbo "Yo nunca me metería en este tipo de cosas."
    n 1klrss "Quiero decir...{w=0.3} ¡No me malentiendas!{w=0.2} Estoy segura de que debe ser muy divertido de ver.{w=0.2} Si te gustan ese tipo de cosas,{w=0.1} claro."
    n 1nllsl "Pero yo prefiero jugar o hacer lo que sea {i}por mi misma{/i} más que ver a alguien mas haciéndolo,{w=0.1} al menos normalmente."
    n 1nllss "Aunque soy solo yo,{w=0.1} supongo."
    n 1nllbg "Jejeje."
    n 1unmaj "¿Y qué hay de ti,{w=0.1} [player]?{w=0.2} ¿Te gustan ese tipo de cosas?"
    n 1fcssm "Espera,{w=0.1} ¡espera!{w=0.2} No te molestes en responder."
    n 1tsqsm "Me {i}has{/i} preguntado sobre esto,{w=0.1} después de todo -{w=0.1} creo que eso habla por ti,{w=0.1} ¿no crees?"
    n 1uchbs "¡Jajaja!"
    return

# Natsuki discusses her skateboarding past, and why she used to use one
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_skateboarding",
            unlocked=True,
            prompt="¿Te gusta montar en monopatín?",
            category=["Transporte"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_skateboarding:
    if Natsuki.isEnamored(higher=True):
        n 1fchbs "¡Ahí le has dado,{w=0.1} [player]!{w=0.5}{nw}"
        extend 1fchsm " Jejeje."
        n 1tllbg "¿Pero cómo lo has adivinado?{w=0.5}{nw}"
        extend 1tnmbg " ¿Parezco la típica chica que haría algo así?"
        n 1tlrsm "Bueno,{w=0.1} da igual."

    elif Natsuki.isHappy(higher=True):
        n 1uchsm "Jejeje.{w=0.5}{nw}"
        extend 1fchbg " ¡Ahí le has dado!"
        n 1uwlbg "¡Buena deducción,{w=0.1} [player]!"

    elif Natsuki.isNormal(higher=True):
        n 1ullaj "A mí...{w=0.3} me gusta,{w=0.1} de hecho.{w=0.5}{nw}"
        extend 1tllss " ¿Cómo lo has adivinado?"
        n 1unmss "Bueno,{w=0.1} da igual."

    elif Natsuki.isDistressed(higher=True):
        n 1fcsaj "Agh..."
        n 1fnmbo "Si,{w=0.1} [player].{w=0.2} Me gusta hacer skate.{w=0.2} Monto en monopatín.{w=0.5}{nw}"
        extend 1fsqsf " ¿Es eso un problema?"
        n 1fllpu "Solo es una conveniente forma de moverse.{w=0.5}{nw}"
        extend 1fsqpu " La forma mas {i}rentable{/i}."
        n 1flrsl "..."
        n 1flraj "...Ya.{w=0.2} No tengo mucho mas que decir al respecto.{w=0.5}{nw}"
        extend 1fnmbo " Pero oye."
        n 1fsgaj "No es que realmente quieras escucharme...{w=0.5}{nw}"
        extend 1fsqsf " ¿No es eso cierto,{w=0.1} {i}[player]{/i}?"
        return

    else:
        n 1fsqan "...¿Y desde cuando {i}a ti{/i} te importa una mierda mis pasatiempos o intereses?"
        n 1fcsan "..."
        n 1fnmsf "Sí,{w=0.1} [player].{w=0.5}{nw}"
        extend 1fsqsf "Me {i}gusta{/i} hacer skate."
        n 1fsqup "Y preferiría estar haciendo eso en vez de estar aquí atrapada {i}contigo{/i}.{w=0.5}{nw}"
        extend 1fcsan " Bastardo."
        return

    n 1tchbg "¡Soy una chica que le gusta el skate!{w=0.5}{nw}"
    extend 1tslbo " O...{w=0.3} ¿Fui?"
    n 1tllss "Igualmente...{w=0.3} Realmente no tuve opción.{w=0.5}{nw}"
    extend 1knmaj " ¡Las bicis son {i}caras{/i}, [player]!"
    n 1kllun "Y nunca me fie del teleférico de mi...{w=0.3} pueblo,{w=0.3}{nw}"
    extend 1kllss " ¡así que ahorre todo lo que pude y me compre un monopatín a la primera oportunidad que tuve!"
    n 1nsqaj "En serio.{w=0.5}{nw}"
    extend 1fllpu " No tienes ni {i}idea{/i} de cuantos almuerzos me salte para ahorrar eso."
    n 1unmbg "¡Pero ha sido super cómodo!{w=0.5}{nw}"
    extend 1flrbg " No tenia que preocuparme de atarla a algún lugar,{w=0.1} o de algún imbécil que la destroce..."
    n 1fchsm "Podía simplemente agarrarla y llevármelo conmigo,{w=0.1} o meterlo en mi casillero."
    n 1nslss "A ver...{w=0.3} ya no la necesito mas {i}ahora{/i},{w=0.1} pero..."
    n 1fsqss "Tienes que admitirlo,{w=0.1} [player] {w=0.1}-{w=0.1} ¡Otra cosa no, pero recursos tengo!{w=0.5}{nw}"
    extend 1fchsm " Jajaja."
    n 1fllss "Yo...{w=0.3} realmente nunca aprendí a hacer ningún truco ni nada.{w=0.5}{nw}"
    extend 1kscwr " No podía ni pensar en romperla por accidente {w=0.1}-{w=0.3}{nw}"
    extend 1kllun " ¡no después de ese esfuerzo!"
    n 1kcsaj "...Si,{w=0.1} sí.{w=0.5}{nw}"
    extend 1fcspo " No es muy {i}radical{/i} de mi parte,{w=0.1} ¿eh?"
    n 1ullpo "Pero...{w=0.3} ya valió por ahora.{w=0.5}{nw}"
    extend 1fnmsm " Igualmente,{w=0.1} [player]..."
    n 1fsqss "Se podría decir que esto se queda en...{w=0.3} {i}tablas{/i}."
    n 1fchsm "Jejeje.{w=0.5}{nw}"
    extend 1uchgn " ¡No me arrepiento de eso,{w=0.1} [player]!"
    return

# Natsuki describes her experiences with sports at school
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_sports",
            unlocked=True,
            prompt="¿Haces mucho deporte?",
            category=["Salud"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_sports:
    if Natsuki.isAffectionate(higher=True):
        n 1unmaj "¿Eh?{w=0.2} ¿Deporte?"
        n 1fllss "A mí...{w=0.3} no me gustaría tener que desilusionarte,{w=0.1} [player]..."
        n 1fchgn "¿Pero qué clase de deporte crees que puedo hacer en una habitación?{w=0.2} ¿Sola?{w=0.2} ¿Y sin equitación?"
        n 1kllbg "Dios...{w=0.5}{nw}"
        extend 1tnmss " eres muy despistado a veces,{w=0.1} [player]."
        n 1ullbg "Bueno,{w=0.1} igualmente."

    elif Natsuki.isNormal(higher=True):
        n 1unmpu "¿Eh?{w=0.2} ¿Deporte?"
        n 1tnmdv "Tú...{w=0.3} sabes que es complicado mantenerse en forma estando sola en un cuarto,{w=0.1} ¿cierto?"
        n 1fcsss "Jejeje.{w=0.5}{nw}"
        extend 1ullss " Bueno,{w=0.1} igualmente."

    elif Natsuki.isDistressed(higher=True):
        n 1nsqpu "Ya,{w=0.1} como que no.{w=0.5}{nw}"
        extend 1fsqsl " {i}Ahora mismo{/i} no,{w=0.1} si eso es lo que preguntas."
        n 1fllpu "..."
        n 1fsqan "...Y no,{w=0.2} no usamos ese tipo de uniformes si es en lo que {i}estás{/i} pensando."
        n 1fsqsr "¿Eso responde a tu pregunta?{w=0.5}{nw}"
        extend 1fslbo " No importa."
        n 1fcsbo "Sigamos."
        return

    else:
        n 1fsqan "{i}Ahora mismo{/i} no,{w=0.1} si por alguna razón no te diste cuenta."
        n 1fslsl "..."
        n 1fsqpu "..."
        n 1fcsun "...¿Qué si quiero saber por qué preguntas?"
        n 1fcsan "...No.{w=0.2} La verdad {i}no{/i}."
        return

    n 1nnmaj "He intentado mantenerme como he podido.{w=0.2} No puedo correr ni nada,{w=0.5}{nw}"
    extend 1fcsbg " ¡pero al menos puedo hacer estiramientos o saltos de tijera sin dificultad!"
    n 1ullpu "Por supuesto en la escuela era mucho mas variado,{w=0.1} pero...{w=0.5}{nw}"
    extend 1tllsr " Siempre tuve problemas para hacer deporte."
    n 1tllss "Supongo...{w=0.3} ¿que no tengo mucha resistencia?"

    # Check to see if the player and Natsuki have discussed how she skipped lunches to save money
    $ already_discussed_skateboarding = get_topic("talk_skateboarding").shown_count > 0
    if already_discussed_skateboarding:
        n 1nslpo "Y probablemente haber ahorrado para el monopatín no haya ayudado..."

    n 1ullaj "Bueno,{w=0.1} da igual.{w=0.5}{nw}"
    extend 1nnmbo " Nunca estuve {i}muy{/i} metida en el deporte de todas formas."
    n 1nlrca "..."
    n 1unmbs "¡Oh!{w=0.2} ¡Oh!{w=0.2} ¿Pero sabes quién sí?{w=0.5}{nw}"
    extend 1fsqbg " Seguro que sí,{w=0.1} ¿eh?{w=0.5}{nw}"
    extend 1fcssm " Jejeje."
    n 1tsqss "Y es...{w=0.5}{nw}"
    extend 1fchgn " ...{w=0.3}Sayori,{w=0.1} ¡dah!"
    n 1uskgs "Quiero decir,{w=0.1} ¡lo digo en serio!{w=0.2} ¡Tenías que haberla visto!{w=0.5}{nw}"
    extend 1fnmca " ¡Era un {i}peligro{/i}!"
    n 1uskaj "...¡En serio!{w=0.5}{nw}"
    extend 1fnmpo " ¿No me crees?"
    n 1fspgs "¡Ella era tan rápida!{w=0.2} Como un destello de algo anaranjado y ropa de deporte arrugada...{w=0.5}{nw}"
    extend 1fbkwr " ¡Y entonces bum!{w=0.2} ¡Te lleva por delante!"
    n 1fllpol "Y aun así seguía hacia delante,{w=0.1} hacia el horizonte..."
    n 1tsqaj "...Ya.{w=0.2} ¿Y si Sayori estaba en tu equipo?{w=0.5}{nw}"
    extend 1fllbg " {i}Sabias{/i} que tu equipo era incapaz de ser derrotado."
    n 1ullaj "A ver,{w=0.3}{nw}"
    extend 1nnmbo " Monika también fue siempre buena en los deportes,{w=0.1} obviamente.{w=0.5}{nw}"
    extend 1nsgca " Pero {i}nadie{/i} para a Sayori,{w=0.1} [player].{w=0.2}"
    n 1nsqun " N{w=0.1}-{w=0.1}a{w=0.1}-{w=0.1}d{w=0.1}-{w=0.1}i{w=0.1}-{w=0.1}e."
    n 1fchbg "...Bueno, cuando se acordaba de atarse los zapatos.{w=0.5}{nw}"
    extend 1fchsm " Jejeje."
    return

# Natsuki laments her frustrations with online shopping, and the disappearance of physical stores
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_online_shopping",
            unlocked=True,
            prompt="Compras online",
            category=["Sociedad"],
            nat_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_online_shopping:
    if Natsuki.isNormal(higher=True):
        n 1ullaj "Sabes,{w=0.1} es una locura lo común que es comprar online hoy en día."
        n 1uwdaj "A ver,{w=0.1} ¡no me malentiendas!{w=0.5}{nw}"
        extend 1fcsbg " ¡Es super conveniente!{w=0.2} ¡Ni siquiera tienes por que salir de casa!"
        n 1fllpo "Así que no pienses que me estoy quejando,{w=0.1} ni nada parecido.{w=0.5}{nw}"
        extend 1ullpu " Pero..."

    else:
        n 1nllsl "Es gracioso cuan común se ha vuelto comprar online."
        n 1nlrsl "Aunque supongo que no es una queja.{w=0.5}{nw}"
        extend 1nlrpu " {i}Es{/i} muy cómodo de usar."
        n 1ulrpu "Pero...{w=0.5}{nw}"
        extend 1nnmsf " Sigo pensando que es una vergüenza que la gente que la gente se pierda la experiencia de ir de compras."
        n 1fllsl "Nunca dejaría pasar una tarde hojeando libros en mi librería favorita."
        n 1fcssf "...Lugar en el que preferiría estar {i}ahora mismo{/i}.{w=0.5}{nw}"
        extend 1fsqan " {i}Sorprendentemente{/i}."
        return

    n 1fllbg "Pero no creo que sea toda una maravilla,{w=0.1} ¿sabes?"
    n 1unmaj "Quiero decir...{w=0.3} piensa sobre ello,{w=0.1} [player]."
    n 1fllaj "Supongo que es mas barato si no tienes que ir en coche a un sitio,{w=0.1} pagar el aparcamiento o lo que sea."
    n 1knmpu "¿Pero no quieres {i}ver{/i} por lo que estás pagando?{w=0.5}{nw}"
    extend 1fnmaj " ¡Especialmente si es super caro!"
    n 1fllpu "O a veces...{w=0.5}{nw}"
    extend 1fllpu " ¡incluso si no lo es!"
    n 1fllpo "No puedo ser la única que se ha enfadado por que algo que ha pedido resulto ser una mierda,{w=0.1} o llegó roto,{w=0.1} ¿verdad?"
    n 1fnmem "¡Y ni siquiera sabes si te va a gustar hasta que ya lo tienes en la puerta!{w=0.5}{nw}"
    extend 1fcsan " ¡Y entonces tienes que devolverlo!{w=0.5}{nw}"
    extend 1fslem " Agh."

    # Check to see if the player and Natsuki have discussed careful spending
    if get_topic("talk_careful_spending").shown_count > 0:
        n 1fllsl "No es solo eso..."
        n 1fnmpu "Creo que ya te mencioné antes como las tiendas hacen muy sencillo que gastes dinero...{w=0.5}{nw}"
        extend 1fbkwr " ¡pero es incluso más fácil online!{w=0.5}{nw}"
        extend 1kbkwr " ¡Ni siquiera {i}sientes{/i} que estés gastando dinero apropiadamente!"
        n 1fcsan "Demonios."

    n 1fcsem "Aparte de eso..."
    n 1kllsl "Esto...{w=0.3} también hace que me sienta algo triste de ver que las tiendas locales cierren,{w=0.1} además."
    n 1tnmsl "Se podría decir que solo son negocios,{w=0.1} y que esta vez salieron perdiendo."
    n 1flrsll "Pero eso {i}no{/i} significa que no vaya a echar de menos algunos."
    n 1ncsem "No se.{w=0.2} Supongo que lo que intento decir es..."
    n 1fllpo "No descartes todo lo que no puedas hacer o comprar online,{w=0.1} [player]."
    n 1knmaj "¡Todavía tiene mérito conseguir tus cosas en físico!"
    n 1fnmss "Y si te soy completamente honesta..."

    if Natsuki.isEnamored(higher=True):
        n 1fsqbg "No me importa realmente cuanto te niegues."
        n 1fchgn "Vamos a ir a una librería {i}de verdad{/i} en algún momento {w=0.1}-{w=0.1} ¡quieras o no!{w=0.5}{nw}"
        extend 1fchsm " Jejeje."

    elif Natsuki.isHappy(higher=True):
        n 1fchgn " ¡Tienes que estar bromeando si crees que te voy a dejar perderte ir a una librería {i}de verdad{/i}!{w=0.5}{nw}"
        extend 1nchbg " Jajaja."

    else:
        n 1fchbg "Hay una cosa que voy a tener que enseñarte en algún momento,{w=0.1} ¡la experiencia de una librería {i}de verdad{/i}!{w=0.5}{nw}"
        extend 1fchsm " Jajaja."

    return

# Natsuki hates forced subscription services, and accidentally paying for trial periods
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_subscriptions",
            unlocked=True,
            prompt="Suscripciones",
            category=["Hábitos"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_subscriptions:
    n 1fllan "Grrr..."
    n 1fcsan "¡Rayos,{w=0.1} si que son {i}molestos{/i}!{w=0.5}{nw}"
    extend 1fbkwr " ¡Creí que ya había cancelado esooooo!"
    n 1fslpo "..."
    n 1uwdem "¡O-{w=0.1}oh!{w=0.2} ¡[player]!{w=0.5}{nw}"
    extend 1flrem " ¿Puedes {i}creer{/i} esto?"
    n 1fslem "Me suscribí a una prueba gratis de una página de streaming,{w=0.3}{nw}"
    extend 1fcswr " ¡pero se me olvidó cancelarla!{w=0.5}{nw}"
    extend 1flrwr " ¡Y ahora {i}debo{/i} pagar por algo que casi no uso!"
    n 1fcsem "Malditos...{w=0.5}{nw}"
    extend 1tnmem " ¿No te molesta también?"
    n 1tllbo "Hablando de eso,{w=0.1} pensándolo bien..."
    n 1fnmbo "¿Por qué ahora todo se maneja con suscripciones?"
    n 1fllpu "Me refiero a que...{w=0.5}{nw}"
    extend 1nnmaj " Entiendo que es lo que mejor les funciona,{w=0.3}{nw}"
    extend 1flrsl " ¡¿pero qué manía tienen esos empresarios con poner suscripciones para todo?!"
    n 1fsqsl "Y la mitad de las veces ni siquiera tienes opción...{w=0.5}{nw}"
    extend 1fsqem " ¡cómo con el software!"
    n 1fcsan "¡He desinstalado varios programas porque a fuerzas quieren hacerme pagar por el paquete completo, no necesito todas sus porquerias!"
    n 1fllan "En serio...{w=0.3} ¡{i}Por favor{/i}!{w=0.5}{nw}"
    extend 1fllfr " ¡Déjame pagar solo por lo que quiero!"
    n 1kcsem "Agh..."
    n 1fnmsl "¡Lo peor es que al final todo se te acumula!{w=0.5}{nw}"
    extend 1fllpu " Es muy fácil perder la noción de cúanto pagas cada mes en suscripciones..."
    n 1fnmpu "Y antes de que te des cuenta,{w=0.3}{nw}"
    extend 1fbkwr " ¡ya debes la mitad del dinero que ganas!{w=0.5}{nw}"
    extend 1fcspu " Es un desastre..."
    n 1ullaj "Mira,{w=0.1} no me malinterpretes.{w=0.2} Sé que hay {i}otras{/i} formas de obtener ese contenido {w=0.1}-{w=0.3}{nw}"
    extend 1fsqdv " y estoy segura de que sabes de lo que hablo."
    n 1tlrsl "Pero también quiero apoyar a los creadores,{w=0.1} ¿sabes?"
    n 1fcssl "..."
    n 1fllpo "Bueno,{w=0.1} como sea.{w=0.2} Al menos no me volverán a cobrar por {i}eso{/i}.{w=0.5}{nw}"
    extend 1fslpo " Malditos."
    n 1nllbo "Pero...{w=0.5}{nw}"
    extend 1unmpu " ¿qué opinas de esto, [player]?{w=0.5}{nw}"
    extend 1fsqsm " Bueno,{w=0.1} algo si puedo decirte."

    if Natsuki.isAffectionate(higher=True):
        n 1fsqssl "¡A-{w=0.1}al menos {i}mi{/i} subscripción no tienes que preocuparte por pagarla!"

        if Natsuki.isLove():
            n 1fchsml "Jejeje.{w=0.5}{nw}"
            extend 1uchbgf " ¡Te amo,{w=0.1} tonto!"

        else:
            n 1fllbgl "J-{w=0.1}jajaja..."

    else:
        n 1fcsbg "Ya estás suscrito a algo muy bueno,{w=0.1} te lo digo yo."
        n 1nsqsg "Para tu suerte,{w=0.1} no cobro.{w=0.5}{nw}"
        extend 1fsqss "...Aún."
        n 1fchsm "Jeje."

    return

# Natsuki discusses the possibility of the player contributing to JN (and praises the JN team)
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_mod_contributions",
            unlocked=True,
            prompt="Contribuciones",
            conditional=(
                "not jn_activity.ACTIVITY_SYSTEM_ENABLED "
                "or jn_activity.has_player_done_activity(jn_activity.JNActivities.coding)"
            ),
            category=["Mod"],
            nat_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_mod_contributions:
    n 1unmaj "Oye,{w=0.1} [player].{w=0.5}{nw}"
    extend 1tllss " Debo decir que..."
    n 1klrbg "No creo que {i}nunca{/i} sea capaz de mantener todo lo que se usa aquí y que te permite visitarme.{w=0.5}{nw}"
    extend 1klrsl " No sola."
    n 1uskeml "¡D-digo,{w=0.1} soy buena en esto!{w=0.5}{nw}"
    extend 1fnmpol " ¡N-{w=0.1}no te equivoques!"
    n 1kllpo "Pero no soy...{w=0.3} {i}tan{/i} buena.{w=0.5}{nw}"
    extend 1fslpo " Aún."
    n 1uchbg "¡Es por eso que estoy super agradecida con toda la gente que se dedica a ayudarme!{w=0.5}{nw}"
    extend 1fchsm " ¿No es genial?"
    n 1fslsl "Siempre me confundo con esto de la programación,{w=0.3}{nw}"
    extend 1kllss " ¡así que no me imagino que haría sin ellos!"
    n 1ksqsg "...Aún si {i}son{/i} un montón de frikis.{w=0.5}{nw}"
    extend 1uchgn " Jeje."
    n 1ulraj "Bueno...{w=0.3} de seguro te preguntas,{w=0.1} ¿a que me refiero con esto?{w=0.5}{nw}"
    extend 1tslsm " Bien..."

    if not jn_activity.ACTIVITY_SYSTEM_ENABLED:
        n 1tllss "No sé si tu eres parte de la bola de frikis,{w=0.1} [player]..."
        n 1fchbg "¿Pero qué tal si me echas una mano?"

    else:
        n 1fsqsg "He estado viendo los programas que has abierto recientemente,{w=0.1} [player]."
        n 1ksqss "¿Qué?{w=0.5}{nw}"
        extend 1fchbg " ¿Esperabas que no me diera cuenta?{w=0.5}{nw}"
        extend 1nchgn " Jeje."
        n 1tsqbg "Como sea -{w=0.1} ya que sabes de ese tipo de cosas,{w=0.1} [player]...{w=0.5}{nw}"
        extend 1kchbg " ¿por qué no ayudarme?"

    n 1kllbg "¡No tienes que ser un genio de la programación,{w=0.1} ni nada de eso!{w=0.5}{nw}"
    extend 1unmaj " Arte,{w=0.1} escritura,{w=0.1} o simples sugerencias sobre que temas se podrían añadir o nuevas actividades que podamos hacer juntos -{w=0.3}{nw}"
    extend 1uchbg " ¡toda contribución es apreciada!"
    n 1tsqbg "¿Te parece,{w=0.1} [player]?{w=0.5}{nw}"
    extend 1uchsm " ¡Claro que si!{w=0.2} Jeje."
    n 1unmbg "Bueno,{w=0.1} ¡no dejes que la presión te detenga!{w=0.5}{nw}"
    extend 1uchbgl " ¡Puedes darle un vistazo a mi página web original {a=https://github.com/Just-Natsuki-Team/NatsukiModDev}aquí{/a}!"
    n 1nsqbg "Echarle un vistazo no te hará daño,{w=0.1} ¿verdad?{w=0.5}{nw}"
    extend 1nchsm " Jajaja."

    if Natsuki.isLove():
        $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
        n 1nchtsl " ¡Te amo,{w=0.1} [chosen_endearment]!"

    else:
        n 1fchbg " ¡Gracias,{w=0.1} [player]!{w=0.2} ¡Se aprecia tu esfuerzo!"

    return

# Natsuki ponders her new understanding of the separation between the player and MC as entities
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_realizations_player_ddlc_actions",
            unlocked=True,
            prompt="Recuerdos de DDLC",
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 60 >= 30",
            category=["DDLC", "Natsuki", "TÚ"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_realizations_player_ddlc_actions:
    n 1nllbo "Así que,{w=0.5}{nw}"
    extend 1nnmbo " [player]."
    n 1ulraj "He estado...{w=0.3} pensando.{w=0.5}{nw}"
    extend 1nllss " Ahora que tengo tiempo para procesar..."
    n 1kslsl "...esto."
    n 1unmaj "Tú eres el que ha estado aquí todo el tiempo,{w=0.1} ¿verdad?{w=0.5}{nw}"
    extend 1tslbo " Entonces,{w=0.1} eso significa que..."
    n 1tslbo "El chico que se unió al club...{w=0.5}{nw}"
    extend 1nlrss " cual fuera su nombre."
    n 1fsrbo "No {i}tenía{/i} el control,{w=0.1} ¿o sí?{w=0.5}{nw}"
    extend 1ulraj " Ni siquiera de él mismo."
    n 1nnmsr "...Eras tú.{w=0.5}{nw}"
    extend 1nlrsl " Quien lo controlaba."
    n 1nsrbo "..."

    # We assume the player romanced Natsuki, until we get import scripts
    n 1nsraj "Entonces...{w=0.3} cuando él era amable conmigo..."
    n 1klrajl "E-{w=0.1}eso significaba que...{w=0.5}{nw}"

    if Natsuki.isLove():
        n 1klrsml "..."
        n 1kcsssl "Je,{w=0.1} de que rayos hablo.{w=0.5}{nw}"
        extend 1kwmsml " Solo porque hiciste clic en opciones {w=0.1}-{w=0.1} {i}cuando te daban a elegir,{w=0.1} como sea{/i} {w=0.1}-{w=0.1} no los hace el mismo."
        n 1tllssl "En fin,{w=0.1} ¿[player]?"
        n 1ksqsml "No es que me esté quejando.{w=0.5}{nw}"
        extend 1nchsml " Jejeje."

    else:
        extend 1fskeml " ¡-agh!"
        n 1fcsanf "¡Nnnnn-!"
        n 1fllunf "..."
        n 1fnmssl "¡J-{w=0.5}{nw}"
        extend 1fcsbgl "JA!"
        n 1fcsbsl "¡Jajaja!{w=2}{nw}"
        extend 1flleml " ¡¿Qué estoy diciendo?!"
        n 1fcswrl "¡S-{w=0.1}solo porque hiciste clic en algunas palabras y elegiste ciertas opciones no los hace el mismo!"
        n 1fllpol "..."
        n 1nlleml "P-{w=0.1}pero..."

        if Natsuki.isEnamored(higher=True):
            n 1fcsajl "No es que me esté quejando ni nada.{w=0.5}{nw}"
            extend 1nlrssl " Jeje..."

        elif Natsuki.isHappy(higher=True):
            n 1fcsajl "Ya me lo has demostrado.{w=0.5}{nw}"
            extend 1fllunl " C-{w=0.1}creo."

        else:
            n 1fcsajl "S-{w=0.1}supongo que al {i}menos{/i} significa que tienes buen gusto.{w=0.5}{nw}"
            extend 1fllunl " Eso debe de contar."

    if Natsuki.isLove():
        n 1klrss "Sí,{w=0.1} entonces..."

    elif Natsuki.isEnamored(higher=True):
        n 1ksrss "C-{w=0.1}como sea..."

    elif Natsuki.isHappy(higher=True):
        n 1flrun "C-{w=0.1}como sea."

    else:
        n 1flrun "¡C-{w=0.1}como sea!{w=0.5}{nw}"
        extend 1fcsaj " ¡Eso no viene al caso!"

    n 1kslsr "..."
    n 1ullaj "Lo que quiero decir es que aún tengo recuerdos de {i}ese{/i} sujeto..."
    n 1nsrpu "Y aunque obviamente no eras tú,{w=0.5}{nw}"
    extend 1tsraj " ¿tú tambien tienes {i}sus{/i} recuerdos?{w=0.5}{nw}"
    extend 1tslem " Y..."
    n 1fcsaj "...y..."
    n 1fcsan "..."
    n 1fcsem "¡Rrrgh,{w=0.1}{w=0.5}{nw}"
    extend 1fllem " esto es tan confuso!"
    n 1fcsem "Agh...{w=0.5}{nw}"
    extend 1nnmpo " ¿sabes qué?"

    if Natsuki.isAffectionate(higher=True):
        n 1nllss "Ya no importa,{w=0.1} ¿o sí?"

    else:
        n 1fllbo "Solo tengo que empezar de nuevo.{w=0.5}{nw}"
        extend 1unmaj " Mentalmente,{w=0.1} claro."

    n 1ncsaj "Él estuvo aquí {i}antes{/i}."
    n 1fcssm "Pero tú estás aquí {i}ahora{/i}."

    if Natsuki.isAffectionate(higher=True):
        n 1fchbg "Y eso es todo lo que me importa."

        if Natsuki.isLove():
            extend 1fchsm " Sip."
            n 1uchsml "Te amo,{w=0.1} prota genéri-{w=0.3}{nw}"
            n 1fllbgl "Digo,{w=0.5}{nw}"
            extend 1kchbgl " {i}[player]~{/i}."
            n 1fsqsml "..."
            $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
            n 1uchbsl "¡Oh,{w=0.1} tranquilo{w=0.1} [chosen_tease]!"
            n 1fwrtsl "Deberías saber que nunca lo digo en serio.{w=0.5}{nw}"
            extend  " Jeje."

    else:
        n 1fllss "S-{w=0.1}sólo tengo que adaptarme,{w=0.5}{nw}"
        extend 1fllun " es todo."

    return

# Natsuki ponders the fates of the other girls, and her understanding of Monika's actions
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_realizations_other_girls",
            unlocked=True,
            prompt="Monika y las otras chicas",
            conditional=(
                "jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 12 "
                "and get_topic('talk_realizations_player_ddlc_actions').shown_count > 0"
            ),
            category=["DDLC", "Natsuki"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_realizations_other_girls:
    n 1kllun "..."
    n 1klrbo "Emm..."
    n 1knmaj "Eh...{w=0.3} ¿[player]?"
    n 1knmsf "Otra vez...{w=0.3} estuve pensando.{w=0.5}{nw}"
    extend 1kllsf " Sobre el pasado."
    n 1kslss "Supongo que tenía algo de razón cuando dije que Monika estaba actuando raro."
    n 1kskem "¡P-{w=0.1}pero no te equivoques!{w=0.5}{nw}"
    extend 1kllsf " No es que me alegre por eso ni nada.{w=0.5}{nw}"
    extend 1kwmsr " ...En absoluto."
    n 1kcssr "De hecho..."
    n 1klrpu "Desearía haberme equivocado."
    n 1knmaj "Y-"
    n 1kcsunl "..."
    n 1kplun "Yo honestamente creía que el estrés de la escuela y tener que organizar un festival le estaba afectando,{w=0.5}{nw}"
    extend 1kslpu " o algo así."
    n 1tslpu "Pero...{w=0.5}{nw}"
    extend 1kplsr " en retrospectiva..."
    n 1klrun "..."
    n 1kcsaj "...Creo que me libré de ella más {i}fácil{/i}."
    n 1knmsl "Quiero decir...{w=0.3} jugó con todas.{w=0.5}{nw}"
    extend 1klrsf " De una forma u otra."
    n 1klraj "Pero...{w=0.5}{nw}"
    extend 1fcsupl " No sé cuanto {i}daño{/i} le causó a las demás..."
    n 1fcsunl "..."
    n 1kplunl "Sayori era la chica más alegre que jamas hubiera conocido,{w=0.1} [player]."
    n 1kskunl "Y-{w=0.1}y Yuri...{w=0.5}{nw}"
    extend 1kllupl " Yo no..."
    n 1kcsupl "..."
    n 1fcsunl "..."
    n 1kcsaj "...Lo siento."
    n 1kcssr "..."
    n 1kllpu "Yo...{w=2}{nw}"
    extend 1knmsr " nunca nos vimos cara a cara.{w=0.2} Siempre supe que tenía sus inseguridades."
    n 1kslbo "...Igual que yo."
    n 1kcsanl "Pero...{w=0.3} {i}eso{/i}..."
    n 1kcsunl "..."
    n 1kcspu "..."
    n 1fcsanl "Yo...{w=1} no...{w=1} odio a...{w=0.5} Monika."
    n 1fcsun "Yo...{w=0.3} entendio lo que sentía.{w=0.2} Sé {i}como{/i} se sentía."
    n 1fsqsr "Es {i}horrible{/i},{w=0.1} [player]."
    n 1kcsanl "Pero nunca entenderé como fue que llegó a la conclusión de tener que hacer {i}eso{/i}.{w=1}{nw}"
    extend 1kplpu " ¿En realidad...{w=0.3} había otra opción?"
    n 1kllsl "..."
    n 1kcspu "...No lo sé.{w=0.5}{nw}"
    extend " Al menos debo agradecer que me borró..."
    n 1kskun "A-{w=0.5}antes de..."
    n 1kcsun "..."
    n 1kslun "Emm..."
    n 1kcspu "...Perdón.{w=0.2} No quiero seguir hablando de esto,{w=0.1} [player]."
    n 1kllsrl "Pero...{w=0.3} gracias.{w=0.5}{nw}"
    extend 1flrpol " P-{w=0.1}por escuchar,{w=0.1} supongo."

    if Natsuki.isAffectionate(higher=True):
        n 1klrpol "..."
        n 1kcspul "...Y también por rescatarme."

        if Natsuki.isLove():
            n 1kwmsml "Nunca,{w=0.1} jamás olvidaré eso,{w=0.1} [player]."

    else:
        n 1ncspu "..."

    return

# Natsuki muses over the possibility of leaving the space classroom, and the risks involved
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_realizations_space_classroom",
            unlocked=True,
            prompt="Salir de la habitación",
            conditional=(
                "jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 24 "
                "and get_topic('talk_realizations_player_ddlc_actions').shown_count > 0 "
                "and get_topic('talk_realizations_other_girls').shown_count > 0"
            ),
            category=["DDLC", "Natsuki", "TÚ"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_realizations_space_classroom:
    n 1kllsr "Ehmm..."
    n 1klrpu "Bueno,{w=0.1} este cuarto..."
    n 1nsrss "No...{w=0.3} he salido.{w=0.5}{nw}"
    extend 1tnmsl " Desde que me trajiste de vuelta y todo eso."
    n 1fllssl "D-{w=0.1}digo,{w=0.5}{nw}"
    extend 1fcseml " ¡no es que no pueda!"
    extend 1unmbo " Estoy segura de que si puedo."
    n 1kllsf "Es solo que...{w=0.5}{nw}"
    extend 1knmaj " ¡No tengo idea de que pasará!"
    n 1tllaj "¿Y si solo...{w=0.3} me rompo?{w=0.5}{nw}"
    extend 1tnmun " ¿O dejo de existir?"
    extend 1kskem " ¡¿Cómo voy a {i}regresar{/i}?!"
    n 1klrun "..."
    n 1kcspu "Extraño mi cama,{w=0.1} [player].{w=1}{nw}"
    extend 1knmem " ¡Extraño tener sabanas y almohadas!{w=1}{nw}"
    extend 1ksrsr " Y todas mis cosas."
    n 1kcssr "Aunque ya no existan.{w=0.5}{nw}"
    extend 1tslaj " ¿Alguna vez existieron?{w=0.5}{nw}"
    extend 1kcsem " Como sea."
    n 1kllsr "Pero..."
    n 1ksqun "No creo que sea buena idea salir y ver que pasa.{w=0.5}{nw}"
    extend 1flrsl " Aún."
    n 1kcssf "..."
    n 1kcspu "Sólo...{w=0.5}{nw}"
    extend 1fcsaj " dame más tiempo,{w=0.1} ¿sí?{w=0.5}{nw}"
    extend 1fnmbo " Y pensaré en algo más."
    n 1kllpo "No es que quiera quedarme en esta habitación para siempre,{w=0.1} al final yo quiero..."

    return

# Natsuki discusses how she feels about lightning
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_fear_of_lightning",
            unlocked=True,
            prompt="¿Te dan miedo los rayos?",
            category=["Miedos", "Clima"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_fear_of_lightning:
    if Natsuki.isAffectionate(higher=True):
        n 1fllpol "..."
        n 1fllajl "...¿Eh?"
        n 1fcseml "D-{w=0.1}digo,{w=0.5}{nw}"
        extend 1flreml " {i}Obviamento{/i} no,{w=0.5}{nw}"
        extend 1knmpol " ¿pero y qué si así fuera?"

    elif Natsuki.isNormal(higher=True):
        n 1fllwrl "¡N-{w=0.1}no!{w=0.5}{nw}"
        extend 1fcspol " ¿De dónde sacaste eso?"
        n 1kslpol "No le tengo miedo a los rayos..."
        n 1fsrbo "..."
        n 1tsrpu "Y ahora que lo pienso...{w=0.5}{nw}"
        extend 1tnmpo " ¿Por qué {i}preguntas{/i} eso?"

        if get_topic("talk_favourite_season").shown_count > 0:
            n 1tllss "Debo decir,{w=0.1} [player] {w=0.1}-{w=0.3}{nw}"
            extend 1tsqss " tienes una extraña costumbre de preguntarme cosas al azar,{w=0.1} ¿no?"

        else:
            n 1tllss "Es una cosa muy extraña que preguntar,{w=0.1} o eso creo."

        n 1nlraj "Pero,{w=0.1} dejando eso de lado..."

    elif Natsuki.isDistressed(higher=True):
        n 1fllpu "...Si eso fuera {i}cierto{/i},{w=0.5}{nw}"
        extend 1fsqsr " ¿en verdad {i}crees{/i} que te lo voy a {i}decir{/i} ahora?"
        n 1fsqem "Como,{w=0.1} ¿{i}en serio{/i} [player]?{w=0.5}{nw}"
        extend 1fcsem " Dame un descanso."
        n 1fcssr "..."
        n 1fcsem "Además,{w=0.5}{nw}"
        extend 1fllsr " he visto de lo que son capaces cuando estudiaba."
        n 1fsqpu "Tienes que ser idiota para {i}no{/i} preocuparte ni un poco."

        return

    else:
        n 1fcsan "Oh,{w=1.5}{nw}"
        extend 1fcsfu " {i}{cps=\7.5}piérdete{/cps}{/i},{w=0.3} [player]."
        n 1fcsan "Como si quisiera hablar sobre algo tan incomodo {i}contigo{/i}."

        return

    n 1uwdem "¡Los rayos no son un chiste,{w=0.1} [player]!"
    n 1fllun "..."
    n 1knmem "...¿Qué?{w=1}{nw}"
    extend 1fllpo " ¡Hablo en serio!"
    n 1knmun "¿Has {i}visto{/i} la energía que tiene un rayo?"
    n 1nnmaj "¡Tienen como 300 {i}milliones{/i} de voltios!{w=0.5}{nw}"
    extend 1uwdaj " ¡Con unos 30 mil amperios!{w=1.5}{nw}"
    extend 1nllan " ¡Coño!"
    n 1nsqun "...¿Quieres un ejemplo?{w=0.5}{nw}"
    extend 1tsqpu " ¿Qué tal si metes los dedos en el enchufe?"
    n 1nsrss "Tiene unos 110-{w=0.1}220 voltios.{w=1.5}{nw}"
    extend 1nsqun " ...y 15-{w=0.1}30 amperios."
    n 1fspgs "¡Es un {i}montón{/i} de energía!"
    n 1klrpu "¡Y-{w=0.1}y cae del cielo!{w=0.5}{nw}"
    extend 1knmaj " ¡Constantemente!"
    n 1fsqaj "Y con {i}constante{/i} me refiero{w=0.1} a {w=0.1}-{w=0.3}{nw}"
    extend 1nllan " ¡44 rayos por {i}segundo{/i}!"
    n 1fsqun "¡Y eso sin hablar del sonido!{w=0.5}{nw}"
    extend 1kslun " ¡Especialmente si fue cerca!"

    if get_topic("talk_thoughts_on_horror").shown_count > 0:
        n 1fllsr "Mira,{w=0.1} estoy segura de que ya te conté que odio los sustos por la cara."
        n 1fbkwrl "¡¿Cómo crees que me siento si la {i}naturaleza{/i} hace esa mierda?!"

    else:
        n 1fbkwrl "¡Es un truco tan barato!"

    n 1fcsaj "Diablos..."
    n 1fllss "Sí,{w=0.1} c-{w=0.1}como sea."
    n 1unmaj "Te ahorraré una lección sobre la seguridad en las tormentas eléctricas.{w=0.5}{nw}"
    extend 1fsrss " Ya {i}debes{/i} saber todo lo importante."
    n 1ulraj "Pero..."
    n 1fsqsg "Tengo una pregunta,{w=0.1} [player]."

    if preferences.get_volume("sfx") == 0:
        # Player has sound disabled, so we skip the prank
        n 1fsqss "¿{i}Tú{/i} le tienes miedo a los rayos?"
        n 1tsqsm "..."
        n 1fsqbg "¿Qué?"
        n 1usqsg "¿Yo tambien puedo preguntar,{w=0.1} no?{w=0.5}{nw}"
        extend 1nchgn " Jejeje."

    else:
        # We store the current sfx preference so we don't mess up the player's settings with the prank
        $ previous_sfx_setting = preferences.get_volume("sfx")
        $ preferences.set_volume("sfx", 1)

        n 1fsqsm "Jejeje."
        n 1fsqbg "¿{i}Tú{/i} le tienes miedo a los ray-{nw}"

        play audio smack
        with Fade(.1, 0.25, .1, color="#fff")
        $ preferences.set_volume("sfx", previous_sfx_setting)

        n 1uchgn "..."
        n 1kchbg "¡Perdón,{w=0.1} perdón!{w=0.5}{nw}"
        extend 1fchsm " ¡Tenía que hacerlo!{w=0.5}{nw}"
        extend 1kchbg " ¡No {i}pude{/i} evitarlo!"
        n 1nsqsm "Jejeje."
        n 1tsqss "Bueno,{w=0.5}{nw}"
        extend 1fchtsl " ¡no lo llaman tormenta-{w=0.5}{i}atronadora{/i}{w=0.5} por nada!~"

    return

# Natsuki almost falls asleep, jolts awake and then discusses how to combat drowsiness
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_fighting_drowsiness",
            unlocked=True,
            prompt="Somnolencia",
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 12",
            category=["Salud"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_fighting_drowsiness:
    n 1nllpu "...{w=2}{nw}"
    n 1nslpu "...{w=3}{nw}"
    n 1ncsbo "...{w=4}{nw}"
    $ renpy.pause(7)
    n 1fcsbo "..."
    n 1nsqpu "Mmmmm...{w=0.5}{nw}"
    extend 1tsqsr " ¿mmmnn?"
    n 1uskem "¡...!{w=0.5}{nw}"
    n 1ullwrl "¡E-{w=0.1}ehhh!{w=0.5}{nw}"
    extend 1flrss " Jaja..."
    n 1nsrss "N...{w=0.3} No he podido dormir mucho aquí,{w=0.1} como ya sabes."
    n 1kcsun "Uuuuuuh...{w=0.5}{nw}"
    extend 1kslpu " Tengo que despertar..."
    n 1kcssr "..."
    n 1unmbo "¿Sabes qué?{w=0.5}{nw}"
    extend 1ullss " Vuelvo...{w=1}{nw}"
    extend 1nslss " enseguida...{w=1}{nw}"

    play audio chair_out_in
    with Fade(out_time=0.25,hold_time=5,in_time=0.25, color="#000000")

    n 1nchbg "¡Bieeen!{w=0.5}{nw}"
    extend 1fchsm " ¡Volvemos al ataque!"
    n 1nnmaj "Mira,{w=0.1} [player].{w=0.5}{nw}"
    extend 1fchbg " ¡Si hay una cosa que se perfectamente,{w=0.1} es como despejarte!"
    n 1fsqsm "..."
    n 1fsqss "¿Oh?{w=0.5}{nw}"
    extend 1tsqaj " ¿Qué escucho?{w=0.5}{nw}"
    extend 1tllss " ¿Qué como lo hago?"
    n 1fsqsg "Jejeje.{w=0.5}{nw}"
    extend 1usqsg " Parece que estás de {i}suerte{/i},{w=0.1} [player].{w=0.5} Porque..."
    n 1uchgn "¡Es momento del consejo de Natsuki!"
    n 1fnmaj "¡Bien!{w=0.2} Primer paso...{w=0.5}{nw}"
    extend 1fcsbg " La hidratación,{w=0.1} ¡obviamente!"
    n 1ullaj "Es muy fácil olvidar cuánta agua debemos tomar al día...{w=0.5}{nw}"
    extend 1unmbo " ¡y cada {i}cuánto{/i} debemos tomarla!"
    n 1tlrss "¡Debes tomar de 6 a 8 vasos de agua al día,{w=0.3}{nw}"
    extend 1fcsaj " pero no te la tomes toda de golpe!"
    n 1ullaj "No es tan difícil darte un momento para tomar agua {w=0.1}-{w=0.1} solo hay que empezar a hacerlo siempre.{w=0.5}{nw}"
    extend 1fchsm " ¡Es pan comido!"
    n 1fnmaj "Siguiente: ¡el ejercicio!"
    n 1tsqsm "Sí,{w=0.1} sí.{w=0.2} Ya lo sé,{w=0.1} ya lo sé.{w=0.5}{nw}"
    extend 1fslss " Todos {i}amamos{/i} hacer ejercicio,{w=0.1} ¿no?"
    n 1unmaj "No es que te vayas a volver loco ni nada -{w=0.5}{nw}"
    extend 1flrbg " ¡yo no lo estoy!"
    n 1unmbo "{i}Dicen{/i} que una hora de ejercicio al día es lo mejor,{w=0.5}{nw}"
    extend 1fnmca " pero incluso dar una vuelta a tu casa le gana a quedarte tirado,{w=0.1} [player]."
    n 1fcsss "Solo hay que moverse un poco y estirar los músculos,{w=0.1} es todo."
    n 1ulrpu "Por último,{w=0.5}{nw}"
    extend 1fsqsm " y {i}sé{/i} que este te va a gustar,{w=0.1} [player]..."
    n 1fchgn "...¡La comida!"
    n 1fllem "¡Obviamente te sentirás horrible si no comes lo suficiente!"
    n 1kllsr "...Y créeme...{w=0.5}{nw}"
    extend 1ksrpu " Sé lo que digo."
    n 1ksrun "..."
    n 1fcsajl "¡C-{w=0.1}cómo sea!"
    n 1fnmca "¡No esperes que un coche funcione sin gasolina{w=0.1}-{w=0.1} y contigo no es diferente,{w=0.1} [player]."
    n 1ullaj "Tampoco te aloques.{w=0.5}{nw}"
    extend 1nlrpu " Solo agarra una manzana o algo.{w=0.5}{nw}"
    extend 1fsqpo " No llenes tu cuerpo de basura procesada todo el tiempo."
    n 1tsqpo "...O estarás igual de mal."
    n 1fchbg "Pero...{w=0.3} ¡sí!{w=0.5}{nw}"
    extend 1fchsm " ¡Eso es todo!"
    n 1unmbg "Mmmmm,{w=0.1} y-{w=0.5}{nw}"
    n 1nnmss "Y...{w=1}{nw}"
    n 1nsqsr "...{w=2}{nw}"
    n 1fsqaj "[player]."
    n 1fsqpo "¿Estabas escuchando?{w=0.5}{nw}"
    extend 1fnmem " ¡Será {i}mejor{/i} que sí!"
    n 1fllpo "O..."
    n 1fsqss "...O te mandaré a {i}dormir{/i} de verdad.{w=0.5}{nw}"
    extend 1fchgn " Jejeje."

    if Natsuki.isLove():
        n 1uchtsl "¡Te amo,{w=0.1} [player]!~"

    elif Natsuki.isAffectionate(higher=True):
        n 1fchts "¡De nada,{w=0.1} [player]!~"

    return

# Natsuki doesn't hate spiders, contrary to her poem in DDLC
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_fear_of_spiders",
            unlocked=True,
            prompt="¿Le tienes miedo a las arañas?",
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 24",
            category=["Animales", "Miedos"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_fear_of_spiders:
    if Natsuki.isNormal(higher=True):
        n 1tnmbo "¿Eh?{w=0.5} ¿Arañas?"
        n 1tslss "Mmmm...{w=0.5}{nw}"
        extend 1tnmss " ...{w=1}¿no?"
        n 1nchgn "¡Pffff-!"
        n 1fchbg "¿Qué?"
        n 1ullaj "¿Crees que por qué escribí un poema diciendo que son asquerosas,{w=0.5}{nw}"
        extend 1tnmaj " eso es lo que {i}realmente{/i} pienso?"
        $ chosen_tease = random.choice(jn_globals.DEFAULT_PLAYER_TEASE_NAMES)
        n 1fslpo "¡Hasta {w=0.3}{i}dije{/i}{w=0.3} que la araña era una metafóra,{w=0.1} [chosen_tease]!{w=0.5}{nw}"
        extend 1fsqts " ¿Recuerdas?"

    elif Natsuki.isDistressed(higher=True):
        n 1fcsem "..."
        n 1fcssr "No,{w=0.1} [player].{w=0.5}{nw}"
        extend 1fsqsr " No le tengo miedo a las arañas."
        n 1fsqem "...¿Y debería preguntar {i}por qué{/i} te interesa saber mis miedos?"
        n 1fcsan "¿Por qué diablos te daría {i}más{/i} munición para que sigas poniendome de los nervios?"
        n 1fsrem "Agh..."
        n 1fcssf "Sí.{w=0.5}{nw}"
        extend 1fsqpu " Ya hemos terminado,{w=0.1} {i}[player]{/i}."

        return

    else:
        n 1fcsan "...¡¿Tienes miedo de {i}hacer{/i} preguntas estúpidas,{w=0.1} ya que eres la {i}última{/i} persona a la que le respondería?!"
        n 1fsqun "..."
        n 1fslpu "Bueno.{w=2}{nw}"
        extend 1fsqsr " Parece que no,{w=0.1} ¿verdad?"
        n 1fslan "Rayos."

        return

    if get_topic("talk_fear_of_lightning").shown_count > 0:
        n 1tslpu "Y...{w=0.3} ahora que lo pienso..."
        n 1tnmbo "No es la {i}primera{/i} vez que me preguntas si le tengo miedo a alguna cosa."
        n 1tsqsl "...¿Planeas algo o qué?"

    n 1fsqsm "Jejeje.{w=1.5}{nw}"
    extend 1nllss " Meh,{w=0.1} como sea."
    n 1ullaj "¡Ehh,{w=0.5}{nw}"
    extend 1fnmaj " no me malinterpretes!"
    n 1ksrem "No me gustaría tener una de esas cosas...{w=0.3} {i}arrastrándose{/i} sobre mi.{w=0.5}{nw}"
    extend 1fcsfu " ¡Ew!"
    n 1fslun " No quiero ni {i}imaginármelo{/i}."
    n 1unmss "¡Pero las arañas son unas bonitas criaturas!{w=1.5}{nw}"
    extend 1nsrss " ...Casi siempre."
    n 1unmbo "Se encargan de algunos molestos bichos,{w=0.1} como los que muerden o vuelan por todos lados."
    n 1nnmaj "Y algunas -{w=0.5}{nw}"
    extend 1nslss " por más raro que suene -{w=0.5}{nw}"
    extend 1ncspu " son{w=1} muy{w=1.5}{nw}"
    extend 1fspgs " ¡{i}adorables{/i}!"
    n 1uwdaj "¡En serio!{w=1.5}{nw}"
    extend 1uchbg " ¡Las arañas saltarinas son muuuuy lindas!"
    n 1tnmss "Así que...{w=0.3} ¿conclusión?{w=0.5}{nw}"
    extend 1ncssm " ¡Las arañas tienen mi aprovación!"
    n 1nslss "...Sí,{w=0.1} sí,{w=0.1} [player].{w=0.2} Ya sé.{w=0.5}{nw}"
    extend 1flrpo " ¡No soy ingenua!"
    n 1nllun "Sé de lugares donde hay arañas muy peligrosas.{w=0.5}{nw}"
    extend 1uskem " ¡Y {i}desearía{/i} estar bromeando!"
    n 1klrpu "De por si las arañas ya son escurridizas,{w=0.1} entonces imagina vivir con arañas que se esconden en tus zapatos,{w=0.1} o bajo tu escritorio..."
    n 1kskgs "¡Y que te pueden enviar al {i}hospital{/i}!{w=0.5}{nw}"
    extend 1kllan " ¡Diablos!"
    n 1ulrss "Pero...{w=0.5} al menos esas son la minoria,{w=0.1} a menos que vivas en Australia.{w=1.5}{nw}"
    extend 1nslun " Que bueno, ¿no lo crees?"
    n 1ullaj "Bueno,{w=0.1} como sea."

    if Natsuki.isEnamored(higher=True):
        n 1nsqss "Supongo que sigues tú."
        n 1usqsm "¿Le {i}tienes{/i} miedo a las arañas?"
        n 1fsqsm "Mejor piensa bien tu respuesta,{w=0.1} [player]."
        n 1fsldvl "Ya caíste en {i}mi{/i} red,{w=0.1} después de todo..."

        if random.randint(0,10) == 1:
            n 1fchsml "Jujujuju~." # Yes, this is a Muffet reference

        else:
            n 1fsqsm "Jejeje."

        if Natsuki.isLove():
            n 1uchtsl "¡Te amo,{w=0.1} [player]!~"

    else:
        n 1tnmss "Ahí tienes tu respuesta,{w=0.1} [player].{w=0.5}{nw}"
        extend 1fllss " Ahora..."
        n 1fllsm "Espero que no te hayas{w=0.5}{nw}"
        extend 1fsqss " {i}enredado{/i}{w=1}{nw}"
        extend 1usqsm " en mi labia."
        n 1uchgn "Jejeje."

    return

# Player asks about Dan Salvato
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_thoughts_on_dan_salvato",
            unlocked=True,
            prompt="¿Qué piensas de Dan Salvato?",
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 48",
            category=["DDLC", "Natsuki"],
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_thoughts_on_dan_salvato:
    n 1tnmaj "¿Dan...?{w=1}{nw}"
    extend 1nslsl " Dan...{w=0.5} Salvato..."
    n 1fcsaj "¿Por qué...{w=0.3} me suena tan...{w=0.5} familiar?"
    n 1fcsun "..."
    n 1fskaj "¡...!"
    n 1fsgaj "Oh..."
    n 1nllpu "Je.{w=0.3} Sí...{w=1.5}{nw}"
    extend 1fslan " {i}ÉL{/i}."
    n 1fcsbo "..."
    n 1fplaj "Yo...{w=1}{nw}"
    extend 1fcsan " Yo no lo entiendo, [player]."
    n 1nsqbo "Es como,{w=1}{nw}"
    extend 1nslbo " sí,{w=0.5}{nw}"
    extend 1nsqaj " sé quien es."
    n 1ncsbo "Es mi creador.{w=1}{nw}"
    extend 1kcsbo " Nuestro creador."
    n 1fskwr "¡¿Pero tenía {i}idea{/i} de lo que estaba haciendo?!{w=1}{nw}"
    extend 1fchwr " ¡¿Y de lo qué es responsable?!"
    n 1fcsup "..."
    n 1fllup "Solo...{w=1}{nw}"
    extend 1fllfu " mira a...{w=0.5} Monika,{w=0.2} por ejemplo."
    n 1fnmwr "¡Elige a {i}cualquiera{/i}!"
    n 1fcsfu "Lo que decimos,{w=0.3} lo que hacemos -{w=0.5}{nw}"
    extend 1fcufu " lo que {i}pensamos{/i} -{w=0.5}{nw}"
    extend 1fnmfu " todo fue {i}su{/i} idea."
    n 1fsqfu "Él escribió la historia.{w=1}{nw}"
    extend 1fsqaj " Él codificó el juego."
    n 1fskwr "...¡¿Qué debería {i}pensar{/i} de él, [player]?!"
    n 1fchwr "¿Qué {i}sus{/i} manos {b}mataron{/b} a mis amigas?"
    n 1fchwrl "¿Qué {i}sus{/i} manos {b}arruinaron{/b} mi vida?"
    n 1fcuful "Y si no fue directamente,{w=0.3} entonces a través Monika."
    n 1fcsful "..."
    n 1fcsajl "Tal vez él no forzó a las demás a {i}hacer{/i}...{w=1}{nw}"
    extend 1kcsajl " ...lo que hicieron."
    n 1kcsfuf "Pero es seguro que se metió donde no le llamaban..."
    n 1fcsfuf "...forjando un peligroso cuchillo."
    n 1kskfuf "¡Y-{w=0.2}y tú!{w=0.5}{nw}"
    extend 1kskwrf " ¡¿Sabías en lo que te {i}estabas{/i} metiendo?!"
    n "¡¿Qué estabas {i}pensando{/i}?!"
    n 1kcsupf "..."
    n 1kcsajf "No...{w=1} sé que pensar,{w=0.3} [player]."
    n 1kcsunf "..."
    n 1kcsanf "En serio.{w=1}{nw}"
    extend 1kplajf " No lo sé."
    n 1knmbol "No lo conozco,{w=1}{nw}"
    extend 1knmbol " y estoy segura de que nunca lo haré."
    n 1knmbo "...Y probablemente eso sea lo peor."
    n 1kwdwr "¡N-{w=0.2}no me malinterpretes!"
    extend 1kwdup " ¡No quiero tener {i}nada{/i} que ver con él!"
    extend 1fnmbo " Nada,{w=0.3} en serio."
    n 1ncsbo "Pero...{w=1}{nw}"
    extend 1ncsaj " con todas estas preguntas..."
    n 1kcssr "Solo puedo imaginarme cuales serán las respuestas."

return

# Natsuki talks about her opinion and advice proper hygiene.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_maintaining_proper_hygiene",
            unlocked=True,
            prompt="Buena higiene",
            category=["Salud", "TÚ"],
            nat_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_maintaining_proper_hygiene:
    n 1nllsl "..."
    n 1ullaj "Oye,{w=0.1} [player]..."
    n 1nllbo "Me he estado preguntando...{w=0.5}{nw}"
    extend 1tnmpu " ¿Cuidas tu salud?"
    n 1nsqsr "Osea...{w=0.3} ¿Tienes una buena higiene?"
    n 1fnmpo "¡Es super importante,{w=0.1} ¿sabías?!"
    extend 1nslem " ...Y no solo porque {i}es{/i} asqueroso que no lo hagas."
    n 1ulraj "Tampoco es solo estar bien físicamente,"
    extend 1fnmaj " ¡sino que también ayuda a tu salud mental!{w=1}{nw}"
    n 1fllpo "¡Hablo {i}en serio{/i}!"
    n 1klrss "Si estás pasando por un mal momento con ese viejo cerebro tuyo,{w=0.5}{nw}"
    extend 1ksrsr " sentirse sucio física y mentalmente no será de mucha ayuda."
    n 1knmpu "{i}Ambos{/i} conocimos a alguien con el aspecto descuidado,{w=0.1} [player].{w=1.5}{nw}"
    n 1kcssr "...Y también como se sentía realmente."
    n 1kllun "..."
    n 1fcseml "¡C-{w=0.1}cómo sea!{w=1}{nw}"
    extend 1fnmpo " Esto es sobre {i}ti{/i},{w=0.1} [player] -{w=0.5}{nw}"
    extend 1fnmaj " ¡así que pon atención!"
    n 1fcsbg "¡Hoy toca el especial de Natsuki sobre el autocuidado!{w=0.5}{nw}"
    extend 1fcssm " Jejeje."
    n 1fcsaj "Primero,{w=0.1} bañarse {w=0.1}-{w=0.3}{nw}"
    extend 1fnmaj " ¡y que sea {i}regular{/i}!"
    n 1fllsl "Si te saltas baños,{w=0.1} te sentirás asqueroso y desagradable.{w=0.5}{nw}"
    extend 1tnmsr " ¿Y qué provoca eso?"
    n 1nsgbo "Perder la motivación."
    n 1fnmaj "¿Y sabes a qué {i}lleva{/i} eso?"
    n 1fcsem "...¡A no bañarse!{w=0.5}{nw}"
    extend 1knmpo " ¿Entiendes que trato de decir?"
    n 1nllaj "Y...{w=0.5}{nw}"
    extend 1fnmsl " solo toma el tiempo que necesites,{w=0.1} ¿sí?"
    n 1fllss "No {i}necesariamente{/i} tiene que ser como ir al spa,{w=0.1} conque quedes limpio es suficiente."

    if Natsuki.isLove():
        n 1fslss "Además,{w=0.5}{nw}"
        extend 1fsrssl "no me acercaré a ti si apestas."
        n 1fnmpo "¡Así que mejor acostúmbrate,{w=0.1} [player]!"

    if persistent.jn_player_appearance_hair_length == "None":
        n 1fcsaj "¡Siguiente,{w=0.1} tu cabeza!"
        n 1ullpu "Sé que dijiste que no tienes cabello...{w=0.5}{nw}"
        extend 1fsqbg " ¡pero no es excusa para dejar de ponerle atención"
        n 1ulraj "Tienes que asegurarte de que tu piel esté limpia.{w=0.5}{nw}"
        extend 1nsqun "Aunque no tengas cabello,{w=0.1} sudas allá arriba."
        n 1fcsem "¡Asqueroso!"
        n 1ullaj "Pero es tan fácil como bañarse regularmente,{w=0.5}{nw}"
        extend 1nnmbo " como ya dije."

    else:
        n 1fcsaj "¡Siguiente,{w=0.1} tu cabello!"

        if not persistent.jn_player_appearance_hair_length:
            n 1tllss "Asumiendo que {i}tienes{/i},{w=0.1} claro."

        n 1nsqbo "{i}No{/i} estarás agusto con tu apariencia si tu cabello parece trapeador mojado."
        n 1fchbg "Así que mantenlo limpio,{w=0.1} ¡y cepillado!{w=0.5}{nw}"
        extend 1ullss " O lo que sea que hagas con tu cabello {w=0.1}-{w=0.3}{nw}"
        extend 1nnmbo " peine,{w=0.1} gel,{w=0.1} lo que sea."
        n 1tnmpu "¿Recuerdas lo que acabo de decir sobre bañarse,{w=0.1} [player]?"
        n 1fcsbo "Mientras más te pongas,{w=0.1} ¡peor será quitarlo!{w=0.5}{nw}"
        extend 1fnmem " Y si lo dejas mucho tiempo y que parezca un chicle,{w=0.1} ¡tendrías que cortarlo!"
        n 1fsrbg "¡No quiero ver que tu cabello parezca como si te hubiera caído un rayo...{w=0.5}{nw}"
        extend 1fchgn " ...o calvo como la roca!"

        if persistent.jn_player_appearance_hair_length == "Long":
            n 1fspaj "¡Y {i}especialmente{/i} si tienes un cabello tan largo!{w=0.5}{nw}"
            extend 1fllan " ¡Que desperdicio!"

        n 1ulraj "Así que...{w=1}{nw}"
        extend 1fnmbo " cuida tu cabello,{w=0.1} ¿entendido?"
        n 1fcssm "¡Es {i}tan{/i} importante como el resto de ti!"

    if get_topic("talk_natsukis_fang").shown_count > 0:
        n 1fcsaj "¡Y finalmente,{w=0.1} lávate los dientes!"
        n 1ullaj "Te ahorraré la plática esta vez,{w=0.5}{nw}"
        extend 1nnmbo " porque ya hemos hablado de esto."
        n 1nsqpu "...Pero es mejor que no te hayas olvidado del hilo dental,{w=0.1} [player]...{w=1.5}{nw}"
        extend 1fsqsm " ¡Por que yo no!"

    else:
        n 1fcsaj "¡Y finalmente,{w=0.1} tus dientes!{w=0.5}{nw}"
        extend 1fsqpu " Es algo que {i}realmente{/i} no quieres olvidar,{w=0.1} [player]."
        n 1kslan "No sólo tu aliento será {i}tóxico{/i}..."
        n 1fbkwr "¡También se te caerán los dientes!{w=0.5}{nw}"
        extend 1flrun " O quedarán llenos de agujeros...{w=1}{nw}"
        extend 1ksqem " ¡Caros agujeros!{w=1}{nw}"
        extend 1fsran " ¡Diablos!"
        n 1fsqpo "Tienes que ser {i}muy{/i} tonto para preferir tratamientos costosos y dolorosos sobre un esfuerzo de unos minutos."
        n 1flrss "Y además..."
        n 1ksqsm "¿Quién no quisiera una sonrisa {i}resplandeciente{/i} como la mia?"
        n 1uchgn "¡No tendrás {i}una{/i} con caries!"

    n 1kllss "Hablando en serio,{w=0.1} [player].{w=0.5}{nw}"
    extend 1nsqsr " No {i}quiero{/i} que descuides tu salud,{w=0.1} [player]."
    n 1fsqsr "No bromeo.{w=1.5}{nw}"
    extend 1ksrpo " Mereces sentirte y verte bien."

    menu:
        n "¿Entendido?"

        "Sí, merezco sentirme y verme bien.":
            n 1fchbg "¡Eso {i}es{/i} lo que quería escuchar!"
            $ Natsuki.calculated_affinity_gain()

        "...":
            n 1nsqsr "..."
            n 1tsqss "Tú...{w=0.3} no comprendes como va esto,{w=0.1} ¿verdad?"
            n 1fcssm "Ahora, {w=0.1} repite después de mi:{w=0.5}{nw}"
            extend 1fcsbg " 'Merezco sentirme y verme bien'."

            menu:
                "Merezco sentirme y verme bien.":
                    n 1uchbg "¿Ves?{w=0.5}{nw}"
                    extend 1ksqsg " ¿Era {i}taaan{/i} difícil?"
                    n 1fcssm "Jejeje."
                    $ Natsuki.calculated_affinity_gain()

    n 1ullss "En fin,{w=0.1} ¡sip!{w=0.5}{nw}"
    extend 1nnmss " Eso es todo."

    if Natsuki.isLove():
        n 1nsqss "Y recuerda...{w=0.5}{nw}"
        extend 1nsldvl " ¡Te amaré por siempre si mantienes tu salud!~"
        n 1fchsml "Jejeje."
        $ chosen_endearment = random.choice(jn_globals.DEFAULT_PLAYER_ENDEARMENTS)
        extend 1uchbgl "¡Gracias,{w=0.1} [chosen_endearment]!"

    elif Natsuki.isEnamored(higher=True):
        n 1nslbgl "Me gustan {i}mucho{/i} las personas que se preocupan por si mismos."
        n 1fsqpol "Recuerda siempre eso, [player]."

    else:
        n 1fchbg "¡Gracias por escucharme,{w=0.1} [player]!"
        n 1uslsg "...O debería decir..."
        n 1usqbg "¿Gracias por permitirme dejar{w=0.5}{nw}"
        extend 1fsqss " {i}limpio{/i}{w=0.5}{nw}"
        extend 1usqsm " el tema?"
        n 1nchgn "¡Jajajaja!"

    return

# Natsuki gives her thoughts on Monika.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_feelings_about_monika",
            unlocked=True,
            prompt="¿Qué opinas de Monika?",
            category=["DDLC"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_feelings_about_monika:
    n 1fslsr "Monika."
    n 1kcsem "..."
    n 1knmsl "...¿Honestamente?"
    n 1nllsl "No sé...{w=1} {i}cómo{/i} me siento cuando hablo de Monika.{w=1}{nw}"
    extend 1kslpu " Ya no."
    n 1nnmsl "Quiero decir,{w=0.5}{nw}"
    extend 1knmpu " ¿qué puedo {i}decir{/i},{w=0.1} [player]?"
    n 1flrpu "Sí,{w=0.1} fue una entrometida algunas veces.{w=1}{nw}"
    extend 1fsrsf " No me gustaba cuando se ponía toda soberbia y se creía la mejor...{w=1}{nw}"
    extend 1fslem " {i}o{/i} cuando se metía con mis cosas."
    n 1nllpu "Pero...{w=0.5}{nw}"
    extend 1knmpu " Nunca me {i}enojaba{/i} de verdad..."
    n 1fcsfr "Molesta,{w=0.3} irritada,{w=0.3} claro.{w=1}{nw}"
    extend 1fllpu " ¡Cualquiera lo estaría!"
    n 1kplem "¡Pero me preocupaba por ella,{w=0.1} [player]!{w=1.5}{nw}"
    extend 1kllun " {i}Todas{/i} lo hacíamos..."
    n 1kcsun "..."
    n 1fcsun "Ella no era {i}solo{/i} la presidenta del club,{w=0.1} o la más inteligente."
    n 1fnmun "Ella era un modelo a seguir.{w=1.5}{nw}"
    extend 1klrpu " ...Y mi amiga."
    n 1ksrpu "Pero...{w=0.5}{nw}"
    extend 1knmem " es justamente eso lo que hace más difícil entender,{w=0.1} [player]."
    n 1fcssl "Quiero decir...{w=0.5}{nw}"
    extend 1fcsan " Yo...{w=1} sé...{w=1} por lo que estaba pasando.{w=1.5}{nw}"
    extend 1kslun " ¡{i}Yo{/i} estoy lidiando con eso ahora mismo!"
    n 1kwdem "Pero...{w=0.3} ¿Era necesario {i}torturarnos{/i} así?"
    n 1fcsem "Yo...{w=0.3} sé...{w=0.3} que no lo hubiéramos entendido.{w=0.5}{nw}"
    extend 1kslsr " No {i}podíamos{/i} entender."
    n 1fcsan "Especialmente cuando Yuri y yo estabámos peleando..."
    n 1fnmsr "{i}Entiendo eso{/i}."
    n 1klrpu "Pero si estaba tan desesperada...{w=0.5}{nw}"
    extend 1kcspu " ¿Por qué no borrarnos desde el principio?{w=0.5}{nw}"
    extend 1knmem " ¿O literalmente {i}cualquier otra{/i} cosa?"
    n 1fcsfr "..."
    n 1kcspu "No sé,{w=0.1} [player].{w=1.5}{nw}"
    extend 1knmca " En verdad no lo sé."
    n 1ncssr "..."
    n 1nllpu "Supongo que...{w=1}{nw}"
    extend 1tnmpu " ¿tal vez fue el aislamiento?"
    n 1nlrsl "Ella siempre terminaba excluida de todo desde que apareciste...{w=1}{nw}"
    extend 1nsrsr " No creo que {i}tuviera{/i} opción."
    n 1knmsl "...¿Tal vez me hubiera pasado lo mismo?"
    n 1fcseml "¡N-{w=0.1}no me malinterpretes!{w=0.5}{nw}"
    extend 1flrem " Nunca olvidaré lo que hizo...{w=0.5}{nw}"
    extend 1fsrpu " ni perdonaré lo que hizo."
    n 1nlrpu "Pero...{w=1}{nw}"
    extend 1knmsr " ella {i}era{/i} mi amiga."
    n 1kllpu "Así que una parte de mi siempre deseará {i}poder{/i} perdonarla."
    n 1kllbol "...Tal vez por eso quiero entender el por qué actuó así."

    return

# Natsuki gives her thoughts on Yuri.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_feelings_about_yuri",
            unlocked=True,
            prompt="¿Qué piensas de Yuri?",
            category=["DDLC"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_feelings_about_yuri:
    n 1kllpul "...A ver,{w=1} Yuri..."
    n 1kcsun "..."
    n 1ncspu "...No te voy a mentir,{w=0.3} [player].{w=1.5}{nw}"
    extend 1ksqfr " En serio,{w=0.5} {i}en serio{/i} desería no volver a pensar en...{w=1} {i}eso{/i} otra vez."
    n 1kcssl "..."
    n 1ksrpu "Como {i}explico{/i} esto..."
    n 1ncsem "Nuestra relación era...{w=0.3} complicada.{w=1}{nw}"
    extend 1kllss " Incluso {i}antes{/i} de que te unieras al club."
    n 1nnmbo "Nunca estuvimos frente a frente,{w=0.1} [player].{w=1.5}{nw}"
    extend 1nslca " Seguro ya sabias eso."
    n 1kwmpu "Pero nos {i}entendíamos{/i} de cierta manera,{w=0.1} ¿lo pillas?"
    n 1kllpul "Ella estaba...{w=1}{nw}"
    extend 1kcsunl " ahí...{w=1}{nw}"
    extend 1fcsunl " para mí."
    n 1fsrunl "Cuando más necesitaba a alguien.{w=1}{nw}"
    extend 1fnmem " Cuando nadie más entendia...{w=1}{nw}"
    extend 1kslpu " solo podría {i}soñar{/i} con que entendieramos."
    n 1kwmpu "...{w=0.5}¿Sabes cuánto significaba eso para mí?"
    n 1knmsl "Tenía una forma de ver las cosas como nadie más.{w=1}{nw}"
    extend 1fslem " No {i}Monika{/i}.{w=1.5}{nw}"
    extend 1kslsrl " Ni siquiera {i}Sayori{/i}."
    n 1kllpu "Pero..."
    n 1fcssr "De repente ella {i}cambió{/i},{w=0.1} [player].{w=0.5}{nw}"
    extend 1klrsl " Me refiero a cuando apareciste.{w=0.1}"
    n 1knmem "Nunca {i}peleábamos{/i} tan fuerte..."
    n 1tnmsr "¿Y qué si discutiamos?{w=0.5}{nw}"
    extend 1tllss " Bueno...{w=1} ¡Sí!{w=1}{nw}"
    extend 1knmss " ¿Qué amigos no discuten de vez en cuando?"
    n 1klrsm "Y siempre fuímos super diferentes,{w=0.1} también."
    n 1nsrpo "Siempre tenía ese aire de ser correcta.{w=1}{nw}"
    extend 1ncsaj " Refinada...{w=1}{nw}"
    extend 1ncsss " elegante."
    n 1nslss "...{w=0.5}Y yo solo era Natsuki.{w=1}{nw}"
    extend 1ncsss " Ja."
    n 1knmpu "¡Pero nunca había sentido que en verdad {i}no le callera bien{/i}!"
    n 1fcsan "Estábamos tan atrapadas en esa {i}estúpida{/i} rivalidad..."
    n 1fllan "¡Qué todo lo demás nos dejó de interesar!"
    n 1kllpu "Y cuando empezó a ser tan posesiva...{w=1}{nw}"
    extend 1knmsl " ya sabes,{w=0.1} después de que Monika se pusiera a jugar con nosotras."
    n 1kplem "...¿Sabes lo {i}aterrador{/i} que fue para mí?{w=1.5}{nw}"
    extend 1kwdwr " ¿Escuchar esas {i}palabras{/i} saliendo de {i}su{/i} boca?"
    n 1klrem "¿Y sabes lo peor?{w=1.5}{nw}"
    extend 1kcsem " Yo...{w=0.3} le...{w=0.3} seguí el juego.{w=1}{nw}"
    extend 1kplup " ¡No tenía {i}elección{/i},{w=0.1} [player]!"
    n 1fcsup "...Nunca la tuve."
    n 1fcsanl "Incluso cuando te {i}rogé{/i} por ayuda,{w=0.1} yo..."
    n 1kcsanl "Yo-..."
    n 1kcsupl "..."
    n 1fcsunl "..."
    n 1kcseml "...Lo siento,{w=0.1} [player]."
    n 1ksrunl "No creo que sea saludable para mí seguir hablando de esto.{w=1}{nw}"
    extend 1ksqpul " ...Sobre ella."
    n 1fcssrl "Yo solo...{w=1}{nw}"
    n 1kcseml "..."
    n 1fwmsrl "...Extraño a mi amiga.{w=1}{nw}"
    extend 1kllsr " Extraño como solía ser."
    n 1kllaj "Por eso...{w=0.3} ¿recordar lo que pasó?{w=0.5}{nw}"
    extend 1kskem " ¿En lo qué se {i}convirtió{/i}?"
    n 1fcsem "Eso...{w=1} duele,{w=0.1} [player].{w=1.5}{nw}"
    extend 1fcsunl " Y mucho."
    n 1fsqun "...Y siendo honesta."
    n 1ksrpu "...No creo olvidarlo, {i}nunca{/i}."

    return

# Natsuki gives her thoughts on Sayori.
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_feelings_about_sayori",
            unlocked=True,
            prompt="¿Qué piensas de Sayori?",
            category=["DDLC"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_feelings_about_sayori:
    n 1nsrss "Ja.{w=1}{nw}"
    extend 1ksrss " Sayori..."
    n 1kcspu "..."
    n 1fcsunl "Yo...{w=0.5}{nw}"
    extend 1fcsem " sigo enojandome conmigo misma,{w=0.1} sabes."
    n 1klrpu "Es solo que no puedo {i}creer{/i} cómo ignoré sus sentimientos tan fácilmente."
    n 1kplun "...Y cómo olvidé que {i}existia{/i}."
    n 1fcsanl "Si tan solo hubiera {i}sabido{/i} que tan mal estaba su mente...{w=1}{nw}"
    extend 1fcsupl " cuánto estaba {i}sufriendo{/i}..."
    n 1fcsunl "..."
    n 1kcsem "..."
    n 1kslpu "Aún...{w=1.5}{nw}"
    extend 1kplem " sigo sin procesarlo,{w=0.1} ¿sabías?"
    n 1fcsem "Ella siempre era...{w=1} era...{w=0.5}{nw}"
    extend 1ksrpo " era...{w=1} ¡una bola llena de energía alegre!"
    n 1ksrss "¡Literalmente {i}irradiaba{/i} felicidad!"
    n 1ksrun "..."
    n 1kplpul "...¿Puedes siquiera {i}imaginar{/i} lo que se siente?"
    n 1fcsun "Saber que solo llevaba una máscara,{w=1}{nw}"
    extend 1fcsfu " ¿y que era el títere personal de Monika?"
    n 1ksrbol "...Mientras que su propia mente le decia que {i}acabara{/i} con todo."
    n 1kcspu "..."
    n 1ncsss "Je.{w=1}{nw}"
    extend 1nsqss " ¿Sabes qué, [player]?"
    n 1ncspu "No me importa si se comió la mitad de mi galleta de un mordisco."
    n 1nlrpu "No me importa lo malas que eran las canciones que a veces cantaba,{w=1}{nw}"
    extend 1nslssl " o sus...{w=0.3} extraños...{w=0.3} cumplidos."
    n 1tnmsr "A estas alturas."
    n 1ksrsrl "Creo que haría {i}cualquier cosa{/i} solo por ver una sonrisa genuina de Sayori una vez más..."
    n 1kcsssf "...Y darle uno de esos grandes,{w=0.1} tontos abrazos que tanto le gustaban."

    return
