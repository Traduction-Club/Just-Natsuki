# General tracking; the player unlocks Snap by admitting boredom to Natsuki at least once
default persistent.jn_snap_unlocked = False
default persistent.jn_snap_explanation_given = False

# Natsuki will refuse to play with a cheater
default persistent.jn_snap_player_is_cheater = False

# Transition for the "Snap"! popup
define popup_hide_transition = Dissolve(0.75)

init 0 python in jn_snap:
    import random
    import store
    import store.jn_apologies as jn_apologies
    import time

    # Card config
    _CARD_VALUES = range(1, 11)
    _CARD_SUITS = [
        "picas",
        "diamantes",
        "corazones",
        "espadas"
    ]

    _current_table_card_image = "mod_assets/games/snap/cards/blank.png"
    _turn_indicator_image = "mod_assets/games/snap/ui/turn_indicator_none.png"

    _SNAP_UI_Z_INDEX = 4
    _SNAP_POPUP_Z_INDEX = 5

    # Quips
    _PLAYER_CORRECT_SNAP_QUIPS = [
        "¡Nnnnn-!",
        "¡Agh!{w=0.2} ¡Vamos!",
        "¡S-{w=0.1}sí que eres rápido!",
        "¡Justo iba a decirlooo!",
        "Podrías esperar un poco,{w=0.1} [player]...",
        "¡Uuuuuuh-!",
        "¡Otra vez no!{w=0.2} Grrr...",
        "Maldita sea...",
        "No puede ser...",
        "Que tonta soy...",
        "¿Otra vez?{w=0.2} ¿En serio?",
        "Agh...",
        "Que ridículo...",
        "Seré lenta...",
        "¡Dios! Sigamos...",
        "¡Demonios!",
        "¡Dioooooos!",
        "¡Oh, venga ya,{w=0.2} [player]!",
        "¡¿Cómo puedes ser {i}tan{/i} rápido?!"
    ]

    _NATSUKI_CORRECT_SNAP_QUIPS = [
        "¡SNAP!{w=0.2} ¡Jajaja!",
        "¡Snap!{w=0.2} ¡Jajaja!",
        "¡SNAP!{w=0.2} Jejeje.",
        "¡SNAP!",
        "¡Snap!",
        "¡Snap~!",
        "¡Snap!{w=0.2} ¡Snap snap snap!",
        "¡Snappy snap!",
        "¡Bum!{w=0.2} ¡Snap!",
        "¡Snap!{w=0.2} ¡Snap!",
        "¡Snap!{w=0.2} ¡Snap!{w=0.2} ¡Snap!",
        "¡Sí!{w=0.2} ¡SNAP!",
        "¡Vamos!{w=0.2} ¡SNAP!",
        "¡Vamos!{w=0.2} ¡Snap!{w=0.2} ¡Snap!",
        "¡Snap snap puñetero snap!",
        "¡SNAAAP!{w=0.2} Jejeje.",
        "¡Bam!{w=0.2} ¡Snap!"
    ]

    _PLAYER_INCORRECT_SNAP_QUIPS = [
        "¿Oh?{w=0.2} Alguien es un impaciente,{w=0.1} ¿eh?",
        "Upsie dupsi,{w=0.1} [player]~.{w=0.2} Jejeje.",
        "Buena esa,{w=0.1} idiota.{w=0.2} ¡Jajaja!",
        "Demasiado rápido,{w=0.1} [player].{w=0.2} Jejeje.",
        "¡Jajaja!{w=0.2} ¿Qué ha sido eso,{w=0.1} [player]?",
        "Oye,{w=0.1} [player] -{w=0.1} ¡se supone que tienes que mirar las cartas!{w=0.2} Jejeje.",
        "¡Buen intento,{w=0.1} bobo!{w=0.2} ¡Jajaja!"
    ]

    _NATSUKI_INCORRECT_SNAP_QUIPS = [
        "Sn-...{w=0.3} oh.",
        "¡Snap!{w=0.2} Espera...",
        "¡SNAP!{w=0.2} ¿Eh...?{w=0.2} O-{w=0.1}oh.",
        "Snap sna-...{w=0.3} grrr."
    ]

    # Out of game tracking
    _player_win_streak = 0
    _natsuki_win_streak = 0
    last_game_result = None

    # Game outcomes
    RESULT_PLAYER_WIN = 0
    RESULT_NATSUKI_WIN = 1
    RESULT_DRAW = 3
    RESULT_FORFEIT = 4

    # In-game tracking
    _is_player_turn = None
    _player_forfeit = False
    _player_is_snapping = False
    _player_failed_snap_streak = 0
    _natsuki_can_fake_snap = False
    _natsuki_skill_level = 0
    _controls_enabled = False

    # Collections of cards involved in the game
    _cards_in_deck = []
    _cards_on_table = []
    _natsuki_hand = []
    _player_hand = []

    # A little something extra
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
        # Clear the old hands
        del _player_hand[:]
        del _natsuki_hand[:]

        # Generate all possible card combinations based on suits and values
        for card_suit in _CARD_SUITS:
            for card_value in _CARD_VALUES:
                _cards_in_deck.append((card_suit, card_value))

        # Assign each player their deck
        random.shuffle(_cards_in_deck)
        switch = False
        for card in _cards_in_deck:
            # We alternate between Natsuki and the player's hands when giving cards out
            if switch:
                switch = False
                _player_hand.append(card)

            else:
                switch = True
                _natsuki_hand.append(card)

        # Finally clear here, since we can't remove elements while iterating through
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
                renpy.play("mod_assets/sfx/card_place.mp3")
                _is_player_turn = False

        else:
            if (len(_natsuki_hand) > 0):
                new_card = _natsuki_hand.pop(0)
                _cards_on_table.append(new_card)
                renpy.play("mod_assets/sfx/card_place.mp3")
                _is_player_turn = True

        update_turn_indicator()
        draw_card_onscreen()

    def _get_card_label_to_display():
        """
        Returns a string representing the uppermost card on the table pile
        """
        if len(_cards_on_table) >= 1:
            return "{0} de {1}".format(_cards_on_table[-1][0], _cards_on_table[-1][1])

        else:
            return "¡Ninguna!"

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

        # We set this here so Natsuki can't try to snap while the player is snapping
        if is_player:
            _player_is_snapping = True

        # If the suit/value on the last placed card matches the preceding card, the snap is valid
        if _get_snap_result():

            if is_player:
                # Player called snap successfully; give them the cards on the table
                for card in _cards_on_table:
                    _player_hand.append(card)

            else:
                # Natsuki called snap successfully; give her the cards on the table
                for card in _cards_on_table:
                    _natsuki_hand.append(card)

            # Clear the cards on the table
            del _cards_on_table[:]
            renpy.play("mod_assets/sfx/card_shuffle.mp3")
            draw_card_onscreen()

            # Use of renpy.call here is a stopgap and will be reworked, as renpy.call risks breaking label flow if not carefully applied.
            # Please use renpy.jump instead of this approach

            # Natsuki comments on the correct snap
            renpy.call("snap_quip", is_player_snap=is_player, is_correct_snap=True)

        else:
            # Natsuki comments on the incorrect snap
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
            return "¡Nadie!"

        elif _is_player_turn:
            return "¡Tú!"

        else:
            return renpy.substitute("[n_name]")

label snap_intro:
    n 1nchbs "¡Muuuuy bien!{w=0.2} ¡Hora de jugar un poquito de Snap!"
    if not persistent.jn_snap_explanation_given:
        n 1nnmaj "Oh -{w=0.1} antes de empezar,{w=0.1} ¿quieres que te lo explique?{w=0.2} Ya sabes,{w=0.1} ¿cómo se juega y tal?"
        n 1nnmsm "Es un juego super simple,{w=0.1} pero creí que sería mejor preguntarte."
        n 1fcsbg "¡No me gustaría ganar solo porque no tienes idea de cómo se juega!"
        n 1nnmbg "Así que..."
        n 1nnmsm "¿Te lo explico?"
        menu:
            n "¿Quieres que te dé una explicación rápida de las normas?"

            "Si, ¡por favor!":
                jump snap_explanation

            "No,{w=0.1} estoy listo.":
                n 1fsqbg "¿Oh?{w=0.2} Ya estas listo,{w=0.1} ¿Eh?"
                n 1fchbs "¡Listo para que te patee el trasero! {w=0.2} ¡Vamos allá,{w=0.1} [player]!"
                $ persistent.jn_snap_explanation_given = True

    jump snap_start

label snap_explanation:
    n 1nnmss "¡Muy bien!{w=0.2} Las reglas son realmente simples,{w=0.1} como ya te dije."
    n 1nnmsm "Básicamente,{w=0.1} cada uno tenemos la mitad del mazo."
    n 1nnmaj "Entonces,{w=0.1} nos debemos turnar para poner las cartas boca arriba en la mesa -{w=0.1} ¡pero no podemos {i}ni escoger la tarjeta ni verla{/i} antes de sacarla!"
    n 1fsgbg "¿Me sigues,{w=0.1} [player]?{w=0.2} Jejeje."
    n 1nnmbg "Si la carta que ya estaba colocada coincide ya sea con {i}el numero o el palo{/i} de la carta que colocamos..."
    n 1uchbs "¡Entonces hay que gritar 'Snap'!"
    n 1nnmsm "Y el primero que lo diga se lleva las cartas en la mesa."
    n 1unmaj "Oh -{w=0.1} pero ten cuidado,{w=0.2} [player]."
    n 1fllsg "Cuando dices snap,{w=0.2} el turno pasa al otro jugador..."
    n 1fsqsg "Así que no lo digas a menos de tenerlo claro,{w=0.1} ¿'tá bien?"
    n 1uchbg "¡El ganador es aquel que consiga hacerse con todas las cartas!"
    n 1fcsbs "La cual normalmente voy a ser yo,{w=0.1} obviamente."
    n 1unmaj "Oh,{w=0.1} cierto -{w=0.1} también pierdes si te quedas sin cartas,{w=0.1} así que también ten eso en cuenta."
    n 1nnmsm "Así que...{w=0.3} ¿cómo lo ves,{w=0.1} [player]?{w=0.2} ¿Lo has entendido todo?"
    menu:
        n "¿Entiendes bien las normas?"
        "¿Podrías repetírmelo otra vez,{w=0.1} por favor?":
            n 1unmaj "¿Eh?{w=0.2} Bueno,{w=0.1} vale..."
            jump snap_explanation

        "Ya lo entendí.{w=0.2} ¡Vamo' a jugar!":
            n 1uchbg "¡Eso era lo que yo estaba buscando!{w=0.2} ¡Esas ganas de guerra!"
            n 1fllbg "Debería avisarte,{w=0.1} [player]..."
            n 1fchbs "¡No voy a contenerme!{w=0.2} ¡Hagámoslo!"
            $ persistent.jn_snap_explanation_given = True
            jump snap_start

        "Gracias, [n_name]. Juguemos mas tarde.":
            n 1unmaj "¿Eh?{w=0.2} Bueno,{w=0.1} está bien..."
            n 1fllpo "...Aguafiestas."
            jump ch30_loop

label snap_start:
    # Reset everything ready for a fresh game
    play audio card_shuffle
    n "..."
    $ jn_snap._reset()
    $ jn_snap._generate_hands()

    # Reset the UI
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
        n 1nchgn "Jejeje.{w=0.2} Que mala pata,{w=0.1} [player].{w=0.2} ¡Parece que te toca ser el primero!"

    else:
        n 1flrpol "Hmph...{w=0.3} Has tenido suerte esta vez.{w=0.2} Parece ser que me toca ir primero,{w=0.1} [player]."

    $ jn_globals.player_is_ingame = True
    $ jn_snap._controls_enabled = True
    jump snap_main_loop

label snap_main_loop:

    # First, let's check to see if anyone has won yet
    if len(jn_snap._player_hand) == 0 and len(jn_snap._natsuki_hand) == 0:
        # We tied somehow? End the game
        $ jn_snap._player_win_streak = 0
        $ jn_snap._natsuki_win_streak = 0
        $ jn_snap.last_game_result = jn_snap.RESULT_DRAW
        jump snap_end

    elif len(jn_snap._player_hand) == 0:
        # Player has lost; end the game
        $ jn_snap._player_win_streak = 0
        $ jn_snap._natsuki_win_streak += 1
        $ jn_snap.last_game_result = jn_snap.RESULT_NATSUKI_WIN
        jump snap_end

    elif len(jn_snap._natsuki_hand) == 0:
        # Natsuki has lost; end the game
        $ jn_snap._player_win_streak += 1
        $ jn_snap._natsuki_win_streak = 0
        $ jn_snap.last_game_result = jn_snap.RESULT_PLAYER_WIN
        jump snap_end

    $ renpy.pause(delay=max(0.33, (3.0 - (jn_snap._natsuki_skill_level * 0.5))))

    # Natsuki's snap logic

    # If a correct snap is possible, and the player isn't snapping already, Natsuki will try to call it: the higher the difficulty, the quicker Natsuki will be.
    if not jn_snap._player_is_snapping:
        if jn_snap._get_snap_result():
            $ jn_snap._call_snap()

        # She may also snap by mistake, assuming it makes sense to do so: the higher the difficulty, the less she'll accidentally jn_snap.
        elif random.choice(range(0,10 + jn_snap._natsuki_skill_level)) == 1 and len(jn_snap._cards_on_table) >= 2 and jn_snap._natsuki_can_fake_snap:
            $ jn_snap._call_snap()
            $ jn_snap._natsuki_can_fake_snap = False

    if not jn_snap._is_player_turn:
        # Natsuki gets to place a card
        $ jn_snap._place_card_on_table(False)

        # If Natsuki only has one card left, she'll try to see if she can snap before admitting defeat
        if len(jn_snap._natsuki_hand) == 0:
            $ renpy.pause(delay=max(0.33, (1.25 - (jn_snap._natsuki_skill_level * 0.5))))

            if jn_snap._get_snap_result():
                $ jn_snap._call_snap()

        $ jn_snap._is_player_turn = True
        $ jn_snap._natsuki_can_fake_snap = True

    jump snap_main_loop

label snap_quip(is_player_snap, is_correct_snap):

    $ cheat_check = False

    # Generate the quip based on what just happened
    if is_player_snap:

        # Player snapped, and was correct
        if is_correct_snap:
            $ jn_snap._player_failed_snap_streak = 0
            $ quip = renpy.substitute(random.choice(jn_snap._PLAYER_CORRECT_SNAP_QUIPS))
            show natsuki 1kwmsr zorder JN_NATSUKI_ZORDER

            # Some UE things to make it fun
            play audio smack
            hide snap_popup
            show snap_popup zorder jn_snap._SNAP_POPUP_Z_INDEX
            hide snap_popup with popup_hide_transition

        # Player snapped, and was incorrect
        else:
            $ jn_snap._player_failed_snap_streak += 1

            # Cheating warning
            if jn_snap._player_failed_snap_streak == 3 and not persistent.jn_snap_player_is_cheater:
                $ cheat_check = True
                n 1fnmaj "¡[player]!"
                n 1fnmsf "¡Estás gritando Snap a lo loco cada vez que te toca a ti!"
                n 1fnmpo "¡Así no es como se juega a esto!"
                n 1fllpo "Espero que no estes intentando hacer trampa,{w=0.1} [player]."
                n 1fsqsl "No me gusta jugar con tramposos."

            # Natsuki calls off the game
            elif jn_snap._player_failed_snap_streak == 6 and not persistent.jn_snap_player_is_cheater:
                $ jn_snap_controls_enabled = False
                n 1fcsaj "Agh...{w=0.3} Mira,{w=0.1} [player]."
                n 1fsqaj "Si no vas a jugar justamente,{w=0.1} ¿entonces por qué debería molestarme en jugar contigo?"
                n 1fsqsl "Ya te había advertido antes,{w=0.1} ¡¿verdad?!"
                n 1fcssl "..."
                n 1fnmsr "Ya estoy harta de jugar a esto,{w=0.1} [player]."

                $ _player_win_streak = 0
                $ persistent.jn_snap_player_is_cheater = True
                $ Natsuki.percentage_affinity_loss(1)
                $ jn_apologies.add_new_pending_apology(jn_apologies.TYPE_CHEATED_GAME)

                # Hide all the UI
                hide player_natsuki_hands
                hide current_table_card
                hide player_hand_icon
                hide natsuki_hand_icon
                hide turn_indicator_icon
                hide screen snap_ui

                play audio drawer
                with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

                # Reset the ingame flag, then hop back to ch30 as getting here has lost context
                $ jn_globals.player_is_ingame = False
                jump ch30_loop

            # Generic incorrect quip/tease
            else:
                $ quip = renpy.substitute(random.choice(jn_snap._PLAYER_INCORRECT_SNAP_QUIPS))
                show natsuki 1fsqsm zorder JN_NATSUKI_ZORDER

    else:

        # Natsuki snapped, and was correct
        if is_correct_snap:
            $ quip = renpy.substitute(random.choice(jn_snap._NATSUKI_CORRECT_SNAP_QUIPS))
            show natsuki 1uchbg zorder JN_NATSUKI_ZORDER

            # Some UE things to make it fun
            play audio smack
            show snap_popup zorder jn_snap._SNAP_POPUP_Z_INDEX
            hide snap_popup with popup_hide_transition

        # Natsuki snapped, and was incorrect
        else:
            $ quip = renpy.substitute(random.choice(jn_snap._NATSUKI_INCORRECT_SNAP_QUIPS))
            show natsuki 1fsqsr zorder JN_NATSUKI_ZORDER

    # Natsuki quips; disable controls so player can't skip dialogue
    $ jn_snap._controls_enabled = False

    if not cheat_check:
        n "[quip]"

    show natsuki 1uchsm at jn_left
    $ jn_snap._controls_enabled = True

    # Now we reset the flags so nothing can happen before the quip has completed
    if is_player_snap:
        $ jn_snap._player_is_snapping = False
        $ jn_snap._is_player_turn = False

    else:
        $ jn_snap._is_player_turn = True

    $ jn_snap.update_turn_indicator()

    return

label snap_end:

    $ jn_snap._controls_enabled = False

    # Player won, Natsuki amger
    if jn_snap.last_game_result == jn_snap.RESULT_PLAYER_WIN:

        if jn_snap._player_win_streak > 10:
            n 1fllpol "Si,{w=0.1} sí.{w=0.2} Has vuelto a ganar."
            n 1fsqsml "...Friki.{w=0.2} Jejeje."

        elif jn_snap._player_win_streak == 10:
            n 1fcsanf "¡¡Nnnnnnnnnn-!!"
            n 1fbkwrl "¿P-pero que es esto,{w=0.1} [player]?"
            n 1fbkful "¡¿Cómo eres tan bueno en esto?!"
            n 1flrpol "Agh..."

        elif jn_snap._player_win_streak == 5:
            n 1kbkwrl "¡Bien!{w=0.2} ¡Vale!{w=0.2} ¡Ya lo pillo!"
            n 1flleml "Eres bueno en el Snap,{w=0.1} ¡¿vale?!"
            n 1fllpol "Dios..."
            n 1klrpol "Mira...{w=0.3} ¿y si te dejas un poquito?"
            n 1kplpol "...¿Por favor?"

        elif jn_snap._player_win_streak == 3:
            n 1fcsbg "¡Ojo!{w=0.2} Alguien ha estado practicando,{w=0.1} ¿eh?"
            n 1fsqsg "O puede ser que solo tengas una racha de suerte,{w=0.1} [player]."

        else:
            n 1nllpo "Bueno,{w=0.1} caray.{w=0.2} Supongo que eso es todo,{w=0.1} ¿eh?"
            n 1nsqsm "¡Bien jugado supongo,{w=0.1} [player]!"

    # Natsuki won, Natsuki happ
    elif jn_snap.last_game_result == jn_snap.RESULT_NATSUKI_WIN:

        if jn_snap._natsuki_win_streak > 10:
            n 1fchgnl "Hombre,{w=0.1} ¡no podía haber sido más fácil!{w=0.2} Casi me siento mal y todo..."
            n 1fsqsm "...Casi.{w=0.2} Jejeje."

        if jn_snap._natsuki_win_streak == 10:
            n 1fchbsl "Dios,{w=0.1} [player]...{w=0.3} ¿estás teniendo un mal día o algo así?"
            n 1fchbs "¡Jajaja!"
            n 1nchsm "Seguiremos aquí hasta que te aburras,{w=0.1} ¿no es así?"

        elif jn_snap._natsuki_win_streak == 5:
            n 1fcsss "¿Oh?{w=0.2} ¿Y esto?{w=0.2} ¿Esta habilidad?"
            n 1fcssg "No te preocupes por eso."
            n 1fchgn "Es mi don natural,{w=0.1} [player]~."
            n 1uchbs "¿Qué te esperabas{w=0.1} retando a una pro como la que tienes delante?"
            n 1nsqsm "Jejeje."

        elif jn_snap._natsuki_win_streak == 3:
            n 1fchbg "¡Sí!{w=0.2} ¡Gané otra vez!"
            n 1fsqsm "Jejeje."

        else:
            n 1uchbs "¡Gané!{w=0.2} ¡Gané! ¡Síii!"
            n 1fsqsm "Justo como pensaba,{w=0.1} ¿sabes?{w=0.2} Jajaja."

    # What
    elif jn_snap.last_game_result == jn_snap.RESULT_DRAW:
        n 1tnmaj "...Eh.{w=0.2} ¿En serio hemos empatado?"
        n 1tllsl "Eso es...{w=0.3} bastante sorprendente,{w=0.1} de hecho.{w=0.2} Que raro."
        n 1nnmsm "Bueno,{w=0.1} es lo que tenía que ser,{w=0.1} ¡supongo!"

    else:
        # Assume forfeit
        n 1unmaj "¿Oh?{w=0.2} ¿Te rindes?"
        n 1nchgn "Bueno,{w=0.1} está bien supongo.{w=0.2} Deja que me apunte otra victoria para mi entonces.{w=0.2} Jejeje."

    # Award affinity for playing to completion with best girl
    $ Natsuki.calculated_affinity_gain()

    if jn_snap._player_win_streak >= 3:
        n 1fcsanl "¡Uuuuuuh-!"
        n 1fnmwrl "¡Y-{w=0.1}yo exijo la revancha!{w=0.2} ¡No me voy a rendir tan fácilmente!"

    elif jn_snap._natsuki_win_streak >= 3:
        n 1fsqbg "Jejeje.{w=0.2} Eso no puede ser {i}todo{/i} lo que tienes,{w=0.1} [player].{w=0.2} ¡Revancha!"

    else:
        n 1nsqsm "Así que..."

    menu:
        n "¡A jugar otra vez!"

        "¡Ahí le has dado!":
            n 1fsqsg "Claro,{w=0.1} ¡sabía que dirías eso,{w=0.1} [player]!"
            $ jn_snap._natsuki_skill_level += 1
            jump snap_start

        "Esta vez paso.":
            n 1kllpo "Owww...{w=0.3} bueno,{w=0.1} vale."
            n 1nchbg "Gracias por jugar conmigo,{w=0.1} [player]~."

            if jn_snap._player_win_streak >= 3:
                n 1flrpol "...Incluso si me has dejado humillada."

            elif jn_snap._natsuki_win_streak >= 3:
                n 1fchbgl "Quiero verte luchar con más intensidad la próxima vez. ¡Jajaja!"

            # Hide all the UI
            hide player_natsuki_hands
            hide current_table_card
            hide player_hand_icon
            hide natsuki_hand_icon
            hide turn_indicator_icon
            hide screen snap_ui

            play audio drawer
            with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

            # Reset the ingame flag, then hop back to ch30 as getting here has lost context
            $ jn_globals.player_is_ingame = False
            jump ch30_loop

label snap_forfeit:
    $ jn_snap._controls_enabled = False
    n 1knmpo "Owww...{w=0.3} ¿No te estarás rindiendo tan pronto, verdad,{w=0.1} [player]?"
    menu:
        n "...¿Es eso?"

        "Si, me rindo.":
            n 1kllpo "Oh...{w=0.3} bueno,{w=0.1} vale."
            n 1fllsg "Pero para que lo sepas..."
            n 1fchgn "¡Esta me la apunto como victoria para mí!{w=0.2} Jejeje."

            # Hit the streaks
            $ jn_snap._player_win_streak = 0
            $ jn_snap._natsuki_win_streak += 1

            # Hide all the UI
            hide player_natsuki_hands
            hide current_table_card
            hide player_hand_icon
            hide natsuki_hand_icon
            hide turn_indicator_icon
            hide screen snap_ui

            play audio drawer
            with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

            # Reset the ingame flag, then hop back to ch30 as getting here has lost context
            $ jn_globals.player_is_ingame = False
            jump ch30_loop

        "¡Ni en sueños!":
            n 1tsqdv "¡Pffffft!{w=0.2} ¿Oh, en serio?"
            n 1fchbs "¡Entonces vamos al juego,{w=0.1} [player]!"
            $ jn_snap._controls_enabled = True
            $ jn_snap._natsuki_skill_level += 1
            jump snap_main_loop

# This is the card currently on the top of the pile being shown
image current_table_card:
    anchor(0, 0)
    pos(1000, 100)
    jn_snap._current_table_card_image

# Icons representing each player's hand
image player_hand_icon:
    anchor(0,0)
    pos (675, 110)
    jn_snap._CARD_FAN_IMAGE_PLAYER

image natsuki_hand_icon:
    anchor(0,0)
    pos (675, 180)
    jn_snap._CARD_FAN_IMAGE_NATSUKI

# Icon representing who's turn it is
image turn_indicator_icon:
    anchor(0,0)
    pos(675, 250)
    jn_snap._turn_indicator_image

# Self-explanatory, you dummy
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

# Game UI
screen snap_ui:
    zorder jn_snap._SNAP_UI_Z_INDEX

    # Game information
    text "En la mesa: {0}".format(len(jn_snap._cards_on_table)) size 22 xpos 1000 ypos 50 style "categorized_menu_button"
    text "Mano de [player]: {0}".format(len(jn_snap._player_hand)) size 22 xpos 750 ypos 125 style "categorized_menu_button"
    text "Mano de [n_name]: {0}".format(len(jn_snap._natsuki_hand)) size 22 xpos 750 ypos 195 style "categorized_menu_button"
    text "Turno: {0}".format(jn_snap.get_turn_label_to_display()) size 22 xpos 750 ypos 265 style "categorized_menu_button"

    # Options
    style_prefix "hkb"
    vbox:
        xpos 1000
        ypos 440

        # Place card, but only selectable if player's turn, and both players are still capable of playing
        textbutton _("Echar carta"):
            style "hkbd_button"
            action [
                Function(jn_snap._place_card_on_table, True),
                SensitiveIf(jn_snap._is_player_turn and (len(jn_snap._natsuki_hand) > 0 or len(jn_snap._player_hand) > 0) and jn_snap._controls_enabled)]

        # Forfeit, but only selectable if player's turn, and both players are still capable of playing
        textbutton _("Rendirse"):
            style "hkbd_button"
            action [
                Function(renpy.jump, "snap_forfeit"),
                SensitiveIf(jn_snap._is_player_turn and (len(jn_snap._natsuki_hand) > 0 or len(jn_snap._player_hand) > 0) and jn_snap._controls_enabled)]

        # Snap, but only selectable if there's enough cards down on the table, and both players are still capable of playing
        textbutton _("¡Snap!"):
            style "hkbd_button"
            action [
                Function(jn_snap._call_snap, True),
                SensitiveIf(len(jn_snap._cards_on_table) >= 2 and not jn_snap._player_is_snapping and (len(jn_snap._natsuki_hand) > 0 or len(jn_snap._player_hand) > 0) and jn_snap._controls_enabled)]
