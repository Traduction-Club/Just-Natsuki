label ch30_autoload:
    #Start with black scene
    scene black

    python:
        quick_menu = True
        style.say_dialogue = style.normal
        in_sayori_kill = None
        allow_skipping = True
        config.allow_skipping = False

    #Do all the things here for initial setup/flow hijacking

    #FALL THROUGH

label ch30_holiday_check:
    python:
        import datetime
        import store.jn_utils as jn_utils

        jn_utils.log("Holiday check: {0}".format(jn_get_holiday_for_date(datetime.datetime.now().date())))
    #Run holiday checks and push/setup holiday related things here

    #FALL THROUGH

label ch30_init:
    python:
        import random

        # Check the daily affinity cap and reset if need be
        Natsuki.check_reset_daily_affinity_gain()

        # Outfit selection
        if persistent.jn_natsuki_auto_outfit_change_enabled:
            jn_outfits.set_outfit_for_time_block()

        # Determine if the player should get a prolonged leave greeting
        if (datetime.datetime.now() - persistent.jn_last_visited_date).total_seconds() / 604800 >= 1:
            persistent.last_apology_type = jn_apologies.TYPE_PROLONGED_LEAVE

        elif not persistent.last_apology_type == jn_apologies.TYPE_SUDDEN_LEAVE:
            Natsuki.calculated_affinity_gain()

        # Add to the total visits counter and set the last visit date
        persistent.jn_total_visit_count += 1
        persistent.jn_last_visited_date = datetime.datetime.now()

        # Pick a greeting or random event
        if not jn_topic_in_event_list_pattern("^greeting_"):
            if (
                random.randint(0, 10) == 1
                and (not persistent.jn_player_admission_type_on_quit and not persistent.jn_player_apology_type_on_quit)
                and jn_events.select_event()
            ):
                push(jn_events.select_event())
                renpy.call("call_next_topic", False)

            else:
                push(greetings.select_greeting())
                persistent.jn_player_admission_type_on_quit = None
                persistent.jn_player_apology_type_on_quit = None

    #FALL THROUGH

label ch30_visual_setup:
    python:
        # Draw background
        main_background.draw(full_redraw=True)

        if persistent.jn_random_weather and 6 < store.jn_get_current_hour() <= 18:
            jn_atmosphere.show_random_sky()

        elif (
            store.jn_get_current_hour() > 6 and store.jn_get_current_hour() <= 18
            and not jn_atmosphere.is_current_weather_sunny()
        ):
            jn_atmosphere.show_sky(jn_atmosphere.WEATHER_SUNNY)

    show screen hkb_overlay
    play music audio.just_natsuki_bgm

    #FALL THROUGH

#The main loop
label ch30_loop:
    show natsuki idle at jn_center zorder JN_NATSUKI_ZORDER

    # TODO: topic selection here once wait system is implemented
    #Run our checks
    python:
        _now = datetime.datetime.now()

        if LAST_MINUTE_CHECK.minute is not _now.minute:
            minute_check()
            LAST_MINUTE_CHECK = _now

            if LAST_MINUTE_CHECK.minute in (0, 15, 30, 45):
                quarter_hour_check()

            if LAST_MINUTE_CHECK.minute in (0, 30):
                half_hour_check()

        if LAST_HOUR_CHECK is not _now.hour:
            hour_check()
            LAST_HOUR_CHECK = _now.hour

        if LAST_DAY_CHECK is not _now.day:
            day_check()
            LAST_DAY_CHECK = _now.day

        jn_globals.player_is_in_conversation = False

    #Now, as long as there's something in the queue, we should go for it
    while persistent._event_list:
        call call_next_topic

    #FALL THROUGH

label ch30_wait:
    window hide
    $ renpy.pause(delay=5.0, hard=True)
    jump ch30_loop

#Other labels
label call_next_topic(show_natsuki=True):
    if show_natsuki:
        show natsuki at jn_center

    if persistent._event_list:
        $ _topic = persistent._event_list.pop(0)

        if renpy.has_label(_topic):
            # Notify if the window isn't currently active
            if (persistent.jn_notify_conversations
                and jn_utils.get_current_session_length().total_seconds() > 60
                and not jn_activity.get_jn_window_active()):
                    play audio notification
                    $ jn_activity.taskbar_flash()

            # Call the pending topic, and disable the UI
            $ jn_globals.player_is_in_conversation = True
            call expression _topic

    python:
        #Collect our return keys here
        #NOTE: This is instance checked for safety
        return_keys = _return if isinstance(_return, dict) else dict()

        topic_obj = get_topic(_topic)

        #Handle all things which act on topic objects here, since we can't access attributes of Nonetypes
        if topic_obj is not None:
            #Increment shown count, update last seen
            topic_obj.shown_count += 1
            topic_obj.last_seen = datetime.datetime.now()

            #Now manage return keys
            if "derandom" in return_keys:
                topic_obj.random = False

    #This topic might quit
    if "quit" in return_keys:
        jump quit

    # Reenable the UI and hop back to the loop
    python:
        global LAST_TOPIC_CALL
        LAST_TOPIC_CALL = datetime.datetime.now()
        jn_globals.player_is_in_conversation = False

    jump ch30_loop

init python:
    LAST_TOPIC_CALL = datetime.datetime.now()
    LAST_MINUTE_CHECK = datetime.datetime.now()
    LAST_HOUR_CHECK = LAST_MINUTE_CHECK.hour
    LAST_DAY_CHECK = LAST_MINUTE_CHECK.day

    _NAT_SAYS = 0
    _PLAYER_SAYS = 1

    _SAYS_RANGE = [
        _NAT_SAYS,
        _PLAYER_SAYS
    ]

    def minute_check():
        """
        Runs every minute during breaks between topics
        """
        jn_utils.save_game()

        # Check the daily affinity cap and reset if need be
        Natsuki.check_reset_daily_affinity_gain()

        # Run through all externally-registered minute check actions
        if len(jn_plugins.minute_check_calls) > 0:
            for action in jn_plugins.minute_check_calls:
                eval(action.statement)

        # Check what the player is currently doing
        jn_activity.get_current_activity()

        # Push a new topic every couple of minutes
        # TODO: Move to a wait/has-waited system to allow some more flexibility
        if (
            persistent.jn_natsuki_random_topic_frequency is not jn_preferences.random_topic_frequency.NEVER
            and datetime.datetime.now() > LAST_TOPIC_CALL + datetime.timedelta(minutes=jn_preferences.random_topic_frequency.get_random_topic_cooldown())
            and not persistent._event_list
        ):

            if not persistent.jn_natsuki_repeat_topics:
                topic_pool = Topic.filter_topics(
                    topics.TOPIC_MAP.values(),
                    unlocked=True,
                    nat_says=True,
                    location=main_background.location.id,
                    affinity=Natsuki._getAffinityState(),
                    is_seen=False
                )

            else:
                topic_pool = Topic.filter_topics(
                    topics.TOPIC_MAP.values(),
                    unlocked=True,
                    nat_says=True,
                    location=main_background.location.id,
                    affinity=Natsuki._getAffinityState()
                )

            if topic_pool:
                if (not persistent.jn_natsuki_repeat_topics):
                    # More random topics available, reset out of topics warning
                    store.persistent._jn_out_of_topics_warning_given = False

                queue(random.choice(topic_pool).label)

            elif not store.persistent.jn_natsuki_repeat_topics and not store.persistent._jn_out_of_topics_warning_given:
                # Out of random topics
                queue("talk_out_of_topics")

        pass

    def quarter_hour_check():
        """
        Runs every fifteen minutes during breaks between topics
        """

        # Run through all externally-registered quarter-hour check actions
        if len(jn_plugins.quarter_hour_check_calls) > 0:
            for action in jn_plugins.quarter_hour_check_calls:
                eval(action.statement)

        jn_random_music.random_music_change_check()

        pass

    def half_hour_check():
        """
        Runs every thirty minutes during breaks between topics
        """

        # Run through all externally-registered half-hour check actions
        if len(jn_plugins.half_hour_check_calls) > 0:
            for action in jn_plugins.half_hour_check_calls:
                eval(action.statement)

        pass

    def hour_check():
        """
        Runs ever hour during breaks between topics
        """

        # Run through all externally-registered hour check actions
        if len(jn_plugins.hour_check_calls) > 0:
            for action in jn_plugins.hour_check_calls:
                eval(action.statement)

        # Draw background
        main_background.check_redraw()
        jn_atmosphere.show_current_sky()

        # Update outfit
        if jn_outfits.get_outfit_for_time_block().reference_name is not jn_outfits.current_outfit_name:

            # We call here so we don't skip day_check, as call returns us to this point
            renpy.call("outfits_time_of_day_change")

        pass

    def day_check():
        """
        Runs every day during breaks between topics
        """

        # Run through all externally-registered day check actions
        if len(jn_plugins.day_check_calls) > 0:
            for action in jn_plugins.day_check_calls:
                eval(action.statement)

        pass

label talk_menu:
    python:
        # Get the flavor text for the talk menu, based on affinity state
        if Natsuki.isEnamored(higher=True):
            _talk_flavor_text = random.choice(store.jn_globals.DEFAULT_TALK_FLAVOR_TEXT_LOVE_ENAMORED)

        elif Natsuki.isNormal(higher=True):
            _talk_flavor_text = random.choice(store.jn_globals.DEFAULT_TALK_FLAVOR_TEXT_AFFECTIONATE_NORMAL)

        elif Natsuki.isDistressed(higher=True):
            _talk_flavor_text = random.choice(store.jn_globals.DEFAULT_TALK_FLAVOR_TEXT_UPSET_DISTRESSED)

        else:
            _talk_flavor_text = random.choice(store.jn_globals.DEFAULT_TALK_FLAVOR_TEXT_BROKEN_RUINED)

        # Ensure any variable references are substituted
        _talk_flavor_text = renpy.substitute(_talk_flavor_text)

    $ show_natsuki_talk_menu()

    menu:
        n "[_talk_flavor_text]"

        "Hablemos sobre...":
            call player_select_topic

        "Háblame otra vez de...":
            call player_select_topic(is_repeat_topics=True)

        "¡Te amo, [n_name]!" if Natsuki.isLove() and persistent.jn_player_love_you_count > 0:
            $ push("talk_i_love_you")
            jump call_next_topic

        "Me siento..." if Natsuki.isHappy(higher=True):
            jump player_admissions_start

        "Quiero decirte algo..." if Natsuki.isHappy(higher=True):
            jump player_compliments_start

        "Quiero disculparme...":
            jump player_apologies_start

        "Adiós..." if Natsuki.isAffectionate(higher=True):
            jump farewell_menu

        "Adiós" if Natsuki.isHappy(lower=True):
            jump farewell_start

        "No importa":
            jump ch30_loop

    return

label player_select_topic(is_repeat_topics=False):
    python:
        if (is_repeat_topics):
            _topics = Topic.filter_topics(
                topics.TOPIC_MAP.values(),
                nat_says=True,
                unlocked=True,
                location=main_background.location.id,
                affinity=Natsuki._getAffinityState(),
                is_seen=True
            )

        else:
            _topics = Topic.filter_topics(
                topics.TOPIC_MAP.values(),
                player_says=True,
                unlocked=True,
                location=main_background.location.id,
                affinity=Natsuki._getAffinityState()
            )

        # Sort the topics we can pick by prompt for a cleaner appearance
        _topics.sort(key=lambda topic: topic.prompt)

        # Present the topic options grouped by category to the player
        menu_items = menu_dict(_topics)

    call screen categorized_menu(menu_items,(1020, 70, 250, 572), (740, 70, 250, 572), len(_topics))

    $ _choice = _return

    # We got a string, we should push
    if isinstance(_choice, basestring):
        $ push(_choice)
        jump call_next_topic

    # -1 means go back
    elif _choice == -1:
        jump talk_menu

    # Clear _return
    $ _return = None

    jump ch30_loop

label farewell_menu:
    python:
        # Sort the farewell options by their display name
        avaliable_farewell_options = jn_farewells.get_farewell_options()
        avaliable_farewell_options.sort(key = lambda option: option[0])
        avaliable_farewell_options.append(("Adiós.", "farewell_start"))

    call screen scrollable_choice_menu(avaliable_farewell_options, ("No importa.", None))

    if isinstance(_return, basestring):
        show natsuki at jn_center
        $ push(_return)
        jump call_next_topic

    jump ch30_loop

label extras_menu:
    python:
        avaliable_extras_options = []

        # Since conditions can change, we check each time if each option is now avaliable due to context changes (E.G affinity is now higher)
        for extras_option in jn_plugins.extras_options:
            if eval(extras_option.visible_if):
                avaliable_extras_options.append((extras_option.option_name, extras_option.jump_label))

        # Sort the extras options by their display name
        avaliable_extras_options.sort(key = lambda option: option[0])

    call screen scrollable_choice_menu(avaliable_extras_options, ("No importa.", None))

    if isinstance(_return, basestring):
        $ renpy.jump(_return)

    jump ch30_loop

label try_force_quit:
    # Decision making that overrides the default Ren'Py quit behaviour
    if (
        jn_introduction.JNIntroductionStates(persistent.jn_introduction_state) == jn_introduction.JNIntroductionStates.complete
        and jn_farewells.JNForceQuitStates(persistent.jn_player_force_quit_state) == jn_farewells.JNForceQuitStates.not_force_quit
    ):
        # Player hasn't force quit before, special dialogue
        $ push("farewell_force_quit")
        $ renpy.jump("call_next_topic")

    elif not jn_introduction.JNIntroductionStates(persistent.jn_introduction_state) == jn_introduction.JNIntroductionStates.complete:
        # Player hasn't passed the intro sequence, just quit
        $ renpy.jump("quit")

    else:
        # Standard quit behaviour
        if Natsuki.isAffectionate(higher=True):
            n 1kplpo "E-{w=0.1}espera,{w=0.1} ¿qué?{w=0.2} ¿No vas a despedirte primero{w=0.1} [player]?"

        elif Natsuki.isNormal(higher=True):
            n 1kskem "¡O-{w=0.1}oye!{w=0.2} No te irás así,{w=0.1} ¿verdad?"

        elif Natsuki.isDistressed(higher=True):
            n 1fsqpu "...¿En serio?{w=0.2} ¿Ahora ni siquiera me dices 'adiós'?"

        else:
            n 1fsqsf "...Oh.{w=0.2} Te vas."

        menu:
            # Back out of quitting
            "No importa.":
                if Natsuki.isAffectionate(higher=True):
                    n 1kllssl "G-{w=0.1}gracias,{w=0.1} [player].{w=1}{nw}"
                    n 1tllss "Ahora,{w=0.1} ¿dónde estaba...?{w=1}{nw}"
                    extend 1unmbo " Oh,{w=0.1} cierto.{w=1}{nw}"

                elif Natsuki.isNormal(higher=True):
                    n 1flleml "¡B-{w=0.1}bien!{w=1}{nw}"
                    extend 1kllpol " Bien...{w=1}{nw}"
                    n 1tslpu "Ahora...{w=0.3} ¿qué estaba diciendo?{w=0.5}{nw}"
                    extend 1nnmbo " Oh,{w=0.1} cierto.{w=1}{nw}"

                elif Natsuki.isDistressed(higher=True):
                    n 1fsqfr "...gracias.{w=1}{nw}"
                    n 1fslpu "Como estaba {i}diciendo{/i}...{w=1}{nw}"

                else:
                    n 1fcsfr "Lo que sea.{w=1}{nw}"
                    n 1fsqsl "{cps=\7.5}Como iba diciendo.{/cps}{w=1}{nw}"

                return

            # Continue force quit
            "...":
                hide screen hkb_overlay
                if Natsuki.isAffectionate(higher=True):
                    n 1kwmem "Vamos,{w=0.2} [player]...{w=1}{nw}"
                    play audio glitch_c
                    stop music
                    n 1kcsup "¡...!{nw}"

                elif Natsuki.isNormal(higher=True):
                    n 1fwmun "...¿En serio,{w=0.2} [player]?{w=1}{nw}"
                    play audio glitch_c
                    stop music
                    n 1kcsfu "¡Hnnng-!{nw}"

                elif Natsuki.isDistressed(higher=True):
                    n 1fslun "No dejes que la puerta te pegue al salir.{w=1}{nw}"
                    extend 1fsqem " Imbécil.{w=1}{nw}"
                    play audio glitch_c
                    stop music
                    n 1fcsan "¡Nnngg-!{nw}"

                else:
                    n 1fslun "Jeh.{w=1}{nw}"
                    extend 1fsqfr "...tal vez {i}no deberías{/i} regresar.{w=1}{nw}"
                    play audio glitch_c
                    stop music
                    n 1fcsfr "...{nw}"

                    if (random.randint(0, 10) == 1):
                        play sound glitch_d loop
                        show glitch_garbled_red zorder 99 with vpunch
                        $ renpy.pause(random.randint(4,13))
                        stop sound
                        play audio glitch_e
                        show glitch_garbled_n zorder 99 with hpunch
                        $ renpy.pause(0.025)
                        hide glitch_garbled_n
                        hide glitch_garbled_red

                # Apply consequences for force quitting, then glitch quit out
                $ Natsuki.calculated_affinity_loss()
                $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_SUDDEN_LEAVE)
                $ persistent.jn_player_apology_type_on_quit = jn_apologies.TYPE_SUDDEN_LEAVE

                play audio static
                show glitch_garbled_b zorder 99 with hpunch
                hide glitch_garbled_b
                $ renpy.jump("quit")
