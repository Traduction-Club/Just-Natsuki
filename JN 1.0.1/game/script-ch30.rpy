label ch30_autoload:

    scene black

    python:
        quick_menu = True
        style.say_dialogue = style.normal
        in_sayori_kill = None
        config.skipping = False
        config.allow_skipping = False
        n.display_args["callback"] = jnNoDismissDialogue
        n.what_args["slow_abortable"] = False
        n.display_args["callback"] = jnNoDismissDialogue
        n.what_args["slow_abortable"] = False





label ch30_holiday_check:
    python:
        import datetime
        import store.jn_utils as jn_utils

        jn_utils.log("Holiday check: {0}".format(jn_get_holiday_for_date(datetime.datetime.now().date())))





label ch30_visual_setup:

    show black zorder 99


    $ main_background.show()


    $ jn_atmosphere.updateSky()



label ch30_init:
    python:
        import random


        jn_data_migrations.runRuntimeMigrations()


        persistent._jn_version = config.version
        jn_utils.log("Current persisted version post-mig check: {0}".format(store.persistent._jn_version))


        if Natsuki.isEnamored(higher=True) and persistent._jn_nicknames_natsuki_allowed and persistent._jn_nicknames_natsuki_current_nickname:
            n_name = persistent._jn_nicknames_natsuki_current_nickname

        if Natsuki.isEnamored(higher=True) and persistent._jn_nicknames_player_allowed and persistent._jn_nicknames_player_current_nickname:
            player = persistent._jn_nicknames_player_current_nickname


        Natsuki.checkResetDailyAffinityGain()

        Natsuki.setInConversation(True)


        if (datetime.datetime.now() - persistent.jn_last_visited_date).total_seconds() / 604800 >= 2:
            Natsuki.setQuitApology(jn_apologies.ApologyTypes.prolonged_leave)


        elif not persistent._jn_player_apology_type_on_quit:
            Natsuki.calculatedAffinityGain()


        persistent.jn_total_visit_count += 1
        persistent.jn_last_visited_date = datetime.datetime.now()


        if Natsuki.isHappy(higher=True) and persistent.jn_custom_outfits_unlocked:
            jn_outfits.load_custom_wearables()
            jn_outfits.load_custom_outfits()

        jn_outfits.JNWearable.load_all()
        jn_outfits.JNOutfit.load_all()
        jn_utils.log("Outfit data loaded.")


        if persistent.jn_natsuki_auto_outfit_change_enabled or persistent.jn_natsuki_outfit_on_quit == "jn_temporary_outfit":
            
            Natsuki.setOutfit(jn_outfits.get_realtime_outfit())

        elif jn_outfits.outfit_exists(persistent.jn_natsuki_outfit_on_quit):
            
            Natsuki.setOutfit(jn_outfits.get_outfit(persistent.jn_natsuki_outfit_on_quit))

        else:
            
            Natsuki.setOutfit(jn_outfits.get_outfit("jn_school_uniform"))

        jn_utils.log("Outfit set.")


        if not jn_topic_in_event_list_pattern("^greeting_"):
            if (
                random.randint(1, 10) == 1
                and (not persistent.jn_player_admission_type_on_quit and not persistent._jn_player_apology_type_on_quit)
                and jn_events.select_event()
            ):
                push(jn_events.select_event())
                renpy.call("call_next_topic", False)
            
            else:
                push(greetings.select_greeting())
                persistent.jn_player_admission_type_on_quit = None
                persistent._jn_player_apology_type_on_quit = None


    show natsuki idle zorder JN_NATSUKI_ZORDER at jn_center
    hide black with Dissolve(2)
    show screen hkb_overlay
    play music audio.just_natsuki_bgm


    if Natsuki.isAffectionate(higher=True):
        if (
            (not persistent._jn_natsuki_chibi_seen and persistent.jn_total_visit_count > 50)
            or (random.randint(1, 1000) == 1)
        ):
            $ import random
            $ jn_stickers.stickerWindowPeekUp(at_right=random.choice([True, False]))




label ch30_loop:
    show natsuki idle zorder JN_NATSUKI_ZORDER at jn_center



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

        Natsuki.setInConversation(False)


    while persistent._event_list:
        call call_next_topic



label ch30_wait:
    window hide
    python:
        import random

        if (random.randint(1, 10000) == 1):
            jn_stickers.stickerWindowPeekUp(at_right=random.choice([True, False]))

        jnPause(delay=5.0, hard=True)

    jump ch30_loop


label call_next_topic(show_natsuki=True):
    if show_natsuki:
        show natsuki idle zorder JN_NATSUKI_ZORDER at jn_center

    if persistent._event_list:
        $ _topic = persistent._event_list.pop(0)

        if renpy.has_label(_topic):

            if (persistent._jn_notify_conversations
                and jn_utils.get_current_session_length().total_seconds() > 60
                and not jn_activity.getJNWindowActive()
                and not _topic in ["random_music_change", "weather_change"]):

                play audio notification
                python:
                    jn_activity.taskbarFlash()
                    store.happy_emote = jn_utils.getRandomHappyEmoticon()
                    store.angry_emote = jn_utils.getRandomAngryEmoticon()
                    store.sad_emote = jn_utils.getRandomSadEmoticon()
                    store.tease_emote = jn_utils.getRandomTeaseEmoticon()
                    store.confused_emote = jn_utils.getRandomConfusedEmoticon()

                    ENAMORED_NOTIFY_MESSAGES = [
                            "[player]! [player]! Wanna talk? [happy_emote]",
                            "Hey! You got a sec? [happy_emote]",
                            "Wanna talk? [happy_emote]",
                            "[player]! I got something! [happy_emote]",
                            "Heeey! Wanna talk?",
                            "Talk to meeee! [angry_emote]",
                            "I'm talking to you, dummy! [tease_emote]"
                        ]
                    AFFECTIONATE_NOTIFY_MESSAGES = [
                            "Wanna talk?",
                            "[player]! You wanna talk?",
                            "Hey! Hey! Talk to me! [angry_emote]",
                            "Hey dummy! I'm talking to you!",
                            "[player]! I just thought of something! [confused_emote]",
                            "[player]! I wanna talk to you!",
                            "I just thought of something, [player]!"
                        ]
                    HAPPY_NOTIFY_MESSAGES = [
                            "[player]! Did you have a sec?",
                            "[player]? Can I borrow you?",
                            "Hey! Come here a sec?",
                            "Hey! I wanna talk!",
                            "You there, [player]?"
                        ]
                    NORMAL_NOTIFY_MESSAGES = [
                            "You wanna talk?",
                            "Hey... are you busy?",
                            "[player]? Did you have a sec?",
                            "Can I borrow you for a sec?",
                            "You there, [player]?",
                            "Hey... you still there?",
                            "[player]? Are you there?"
                        ]

                    if Natsuki.isNormal(higher=True):
                        if Natsuki.isEnamored(higher=True):
                            notify_message = random.choice(ENAMORED_NOTIFY_MESSAGES)
                        
                        elif Natsuki.isAffectionate(higher=True):
                            notify_message = random.choice(AFFECTIONATE_NOTIFY_MESSAGES)
                        
                        elif Natsuki.isHappy(higher=True):
                            notify_message = random.choice(HAPPY_NOTIFY_MESSAGES)
                        
                        else:
                            notify_message = random.choice(NORMAL_NOTIFY_MESSAGES)
                        
                        jn_activity.notifyPopup(renpy.substitute(notify_message))


            $ Natsuki.setInConversation(True)
            call expression _topic

    python:


        return_keys = _return if isinstance(_return, dict) else dict()

        topic_obj = get_topic(_topic)


        if topic_obj is not None:
            
            topic_obj.shown_count += 1
            topic_obj.last_seen = datetime.datetime.now()
            
            
            if "derandom" in return_keys:
                topic_obj.random = False


    if "quit" in return_keys:
        jump quit


    python:
        global LAST_TOPIC_CALL
        LAST_TOPIC_CALL = datetime.datetime.now()
        Natsuki.setInConversation(False)

    jump ch30_loop

init python:
    LAST_TOPIC_CALL = datetime.datetime.now()
    LAST_MINUTE_CHECK = datetime.datetime.now()
    LAST_HOUR_CHECK = LAST_MINUTE_CHECK.hour
    LAST_DAY_CHECK = LAST_MINUTE_CHECK.day

    def minute_check():
        """
        Runs every minute during breaks between topics
        """
        jn_utils.save_game()
        
        
        Natsuki.checkResetDailyAffinityGain()
        
        
        if len(jn_plugins.minute_check_calls) > 0:
            for action in jn_plugins.minute_check_calls:
                eval(action.statement)
        
        
        current_activity = jn_activity.ACTIVITY_MANAGER.getCurrentActivity()
        
        if (
            Natsuki.isHappy(higher=True)
            and persistent.jn_custom_outfits_unlocked
            and len(jn_outfits._SESSION_NEW_UNLOCKS)
        ):
            queue("new_wearables_outfits_unlocked")
        
        
        
        elif (
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
                    affinity=Natsuki._getAffinityState(),
                    excludes_categories=["Setup"]
                )
            
            if topic_pool:
                if (not persistent.jn_natsuki_repeat_topics):
                    
                    store.persistent._jn_out_of_topics_warning_given = False
                
                Natsuki.calculatedAffinityGain()
                queue(random.choice(topic_pool).label)
            
            elif not store.persistent.jn_natsuki_repeat_topics and not store.persistent._jn_out_of_topics_warning_given:
                
                queue("talk_out_of_topics")
        
        elif (
            persistent._jn_notify_activity
            and Natsuki.isAffectionate(higher=True)
            and current_activity.activity_type != jn_activity.ACTIVITY_MANAGER.last_activity.activity_type
            and random.randint(1, 20) == 1
        ):
            
            jn_activity.ACTIVITY_MANAGER.last_activity = current_activity
            if jn_activity.ACTIVITY_MANAGER.last_activity.getRandomNotifyText():
                jn_activity.notifyPopup(jn_activity.ACTIVITY_MANAGER.last_activity.getRandomNotifyText())
        
        return

    def quarter_hour_check():
        """
        Runs every fifteen minutes during breaks between topics
        """
        
        
        if len(jn_plugins.quarter_hour_check_calls) > 0:
            for action in jn_plugins.quarter_hour_check_calls:
                eval(action.statement)
        
        queue("weather_change")
        queue("random_music_change")
        
        return

    def half_hour_check():
        """
        Runs every thirty minutes during breaks between topics
        """
        
        
        if len(jn_plugins.half_hour_check_calls) > 0:
            for action in jn_plugins.half_hour_check_calls:
                eval(action.statement)
        
        return

    def hour_check():
        """
        Runs every hour during breaks between topics
        """
        
        
        if len(jn_plugins.hour_check_calls) > 0:
            for action in jn_plugins.hour_check_calls:
                eval(action.statement)
        
        queue("weather_change")
        
        
        main_background.check_redraw()
        
        if (
            persistent.jn_natsuki_auto_outfit_change_enabled
            and not Natsuki.isWearingOutfit(jn_outfits.get_realtime_outfit().reference_name)
        ):
            
            renpy.call("outfits_auto_change")
        
        return

    def day_check():
        """
        Runs every day during breaks between topics
        """
        
        
        if len(jn_plugins.day_check_calls) > 0:
            for action in jn_plugins.day_check_calls:
                eval(action.statement)
        
        queue("weather_change")
        
        return

label talk_menu:
    python:

        if Natsuki.isEnamored(higher=True):
            _talk_flavor_text = random.choice(store.jn_globals.DEFAULT_TALK_FLAVOR_TEXT_LOVE_ENAMORED)

        elif Natsuki.isNormal(higher=True):
            _talk_flavor_text = random.choice(store.jn_globals.DEFAULT_TALK_FLAVOR_TEXT_AFFECTIONATE_NORMAL)

        elif Natsuki.isDistressed(higher=True):
            _talk_flavor_text = random.choice(store.jn_globals.DEFAULT_TALK_FLAVOR_TEXT_UPSET_DISTRESSED)

        else:
            _talk_flavor_text = random.choice(store.jn_globals.DEFAULT_TALK_FLAVOR_TEXT_BROKEN_RUINED)


        _talk_flavor_text = renpy.substitute(_talk_flavor_text)

    $ show_natsuki_talk_menu()
    $ Natsuki.setInConversation(True)

    menu:
        n "[_talk_flavor_text]"
        "Let's talk about...":

            call player_select_topic
        "Tell me again about...":

            call player_select_topic (is_repeat_topics=True)

        "I love you, [n_name]!" if Natsuki.isLove(higher=True) and persistent.jn_player_love_you_count > 0:
            $ push("talk_i_love_you")
            jump call_next_topic

        "I feel..." if Natsuki.isHappy(higher=True):
            jump player_admissions_start

        "I want to tell you something..." if Natsuki.isHappy(higher=True):
            jump player_compliments_start
        "I want to say sorry...":

            jump player_apologies_start

        "About your outfit..." if Natsuki.isHappy(higher=True) and persistent.jn_custom_outfits_unlocked:
            jump outfits_menu

        "Goodbye..." if Natsuki.isAffectionate(higher=True):
            jump farewell_menu

        "Goodbye." if Natsuki.isHappy(lower=True):
            jump farewell_start
        "Nevermind.":

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


        _topics.sort(key=lambda topic: topic.prompt)


        menu_items = menu_dict(_topics)

    call screen categorized_menu(
        menu_items=menu_items,
        category_pane_space=(1020, 70, 250, 572),
        option_list_space=(740, 70, 250, 572),
        category_length=len(_topics))

    $ _choice = _return


    if isinstance(_choice, basestring):
        $ push(_choice)
        jump call_next_topic


    elif _choice == -1:
        jump talk_menu


    $ _return = None

    jump ch30_loop

label farewell_menu:
    python:

        available_farewell_options = jn_farewells.get_farewell_options()
        available_farewell_options.sort(key = lambda option: option[0])
        available_farewell_options.append(("Goodbye.", "farewell_start"))

    call screen scrollable_choice_menu(available_farewell_options, ("Nevermind.", None))

    if isinstance(_return, basestring):
        show natsuki idle zorder JN_NATSUKI_ZORDER at jn_center
        $ push(_return)
        jump call_next_topic

    jump ch30_loop

label outfits_menu:
    $ outfit_options = [
        ("Can you wear an outfit for me?", "outfits_wear_outfit"),
        ("Can I suggest a new outfit?", "outfits_suggest_outfit"),
        ("Can I remove an outfit I suggested?", "outfits_remove_outfit"),
        ("Can you search again for new outfits?", "outfits_reload")
    ]
    call screen scrollable_choice_menu(outfit_options, ("Nevermind.", None))

    if isinstance(_return, basestring):
        show natsuki idle zorder JN_NATSUKI_ZORDER at jn_center
        $ push(_return)
        jump call_next_topic

    jump ch30_loop

label extras_menu:
    python:
        Natsuki.setInConversation(True)
        avaliable_extras_options = []


        for extras_option in jn_plugins.extras_options:
            if eval(extras_option.visible_if):
                avaliable_extras_options.append((extras_option.option_name, extras_option.jump_label))


        avaliable_extras_options.sort(key = lambda option: option[0])

    call screen scrollable_choice_menu(avaliable_extras_options, ("Nevermind.", None))

    if isinstance(_return, basestring):
        $ renpy.jump(_return)

    jump ch30_loop

label try_force_quit:

    if (
        jn_introduction.JNIntroductionStates(persistent.jn_introduction_state) == jn_introduction.JNIntroductionStates.complete
        and jn_farewells.JNForceQuitStates(persistent.jn_player_force_quit_state) == jn_farewells.JNForceQuitStates.not_force_quit
    ):

        $ push("farewell_force_quit")
        $ renpy.jump("call_next_topic")

    elif not jn_introduction.JNIntroductionStates(persistent.jn_introduction_state) == jn_introduction.JNIntroductionStates.complete:

        $ renpy.jump("quit")
    else:


        if Natsuki.isAffectionate(higher=True):
            n 1kplpo "W-{w=0.1}wait,{w=0.1} what?{w=0.2} Aren't you going to say goodbye first,{w=0.1} [player]?"

        elif Natsuki.isNormal(higher=True):
            n 1kskem "H-{w=0.1}hey!{w=0.2} You aren't just going to leave like that,{w=0.1} are you?"

        elif Natsuki.isDistressed(higher=True):
            n 1fsqpu "...Really?{w=0.2} I don't even get a 'goodbye' now?"
        else:

            n 1fsqsf "...Oh.{w=0.2} You're leaving."

        menu:
            "Nevermind.":

                if Natsuki.isAffectionate(higher=True):
                    n 1kllssl "T-{w=0.1}thanks,{w=0.1} [player].{w=1}{nw}"
                    n 1tllss "Now,{w=0.1} where was I...?{w=1}{nw}"
                    extend 1unmbo " Oh,{w=0.1} right.{w=1}{nw}"

                elif Natsuki.isNormal(higher=True):
                    n 1flleml "G-{w=0.1}good!{w=1}{nw}"
                    extend 1kllpol " Good...{w=1}{nw}"
                    n 1tslpu "Now...{w=0.3} what was I saying again?{w=0.5}{nw}"
                    extend 1nnmbo " Oh,{w=0.1} right.{w=1}{nw}"

                elif Natsuki.isDistressed(higher=True):
                    n 1fsqfr "...Thank you.{w=1}{nw}"
                    n 1fslpu "As I was {i}saying{/i}...{w=1}{nw}"
                else:

                    n 1fcsfr "Whatever.{w=1}{nw}"
                    n 1fsqsl "{cps=7.5}As I was saying.{/cps}{w=1}{nw}"

                return
            "...":


                hide screen hkb_overlay
                if Natsuki.isAffectionate(higher=True):
                    n 1kwmem "Come on,{w=0.2} [player]...{w=1}{nw}"
                    play audio glitch_c
                    stop music
                    n 1kcsup "...!{nw}"

                elif Natsuki.isNormal(higher=True):
                    n 1fwmun "...Really,{w=0.2} [player]?{w=1}{nw}"
                    play audio glitch_c
                    stop music
                    n 1kcsfu "Hnnng-!{nw}"

                elif Natsuki.isDistressed(higher=True):
                    n 1fslun "Don't let the door hit you on the way out.{w=1}{nw}"
                    extend 1fsqem " Jerk.{w=1}{nw}"
                    play audio glitch_c
                    stop music
                    n 1fcsan "Nnngg-!{nw}"
                else:

                    n 1fslun "Heh.{w=1}{nw}"
                    extend 1fsqfr "...Maybe you {i}shouldn't{/i} come back.{w=1}{nw}"
                    play audio glitch_c
                    stop music
                    n 1fcsfr "...{nw}"

                    if (random.randint(0, 10) == 1):
                        play sound glitch_d loop
                        show glitch_garbled_red zorder 99 with vpunch
                        $ jnPause(random.randint(4,13), hard=True)
                        stop sound
                        play audio glitch_e
                        show glitch_garbled_n zorder 99 with hpunch
                        $ jnPause(0.025, hard=True)
                        hide glitch_garbled_n
                        hide glitch_garbled_red


                python:
                    Natsuki.percentageAffinityLoss(2)
                    Natsuki.addApology(jn_apologies.ApologyTypes.sudden_leave)
                    Natsuki.setQuitApology(jn_apologies.ApologyTypes.sudden_leave)

                play audio static
                show glitch_garbled_b zorder 99 with hpunch
                hide glitch_garbled_b
                $ renpy.jump("quit")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc