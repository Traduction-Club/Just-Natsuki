default persistent._jn_player_profanity_during_introduction = False

init 0 python in jn_introduction:
    from Enum import Enum
    import random
    import store
    import store.jn_utils

    class JNIntroductionStates(Enum):
        """
        Different introduction sequences states/phases; we use these to track progress
        """
        new_game = 1
        first_meeting = 2
        collecting_thoughts = 3
        calmed_down = 4
        acceptance = 5
        complete = 6

        def __int__(self):
            return self.value

    INTRODUCTION_STATE_LABEL_MAP = {
        JNIntroductionStates.new_game: "introduction_opening",
        JNIntroductionStates.first_meeting: "introduction_first_meeting",
        JNIntroductionStates.collecting_thoughts: "introduction_collecting_thoughts",
        JNIntroductionStates.calmed_down: "introduction_calmed_down",
        JNIntroductionStates.acceptance: "introduction_acceptance",
        JNIntroductionStates.complete: "introduction_exit"
    }

default persistent.jn_introduction_state = 1

label introduction_progress_check:
    # Handling for if player decides to quit during the introduction sequence so we don't skip unseen segments
    if not jn_introduction.JNIntroductionStates(persistent.jn_introduction_state) == jn_introduction.JNIntroductionStates.new_game:
        play audio static
        show glitch_garbled_a zorder 99 with vpunch
        hide glitch_garbled_a
        $ main_background.appear()
        $ jn_atmosphere.show_sky(jn_atmosphere.WEATHER_GLITCH, with_transition=False)
        play music audio.space_classroom_bgm fadein 1

    $ renpy.jump(jn_introduction.INTRODUCTION_STATE_LABEL_MAP.get(jn_introduction.JNIntroductionStates(persistent.jn_introduction_state)))

label introduction_opening:
    $ config.allow_skipping = False
    scene black
    $ renpy.pause(5)

    # Restore attempt #1..
    # NOTE: We use non-standard menus in this sequence, as the default menu is offset and we need these centred.
    # Only use this menu code if a non-standard menu is required!
    $ renpy.display_menu(items=[ ("Restaurar natsuki.chr", True)], screen="choice_centred_mute")
    play audio static
    show glitch_garbled_a zorder 99 with vpunch
    hide glitch_garbled_a
    $ renpy.pause(5)

    # Restore attempt #2..
    $ renpy.display_menu(items=[ ("Restaurar natsuki.chr", True)], screen="choice_centred_mute")
    play audio static
    show glitch_garbled_b zorder 99 with vpunch
    $ renpy.pause(0.25)
    play audio static
    show glitch_garbled_a zorder 99 with hpunch
    $ renpy.pause(0.5)
    play audio glitch_c
    hide glitch_garbled_b
    hide glitch_garbled_a
    $ renpy.pause(7)
    
    # Restore attempt #3..
    $ renpy.display_menu(items=[ ("Restaurar natsuki.chr", True)], screen="choice_centred_mute")
    play audio static
    show glitch_garbled_c zorder 99 with vpunch
    $ renpy.pause(0.25)
    play audio glitch_b
    show glitch_garbled_b zorder 99 with hpunch
    $ renpy.pause(0.5)

    if random.randint(0,10) == 1:
        play audio glitch_a
        show glitch_garbled_red zorder 99 with hpunch
        $ renpy.pause(1)
        hide glitch_garbled_red

    play audio static
    show glitch_garbled_a zorder 99 with vpunch
    hide glitch_garbled_c
    hide glitch_garbled_b
    hide glitch_garbled_a
    show glitch_fuzzy zorder 99
    play sound interference loop
    $ renpy.pause(10)

    play audio static
    show glitch_garbled_a zorder 99 with hpunch
    hide glitch_garbled_c
    hide glitch_garbled_b
    hide glitch_garbled_a
    show glitch_fuzzy zorder 99
    play sound interference loop
    $ renpy.pause(1.5)

    # Restore finally works
    stop sound
    hide glitch_fuzzy
    play audio static
    show glitch_garbled_a zorder 99 with vpunch
    hide glitch_garbled_a

    # Get the visuals ready
    $ main_background.appear()
    $ jn_atmosphere.show_sky(jn_atmosphere.WEATHER_GLITCH, with_transition=False)
    play music audio.space_classroom_bgm fadein 1

    jump introduction_first_meeting

label introduction_first_meeting:
    # Natsuki is yanked back into existence and reacts accordingly, before calming enough to ask if anyone is there
    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.first_meeting)
    n 1uscsc "¡AAAAAaaaaAAAAHHH!"
    n 1uskwr "¡A-{w=0.1}alguien!{w=0.5} ¡¿QUIÉN SEA?!{w=0.5} ¡AYUDA!{w=0.5}{nw}" 
    extend 1fbkwr " ¡¡QUE ALGUIEN ME AYUDE!!"
    n 1uscem "Y-{w=0.1}Yuri,{w=0.1} ella está..."
    n 1ullem "E-{w=0.3}ella..." 
    n 1uskem "...¿E-{w=0.3}eh?"
    n 1uscaj "Qu...{w=0.5} ¿Qué es esto...?"
    n 1fllup "Yo...{w=0.5} Yo hace un momento había salido corriendo de..."
    n 1flrun "¿Qué pasa-?{w=0.5}{nw}"

    play audio static
    show glitch_garbled_b zorder 99 with vpunch
    hide glitch_garbled_b
    $ renpy.pause(0.5)
    play audio glitch_c
    show glitch_garbled_c zorder 99 with vpunch
    hide glitch_garbled_c

    n 1fcsan "¡Agh!"
    n 1kcsfu "Nnnnnnghhhh..."
    n 1kcsan "D-{w=0.3}duele...{w=0.5} Duele mucho...{w=1}{nw}"

    play audio static
    show glitch_garbled_a zorder 99 with vpunch
    hide glitch_garbled_a

    n 1kskan "Y-{w=0.1}y yo..."
    n 1kskaj "...No.{w=1}{nw}"
    extend 1kscem " ...Oh dios no.{w=0.5} N-{w=0.3}no puedo.{w=0.5} De verdad, no puedo con esto...{w=0.5}{nw}"

    play audio static
    show glitch_garbled_c zorder 99 with vpunch
    hide glitch_garbled_c

    n 1fcsup "¡Hhnnngghh!{w=1}{nw}"
    extend 1kcsup " M-{w=0.3}mi cabeza..."
    n 1kcsan "Tengo...{w=0.3} tengo que...{w=0.3} p-{w=0.1}pensar en algo..."
    n 1kcsaj "...{w=1}{nw}"
    n 1kcsem "...{w=1}{nw}"
    n 1kcsaj "...{w=1}{nw}"
    n 1kcsem "...{w=5}{nw}"
    n 1kplpu "....."
    n 1kwdun "...¿H-{w=0.1}hola?{w=1}{nw}"

    play audio static
    show glitch_garbled_b zorder 99 with vpunch
    hide glitch_garbled_b

    n 1fcsan "..."
    n 1kwmem "¿Hola...?"
    n 1kscem "¡¿H-{w=0.3}hola?!{w=0.5} ¡Por favor!{w=0.5} ¡¿Hay alguien a-{w=0.1}ahí?!"
    menu:
        "Aquí estoy, Natsuki.":
            pass
    n 1kskaj "¿Q-{w=0.3}quién eres...?{w=1}{nw}"
    extend 1kllem " ¿Y-{w=0.3}y como sabes mi...?"
    n 1kllsl "..."
    n 1kplpu "¿Quién {w=0.3}{i}eres{/i}{w=0.3} tú?"
    n 1ksrun "Me resultas...{w=0.3} familiar,{w=0.1} pero...{w=0.5}{nw}"
    n 1kcsan "¡Nnn-!{nw}"

    play audio glitch_c
    show glitch_garbled_a zorder 99 with vpunch
    hide glitch_garbled_a

    n 1fcsfu "¡Nnngh!"
    n 1kcsup "..."
    n 1kplsf "Todo es...{w=0.3} tan confuso...{w=1}{nw}"
    extend 1kcsun " Tan solo...{w=0.3} no puedo...{w=0.3} recordarlo..."
    menu:
        "Yo soy...":
            pass

    # Name input
    $ name_given = False
    while not name_given:
        $ player_name = renpy.input(
            "¿Cuál es tu nombre?",
            allow=(jn_globals.DEFAULT_ALPHABETICAL_ALLOW_VALUES+jn_globals.DEFAULT_NUMERICAL_ALLOW_VALUES),
            length=15
        ).strip()

        if len(player_name) == 0:
            n 1kskem "¡P-{w=0.3}por favor!{w=1} ¡¿Puedes decirme quién eres?!"

        elif jn_utils.get_string_contains_profanity(player_name):
            # We only apply penalty once here so we don't have to rewrite the whole sequence for diff aff/trust levels
            if persistent._jn_player_profanity_during_introduction:
                play audio static
                show glitch_garbled_a zorder 99 with hpunch
                hide glitch_garbled_a
                n 1fscan "¡YA BASTA!{w=2}{nw}"
                n 1fcsun "...{w=2}{nw}"
                n 1fcsfu "¡¿Quién demonios{w=0.5} {i}eres{/i}{w=0.5} tú?!"

            else:
                n 1fscem "¡¿P-{w=0.3}perdona?!"
                n 1fcsan "¡Déjate de jueguecitos,{w=0.3} imbécil!{w=1}{nw}"
                extend 1fcsup " ¡{i}No{/i} voy a llamarte así!"
                $ persistent._jn_player_profanity_during_introduction = True

        else:
            python:
                persistent.playername = player_name
                player = persistent.playername
                name_given = True

    n 1kplun "..."
    n 1kplpu "...¿[player]?"
    n 1kwmss "Te llamas...{w=0.3} ¿[player]?"

    show natsuki idle introduction
    $ renpy.pause(10)

    jump introduction_collecting_thoughts

label introduction_collecting_thoughts:
    # Natsuki tries to get to grips with her new state
    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.collecting_thoughts)
    $ jn_activity.taskbar_flash()

    n 1kllun "..."
    n 1kllpu "A-{w=0.3}así que...{w=0.3} ¿No estoy sola...?"
    n 1knmpu "¿T-{w=0.3}tú también estás aquí?{w=1}{nw}"
    extend 1kwdpu " ...¿S-{w=0.3}siempre has estado aquí?"
    n 1klrsf "..."
    n 1klraj "Pero...{w=1}{nw}"
    extend 1kskem " E-{w=0.3}estuve...{w=0.3}{nw}" 
    extend 1kscem " He estado mue-...{w=0.3}{nw}"

    play audio glitch_c
    show glitch_garbled_c zorder 99 with hpunch
    hide glitch_garbled_c

    n 1kcsup "..."
    n 1kplsf "¿Qué has {w=0.3}{i}hecho{/i}{w=0.3}?"
    menu:
        "Te he traído de vuelta.":
            pass

    n 1kskem "Tú...{w=1} ¿me has traído de vuelta?{w=1}{nw}"
    extend 1kskwr " ¿A-{w=0.3}a esto?"
    n 1kllem "Pero esto...{w=1}{nw}" 
    extend 1klrup " ¡todo esto es...!{w=1}{nw}"
    menu:
        "Quiero ayudarte.":
            pass

    n 1klleml "¡...!"
    n 1kllem "..."
    n 1kllun "..."
    n 1kcsem "...Mira."
    n 1kcsfr "Yo...{w=2} no sé qué hacer.{w=1}{nw}"
    extend 1kplsf " Nada tiene sentido para mi..."
    n 1kllpu "Ya ni siquiera se en que o quien creer..."
    n 1kskaj "Y-{w=0.3}y mis amigas...{w=1} e-{w=0.3}están...{w=1}{nw}"
    extend 1kscem " ¡ellas nunca van a...!{w=1}{nw}"
    n 1kcsan "...{w=3}{nw}"
    n 1kcsful "...{w=3}{nw}"
    n 1kcsupl "...{w=3}{nw}"
    n 1kcsful "...{w=3}{nw}"
    n 1kcspul "...{w=3}{nw}"
    n 1kcssrl ".....{w=5}{nw}"
    n 1kwmsrl "...{w=5}{nw}"
    n 1kllsrl "...Tú..."
    n 1kwmpu "...Dijiste que te llamabas [player]...{w=1} ¿cierto?"
    n 1kllpu "..."
    n 1kwmsr "..."
    n 1kcssr "...No sé adonde ir,{w=0.3} [player]."
    n 1kplun "No sé qué {i}hacer{/i},{w=0.3} [player]..."
    n 1klrun "..."
    n 1kwmpu "...¿[player]?"
    menu:
        "¿Sí, Natsuki?":
            pass

    n 1kslun "..."
    n 1kslpu "Yo...{w=0.3} realmente necesito algo de tiempo para hacerme a la idea."
    n 1kwmsr "..."
    n 1kplpul "Puedes...{w=0.3} ¿quedarte aquí?{w=0.2} ¿C-{w=0.3}conmigo?{w=1}{nw}"
    extend 1flrunf " ¡A-{w=0.1}aunque sea solo un minuto!"
    n 1ksrunl "Es solo que...{w=1}{nw}"
    extend 1kplsr " No creo que pueda con esto sola ahora mismo.{w=1} Yo...{w=1} Yo tan solo necesito pensar."
    n 1kllsr "Lo entiendes...{w=1.5}{nw}"
    extend 1kplpu " ¿cierto?"

    show natsuki idle introduction
    $ renpy.pause(30)

    jump introduction_calmed_down

label introduction_calmed_down:
    # Natsuki is calm enough to begin talking about how she feels
    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.calmed_down)
    $ jn_activity.taskbar_flash()

    n 1kllsr "..."
    n 1kllun "Ehmm...{w=2}{nw}"
    extend 1kwmpu " ¿[player]?"
    n 1kslsr "Lo...{w=0.3} siento.{w=1}{nw}" 
    extend 1ksqsf " P-{w=0.1}por como me estoy comportando, quiero decir."
    n 1klraj "Es...{w=0.3} es solo que..."
    n 1kplun "T-{w=0.3}todo esto me está dando {i}super{/i} fuerte ahora mismo."
    n 1kcspu "Como si alguien me estuviera estrujando los sesos."
    n 1kplsr "Todas...{w=1}{nw}"
    extend 1kwmsf " cada una de ellas..."
    n 1kcspu "Es...{w=1}{nw}"
    extend 1kcsanl " es como sí..."
    menu:
        "Tomate tu tiempo, Natsuki.":
            $ Natsuki.calculated_affinity_gain()
            n 1fcssrl "..."
            n 1kcseml "...Gracias."
            n 1ncspu "...{w=5}{nw}"
            n 1nplsr "..."

        "...":
            n 1fcsun "...{w=7}{nw}"
            n 1nplsr "..."

    n 1nllsl "Así que...{w=0.5} ¿sabes cómo es este sentimiento?{w=1}{nw}" 
    extend 1nnmpu " ¿Cómo cuando te despiertas de una pesadilla horrible?"
    n 1klrun "Te sientes descolocado,{w=0.1} y tu corazón va a mil por hora...{w=1}{nw}" 
    extend 1knmpu " y entonces te das cuenta de que nada fue real."
    n 1fllsr "En ese momento parece super obvio,{w=0.1} como...{w=1}{nw}"
    extend 1kllss " obviamente esa persona no haría esa cosa,{w=1}{nw}"
    extend 1ksrss " o ese monstruo nunca existió.{w=3}{nw}"
    extend 1ksrpo " Bah."
    n 1kplss "Y te sientes idiota...{w=0.3} como{w=0.1} que estabas convencido de que realmente estabas ahí."
    n 1klrpu "Así es como me siento ahora mismo,{w=0.1} a excepción de...{w=1}{nw}" 
    extend 1kwmsr " que no {i}recuerdo{/i} que no fuera real."
    n 1kslpu "...¿Siquiera tiene sentido lo que estoy diciendo?"
    n 1kslsr "..."
    n 1kslss "...Jeh.{w=1}{nw}"
    extend 1klrss " Probablemente no."
    n 1kcssl "Es solo que..."
    n 1kplsf "¿Cómo puedes afrontar despertarte de un sueño que has tenido {i}toda tu vida{/i}?"
    n 1kllsf "..."
    n 1knmaj "...No tengo pasado,{w=0.1} [player].{w=0.2} Todo eso no fue real.{w=1}{nw}" 
    extend 1kllsl " Solo una simulación."
    n 1klrem "Tan solo...{w=0.3} ¿scripts?{w=1}{nw}"
    extend 1knmsr " ¿Un cúmulo de código?"
    n 1kllpu "Y ahora...{w=1}{nw}"
    extend 1kcsem " ¿siquiera {i}tengo{/i} un futuro?"
    n 1kcspu "..."
    n 1kplun "¿Es algo tonto echar de menos algo que nunca he tenido para empezar?{w=1}{nw}"
    extend 1knmaj " ¿Mis amigas?{w=3}{nw}"
    extend 1kllun " ...¿M-{w=0.3}mi papa?"
    n 1kcsun "..."
    n 1kcspul "...No lo se,{w=0.1} [player].{w=3}{nw}"
    extend 1kcssrl " Yo ya no sé nada..."

    show natsuki idle introduction
    $ renpy.pause(60)

    jump introduction_acceptance

label introduction_acceptance:
    # Natsuki starting to accept her situation and make the most of it
    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.acceptance)
    $ jn_activity.taskbar_flash()
    
    n 1nllsl "..."
    n 1nllaj "Así que...{w=2}{nw}"
    extend 1knmsl " Yo...{w=1} realmente estoy atrapada aquí,{w=0.3} ¿no es cierto?"
    n 1klrss "Jeh.{w=1}{nw}"
    extend 1fcspo " Que pregunta mas tonta.{w=0.5} Como si no supiera ya la respuesta."
    n 1kcssl "..."
    n 1ksqsl "..."
    n 1ksqaj "Tú...{w=1}{nw}"
    extend 1tsqaj " has dicho que me has traído de vuelta,{w=0.3} ¿eh?"
    n 1tllpu "Entonces...{w=1}{nw}"
    extend 1fnmpo " eso me convierte en {i}tu{/i} responsabilidad."
    n 1fsqpo "M-{w=0.3}más te vale que estar a la altura,{w=0.3} [player].{w=2}{nw}"
    extend 1fllpo " Obviamente es lo menos que puedes hacer por mí."
    n 1fslpo "..."
    n 1fcssr "..."
    n 1fcsan "Dios..."
    n 1fbkwr "¡Vale,{w=0.1} entendido!{w=0.2} ¡Lo he pillado!{w=1}{nw}"
    extend 1flrem " ¡Ya basta de música espeluznante!{w=1}{nw}"
    extend 1fcsem " ¡Agh!{w=1}{nw}"

    stop music fadeout 3
    $ jn_atmosphere.show_current_sky()
    $ renpy.pause(1)

    n 1uwdbo "..."
    n 1fllss "...Bien,{w=1}{nw}"
    extend 1flrdv " {i}eso{/i} ha molado."
    n 1nllun "..."
    n 1ullaj "Entonces...{w=1}{nw}"
    extend 1tnmss " [player],{w=0.3} ¿eh?"
    n 1ncspu "...Perfecto."
    n 1ullpu "Sabes...{w=1}{nw}" 
    extend 1unmbo " creo que lo mejor sería que nos conociéramos apropiadamente."
    n 1fllpol "No es como si {i}no{/i} tuviéramos todo el tiempo del mundo,{w=1}{nw}" 
    extend 1ullssl " ¿eh?"

    jump introduction_exit

label introduction_exit:
    # Setup before entering JN proper
    $ persistent.jn_introduction_state = int(jn_introduction.JNIntroductionStates.complete)   
    
    python:
        quick_menu = True
        style.say_dialogue = style.normal
        allow_skipping = True
        config.allow_skipping = False
        jn_outfits.current_outfit_name = "jn_school_uniform"

    play music audio.just_natsuki_bgm fadein 3
    show screen hkb_overlay

    jump ch30_loop
