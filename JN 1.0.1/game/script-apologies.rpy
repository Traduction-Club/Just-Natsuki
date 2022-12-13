default persistent._apology_database = dict()


default persistent._jn_player_apology_type_on_quit = None


default persistent._jn_player_pending_apologies = list()

init python in jn_apologies:
    from Enum import Enum
    import store

    APOLOGY_MAP = dict()

    class ApologyTypes(Enum):
        """
        Identifiers for different nickname types.
        """
        bad_nickname = 1
        cheated_game = 2
        generic = 3
        prolonged_leave = 4
        rude = 5
        sudden_leave = 6
        unhealthy = 7
        scare = 8
        bad_player_name = 9
        
        def __str__(self):
            return self.name
        
        def __int__(self):
            return self.value

    def get_all_apologies():
        """
        Gets all apology topics for the currently pending apologies, as well as the generic

        OUT:
            List<Topic> for all current pending apologies
        """
        return_apologies = [
            store.get_topic("apology_generic")
        ]
        for apology_type in store.persistent._jn_player_pending_apologies:
            return_apologies.append(store.get_topic(str("apology_{0}".format(ApologyTypes(apology_type)))))
        
        return return_apologies


label player_apologies_start:
    python:
        apologies_menu_items = [
            (_apologies.prompt, _apologies.label)
            for _apologies in jn_apologies.get_all_apologies()
        ]
        apologies_menu_items.sort()

    call screen scrollable_choice_menu(apologies_menu_items, ("Nevermind.", None))

    if _return:
        $ push(_return)
        jump call_next_topic

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For calling you a hurtful name.",
            label="apology_bad_nickname",
            unlocked=True,
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_bad_nickname:
    if persistent._jn_nicknames_natsuki_allowed:

        if Natsuki.isEnamored(higher=True):
            n 1kcssf "..."
            n 1knmsf "That hurt,{w=0.1} [player].{w=0.2} What you did."
            n 1kplsf "That really hurt me."
            n 1kcssf "..."
            n 1kplss "I'm...{w=0.3} glad you've chosen to apologize."
            n 1knmsr "Just please...{w=0.3} try to consider my feelings next time,{w=0.1} alright?"
            $ Natsuki.calculatedAffinityGain()

        elif Natsuki.isNormal(higher=True):
            n 1fcssr "..."
            n 1fnmsl "...Fine.{w=0.2} I accept your apology, okay?"
            n 1uplsl "Just please knock it off,{w=0.1} [player]."
            n 1uplaj "It isn't funny.{w=0.2} It isn't a joke."
            n 1fllsl "...And I know you're better than that."
            $ Natsuki.calculatedAffinityGain()

        elif Natsuki.isDistressed(higher=True):
            n 1fsqsl "...Are you sure,{w=0.1} [player]?"
            n 1fllaj "I mean...{w=0.3} if you actually cared about my feelings..."
            n 1fsqan "Why would you even think about doing that in the first place?"
            n 1fcsaj "Behaving like that doesn't make you funny,{w=0.1} [player]."
            n 1fsqsr "It makes you toxic."
            n 1fcssr "..."
            n 1fllsr "...Thanks,{w=0.1} I guess.{w=0.2} For the apology."
            n 1fsqsl "Just quit while you're ahead,{w=0.1} understand?"
            $ Natsuki.calculatedAffinityGain()
        else:

            n 1fcsan "...I honestly don't know what I find more {i}gross{/i} about you,{w=0.1} [player]."
            n 1fcsaj "The fact you even did it in the first place..."
            n 1fsqfu "...Or that you think a simple apology makes all that a-okay."
            n 1fcssr "..."
            n 1fcsantsa "Don't think this changes a thing,{w=0.1} [player]."
            n 1fsqsrtsb "Because it doesn't."
    else:


        if Natsuki.isEnamored(higher=True):
            n 1fcsfr "...[player]."
            n 1fplsr "I warned you."
            n 1kplsl "I warned you so many times."
            n 1fplsl "Did you think apologizing {i}now{/i} would change anything?"
            n 1fcssl "..."
            n 1kcsaj "...Look,{w=0.1} [player]."
            n 1kplsr "I appreciate your apology,{w=0.1} okay?{w=0.2} I do."
            n 1kllsr "But...{w=0.3} it's just like I said.{w=0.2} Actions have consequences."
            n 1kcssr "I hope you can understand."
            $ Natsuki.calculatedAffinityGain()

        elif Natsuki.isNormal(higher=True):
            n 1fcssr "...[player]."
            n 1fsqsr "Look.{w=0.2} You're sorry,{w=0.1} I get it.{w=0.2} I'm sure you mean it too."
            n 1fcssl "But...{w=0.3} it's like I said.{w=0.1} Actions have consequences."
            n 1kcssl "I hope you can understand."
            $ Natsuki.calculatedAffinityGain()

        elif Natsuki.isDistressed(higher=True):
            n 1fupfu "Ugh...{w=0.3} really,{w=0.1} [player]?"
            n 1fcsan "..."
            n 1fsqfr "I {i}said{/i} actions have consequences."
            n 1fcsfr "I appreciate the apology.{w=0.2} But that's all you're getting."
            $ Natsuki.calculatedAffinityGain()
        else:

            n 1kcsfr "...Wow.{w=0.2} Just wow."
            n 1fcsfu "{i}Now{/i} you choose to apologize?"
            n 1kcssrtsa "..."
            n 1fsqfutsb "Whatever.{w=0.2} I literally don't care."
            n 1fcsantsa "This changes {i}nothing{/i},{w=0.1} [player]."

    $ Natsuki.removeApology(jn_apologies.ApologyTypes.bad_nickname)
    return


init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For cheating during our games.",
            label="apology_cheated_game",
            unlocked=True,
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_cheated_game:
    if Natsuki.isEnamored(higher=True):
        n 1kchbg "Ehehe.{w=0.2} It's fine,{w=0.1} [player]."
        n 1nllsm "We all get a little too competitive sometimes,{w=0.1} right?"
        n 1nsqsm "Just remember though."
        n 1fsqbg "Two can play at that game!"
        $ Natsuki.calculatedAffinityGain()
        $ persistent.jn_snap_player_is_cheater = False

    elif Natsuki.isNormal(higher=True):
        n 1fsqbg "Huh?{w=0.2} Oh,{w=0.1} that."
        n 1nnmaj "Yeah,{w=0.1} yeah.{w=0.2} It's fine."
        n 1nllsl "Just play fair next time,{w=0.1} 'kay?"
        $ Natsuki.calculatedAffinityGain()
        $ persistent.jn_snap_player_is_cheater = False

    elif Natsuki.isDistressed(higher=True):
        n 1fcssl "Whatever,{w=0.1} [player]."
        n 1fsqsl "But thanks for the apology,{w=0.1} I guess."
        $ Natsuki.calculatedAffinityGain()
        $ persistent.jn_snap_player_is_cheater = False
    else:

        n 1fcsan "Whatever.{w=0.2} I don't care."
        n 1fsqantsa "As if I could expect much better from {i}you{/i},{w=0.1} anyway."
        $ persistent.jn_snap_player_is_cheater = False

    $ Natsuki.removeApology(jn_apologies.ApologyTypes.cheated_game)
    return


init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For something.",
            label="apology_generic",
            unlocked=True
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_generic:
    if len(persistent._jn_player_pending_apologies) == 0:

        if Natsuki.isEnamored(higher=True):
            n 1tnmaj "Huh?{w=0.2} You're sorry?"
            n 1tllaj "I...{w=0.3} don't get it,{w=0.1} [player].{w=0.2} You haven't done anything to upset me..."
            n 1tnmsl "Did you upset someone else or something?"
            n 1ncssl "..."
            n 1kchbg "Well,{w=0.1} there's no point sitting around here feeling sorry for yourself."
            n 1unmsm "You're gonna make things right,{w=0.1} [player]. 'Kay?"
            n 1kchbg "And no -{w=0.1} this isn't up for discussion."
            n 1fchsm "Whatever you did,{w=0.1} you'll fix things up and that's all there is to it."
            $ chosen_tease = jn_utils.getRandomTease()
            n 1fchbg "You have my vote of confidence,{w=0.1} [chosen_tease] -{w=0.1} now do your best!"
            n 1uchsm "Ehehe."

        elif Natsuki.isNormal(higher=True):
            n 1tnmaj "Eh?{w=0.2} You're sorry?"
            n 1nllaj "What for,{w=0.1} [player]?{w=0.2} I don't remember you getting on my nerves lately..."
            n 1fnmcal "Did you do something dumb that I don't know about?"
            n 1ncsca "..."
            n 1knmpu "Well,{w=0.1} whatever it was -{w=0.1} it's not like it's unfixable,{w=0.1} you know?"
            n 1fcsbg "Now get out there and put things right,{w=0.1} [player]!{w=0.2} I believe in you!"

        elif Natsuki.isDistressed(higher=True):
            n 1fsqbo "...You're sorry,{w=0.1} are you?"
            n 1fsqan "Did you hurt someone besides me,{w=0.1} this time?"
            n 1fcssl "..."
            n 1fsqsl "Well,{w=0.1} whatever.{w=0.2} I don't really care right now."
            n 1fsqaj "But you better go make things right,{w=0.1} [player]."
            n 1fllsl "You can do that,{w=0.1} at least."
        else:

            n 1fcsan "...Huh.{w=0.2} Wow."
            n 1fsqan "So you {i}do{/i} actually feel remorse,{w=0.1} then."
            n 1fcssl "..."
            n 1fsqfutsb "Whatever.{w=0.2} It isn't {i}me{/i} you should be apologizing to,{w=0.1} anyway."
    else:


        if Natsuki.isEnamored(higher=True):
            n 1kplsr "...[player].{w=0.2} Come on."
            n 1knmsr "You know what you did wrong."
            n 1knmaj "Just apologize properly,{w=0.1} alright?"
            n 1kllbo "I won't get mad."
            n 1kcsbo "I just wanna move on."
            $ Natsuki.percentageAffinityLoss(2.5)

        elif Natsuki.isNormal(higher=True):
            n 1fnmsf "Come on,{w=0.1} [player]."
            n 1fnmaj "You know what you did."
            n 1nllsl "Just apologize properly so we can both move on."
            $ Natsuki.percentageAffinityLoss(2)

        elif Natsuki.isDistressed(higher=True):
            n 1fupem "Ugh..."
            n 1fnman "Really,{w=0.1} [player].{w=0.2} Haven't you screwed with me enough?"
            n 1fsqfu "If you're gonna apologize,{w=0.1} have the guts to do it properly."
            n 1fsqsf "You owe me that much,{w=0.1} at least."
            $ Natsuki.percentageAffinityLoss(1.5)
        else:

            n 1fsqfu "...Do you even know how you sound?"
            n 1fnmfutsf "Do you even {i}listen{/i} to yourself?"
            n 1fcsfutsa "Apologize properly or don't bother."
            $ Natsuki.percentageAffinityLoss(1)

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For abandoning you.",
            label="apology_prolonged_leave",
            unlocked=True,
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_prolonged_leave:
    if Natsuki.isEnamored(higher=True):
        n 1kcssl "...[player]."
        n 1knmsl "We've been together a while now,{w=0.1} haven't we?"
        n 1kllsll "I...{w=0.3} really...{w=0.3} like spending time with you.{w=0.2} Why do you think I'm always here when you drop in?"
        n 1kllaj "So..."
        n 1knmsl "Can you imagine how it makes me feel when you just...{w=0.3} don't turn up?"
        n 1kcssl "..."
        n 1kplsl "I waited for you,{w=0.1} [player]."
        n 1kcsun "I waited a long time."
        n 1kcsup "I was starting to wonder if you were ever going to come back,{w=0.1} or if something happened..."
        n 1kcssf "..."
        n 1kplsm "Thanks,{w=0.1} [player].{w=0.2} I accept your apology."
        n 1kplbo "Just...{w=0.3} some notice would be nice next time,{w=0.1} is all."
        n 1kllbo "That isn't too much to ask...{w=0.3} right?"
        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isNormal(higher=True):
        n 1fcsunl "[player]..."
        n 1fbkwrl "What were you thinking?!{w=0.2} Just vanishing like that!"
        n 1fwmunl "I waited so long for you...{w=0.3} I was starting to wonder if something bad happened!"
        n 1fsqpol "N-{w=0.1}not that I care {i}that{/i} much,{w=0.1} but still...!"
        n 1fllunl "..."
        n 1fllpo "I'm...{w=0.3} grateful for your apology,{w=0.1} [player]."
        n 1fnmpo "Just...{w=0.3} no more disappearing acts,{w=0.1} alright?"
        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isDistressed(higher=True):
        n 1fcsbo "[player]."
        n 1fnmbo "I know we haven't exactly been seeing eye-to-eye lately."
        n 1knmaj "But do you know how {i}scary{/i} it is to me when you just disappear like that?"
        n 1fllsl "In case you haven't already noticed,{w=0.1} I don't exactly have many other people to talk to..."
        n 1fcssl "..."
        n 1fsqsl "Thanks for the apology,{w=0.1} I guess."
        n 1fsqbo "Just don't do that again."
        $ Natsuki.calculatedAffinityGain()
    else:

        n 1kcspu "...Ha...{w=0.3} ah...{w=0.3} haha..."
        n 1fsqan "Y-{w=0.1}you're apologizing to me?{w=0.2} For not being here?"
        n 1kcssl "...Heh..."
        n 1fsqfutsb "You should be apologizing that you {i}came back{/i}."

    $ Natsuki.removeApology(jn_apologies.ApologyTypes.prolonged_leave)
    return


init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For being rude to you.",
            label="apology_rude",
            unlocked=True,
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_rude:
    if Natsuki.isEnamored(higher=True):
        n 1kcsbo "...[player]."
        n 1knmbo "I know I give as good as I get.{w=0.2} Maybe I'm a little snappy sometimes,{w=0.1} too."
        n 1kplsl "But that was really,{w=0.1} really rude,{w=0.1} [player]."
        n 1kcsun "There was no need for that."
        n 1kcssl "..."
        n 1kplss "Thanks for the apology,{w=0.1} [player].{w=0.2} I really do appreciate it."
        n 1kllaj "Just...{w=0.3} try not to do that again,{w=0.1} 'kay?"
        n 1kplsll "It would mean a lot to me."
        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isNormal(higher=True):
        n 1fcssl "[player]..."
        n 1fnmsl "I'm glad you're apologizing for what you did,{w=0.1} but you gotta understand."
        n 1fcswr "You can't just treat people like that!"
        n 1fplsf "It...{w=0.3} really hurts when you act that way - {w=0.1}and that doesn't just apply to me."
        n 1fcssf "..."
        n 1fllsf "Let's just move on and forget about this,{w=0.1} alright?"
        n 1nllsf "Thanks,{w=0.1} [player]."
        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isDistressed(higher=True):
        n 1fcsan "..."
        n 1fsqfu "I gotta ask,{w=0.1} [player].{w=0.2} Are you like that on purpose,{w=0.1} or are you making a special effort?"
        n 1fsqan "Because I honestly can't tell anymore."
        n 1fcssr "..."
        n 1fsqaj "...Fine.{w=0.2} I guess I should accept your apology."
        n 1fsqan "I just hope you don't treat others how you're treating me."
        $ Natsuki.calculatedAffinityGain()
    else:

        n 1kcsan "Ha...{w=0.3} aha..."
        n 1fsqan "You're apologizing...{w=0.3} to me?{w=1} Why?"
        n 1fsqpu "I don't expect {i}any{/i} better from you."
        n 1fcsun "..."
        n 1fsqfutsb "You can {i}stick{/i} your apology,{w=0.1} [player]."
        n 1fcsfutsa "It means nothing to me."

    $ Natsuki.removeApology(jn_apologies.ApologyTypes.rude)
    return


init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For leaving without saying goodbye.",
            label="apology_sudden_leave",
            unlocked=True,
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_sudden_leave:
    if Natsuki.isEnamored(higher=True):
        n 1fcsunl "[player]..."
        n 1knmunl "Do you know how much it hurts when you do that?"
        n 1kcsunl "It's like you're just slamming a door in my face."
        n 1klrajl "And I'm just left wondering...{w=0.3} did I do something wrong?{w=0.2} Did I upset them?"
        n 1kcsajl "It sucks,{w=0.1} [player].{w=0.2} It really sucks."
        n 1kcssl "..."
        n 1knmss "I'm grateful for the apology,{w=0.1} but please..."
        n 1knmsm "You can at least spare the time to say goodbye properly to me,{w=0.1} right?"
        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isNormal(higher=True):
        n 1fllsl "..."
        n 1fnmsl "Hey,{w=0.1} [player]."
        n 1fnmaj "Have you ever had a conversation where one person just walks away?"
        n 1fsqaj "No 'goodbye',{w=0.1} no 'see you later',{w=0.1} nothing?{w=0.2} They just leave?"
        n 1fsqbo "How would that make you feel?"
        n 1ksqaj "Unwanted?{w=0.2} Not worth the manners?"
        n 1fllsl "Because that's just how you made me feel,{w=0.1} [player]."
        n 1fcssl "..."
        n 1flraj "I accept the apology,{w=0.1} okay?"
        n 1knmaj "Just...{w=0.3} remember to at least say goodbye to me properly."
        n 1nnmsl "You can do that much,{w=0.1} right?"
        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isDistressed(higher=True):
        n 1fsqsl "[player]."
        n 1fsqan "Do you even {i}care{/i} how rude that is?"
        n 1fsqfu "To just vanish mid-conversation with someone?"
        n 1fcssr "..."
        n 1fsqsr "Look,{w=0.1} fine.{w=0.2} Apology accepted,{w=0.1} for now."
        n 1fsqaj "But really,{w=0.1} [player].{w=0.2} I expected better -{w=0.1} even from you."
        $ Natsuki.calculatedAffinityGain()
    else:

        n 1fcsan "...Heh.{w=0.2} Honestly?"
        n 1fsqantsb "Whatever.{w=0.2} I don't care.{w=0.2} Keep your apology."
        n 1fsqsftse "You've so many other things to be sorry for.{w=0.2} What's another on the pile,{w=0.1} right?"

    $ Natsuki.removeApology(jn_apologies.ApologyTypes.sudden_leave)
    return


init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For not taking care of myself properly.",
            label="apology_unhealthy",
            unlocked=True,
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_unhealthy:
    if Natsuki.isEnamored(higher=True):
        n 1kcssml "[player],{w=0.1} [player],{w=0.1} [player]..."
        n 1knmajl "What am I gonna do with you?"
        n 1kllsll "Honestly..."
        n 1kwmsl "You know I just want what's best for you,{w=0.1} right?"
        n 1klrsl "It...{w=0.3} hurts when you don't take care of yourself."
        n 1kcssl "..."
        n 1knmss "Thanks,{w=0.1} [player].{w=0.2} I accept your apology."
        n 1knmbo "Just please...{w=0.3} take better care of yourself,{w=0.1} alright?"
        n 1kllbol "I'll get mad if you don't.{w=0.2} For real,{w=0.1} this time."
        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isNormal(higher=True):
        n 1fupbol "Ugh...{w=0.3} [player]."
        n 1fnmbo "Look.{w=0.2} I accept your apology."
        n 1knmaj "But you gotta take better care of yourself!"
        n 1fllpo "I'm not always gonna be here to babysit you,{w=0.1} you know..."
        n 1fnmem "A-{w=0.1}and it's not like I'm making an exception for you,{w=0.1} by the way!"
        n 1nlrbo "I just care about all my friends like this,{w=0.1} so...{w=0.3} yeah."
        n 1knmsl "Try and make more of an effort to look after yourself,{w=0.1} 'kay?"
        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isDistressed(higher=True):
        n 1fcssl "...Look.{w=0.2} [player]."
        n 1flrsl "Firstly,{w=0.1} thanks for the apology.{w=0.2} If you even meant it,{w=0.1} anyway."
        n 1fcsaj "But I'm really struggling to see why I should care."
        n 1fcssl "..."
        n 1fnmsl "Just...{w=0.3} take more care of yourself."
        n 1fsqsl "...And while you're at it, perhaps try taking better care of me.{w=0.2} Thanks."
        $ Natsuki.calculatedAffinityGain()
    else:

        n 1kcsun "...Heh."
        n 1fcsantsa "At least you care that {i}you{/i} aren't being treated right."

    $ Natsuki.removeApology(jn_apologies.ApologyTypes.unhealthy)
    return


init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For scaring you.",
            label="apology_scare",
            unlocked=True,
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_scare:
    if Natsuki.isEnamored(higher=True):
        n 1fskwrf "A-{w=0.1}and I should think so too,{w=0.1} [player] -{w=0.1} jeez!"
        n 1fwmpof "Are you trying to give me a heart attack or what?"
        n 1fcspol "..."
        n 1kllbol "Thank you,{w=0.1} [player].{w=0.2} I accept your apology."
        n 1kplbol "Just please...{w=0.3} no more surprises like that,{w=0.1} okay?{w=0.1} For me?"
        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isNormal(higher=True):
        n 1fbkwrl "A-{w=0.1}and you're right {i}to{/i} be sorry,{w=0.1} [player]!"
        n 1flleml "I {i}hate{/i} being made to feel like that!{w=0.2} Dummy..."
        n 1fcspo "..."
        n 1fnmpo "Alright,{w=0.1} look.{w=0.1} I accept your apology,{w=0.1} okay?"
        n 1knmaj "Just don't do stuff like that to me.{w=0.2} Please?"
        n 1flrsl "I'm not messing around,{w=0.1} [player]."
        $ Natsuki.calculatedAffinityGain()

    elif Natsuki.isDistressed(higher=True):
        n 1fsqsl "...Look,{w=0.1} [player].{w=0.2} I'm already upset.{w=0.2} Why are you trying to make me feel even worse?"
        n 1fsqfu "Did you think it was funny?{w=0.2} Or are you trying to piss me off?"
        n 1fcsan "..."
        n 1fcssl "Whatever.{w=0.2} Fine.{w=0.2} Apology accepted,{w=0.1} if you even meant it."
        n 1fsqsf "Just knock it off."
        $ Natsuki.calculatedAffinityGain()
    else:

        n 1fsqfu "Stick it,{w=0.1} [player]."
        n 1fcsantsa "We both know you don't mean that."

    $ Natsuki.removeApology(jn_apologies.ApologyTypes.scare)
    return


init 5 python:
    registerTopic(
        Topic(
            persistent._apology_database,
            prompt="For asking you to call me a bad name.",
            label="apology_bad_player_name",
            unlocked=True,
        ),
        topic_group=TOPIC_TYPE_APOLOGY
    )

label apology_bad_player_name:
    if persistent._jn_nicknames_player_allowed:

        if Natsuki.isEnamored(higher=True):
            n 1ncspuesi "..."
            n 1nllsl "...It's fine,{w=0.1} [player]."
            n 1ncsaj "Just..."
            n 1ksrsl "..."
            n 1kcstr "I really hate when I try to do something nice...{w=1}{nw}"
            extend 1ksqsr " and it just gets thrown back in my face,{w=0.1} you know?"
            n 1fcstr "I didn't {i}have{/i} to listen to what you wanted."
            n 1knmsrl "...So do you seriously think saying stuff like that {i}makes{/i} me want to do that again in the future?"
            n 1fllsrl "Because it {i}doesn't{/i},{w=0.1} [player]."
            n 1fcssrl "..."
            n 1kcsajsbl "...Look.{w=1}{nw}"
            extend 1nllpul " It's all water under the bridge,{w=0.1} okay?{w=0.75}{nw}"
            extend 1fllpol " I accept your apology."
            n 1fnmpol "Just use your noggin next time.{w=0.75}{nw}"
            extend 1fcspol " I {i}know{/i} there's one on your shoulders somewhere."
            n 1fsrunl "...Just don't start trying to prove me wrong on that.{w=0.75}{nw}"
            extend 1ksqpol " Please?"
            $ Natsuki.calculatedAffinityGain()

        elif Natsuki.isNormal(higher=True):
            n 1tnmpueqm "...Huh?{w=1}{nw}"
            extend 1nnmsl " Oh,{w=0.3} right.{w=0.75}{nw}"
            extend 1fslbol " The whole name thing."
            n 1ncspuesi "..."
            n 1fsqca "...That was still a jerkish thing to do,{w=0.5}{nw}"
            extend 1fslca " you know."
            n 1fcsemlsbl "You're just lucky I don't keep pointless grudges forever."
            extend 1fcsca " I'm a bigger person than that."
            n 1nllaj "So...{w=1}{nw}"
            extend 1nnmsl " you're forgiven.{w=0.75}{nw}"
            extend 1nsrbo " I guess."
            n 1fnmcal "Just think about what you come out with.{w=0.5}{nw}"
            extend 1ksrcalsbr " It really isn't hard,{w=0.1} is it?"
            $ Natsuki.calculatedAffinityGain()

        elif Natsuki.isDistressed(higher=True):
            n 1fcsan "...You are just unbelievable,{w=0.1} [player]."
            n 1fsqfu "Did it {i}seriously{/i} take you this long to admit you were wrong to say that?"
            n 1flrem "Like,{w=0.5}{nw}"
            extend 1fnmsc " are you {i}trying{/i} to be funny?"
            n 1fsqup "...Or are you really just {b}that{/b} arrogant?"
            n 1fcsan "..."
            n 1fsqanean "...You know what?{w=0.5}{nw}"
            extend 1fcsfuean " Fine.{w=1}{nw}"
            extend 1fllwr " Who cares?{w=0.75}{nw}"
            extend 1fsqfultsb " You clearly don't."
            n 1fcsfrtsa "I'll accept your half-baked {i}attempt{/i} at an apology."
            n 1fsqfutsb "But only because it's less effort than getting angry about it."
        else:

            n 1fsquntdr "Heh.{w=0.75}{nw}"
            extend 1fsqantsb " {i}Now{/i} you apologize,{w=0.1} huh?"
            n 1fnmanltsfean "After all this time?"
            n 1fcsanltsd "..."
            n 1fcsfultsa "You know what?{w=1}{nw}"
            extend 1fsqfultsb " Maybe I {i}should{/i} just call you that name."
            n 1fskscftdc "Why not?!{w=1}{nw}"
            extend 1fskfuftdc " Not like you {i}aren't{/i} acting like it."
            extend 1fcsanltsd " Jerk."
    else:


        if Natsuki.isEnamored(higher=True):
            n 1nllsl "..."
            n 1knmsl "[player]."
            n 1knmaj "...Exactly how many times did I warn you?"
            n 1fnmem "How many times did I {i}forgive{/i} you?{w=1}{nw}"
            extend 1fcsemean " Because I honestly lost count."
            n 1kcsfresi "..."
            n 1nsqsr "Sorry,{w=0.1} [player].{w=0.5}{nw}"
            extend 1flltr " Every joke runs its course."
            n 1fsqunl "And I am {i}not{/i} going to be the butt of this one again."
            n 1fcsajl "So."
            n 1fllcal "Fine.{w=0.5} I'll accept your apology..."
            n 1fsqcalesi "...And you're going to accept the consequences."
            n 1fcstrl "Sorry,{w=0.3} [player]."
            extend 1fsqbol " But we're done with names here."
            $ Natsuki.calculatedAffinityGain()

        elif Natsuki.isNormal(higher=True):
            n 1fcsemesi "...You've got to be kidding me,{w=0.5} right?"
            n 1fllaj "You were a jerk so many times to me about that..."
            n 1fsqan "...And you leave it this long to even {i}apologize{/i}?"
            n 1fcsemesi "..."
            n 1fsqtr "You're just lucky I'm not one for holding dumb grudges."
            n 1fcsaj "So,{w=0.3} [player]."
            n 1fslpo "I guess I'll accept the apology."
            n 1fnmfr "...But you can {i}forget{/i} about me accepting any more of your nicknames."
            n 1fsqtr "I'm done being messed around."
            $ Natsuki.calculatedAffinityGain()

        elif Natsuki.isDistressed(higher=True):
            n 1fcsan "{i}Wow{/i}.{w=1}{nw}"
            extend 1fcsfu " I would say I'm speechless,{w=0.3} if it were literally {i}anyone{/i} else."
            n 1fsqfuean "But {i}you{/i}?"
            n 1fcsem "I've about come to {i}expect{/i} this sort of crap from you."
            n 1fsqwrean "So you know what?{w=0.75}{nw}"
            extend 1fcssclean " Screw this,{w=0.75}{nw}"
            extend 1fskscltsc " and screw your apology!"
            n 1fcsscltsa "If {i}you{/i} aren't gonna listen,{w=0.5}{nw}"
            extend 1fllscltsc " then you can tell me why I {b}should{/b}!"
        else:

            n 1fcsfultdrean "Oh,{w=1}{nw}"
            extend 1fcsscltsaean " take a hike,{w=0.5}{nw}"
            extend 1fsqscltsbean " [player]!"
            n 1fcswrltsd "You {i}need{/i} a walk if you {i}seriously{/i} think after all of your crap,{w=0.75}{nw}"
            extend 1fskwrftdcean " I'm gonna be the one listening to {b}you{/b}!"

    $ Natsuki.removeApology(jn_apologies.ApologyTypes.bad_player_name)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
