#Datetime of when the first screenshot was taken
default persistent.jn_first_screenshot_taken = None

#Amount of good screenshots taken (permission granted)
default persistent.jn_screenshot_good_shots_total = 0

#Amount of bad screenshots taken (no perms granted)
default persistent.jn_screenshot_bad_shots_total = 0

init python in jn_screenshots:
    import os
    import random
    import store

    # Check and create the screenshot directory
    _screenshot_dir = os.path.join(renpy.config.basedir, "screenshots")
    if not os.path.exists(_screenshot_dir):
        os.makedirs(_screenshot_dir)

    # Are screenshots enabled
    __screenshots_enabled = True

    ## Tracking
    # Amount of bad screenshot taken in succession
    bad_screenshot_streak = 0

    #Does the player have permission to take screenshots?
    __has_screenshot_permission = False

    # Prevent the player from taking screenshots completely
    __screenshots_blocked = False

    # Reaction/response permutations so Natsuki feels more dynamic

    # LOVE - ENAMORED
    love_enamored_reactions = [
        "[player]...{w=0.3} todavía te acuerdas de lo que te dije sobre las fotos, ¿cierto?",
        "[player]...{w=0.3} ¿te has olvidado de lo que te dije?",
        "[player]...{w=0.3} creo que te has olvidado de algo.",
        "Oye...{w=0.3} ¿te acuerdas de cuando hablamos de las fotos?",
        "[player],{w=0.1} vamos. Ya hemos hablado de esto..."
    ]

    love_enamored_responses = [
        "En serio, no me gusta ser sorprendida con fotos cuando estoy distraída.",
        "De verdad que odio que me saquen fotos sin permiso.",
        "No me gusta nada que me saquen fotos sin consentimiento, va en serio.",
        "Las fotos sorpresa me hacen sentir incómoda.",
        "Me gustaría saber cuando vas a sacarme una foto."
    ]

    # AFFECTIONATE - NORMAL
    affectionate_normal_reactions = [
        "¡[player]!{w=0.2} ¡¿Qué estás haciendo?!",
        "¡A-ah!{w=0.2} ¡[player]!",
        "¡O-oye!{w=0.2} ¡[player]!",
        "¡¿D-disculpa?!",
        "¡Oye!",
        "¡¿P-pero qué?! ¡[player]!",
        "¡Kyaaahh!{w=0.2} ¡¿Por qué?!"]

    affectionate_normal_responses = [
        "¡No me has dicho que me ibas a sacar una foto!",
        "Creí que te había dicho que preguntaras si querías una foto.",
        "No me gustan las fotos sorpresas,{w=0.1} ¡¿recuerdas?!"
    ]

    # UPSET-
    upset_minus_reactions = [
        "¡¿Podrías parar?!",
        "Vale, ¡vale! ¡Para!",
        "¡Oye! ¡Estate quieto!",
        "¡[player]!{w=0.2} ¡Déjalo ya!",
        "¡[player]!{w=0.2} ¡Para de una vez!",
        "¡[player]!{w=0.2} ¡Deja de hacer eso!",
        "Mira, ¡es suficiente!",
        "Muy bien, ¡ya me he hartado!",
        "¡Agh! ¡Dame un respiro,{w=0.1} [player]!",
        "¡[player]!{w=0.2} ¡¿Puedes parar?!",
        "¡De verdad que me estoy hartando de esto,{w=0.1} [player]!"]

    upset_minus_responses = [
        "Si no te he dado permiso,{w=0.1} ¡significa que no quiero que lo hagas!",
        "¡Te dije que preguntases si es que quieres sacarme una foto!",
        "¡¿Es que no me escuchas?!{w=0.2} ¡Te dije que me preguntes si quieres una foto mía!",
        "¡Recuerdo haber dejado claro que no quiero fotitos sorpresa!"
    ]

    def enable_screenshots():
        """
        Enables screenshots.
        """
        global __screenshots_enabled
        __screenshots_enabled = True

    def disable_screenshots():
        """
        Disables screenshots.
        """
        global __screenshots_enabled
        __screenshots_enabled = False

    def are_screenshots_enabled():
        """
        Returns True if screenshots are enabled.
        """
        return __screenshots_enabled

    def are_screenshots_blocked():
        """
        Returns True if screenshots are blocked.
        """
        return __screenshots_blocked

    def is_allowed_to_take_screenshot():
        """
        Checks if the player is allowed to take a screenshot.

        OUT:
            boolean - True if the player is allowed to take a screenshot, False otherwise.
        """
        return not __screenshots_blocked and __has_screenshot_permission

    def revoke_screenshot_permission(block=False):
        """
        Revokes the player's permission to take a screenshot.

        IN:
            block - If True, the player will also be blocked from taking screenshots.
        """
        global __has_screenshot_permission

        __has_screenshot_permission = False
        if block:
            block_screenshots()

    def grant_screenshot_permission(unblock=False):
        """
        Grants the player permission to take a screenshot.

        IN:
            unblock - If True, the player will also be unblocked from taking screenshots.
        """
        global __has_screenshot_permission

        __has_screenshot_permission = True

        if unblock:
            unblock_screenshots()

    def block_screenshots():
        """
        Blocks the player from taking screenshots.
        """
        global __screenshots_blocked
        __screenshots_blocked = True

    def unblock_screenshots():
        """
        Unblocks the player from taking screenshots.
        """
        global __screenshots_blocked
        __screenshots_blocked = False

    #Register this as the new screenshot hotkey
    for screenshot_key in ("s", "alt_K_s", "alt_shift_K_s", "noshift_K_s"):
        store.jn_register_label_keymap("attempt_screenshot", "screenshot_dialogue", screenshot_key)

# Attempt to produce a screenshot, render associated effects
label take_screenshot:
    if Natsuki.isBroken(higher=True):
        $ renpy.screenshot("{0}/screenshot_{1}.png".format(jn_screenshots._screenshot_dir, datetime.datetime.now().strftime(r"%d-%m-%Y_%H-%M-%S")))
        $ jn_utils.log("Captura de pantalla realizada por el jugador en {0}".format(datetime.datetime.now().strftime(r"%d/%m/%Y, %H:%M")))

    else:
        n 1fsqsr "No, [player].{w=0.1} Eso se queda desactivado."
        return

    hide window
    play audio camera_shutter
    with Fade(.15, 0, .50, color="#fff")
    return

# Handles dialogue and mechanics related to screenshots
label screenshot_dialogue:

    if (
        jn_introduction.JNIntroductionStates(persistent.jn_introduction_state) != jn_introduction.JNIntroductionStates.complete
        or jn_screenshots.are_screenshots_blocked()
    ):
        return

    $ jn_screenshots.disable_screenshots()

    if persistent.jn_first_screenshot_taken is None:
        # Set the date for the first ever screenshot, play the camera effects
        $ persistent.jn_first_screenshot_taken = datetime.datetime.now()
        call take_screenshot

        if Natsuki.isNormal(higher=True):
            n 1uskajl "¿E-eh?{w=0.2} ¿Qué ha sido ese destello que acabo de ver?"
            n 1fskanl "No me digas...{w=0.3} ¡¿Eso ha sido una cámara?!{w=0.2} ¡¿Hay una cámara aquí?!"
            n 1fcssr "..."
            n 1kplpu "[player]...{w=0.3} ¿h-has hecho tú esto...?"
            menu:
                "Si, fue cosa mía.":
                    n 1fcsbgl "¡O-oh!{w=0.2} ¡Aja!{w=0.2} B-bueno,{w=0.1} al menos lo admites."

                "No, yo no fui.":
                    n 1tnmpu "¿Eh?{w=0.2} Pero entonces...{w=0.3} ¿quién...?"
                    n 1tllpu "..."

                "No estoy seguro.":
                    n 1tllpu "Eso es...{w=0.3} un poco preocupante..."
                    n 1tnmpu "..."

            n 1nnmpu "Bueno...{w=0.3} como sea.{w=0.1} La verdad es que{w=0.1} nunca he estado muy cómoda con que me saquen fotos sin mi permiso."
            n 1klrbol "A mi...{w=0.3} no me gusta nada{w=0.1} nada eso."
            n 1klraj "Así que, a partir de ahora,{w=0.1} ¿por favor podrías preguntarme la próxima vez que me quieras sacar una foto?"
            n 1klrbo "Te lo agradecería,{w=0.1} [player]."

        elif Natsuki.isDistressed(higher=True):
            n 1fskpu "..."
            n 1fsqpu "You're taking pictures of me,{w=0.1} aren't you?"
            menu:
                "Sí.":
                    n 1fsqaj "Claro...{w=0.3} no.{w=0.1} No voy a permitir eso."
                    n 1fsqsl "Voy a desactivarlo."

                "No.":
                    n 1fcsan "..."
                    n 1fsqpu "No hay nadie aquí aparte de nosotros dos,{w=0.1} [player]."
                    n 1fsqan "...{w=0.3}¿Así que por que tienes que mentirme?"
                    n 1fcssr "Da igual.{w=0.1} No importa.{w=0.1} Voy a desactivar eso."

            $ jn_screenshots.unblock_screenshots()
            $ Natsuki.percentage_affinity_loss(1.5)

        else:
            n 1fscem "..."
            n 1fscanl "¿U-{w=0.1}una camara...?"
            n 1kcsfrl "...No.{w=0.2} N-{w=0.1}no puedo.{w=0.2} No."
            n 1fcsunl "Me importa un carajo.{w=0.2} Se queda apagada."
            $ jn_screenshots.unblock_screenshots()
            $ Natsuki.percentage_affinity_loss(1)

    # Positive screenshot route, as we have Natsuki's permission
    elif jn_screenshots.is_allowed_to_take_screenshot():
        $ persistent.jn_screenshot_good_shots_total += 1
        n 1unmaj "¿Eh?{w=0.2} ¿Quieres sacarme una foto ahora mismo?"

        if Natsuki.isEnamored(higher=True):
            n 1uchbg "¡Jajaja!{w=0.2} ¡Claro!"

        elif Natsuki.isHappy(higher=True):
            n 1kllpu "Bueno...{w=0.2} Está bien."

        else:
            n 1nlrsl "...Bueno.{w=0.1} Pero hazlo rápido."

        call take_screenshot

        # Retract the permission Natsuki gave, as the picture has been taken
        if Natsuki.isEnamored(higher=True):
            n 1uchsml "¡Valeee!{w=0.2} Pregúntame otra vez si es que quieres otra foto,{w=0.1} ¿de acuerdo?"

        else:
            n 1knmbo "¿Ya está?{w=0.2} Asegúrate de preguntarme si quieres sacarme otra foto."

        $ jn_screenshots.revoke_screenshot_permission()

    # Too many bad screenshots in a row; Natsuki is upset
    elif jn_screenshots.bad_screenshot_streak >= 3:

        show natsuki 1fsqsr

        # Add pending apology
        $ jn_apologies.add_new_pending_apology(store.jn_apologies.TYPE_SCREENSHOT)

        # Update tracking and block further screenshots
        $ persistent.jn_screenshot_bad_shots_total += 1
        $ jn_screenshots.revoke_screenshot_permission(block=True)

        call take_screenshot
        n 1fcswr "Mira,{w=0.1} ¡creo que ya estoy cansada de esto!{w=0.2} Simplemente voy a desactivarlo por ahora."
        return

    elif not jn_screenshots.is_allowed_to_take_screenshot():
        # Update tracking and take shot
        $ persistent.jn_screenshot_bad_shots_total += 1
        $ jn_screenshots.bad_screenshot_streak += 1

        call take_screenshot
        $ jn_utils.log("Estado de afecto actual: {0}".format(Natsuki._getAffinityState()))

        show natsuki 1fsqsr zorder 3

        # Add pending apology
        $ jn_apologies.add_new_pending_apology(store.jn_apologies.TYPE_SCREENSHOT)

        if Natsuki.isEnamored(higher=True):

            # Pick the reaction and response; Natsuki is surprised but not angry
            $ chosen_reaction = renpy.substitute(renpy.random.choice(jn_screenshots.love_enamored_reactions))
            $ chosen_response = renpy.substitute(renpy.random.choice(jn_screenshots.love_enamored_responses))

            n 1kwmpu "[chosen_reaction]"
            n 1kllpu "[chosen_response]"
            n 1knmbo "Así que...{w=0.3} podrás recordarlo para la próxima vez,{w=0.1} ¿cierto?"
            n 1klrbg "Que no muerdo...{w=0.3} Jajaja..."
            n 1klrsl "Ahora,{w=0.2} ¿en qué estábamos?"
            $ Natsuki.percentage_affinity_loss(2.5)

        elif Natsuki.isNormal(higher=True):
            # Pick the reaction and response; Natsuki is irritated
            $ chosen_reaction = renpy.substitute(renpy.random.choice(jn_screenshots.affectionate_normal_reactions))
            $ chosen_response = renpy.substitute(renpy.random.choice(jn_screenshots.affectionate_normal_responses))

            n 1fbkwrl "[chosen_reaction]"
            n 1fnmeml "[chosen_response]"
            n 1fllem "Hmph...{w=0.3} ¿podrías al menos avisarme antes la próxima vez?"
            n 1fllsl "Gracias..."
            n 1fnmsl "Ahora,{w=0.2} ¿en qué estábamos?"
            $ Natsuki.percentage_affinity_loss(2)

        elif Natsuki.isDistressed(higher=True):

            # Pick the reaction and response; Natsuki is clearly upset
            $ chosen_reaction = renpy.substitute(renpy.random.choice(jn_screenshots.upset_minus_reactions))
            $ chosen_response = renpy.substitute(renpy.random.choice(jn_screenshots.upset_minus_responses))

            n 1fcsan "[chosen_reaction]"
            n 1fnmfu "[chosen_response]"
            n 1fsqan "No vuelvas a hacer eso."
            n 1fcssr "Ahora,{w=0.2} ¿en qué estábamos?"
            $ Natsuki.percentage_affinity_loss(1.5)

        else:
            # Natsuki isn't putting up with this
            n 1fcsan "¿Sabes qué,{w=0.1} [player]?{w=0.2} No.{w=0.1} No voy a dejarte hacer eso más."
            n 1fcssr "Voy a desactivarlo.{w=0.1} {i}Tampoco es que me vayas a escuchar aunque me queje.{/i}"
            $ Natsuki.percentage_affinity_loss(1)
            $ jn_screenshots.revoke_screenshot_permission(block=True)

    #Enable screenshots again
    $ jn_screenshots.enable_screenshots()
    return

# Ask Natsuki for permission to take a picture of her, or have her call out the player if permission already given!
init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_get_picture_permission",
            unlocked=True,
            prompt="¿Puedo sacarte una foto?",
            conditional="persistent.jn_first_screenshot_taken is not None",
            category=["TÚ", "Fotografía"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_get_picture_permission:
    # The player was warned!
    if jn_screenshots.are_screenshots_blocked():
        n 1fsqpu "Eh...{w=0.3} No,{w=0.1} no voy a volver a encender la cámara,{w=0.1} [player]."
        return

    if Natsuki.isEnamored(higher=True):
        if jn_screenshots.is_allowed_to_take_screenshot():
            n 1uchgn "¡Jajaja!{w=0.2} Ya te dije que podías,{w=0.1} ¡idiota!"
            n 1unmbg "Estoy lista,{w=0.1} ¡cuando quieras!"

        else:
            n 1unmbg "¿Eh?{w=0.2} ¿Una foto?{w=0.2} ¡Por supuesto!"
            $ jn_screenshots.grant_screenshot_permission()

    elif Natsuki.isAffectionate(higher=True):
        if jn_screenshots.is_allowed_to_take_screenshot():
            n 1tnmpu "¿Eh?{w=0.2} ¿No me habías preguntado eso ya?"
            n 1fllpol "Está bien,{w=0.1} ¡así que dale!"

        else:
            n 1nllss "¿Oh?{w=0.2} ¿Quieres hacerme una foto?{w=0.2} ¡Está bien!"
            $ jn_screenshots.grant_screenshot_permission()

    elif Natsuki.isHappy(higher=True):
        if jn_screenshots.is_allowed_to_take_screenshot():
            n 1nllss "¿Hmm?{w=0.2} ¿Una foto?{w=0.2} Bueno,{w=0.1} vale."
            $ jn_screenshots.grant_screenshot_permission()

        else:
            n 1fcspol "Uuuuh...{w=0.3} Ya te dije que puedes,{w=0.1} [player]."
            n 1knmpo "Simplemente hazlo rápido,{w=0.1} ¿entendido?"

    elif Natsuki.isUpset(higher=True):
        if jn_screenshots.is_allowed_to_take_screenshot():
            n 1fnmpu "{i}Ya{/i} te dije que puedes,{w=0.1} [player]."

        else:
            # Indecisive; this lets lower affinity players have a chance at screenshots without upsetting Natsuki
            n 1fnmpu "¿Quieres una foto?"
            n 1fcspu "...{w=0.3}déjame pensármelo."
            n 1fcsbo "..."
            # We take into account the player's behaviour with pictures so far
            $ natsuki_approves = random.randint(1, 100) <= (100 - (jn_screenshots.bad_screenshot_streak * 25))
            if natsuki_approves:
                n 1fllbo "Está bien,{w=0.1} supongo.{w=0.1} Que sea rápido."
                $ jn_screenshots.grant_screenshot_permission()

            else:
                n 1fcsbo "Lo siento.{w=0.2} No quiero que me saquen fotos ahora mismo."
                $ jn_screenshots.revoke_screenshot_permission()

    elif Natsuki.isDistressed(higher=True):
        n 1fsqfr "No.{w=0.1} {b}No{/b} quiero que me saquen fotos ahora mismo."
        $ jn_screenshots.revoke_screenshot_permission()

    else:
        n 1fsqan "..."
        $ jn_screenshots.revoke_screenshot_permission()
    return
