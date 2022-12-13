
default persistent.jn_snap_unlocked = False
default persistent.jn_snap_explanation_given = False


default persistent.jn_snap_player_is_cheater = False

init python in jn_snap:
    import random
    import store
    import store.jn_apologies as jn_apologies
    import time


    _CARD_VALUES = range(1, 11)
    _CARD_SUITS = [
        "clubs",
        "diamonds",
        "hearts",
        "spades"
    ]

    _current_table_card_image = "mod_assets/games/snap/cards/blank.png"
    _turn_indicator_image = "mod_assets/games/snap/ui/turn_indicator_none.png"

    _SNAP_UI_Z_INDEX = 4
    _SNAP_POPUP_Z_INDEX = 5


    _PLAYER_CORRECT_SNAP_QUIPS = [
        "Nnnnn-!",
        "Ugh!{w=0.2} Come on!",
        "Y-{w=0.1}You're fast!",
        "But I was just about to call ittt!",
        "Just you wait,{w=0.1} [player]...",
        "Uuuuuu-!",
        "Not again!{w=0.2} Grrr...",
        "Damn it...",
        "Fudge...",
        "So dumb...",
        "Again?{w=0.2} Really?",
        "Ugh...",
        "So ridiculous...",
        "So dumb...",
        "Jeez! Whatever...",
        "Jeez!",
        "Jeeeeeez!",
        "Oh come on,{w=0.2} [player]!",
        "How are you {i}that{/i} fast?!"
    ]

    _NATSUKI_CORRECT_SNAP_QUIPS = [
        "SNAP!{w=0.2} Ahaha!",
        "Snap!{w=0.2} Ahaha!",
        "SNAP!{w=0.2} Ehehe.",
        "SNAP!",
        "Snap!",
        "Snap~!",
        "Snap!{w=0.2} Snap snap snap!",
        "Snappy snap!",
        "Boom!{w=0.2} Snap!",
        "Snap!{w=0.2} Snap!",
        "Snap!{w=0.2} Snap!{w=0.2} Snap!",
        "Yes!{w=0.2} SNAP!",
        "Yeah!{w=0.2} SNAP!",
        "Yeah!{w=0.2} Snap!{w=0.2} Snap!",
        "Snap snap freaking snap!",
        "SNAAAP!{w=0.2} Ehehe.",
        "Bam!{w=0.2} Snap!"
    ]

    _PLAYER_INCORRECT_SNAP_QUIPS = [
        "Oh?{w=0.2} Someone's impatient,{w=0.1} huh?",
        "Oopsie daisy,{w=0.1} [player]~.{w=0.2} Ehehe.",
        "Nice one,{w=0.1} dummy.{w=0.2} Ahaha!",
        "Real smooth,{w=0.1} [player].{w=0.2} Ehehe.",
        "Ahaha!{w=0.2} What was that,{w=0.1} [player]?",
        "Hey,{w=0.1} [player] -{w=0.1} you're meant to read the cards!{w=0.2} Ehehe.",
        "Great play,{w=0.1} dummy!{w=0.2} Ahaha!"
    ]

    _NATSUKI_INCORRECT_SNAP_QUIPS = [
        "Sn-...{w=0.3} oh.",
        "Snap!{w=0.2} Wait...",
        "SNAP!{w=0.2} Huh...?{w=0.2} O-{w=0.1}oh.",
        "Snap sna-...{w=0.3} grrr."
    ]


    _player_win_streak = 0
    _natsuki_win_streak = 0
    last_game_result = None


    RESULT_PLAYER_WIN = 0
    RESULT_NATSUKI_WIN = 1
    RESULT_DRAW = 3
    RESULT_FORFEIT = 4


    _is_player_turn = None
    _player_forfeit = False
    _player_is_snapping = False
    _player_failed_snap_streak = 0
    _natsuki_can_fake_snap = False
    _natsuki_skill_level = 0
    _controls_enabled = False


    _cards_in_deck = []
    _cards_on_table = []
    _natsuki_hand = []
    _player_hand = []


    if random.choice(range(1, 100)) == 1:
        _CARD_FAN_IMAGE_PLAYER = "mod_assets/games/snap/ui/card_fan_icon_alt.png"

    else:
        _CARD_FAN_IMAGE_PLAYER = "mod_assets/games/snap/ui/card_fan_icon.png"

    _CARD_FAN_IMAGE_NATSUKI = "mod_assets/games/snap/ui/card_fan_icon.png"

    _SNAP_POPUP_SPRITES = [
        "mod_assets/games/snap/ui/snap_a.png",
        "mod_assets/games/snap/ui/snap_b.png",
        "mod_assets/games/snap/ui/snap_c.png",
        "mod_assets/games/snap/ui/snap_d.png"
    ]

    def _reset(complete_reset=False):
        """
        Resets the in-game variables associated with Snap

        IN:
            - true_reset - boolean flag; if True will also reset Natsuki's skill level, etc.
        """
        _is_player_turn = None
        _player_forfeit = False
        _player_is_snapping = False
        _player_failed_snap_streak = 0
        _natsuki_can_fake_snap = False
        del _cards_in_deck[:]
        del _cards_on_table[:]
        
        if complete_reset:
            _natsuki_skill_level = 1

    def _generate_hands():
        """
        Generates a deck of cards based on the card configuration
        Deck is then shuffled, and the players are then assigned their hands
        Finally, the deck is cleared
        """
        
        del _player_hand[:]
        del _natsuki_hand[:]
        
        
        for card_suit in _CARD_SUITS:
            for card_value in _CARD_VALUES:
                _cards_in_deck.append((card_suit, card_value))
        
        
        random.shuffle(_cards_in_deck)
        switch = False
        for card in _cards_in_deck:
            
            if switch:
                switch = False
                _player_hand.append(card)
            
            else:
                switch = True
                _natsuki_hand.append(card)
        
        
        del _cards_in_deck[:]

    def _place_card_on_table(is_player=False):
        """
        Takes the top-most card from the player's hand and places it on the table pile

        IN:
            - is_player boolean value representing if the player or Natsuki is the one placing their card down.
        """
        global _is_player_turn
        if is_player:
            if (len(_player_hand) > 0):
                new_card = _player_hand.pop(0)
                _cards_on_table.append(new_card)
                renpy.play("mod_assets/sfx/card_place.ogg")
                _is_player_turn = False
        
        else:
            if (len(_natsuki_hand) > 0):
                new_card = _natsuki_hand.pop(0)
                _cards_on_table.append(new_card)
                renpy.play("mod_assets/sfx/card_place.ogg")
                _is_player_turn = True
        
        update_turn_indicator()
        draw_card_onscreen()

    def _get_card_label_to_display():
        """
        Returns a string representing the uppermost card on the table pile
        """
        if len(_cards_on_table) >= 1:
            return "{0} of {1}".format(_cards_on_table[-1][0], _cards_on_table[-1][1])
        
        else:
            return "None!"

    def _get_snap_result():
        """
        Compares the last two cards placed on the table pile, and returns True if either:
            - The suits on both cards match
            - The values on both cards match
        Otherwise, returns False
        Used by Natsuki's logic to determine if she should "spot" the snap opportunity
        """
        if len(_cards_on_table) >= 2:
            return _cards_on_table[-1][0] == _cards_on_table[-2][0] or _cards_on_table[-1][1] == _cards_on_table[-2][1]
        
        else:
            return False

    def _call_snap(is_player=False):
        """
        Attempts to call snap and award cards for the player or Natsuki, based on who made the call

        IN:
            - is_player boolean value representing if the player or Natsuki was the one who made the call
        """
        global _is_player_turn
        global _player_is_snapping
        
        
        if is_player:
            _player_is_snapping = True
        
        
        if _get_snap_result():
            
            if is_player:
                
                for card in _cards_on_table:
                    _player_hand.append(card)
            
            else:
                
                for card in _cards_on_table:
                    _natsuki_hand.append(card)
            
            
            del _cards_on_table[:]
            renpy.play("mod_assets/sfx/card_shuffle.ogg")
            draw_card_onscreen()
            
            
            
            
            
            renpy.call("snap_quip", is_player_snap=is_player, is_correct_snap=True)
        
        else:
            
            renpy.call("snap_quip", is_player_snap=is_player, is_correct_snap=False)

    def draw_card_onscreen():
        """
        Shows the card currently on top of the table pile, or nothing if no cards are on the pile
        """
        global _current_table_card_image
        
        if len(_cards_on_table) is not 0:
            _current_table_card_image = "mod_assets/games/snap/cards/{0}/{1}.png".format(_cards_on_table[-1][0], _cards_on_table[-1][1])
        
        else:
            _current_table_card_image = "mod_assets/games/snap/cards/blank.png"
        
        renpy.show(name="current_table_card", zorder=_SNAP_UI_Z_INDEX)

    def update_turn_indicator():
        """
        Updates the turn indicator graphic to display who's turn it is to move
        """
        global _turn_indicator_image
        
        if _is_player_turn is None:
            _turn_indicator_image = "mod_assets/games/snap/ui/turn_indicator_none.png"
        
        elif _is_player_turn:
            _turn_indicator_image = "mod_assets/games/snap/ui/turn_indicator_player.png"
        
        else:
            _turn_indicator_image = "mod_assets/games/snap/ui/turn_indicator_natsuki.png"
        
        renpy.show(name="turn_indicator_icon", zorder=_SNAP_UI_Z_INDEX)

    def get_turn_label_to_display():
        """
        Returns a turn descriptor label based on who's turn it is to move
        """
        if _is_player_turn is None:
            return "Nobody!"
        
        elif _is_player_turn:
            return "Yours!"
        
        else:
            return renpy.substitute("[n_name]")

label snap_intro:
    n 1nchbs "Alriiiight!{w=0.2} Let's play some Snap!"
    if not persistent.jn_snap_explanation_given:
        n 1nnmaj "Oh -{w=0.1} before we start,{w=0.1} did you want an explanation?{w=0.2} You know,{w=0.1} on how it works?"
        n 1nnmsm "It's a super simple game,{w=0.1} but I thought I'd better ask."
        n 1fcsbg "I don't wanna win just because you didn't know what you were doing!"
        n 1nnmbg "So..."
        n 1nnmsm "How about it?"
        menu:
            n "Want me to run through the rules real quick?"
            "Yes please!":

                jump snap_explanation
            "No,{w=0.1} I'm ready.":

                n 1fsqbg "Oh?{w=0.2} You're ready,{w=0.1} huh?"
                n 1fchbs "Ready to get your butt kicked!{w=0.2} Let's go,{w=0.1} [player]!"
                $ persistent.jn_snap_explanation_given = True

    jump snap_start

label snap_explanation:
    n 1nnmss "Alright!{w=0.2} So the rules are dead simple,{w=0.1} like I was saying before."
    n 1nnmsm "Basically,{w=0.1} we each get half a deck of cards."
    n 1nnmaj "Then,{w=0.1} we take it in turns placing a card face up on the table -{w=0.1} we don't get to {i}pick or see{/i} the card before,{w=0.1} though!"
    n 1fsgbg "Following me so far,{w=0.1} [player]?{w=0.2} Ehehe."
    n 1nnmbg "If the card just placed down on the table matches either the {i}value or suit{/i} of the card that was there before..."
    n 1uchbs "Then we gotta call Snap!"
    n 1nnmsm "Whoever calls it first gets the cards on the table."
    n 1unmaj "Oh -{w=0.1} but you gotta be careful,{w=0.2} [player]."
    n 1fllsg "When you call snap,{w=0.2} it becomes the other player's turn..."
    n 1fsqsg "So don't shout unless you know you got it,{w=0.1} 'kay?"
    n 1uchbg "The winner is whoever ends up with all the cards first!"
    n 1fcsbs "Which is usually me,{w=0.1} obviously."
    n 1unmaj "Oh,{w=0.1} right -{w=0.1} you also lose if you run out of cards to play,{w=0.1} so you should keep that in mind too."
    n 1nnmsm "So...{w=0.3} how about it,{w=0.1} [player]?{w=0.2} You got all that?"
    menu:
        n "Do the rules all make sense to you?"
        "Could you go over them again,{w=0.1} please?":
            n 1unmaj "Huh?{w=0.2} Well,{w=0.1} okay..."
            jump snap_explanation
        "Got it.{w=0.2} Let's play!":

            n 1uchbg "That's what I'm talking about!{w=0.2} Some fighting spirit!"
            n 1fllbg "I should warn you though,{w=0.1} [player]..."
            n 1fchbs "I'm not gonna hold back!{w=0.2} Let's do this!"
            $ persistent.jn_snap_explanation_given = True
            jump snap_start
        "Thanks, [n_name]. I'll play later.":

            n 1unmaj "Huh?{w=0.2} Well,{w=0.1} alright..."
            n 1fllpo "...Spoilsport."
            jump ch30_loop

label snap_start:

    play audio card_shuffle
    n "..."
    $ jn_snap._reset()
    $ jn_snap._generate_hands()


    $ jn_snap.draw_card_onscreen()
    $ jn_snap.update_turn_indicator()

    show natsuki 1uchsm at jn_left
    show player_hand_icon zorder jn_snap._SNAP_UI_Z_INDEX
    show natsuki_hand_icon zorder jn_snap._SNAP_UI_Z_INDEX
    show turn_indicator_icon zorder jn_snap._SNAP_UI_Z_INDEX
    show screen snap_ui

    n 1nchbg "Okaaay!{w=0.2} That's the deck shuffled!"
    n 1fnmsm "Let's see who's going first..."

    play audio coin_flip
    n 1fnmpu "..."
    $ jn_snap._is_player_turn = random.choice([True, False])
    $ jn_snap.update_turn_indicator()

    if jn_snap._is_player_turn:
        n 1nchgn "Ehehe.{w=0.2} Bad luck,{w=0.1} [player].{w=0.2} Looks like you're up first!"
    else:

        n 1flrpol "Hmph...{w=0.3} you got lucky this time.{w=0.2} Looks like I'm first,{w=0.1} [player]."

    $ Natsuki.setInGame(True)
    $ jn_snap._controls_enabled = True
    jump snap_main_loop

label snap_main_loop:


    if len(jn_snap._player_hand) == 0 and len(jn_snap._natsuki_hand) == 0:

        $ jn_snap._player_win_streak = 0
        $ jn_snap._natsuki_win_streak = 0
        $ jn_snap.last_game_result = jn_snap.RESULT_DRAW
        jump snap_end

    elif len(jn_snap._player_hand) == 0:

        $ jn_snap._player_win_streak = 0
        $ jn_snap._natsuki_win_streak += 1
        $ jn_snap.last_game_result = jn_snap.RESULT_NATSUKI_WIN
        jump snap_end

    elif len(jn_snap._natsuki_hand) == 0:

        $ jn_snap._player_win_streak += 1
        $ jn_snap._natsuki_win_streak = 0
        $ jn_snap.last_game_result = jn_snap.RESULT_PLAYER_WIN
        jump snap_end

    $ jnPause(delay=max(0.33, (3.0 - (jn_snap._natsuki_skill_level * 0.5))), hard=True)




    if not jn_snap._player_is_snapping:
        if jn_snap._get_snap_result():
            $ jn_snap._call_snap()


        elif random.choice(range(0,10 + jn_snap._natsuki_skill_level)) == 1 and len(jn_snap._cards_on_table) >= 2 and jn_snap._natsuki_can_fake_snap:
            $ jn_snap._call_snap()
            $ jn_snap._natsuki_can_fake_snap = False

    if not jn_snap._is_player_turn:

        $ jn_snap._place_card_on_table(False)


        if len(jn_snap._natsuki_hand) == 0:
            $ jnPause(delay=max(0.33, (1.25 - (jn_snap._natsuki_skill_level * 0.5))), hard=True)

            if jn_snap._get_snap_result():
                $ jn_snap._call_snap()

        $ jn_snap._is_player_turn = True
        $ jn_snap._natsuki_can_fake_snap = True

    jump snap_main_loop

label snap_quip(is_player_snap, is_correct_snap):

    $ cheat_check = False


    if is_player_snap:


        if is_correct_snap:
            $ jn_snap._player_failed_snap_streak = 0
            $ quip = renpy.substitute(random.choice(jn_snap._PLAYER_CORRECT_SNAP_QUIPS))
            show natsuki 1kwmsr zorder JN_NATSUKI_ZORDER


            play audio smack
            show snap_popup zorder jn_snap._SNAP_POPUP_Z_INDEX
            $ jnPause(0.75)
            hide snap_popup
        else:


            $ jn_snap._player_failed_snap_streak += 1


            if jn_snap._player_failed_snap_streak == 3 and not persistent.jn_snap_player_is_cheater:
                $ cheat_check = True
                n 1fnmaj "[player]!"
                n 1fnmsf "You're just calling Snap whenever it's your turn!"
                n 1fnmpo "That's not how you play at all!"
                n 1fllpo "I hope you aren't trying to cheat,{w=0.1} [player]."
                n 1fsqsl "I don't like playing with cheaters."


            elif jn_snap._player_failed_snap_streak == 6 and not persistent.jn_snap_player_is_cheater:
                $ jn_snap_controls_enabled = False
                n 1fcsaj "Ugh...{w=0.3} look,{w=0.1} [player]."
                n 1fsqaj "If you aren't gonna play fairly,{w=0.1} then why should I bother playing at all?"
                n 1fsqsl "I even warned you before,{w=0.1} too!"
                n 1fcssl "..."
                n 1fnmsr "We're done with this game,{w=0.1} [player]."

                $ _player_win_streak = 0
                $ persistent.jn_snap_player_is_cheater = True
                $ Natsuki.percentageAffinityLoss(1)
                $ Natsuki.addApology(jn_apologies.ApologyTypes.cheated_game)


                hide player_natsuki_hands
                hide current_table_card
                hide player_hand_icon
                hide natsuki_hand_icon
                hide turn_indicator_icon
                hide screen snap_ui

                play audio drawer
                with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")


                $ Natsuki.setInGame(False)
                jump ch30_loop
            else:


                $ quip = renpy.substitute(random.choice(jn_snap._PLAYER_INCORRECT_SNAP_QUIPS))
                show natsuki 1fsqsm zorder JN_NATSUKI_ZORDER
    else:



        if is_correct_snap:
            $ quip = renpy.substitute(random.choice(jn_snap._NATSUKI_CORRECT_SNAP_QUIPS))
            show natsuki 1uchbg zorder JN_NATSUKI_ZORDER



            play audio smack
            show snap_popup zorder jn_snap._SNAP_POPUP_Z_INDEX
            $ jnPause(0.75)
            hide snap_popup
        else:


            $ quip = renpy.substitute(random.choice(jn_snap._NATSUKI_INCORRECT_SNAP_QUIPS))
            show natsuki 1fsqsr zorder JN_NATSUKI_ZORDER


    $ jn_snap._controls_enabled = False

    if not cheat_check:
        n "[quip]"

    show natsuki 1uchsm at jn_left
    $ jn_snap._controls_enabled = True


    if is_player_snap:
        $ jn_snap._player_is_snapping = False
        $ jn_snap._is_player_turn = False
    else:

        $ jn_snap._is_player_turn = True

    $ jn_snap.update_turn_indicator()

    return

label snap_end:

    $ jn_snap._controls_enabled = False


    if jn_snap.last_game_result == jn_snap.RESULT_PLAYER_WIN:

        if jn_snap._player_win_streak > 10:
            n 1fllpol "Yeah,{w=0.1} yeah.{w=0.2} You won again."
            n 1fsqsml "...Nerd.{w=0.2} Ehehe."

        elif jn_snap._player_win_streak == 10:
            n 1fcsanf "Nnnnnnnnnn-!!"
            n 1fbkwrl "W-what even is this,{w=0.1} [player]?"
            n 1fbkful "How are you so good at this?!"
            n 1flrpol "Ugh..."

        elif jn_snap._player_win_streak == 5:
            n 1kbkwrl "Okay!{w=0.2} Alright!{w=0.2} I get it!"
            n 1flleml "You're good at Snap,{w=0.1} okay?!"
            n 1fllpol "Jeez..."
            n 1klrpol "Now...{w=0.3} how about letting up just a little?"
            n 1kplpol "...Please?"

        elif jn_snap._player_win_streak == 3:
            n 1fcsbg "Oho!{w=0.2} Someone's been practicing,{w=0.1} huh?"
            n 1fsqsg "Or maybe you're just on a lucky streak,{w=0.1} [player]."
        else:

            n 1nllpo "Well,{w=0.1} heck.{w=0.2} I guess that's it,{w=0.1} huh?"
            n 1nsqsm "Well played though,{w=0.1} [player]!"


    elif jn_snap.last_game_result == jn_snap.RESULT_NATSUKI_WIN:

        if jn_snap._natsuki_win_streak > 10:
            n 1fchgnl "Man,{w=0.1} this is just too easy!{w=0.2} I almost feel bad..."
            n 1fsqsm "...Almost.{w=0.2} Ehehe."

        if jn_snap._natsuki_win_streak == 10:
            n 1fchbsl "Jeez,{w=0.1} [player]...{w=0.3} are you having a bad day or what?"
            n 1fchbselg "Ahaha!"
            n 1nchsm "So long as you're having fun though,{w=0.1} right?"

        elif jn_snap._natsuki_win_streak == 5:
            n 1fcsss "Oh?{w=0.2} This?{w=0.2} This skill?"
            n 1fcssg "Don't worry about it."
            n 1fchgn "It's all natural,{w=0.1} [player]~."
            n 1uchbs "What did you expect,{w=0.1} challenging a pro like that?"
            n 1nsqsm "Ehehe."

        elif jn_snap._natsuki_win_streak == 3:
            n 1fchbg "Yes!{w=0.2} I win again!"
            n 1fsqsm "Ehehe."
        else:

            n 1uchbs "I won!{w=0.2} I won! Yesss!"
            n 1fsqsm "Just as predicted,{w=0.1} right?{w=0.2} Ahaha."


    elif jn_snap.last_game_result == jn_snap.RESULT_DRAW:
        n 1tnmaj "...Huh.{w=0.2} We actually tied?"
        n 1tllsl "That's...{w=0.3} almost impressive,{w=0.1} actually.{w=0.2} Weird."
        n 1nnmsm "Well,{w=0.1} whatever,{w=0.1} I guess!"
    else:


        n 1unmaj "Oh?{w=0.2} You're giving up?"
        n 1nchgn "Well,{w=0.1} I guess that's fine.{w=0.2} Let me just chalk up another win for me,{w=0.1} then.{w=0.2} Ehehe."


    $ Natsuki.calculatedAffinityGain()

    if jn_snap._player_win_streak >= 3:
        n 1fcsanl "Uuuuuu-!"
        n 1fnmwrl "I-{w=0.1}I demand a rematch!{w=0.2} I'm not going down like this!"

    elif jn_snap._natsuki_win_streak >= 3:
        n 1fsqbg "Ehehe.{w=0.2} That can't be {i}all{/i} you've got,{w=0.1} [player].{w=0.2} Rematch!"
    else:

        n 1nsqsm "So..."

    menu:
        n "Let's play again!"
        "You're on!":

            n 1fsqsg "Yeah,{w=0.1} you bet you are,{w=0.1} [player]!"
            $ jn_snap._natsuki_skill_level += 1
            jump snap_start
        "I'll pass.":

            n 1kllpo "Awww...{w=0.3} well,{w=0.1} okay."
            n 1nchbg "Thanks for playing,{w=0.1} [player]~."

            if jn_snap._player_win_streak >= 3:
                n 1flrpol "...Even if you did kick my butt."

            elif jn_snap._natsuki_win_streak >= 3:
                n 1fchbgl "I wanna see more fight in you next time, though. Ahaha!"


            hide player_natsuki_hands
            hide current_table_card
            hide player_hand_icon
            hide natsuki_hand_icon
            hide turn_indicator_icon
            hide screen snap_ui

            play audio drawer
            with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")


            $ Natsuki.setInGame(False)
            jump ch30_loop

label snap_forfeit:
    $ jn_snap._controls_enabled = False
    n 1knmpo "Awww...{w=0.3} you're not giving up already are you,{w=0.1} [player]?"
    menu:
        n "...Are you?"
        "Yes, I give up.":

            n 1kllpo "Oh...{w=0.3} well,{w=0.1} okay."
            n 1fllsg "But just so you know..."
            n 1fchgn "I'm chalking this up as a win for me!{w=0.2} Ehehe."


            $ jn_snap._player_win_streak = 0
            $ jn_snap._natsuki_win_streak += 1


            hide player_natsuki_hands
            hide current_table_card
            hide player_hand_icon
            hide natsuki_hand_icon
            hide turn_indicator_icon
            hide screen snap_ui

            play audio drawer
            with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")


            $ Natsuki.setInGame(False)
            jump ch30_loop
        "In your dreams!":

            n 1tsqdv "Pffffft!{w=0.2} Oh really?"
            n 1fchbs "Game on then,{w=0.1} [player]!"
            $ jn_snap._controls_enabled = True
            $ jn_snap._natsuki_skill_level += 1
            jump snap_main_loop


transform snap_popup_fadeout:
    easeout 0.75 alpha 0


image current_table_card:
    anchor (0, 0)
    pos (1000, 100)
    jn_snap._current_table_card_image


image player_hand_icon:
    anchor (0,0)
    pos (675, 110)
    jn_snap._CARD_FAN_IMAGE_PLAYER

image natsuki_hand_icon:
    anchor (0,0)
    pos (675, 180)
    jn_snap._CARD_FAN_IMAGE_NATSUKI


image turn_indicator_icon:
    anchor (0,0)
    pos (675, 250)
    jn_snap._turn_indicator_image


image snap_popup:
    block:
        choice:
            "mod_assets/games/snap/ui/snap_a.png"
        choice:
            "mod_assets/games/snap/ui/snap_b.png"
        choice:
            "mod_assets/games/snap/ui/snap_c.png"
        choice:
            "mod_assets/games/snap/ui/snap_d.png"

    snap_popup_fadeout


screen snap_ui:
    zorder jn_snap._SNAP_UI_Z_INDEX


    text "Cards down: {0}".format(len(jn_snap._cards_on_table)) size 22 xpos 1000 ypos 50 style "categorized_menu_button"
    text "[player]'s hand: {0}".format(len(jn_snap._player_hand)) size 22 xpos 750 ypos 125 style "categorized_menu_button"
    text "[n_name]'s hand: {0}".format(len(jn_snap._natsuki_hand)) size 22 xpos 750 ypos 195 style "categorized_menu_button"
    text "Turn: {0}".format(jn_snap.get_turn_label_to_display()) size 22 xpos 750 ypos 265 style "categorized_menu_button"


    style_prefix "hkb"
    vbox:
        xpos 1000
        ypos 440


        textbutton _("Place"):
            style "hkbd_button"
            action [
                Function(jn_snap._place_card_on_table, True),
                SensitiveIf(jn_snap._is_player_turn and (len(jn_snap._natsuki_hand) > 0 or len(jn_snap._player_hand) > 0) and jn_snap._controls_enabled)]


        textbutton _("Forfeit"):
            style "hkbd_button"
            action [
                Function(renpy.jump, "snap_forfeit"),
                SensitiveIf(jn_snap._is_player_turn and (len(jn_snap._natsuki_hand) > 0 or len(jn_snap._player_hand) > 0) and jn_snap._controls_enabled)]


        textbutton _("Snap!"):
            style "hkbd_button"
            action [
                Function(jn_snap._call_snap, True),
                SensitiveIf(len(jn_snap._cards_on_table) >= 2 and not jn_snap._player_is_snapping and (len(jn_snap._natsuki_hand) > 0 or len(jn_snap._player_hand) > 0) and jn_snap._controls_enabled)]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
