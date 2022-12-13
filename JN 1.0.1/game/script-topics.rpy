default persistent._topic_database = dict()


default persistent._jn_out_of_topics_warning_given = False


default persistent.jn_player_pet = None


default persistent.jn_player_favourite_season = None


default persistent.jn_player_appearance_declined_share = False
default persistent.jn_player_appearance_eye_colour = None
default persistent.jn_player_appearance_hair_length = None
default persistent.jn_player_appearance_hair_colour = None
default persistent.jn_player_appearance_height_cm = None


default persistent.jn_player_gaming_frequency = None
default persistent.jn_player_can_drive = None
default persistent._jn_player_has_flown = None


default persistent.jn_player_love_you_count = 0


default persistent.jn_player_tea_coffee_preference = None

init python in topics:
    import store
    TOPIC_MAP = dict()

label menu_nevermind:
    n "Okay!"
    jump ch30_loop



init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="date_go2_beach",
            unlocked=True,
            prompt="Wanna go to the beach?",
            player_says=True,
            category=["date"]
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label date_go2_beach:
    n "I love the beach"
    n "Let's go!"
    $ main_background.changeLocation(beach)
    $ main_background.draw(full_redraw=True)
    return

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="date_go2_room",
            unlocked=True,
            prompt="Let's return",
            player_says=True,
            category=["date"]
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label date_go2_room:
    n "Heading back then?"
    n "Alright!"
    $ main_background.changeLocation(classroom)
    $ main_background.draw(dissolve_all=True, full_redraw=True)
    return


label talk_out_of_topics:
    if Natsuki.isNormal(higher=True):
        n 1kllpo "Uhmm..."
        n 1knmaj "Hey...{w=0.5}{nw}"
        extend 1knmss " [player]?"
        n 1fslss "I'm...{w=0.3} kinda struggling to think of more stuff I wanna talk about."
        n 1ulraj "So...{w=0.5}{nw}"
        extend 1nsrss " I don't think I'm gonna talk much until I think of something else."
        n 1nsrpo "..."
        n 1tnmem "What?{w=0.5}{nw}"
        extend 1fllpol " I don't just talk because I like the sound of my own voice,{w=0.1} you know!"
        n 1tllpu "But...{w=0.5}{nw}"
        extend 1unmbo " I guess I {i}could{/i} just tell you about whatever comes to mind."
        n 1nchbg "So...{w=0.3} how about it?"

        menu:
            n "Do you mind if I repeat some stuff?"
            "Sure, I don't mind listening.":

                $ persistent.jn_natsuki_repeat_topics = True
                n 1uchgn "Okaaay!{w=0.5}{nw}"
                extend 1tcsaj " Now,{w=0.1} let me think..."
            "I'd rather wait.":

                n 1tllaj "Well...{w=0.5}{nw}"
                extend 1tnmbo " if you're sure."

                if Natsuki.isAffectionate(higher=True):
                    n 1kwmpol "I'll try to come up with something soon,{w=0.5}{nw}"
                    extend 1klrssl " 'kay?"
                else:

                    n 1flrpol "J-{w=0.1}just don't make the silence all awkward,{w=0.1} got it?!"

    elif Natsuki.isDistressed(higher=True):
        n 1nllsf "..."
        n 1fllaj "Yeah,{w=0.1} so.{w=0.5}{nw}"
        extend 1fnmsl " I haven't got anything else to say."
        n 1fsqpu "...Or stuff I want to tell {i}you{/i},{w=0.1} anyway."
        n 1fslsr "So I'm just gonna shut up."
        n 1fcsun "Heh.{w=0.5}{nw}"
        extend 1fsqun " Not like that's a {i}problem{/i} for you,{w=0.1} huh?"
    else:

        n 1fslun "...{w=2}{nw}"
        extend 1fsqem " What?"
        n 1fcsan "You're the {i}last{/i} person I wanna think of more stuff to talk about with.{w=1}{nw}"
        extend 1fsrem " Jerk."

    $ persistent._jn_out_of_topics_warning_given = True
    return




init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_did_you_have_pets",
            unlocked=True,
            prompt="Did you ever have any pets?",
            category=["Life", "Animals", "Family"],
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_did_you_have_pets:
    python:

        pet_options = [
            ("Birds", "birds"),
            ("Cats", "cats"),
            ("Chameleons", "chameleons"),
            ("Dogs", "dogs"),
            ("Ferrets", "ferrets"),
            ("Fish", "fish"),
            ("Frogs", "frogs"),
            ("Geckos", "geckos"),
            ("Gerbils", "gerbils"),
            ("Guinea pigs", "guinea_pigs"),
            ("Hamsters", "hamsters"),
            ("Horses", "horses"),
            ("Insects", "insects"),
            ("Lizards", "lizards"),
            ("Mice", "mice"),
            ("Rats", "rats"),
            ("Rabbits", "rabbits"),
            ("Snakes", "snakes"),
            ("Something else", "something_else")
        ]

        pet_options.sort()

    if get_topic("talk_did_you_have_pets").shown_count > 0:
        n 1tnmsl "Wait...{w=0.3} didn't we talk about this before,{w=0.1} [player]?"
        n 1unmsl "Well anyway,{w=0.1} not much has changed."
        n 1ullsl "I still don't have a pet,{w=0.1} as much as I wish I did."
        n 1nnmsm "Maybe I should get one soon.{w=0.2} Hmm..."
    else:

        n 1tnmsl "Huh?{w=0.2} Did I ever have any pets?"
        n 1fllaj "You know,{w=0.1} I really wish I had.{w=0.1} But I was never allowed anything!"
        n 1fsgpo "It was always about the mess it would make,{w=0.1} or how much it would cost,{w=0.1} or literally anything else they could think of..."
        n 1fnmaj "Even when I said {i}I'd{/i} take care of everything!"
        n 1fslem "Ugh..."
        n 1fslun "It still annoys me...{w=0.3}{nw}"
        extend 1uchgn " but then again,{w=0.1} it's not like I can't keep a pet here instead,{w=0.1} right?{w=0.1} Ehehe."

    if persistent.jn_player_pet is None:
        n 1unmbg "But what about you,{w=0.1} [player]?"
        menu:
            n "Do you have any pets?"
            "Yes, I do.":

                n 1uspaw "Oh!{w=0.2} Oh oh oh!{w=0.2} You gotta tell me,{w=0.1} [player]!"
                n 1uspbs "What do you have?{w=0.2} What do you have?"
                show natsuki 1uspbs at jn_left
                call screen scrollable_choice_menu(pet_options)
            "No, I don't.":

                n 1usgem "Aww...{w=0.3} I'll admit,{w=0.1} I'm a little disappointed."
                n 1nchbg "Well,{w=0.1} then you gotta let me know if you get one,{w=0.1} [player]!"
                n 1uchgn "I wanna hear all about it!"
                return
            "I used to.":

                n 1kplaj "Oh...{w=0.3} oh gosh."
                n 1kllbo "I'm really sorry to hear that,{w=0.1} [player]."
                n 1knmbo "I hope you're managing okay now."
                n 1kcsbo "..."
                n 1knmbo "I...{w=0.3} think we should talk about something else, alright?"
                return
    else:

        n 1unmbs "What about you,{w=0.1} [player]?"
        show natsuki 1fspgs at jn_center
        menu:
            n "Did you get a new pet?"
            "Yes, I did.":

                n 1uwdgsesu "!{w=0.5}{nw}"
                n 1uspaw "Y-{w=0.2}you gotta tell me!{w=0.75}{nw}"
                extend 1fspgsedz " What did you get?{w=0.3} What did you get?"
                show natsuki 1fspca at jn_left
                call screen scrollable_choice_menu(pet_options)
            "No, I didn't.":

                n 1usgem "Aww...{w=0.3} I'll admit,{w=0.1} I'm a little disappointed."
                n 1nchbg "Well,{w=0.1} then you gotta let me know if you get one,{w=0.1} [player]!"
                n 1uchgn "I wanna hear all about it!"
                return
            "I lost one.":

                n 1knmaj "Oh...{w=0.3} oh jeez..."
                n 1knmfr "Sorry,{w=0.1} [player].{w=0.2} A-{w=0.1}are you okay?"
                n 1kllbo "Maybe we should talk about something else to keep your mind off things..."

                if Natsuki.isAffectionate(higher=True):
                    n 1knmbo "I'm...{w=0.5} here {w=0.3}for you,{w=0.1} [player]."

                return

    if isinstance(_return, basestring):
        show natsuki at jn_center
        $ persistent.jn_player_pet = _return

    if _return == "birds":
        n 1uchgn "Oh!{w=0.2} Neat!"
        n 1nnmsm "I don't think I'd keep birds myself,{w=0.1} but they brighten up rooms for sure!"
        n 1tnmaj "It doesn't get too noisy for you,{w=0.1} I hope?"
        n 1uchsm "I'm sure yours appreciate your company though."

    elif _return == "cats":
        n 1uchsm "Yay!{w=0.2} Cats!"
        n 1uchgn "I really wish I had one,{w=0.1} I love seeing all the dumb situations they get into!"
        n 1unmbs "I hope you didn't just say that because {i}I{/i} like them,{w=0.1} though.{w=0.5}{nw}"
        extend 1uchsm " Ehehe."
        n 1tnmsm "Just don't pamper it too much,{w=0.1} [player]!"

    elif _return == "chameleons":
        n 1unmaj "Oh!{w=0.2} Chameleons!"
        n 1uchgn "That's super cool,{w=0.1} [player]!"
        n 1unmbg "The color changing is crazy enough,{w=0.1} but those eyes too{w=0.1} -{w=0.1} it's like someone just made them up!"
        n 1uchgn "Still{w=0.1} -{w=0.1} that's awesome!"
        n 1unmbg "You better take good care of it,{w=0.1} okay?"

    elif _return == "dogs":
        n 1uwdaj "Oh!{w=0.2} A dog?{w=0.5}{nw}"
        extend 1uchbs " Awesome!"
        n 1nnmsm "I don't think a dog would be my first choice,{w=0.1} what with all the walks and all that."
        n 1uchbs "But I can't think of a more loving pet!"
        n "I hope yours looks after you as much as you look after it!"

    elif _return == "ferrets":
        n 1unmlg "Oh!{w=0.2} A ferret?"
        n 1uchbs "That's {i}adorable{/i}!"
        n 1tllbg "But...{w=0.3} I've always wondered.{w=0.5}{nw}"
        n 1tchbg " Are they more like a cat,{w=0.1} or a dog?"
        n 1flrss "Well,{w=0.1} whatever.{w=0.2} Either way,{w=0.1} [player]..."
        n 1unmlg "You better take good care of the little guy!"

    elif _return == "fish":
        n 1unmaj "Ooh!{w=0.2} Fish are interesting!"
        n 1kllnv "I don't think I'd call them super affectionate personally..."
        n 1uchgn "But I think they're a neat way to relieve stress!{w=0.2} They must be calming to watch in their own little world."
        n 1nsqsm "I bet you feel like you could lose yourself in that tank.{w=0.5}{nw}"
        extend 1nchsm " Ehehe."

    elif _return == "frogs":
        n 1kspaw "Ooh!{w=0.2} Froggies!"
        extend 1kspbs " Cute!"
        n 1fsqsm "I seriously can't get enough of their faces.{w=0.5}{nw}"
        extend 1fbkbs " They always look so confused!"
        n 1fllbg "Ehehe.{w=0.2} Well,{w=0.1} [player]..."
        n 1fchgn "You better {i}hop{/i} to it and take care of yours!"

    elif _return == "geckos":
        n 1uchbg "Awww!{w=0.5}{nw}"
        extend 1uchsm " Geckies!{w=1} Cute!"
        n 1kllsm "They're like goofy little lizards!{w=0.5}{nw}"
        extend 1nchsm " Ehehe."
        n 1nsqsr "Just a warning though,{w=0.1} [player]..."
        n 1fsqpo "I better not hear about any tails falling off on your watch!"

    elif _return == "gerbils":
        n 1kspaw "Awww!{w=0.2} I like gerbils!"
        n 1uchbs "It's so cute how they live in little groups to keep each other company."
        n 1unmbs "They're good at digging,{w=0.1} too{w=0.1} -{w=0.1} like seriously good!"
        n "Take good care of yours for me,{w=0.1} okay?"

    elif _return == "guinea_pigs":
        n 1unmaj "Ooh!{w=0.2} I like guinea pigs!"
        n 1uchbs "I don't know much about them,{w=0.1} but I love the little sounds they make."
        n "It's like they're always having a conversation!"
        n 1unmbs "Take good care of yours for me,{w=0.1} okay?"

    elif _return == "hamsters":
        n 1uspbs "Oh my gosh!{w=0.2} Hammies!"
        n 1uchbs "Aaaaaah!{w=0.2} I love them so much!"
        n 1uspbs "I love their little tails,{w=0.1} and their little paws,{w=0.1} and their little whiskers,{w=0.2} and-"
        n "And!{w=0.2} And..."
        n 1uwdbol "..."
        n 1uchbsl "A-{w=0.1}ahaha!{w=0.2} I'm...{w=0.5}"
        extend 1fslsslsbl " getting a little carried away."
        n 1fcspof "Y-{w=0.2}you better take good care of yours for me,{w=0.1} alright?"

    elif _return == "horses":
        n 1uspaw "W-{w=0.1}wow!{w=0.2} You aren't just messing with me,{w=0.1} right?!"
        n 1uspbs "Horses?!{w=0.2} That's amazing,{w=0.1} [player]!"
        n 1uchbs "You totally gotta teach me how to ride some day!"
        n 1uchbs "Make sure you visit yours often,{w=0.1} alright?"
        n 1unmlg "Oh -{w=0.2} and wear a helmet if you ride!"

    elif _return == "insects":
        n 1twmsc "Ack-{w=0.5}{nw}"
        n 1kslupsbl "Nnnnn..."
        n 1kwmsg "...I wish I could share your enthusiasm!{w=0.5}{nw}"
        extend 1kllss " Ahaha..."
        n 1nslunsbl "..."
        n 1nnmemleshsbl "I-{w=0.2}I mean,{w=0.75}{nw}"
        extend 1fcstrlsbr " it's cool that's something you're into!{w=0.75}{nw}"
        extend 1ksrcalsbr " But..."
        n 1ksqun "I don't think I could stomach creepy crawlies myself."
        n 1ksrunsbr "You've certainly got an...{w=0.3} interesting taste,{w=0.1} [player]."
        n 1fchsssbr "...Though I'm sure you take great care of yours!"

    elif _return == "lizards":
        n 1uchgn "Ooh!{w=0.2} Lizards,{w=0.1} huh?"
        n 1fsqss "...I trust you aren't just as cold-blooded yourself,{w=0.1} [player]."
        n 1fchgn "...Pffffft!{w=0.5}{nw}"
        extend 1uchlg " I'm kidding, [player]!{w=0.2} I'm just kidding!"
        n 1unmbg "Cool looking critters though!{w=0.2}"
        extend 1tllbg " I think you'd actually be hard pressed to find a more varied kind of pet."
        n 1uchgn "You better keep yours nice and toasty,{w=0.1} [player]!"

    elif _return == "mice":
        n 1uchgn "Ehehe.{w=0.2} Mice are adorable!"
        n 1nllaj "I'm still not sure how I feel about the tail..."
        n 1unmbg "But they're so curious and sociable!{w=0.2} I love watching them play together."
        n 1uchgn "Make sure you take care of yours for me,{w=0.1} okay?"

    elif _return == "rats":
        n 1unmbs "Rats,{w=0.1} huh?"
        n 1fsgsg "Were you expecting me to be grossed out?"
        n 1uchbselg "Ahaha!"
        n 1unmsm "Rats are fine.{w=0.2} They're surprisingly intelligent,{w=0.1} too!"
        n 1uchgn "Are you perhaps training yours,{w=0.1} [player]?{w=0.2} Ehehe."
        n 1unmbs "Make sure you take care of yours for me,{w=0.1} okay?"

    elif _return == "rabbits":
        n 1kspaw "Awwwwww!{w=0.2} Bunnies!"
        n 1kcuaw "They're so cuuute!{w=0.2} I love them!"
        n 1uchbs "Especially the ones with the floppy ears,{w=0.1} they look so cuddly!"
        n 1knmbo "It's a shame they need so much space,{w=0.1} though."
        n 1uchgn "But I'm sure yours have plenty of room to roam!{w=0.2} Ehehe."

    elif _return == "snakes":
        n 1uskaj "H-{w=0.1}huh?{w=0.5}{nw}"
        extend 1uscem " S-{w=0.1}snakes?"
        n 1fcsun "Uuuuuu..."
        n 1kcsaj "...Fine.{w=0.2} I'll just be straight with you, [player].{w=0.5}{nw}"
        extend 1kllsl " I'm...{w=0.3} not great with those."
        n 1kllaj "S-{w=0.1}snakes,{w=0.1} I mean."
        n 1kllsl "They just...{w=0.3} don't really agree with me.{w=0.2} I don't know why."
        n 1fcsgsl "B-{w=0.1}but that's not to say that they {i}can't{/i} be cute,{w=0.1} obviously!{w=0.5}{nw}"
        extend 1flrpo " Making that assumption would just be ignorant."
        n 1ksrpo "...And they deserve care just like any other pet.{w=0.5}{nw}"
        extend 1flraj " So..."
        n 1fnmpo "You better not be flaking out on yours,{w=0.1} [player]!"

    elif _return == "something_else":
        n 1unmaj "Ooh!{w=0.2} An exotic owner, are we?"
        n 1tsgsg "I wonder if that says something about the rest of your tastes?{w=0.2} Ehehe."
        n 1uchgn "I trust you take good care of yours.{w=0.1} Uncommon pets can be pretty demanding!"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_service_animals",
            unlocked=True,
            prompt="Service animals",
            category=["Animals"],
            nat_says=True,
            affinity_range=(jn_affinity.DISTRESSED, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_service_animals:
    n 1ullbo "Hmm..."
    n 1unmaj "Hey [player],{w=0.1} have you ever heard of service animals?"
    n 1unmbg "They're like animals people train up specially to do jobs that humans can't do easily."

    if Natsuki.isNormal(higher=True):
        n 1unmbs "Some work in airports to keep people safe,{w=0.1} others help in rescues...{w=0.3} it's super cool!"
        n 1uwmsm "But there's one type that's especially awesome..."
        n 1uchgn "Emotional support animals!"
        n 1ullaj "They're like really tame pets that are used to comfort people going through a bad time."
        n 1ulraj "They come in all different shapes and sizes too!{w=0.5}{nw}"
        n 1nnmpu " Dogs and cats -{w=0.5}{nw}"
        extend 1fslss " {i}obviously{/i}{w=0.5}{nw}"
        extend 1uwdgs " -{w=0.2} but even horses sometimes!"
        n 1fchbg "Awesome,{w=0.1} right?"
        n 1kllss "..."
        n 1ulrbo "..."
        n 1uplaj "You know,{w=0.1} [player]..."
        n 1kcsaj "Sometimes I wonder if one could have helped Sayori..."
        n 1klrfr "...but I try not to think about that too much."
        n 1knmem "They {i}are{/i} great,{w=0.1} but they don't do miracles."
        n 1kwmem "[player]...{w=0.3} I really hope you never have to seek their help."
        n 1kwmnv "And on that note,{w=0.1} if you do need support?"

        if Natsuki.isAffectionate(higher=True):
            n 1fcssrl "I-{w=0.2}I want you to know that you can depend on me,{w=0.1} 'kay?"

            if Natsuki.isLove(higher=True):
                n 1kwmnv "I love you,{w=0.1} [player]."
                return
        else:

            n 1fcssrl "Just...{w=0.5}{nw}"
            extend 1fnmsl " don't be dumb about it,{w=0.1} [player].{w=0.5}{nw}"
            extend 1kllss " I can listen if you need me to."
            n 1fcsajl "I-{w=0.1}I'm not a jerk!{w=0.5}{nw}"
            extend 1flrpol " It's just the least anyone can do,{w=0.1} that's all."
    else:

        n 1unmbo "They work in a bunch of places.{w=0.2} Airports and rescues and stuff,{w=0.1} usually."
        n 1unmss "But I really like emotional support animals."
        n 1nnmsl "They're like specially tame pets that are used to comfort those having a bad time."
        n 1nsgbo "..."
        n 1nsgaj "And...{w=0.3} to be perfectly honest?"
        n 1fcsun "Sometimes I feel like I could use one."
        return

    n 1ksrfr "..."
    n 1kwmfr "That got kinda heavy,{w=0.1} didn't it?"
    n 1kwmbg "Well,{w=0.1} enough of that.{w=0.2}"
    extend 1uwmss " What else do you wanna talk about?"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_using_computers_healthily",
            unlocked=True,
            prompt="Using computers healthily",
            conditional="store.jn_utils.get_current_session_length().total_seconds() / 3600 >= 8",
            category=["Life", "You", "Health"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_using_computers_healthily:
    n 1unmaj "Huh."
    n 1tnmaj "Hey,{w=0.1} [player].{w=0.2} I just thought of something."
    n 1unmsf "You gotta be at your computer to talk to me,{w=0.1} right?"
    n 1ullsf "And you've been here a while already..."

    if (jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.work_applications)
        or jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(JNActivities.artwork)
        or jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(JNActivities.coding)):
        n 1knmaj "In fact, I've even {i}seen{/i} you working on a lot of stuff myself!"
        n 1kllsl "..."

    n 1nchgn "Alright,{w=0.1} that's it!{w=0.2} I've decided."
    n 1uchgn "I'm gonna give you a little lesson on using your computer the right way!"
    n 1nnmss "Number one:{w=0.2} posture!"
    n 1fwmlg "Sit up straight,{w=0.1} and back against the chair,{w=0.1} [player].{w=0.2}"
    extend 1uchlg " I mean it!"
    n 1tnmlg "You don't want back problems,{w=0.1} do you?"
    n 1nnmsm "Make sure your feet can still touch the floor,{w=0.1} though.{w=0.2}"
    extend 1uchgn " Even I can do that!"
    n 1nnmaj "Number two:{w=0.2} distance!"
    n 1nsggn "I know you can't get enough of me,{w=0.1}"
    extend 1fnmpo " but I don't wanna see you pressing your face against the screen.{w=0.2} It's weird."
    n 1uchgn "So make sure you sit about an arm's length away from the display,{w=0.1} alright?"
    n 1uwdaj "Oh!{w=0.2} Don't forget to keep your stuff in easy reach though{w=0.1} -{w=0.1}"
    extend 1unmsm " like your mouse."
    n 1unmbg "Number three:{w=0.2} breaks!"
    n 1uwmbg "I don't know about you,{w=0.1} but I get all fidgety if I stay still too long..."
    n 1fchgn "So make sure you get off your butt and do some stretches a few times per hour!"
    n 1fsqsg "You could even get some water or something if you {i}really{/i} need an excuse to move."
    n 1nnmsm "It'd also give your eyes a rest from the screen!"
    n 1uchbs "Alright {w=0.1}-{w=0.1} and the last one!{w=0.2} This one's important,{w=0.1}"
    extend 1uchgn " so listen up good!"
    n 1unmbo "If you ever feel unwell {w=0.1}-{w=0.1} like your back aches,{w=0.1} or your eyes hurt or something..."
    n 1nwmbo "Please just stop whatever you're doing.{w=0.2} Your health comes first.{w=0.2} I don't care what needs to be done."
    n 1unmsm "Take some time to feel better,{w=0.1} then make sure all your stuff is set up right like I said."
    n "Don't carry on until you feel well enough {w=0.1}-{w=0.1} talk to someone if you have to!"
    n 1uchgn "Okaaay!{w=0.2} Lecture over!"
    n 1ullaj "Wow...{w=0.3} I rambled on a while,{w=0.1} didn't I?{w=0.2}"
    extend 1klrbgl " Sorry,{w=0.1} sorry!{w=0.2} Ehehe."

    if Natsuki.isEnamored(higher=True):
        n 1kwmsml "But you know I only do these things because I really care about you,{w=0.1} [player]...{w=0.3} right?"
        n 1kwmnvl "So please...{w=0.3} take care of yourself, okay?{w=0.2} I don't want you hurting because of me."

        if Natsuki.isLove(higher=True):
            $ chosen_endearment = jn_utils.getRandomEndearment()
            n 1kwmsml "I love you,{w=0.1} [chosen_endearment]."
            n 1kwmnvl "..."
            return
    else:

        n 1usglg "But you know I only say these things because I care."
        n 1nsqpo "...And I don't want you whining to me that your back hurts.{w=0.2}"

    n 1nchgn "Ahaha...{w=0.3} now, where were we?"
    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_staying_active",
            unlocked=True,
            prompt="Staying active",
            conditional="persistent.jn_total_visit_count >= 10",
            category=["Life", "You", "Health"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_staying_active:
    n 1nnmbo "Hey,{w=0.1} [player]..."
    n 1nllsr "You should get out more."
    n 1fsqsm "..."
    n 1fchbg "Ahaha!{w=0.2} No,{w=0.1} really!{w=0.2} I'm serious!"
    n 1ulraj "At school,{w=0.1} it was super easy to get exercise since we had to walk everywhere,{w=0.1} and we had sports and such..."
    n 1nsqsf "It's not so straightforward when you have a job and other stuff to worry about,{w=0.1} though."
    n 1fllss "I'm not gonna lie and say I worked out or anything like that..."
    n 1ullaj "But I tried to get some walks in when I could.{w=0.5}{nw}"
    extend 1uchgn " Any excuse to hit the bookshop is reason enough for me!"
    n 1kslsl "...Or {i}was{/i} reason enough, anyway."
    n 1fllaj "But still {w=0.1}-{w=0.5}{nw}"
    extend 1unmbg " you should give it a shot too,{w=0.1} [player]!"
    n 1nlrss "It doesn't have to be a hike or anything crazy{w=0.1} -{w=0.3}{nw}"
    extend 1nnmsm " it's more about keeping at it,{w=0.1} really."
    n 1fchsm "Even a daily ten minute walk will help you feel refreshed and awake!"
    n 1ullaj "So...{w=0.5}{nw}"
    extend 1fnmss " make sure you get out soon,{w=0.1} [player]."

    if Natsuki.isEnamored(higher=True):
        n 1fchbg "I wanna see you fighting fit!{w=0.5}{nw}"
        extend 1uchsm " Ehehe."
        return

    n 1fchbg "It's the least you can do!"
    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_relieving_stress",
            unlocked=True,
            prompt="Relieving stress",
            category=["Life", "You", "Health"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_relieving_stress:
    n 1ullaj "You know,{w=0.1} I'll admit it,{w=0.1} [player]."
    n 1flrbg "I...{w=0.3} kinda have a short fuse.{w=0.5}{nw}"
    extend 1klrss " Ehehe."
    n 1fnmss "I've been trying to work on that though,{w=0.3}{nw}"
    extend 1fchbg " and I'd love to share some of the ways I deal with stress!"
    n 1unmss "Personally,{w=0.1} I think the best way to deal with it if you can is to try and create some distance."
    n 1nslss "Back before all of...{w=0.3} this,{w=0.5}{nw}"
    extend 1nllss " if things got a little too much,{w=0.1} I just stepped outside if I could."
    n 1unmbo "Some fresh air and a change of scenery can really put things into context.{w=0.5}{nw}"
    extend 1fwdaj " It's crazy effective!"
    n 1ulraj "But don't just create physical distance,{w=0.1} though.{w=0.5}{nw}"
    extend 1fnmpu " Distance yourself mentally too!"
    n 1ncssr "If something is stressing you out,{w=0.1} you need to starve it of attention."
    n 1fslpo "I can't really go outside now,{w=0.5}{nw}"
    extend 1nllsf " so I just read something,{w=0.1} or watch some dumb videos."
    n 1fchbg "But do whatever works for you; {w=0.1}we all have our own comfort zones!"
    n 1fslpo "A-{w=0.1}and of course,{w=0.1} you could always come see me,{w=0.1} you know..."
    n 1fchbgl "A-{w=0.1}anyway!"
    n 1unmpu "The point is to always try and come back with a clean headspace,{w=0.3}{nw}"
    extend 1nnmss " and don't sweat the small things."
    n 1tnmss "You can manage that,{w=0.1} right [player]?"
    n 1uchsm "I'll keep working on it if you do!"
    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_careful_spending",
            unlocked=True,
            prompt="Careful spending",
            category=["Life", "You", "Health", "Society"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_careful_spending:
    n 1tllsr "..."
    n 1fllsr "..."
    n 1tnmpu "Hmm...?"
    n 1uwdgsesu "O-{w=0.1}oh!{w=0.5}{nw} "
    extend 1flrbg " A-{w=0.1}aha!{w=0.5}{nw}"
    extend 1flrdvl " I spaced out!"
    n 1unmaj "I was just thinking..."
    n 1flrbo "It's so easy to spend more than you mean nowadays,{w=0.1} you know?"
    n 1flrpu "Like...{w=0.3} it seems everywhere you look,{w=0.1} there's a sale,{w=0.1} or deals,{w=0.1} or some kind of special offer..."
    n 1unmpu "And every place accepts all kinds of ways of paying,{w=0.1} too.{w=0.5}{nw}"
    extend 1fsrpo " They make it super convenient!"
    n 1fsrpo "I guess what I'm getting at is...{w=0.3} try to be careful of your spending habits,{w=0.1} okay?"
    n 1unmss "Try not to buy junk you don't need{w=0.1} -{w=0.3}{nw}"
    extend 1flrbg " think of how much you threw away the last time you cleaned out!"
    n 1uwdajl "T-{w=0.1}that's not to say you shouldn't treat yourself,{w=0.1} of course!{w=0.5}{nw}"
    extend 1flrssl " You deserve cool stuff too!"
    n 1flrss "Money can't buy happiness...{w=0.5}{nw}"
    extend 1fchgn " but it sure as hell makes finding it easier.{w=0.5}{nw}"
    extend 1uchbselg " Ahaha!"
    n 1nllss "Well,{w=0.1} anyway.{w=0.5}{nw}"
    extend 1tnmsg " Just try to think a little before you spend,{w=0.1} [player]{w=0.1} -{w=0.3}{nw}"
    extend 1uchbs " that's all I'm saying!"

    if Natsuki.isAffectionate(higher=True):
        n 1nslbg "Besides..."
        n 1fsqsm "Gotta save up all we can for when we can hang out,{w=0.1} right?{w=0.5}{nw}"
        extend 1uchsm " Ehehe."

        if Natsuki.isLove(higher=True):
            n 1uchbgl "Love you,{w=0.1} [player]~!"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_eating_well",
            unlocked=True,
            prompt="Eating well",
            category=["Life", "You", "Health", "Food"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_eating_well:
    n 1unmaj "Hey,{w=0.1} [player]..."
    menu:
        n "Have you eaten today?"
        "Yes":

            n 1fnmbg "Aha!{w=0.5}{nw}"
            extend 1fsqbg " But did you eat {i}well{/i},{w=0.1} [player]?"
        "No":

            n 1knmpu "Huh?{w=0.2} What?{w=0.5}{nw}"
            extend 1knmem " Why not?!"
            n 1fnmem "You aren't skipping meals,{w=0.1} are you?"
            n 1flrpo "You better not be,{w=0.1} [player]."

    n 1unmpu "It's super important to make sure you aren't only eating regularly,{w=0.3}{nw}"
    extend 1fnmpu " but eating decently too!"
    n 1fnmsr "The right diet makes all the difference,{w=0.1} [player]."
    n 1ullaj "So...{w=0.5}{nw}"
    extend 1nnmaj " try and make an effort with your meals,{w=0.1} got it?"
    n 1fnmaj "And I mean a real effort!{w=0.5}{nw}"
    extend 1ulrss " Try to prepare them from scratch if you can;{w=0.3}{nw}"
    extend 1flrss " it's often cheaper than ready meals anyway."
    n 1unmss "Cut back on things like salt and sugar and stuff too...{w=0.5}{nw}"
    extend 1nslpo " as well as anything really processed."
    n 1unmaj "Oh {w=0.1}-{w=0.3}{nw}"
    extend 1fnmaj " and like I said,{w=0.1} have meals regularly too!"
    n 1fchbg "You shouldn't find yourself snacking on junk if you have proper meals throughout the day."
    n 1usqsm "Your bank balance and your body will thank you.{w=0.5}{nw}"
    extend 1nchsm " Ehehe."

    if Natsuki.isAffectionate(higher=True):
        n 1fsqsm "And besides..."
        n 1usqss "I gotta get you into good habits by yourself before I'm there to make you."
        n 1fchgnelg "Ahaha!{w=0.2} I'm kidding,{w=0.1} [player]!{w=0.2} I'm kidding!"
        n 1fsqsm "...Mostly."

        if Natsuki.isEnamored(higher=True):
            n 1uchsm "Love you, [player]~!{w=0.2} Ehehe."
            return

    n 1fllss "Now...{w=0.3} where were we?"
    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_weather_setup_main",
            unlocked=True,
            prompt="Setting up the weather",
            category=["Setup", "Weather"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_weather_setup_main:
    if persistent._jn_weather_api_key:
        $ persistent._jn_weather_setup_started = True

    if persistent._jn_weather_setup_started:

        n 1unmajesu "Oh!{w=1}{nw}"
        extend 1fcsbg " Yeah,{w=0.1} I remember!"
        n 1ulraj "So..."
        show natsuki 1unmbg at jn_center

        menu:
            n "Where did you wanna start from,{w=0.1} [player]?"
            "I want to give you an API key.":


                n 1unmaj "You wanna give me an API key?{w=1}{nw}"
                extend 1fchbg " Sure!"
                n 1nchbg "I'll just walk you through it just in case,{w=0.1} 'kay?"


                $ persistent._jn_weather_api_configured = False
                $ persistent._jn_weather_setting = int(jn_preferences.weather.JNWeatherSettings.disabled)

                jump talk_weather_setup_api_key

            "I want to give you my location." if persistent._jn_weather_api_key:

                n 1unmaj "You wanna go through your location?{w=1}{nw}"
                extend 1fchbg " Sure!"
                n 1nchbg "I'll just walk you through it just in case,{w=0.1} 'kay?"


                $ persistent._jn_weather_api_configured = False
                $ persistent._jn_weather_setting = int(jn_preferences.weather.JNWeatherSettings.disabled)

                jump talk_weather_setup_location

            "Can you try testing everything I've told you again?" if persistent._jn_weather_api_key and persistent._jn_player_latitude_longitude:

                n 1unmaj "You just want me to try testing it all again?{w=0.75}{nw}"
                extend 1fchbgeme " Right-o!"


                $ persistent._jn_weather_api_configured = False
                $ persistent._jn_weather_setting = int(jn_preferences.weather.JNWeatherSettings.disabled)

                jump talk_weather_setup_verify
            "Nevermind.":


                n 1tsqpu "Uh...{w=0.5}{nw}"
                extend 1tsrpu " huh."
                n 1fchbg "Well,{w=0.1} your loss,{w=0.3} [player]!"
                extend 1fchsm " Ehehe."

                return
    else:


        n 1fslbo "..."
        n 1fcsem "Urgh...{w=1.5}{nw}"
        extend 1fsrem " so annoying!"
        n 1fbkwr "Why is this so hard to get right...?!"
        n 1fllpo "Stupid...{w=0.5}{nw}"
        extend 1fcsan " Nnnnnn-!"

        menu:
            "What's the matter, Natsuki?":
                n 1uwdpueqm "Huh?{w=0.5}{nw}"
                extend 1uwdajesu " Oh!{w=0.5} [player]!{w=1}{nw}"
                extend 1fllbgsbr " I'm glad you asked!"
            "What're you complaining about?":

                n 1fwdemesh "...!{w=0.5}{nw}"
                n 1fcsgs "Well,{w=0.1} your attitude,{w=0.1} for one thing!{w=1}{nw}"
                extend 1fslca " Anyway..."

        n 1ullaj "So...{w=0.5}{nw}"
        extend 1flrss " I'm not really one to just sit around and admire the view."
        n 1nsqbo "But seriously,{w=0.1} [player]...{w=1}{nw}"
        extend 1fllpo " it's super boring out there!"
        n 1nsqpo "Outside the room,{w=0.1} I mean.{w=1}{nw}"
        extend 1fbkwr " Nothing ever changes!"
        n 1ulraj "But...{w=1}{nw}"
        extend 1fchbg " I've been doing a little tinkering,{w=0.1} and I think I found a way to make things a little more dynamic!"
        n 1fslsr "I just can't get it all to work properly..."
        n 1fcsem "It's just...{w=1}{nw}"
        extend 1fcssr " it's really bugging me.{w=1}{nw}"
        extend 1fslan " I hate it when I can't get stuff to go right!"

        menu:
            "Perhaps I could help?":
                n 1unmpu "Huh?{w=0.5}{nw}"
                extend 1unmbg " Really?!{w=0.5}{nw}"
                extend 1uchbs " Thanks,{w=0.1} [player]!"
                n 1fllssl "N-{w=0.3}not that I was {i}waiting{/i} for help,{w=0.1} {i}obviously{/i}!"
            "What do I have to do?":

                n 1fcsem "Jeez,{w=0.1} [player]...{w=0.3}"
                extend 1fsqpo " what's with the attitude today?"
                n 1kslpo "I'm {i}trying{/i} to do something nice here..."

        n 1ullaj "Well,{w=0.1} anyway..."
        n 1fllss "What I'm {i}trying{/i} to do is add some atmosphere to this place,{w=1}{nw}"
        extend 1fsqsm " and what better way to do that than..."
        n 1fchbg "Some actual weather!"
        n 1nsqsl "And not {i}just{/i} some randomly changing thing..."
        n 1ulraj "I wanna set things up so the weather here matches what it's like where you are,{w=0.1} [player]."
        n 1fcsbg "I know{w=0.1} -{w=0.5}{nw}"
        extend 1fchbg " awesome,{w=0.1} right?"
        n 1ullaj "But...{w=1}{nw}"
        extend 1nnmbo " I need you to go to this website I found."
        n 1kchbg "Don't worry,{w=0.1} I won't make you go search for it.{w=1}{nw}"
        extend 1uchgn " I'm not {i}that{/i} mean!"
        n 1unmss "It's called OpenWeatherMap,{w=0.5}{nw}"
        extend 1uchbg " and it's {i}super{/i} cool!{w=1}{nw}"
        extend 1fcssm " It's just what I need to make this work."
        n 1fllss "I'll need a little time to get this all set up,{w=0.1} though.{w=1}{nw}"
        extend 1ulraj " So..."

        menu:
            n "Are you okay if we get started now,{w=0.1} [player]?"
            "Sure.":

                n 1uchbg "Alright!"
                $ persistent._jn_weather_setup_started = True
                jump talk_weather_setup_api_key
            "I can't right now.":

                n 1nnmbo "Oh.{w=1.5}{nw}"
                extend 1nllss " Well..."
                n 1nllaj "Just let me know when you have the time,{w=0.1} 'kay?"
                n 1fcsbg "It'll be {i}super{/i} worth it!"
                return

label talk_weather_setup_api_key:

    n 1nchbg "Okaaay!{w=1}{nw}"
    extend 1fchbg " Let's get started!"
    n 1ullaj "So like I said{w=0.1} -{w=0.3}{nw}"
    extend 1unmaj " the website is called OpenWeatherMap.{w=1}{nw}"
    extend 1nnmsm " You can get there from {a=[store.jn_globals.LINK_OPEN_WEATHER_MAP_HOME]}here{/a}!"
    n 1ulraj "So..."

    menu:
        n "Do you have the website open,{w=0.1} [player]?"
        "Yes, I have the website open.":

            n 1nchbg "Awesome!{w=0.5}{nw}"
            extend 1nchgn " Step one complete!"
        "No, I couldn't get to the website.":

            n 1tnmaj "Huh?{w=1} Why not?{w=1}{nw}"
            extend 1tnmsr " Is it down or something?"
            n 1tslaj "Well...{w=1}{nw}"
            extend 1tnmss " Maybe we can try this again later?"
            n 1fllss "Just let me know when you're ready!"

            jump ch30_loop


    n 1nchbg "'Kay!{w=0.5}{nw}"
    extend 1fcssm " Now for step two!"
    n 1nllaj "Basically I need something called an API key,{w=1}{nw}"
    extend 1nnmbo " which will let me use that website to find out what the weather is like over there."
    n 1fslbo "But I can't do that myself...{w=1.5}{nw}"
    extend 1fchsm " which is where you come in,{w=0.1} [player]!"
    n 1nlrss "You'll need to make an account before you can get an API key."
    extend 1kchbg " It's totally free though!"
    n 1ullaj "You can create an account {a=[store.jn_globals.LINK_OPEN_WEATHER_MAP_SIGN_UP]}here{/a},{w=1}{nw}"
    extend 1nnmsm " or you can sign in using the menu at the top."
    n 1fcsaj "Just make sure to go through all the options carefully{w=0.1} -{w=0.5}{nw}"
    extend 1nsqpo " don't just dash through it!"
    n 1unmaj "Oh{w=0.1} -{w=0.5}{nw}"
    extend 1flrss " and make sure you confirm your email address once you've created it,{w=0.1} 'kay?"
    n 1nchbg "{a=[store.jn_globals.LINK_OPEN_WEATHER_MAP_SIGN_UP]}Here's{/a} that link once more,{w=0.1} just in case!"
    n 1fnmsm "Now..."

    menu:
        n "Did you get an account sorted,{w=0.1} [player]?"
        "Yes, I have an account set up.":

            n 1fchsm "Awesome!"
            n 1tllss "You'll probably want to make sure you save your login details somewhere secure,{w=0.5}{nw}"
            extend 1fchsm " juuuust in case."
            n 1fchts "Don't forget to confirm your email address too!"
            n 1fsqsm "Now,{w=0.1} here comes the challenging part..."
        "I already had an account set up.":

            n 1fchsm "Awesome!{w=0.5}{nw}"
            extend 1fchsm " The rest of this should be a piece of cake!"




    n 1usqsm "Are you ready,{w=0.1} [player]?"
    n 1fchsm "You need to get your API key and send it to me!"
    n 1ullss "You can find your keys {a=[store.jn_globals.LINK_OPEN_WEATHER_MAP_API_KEYS]}here{/a},{w=1}{nw}"
    extend 1unmaj " or you can get there using the menu like before."
    n 1tsqsm "You got all that?"
    n 1fsqsm "Ehehe.{w=0.5}{nw}"
    extend 1fchbg " Then take it away,{w=0.1} [player]!"

    $ player_input_valid = False


    while not player_input_valid:

        $ player_input = renpy.input("Enter your API key (or type Nevermind to go back):")

        if not player_input or player_input == "":
            n 1tsqsm "I {i}thought{/i} I asked for an {i}API key{/i},{w=0.1} [player]?"
            extend 1fchbl " Try again!"

        elif player_input.replace(" ", "").lower() == "nevermind":

            n 1tnmaj "Huh?{w=0.2} You don't wanna continue?"
            n 1tllbo "That's fine,{w=0.1} I guess."
            n 1fcsbg "Just let me know when you're ready,{w=0.1} 'kay?"

            jump ch30_loop
        else:


            $ player_input_valid = True
            $ persistent._jn_weather_api_key = player_input
            n 1uchbg "Alright!{w=0.2} I got it!"

            jump talk_weather_setup_location

label talk_weather_setup_location:
    n 1fsqbg "Now for the final piece of the puzzle..."
    n 1uchbg "...Your location,{w=0.1} obviously!"
    n 1ullaj "There's a couple ways to do this,{w=1}{nw}"
    extend 1nnmsm " but I thought it'd be best to just ask."
    n 1ulraj "So..."

    menu:
        n "How do you wanna tell me, [player]?"
        "Can you try locating me through the Internet?":

            n 1fchsm "Sure, I can give it a shot!{w=1}{nw}"
            extend 1fcssm " Just give me a second here...{w=1}{nw}"

            $ ip_latitude_longitude = jn_atmosphere.getLatitudeLongitudeByIpAddress()
            if not ip_latitude_longitude:

                n 1fslpu "...Huh."
                n 1knmpo "I {i}tried{/i} to look you up, but I couldn't find anything!"
                n 1flrpo "..."
                n 1tlraj "Well..."
                extend 1tllbg " looks like we're gonna have to do things the old-fashioned way,{w=0.1} [player]."

                jump talk_weather_setup_manual_coords
            else:


                n 1nwdbg "Aha!{w=0.5}{nw}"
                extend 1uchbg " I think I got it!"
                n 1nwlbg "Now...{w=0.3} wanna see something awesome, [player]?{w=1}{nw}"
                extend 1fsqsm " I know you do."
                n 1ncsbo "...{w=1}{nw}"

                python:

                    show_map_success = False
                    try:
                        jn_open_google_maps(ip_latitude_longitude[0], ip_latitude_longitude[1])
                        show_map_success = True

                    except Exception as exception:
                        store.jn_utils.log(exception.message, jn_utils.SEVERITY_ERR)

                if show_map_success:
                    n 1fchbg "Ta-da!{w=0.5} Found you!"
                    n 1fsqsm "..."
                    n 1tsqsm "Well?{w=1}{nw}"
                    extend 1tsqss " Am I right or what, [player]?"
                    menu:
                        "Yes, you found me.":
                            n 1fcsbg "Like a pro!"
                            extend 1fcssm " Ehehe."
                            n 1fllss "I'll just note those down real quick..."

                            $ persistent._jn_player_latitude_longitude = ip_latitude_longitude
                            jump talk_weather_setup_verify
                        "No, that's not right.":

                            n 1fnmgs "What?{w=0.2} Are you kidding me!?"
                            n 1flrsl "Ugh..."
                            n 1nlrpu "And I was so proud of myself for figuring that out,{w=0.1} too..."
                            n 1nnmss "Well,{w=0.1} it looks like we're gonna have to do things the old-fashioned way."

                            jump talk_weather_setup_manual_coords
                else:

                    n 1fnmaj "Eh?{w=0.2} What the...?"
                    n 1nnmpu "Huh.{w=0.2} Weird."
                    n 1nlrss "Well,{w=0.1} I {i}was{/i} gonna show you something neat,{w=0.5}{nw}"
                    extend 1nslpo " but it looks like something messed up."
                    n 1nlrss "Hey,{w=0.1} [player]...{w=0.3}"
                    extend 1flrbg " could you look these coordinates up and tell me if I got it right?"
                    n 1tslbo "I'm {i}pretty{/i} sure your latitude is [ip_latitude_longitude[0]],{w=0.1} and your longitude is [ip_latitude_longitude[1]]."
                    n 1nllbo "..."
                    n 1tnmss "Well,{w=0.3} [player]?"
                    menu:
                        n "How're we looking?"
                        "Yes, that looks good to me.":

                            n 1kchbg "Phew!"
                            extend 1nsldv " I was kinda worried I'd have to get a little more creative..."

                            $ persistent._jn_player_latitude_longitude = ip_latitude_longitude
                            jump talk_weather_setup_verify
                        "No, that's not right.":

                            n 1fcsan "Uuuuuuu..."
                            n 1nslpo "Fine.{w=1}{nw}"
                            extend 1usqpo " It looks like we're gonna have to do things the old-fashioned way."

                            jump talk_weather_setup_manual_coords
        "I want to tell you where I am myself.":

            n 1uchgn "Well, you're the boss!"

            jump talk_weather_setup_manual_coords
        "Nevermind.":

            n 1fllpo "Well...{w=1}{nw}"
            extend 1nslpo " fine."
            n 1fchbg "Just let me know when you wanna go through all this again,{w=0.1} 'kay?"

            jump ch30_loop

label talk_weather_setup_manual_coords:
    n 1ulraj "So,{w=0.3}{nw}"
    extend 1nnmbo " I'm going to need to know a few things to find out where you are."
    n 1flrss "Let's start off with the basics{w=0.1} -{w=0.5}{nw}"
    extend 1fchsm " Hemispheres!"
    n 1unmaj "Do you live in the {b}Northern{/b} or {b}Southern{/b} Hemisphere?"
    n 1nllss "Just in case you didn't know,{w=0.1} it basically just means if you live {b}North{/b} or {b}South{/b} of the {b}equator{/b}."
    n 1nllaj "So..."
    show natsuki 1tsqsm at jn_center
    menu:
        n "Which do you live in,{w=0.1} [player]?"
        "The Northern Hemisphere.":

            $ player_in_southern_hemisphere = False
            $ persistent.hemisphere_north_south = "North"

            n 1unmaj "The Northern Hemisphere?{w=1}{nw}"
            extend 1flrbg " Well hey!{w=1}{nw}"
            extend 1fchbg " Just like me!"
        "The Southern Hemisphere.":

            $ player_in_southern_hemisphere = True
            $ persistent.hemisphere_north_south = "South"

            n 1unmaj "The Southern Hemisphere?{w=1}{nw}"
            extend 1fchbg " Gotcha!"

    n 1uchbg "Okay,{w=0.1} now time for the other two!"
    n 1tnmss "Do you live in the {b}Eastern{/b} or {b}Western{/b} Hemisphere?"
    n 1ulraj "This one's a little more tricky,{w=0.1} but I find it helps to think of it this way:"
    n 1nnmbo "If we took a world map and cut it in half {b}vertically{/b} down the middle..."
    show natsuki 1unmaj at jn_center
    menu:
        n "Would you live in the {b}Eastern half{/b},{w=0.1} or the {b}Western half{/b}?"
        "The Eastern half.":

            $ player_in_western_hemisphere = False
            $ persistent._jn_hemisphere_east_west = "East"

            if not player_in_southern_hemisphere:
                n 1unmbg "Wow!{w=1}{nw}"
                extend 1fchbg " Just like me again,{w=0.1} [player]!"
                n 1tslss "It really is a small world,{w=0.1} huh?"
            else:

                n 1fchbg "Well hey!{w=0.5} Just like me!"
        "The Western half.":

            $ player_in_western_hemisphere = True
            $ persistent._jn_hemisphere_east_west = "West"

            n 1fchbg "The Western half.{w=0.5} Gotcha!"


    n 1fllss "Now with that out of the way,{w=0.1} I just need your coordinates!"
    n 1fsqss "And by those,{w=0.5}{nw}"
    extend 1fchsm " I mean your {b}latitude{/b} and {b}longitude{/b}!"
    n 1ullaj "I always used {a=[store.jn_globals.LINK_LAT_LONG_HOME]}this{/a} website to look mine up for homework,{w=0.1} but you can use your phone or whatever too."
    n 1unmaj "Oh,{w=0.3}{nw}"
    extend 1fnmbo " and don't worry about making it positive or negative.{w=1}{nw}"
    extend 1fcssm " I'll take care of that!"
    n 1ullss "We'll start off with your {b}latitude{/b} first."
    n 1fchsm "So...{w=0.3} take it away!"
    $ player_latitude = renpy.input(prompt="Enter your {b}latitude{/b}:", allow="0123456789.")


    n 1fchbg "Alright!{w=0.5}{nw}"
    extend 1nchsm " Now finally,{w=0.1} I just need your {b}longitude{/b}!"
    n 1fcssm "Just like last time,{w=0.1} I can figure it out without any positive or negative symbols."
    n 1fchsm "Take it away,{w=0.1} [player]!"
    $ player_longitude = renpy.input("Enter your {b}longitude{/b}:", allow="0123456789.")


    python:
        if player_in_southern_hemisphere:
            player_latitude = "-" + player_latitude

        if player_in_western_hemisphere:
            player_longitude = "-" + player_longitude

        player_latitude = float(player_latitude)
        player_longitude = float(player_longitude)

    n 1fcssm "'Kay!"
    extend 1fchsm " I think we're nearly there now,{w=0.1} [player]!"
    extend 1fcsbg " Let me just open up a map real quick...{w=1}{nw}"

    python:

        show_map_success = False
        try:
            jn_open_google_maps(player_latitude, player_longitude)
            show_map_success = True

        except Exception as exception:
            store.jn_utils.log(exception.message, store.jn_utils.SEVERITY_ERR)

    if show_map_success:
        n 1uchgn "Ta-da!"
        n 1fnmbg "How about it,{w=0.1} [player]?{w=1}{nw}"

        menu:
            n "Close enough,{w=0.1} right?"
            "Yes, that's close enough.":

                n 1fchbg "Finally!{w=1}{nw}"
                extend 1nchsm " I'll just note all that down real quick..."

                $ persistent._jn_player_latitude_longitude = (player_latitude, player_longitude)
                jump talk_weather_setup_verify
            "No, that's not right at all.":

                n 1tnmem "What?{w=0.2} Really?!"
                n 1fcsem "Ugh..."
                n 1fcsaj "Let's...{0.5} try again,{w=0.1} alright?{w=1}{nw}"
                extend 1fnmpo " I really wanna get this working!"

                jump talk_weather_setup_manual_coords
    else:

        n 1fllaj "Urgh...{w=0.3} really?{w=0.2} This is {i}such{/i} a pain!"
        n 1nlrsl "I can't seem to show you where I think you are on a map,{w=0.1} so I'll just ask to make sure."
        n 1nnmss "I've done some checks to work out the coordinates,{w=0.1} and from what you said..."
        n 1nnmaj "Your overall latitude would be [player_latitude],{w=0.1} and your overall longitude would be [player_longitude]."
        menu:
            n "Is [player_latitude], [player_longitude] correct?"
            "Yes, that's right.":

                n 1fcsem "Finally!{w=1}{nw}"
                extend 1kslpo " Jeez..."

                $ persistent._jn_player_latitude_longitude = (player_latitude, player_longitude)
                jump talk_weather_setup_verify
            "No, that's still not right.":

                n 1tnmem "What?{w=0.2} Really?!"
                n 1fcsem "Ugh..."
                n 1fcsaj "Let's...{0.5} try again,{w=0.1} alright?{w=1}{nw}"
                extend 1fnmpo " I really wanna get this working!"

                jump talk_weather_setup_manual_coords
            "Nevermind.":

                n 1fllpo "Jeez...{w=1}{nw}"
                extend 1tlrss " what a mess,{w=0.1} huh?"
                n 1fcspo "..."
                n 1nllaj "Well,{w=0.1} thanks anyway.{w=1}{nw}"
                extend 1nnmaj " We can always try again later,{w=0.5}{nw}"
                extend 1tnmss " right?"

                jump ch30_loop

label talk_weather_setup_verify:
    n 1nchbg "Okaaay!{w=1}{nw}"
    extend 1fnmsm " I think we're almost done now,{w=0.1} [player]!"
    n 1ncsbo "Let me just check everything is in order here...{w=1.5}{nw}"

    if jn_atmosphere.getWeatherFromApi():
        n 1fchbg "Yes!"
        extend 1uchbs " It's working,{w=0.5} it's working!{w=1}{nw}"
        extend 1nchsml " Ehehe."
        n 1nchbgl "Thanks a bunch,{w=0.1} [player]!{w=1}{nw}"
        extend 1uchgnledz " This is gonna be {i}super{/i} awesome!"
        $ Natsuki.calculatedAffinityGain()

        python:
            persistent._jn_weather_api_configured = True
            persistent._jn_weather_setting = int(jn_preferences.weather.JNWeatherSettings.real_time)
            jn_atmosphere.updateSky()
    else:

        n 1fcsaj "Oh,{w=0.5}{nw}"
        extend 1fllan " come {i}on!{/i}"
        n 1fcsem "Ugh..."
        n 1fslem "And I was so stoked about it,{w=0.1} too..."
        n 1fcsem "I'm sorry,{w=0.1} [player].{w=1}{nw}"
        extend 1knmemsbl " I can't get it all to work!"
        n 1fsrem "Talk about a disappointment..."
        n 1nsrposbl "..."
        n 1unmgsesu "Ah!{w=0.5}{nw}"
        extend 1fnmgs " I just thought of something!"
        n 1tnmpueqm "Did you have to make a new account for OpenWeatherMap,{w=0.2} [player]?{w=0.75}{nw}"
        extend 1tslbo " Or like,{w=0.2} did you make a new API key?"
        n 1tnmss "I...{w=1}{nw}"
        extend 1fsrdvsbr " kinda spaced out a little when you told me before.{w=0.75}{nw}"
        extend 1nlrajsbr " So..."
        show natsuki 1tnmslsbr at jn_center

        menu:
            n "Do you remember?{w=0.3} Like,{w=0.2} at all?"
            "I created a new account.":

                $ new_account_or_key = True
            "I created a new API key.":

                $ new_account_or_key = True
            "I already had an account, and used an existing API key.":

                $ new_account_or_key = False
                n 1tslpusbr "...Huh."
                n 1tslsr "I'm...{w=0.75}{nw}"
                extend 1kcsemesisbl " kinda stumped then,{w=0.2} actually."
                n 1tsrsl "I mean..."
                n 1tnmpueqm "Maybe you just gave me the wrong key...?"
                extend 1fchbgsbl " Or your internet just isn't feeling it today?"
                n 1nslsssbl "I don't know."
                n 1fllsssbl "Just...{w=0.5}{nw}"
                extend 1knmsssbr " let me know when if you wanna try again,{w=0.2} 'kay?"
                n 1knmcaesssbr "It'll be awesome!{w=0.5}{nw}"
                extend 1knmpolesssbr " I-{w=0.3}I promise!"

        if new_account_or_key:
            n 1tslbo "So you did,{w=0.2} huh..."
            n 1fslpuesp "..."
            n 1unmgsesu "Oh!{w=0.5}{nw}"
            extend 1fsrdvsbl " Right!"
            n 1fsrsssbl "I forgot to say..."
            n 1fsldvsbr "It might take a day or so for your API key to actually {i}activate{/i} so I can use it..."
            n 1kchsssbr "Ehehe.{w=0.5}{nw}"
            extend 1fchblsbl " Oops!"
            n 1fllsssbl "Just...{w=0.5}{nw}"
            extend 1knmsssbr " let me know when you wanna try again,{w=0.2} 'kay?"
            n 1fnmcasbr "I really wanna get this all working!"
            n 1fcstr "Because when I do,{w=0.2} you bet it's gonna be{w=0.3}{nw}"
            extend 1fspgsledz " {i}awesome{/i}!"

    jump ch30_loop


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_favourite_season",
            unlocked=True,
            prompt="What's your favourite season?",
            category=["Weather", "Nature"],
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )
label talk_favourite_season:
    n 1unmbo "Huh?{w=0.2} My favourite season?"


    if not persistent.jn_player_favourite_season:
        n 1tllss "That's a little random,{w=0.1} isn't it?"
        n 1tnmss "Well...{w=0.3} anyway.{w=0.3}{nw}"
        extend 1fnmaw " Tough question, [player]!"
        n 1fsrsl "I think if I had to pick..."
        n 1fchts "It'd be summer!{w=0.2} Duh!"
        n 1fsqss "Why?{w=0.5}{nw}"
        extend 1fchgn " Just think about it,{w=0.1} [player]!"
        n 1ullbg "Long trips to the beach...{w=0.5}{nw}"
        extend 1ncssm " ice cream in the shade...{w=0.5}{nw}"
        extend 1ksrss " lazy evening walks to the shops..."
        n 1flleml "I-{w=0.1}I mean,{w=0.3}{nw}"
        extend 1fllbgl " what's not to love?"
        n 1fchbg "I can just enjoy life out there without having to worry about the weather!"
        n 1usqsg "I don't think I need to make my case any more clear,{w=0.1} do I?{w=0.5}{nw}"
        extend 1uchsm " Ahaha."
        n 1unmaj "Although...{w=0.3} what about you,{w=0.1} [player]?"
        menu:
            n "What's your favourite season?"
            "Spring":

                n 1fnmss "Oh?{w=0.2} Spring,{w=0.1} huh?"
                n 1tllsr "Hmmm..."
                n 1unmss "I mean,{w=0.1} I kinda get it.{w=0.2} It's the sign winter finally got lost,{w=0.1} right?"
                n 1ulrss "And I suppose the flowers blooming again is kinda cool to see."
                n 1fsqan "But the rain!{w=0.2} Jeez!{w=0.5}{nw}"
                extend 1fcspu " It just never stops!"
                n 1fllpo "Roll on summer,{w=0.1} I say."

                $ persistent.jn_player_favourite_season = "Spring"
            "Summer":

                n 1fsgbg "Aha!{w=0.2} I knew it!"
                n 1fsqbg "Nobody can resist some fun in the sun,{w=0.1} am I right?"
                n 1fnmbg "I'm glad we both agree,{w=0.1} [player].{w=0.5}{nw}"
                extend 1fchsm " Ehehe."

                $ persistent.jn_player_favourite_season = "Summer"
            "Autumn":

                n 1unmaj "Autumn?{w=0.5}{nw}"
                extend 1nllaj " Not a bad choice,{w=0.1} actually!"
                n 1ullsm "I like when it's still warm enough in the day to go out and do things..."
                n 1ucsss "But you also get that crisp,{w=0.1} fresh morning air to wake you up."
                n 1ullaj "The falling leaves are super pretty too."
                n 1fcsan "It's just...{w=0.5}{nw}"
                extend 1fsrsr " it's all ruined when the rain comes,{w=0.1} you know?"
                n 1fsqsr "Trudging through all those sloppy leaves is just gross.{w=0.5}{nw}"
                extend 1fcssf " No thanks!"

                $ persistent.jn_player_favourite_season = "Autumn"
            "Winter":

                n 1tnmsf "Huh?{w=0.2} Really?"
                n 1tnmaj "Winter is the last thing I expected you to say,{w=0.1} [player]!"
                n 1tlrbo "Though...{w=0.3} I get it, kinda."
                n 1fcsbg "It's the perfect time of year to get super snug and spend some quality reading time!"
                n 1fslss "Especially since there's not much you can do outside,{w=0.1} anyway."

                $ persistent.jn_player_favourite_season = "Winter"
    else:


        n 1tllbo "Hang on...{w=0.5}{nw}"
        extend 1tnmss " didn't we talk about this before,{w=0.1} [player]?"
        n 1nlrpu "Well,{w=0.1} anyway..."
        n 1ucsbg "I still love summer,{w=0.1} as you know{w=0.1} -{w=0.3}{nw}"
        extend 1fcsbg " and nothing's gonna change that any time soon!"
        n 1tsqsg "What about you,{w=0.1} [player]?"
        menu:
            n "Still rooting for [persistent.jn_player_favourite_season]?"
            "Yes.":
                n 1fcsbg "Ehehe.{w=0.2} I thought as much,{w=0.1} [player]."

                if persistent.jn_player_favourite_season == "Summer":
                    n 1uchbg "You already picked the best season,{w=0.1} after all!"
                else:

                    n 1fllss "Well...{w=0.3} I'm afraid you're not gonna sway me!{w=0.5}{nw}"
                    extend 1uchbg " Ahaha!"
            "No.":

                n 1tsgbg "Oh?{w=0.2} Changed our mind,{w=0.1} have we?"
                n 1tsqss "Well?{w=0.5}{nw}"
                extend 1fchbg " Tell me then,{w=0.1} [player]!"
                menu:
                    n "What's your favourite season?"
                    "Spring":

                        $ new_favourite_season = "Spring"
                    "Summer":

                        $ new_favourite_season = "Summer"
                    "Autumn":

                        $ new_favourite_season = "Autumn"
                    "Winter":

                        $ new_favourite_season = "Winter"

                $ season_preference_changed = False
                if persistent.jn_player_favourite_season == new_favourite_season:
                    n 1fnmgs "Hey!{w=0.2} [player]!"
                    n 1fsqpo "I thought you said you'd changed your mind?"
                    n 1fllem "You haven't changed your mind at all!{w=0.2} You said [persistent.jn_player_favourite_season] last time,{w=0.1} too!"
                    $ chosen_tease = jn_utils.getRandomTease()
                    n 1fcsem "Jeez...{w=0.5}{nw}"
                    extend 1fnmpo " you're such a wind-up sometimes,{w=0.1} [chosen_tease]!"

                    if Natsuki.isAffectionate(higher=True):
                        n 1flrpol "N-{w=0.1}not that I {i}dislike{/i} that side of you,{w=0.1} o-{w=0.1}or anything."
                    else:

                        n 1fsqsm "But...{w=0.3} I think I can {i}weather{/i} it."
                        n 1fsrss "For now."
                else:

                    $ persistent.jn_player_favourite_season = new_favourite_season
                    $ season_preference_changed = True

                if season_preference_changed and persistent.jn_player_favourite_season == "Spring":
                    n 1usqss "Ooh?{w=0.2} Favouring Spring now,{w=0.1} [player]?"
                    n 1nlrbo "I could do without all the rain,{w=0.1} but I get it."
                    n 1flrpu "Hmm...{w=0.3} Spring..."
                    n 1tlrbo "I wonder...{w=0.5}{nw}"
                    extend 1tnmss " do you grow anything,{w=0.1} [player]?"
                    n 1fchsm "Ahaha."

                elif season_preference_changed and persistent.jn_player_favourite_season == "Summer":
                    n 1fchbs "Aha!{w=0.2} See?"
                    n 1fsqbs "You knew I was right all along,{w=0.1} didn't you?"
                    n 1usqsg "Don't even try to deny it,{w=0.1} [player].{w=0.5}{nw}"
                    extend 1fchbg " Summer is the best!"
                    n 1uchsm "I'm just glad you came around.{w=0.2} That's the important thing!"

                elif season_preference_changed and persistent.jn_player_favourite_season == "Autumn":
                    n 1usqsm "Oh?{w=0.2} You've taken the {i}fall{/i} for Autumn,{w=0.1} have you?"
                    n 1fchsm "Ehehe."
                    n 1ullss "I'll admit,{w=0.1} it's a pretty season,{w=0.1} with all the golden leaves and stuff..."
                    n 1nslss "So long as the weather stays warm,{w=0.1} anyway."

                elif season_preference_changed and persistent.jn_player_favourite_season == "Winter":
                    n 1tllss "Winter,{w=0.1} huh?{w=0.2} I wasn't expecting that."
                    n 1tnmbo "Do you prefer being indoors now or something,{w=0.1} [player]?"
                    n 1flrss "Well,{w=0.1} if you prefer being all cosy inside..."
                    n 1fsqsm "Then you better not be slacking on your reading,{w=0.1} [player]!{w=0.5}{nw}"
                    extend 1fchsm " Ehehe."




    python:
        spring_sweater = jn_outfits.get_wearable("jn_clothes_bee_off_shoulder_sweater")
        summer_sweater = jn_outfits.get_wearable("jn_clothes_creamsicle_off_shoulder_sweater")
        autumn_sweater = jn_outfits.get_wearable("jn_clothes_autumn_off_shoulder_sweater")
        winter_sweater = jn_outfits.get_wearable("jn_clothes_nightbloom_off_shoulder_sweater")

    if (
        (
            not spring_sweater.unlocked
            or not summer_sweater.unlocked
            or not autumn_sweater.unlocked
            or not winter_sweater.unlocked
        )
        and Natsuki.isHappy(higher=True) 
        and persistent.jn_custom_outfits_unlocked
    ):
        n 1flrpu "..."
        n 1ulraj "Actually,{w=0.3}{nw}"
        extend 1fnmss " you know what?"
        n 1fcsss "Give me a sec here.{w=0.75}{nw}"
        extend 1uchgnl " I've got {i}just{/i} the thing!{w=1}{nw}"

        show black zorder 4 with Dissolve(0.5)
        $ jnPause(1)
        play audio zipper
        $ jnPause(2)

        python:
            import copy

            spring_sweater.unlock()
            summer_sweater.unlock()
            autumn_sweater.unlock()
            winter_sweater.unlock()
            temporary_outfit = copy.copy(jn_outfits.get_outfit(Natsuki.getOutfitName()))

            if persistent.jn_player_favourite_season == "Spring":
                temporary_outfit.clothes = spring_sweater

            elif persistent.jn_player_favourite_season == "Summer":
                temporary_outfit.clothes = summer_sweater

            elif persistent.jn_player_favourite_season == "Autumn":
                temporary_outfit.clothes = autumn_sweater

            else:
                temporary_outfit.clothes = winter_sweater

            jn_outfits.save_temporary_outfit(temporary_outfit)

        play audio clothing_ruffle
        $ jnPause(2)
        play audio zipper
        $ jnPause(1)
        show natsuki 1fsqsm at jn_center
        hide black with Dissolve(1.25)

        n 1fsqsm "..."
        n 1tsqssl "...Well,{w=0.2} [player]?{w=1}{nw}"
        extend 1tcsssl " You gotta admit..."
        n 1fsqss "Whatever your preference?"
        n 1fcsbgedz "My fashion is {i}always{/i} in-season."
        n 1fchsml "Ehehe."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_time_management",
            unlocked=True,
            prompt="Time management",
            category=["Life"],
            nat_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_time_management:
    n 1ullaj "Hey,{w=0.1} [player]..."
    n 1unmaj "Do you have off days sometimes?{w=0.2} Where you struggle to get anything done?"
    n 1flrpo "Or you just get distracted super easily?"
    n 1unmbo "To be honest?{nw}"
    extend 1fllss "{w=0.2} I struggled with that for a while.{nw}"
    extend 1fbkwr "{w=0.2} Especially when things like assignments are so boring!"
    n 1nllaj "But...{w=0.5}{nw}"
    extend 1fllbg " I figured out a way of managing that{w=0.1} -{w=0.1} and you should know it too,{w=0.1} [player]!"
    n 1fchbg "Time boxing!"
    n 1nsqpo "And no,{w=0.1} it's not as literal as it sounds."
    n 1nnmaj "The idea is that you set aside a period during the day you want to work{w=0.1} -{w=0.1} like the school day,{w=0.1} or a few hours in the evening."
    n 1fnmbg "Then for each hour in that period,{w=0.1} you split it!"
    n 1ulraj "So for any given hour,{w=0.1} you spend most of that working,{w=0.1} and the remainder on some kind of break."
    n 1unmss "The idea is that it becomes way easier to stay focused and motivated since you always have a breather coming up."
    n 1uchsm "Personally,{w=0.1} I find a 50/10 split works best for me."
    n 1nllbo "So I spend 50 minutes of each hour studying,{w=0.3}{nw}"
    extend 1uchsm " and 10 minutes doing whatever I want."
    n 1usqbg "You'd be surprised how much manga time I can sneak in!"
    n 1unmaj "Don't just take my schedule as a rule though.{w=0.5}{nw}"
    extend 1fchbg " Find a balance that works for you, [player]!"
    n 1fslbg "Though I should remind you...{w=0.3} the key word here is {i}balance{/i}."
    n 1fsqsr "I'm not gonna be impressed if you work too much...{w=0.5}{nw}"
    extend 1fnmpo " Or just slack off!"
    if Natsuki.isAffectionate(higher=True):
        n 1ullbo "Although...{w=0.3} now that I think about it..."
        n 1tsqsm "Perhaps I should timebox our time together,{w=0.1} [player]."
        extend 1uchbselg " Ahaha!"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_sweet_tooth",
            unlocked=True,
            prompt="Do you have a sweet tooth?",
            category=["Health", "Food"],
            player_says=True,
            affinity_range=(jn_affinity.DISTRESSED, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_sweet_tooth:
    n 1unmbo "Huh?{w=0.2} Do I have a sweet tooth?"


    if Natsuki.isAffectionate(higher=True):
        n 1fspbg "You bet I do!"
        n 1nsqts "What else were you expecting,{w=0.1} [player]?"
        extend 1fchsm "{w=0.2} Ehehe."

    elif Natsuki.isNormal(higher=True):
        n 1fllss "Well,{w=0.1} yeah.{w=0.2} Of course I do!"
    else:

        n 1nnmsl "Well...{w=0.3} yeah.{w=0.2} Why wouldn't I?"

    n 1nllaj "Baked stuff is okay,{w=0.1} but I find it gets kinda sickly before long."
    n 1ullaj "But to be completely honest,{w=0.1} if I had a choice?{w=0.5}{nw}"
    extend 1unmbo " Just give me a bunch of candy every time."

    if Natsuki.isNormal(higher=True):
        n 1uwdaj "There's so much more variety!{w=0.2} Like...{w=0.3} there's always something for whatever I feel like!"
        n 1tllss "I think if I had to pick a favourite though,{w=0.3}{nw}"
        extend 1fllss " it'd be those fizzy ones."
        n 1fchbg "Just that perfect mix of sweet and sour,{w=0.1} you know?"
        n 1flraj "Jeez...{w=0.5}{nw}"
        extend 1fchts " I can feel my tongue tingling already just thinking about them!"
        n 1fsrts "..."
        n 1flleml "A-{w=0.1}anyway!"
        n 1fcseml "It isn't like I'm snacking on treats all the time though."
        n 1fllpo "I've got way better things to spend my money on."
        n 1fnmss "And...{w=0.3} it's not exactly healthy either.{w=0.5}{nw}"
        extend 1fchsm " Ahaha."


    if Natsuki.isAffectionate(higher=True):
        n 1fsqsm "Though I have to say,{w=0.1} [player]."
        n 1fsqssl "I'm pretty sure you have a sweet tooth too."
        n 1fsrbgl "It'd explain why you're spending so much time with me,{w=0.1} a-{w=0.1}after all."
        n 1fchbgl "Ahaha!"

    elif Natsuki.isNormal(higher=True):
        n 1fllbg "I could go for some candy right now,{w=0.1} actually.{w=0.5}{nw}"
        extend 1fslss " But...{w=0.3} I think I'll hold back."
        n 1usqbg "Someone's gotta be a role model to you,{w=0.1} [player].{w=0.2} Am I right?"
        n 1fchsm "Ehehe."
    else:

        n 1nnmbo "..."
        n 1nlrbo "That being said..."
        n 1flrsr "I...{w=0.3} could really use some chocolate right now."
        n 1fsqsr "I'll let {i}you{/i} figure out why,{w=0.1} [player]."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_player_appearance",
            unlocked=True,
            prompt="My appearance",
            category=["You"],
            player_says=True,
            affinity_range=(jn_affinity.ENAMORED, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_player_appearance:

    if persistent.jn_player_appearance_declined_share:
        n 1unmaj "Huh?{w=0.2} Your appearance?"
        n 1ullaj "If I remember,{w=0.1} [player]{w=0.1} -{w=0.3}{nw}"
        extend 1tnmbo " you said didn't want to share it with me before."
        n 1tlrbo "Huh. Well..."
        menu:
            n "Did you change your mind,{w=0.1} [player]?"
            "Yes, I want to share my appearance.":

                n 1fcsbg "A-{w=0.1}aha!{w=0.2} I knew you'd come around eventually,{w=0.1} [player].{nw}"
                extend 1fchgn "{w=0.2} Let's not waste any time!"
            "No, I still don't want to share my appearance.":

                n 1nllsl "Oh..."
                n 1unmaj "Well,{w=0.1} it's your call,{w=0.1} [player]."
                n 1unmss "Just let me know if you change your mind again,{w=0.1} alright?"
                return


    elif persistent.jn_player_appearance_eye_colour is not None:
        n 1unmaj "Huh?{w=0.2} Your appearance?"
        n 1tllbo "But...{w=0.3} I was sure you already shared that with me,{w=0.1} [player]."
        n 1uspgs "Ooh!{w=0.5}{nw}"
        extend 1unmbg " Did you dye your hair or something?"
        n 1fllbg "Or...{w=0.3} maybe you just made a mistake last time?"
        n 1tslbg "Well...{w=0.5}{nw}"
        extend 1unmbg " either way."
        menu:
            n "Did you want to share your appearance again,{w=0.1} [player]?"
            "Yes, my appearance has changed.":

                n 1fcssm "Aha!{w=0.2} I thought so!"
                n 1fchgn "I can't wait to find out how!"
            "No, my appearance hasn't changed.":

                n 1tnmsr "H-{w=0.1}huh?{w=0.2} Just pulling my leg,{w=0.1} are you?"
                n 1tsrsf "Okaaay..."
                n 1tnmss "Just let me know if you actually {i}do{/i} change something then,{w=0.2} 'kay?"
                return
    else:


        n 1tlrbo "Huh..."
        n 1tnmbo "You know,{w=0.1} [player].{w=0.2} I just realized something."
        n 1unmaj "You've seen a lot of me,{w=0.1} right?{w=0.5}{nw}"
        extend 1fslssl " B-{w=0.1}by spending time with me here,{w=0.1} I mean."
        n 1ullaj "So...{w=0.3} you kinda know exactly who you're dealing with."
        n 1uwdgs "But I don't have a clue about who {i}I'm{/i} dealing with!"
        n 1fsqsm "And honestly?{w=0.2} You should know me by now.{w=0.5}{nw}"
        extend 1fsqbg " I'm actually pretty curious!"
        n 1nchbg "Don't worry though{w=0.1} -{w=0.1} anything you tell me is staying strictly between us,{w=0.1} obviously!"
        n 1fllsfl "N-{w=0.1}not like anyone else would care {i}that{/i} much,{w=0.1} anyway."
        n 1unmsm "So...{w=0.3} how about it, [player]?"
        menu:
            n "Do you wanna share your appearance with me, [player]?"
            "Sure!":

                n 1uchbsl "Yes!{w=0.5}{nw}"
                extend 1fcsbgl " I-{w=0.1}I mean good!{w=0.5}{nw}"
                n 1fchbg "Let's get started then,{w=0.1} shall we?"
            "I'm not comfortable sharing that.":

                n 1unmsl "Oh..."
                n 1ullaj "That's kind of disappointing to hear,{w=0.1} if I'm being honest."
                n 1nchss "But I totally get it,{w=0.1} [player].{w=0.2} So don't worry,{w=0.1} 'kay?"
                n 1fsqss "You better let me know if you feel like telling me later though!"
                $ persistent.jn_player_appearance_declined_share = True
                return

    n 1uchgn "Okaaay!{w=0.2} Let's start with...{w=0.5}{nw}"
    extend 1fchbg " your eyes!"
    n 1unmbg "They say the eyes are the window to the soul,{w=0.1} so it only makes sense to begin there,{w=0.1} right?"
    n 1flldvl "..."
    n 1fcseml "A-{w=0.1}anyway...!"


    menu:
        n "How would you describe your eye colour,{w=0.1} [player]?"
        "Amber":

            n 1unmaj "Ooh!{w=0.2} I don't think I've seen someone with amber eyes before."
            n 1fchbg "That's awesome,{w=0.1} [player]!{w=0.2} I bet those help you stand out,{w=0.1} right?"
            $ persistent.jn_player_appearance_eye_colour = "Amber"
        "Blue":

            n 1unmbg "Blue eyes,{w=0.1} huh?{w=0.2} Cool!"
            n 1fsgsm "I really like how striking they are!"
            $ persistent.jn_player_appearance_eye_colour = "Blue"
        "Brown":

            n 1unmaj "Brown eyes,{w=0.1} huh?{w=0.5}{nw}"
            extend 1fchsm " I'm not complaining!"
            n 1tsqss "Nice and natural,{w=0.1} am I right?{w=0.5}{nw}"
            extend 1uchsm " Ahaha."
            $ persistent.jn_player_appearance_eye_colour = "Brown"
        "Grey":

            n 1unmaj "Oh?{w=0.2} Grey eyes?{w=0.2} Super neat, [player]!"
            n 1tllss "I don't think I've seen anyone with grey eyes before!"
            $ persistent.jn_player_appearance_eye_colour = "Grey"
        "Green":

            n 1fsgbg "Aha!{w=0.2} I had you figured for green eyes,{w=0.1} [player]."
            n 1fsqbg "I bet you're proud of them,{w=0.1} no?{w=0.5}{nw}"
            extend 1uchsm " Ehehe."
            $ persistent.jn_player_appearance_eye_colour = "Green"
        "Hazel":

            n 1unmaj "Ooh!{w=0.2} Hazel,{w=0.1} huh?{w=0.5}{nw}"
            extend 1fsqbg " Classy!"
            n 1tslsm "Hmm...{w=0.3} I wonder if yours are closer to green or brown,{w=0.1} [player]?"
            $ persistent.jn_player_appearance_eye_colour = "Hazel"
        "Mixed":

            n 1unmaj "Wow!{w=0.2} Do you have two different colours or something,{w=0.1} [player]?"
            n 1fchbg "Now if that isn't unique,{w=0.1} I don't know what is!"
            $ persistent.jn_player_appearance_eye_colour = "Mixed"
        "Other":

            n 1unmaj "Oh?{w=0.2} Something a bit off the beaten trail,{w=0.1} huh?"
            n 1tlrss "...Or maybe you just wear contacts a lot?{w=0.5}{nw}"
            extend 1unmsg " Well,{w=0.1} whatever."
            n 1ncsss "I'm sure they look fine either way."
            $ persistent.jn_player_appearance_eye_colour = "Other"

    n 1uchbg "Alright!{w=0.2} That's one down!"
    n 1ullaj "So next,{w=0.1} we have...{w=0.5}{nw}"
    extend 1fchsm " your hair,{w=0.1} of course!"
    n 1nnmsm "We'll just start off with the length for now."
    n 1ullss "Now..."


    menu:
        n "How would you describe your hair length,{w=0.1} [player]?"
        "Short.":

            n 1ncsss "Ah,{w=0.1} the low maintenance approach{w=0.1} -{w=0.1} I see,{w=0.1} I see.{w=0.5}{nw}"
            extend 1fchbg " Trendy!"
            n 1unmaj "To be honest though,{w=0.1} I totally get it."
            n 1fslpo "I have no idea how you even keep long hair looking good..."
            n 1nslpo "It just seems like way too much effort to me."
            $ persistent.jn_player_appearance_hair_length = "Short"
        "Mid-length.":

            n 1fcsbg "Aha!{w=0.2} The perfect balance,{w=0.1} am I right?"
            n 1fllss "Just long enough for pretty much any style..."
            n 1fchgn "And yet still short enough to suit a lazy day!{w=0.5}{nw}"
            extend 1nchsm " Ehehe."
            n 1flrbgl "I'm glad we think the same way,{w=0.1} [player]!"
            $ persistent.jn_player_appearance_hair_length = "Mid-length"
        "Long.":

            n 1unmbg "Ooh!{w=0.2} Letting it run free,{w=0.1} are we?"
            n 1fcssm "I bet you take super good care of yours."
            n 1fsqsm "I might even have to borrow your products,{w=0.1} [player].{w=0.5}{nw}"
            extend 1nchsm " Ehehe!"
            $ persistent.jn_player_appearance_hair_length = "Long"
        "I don't have any hair.":

            n 1fnmaj "Hey{w=0.1} -{w=0.1} nothing wrong with that!{nw}"
            extend 1fsqbg "{w=0.2} You wanna know why?"
            n 1fchgn "Because it just means you're aerodynamic,{w=0.1} [player].{w=0.5}{nw}"
            extend 1uchsmelg " Ahaha!"
            $ persistent.jn_player_appearance_hair_length = "None"

    n 1uchbs "Okay!{w=0.5}{nw}"
    extend 1unmbg " I'm really starting to get a picture now."
    n 1fwdgs "We gotta keep the ball rolling,{w=0.1} [player]!"


    if persistent.jn_player_appearance_hair_length == "None":
        n 1fllss "You said you didn't have any hair,{w=0.1} right?{w=0.5}{nw}"
        extend 1fllbg " So I think it's kinda pointless talking about hair colour."
        n 1fslbo "Now,{w=0.1} let's see...{w=0.3} what else..."
    else:

        n 1fchsm "Now for your hair colour!"
        n 1unmbg "So,{w=0.1} [player]..."
        menu:
            n "How would you describe your hair colour?"
            "Auburn":

                n 1unmaw "Ooh!{w=0.2} Auburn,{w=0.1} huh?{w=0.5}{nw}"
                extend 1fwdaw " That's awesome,{w=0.1} [player]!"
                n 1fchbg "It's such a warm colour!"
                $ persistent.jn_player_appearance_hair_colour = "Auburn"
            "Black":

                n 1tsgsm "Black,{w=0.1} huh?{w=0.5}{nw}"
                extend 1nchgn " Nice!"
                n 1usqsg "I bet you feel super slick,{w=0.1} huh [player]?"
                $ persistent.jn_player_appearance_hair_colour = "Black"
            "Blond":

                n 1fnmbg "Aha!{w=0.2} A blond,{w=0.1} are we?{w=0.5}{nw}"
                extend 1fsqts " {w=0.3}...That explains a lot."
                n 1fchgnelg "Ahaha!"
                n 1uchbs "I'm kidding,{w=0.1} [player]!{w=0.2} I'm just kidding!"
                n 1fllbg "I'm actually a little jealous.{w=0.5}{nw}"
                extend 1fsqsm " Just a little."
                $ persistent.jn_player_appearance_hair_colour = "Blond"
            "Brown":

                n 1unmaj "Brown hair,{w=0.1} [player]?{w=0.5}{nw}"
                extend 1nchsm " I'm for it!"
                n 1nchsm "Not too subtle and not too striking,{w=0.1} you know?{w=0.2} It's just right!"
                $ persistent.jn_player_appearance_hair_colour = "Brown"
            "Grey":

                n 1unmaj "Ooh...{w=0.5}{nw}"
                extend 1ullaj " I gotta say...{w=0.5}{nw}"
                extend 1kllbg " I wasn't expecting that!"
                n 1fsqsr "I just hope that isn't from stress,{w=0.1} [player]..."
                n 1fllbg "...Or at least stress from me,{w=0.1} anyway.{w=0.5}{nw}"
                extend 1fchsm " Ehehe."
                $ persistent.jn_player_appearance_hair_colour = "Grey"
            "Red":

                n 1fchsm "Ehehe.{w=0.5}{nw}"
                extend 1usqsm " So you're a red head,{w=0.1} [player]?"
                n 1flrajl "Not that there's anything wrong with that,{w=0.1} o-{w=0.1}obviously!"
                n 1fchbg "I bet that gets you some attention,{w=0.1} huh?"
                n 1fsrpo "Better be the good kind,{w=0.1} though."
                $ persistent.jn_player_appearance_hair_colour = "Red"
            "White":

                n 1unmbg "White hair,{w=0.1} huh?{w=0.5}{nw}"
                extend 1uchsm " Neat!"
                $ persistent.jn_player_appearance_hair_colour = "White"
            "Other":

                n 1unmaj "Oh?{w=0.5}{nw}"
                extend 1fsqsm " It looks like we're more similar in taste than I thought!"
                n 1fsrss "Though I should probably clarify...{w=0.5}{nw}"
                extend 1uchgn " mine is all natural,{w=0.1} [player]!{w=0.2} Ahaha."
                $ persistent.jn_player_appearance_hair_colour = "Other"


    n 1unmbg "Alright!{w=0.2} I think I'm almost done interrogating you now,{w=0.1} [player]."
    n 1fsqsm "Ehehe."
    n 1flrsl "So...{w=0.3} don't tease me when I ask this,{w=0.1} but I gotta know."
    n 1ulrbo "Exactly..."

    $ player_input_valid = False
    while not player_input_valid:
        $ player_input = int(renpy.input(prompt="How tall are you in {i}centimeters{/i},{w=0.2} [player]?", allow="0123456789"))


        if player_input > 75 and player_input <= 300:
            $ player_input_valid = True
            $ persistent.jn_player_appearance_height_cm = player_input

            if player_input < 149:
                n 1unmgs "H-{w=0.1}huh?{w=0.2} Really?"
                n 1unmaj "You're even shorter than me?"
                n 1flldv "Well,{w=0.1} I wasn't expecting that!"
                n 1fnmbg "Don't worry,{w=0.1} [player].{w=0.2} We're both on the same side,{w=0.1} right?{w=0.5}{nw}"
                extend 1fchbg " Ehehe."

            elif player_input == 149:
                n 1unmgs "Seriously?{w=0.2} We're the same height?"
                n 1uchbg "That's amazing,{w=0.1} [player]!"

                if persistent.jn_player_appearance_hair_length = "Medium" and persistent.jn_player_appearance_hair_colour = "Other":
                    n 1fllbg "With the hair and everything too..."
                    n 1uchgn "It's like we're practically twins!"

            elif player_input > 149 and player_input < 166:
                n 1unmaj "Oh?{w=0.2} A little on the shorter side,{w=0.1} [player]?"
                n 1fcsss "Don't worry, don't worry!{w=0.5}{nw}"
                extend 1fllpo " I-{w=0.1}I'm not one to judge,{w=0.1} after all."

            elif player_input >= 166 and player_input < 200:
                n 1unmaj "About average height,{w=0.1} [player]?"
                n 1nchsm "No complaints from me!"

            elif player_input >= 200 and player_input < 250:
                n 1unmaj "Oh?{w=0.2} On the taller side [player],{w=0.1} are we?"
                n 1fllbg "I guess I know who to take shopping,{w=0.1} right?{w=0.5}{nw}"
                extend 1nchsm " Ehehe."
            else:

                n 1unmgs "W-{w=0.1}woah!{w=0.2} What the heck,{w=0.1} [player]?{w=0.2} Really?"
                n 1fbkwr "That's crazy tall!"
                n 1tlrem "Though...{w=0.3} actually...{w=0.5}{nw}"
                extend 1knmpo " I hope that isn't actually just inconvenient for you,{w=0.1} though."
        else:

            n 1fllpo "[player]...{w=0.3} please.{w=0.2} Take this seriously,{w=0.1} alright?"

    n 1uchsm "Okaaay!{w=0.2} I think that's everything."
    n 1unmbg "Thanks a bunch,{w=0.1} [player]!"
    n 1fllbg "I know it wasn't a lot,{w=0.3}{nw}"
    extend 1uchgn " but I feel like I know you so much better now!"

    if Natsuki.isLove(higher=True):
        n 1flldvl "You know,{w=0.1} [player]?{w=0.2} I can just picture it now."
        n 1fnmssl "Meeting you in person somewhere out there,{w=0.1} for the first time..."
        python:

            if persistent.jn_player_appearance_eye_colour == "Other":
                eye_colour_descriptor = "calm"

            else:
                eye_colour_descriptor = persistent.jn_player_appearance_eye_colour.lower()


            if persistent.jn_player_appearance_hair_colour == "Other":
                hair_colour_descriptor = "shiny"

            else:
                hair_colour_descriptor = persistent.jn_player_appearance_hair_colour.lower()


        if persistent.jn_player_appearance_hair_length != "None":
            $ hair_length_descriptor = persistent.jn_player_appearance_hair_length.lower()
            n 1fsqsml "Spotting your [hair_length_descriptor] [hair_colour_descriptor] hair in the distance and hunting you down..."
        else:

            n 1fsqsml "Spotting you in the distance and hunting you down..."


        if persistent.jn_player_appearance_height_cm < 149:
            n 1fllssl "Gazing down into your [eye_colour_descriptor] eyes..."

        elif persistent.jn_player_appearance_height_cm == 149:
            n 1fllssl "Gazing directly into your [eye_colour_descriptor] eyes..."

        elif persistent.jn_player_appearance_height_cm > 149:
            n 1fllssl "Gazing upwards into your [eye_colour_descriptor] eyes..."

        n 1fchunl "Uuuuuu..."
        n 1fsqunl "...{w=0.5}{nw}"
        extend 1fllajl " A-ahem!{w=0.2} Anyway..."
        $ chosen_endearment = jn_utils.getRandomEndearment()
        n 1kllsml "Really.{w=0.2} Thank you,{w=0.1} [chosen_endearment]."
        n 1kcsbgl "This seriously meant a lot to me."

    elif Natsuki.isEnamored():
        n 1fsldvl "...And now I know exactly who I should be watching out for."
        n 1fsqssl "So you better watch out,{w=0.1} [player]."
        n 1fcsbgl "Ehehe."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_drinking_alcohol",
            unlocked=True,
            prompt="Do you drink alcohol?",
            category=["Food", "Health"],
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_drinking_alcohol:
    n 1tnmss "Do I drink alcohol?"
    extend 1tllss " Well...{w=0.3} I can't say I've ever tried it."
    n 1nllsr "I just don't think it's something for me."
    n 1ullpu "That being said,{w=0.1} I knew people who {i}did{/i} drink it..."
    n 1kcspu "But...{w=0.3} I'd...{w=0.3} really rather not get into that,{w=0.1} [player]."
    n 1ncssr "Sorry."
    n 1tlrpu "..."
    n 1uwdajesu "Oh!{w=0.5}{nw}"
    extend 1fllss " That reminds me,{w=0.1} actually!"
    n 1fnmbg "I bet you didn't know,{w=0.1} but guess who just randomly brought some into the club one day?"
    n 1fchgn "...Yuri!"
    n 1tnmbg "Surprised?{w=0.5}{nw}"
    extend 1fcsss " I know,{w=0.1} right?"
    n 1tllss "I mean...{w=0.3} it was just completely out of the blue!"
    n 1uchbs "She just slipped it out from her bag like it was a book or something."
    n 1unmbo "It wasn't even just some random supermarket stuff either...{w=0.5}{nw}"
    extend 1uwdaj " it looked super expensive too!"
    n 1kllss "Honestly,{w=0.1} I couldn't help myself.{w=0.2} I just burst into laughter."
    n 1ullun "I think it was just how non-chalant she was being about it all,{w=0.1} really."
    n 1nnmsl "Monika didn't look impressed,{w=0.1} though..."
    n 1klrsl "And Sayori...{w=0.3} she just got really upset.{w=0.5}{nw}"
    extend 1klrpu " She was shouting and everything!"
    n 1kcspu "It looked like Yuri put a lot of thought into picking something out,{w=0.1} but she was just given a hard time over for it..."
    n 1kcssr "I mean...{w=0.5}{nw}"
    extend 1kllsr " I know we shouldn't have had it in there at all,{w=0.1} and Yuri should have known better."
    n 1fslsr "But she didn't deserve all of...{w=0.5}{nw}"
    extend 1kslsr " that."
    n 1kslaj "I think she was just trying to be nice,{w=0.1} you know?"
    n 1unmsr "It's all in the past now,{w=0.1} obviously.{w=0.5}{nw}"
    extend 1kslsr " But...{w=0.3} that doesn't mean I don't still feel bad about it sometimes."
    n 1kcssr "..."
    if Natsuki.isAffectionate(higher=True):
        n 1kllsr "Hey...{w=0.5}{nw}"
        extend 1knmpu " [player]?"
        n 1klrsr "Can you promise me something?"
        n 1fcssr "It's dumb,{w=0.1} but I don't care."
        n 1nnmsl "It doesn't really matter to me if you drink or not."
        n 1klrpu "But...{w=0.3} if you do?"
        n 1ksqsr "Please just take it all in moderation,{w=0.1} okay?"
        n 1kllsr "I've...{w=0.5}{nw}"
        extend 1fcsan " seen...{w=0.5}{nw}"
        extend 1fcssr " what it can do to people."
        n 1kslsr "...Firsthand."
        n 1ksqsl "You deserve better than that,{w=0.1} [player].{w=0.5}{nw}"
        extend 1kslun " You {i}are{/i} better than that."
        if Natsuki.isLove(higher=True):
            n 1kcsun "..."
            n 1ksqsml "I love you,{w=0.1} [player]."
            n 1fcssrl "I'm {w=0.3}{i}never{/i}{w=0.3} going to let a bottle get between us."
    else:

        n 1unmsr "Hey,{w=0.1} [player]?"
        n 1nllaj "I don't really care that much if you drink or not."
        n 1ncssr "Just...{w=0.3} go easy on the stuff."
        n 1flleml "B-{w=0.1}but only because I'm not gonna clean up after you!"
        n 1fllss "Ahaha..."
        n 1kllsr "..."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_driving",
            unlocked=True,
            prompt="Can you drive?",
            category=["Transport"],
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_driving:

    $ already_discussed_driving = get_topic("talk_driving").shown_count > 0 or get_topic("talk_are_you_into_cars").shown_count > 0
    $ chosen_tease = jn_utils.getRandomTease()

    if already_discussed_driving:
        n 1tnmboeqm "...Huh?{w=0.75}{nw}"
        extend 1tllsssbr " I already told you I can't drive,{w=0.2} [chosen_tease]!"
        n 1fchgnelg "I still don't have a license,{w=0.2} remember?"
        n 1tllaj "And even if I wanted to,{w=0.5}{nw}"
        extend 1nslposbl " I don't think I could afford it..."
    else:

        n 1fchdvesi "Pffft!{w=0.5}{nw}"
        extend 1uchbselg " Ahaha!"
        n 1fchgn "What kind of a question is that,{w=0.1} [player]?"
        n 1tllss "Of course I can't drive,{w=0.1} [chosen_tease]!{w=0.5}{nw}"
        extend 1fchgn " I don't even have a license!"
        n 1kllpo "I mean...{w=0.3} even if I wanted to learn,{w=0.1} I don't think I could afford it."

    n 1uskgs "Lessons are super expensive nowadays!"
    n 1fslem "And then there's tests,{w=0.1} insurance,{w=0.1} fuel,{w=0.1} parking...{w=0.5}{nw}"
    extend 1fsqaj " it's actually pretty gross how fast it all adds up."
    n 1nlraj "I think I'd rather stick to public transport and my own two feet."
    n 1unmaj "But what about you,{w=0.1} [player]?"
    show natsuki 1tnmss at jn_center


    if persistent.jn_player_can_drive is None:
        menu:
            n "Can you drive?"
            "Yes, and I do currently.":

                n 1uwdaj "Wow..."
                extend 1fsraj " ...{w=0.3}show-off."
                n 1fsqpo "..."
                n 1fchbg "Relax,{w=0.1} [player]!{w=0.2} Jeez!{w=0.5}{nw}"
                extend 1nchsm " I'm just messing with you."
                n 1unmbg "That's awesome though{w=0.1} -{w=0.1} you just can't beat the convenience of a car,{w=0.1} right?"

                if Natsuki.isAffectionate(higher=True):
                    n 1fllbg "But I should probably warn you..."
                    n 1fsgsm "I'm picking the songs for our driving playlist."
                    extend 1uchbgelg " Ahaha!"
                else:

                    n 1fllbg "Just remember,{w=0.1} [player]..."
                    n 1fsgsm "I call shotgun.{w=0.5}{nw}"

                $ persistent.jn_player_can_drive = True
                return
            "Yes, but I don't right now.":

                n 1unmaj "Oh?{w=0.2} Is something wrong with your car,{w=0.1} [player]?"
                n 1tllbo "Or perhaps...{w=0.3} you just don't own one at the moment?"
                n 1nnmsm "Well,{w=0.1} I'm not one to judge.{w=0.2} I'm sure you manage just fine."
                n 1flrss "Besides,{w=0.1} you're helping the environment too,{w=0.1} right?"

                if Natsuki.isAffectionate(higher=True):
                    n 1fsgsm "Thoughtful as always,{w=0.1} [player]."
                    extend 1nchsm " Ehehe."

                $ persistent.jn_player_can_drive = True
                return
            "No, I can't.":

                n 1klrsl "Oh..."
                n 1flrss "Well,{w=0.3}{nw}"
                extend 1fchbg " chin up,{w=0.1} [player]!{w=0.2} It isn't the end of the world."
                n 1usgsg "Don't worry -{w=0.3}{nw}"
                extend 1fsgsm " I'll teach you how to use the bus!"
                n 1uchsm "Ehehe."

                if Natsuki.isEnamored(higher=True):
                    n 1fllsm "And besides..."
                    n 1fllssl "That just means we can huddle up on the seat together,{w=0.1} [player]."
                    n 1fcsbgl "A dream come true for you,{w=0.1} right?"
                    n 1flldvl "Ehehe."
                else:

                    n 1fchbg "That's what friends are for, [player]!"

                $ persistent.jn_player_can_drive = False
                return


    elif persistent.jn_player_can_drive:
        menu:
            n "Doing much driving?"
            "Yes, I'm driving frequently.":

                n 1fnmbg "Ah,{w=0.1} so you're at home on the roads,{w=0.1} are you?"
                n 1ullss "Fair enough I suppose -{w=0.1} just remember to drive safe,{w=0.1} [player]!"
            "I only drive sometimes.":

                n 1ullss "Well hey,{w=0.1} at least you're saving on fuel,{w=0.1} right?{w=0.5}{nw}"
                extend 1ullsm " That doesn't sound like a bad thing to me."
                n 1fchsm "Besides,{w=0.1} it just means you can save the miles for ones you enjoy!"
            "No, I'm not driving much.":

                n 1unmaj "Oh?{w=0.5}{nw}"
                extend 1tllbg " That sounds like a bonus to me,{w=0.1} honestly!"
                n 1tnmbg "Just make sure you still get out there if you aren't driving around much though,{w=0.1} 'kay?"
            "No, I can't drive anymore.":

                n 1tnmsl "Oh...{w=0.3} did something happen?"
                n 1kllsl "I'm...{w=0.3} sorry to hear it,{w=0.1} [player]."
                n 1fsgsm "But at least that means more time to hang out with me,{w=0.1} right?{w=0.5}{nw}"
                extend 1fchbg " Ahaha."
                $ persistent.jn_player_can_drive = False

        return
    else:


        menu:
            n "Anything new happening with you on the driving front?"
            "I'm learning to drive!":

                n 1fnmss "Ooh!{w=0.5}{nw}"
                extend 1fchbg " Nice,{w=0.1} [player]!"
                n 1fchsm "Don't sweat the test,{w=0.1} alright?{w=0.2} I'm sure you'll do fine!"

                if Natsuki.isAffectionate(higher=True):
                    n 1uchsm "I believe in you,{w=0.1} [player]!"
            "I passed my test!":

                n 1uskgs "No kidding?{w=0.5}{nw}"
                extend 1uchbs " Yaaay!{w=0.2} Congrats,{w=0.1} [player]!"

                if Natsuki.isLove(higher=True):
                    n 1kwmsm "I knew you could do it,{w=0.1} you big dummy!"
                    extend 1kchsm " Ehehe."

                n 1kwmsm "Just make sure you keep up the good habits when you continue learning on your own,{w=0.1} alright?{w=0.2} Ahaha."
                $ persistent.jn_player_can_drive = True
            "I can drive again!":

                n 1uchbgedz "Hey!{w=0.2} Nice going,{w=0.1} [player]!"
                n 1fchbl "Drive safe!"
                $ persistent.jn_player_can_drive = True
            "Nope, nothing new.":

                n 1unmaj "Oh?{w=0.5}{nw}"
                extend 1nlrss " Well,{w=0.1} fair enough!"
                n 1tnmsm "You and me both then,{w=0.1} in that case?{w=0.5}{nw}"
                extend 1nchsm " Ahaha."

        return
    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_sustainable_fashion",
            unlocked=True,
            prompt="Sustainable fashion",
            category=["Environment", "Fashion"],
            nat_says=True,
            affinity_range=(jn_affinity.UPSET, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_sustainable_fashion:
    n 1nnmaj "Hey,{w=0.1} [player]..."
    n 1nllaj "This is kinda random,{w=0.1} but..."
    extend 1unmpu " are you into fashion?"
    if Natsuki.isHappy(higher=True):
        n 1fcsbg "I know I am!{w=0.2} Can you tell?"
        extend 1nchsm " Ehehe."
    else:

        n 1nnmpu "I know I am."

    n 1fllpu "But what caught me by surprise is just how much waste there is."

    if Natsuki.isNormal(higher=True):
        n 1uwdgs "Seriously,{w=0.1} [player] {w=0.1}-{w=0.1} it's insane!"
        n 1ullaj "People throw away a {i}lot{/i} of clothing...{w=0.5}{nw}"
        extend 1flrem " it's estimated that we toss out around 90{w=0.3} {i}million{/i}{w=0.3} tonnes every year."
        n 1fnman "That's a truck-full every second!{w=0.2} What a waste!"
    else:

        n 1nllbo "It's pretty insane, honestly."
        n 1fnmsl "I remember reading somewhere that we toss out something like 90{w=0.3} {i}million{/i}{w=0.3} tonnes each year."
        n 1fcsan "That's literally a truck-full {i}every{w=0.3} second{/i}."

    n 1fsrem "And we haven't even began to talk about the amount of water used for washing and plastic used for packaging too."
    n 1ksrsr "...Or the conditions some of the workers making our clothes have to put up with."

    if Natsuki.isNormal(higher=True):
        n 1fcssm "It's actually one of the reasons I began learning how to sew!"
        n 1klrsr "I've...{w=0.3} never had tons of money to buy more clothes anyway,{w=0.1} so I try to reuse and fix up what I can."
        n 1fchbg "But you'd be surprised at what you can pull off with a little creativity!"
        extend 1fcssm " And just a pinch of know-how too,{w=0.1} obviously."
        n 1fchgn "Betcha didn't know my favourite pink skirt was hand-made,{w=0.1} did you?"

    n 1unmaj "I think I've lectured you enough now,{w=0.1} [player],{w=0.1} so I won't keep harping on about it."
    n 1nllpu "But...{w=0.3} the next time you're out shopping for clothes,{w=0.1} or looking through some catalogues online?"
    n 1unmpu "Just spare a thought for the environment,{w=0.1} would you?"

    if Natsuki.isAffectionate(higher=True):
        n 1kllssl "For me?"
        n 1nchbg "Ahaha.{w=0.5}{nw}"
        extend 1uchsm " Thanks,{w=0.1} [player]!"

    elif Natsuki.isNormal(higher=True):
        n 1nchbg "Ahaha.{w=0.5}{nw}"
        extend 1uchsm " Thanks,{w=0.1} [player]!"
    else:

        n 1nllsl "Thanks."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_give_nickname",
            unlocked=True,
            prompt="Can I give you a nickname?",
            conditional="persistent._jn_nicknames_natsuki_allowed",
            category=["Natsuki"],
            player_says=True,
            affinity_range=(jn_affinity.ENAMORED, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_give_nickname:

    if persistent._jn_nicknames_natsuki_allowed and persistent._jn_nicknames_natsuki_current_nickname == "Natsuki":
        n 1unmaj "Eh?{w=0.2} You want to give me a nickname?"
        n 1fsqsl "Why?{w=0.2} Natsuki not good enough for you?{w=0.2} Is that it?"
        extend 1fsqpu " Huh?{w=0.2} Come on, [player]!{w=0.2} Spit it out!"
        n 1fsqsm "..."
        n 1fchbg "Relax,{w=0.1} [player]!{w=0.2} Jeez!{w=0.2} I'm just kidding!"
        extend 1fchsm " Ehehe."
        n 1ullbg "Well...{w=0.3} I don't see why not!"
    else:




        if persistent._jn_nicknames_natsuki_bad_given_total == 0:
            n 1unmaj "Oh?{w=0.2} You wanna give me another nickname?"
            n 1uchbg "Sure,{w=0.1} why not!"

        elif persistent._jn_nicknames_natsuki_bad_given_total == 1:
            n 1unmaj "You want to give me a new nickname?"
            n 1unmbo "Alright,{w=0.1} [player]."

        elif persistent._jn_nicknames_natsuki_bad_given_total == 2:
            n 1nnmsl "Another nickname,{w=0.1} [player]?{w=0.5}{nw}"
            extend 1nllsl " Fine."
            n 1ncsaj "Just...{w=0.3} think a little about what you choose,{w=0.1} 'kay?"

        elif persistent._jn_nicknames_natsuki_bad_given_total == 3:
            n 1nnmsl "Alright,{w=0.1} [player]."
            n 1fsqpu "Just remember.{w=0.3} You've had your final warning about this."
            n 1nsqsl "Don't let me down again."


    $ nickname = renpy.input(prompt="What did you have in mind,{w=0.2} [player]?", allow=jn_globals.DEFAULT_ALPHABETICAL_ALLOW_VALUES, length=10).strip()

    if nickname.lower() == "nevermind":
        n 1tnmpu "Huh?{w=0.2} You changed your mind?"
        n 1tllpu "Well...{w=0.3} alright then."
        n 1nnmaj "Just let me know if you actually want to call me something else then,{w=0.1} 'kay?"
        return
    else:

        $ nickname_type = jn_nicknames.get_natsuki_nickname_type(nickname)

    if nickname_type == jn_nicknames.NicknameTypes.invalid:
        n 1tlraj "Uhmm...{w=0.3} [player]?"
        n 1tnmaj "I don't think that's a nickname at all."
        n 1tllss "I'll...{w=0.3} just stick with what I have now,{w=0.1} thanks."
        return

    elif nickname_type == jn_nicknames.NicknameTypes.loved:
        $ persistent._jn_nicknames_natsuki_current_nickname = nickname
        $ n_name = persistent._jn_nicknames_natsuki_current_nickname
        n 1uskgsl "O-{w=0.1}oh!{w=0.2} [player]!"
        n 1ulrunl "..."
        n 1fcsbgl "W-{w=0.1}well,{w=0.1} you have good taste,{w=0.1} at least."
        n 1fcssml "[nickname] it is!{w=0.5}{nw}"
        extend 1uchsml " Ehehe."
        return

    elif nickname_type == jn_nicknames.NicknameTypes.disliked:
        n 1fsqbo "Come on,{w=0.1} [player]...{w=0.3} really?"
        n 1fllsl "You knew I'm not gonna be comfortable being called that."
        n 1fcssl "..."
        n 1nlraj "I'm...{w=0.3} just going to pretend you didn't say that,{w=0.1} alright?"
        return

    elif nickname_type == jn_nicknames.NicknameTypes.hated:
        n 1fskem "W-{w=0.1}what?{w=0.5}{nw}"
        extend 1fscwr " What did you just call me?!"
        n 1fcsan "[player]!{w=0.2} I can't believe you!"
        n 1fcsfu "Why would you call me that?{w=0.5}{nw}"
        extend 1fsqfu " That's {i}awful{/i}!"
        n 1fcspu "..."
        $ persistent._jn_nicknames_natsuki_bad_given_total += 1

    elif nickname_type == jn_nicknames.NicknameTypes.profanity:
        n 1fskpu "E-{w=0.1}excuse me?!"
        n 1fskfu "What the hell did you just call me,{w=0.1} [player]?!"
        n 1fcsan "..."
        n 1fslan "I seriously can't believe you,{w=0.1} [player].{w=0.5}{nw}"
        extend 1fnman " Why would you do that?{w=0.1} Are you {i}trying{/i} to get on my nerves?!"
        n 1fcspu "..."
        $ persistent._jn_nicknames_natsuki_bad_given_total += 1

    elif nickname_type == jn_nicknames.NicknameTypes.funny:
        n 1nbkdv "Pffft!"
        n 1uchbselg "Ahaha!"
        n 1fbkbs "[nickname]?!{w=0.2} What was that meant to be,{w=0.1} [player]?"
        n 1fbkbs "Well...{w=0.3} you're just lucky I have a healthy sense of humour."
        n 1fsgbg "[nickname] it is,{w=0.1} I guess!{w=0.5}{nw}"
        extend 1fchgn " Ehehe."

        $ persistent._jn_nicknames_natsuki_current_nickname = nickname
        $ n_name = persistent._jn_nicknames_natsuki_current_nickname
        return

    elif nickname_type == jn_nicknames.NicknameTypes.nou:
        n 1usqsg "No you~."
        return
    else:

        $ neutral_nickname_permitted = False


        if nickname.lower() == "natsuki":
            n 1fllss "Uhmm...{w=0.5}{nw}"
            extend 1tnmdv " [player]?"
            $ chosen_tease = jn_utils.getRandomTease()
            n 1fchbg "That's just my normal name,{w=0.1} [chosen_tease]!"
            n 1fcsca "Honestly...{w=0.5}{nw}"
            extend 1ksgsg " sometimes I wonder why I bother."
            n 1unmbg "Well,{w=0.1} I'm not complaining!{w=0.2} If it isn't broke,{w=0.1} don't fix it -{w=0.1} right?"
            n 1nchbg "Ahaha."
            $ neutral_nickname_permitted = True

        elif nickname.lower() == "thiccsuki":
            n 1kllunl "..."
            n 1fnmssl "D-{w=0.1}dreaming big,{w=0.1} are we,{w=0.1} [player]?"
            n 1klrsrl "Uhmm..."
            n 1klrpol "I'm...{w=0.3} really...{w=0.3} not a fan,{w=0.1} but if it's what you prefer..."
            $ neutral_nickname_permitted = True

        elif nickname.lower() == persistent.playername.lower():
            n 1fsldv "I...{w=0.3} don't think you thought this through,{w=0.1} [player]."
            n 1tnmbg "Do you even know how confusing that'd be?"
            n 1tlrss "I...{w=0.3} think I'll just stick to what works,{w=0.1} 'kay?{w=0.5}{nw}"
            extend 1fsqsm " Ehehe."
            n 1uchbg "Nice try though!"
        else:


            n 1fllsr "Hmm...{w=0.5}{nw}"
            extend 1ullpu " [nickname],{w=0.1} huh?"
            n 1fllss "[nickname]..."
            n 1fnmbg "You know what?{w=0.2} Yeah!{w=0.2} I like it!"
            n 1fchbg "Consider it done,{w=0.1} [player]!{w=0.5}{nw}"
            extend 1uchsm " Ehehe."
            $ neutral_nickname_permitted = True


        if (neutral_nickname_permitted):
            $ persistent._jn_nicknames_natsuki_current_nickname = nickname
            $ n_name = persistent._jn_nicknames_natsuki_current_nickname

        return


    if persistent._jn_nicknames_natsuki_bad_given_total == 1:
        n 1kllsf "Jeez,{w=0.1} [player]...{w=0.3} that isn't like you at all!{w=0.5}{nw}"
        extend 1knmaj " What's up with you today?"
        n 1kcssl "..."
        n 1knmsl "Just...{w=0.3} don't do that again,{w=0.1} okay?"
        n 1fsqsl "That really hurt,{w=0.1} [player].{w=0.2} Don't abuse my trust."


        $ Natsuki.addApology(jn_apologies.ApologyTypes.bad_nickname)
        $ Natsuki.percentageAffinityLoss(1)

    elif persistent._jn_nicknames_natsuki_bad_given_total == 2:
        n 1fsqsl "I can't believe you did that again to me,{w=0.1} [player]."
        n 1fsqan "I told you it hurts,{w=0.1} and you went ahead anyway!"
        n 1fcsan "..."
        n 1fcsun "I...{w=0.3} really...{w=0.3} like you, [player].{w=0.5}{nw}"
        extend 1kllun " It hurts extra bad when it's you."
        n 1fsqsr "Don't test my patience like this.{w=0.2} You're better than that."


        $ Natsuki.addApology(jn_apologies.ApologyTypes.bad_nickname)
        $ Natsuki.percentageAffinityLoss(2.5)

    elif persistent._jn_nicknames_natsuki_bad_given_total == 3:
        n 1fsqan "You are honestly unbelievable,{w=0.1} [player]."
        n 1fnmfu "I've told you so many times now,{w=0.1} and you still won't knock it off!"
        n 1fcspu "..."
        n 1fsqpu "No more warnings,{w=0.1} [player]."
        menu:
            n "Understand?"
            "I understand.":

                n 1fsqsr "You understand,{w=0.1} do you?"
                n 1fsqan "...Then start acting like it,{w=0.1} [player]."
                n 1fslsl "Thanks."

                $ Natsuki.percentageAffinityLoss(3)
            "...":

                n 1fcssl "Look.{w=0.2} I'm not kidding around,{w=0.1} [player]."
                n 1fnmpu "Acting like this isn't funny,{w=0.1} or cute."
                n 1fsqem "It's toxic."
                n 1fsqsr "I don't care if you're trying to pull my leg.{w=0.2} Quit it."

                $ Natsuki.percentageAffinityLoss(5)


        $ Natsuki.addApology(jn_apologies.ApologyTypes.bad_nickname)

    elif persistent._jn_nicknames_natsuki_bad_given_total == 4:

        n 1fcsan "Yeah,{w=0.1} no.{w=0.2} I've heard enough.{w=0.2} I don't need to hear any more."
        n 1fnmem "When will you learn that your actions have consequences?"
        n 1fcspu "..."
        n 1fnmpu "You know what?{w=0.5}{nw}"
        extend 1fsqpu " Don't even bother answering."
        n 1fsqsr "I warned you,{w=0.1} [player].{w=0.2} Remember that."


        python:
            get_topic("talk_give_nickname").lock()
            Natsuki.percentageAffinityLoss(10)
            persistent._jn_nicknames_natsuki_allowed = False
            persistent._jn_nicknames_natsuki_current_nickname = None
            n_name = "Natsuki"
            Natsuki.addApology(jn_apologies.ApologyTypes.bad_nickname)


    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_sleeping_well",
            unlocked=True,
            prompt="Sleeping well",
            conditional="persistent.jn_total_visit_count >= 5",
            category=["Health", "You"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_sleeping_well:
    n 1fllpu "Huh..."
    n 1fllpu "Hey,{w=0.1} [player].{w=0.5}{nw}"
    extend 1nnmaj " Let me ask you a question,{w=0.1} 'kay?"
    n 1fsqsr "How do you sleep at night?"
    n 1fsqpu "Be honest.{w=0.2} How do you do it?"
    n 1ksqsm "..."
    n 1fchsm "Ehehe.{w=0.2} Did I get you?"
    n 1unmaj "But seriously,{w=0.2} [player].{w=0.5}{nw}"
    extend 1tnmaj " Do you struggle with your sleep?"


    if jn_utils.get_current_session_length().total_seconds() / 3600 >= 12:
        n 1fsqpo "I mean,{w=0.1} you {i}have{/i} been here for a while now..."
        n 1ullaj "So...{w=0.5}{nw}"
        extend 1nnmaj " I kinda figured you might be feeling a little sleepy anyway."

    elif jn_admissions.last_admission_type == jn_admissions.TYPE_TIRED:
        n 1fllpo "I mean,{w=0.1} you even {i}said{/i} you were tired before."
        n 1ullaj "So...{w=0.5}{nw}"
        extend 1nnmaj " it only makes sense to ask,{w=0.1} right?{w=0.2} Anyway..."

    n 1nnmaj "I'll admit,{w=0.1} I get the odd sleepless night myself.{w=0.5}{nw}"
    extend 1fbkwr " It's the worst!"
    n 1fllem "There's nothing I hate more than tossing and turning,{w=0.3}{nw}"
    extend 1fcsan " just waiting for my body to decide it's time for tomorrow to happen."
    n 1ullaj "But...{w=0.5}{nw}"
    extend 1fnmss " you know what they say,{w=0.1} [player]."
    n 1fcsss "With suffering...{w=0.5}{nw}"
    extend 1uchbg " ...comes wisdom!"
    n 1nsqbg "And luckily for you,{w=0.1} I don't mind sharing.{w=0.5}{nw}"
    extend 1nchsm " Ehehe."
    n 1fcsbg "So,{w=0.1} listen up -{w=0.1} it's time for another lesson from yours truly!"
    n 1fnmaj "Alright -{w=0.1} first,{w=0.1} cut the crap!{w=0.2} If you're trying to sleep,{w=0.1} anything high-sugar or high-caffeine is your enemy."
    n 1fllss "So before anything else,{w=0.1} ditch the soda and coffee.{w=0.2} You can thank me later."
    n 1fcsaj "Next up -{w=0.1} no screens!{w=0.5}{nw}"
    extend 1fsqpo " Including this one, [player]."
    n 1unmsl "No screen means no bright lights or distractions to keep you up,{w=0.1} obviously."
    n 1fnmpu "If you're tired then the last thing you need is something beaming whatever at you."

    if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.anime_streaming):
        n 1tsqsr "And no, [player] {w=0.1}-{w=0.3}{nw}"
        extend 1fnmpo " No late-night anime binging sessions either."
        n 1nchgn "Sorry~!"

    n 1fcsbg "Moving on, next is temperature!{w=0.2} If it's hot,{w=0.1} use thinner sheets and vice versa."
    n 1fcspu "Nothing disrupts your sleep more than having to rip off blankets,{w=0.1} or pull some out."
    n 1fsgsg "Keeping up with me so far,{w=0.1} [player]?{w=0.5}{nw}"
    extend 1fchgn " I'm almost done,{w=0.1} don't worry."
    n 1unmaj "Lastly...{w=0.5}{nw}"
    extend 1fchbg " get comfortable!"
    n 1nnmsm "Make sure you have enough pillows to support your head,{w=0.1} or maybe even play some quiet music if you find that helps."
    n 1fcssm "...And that's about it!"
    n 1nllss "You should have known at least a few of those already,{w=0.3}{nw}"
    extend 1unmss " but at any rate..."
    n 1fwlbg "I hope you can rest easy with your newfound knowledge,{w=0.1} [player]!"
    n 1uchsm "Ehehe."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_aging",
            unlocked=True,
            prompt="Aging",
            category=["Life"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_aging:
    n 1unmaj "You know,{w=0.1} [player]..."
    n 1nllpu "I think most people share a bunch of fears."
    n 1unmpu "You get what I mean,{w=0.1} right?{w=0.2} Like presenting stuff to a room full of people,{w=0.1} or failing a test."
    n 1tlrss "Of course,{w=0.1} it's rare to find one that {i}everyone{/i} has..."
    n 1tnmaj "Or at least something that makes anyone feel uneasy."
    n 1unmbg "But...{w=0.3} I think I found one!"
    n 1usgsm "What am I thinking of,{w=0.1} you ask?"
    n 1ullaj "Well...{w=0.3} it's actually kinda boring,{w=0.1} really."
    n 1nnmbo "I was actually thinking about growing older."
    n 1unmpu "Have you ever thought much about it,{w=0.1} [player]?"
    n 1fllbg "It's probably the last thing on your mind if you're pretty young."
    n 1nwmpu "But I think as you actually get older,{w=0.1} it starts to creep in."
    n 1kllpu "You might have less energy,{w=0.1} or friends and family begin drifting away..."
    n 1knmem "Birthdays lose all meaning -{w=0.1} you might even dread them!"
    n 1ullaj "The signs appear in a bunch of ways,{w=0.3}{nw}"
    extend 1knmsl " but that's what makes it unnerving."
    n 1kllaj "Everyone experiences it differently,{w=0.3}{nw}"
    extend 1kskaw " and we don't even know what happens after the end!"
    n 1klrss "Spooky,{w=0.1} huh?"
    n 1ulrpu "Although...{w=0.3} I guess you could say that's more the fear of the unknown than aging itself."
    n 1flraj "What does wind me up though is how immature people can be about it."
    n 1fnmaj "Especially when it comes to relationships between different ages!"
    n 1fslsf "People just get so preachy about it..."
    n 1fllaj "Like...{w=0.3} as long as they're both happy,{w=0.2} it's all legal,{w=0.3}{nw}"
    extend 1fnmem " and nobody is being hurt or made uncomfortable,{w=0.1} who {i}actually{/i} cares?"
    n 1nlrpu "It's just like most stuff,{w=0.1} really."
    n 1unmaj "Besides,{w=0.1} it's not like being a certain age means you {i}have{/i} to be a certain way."
    n 1fchbg "I mean...{w=0.3} look at Yuri!"
    n 1uchgn "Being all old-fashioned like that -{w=0.1} you'd think she's retired!"
    n 1nllbg "But anyway...{w=0.3} I think we got side-tracked."
    n 1unmss "I don't really care how old you are,{w=0.1} [player]."

    if Natsuki.isLove(higher=True):
        $ chosen_tease = jn_utils.getRandomTease()
        n 1klrpol "Y-{w=0.1}you better know that I love you all the same,{w=0.1} [chosen_tease]."
        n 1knmpol "Don't forget that,{w=0.1} 'kay?"
        n 1flrpol "I'll get mad if you do.{w=0.5}{nw}"
        extend 1klrbgl " Ahaha..."

    elif Natsuki.isEnamored(higher=True):
        n 1fllbgl "You've been pretty awesome to me all the same."

    elif Natsuki.isHappy(higher=True):
        n 1fchbgl "You're always fun to hang around with!"
    else:

        n 1fllbg "But...{w=0.3} just in case?"
        n 1fsqsg "We're only having one candle on your birthday cake.{w=0.2} Sorry.{w=0.5}{nw}"
        extend 1uchbgelg " Ahaha!"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_work_life_balance",
            unlocked=True,
            prompt="Work-life balance",
            category=["Life", "Society"],
            nat_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_work_life_balance:
    if Natsuki.isUpset(higher=True):
        n 1ullaj "You know,{w=0.1} [player]..."

    n 1nnmaj "I think it's pretty easy to let your academic or work life creep into your personal time nowadays."
    n 1nlrsl "I mean...{w=0.3} think about it."
    n 1nnmsl "With everyone having mobile phones,{w=0.1} plus usually some kinda computer at home -{w=0.1} it's hard not to be connected somehow."
    n 1flrbo "And like...{w=0.3} if there's already that connection,{w=0.1} then what's to stop work from bugging you during your time off?"
    n 1fsrbo "Or classmates asking for help at the last possible minute?"

    if Natsuki.isUpset(higher=True):
        n 1fcsem "It just gets annoying -{w=0.1} like everyone expects you to always be around to chip in a little more,{w=0.1} or get something done!"
        n 1fnmpo "Overwhelming,{w=0.1} right?"
        n 1fllaj "Huh.{w=0.2} Actually...{w=0.3} now that I think about it..."
        n 1fnmsf "It isn't like that kind of intrusion is only limited to when you're away either."
        n 1fslpu "I've heard {i}way{/i} too many stories of people doing stupid amounts of overtime at work...{w=0.5}{nw}"
        extend 1fnman " sometimes not even paid!"
        n 1fsran "Or even students studying late into the night until they collapse...{w=0.3} it's crazy!"
    else:

        n 1fsqpu "It just gets annoying -{w=0.1} everyone expects you to always be around to do more."
        n 1fslsl "Actually,{w=0.1} now that I think about it..."
        n 1fcsaj "It isn't like that kind of thing is only limited to when you're away either."
        n 1fsrsr "I've heard too many stories of people doing stupid amounts of overtime at work.{w=0.5}{nw}"
        extend 1fsqan " Often not even paid."
        n 1fslem "Or even students studying late into the night until they collapse..."

    if Natsuki.isNormal(higher=True):
        n 1kcsemesi "Ugh...{w=1} I just wish people would value their own time more."
        n 1klrsr "..."
        n 1unmaj "Hey,{w=0.1} [player]..."
        n 1nllaj "I don't know if you're working,{w=0.1} or studying,{w=0.1} or what..."
        n 1fnmsf "But you better not be letting whatever it is take over your life.{w=0.2} Understand?"

        if Natsuki.isEnamored(higher=True):
            n 1knmpu "You are {i}more{/i} than your career,{w=0.1} or your education.{w=0.2} You have your own wants and needs that matter too."
            n 1kllun "I don't want some dumb job or stupid assignment to take over your life."
            n 1fcsun "You're...{w=0.3} way more important than either of those,{w=0.1} [player].{w=0.2} Trust me."

            if Natsuki.isLove(higher=True):
                n 1fllun "Besides..."
                n 1fllssl "You and your time are mine first, [player]."
                n 1flldvl "I already called dibs,{w=0.1} a-{w=0.1}after all.{w=0.5}{nw}"
                extend 1fchsml " Ehehe..."
        else:

            $ chosen_tease = jn_utils.getRandomTease()
            n 1kllpo "People are more than what they do for a living,{w=0.1} after all.{w=0.2} And that includes you too, [chosen_tease]!"

    elif Natsuki.isDistressed(higher=True):
        n 1fllsr "Makes me wish people would value their own time more."
        n 1fnmsr "...I guess that includes you too,{w=0.1} [player]."
        n 1fllpu "You've got better things to do."
        n 1fsqsf "...Like being a decent friend to others for a change.{w=0.2} Am I right?"
    else:

        n 1fslbo "People need to value their own time more,{w=0.1} I guess."
        n 1fcssl "...Heh."
        n 1fcsunl "Maybe I should follow my own advice..."
        n 1fsqanltsb "Because {i}clearly{/i} being here is a waste of my time too."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_using_headphones_carefully",
            unlocked=True,
            prompt="Using headphones carefully",
            category=["Health", "Music", "Technology"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_using_headphones_carefully:
    n 1unmaj "..."
    n 1tnmaj "...?"
    n 1fnmaw "...!"
    n 1fbkwr "...[player]!"
    n 1fnmpo "[player]!{w=0.2} Finally!{w=0.2} Can you hear me now?"
    n 1fllpo "Jeez...{w=0.3} took you long enough!"
    n 1fslsm "..."
    n 1uchbg "Ehehe."
    n 1fnmbg "Admit it,{w=0.1} [player]!{w=0.2} I'll get you one of these days."
    n 1nnmaj "Seriously though -{w=0.1} do you use headphones or anything like that often?"
    n 1nlrpo "I'll admit,{w=0.1} I probably use mine more than I should."
    n 1fnmaj "I was kinda joking about the whole hearing thing,{w=0.1} but this is important,{w=0.1} [player]."
    n 1nlrss "I like cranking it up too -{w=0.1} just don't make a bad habit of it."
    n 1unmsl "There's even warnings in some countries if you have the volume up too loud..."
    n 1fllem "...And for a good reason!"
    n 1fnmpo "Not just to protect your ears either -{w=0.1} you better be careful wearing them out and about too."
    n 1fcsem "I don't wanna hear about you getting knocked over because you didn't hear something coming!"
    n 1unmbo "Oh -{w=0.1} and one last thing,{w=0.1} actually."
    n 1unmpu "You might wear them to focus at work or relax at home -{w=0.1} and that's fine!"
    n 1nnmsr "But please,{w=0.1} [player]."
    n 1flrsr "...Take them off every once and a while,{w=0.1} will you?{w=0.2} For other people,{w=0.1} I mean."
    n 1ncsbo "I get it -{w=0.1} if you just wanna listen to something in peace,{w=0.1} or give yourself some room,{w=0.1} that's okay."

    if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.music_applications):
        n 1kslbg "I know you like your music streaming."

    n 1nsqbo "But don't use them to barricade yourself away from everyone and everything."
    n 1ksrsl "It's...{w=0.3} not healthy to do that either,{w=0.1} [player]."
    n 1nchsm "...And that's about all I had to say!"
    n 1fchbg "Thanks for {i}hearing{/i} me out,{w=0.1} [player]!{w=0.2} Ehehe."
    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_thoughts_on_horror",
            unlocked=True,
            prompt="Thoughts on horror",
            category=["Media", "Literature"],
            nat_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_thoughts_on_horror:

    if Natsuki.isNormal(higher=True):
        n 1unmaj "You know,{w=0.1} [player]..."
        n 1tllaj "I don't think I ever actually explained why I dislike horror so much."
        n 1tlrss "I know I mentioned it before,{w=0.1} but I was kinda caught off guard at the time."
        n 1unmaj "Honestly?"
        n 1nnmsm "Everyone has their tastes,{w=0.1} right? And I can get why people enjoy it."

    elif Natsuki.isDistressed(higher=True):
        n 1nllbo "I don't think I explained why I dislike horror."
        n 1nnmsl "I get everyone has their tastes,{w=0.1} but I don't care for it."
    else:

        n 1kslsl "..."
        n 1fsqun "...I was about to share some of my thoughts on horror with you.{w=1}{nw}"
        extend 1fsrsl " Or at least,{w=0.1} I was thinking about it."
        n 1fsqem "...But then do you know what I realized,{w=0.1} [player]?"
        n 1fsqan "I hate horror -{w=0.5}{nw}"
        extend 1fllem " not that you'd care -{w=0.3}{nw}"
        extend 1fnmful " and honestly?"
        n 1fcsanltsa "Being stuck here with {i}you{/i} is horror enough."
        return

    if Natsuki.isNormal(higher=True):
        n 1fchbg "Like Yuri!"
        n 1fcsss "It's suspenseful,{w=0.1} and fears are a super powerful motivator for characters!"
        n 1ullpu "So don't get me wrong{w=0.1} -{w=0.1} I can totally appreciate the effort that goes into it."
        n 1fllpol "...When it isn't just stupid jumpscares,{w=0.1} a-{w=0.1}anyway."
    else:

        n 1ullpu "I get the effort that goes into it.{w=0.2} For the most part."

    n 1nllpu "But..."
    n 1nnmbo "When I read something -{w=0.1} or watch something -{w=0.1} I'm doing it because for me,{w=0.1} it's how I relax."
    n 1fllbo "I don't want to be made to feel uneasy."
    n 1fllpu "I don't want to be made to jump."
    n 1fllsr "I don't want to have to see gross stuff."
    n 1fcssr "I...{w=0.3} just want to sit back,{w=0.1} feel good and just escape for a while."
    n 1fnmsl "There's more than enough nasty things going out there already,{w=0.1} you know?"
    n 1flrpu "Some things closer to home than others."
    n 1fcssl "..."
    n 1nnmaj "So...{w=0.3} yeah.{w=0.1} That's about all I had to say about it."

    if Natsuki.isAffectionate(higher=True):
        n 1unmss "Though...{w=0.3} if you want to put something on,{w=0.1} [player]?{w=0.2} Go ahead."
        n 1fllssl "If it's you,{w=0.1} I {i}think{/i} I can deal with it."
        n 1flrpol "But...{w=0.3} we're keeping the volume low.{w=0.2} Got it?"

    elif Natsuki.isNormal(higher=True):
        n 1nnmaj "Don't mind me though,{w=0.1} [player].{w=0.2} If you wanna watch something,{w=0.1} go for it."
        n 1flrcal "But you're watching it solo."

    elif Natsuki.isDistressed(higher=True):
        n 1flrsl "..."
        n 1fnmpu "I {i}would{/i} ask that if you were gonna watch something like that,{w=0.1} then to warn me first."
        n 1fsqsrtsb "But you wouldn't listen to me anyway,{w=0.1} would you?"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_gaming",
            unlocked=True,
            prompt="Are you into video games?",
            category=["Games", "Media"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_gaming:
    if Natsuki.isNormal(higher=True):
        n 1unmaj "Gaming?"
        n 1fcsbg "Well...{w=0.3} duh!"
        n 1fnmbg "You bet I'm into gaming,{w=0.1} [player]!"
        n 1ullss "I wouldn't say I'm the most active player...{w=0.2} but I definitely do my share of button mashing."
        n 1nslsg "Hmm..."
        n 1tnmss "I don't think I even need to ask,{w=0.1} but..."
        menu:
            n "What about you,{w=0.1} [player]?{w=0.2} Do you play often?"
            "Absolutely!":

                $ persistent.jn_player_gaming_frequency = "High"
                n 1fcsbg "Yep!{w=0.2} Just as I suspected..."
                n 1uchgn "[player] is a mega-dork."
                n 1uchbselg "Ahaha!"
                n 1uchsm "Relax,{w=0.1} [player]!"
                n 1fllssl "I'm not much better,{w=0.1} after all."
            "I play occasionally.":

                $ persistent.jn_player_gaming_frequency = "Medium"
                n 1fsqsm "Yeah,{w=0.1} yeah.{w=0.2} Believe what you want to believe,{w=0.1} [player]."
                n 1usqbg "I'm not sure I buy it,{w=0.1} though."
            "I don't play at all.":

                $ persistent.jn_player_gaming_frequency = "Low"
                n 1tnmaj "Huh?{w=0.2} Really?"
                n 1tllaj "Not even the odd casual game?"

                if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.gaming):
                    n 1fsqts "Liar.{nw}"

                n 1ncsaj "...Well then."
                n 1fnmbg "It looks like I've got a lot to teach you,{w=0.1} [player]!"

    elif Natsuki.isDistressed(higher=True):
        n 1nnmsl "Huh?{w=0.2} Video games?"
        n 1nslsl "Yeah,{w=0.1} I guess.{w=0.2} For what that's worth to you."
    else:

        n 1nsqsl "Video games...?"
        n 1fsqsltsb "...Heh.{w=0.2} Why,{w=0.3} [player]?{w=1}{nw}"
        extend 1fcsantsa " Was stomping all over my feelings not enough?"
        n 1fsqfultsb "Or were you looking to see if you can stomp all over me in games too?"
        n 1fcsfrltsa "..."
        n 1fcsupl "...I don't wanna talk about this any more.{w=0.2} We're {i}done{/i} here."
        return

    if Natsuki.isNormal(higher=True):
        n 1ullaj "Anyway,{w=0.1} putting that aside..."
        n 1nsgbg "When it comes to my preferences?{w=0.2} I want challenge in my games!"
        n 1fcsbg "I play for the win{w=0.1} -{w=0.1} it's me versus the developers,{w=0.1} and they're not around to stop me!"
        n 1fchbg "Ahaha."
        n 1ullss "I'm actually more into my roguelikes,{w=0.1} to be honest."
        n 1fnmsm "Heh.{w=0.2} Are you surprised,{w=0.1} [player]?"
        n 1fcsbg "Tough as nails,{w=0.1} and I gotta think on my feet{w=0.1} -{w=0.1} plus it's super satisfying learning everything too."
        n 1fchsm "And with how random everything is,{w=0.1} they always feel refreshing and fun to play!"
        n 1fnmbg "Every time I load one up,{w=0.1} I have no idea what I'm up against...{w=0.3} and that's what makes them addicting!"
        n 1fcssm "Ehehe.{w=0.2} Don't worry though, [player]."
        n 1fcsbg "I don't know if you're into that kind of stuff as well,{w=0.1} but..."

        if persistent.jn_player_gaming_frequency == "High":
            n 1fchgn "There's still plenty I can teach you!"

            if Natsuki.isEnamored(higher=True):
                n 1ksqsml "And I bet you'd like that too,{w=0.1} huh?"
                n 1nchbg "Ahaha."

            elif Natsuki.isAffectionate(higher=True):
                n 1fchbg "And I'm not gonna take 'No' for an answer!"

        elif persistent.jn_player_gaming_frequency == "Medium":
            n 1fsqsm "I don't mind showing you how it's done."
            n 1fchbg "I {i}am{/i} a professional,{w=0.1} after all!"
        else:

            if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.gaming):
                n 1fsqts "Liar.{nw}"

            n 1ullaj "Well then...{w=0.5}{nw}"
            extend 1usqsm " I'm sure I can get {i}you{/i} of all people into it."
    else:

        n 1nnmsl "I suppose I look for challenge in my games more than anything."
        n 1nllsl "It's fun pitting myself against the developers and beating them at their own game."
        n 1nsqaj "I guess I could say I like being tested -{w=0.1} so long as I'm in control of it,{w=0.1} that is."
        n 1fsqbo "What does that mean?{w=0.2} I guess I'll spell it out for you,{w=0.1} [player]."
        n 1fsqan "I really {i}don't{/i} like the kind of testing you're doing."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_natsukis_fang",
            unlocked=True,
            prompt="[n_name]'s fang",
            category=["Natsuki"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_natsukis_fang:
    n 1nllbo "..."
    n 1unmaj "Eh?{w=0.2} What's up,{w=0.1} [player]?"
    n 1unmsl "..."
    n 1tnmaj "What?{w=0.2} Is there something on my face?"
    n 1tnmca "..."
    n 1uwdaj "Oh.{w=0.2} Yeah.{w=0.2} I get it."
    n 1nsqss "Just can't help but notice the fang,{w=0.1} right?{w=0.2} Ehehe."
    n 1nllss "You know..."
    n 1nnmaj "I wasn't always happy with my teeth,{w=0.1} [player]."
    n 1flran "I used to be pretty self conscious about them.{w=0.2} People would just keep pointing them out all the time."
    n 1fcsaj "It wasn't...{w=0.3} {i}bad{/i} or anything...{w=0.3} a little annoying at first,{w=0.1} but nothing over the top."
    n 1kslsf "...Mostly."
    n 1ulrsl "But...{w=0.3} I guess I just came to embrace them?"
    n 1fchbg "They're like a trademark or something now!{w=0.2} Which is why I take good care of them."
    n 1fnmsf "You better not be slacking off on yours,{w=0.1} [player]!"
    n 1fnmaj "And I don't just mean skipping the odd brush,{w=0.1} either..."
    n 1fsgss "Yeah.{w=0.2} We both know what's coming,{w=0.2} don't we?"
    n 1fsqbg "When's the last time {i}you{/i} flossed,{w=0.1} [player]?{w=0.2} Be honest."
    n 1tsqsm "..."
    n 1fchbgelg "Ahaha!{w=0.2} Did I call you out?"
    n 1nlrss "Well,{w=0.1} whatever.{w=0.2} I'm just gonna assume you'll go do that later."
    n 1fcsaw "Seriously though.{w=0.2} You better make sure you take care of your teeth!"
    n 1fnmaj "Regular brushing and flossing is important,{w=0.1} but watch your diet too."
    n 1fllsl "Not flossing isn't great,{w=0.1} but constant sugary drinks are even worse!"
    n 1fsgsm "Remember,{w=0.1} [player] -{w=0.1} if you ignore them,{w=0.1} they'll go away~."
    n 1nllss "But no, seriously."

    if Natsuki.isLove(higher=True):
        $ chosen_endearment = jn_utils.getRandomEndearment()
        n 1kllss "Smiles look good on you,{w=0.1} [chosen_endearment]."
        n 1fnmsm "Let's keep them looking that way."
        n 1uchsml "Ehehe.{w=0.2} Love you,{w=0.1} [player]~!"

    elif Natsuki.isEnamored(higher=True):
        n 1fnmsml "I think smiles look good on you,{w=0.1} [player]."
        n 1fchbgl "Let's keep them looking that way!"

    elif Natsuki.isAffectionate(higher=True):
        n 1usqbg "The right smile can make all the difference,{w=0.1} you know.{w=0.2} Just look at mine!"
        n 1uchgn "Ehehe."
    else:

        n 1unmaj "If you don't look after them?"
        n 1fllajl "I'm not holding your hand at the dentist!"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_i_love_you",
            unlocked=True,
            prompt="I love you, {0}!".format(n_name),
            category=["Natsuki", "Romance"],
            player_says=True,
            location="classroom",
            affinity_range=(jn_affinity.ENAMORED, None)
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_i_love_you:

    $ player_initial = jn_utils.getPlayerInitial()
    $ chosen_tease = jn_utils.getRandomTease()
    $ chosen_endearment = jn_utils.getRandomEndearment()
    $ chosen_descriptor = jn_utils.getRandomDescriptor()


    if (
        persistent.affinity >= (jn_affinity.AFF_THRESHOLD_LOVE -1)
        and not persistent._jn_player_confession_accepted
    ):
        n 1uscemf "O-{w=0.1}o-{w=0.1}oh my gosh..."
        n 1uskemf "[player_initial]-{w=0.2}[player]...{w=0.3} y-{w=0.1}you...!"
        n 1fcsanf "Nnnnnnn-!"
        n 1fbkwrf "W-{w=0.1}well it took you long enough!{w=0.2} What did you think you were doing?!"
        n 1flrwrf "I bet you were just waiting for me to say it first!"
        n 1fllemf "Jeez,{w=0.1} [player]...{w=0.3} [chosen_tease]..."
        n 1kllemf "But..."
        n 1fcswrf "B-{w=0.1}but...!"
        n 1flranf "Uuuuuuu-!"
        n 1fchwrf "Oh,{w=0.1} whatever!{w=0.2} I don't care!{w=0.2} I gotta say it!{w=0.2} I gotta say it!"
        n 1kwdemf "[player]!{w=0.2} I love you too!"
        n 1kchbsf "I-{w=0.1}I love...{w=0.3} you too..."
        n 1kplbgf "I...{w=0.3} I..."
        n 1fcsunfsbl "..."

        show natsuki 1kcspuf zorder JN_NATSUKI_ZORDER at jn_center
        show black zorder 3 with Dissolve(0.5)
        play audio clothing_ruffle
        $ jnPause(3.5)
        play audio kiss
        show natsuki 1ksrsmfsbr zorder JN_NATSUKI_ZORDER at jn_center
        $ jnPause(1.5)
        hide black with Dissolve(1.25)

        n 1kchsmf "..."
        n 1kwmsmf "I love you,{w=0.3} [player]..."
        n 1kllsml "..."
        n 1kskemf "S-{w=0.1}sorry...!"
        n 1klrunf "I...{w=0.3} think I got a little carried away..."
        n 1kcssmf "..."
        n 1knmajf "..."
        n 1kbkemf "J-{w=0.1}jeez!{w=0.2} Stop looking at me like that already!"
        n 1fllemf "W-{w=0.1}we're both on the same page now,{w=0.1} so..."
        n 1kllbof "...{w=0.3}T-that's all I had."
        n 1kllsmf "..."
        n 1kllssf "S-{w=0.1}so..."
        n 1kplssf "Where were we?{w=0.2} Ehehe..."

        $ persistent._jn_player_confession_accepted = True
        $ persistent.jn_player_love_you_count += 1
        $ Natsuki.percentageAffinityGain(10)
        return


    elif persistent.jn_player_love_you_count == 0 and not persistent._jn_player_confession_accepted:
        if Natsuki.isEnamored():
            n 1uscgsf "[player_initial]-{w=0.2}[player]!"
            n 1fskgsf "Y-{w=0.1}you...!"
            n 1fcsanf "Nnnnn-!"
            n 1fbkwrf "I-{w=0.1}I know we've been seeing each other a while,{w=0.1} but this is way too sudden!"
            n 1fllwrf "Now you've gone and made it super awkward,{w=0.1} [player]!{w=0.2} Why'd you have to go do that?!"
            n 1fcsemf "Sheesh!"
            n 1fslpof "...I hope you're happy."
            n 1fsqunf "..."
            n 1fnmpof "D-{w=0.1}don't think this means I {i}hate{/i} you or anything,{w=0.1} though..."
            n 1flreml "It's just that...{w=0.3} It's just..."
            n 1fcsanl "Uuuuuu..."
            n 1flrbol "N-{w=0.1}never mind..."
            n 1fcseml "Forget I said anything."
            n 1kllbof "..."
            $ Natsuki.calculatedAffinityGain(base=2, bypass=True)

        elif Natsuki.isAffectionate(higher=True):
            n 1uskwrf "W-{w=0.1}w-{w=0.1}what?"
            n 1fwdwrf "D-{w=0.1}did you just...?"
            n 1fcsanf "Nnnnnnnnn-!"
            n 1fbkwrf "[player_initial]-{w=0.2}[player]!"
            n 1fcsemf "Are you trying to give me a heart attack?!{w=0.2} Jeez!"
            n 1fllemf "You can't just say stuff like that so suddenly..."
            n 1kllunf "..."
            n 1fllajf "I-{w=0.1}I mean..."
            n 1flranf "It's not that I {i}don't{/i} like you,{w=0.1} o-{w=0.1}or anything,{w=0.1} but..."
            n 1fslanf "But...!"
            n 1fcsanf "Uuuuu..."
            n 1fcsajf "F-{w=0.1}forget it!{w=0.2} I-{w=0.1}it's nothing..."
            n 1kslslf "..."
            $ Natsuki.calculatedAffinityGain(bypass=True)

        elif Natsuki.isHappy(higher=True):
            n 1fsqdvl "Pffffft!"
            n 1uchbslelg "Ahaha!"
            n 1tllbgl "You can't be serious,{w=0.1} [player]!{w=0.2} You're just messing with me!{w=0.2} Right?"
            n 1knmbgl "Right,{w=0.1} [player]?"
            n 1knmajf "R-{w=0.1}right...?"
            n 1fllunf "..."
            n 1fcsgsf "J-{w=0.1}jeez!{w=0.2} Enough of this!"
            n 1fsqajf "You really shouldn't mess around with girls like that,{w=0.1} [player]!"
            n 1fslpul "Y-{w=0.1}you're just lucky I've got a great sense of humour."
            n 1fnmpol "S-{w=0.1}so it's fine...{w=0.3} this time..."
            n 1fcsajl "Just...{w=0.3} think a little before you just blurt stuff out!{w=0.2} Sheesh."
            n 1fllslf "[chosen_tease.capitalize()]..."

        elif Natsuki.isNormal(higher=True):
            n 1fscgsf "Urk-!"
            n 1fskanf "W-{w=0.1}what did you..."
            n 1fwdanf "Did you just...?"
            n 1fllajl "..."
            n 1fcsbgf "A-{w=0.1}aha!{w=0.2} I mean...{w=0.3} y-{w=0.1}yeah!{w=0.2} Who wouldn't love me,{w=0.1} right?"
            n 1fllbgf "My wit,{w=0.1} my style,{w=0.1} my killer sense of humour...{w=0.3} I've got it all.{w=0.1} Yeah..."
            n 1fbkwrf "D-{w=0.1}don't get the wrong idea or a-{w=0.1}anything, though!"
            n 1fllssf "I-{w=0.1}I mean,{w=0.1} I'm just glad you have some good taste."
            n 1fllunf "Yeah..."

        elif Natsuki.isUpset(higher=True):
            n 1fcsan "..."
            n 1fnmfu "Seriously,{w=0.1} [player]?{w=0.2} You're really going to say that to me {i}now{/i}?"
            n 1fsqfutsb "The first time you choose to say it...{w=0.3} and you say it {i}now{/i}?"
            n 1fcspu "..."
            n 1fwman "...And you really think I'm gonna buy that {i}now{/i},{w=0.1} [player]?"
            n 1fcsfu "..."
            n 1fcssr "..."
            n 1fsqsr "We're done with this."
            n 1fsqpu "And if you {i}really{/i} feel that way?"
            n 1fsqsftsb "...Then why aren't {i}you{/i} trying to make this work,{w=0.1} [player]?"
            $ Natsuki.percentageAffinityLoss(10)
        else:


            n 1fsqputsb "..."
            n 1fcsuntsa "Y-{w=0.1}you..."
            n 1fcsantsa "You...{w=0.3} h-{w=0.1}how...!"
            n 1fscwr "H-{w=0.1}how {i}dare{/i} you tell me that now!"
            n 1fscfu "{i}How {w=0.3} dare {w=0.3} you.{/i}"
            n 1fcsfu "..."
            n 1fcssr "..."
            n 1fsqsr "You knew how I felt,{w=0.1} [player]..."
            n 1fcsan "You knew for such a long time..."
            n 1fsqfutsb "And now?{w=0.2} {i}Now{/i} is when you tell me?"
            n 1fsquptse "For the {i}first time{/i}?"
            n 1fcsuptsa "..."
            n 1kplan "I...{w=0.3} I c-{w=0.1}can't do this right now."
            n 1kcsantsd "It...{w=0.5} it hurts..."
            n 1kcsfutsd "..."
            n 1fcsputsd "Get out of my sight,{w=0.1} [player]."
            n 1fcsantsd "..."
            n 1fsqfutse "Go!"
            n 1fscsctdc "{i}JUST LEAVE ME ALONE!{/i}{nw}"
            $ Natsuki.percentageAffinityLoss(25)
            $ persistent.jn_player_love_you_count += 1
            return { "quit": None }

        $ persistent.jn_player_love_you_count += 1
    else:


        $ persistent.jn_player_love_you_count += 1
        if Natsuki.isLove(higher=True):


            $ random_response_index = random.randint(0, 11)

            if random_response_index == 0:
                n 1unmbgf "Ehehe.{w=0.2} I love you too,{w=0.1} [chosen_endearment]!"
                n 1uchsmf "You're always [chosen_descriptor] to me."
                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 1:
                n 1tsqssl "Aww,{w=0.1} you don't say?"
                n 1uchbslelg "Ahaha!"
                $ chosen_endearment = chosen_endearment.capitalize()
                n 1kwmbgf "[chosen_endearment],{w=0.1} I love you too!"
                n 1fcsbgf "I'll always be here to stick up for you."
                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 2:
                n 1uchsmf "Aww,{w=0.1} [chosen_endearment]!{w=0.2} I love you too!"
                n 1klrbgf "You're the best thing that's ever happened to me."
                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 3:
                n 1ksqbgf "Oh?{w=0.2} Someone's all needy today,{w=0.1} huh?"
                n 1fsqsmf "Well,{w=0.1} I'd be happy to oblige!"
                n 1uchsmf "I love you too,{w=0.1} [chosen_endearment]!"
                n 1fchbgf "Keep on smiling for me,{w=0.1} 'kay?"
                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 4:
                n 1flrpof "Fawning over me like always,{w=0.1} [player]?"
                n 1usqssf "Ehehe.{w=0.2} Don't worry,{w=0.1} I'm not complaining!"
                n 1uchbgf "I love you too,{w=0.1} [chosen_endearment]!"
                n 1fcssmf "It's just us two against the world!"
                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 5:
                n 1fllbgf "Well,{w=0.1} o-{w=0.1}of course you do.{w=0.2} Ahaha!"
                n 1fchbgf "But...{w=0.3} we both know I love you more,{w=0.1} [player]."
                menu:
                    "No, I love you more.":
                        n 1fnmbgf "No,{w=0.1} I-"
                        n 1tllajl "..."
                        n 1fnmawl "H-{w=0.1}hey...{w=0.3} wait a minute...!"
                        n 1fchgnl "I know where we're going with this!{w=0.2} Nice try,{w=0.1} [player]!"
                        n 1fsqsml "You're just gonna have to accept that I love you more,{w=0.1} and that's just the way it is."
                        menu:
                            "You love me more, and that's just the way it is.":
                                n 1uchgnf "Ehehe.{w=0.2} See?"
                                n 1fwmsmf "That wasn't so hard,{w=0.1} was it?"
                                n 1nchbgf "I looooove you,{w=0.1} [player]~!"
                    "Okay.":

                        n 1uchgnlelg "Pfffft!{w=0.2} Ahaha!"
                        n 1fwltsf "Come on,{w=0.1} [player]!{w=0.2} Where's your fighting spirit?"
                        n 1fchsmf "Well,{w=0.1} whatever.{w=0.2} I'm just glad you accept the truth."
                        n 1uchsmf "Ehehe."

                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 6:
                n 1uchsmf "Ehehe...{w=0.3} I always adore hearing that from you,{w=0.1} [player]."
                n 1usqsmf "...And I think I can guess you like hearing it just as much."
                n 1uchbgf "I love you too,{w=0.1} [chosen_endearment]!"
                n 1nchsmf "I don't need anyone else~."
                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 7:
                n 1nsqajl "Wow,{w=0.1} [player]..."
                n 1tslajl "You really are just a big sappy mess today,{w=0.1} aren't you?"
                n 1tsldvl "Gross..."
                n 1fchbgf "...But just the kind of gross I'm down with.{w=0.2} Ehehe."
                n 1uchbgf "I love you too,{w=0.1} [chosen_endearment]!"
                n 1unmsmf "I'll always have your back."
                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 8:
                n 1uchsmf "Ehehe."
                n 1nchssf "I..."
                n 1uchbsf "Looooooooove you too,{w=0.1} [player]!"
                n 1kwmsmf "You'll always be my rock."
                $ Natsuki.calculatedAffinityGain()
                return

            elif random_response_index == 9:
                n 1fllsmf "I mean...{w=0.3} that's real sweet of you and all,{w=0.1} [player]..."
                n 1fsqsmf "But we both know I love you more~."
                $ player_is_wrong = True
                $ wrong_response_count = 0


                while player_is_wrong:
                    menu:
                        "No, I love {i}you{/i} more!":

                            if wrong_response_count == 1:
                                n 1fsqbgl "Hmm?{w=0.2} Did you mishear me,{w=0.1} [player]?"
                                n 1fchbgf "I said I love {i}you{/i} more,{w=0.2} [chosen_tease]!"

                            elif wrong_response_count == 5:
                                n 1fsqbgl "Oh?{w=0.2} Competitive,{w=0.1} are we?"
                                n 1fslbgl "Ehehe.{w=0.2} Silly [player].{w=0.1} Did nobody ever tell you?"
                                n 1fchgnl "Don't start a fight you can't finish!"
                                n 1fchbgf "Especially this one -{w=0.1} I love {i}you{/i} more~!"

                            elif wrong_response_count == 10:
                                n 1tsqbgl "Oho?{w=0.2} Not bad,{w=0.1} [player]!"
                                n 1fsqbgl "I almost admire your stubbornness..."
                                n 1uchsmf "But not as much as I admire you!{w=0.2} I love {i}you{/i} more!"

                            elif wrong_response_count == 20:
                                n 1fsqbgl "Ehehe.{w=0.2} You're persistent!{w=0.2} I'll give you that."
                                n 1fsqsml "But if you think I'm giving you a win..."
                                n 1fchgnl "Then you've got another thing coming!"
                                n 1uchbgl "I love {i}you{/i} more,{w=0.1} dummy!"

                            elif wrong_response_count == 50:
                                n 1tnmajl "Wow!{w=0.2} This is like...{w=0.3} the 50th time you've been wrong!{w=0.2} In a row!"
                                n 1tsqsgl "Sounds to me like you're in some serious denial there,{w=0.1} [player]~."
                                n 1nllssl "I don't think I can be bothered counting much more from here..."
                                n 1fsqtsl "So why don't you do me a favour and just accept that I love {i}you{/i} more already?"
                                n 1uchsml "Ehehe."
                                n 1fchbgl "Thanks,{w=0.1} [chosen_endearment]~!"

                            elif wrong_response_count == 100:
                                n 1uwdgsl "...Oh!{w=0.2} And it looks like we have our 100th wrong answer!"
                                n 1fllawl "Dim the lights!{w=0.2} Roll the music!"
                                n 1flrbgl "Now,{w=0.1} audience members -{w=0.1} what does our stubborn participant get?"
                                n 1fsqbgl "They get..."
                                n 1uchgnl "A correction!{w=0.2} Wow!"
                                n 1fsqbgl "And that correction is..."
                                n 1fchbsf "[n_name] loves {i}them{/i} way more!{w=0.2} Congratulations,{w=0.1} dummy!"
                                n 1fsqdvl "And now,{w=0.1} to walk away with the grand prize -{w=0.1} all our guest here needs to do..."
                                n 1fchbsl "...Is give up and admit how wrong they are~!{w=0.2} Ehehe."
                            else:

                                $ player_is_wrong_responses = [
                                    "Nope!{w=0.2} I love {i}you{/i} more!",
                                    "Sorry,{w=0.1} bub!{w=0.2} I definitely love {i}you{/i} more!",
                                    "Ehehe.{w=0.2} Nope~!{w=0.2} We both know I love {i}you{/i} more.",
                                    "Hmm...{w=0.3} nah.{w=0.2} Pretty sure I love {i}you{/i} more!",
                                    "Nooooope~!{w=0.2} I love {i}you{/i} more!",
                                    "Silly [player]~.{w=0.2} I love {i}you{/i} more,{w=0.1} remember?",
                                    "Mmmmmmmm...{w=0.3} nope!{w=0.2} I love {i}you{/i} way more,{w=0.1} [player]~!",
                                    "Come come now,{w=0.1} [player].{w=0.2}  Don't be silly!{w=0.2} I definitely love {i}you{/i} more.",
                                    "Wait...{w=0.3} can you hear that?{w=0.2} Oh!{w=0.2} It's how wrong you are -{w=0.1} I love you more,{w=0.1} dummy!"
                                    "You're only wasting your time,{w=0.1} [player]~.{w=0.2} I love {i}you{/i} waaay more!",
                                    "My,{w=0.1} oh my,{w=0.1} [player].{w=0.2} Don't you know that I love {i}you{/i} more by now?{w=0.2} Ehehe.",
                                    "Uh huh...{w=0.3} Nat hears you,{w=0.1} Nat knows you're wrong.{w=0.1} I love {i}you{/i} more,{w=0.1} you goof!",
                                    "You're adorable when you're in denial,{w=0.1} [player].{w=0.2} Ehehe.{w=0.2} I love {i}you{/i} more~!",
                                    "Aww,{w=0.1} come on now,{w=0.1} [player].{w=0.2} If you {i}really{/i} loved me,{w=0.2} you'd admit I love {i}you{/i} more!"
                                ]
                                $ chosen_random_response = renpy.substitute(random.choice(player_is_wrong_responses))
                                n 1fchbgf "[chosen_random_response]"

                            $ wrong_response_count += 1
                        "Okay, fine. You love me more.":

                            $ player_is_wrong = False
                            n 1tsqbgl "See?{w=0.2} Was that really so hard?"
                            n 1uchtsl "Sometimes you just have to admit you're wrong,{w=0.1} [player]~."
                            n 1nchsml "Ehehe."

                            if wrong_response_count >= 10:
                                n 1nsqsml "Nice try,{w=0.1} though~!"

                            $ Natsuki.calculatedAffinityGain()
                            return

            elif random_response_index == 10:
                n 1ksqsml "Ehehe.{w=0.2} I'll never get tired of hearing that from you,{w=0.1} [player]."
                n 1uchsmf "I love you too!"
                n 1uchbgf "You're my numero uno~."
                $ Natsuki.calculatedAffinityGain()
                return
            else:

                n 1usqbgf "Oh?{w=0.2} Lovey-dovey as usual?"
                n 1uslsmf "You're such a softie,{w=0.1} [player].{w=0.2} Ehehe."
                n 1uchbgf "But...{w=0.3} I'm not gonna complain!{w=0.2} I love you too,{w=0.1} [chosen_endearment]!"
                n 1uchsmf "You always make me feel tall."
                $ Natsuki.calculatedAffinityGain()
                return

            return

        elif Natsuki.isEnamored(higher=True):
            n 1fbkwrf "G-{w=0.1}gah!{w=0.2} [player]!"
            n 1fllwrf "What did I say about making things awkward?{w=0.2} Now it's twice as awkward!"
            n 1fcsemf "Jeez..."
            n 1flremf "Let's just talk about something,{w=0.1} alright?"
            n 1flrpof "Y-{w=0.1}you can fawn over me in your {i}own{/i} time!"
            n 1klrpof "Dummy..."
            $ Natsuki.calculatedAffinityGain()
            return

        elif Natsuki.isHappy(higher=True):
            n 1fskemf "H-{w=0.1}hey! I thought I told you not to just come out with stuff like that!"
            n 1fllemf "Jeez..."
            n 1fcsemf "I-{w=0.1}I don't know if you're trying to win me over,{w=0.1} or what..."
            n 1fcspof "But you're gonna have to try a lot harder than that!"
            return

        elif Natsuki.isNormal(higher=True):
            n 1fskemf "G-{w=0.1}gah!"
            n 1fbkwrf "[player_initial]-{w=0.1}[player]!"
            n 1fnmanl "Stop being gross!"
            n 1fcsanl "Jeez..."
            n 1fllajl "I don't know if you think this is a joke,{w=0.1} or what..."
            n 1fsqaj "But it really isn't funny to me,{w=0.1} [player]."
            return

        elif Natsuki.isUpset(higher=True):
            n 1fcssr "..."
            n 1fsqsr "Talk is cheap,{w=0.1} [player]."
            n 1fsqaj "If you {i}really{/i} care about me..."
            n 1fsqpu "Then {i}prove{/i} it."
            $ Natsuki.percentageAffinityLoss(2.5)
            return
        else:

            n 1fsqpu "..."
            n 1fsqan "You're actually unbelievable,{w=0.1} [player]."
            n 1fsqfu "Do you even {i}understand{/i} what you're saying?"
            n 1fcsfu "..."
            n 1fcspu "You know what?{w=0.2} Whatever.{w=0.2} I don't care anymore."
            n 1fsqfu "Say what you like,{w=0.1} [player].{w=0.2} It's all crap,{w=0.1} just like everything else from you."
            $ Natsuki.percentageAffinityLoss(2)
            return

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_natsukis_hairstyle",
            unlocked=True,
            prompt="Why do you style your hair like that?",
            category=["Fashion"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_natsukis_hairstyle:
    if Natsuki.isEnamored(higher=True):
        n 1tnmaj "Hmm?{w=0.2} My hairstyle?"
        n 1fsqss "Why do you ask,{w=0.1} [player]?{w=0.5}{nw}"
        extend 1fsgsg " Looking for a stylist?"
        n 1fchsm "Ehehe."

    elif Natsuki.isNormal(higher=True):
        n 1tnmpu "Huh?{w=0.2} My hairstyle?"
        n 1fsqaj "Wait...{w=0.75}{nw}"
        extend 1fnmeml " a-{w=0.1}are you messing with me?{w=0.2} What do you mean?"
        n 1fslpo "You better not be teasing me,{w=0.1} [player]..."

    elif Natsuki.isDistressed(higher=True):
        n 1nnmsl "...Huh?{w=0.2} Oh.{w=0.2} My hair."
        n 1flrsl "I'm...{w=0.3} surprised you care enough to ask about that."
    else:

        n 1fsqfu "Because I {i}like{/i} it that way.{w=0.75}{nw}"
        extend 1fnman " That good enough for you,{w=0.3} {i}[player]{/i}?"
        n 1fsqantsb "And why would you even {i}care{/i} anyway?{w=1}{nw}"
        extend 1fsqupltsb " You haven't cared about me so far."
        n 1fcsanltsa "Jerk."
        return

    n 1nnmpu "Well,{w=0.1} anyway."
    n 1ullpu "I never really thought about it that much,{w=0.1} honestly."

    if Natsuki.isNormal(higher=True):
        if Natsuki.isWearingHairstyle("jn_hair_twintails"):
            n 1ulrpo "I just thought twintails would look kinda cute on me."
        else:

            n 1ulrpo "I think this hairstyle looks kinda cute on me."

        n 1fsqpo "...Yeah,{w=0.1} yeah.{w=0.2} I know what you're thinking,{w=0.1} [player]."

        if Natsuki.isEnamored(higher=True):
            n 1ksqsm "Was I wrong...?"
            n 1fchbg "Ehehe.{w=0.2} I thought not."

        if Natsuki.isWearingHairstyle("jn_hair_twintails"):
            n 1ullaj "Besides,{w=0.1} I had a whole bunch of ribbon lying around from my craft stuff {w=0.1}-{w=0.5}{nw}"
            extend 1fcsbg " so it isn't like I had to go {i}buy{/i} anything new to try twintails out."
    else:

        if Natsuki.isWearingHairstyle("jn_hair_twintails"):
            n 1nnmsl "I guess I just liked the idea of twintails."
            n 1nlrpu "Besides,{w=0.1} I had some spare ribbons lying around anyways.{w=0.5}{nw}"
            extend 1nsrsr " Not like I had to {i}buy{/i} anything to try doing twintails."
        else:

            n 1nnmsl "I guess I just like this hairstyle."

    n 1ulraj "As for the bangs,{w=0.1} I...{w=0.3} always found it difficult to get my hair cut."

    if Natsuki.isNormal(higher=True):
        n 1flraj "It just costs so much,{w=0.1} you know?{w=0.2} It's super dumb!"
        n 1fnman "Like...{w=0.3} I don't get it at all!"
        n 1fllan "And the annoying thing is that if I were a guy,{w=0.1} it'd be {i}way{/i} cheaper!{w=0.5}{nw}"
        extend 1fbkwrean " What's up with that?!"
        n 1fcspuesi "Ugh...{w=1}{nw}"
        extend 1nsrpo " but yeah."
    else:

        n 1nlrsl "I was always kinda short when it came to getting it cut."
        n 1fsqsl "...And no,{w=0.1} {i}not{/i} in the physical sense."

    if Natsuki.isWearingAccessory(jn_outfits.get_wearable("jn_accessory_hairband_red")):
        n 1ullaj "As for my hairband?{w=0.2} It's just to keep my hair out of my eyes."
    else:

        n 1ullaj "I'm not wearing it now,{w=0.1} but my old hairband was just to keep my hair out of my eyes."

    if Natsuki.isNormal(higher=True):
        n 1fllss "Looking good is a bonus,{w=0.1} but I mostly just got tired of brushing my hair out of my face."
        n 1nsrca "Especially with those bangs!"
        n 1unmaj "Anyway..."

    n 1tllaj "Have I thought about other hairstyles?{w=0.2} Well..."

    if not Natsuki.isWearingHairstyle("jn_hair_twintails"):
        if Natsuki.isEnamored(higher=True):
            n 1tsqsml "Is that not what I'm doing right now?"
            extend 1fchsml " Ehehe."

        elif Natsuki.isNormal(higher=True):
            n 1ullbo "I think that kinda speaks for itself,{w=0.1} really.{w=0.2} I {i}am{/i} trying out a different one..."
        else:

            n 1nsqsl "...Go figure,{w=0.1} [player]."
    else:

        if Natsuki.isEnamored(higher=True):
            $ chosen_tease = jn_utils.getRandomTease()
            n 1fcssml "I'm pretty sure I already let my hair down around you,{w=0.1} [chosen_tease].{w=0.2} That qualifies, right?"
            n 1uchgnlelg "Ahaha!"

        elif Natsuki.isNormal(higher=True):
            n 1unmaj "You know what they say,{w=0.1} [player]."
            n 1fnmbg "If it ain't broke,{w=0.1} don't fix it!"
            n 1uchgn "Ehehe."
        else:

            n 1fslaj "...At this point,{w=0.1} [player]?{w=0.2} I'd rather you stayed {i}out{/i} of my hair."
            n 1fsqbo "Thanks."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_integrity",
            unlocked=True,
            prompt="Having integrity",
            category=["Society", "You"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_integrity:
    n 1ullaj "You know,{w=0.1} [player]..."
    n 1nnmaj "I feel like nowadays,{w=0.1} everyone is trying to make a point,{w=0.1} or preach something."
    n 1flrem "Especially with social media and all that everywhere -{w=0.1} it's crazy!"
    n 1fllem "Like...{w=0.3} there's posts telling you this is bad,{w=0.1} others asking why you don't support something else..."
    n 1fcsan "And of course,{w=0.1} {i}everyone{/i} is tuned in to that -{w=0.1} so it leaks into real life as well!"
    n 1flrsl "Ugh...{w=0.3} it can't only be me that finds it all exhausting,{w=0.1} right?"
    n 1unmaj "I think it makes it kinda easy to lose track of what you really like,{w=0.1} or what you stand for."
    n 1ullaj "Which...{w=0.3} is actually something I really wanted to talk to you about,{w=0.1} [player]."
    n 1fllpu "I'm not saying you should just ignore everyone else,{w=0.1} or never consider other points of view."
    n 1fnmpo "That's just being ignorant."
    n 1knmaj "But...{w=0.3} don't just let other people's opinions or conceptions completely overwrite your own,{w=0.1} 'kay?"
    n 1fnmbo "At least not without a fight,{w=0.1} at least."
    n 1fnmpu "{i}You{/i} are your own master,{w=0.1} [player] -{w=0.1} you have your own opinions,{w=0.1} your own values:{w=0.1} and that's super important!"
    n 1fcsbg "I mean,{w=0.1} look at me!"
    n 1fllaj "So what if someone says what I'm into sucks?{w=0.2} Or if I should be following something more popular?"
    n 1fnmsf "It isn't hurting anyone,{w=0.1} so who are they to judge and tell me what I should be enjoying?"
    n 1fcsbg "It's my life,{w=0.1} so they can jog on!"
    n 1nnmsr "Anyway...{w=0.3} I guess what I'm saying is don't be afraid to stand up for what matters to you,{w=0.1} [player]."
    n 1fcsaj "There's gonna be times you'll be wrong,{w=0.1} but don't let it get to you!"
    n 1flrsl "I just don't like the idea of people being pushed into what isn't right for them."
    n 1nnmpu "That being said,{w=0.1} [player]..."

    if Natsuki.isEnamored(higher=True):
        n 1ksqsm "I'm pretty sure we both know what's right for each other by now,{w=0.1} huh?"
        n 1fcsbglesssbl "Ahaha."

        if Natsuki.isLove(higher=True):
            n 1uchsml "Love you,{w=0.1} [player]~!"

    elif Natsuki.isAffectionate(higher=True):
        n 1ksqsm "I'm pretty sure I know what's right for you..."
        n 1fcsbgledz "Spending more time with me!"
        extend 1nchgnedz " Ehehe."
    else:

        n 1unmss "I'm sure I can help you find what's right for you."
        n 1fllss "That's what friends are for,{w=0.1} right?"
        n 1fcsbg "{i}Especially{/i} ones like me!{w=0.5}{nw}"
        extend 1nchgnedz " Ehehe."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_favourite_animal",
            unlocked=True,
            prompt="What's your favourite animal?",
            category=["Animals", "Nature"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_favourite_animal:
    if Natsuki.isNormal(higher=True):
        n 1fsqsr "Hammies."
        n 1fcssm "That's barely even a question for me,{w=0.1} [player]."
        n 1uwdaj "Like...{w=0.3} if you've seen them,{w=0.1} can you blame me?"
        n 1fcspu "They're...{w=0.5}{nw}"
        n 1fspgsedz "{i}Adorable{/i}!!"
        n 1fbkbsl "I just love everything about them...{w=0.3} the little paws,{w=0.1} the bright eyes, those puffy cheeks..."
        n 1fspbgl "And that tiny little tail...{w=0.3} oh my gosh!{w=0.2} It's just precious!"
        n 1fllan "It really winds me up when people call them boring,{w=0.1} or unaffectionate though.{w=0.2} Like...{w=0.3} have you ever watched one?"
        n 1fnmaj "They all have their own little personalities,{w=0.1} just like any other animal -{w=0.1} only smaller!"
        n 1uwdaj "And if you bond with them,{w=0.1} they aren't afraid to show it -{w=0.1} I've seen videos of them following their owners around,{w=0.1} and even leaping into their hands!"
        n 1fchbg "Plus they're easy to take care of,{w=0.1} too!"
        n 1fchsm "Just top up their food and change their water daily,{w=0.1} and clean their cage out once a week -{w=0.1} no sweat."
        n 1nllpu "Hmm..."
        n 1unmpu "You know,{w=0.1} [player]...{w=0.3} it does get a little quiet when you aren't around,{w=0.1} if you know what I'm getting at..."
        n 1fnmsm "Perhaps one day we could have our own furry friend here too?{w=0.1} Ehehe."
        n 1fllss "Don't worry though,{w=0.1} [player]..."
        n 1ucssm "I don't mind taking care of it."
        n 1fchgn "...But you're in charge of the supplies!"

        if Natsuki.isEnamored(higher=True):
            n 1fchbg "Oh,{w=0.1} and relax -{w=0.1} I'll make sure it'll be well tamed!"
            n 1uslbg "Or..."
            n 1usqts "At least about as tame as you,{w=0.1} huh [player]?{w=0.2} Ahaha!"

            if Natsuki.isLove(higher=True):
                n 1uchbg "Love you~!"

    elif Natsuki.isDistressed(higher=True):
        n 1fsqpu "Hamsters,{w=0.1} if it matters."
        n 1fllpu "Why?{w=0.2} I don't know.{w=0.2} I just think they're cute."
        n 1nllbo "I think people actually underestimate how expressive they can be,{w=0.1} too."
        n 1nnmbo "They're like most animals really -{w=0.1} they all have their own personalities."
        n 1nnmaj "I guess they're pretty easy to take care of as well,{w=0.1} so there's that."
        n 1nlrsl "..."
        n 1flrsl "...I'd be lying if I said I hadn't been thinking about getting one myself..."
        n 1fsqpu "But honestly,{w=0.1} [player]?{w=0.2} If you've shown you can't take care of {i}me{/i}?"
        n 1fcsan "...Then I don't think it'd be fair to bring one here,{w=0.1} either.{w=0.2} Heh."
    else:

        n 1fsqpu "Heh.{w=0.2} Really?{w=0.2} My favourite animal...?"
        n 1fcsantsa "Not you,{w=0.1} [player].{w=0.2} That's for sure."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_favourite_drink",
            unlocked=True,
            prompt="What's your favourite drink?",
            category=["Food"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_favourite_drink:
    if Natsuki.isAffectionate(higher=True):
        n 1unmbg "Ooooh!{w=0.2} My favourite drink?"

    elif Natsuki.isNormal(higher=True):
        n 1unmaj "Mmm?{w=0.2} My favourite drink?"

    elif Natsuki.isDistressed(higher=True):
        n 1nllbo "Huh?{w=0.2} Oh.{w=0.1} My favourite drink."
    else:

        n 1fslsf "...I can't understand why you'd care,{w=0.1} [player]."
        n 1fsqsf "So...{w=0.3} why should I?"
        n 1fsqan "Water.{w=0.2} There's an answer for you.{w=0.2} Happy?"
        n 1fcsanltsa "Now just go away..."
        return

    if Natsuki.isNormal(higher=True):
        n 1ullaj "I gotta say...{w=0.3} it depends on the weather more than anything."
        n 1tnmaj "I mean...{w=0.3} what kind of dope would order an iced drink in the middle of winter?!"
        n 1fllss "But anyway..."
        n 1fcsbg "If it's cold out,{w=0.1} then hot chocolate.{w=0.2} No questions,{w=0.1} no doubts."
        n 1uchgn "In the depths of winter,{w=0.1} you definitely won't get a better option than that!"

        if Natsuki.isAffectionate(higher=True):
            n 1fcsbg "And yeah,{w=0.1} [player] -{w=0.1} whipped cream,{w=0.1} marshmallows -{w=0.1} all of it.{w=0.2} The complete works."
            n 1uchgn "...And I wouldn't accept anything less!"
            n 1fllbg "I mean,{w=0.1} think about it -{w=0.1} if you're getting hot chocolate,{w=0.1} you've already kinda lost on the health front."
            n 1uchgn "So you might as well go all in,{w=0.1} right?{w=0.2} Ahaha."

            if Natsuki.isLove(higher=True):
                n 1fcsdvl "Besides,{w=0.2} I'm not too worried -{w=0.1} we'll just share the calories,{w=0.1} [player]~."

        n 1unmaj "As for warmer weather...{w=0.3} that's a little trickier,{w=0.1} actually."
        n 1fslsr "Let me think..."
        n 1fsrsr "..."
        n 1fchbs "Aha!{w=0.2} I got it!"
        n 1unmbg "It's gotta be those milkshakes,{w=0.1} but from one of those places where you get to choose what goes in it!"
        n 1fsqsm "I don't just mean picking a flavor,{w=0.1} [player]..."
        n 1fchgn "I mean where you can pick any combination of ingredients you want!"
        n 1fllss "Well...{w=0.3} as long as it blends,{w=0.1} anyway."
        n 1ncssm "All kinds of sweets,{w=0.1} any type of milk..."

        if Natsuki.isAffectionate(higher=True):
            n 1ucssm "Though if I had to pick a favourite?"
            n 1fcsbg "It's gotta be strawberries and cream,{w=0.1} obviously."
            n 1fllbgl "And...{w=0.3} maybe with just a dash of chocolate too?{w=0.2} Ehehe."
        else:

            n 1fchbg "Yeah.{w=0.2} That's the real deal!"

        n 1fllpo "Jeez...{w=0.3} all this talk about drinks is making me kinda thirsty,{w=0.1} actually.{w=0.2} So on that note..."
        n 1fnmbg "You need to stay hydrated too,{w=0.1} [player] -{w=0.1} whatever the weather!"
    else:

        n 1flrsl "I suppose it depends what the weather is like."
        n 1fnmbo "Hot chocolate if it's cold out,{w=0.1} though I'm not very picky I guess."
        n 1fllaj "As for warmer weather..."
        n 1fllsl "I don't really know.{w=0.2} Whatever is fine."
        n 1fsqsl "Heh.{w=0.2} Though at this rate,{w=0.1} I shouldn't expect much more than tap water from you anyway.{w=0.2} Right,{w=0.1} [player]?"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_school_uniform",
            unlocked=True,
            prompt="What do you think of your school uniform?",
            category=["Fashion"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_school_uniform:
    if Natsuki.isLove(higher=True):
        n 1fsqctl "Oho?{w=0.2} Does [player] like a girl in uniform?"
        n 1ksqaj "Wow...{w=0.3} you're even {i}more{/i} gross than I thought."
        n 1fsqsm "..."
        $ chosen_tease = jn_utils.getRandomTease()
        n 1uchgn "Oh come on,{w=0.1} [chosen_tease]!{w=0.2} You always get all sulky when I call you that!{w=0.2} I just can't resist."
        n 1fchsm "Ehehe.{w=0.2} So anyway..."

    elif Natsuki.isAffectionate(higher=True):
        n 1unmaj "Huh?{w=0.2} My school uniform?"
        n 1fsqsm "...Ehehe."
        n 1fcsbgl "Why do you ask,{w=0.1} [player]?{w=0.2} Did {i}you{/i} wanna wear it or something?"
        n 1fchgn "Oh!{w=0.2} We can play dress-up!{w=0.2} Wouldn't you like that,{w=0.1} [player]?{w=0.2} It'll be so much fun!"
        n 1uchbselg "I bet I could make you look so cute~.{w=0.1} Ahaha!"
        n 1nllss "Well anyway,{w=0.1} putting jokes aside..."

    elif Natsuki.isNormal(higher=True):
        n 1tnmaj "My school uniform?{w=0.2} That's...{w=0.3} kind of a weird thing to ask me about,{w=0.1} huh?"
        n 1nslaj "Well,{w=0.1} whatever.{w=0.2} I'll let it slide...{w=0.3} this time."

    elif Natsuki.isDistressed(higher=True):
        n 1nsraj "...Huh?{w=0.2} Oh,{w=0.1} the school uniform."
        n 1nsqsl "I...{w=0.3} don't know what you're expecting to hear from me,{w=0.1} [player]."
        n 1fsqsl "I had to wear it for school.{w=0.2} That's the point of a uniform,{w=0.1} if you hadn't realized."
        n 1fsrsf "It doesn't matter if I like it or not."
        n 1fsqbo "...And it matters even less if you do."
        return
    else:

        n 1fsran "Heh.{w=0.2} I like it more than {i}you{/i}.{w=0.2} Jerk."
        return

    n 1unmaj "It's alright,{w=0.1} I guess.{w=0.2} I actually really like the warm colours!"
    n 1nnmss "They're way easier on the eyes than a lot of the other uniforms I've seen around."
    n 1nsqsr "But Oh.{w=0.2} My.{w=0.2} Gosh.{w=0.2} [player]."
    n 1fcsan "The layers.{w=0.2} So many layers."
    n 1fllem "Who even thought someone needs that much clothing?!{w=0.2} For school,{w=0.1} of all places?!"
    n 1fbkwr "I mean...{w=0.3} do you even {i}know{/i} what wearing all that clothing in summer is like?!{w=0.2} It's {i}horrible{/i}!"
    n 1flrpo "And the blazer...{w=0.3} ugh!{w=0.2} It's actually the worst thing ever."
    n 1fsqpo "Like yeah,{w=0.1} I could take some off between class,{w=0.1} but I had to put it all back on when I went in."
    n 1fllpo "...Or get told off.{w=0.2} {i}Again{/i}.{w=0.2} I honestly have no idea how Sayori got away with hers being so scruffy."
    n 1fcsan "And all of the uniform stuff is super expensive too!{w=0.2} Talk about a kick in the teeth!"
    n 1fslan "Jerks."
    n 1fslsr "Ugh...{w=0.3} I seriously wish uniforms were banned or something."
    n 1flrpo "I guess it could be worse.{w=0.5}{nw}"
    extend 1ksrsl " At least it kept me warm when it mattered."

    if not Natsuki.isWearingClothes("jn_clothes_school_uniform"):
        n 1nchgn "...And I'm not wearing it now,{w=0.1} at least!{w=1}{nw}"
        extend 1fcsbg " Always a plus."
        n 1ullaj "That being said...{w=0.75}{nw}"
    else:

        n 1ulraj "But...{w=0.75}{nw}"

    extend 1unmbo " what about you,{w=0.1} [player]?"
    show natsuki 1tnmpu at jn_center

    menu:
        n "Did you have to wear any uniform at school?"
        "Yes, I had to wear uniform.":

            n 1fcsbg "Aha!{w=0.2} So you know the struggle too,{w=0.1} huh?"
        "No, I didn't have to wear uniform.":

            n 1fslsr "..."
            n 1fsqsr "...Lucky."
        "I have to wear uniform now.":

            n 1fchgn "Then you have my condolences,{w=0.1} [player]!{w=0.2} Ahaha."
            n 1fcsbg "Good to know we're on the same page,{w=0.1} though."
        "I don't have to wear uniform now.":

            n 1fslsr "..."
            n 1fsqsr "...Lucky."

    n 1ullss "Well,{w=0.1} anyway..."

    if Natsuki.isLove(higher=True):
        n 1fllss "I still don't particularly {i}like{/i} wearing it..."
        n 1uslbgl "But...{w=0.3} I think I can put up with it.{w=0.2} Just for you,{w=0.1} [player]~."
        n 1usrdvl "Ehehe."

    elif Natsuki.isAffectionate(higher=True):
        n 1usrdvl "I-{w=0.1}if you don't mind it,{w=0.1} [player]?"
        n 1fllbgl "I suppose it has that going for it too,{w=0.1} a-{w=0.1}at least..."

    elif Natsuki.isNormal(higher=True):
        n 1fcsbg "I guess at least I never had to learn how to do a tie!"
        extend 1nchgn " Ehehe."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_flying",
            unlocked=True,
            prompt="Have you ever flown anywhere?",
            category=["Transport"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_flying:
    if Natsuki.isEnamored(higher=True):
        n 1uwdbg "Ooh!{w=0.2} Flying?{w=0.2} Like on a plane?"
        n 1fllun "Nnn...{w=0.3} I wish I could say I have,{w=0.1} [player]..."
        n 1fchbg "Don't get me wrong though!{w=0.2} I'd {i}totally{/i} fly somewhere new if I could!"
        n 1fslsl "It's just...{w=0.3} the price of it all,{w=0.1} you know?"
        n 1kllsl "I've never had a passport,{w=0.1} but it's mainly the tickets and everything beyond that..."

    elif Natsuki.isHappy(higher=True):
        n 1unmaj "Huh?{w=0.2} Flying?{w=0.2} Like on a plane or something?"
        n 1kllaj "I...{w=0.3} wish I could say I have,{w=0.1} [player]."
        n 1fnmbg "Don't get me wrong though!{w=0.2} I'd love to jet off somewhere.{w=0.2} Like for a vacation or something!"
        n 1flrpo "It's just the cost that stops me, you know?"
        n 1fcspo "Even if I had a passport, there's just so many things to pay out for..."

    elif Natsuki.isNormal(higher=True):
        n 1unmaj "Oh?{w=0.2} Like flying on a plane or whatever?"
        n 1kllbo "Uhmm..."
        n 1klraj "I...{w=0.3} never really had the opportunity to fly anywhere,{w=0.1} [player]."
        n 1unmaj "I don't even have a passport or anything like that,{w=0.1} and even if I did?"
        n 1nsraj "It isn't like tickets are...{w=0.3} affordable,{w=0.1} if you know what I mean?"
        n 1nslpo "Especially to someone in my...{w=0.3} position."

    elif Natsuki.isDistressed(higher=True):
        n 1nnmbo "Flying?{w=0.2} Like...{w=0.3} on a plane?"
        n 1fnmsf "No,{w=0.1} [player].{w=0.2} I haven't."
        n 1fllsf "I've never owned a passport,{w=0.1} and it's way too expensive anyway."
        n 1fnmaj "I don't really like the idea of the environmental impact either."
        n 1fsqaj "...But something tells me you don't really care about that last point,{w=0.2} do you?"
        n 1flrca "You know...{w=0.3} just going by my experience so far."
        n 1fsqca "...Am I {i}wrong{/i}?"
        return
    else:

        n 1fsqanean "No,{w=0.1} [player].{w=0.2} I haven't.{w=0.2} And I probably never will."
        n 1fcsanltsa "Gloat all you want.{w=0.2} I don't give a crap if you have."
        return

    n 1ullaj "Besides,{w=0.1} I try not to feel too bad about it.{w=0.2} It's way better for the environment if I don't,{w=0.1} anyway!"
    n 1nnmbo "Flying places is pretty polluting.{w=0.2} I think I'd just feel selfish if I was constantly zooming around,{w=0.1} knowing how bad that is for everyone."
    n 1nllss "But...{w=0.3} that's just me,{w=0.1} I guess."
    n 1unmaj "What about you,{w=0.1} [player]?"
    menu:
        n "Are you a frequent flier?"
        "Yes, I fly regularly.":

            n 1fcsbg "Oh?{w=0.2} Well check you out,{w=0.1} [player]!"
            n 1fslpo "I guess it's {i}plane{/i} to see how well you're doing for yourself?"
            n 1fchbg "Ehehe."
            n 1fnmaj "Just try to avoid racking up too many miles,{w=0.1} [player]."
            n 1fllss "You gotta think about the planet too,{w=0.1} you know..."

            if Natsuki.isEnamored(higher=True):
                n 1fslnvf "E-{w=0.1}especially if people we really care about are in it.{w=0.2} Ahaha..."

            elif Natsuki.isHappy(higher=True):
                n 1fchgn "No excuses,{w=0.1} [player]! Ehehe."

            $ persistent._jn_player_has_flown = True
        "I fly sometimes.":

            n 1unmss "Ooh,{w=0.1} okay!{w=0.2} So the odd vacation or family flight then?"
            n 1fslsm "I see,{w=0.1} I see..."
            n 1fcsbg "Well,{w=0.1} good for you,{w=0.1} [player]!{w=0.2} Everyone should get the chance to explore the world."
            n 1kslss "Hopefully I'll get the chance someday too."

            if Natsuki.isEnamored(higher=True):
                n 1fsqsg "I hope you'll be available when that happens,{w=0.1} [player]."
                n 1fchgnl "You're gonna be my tour guide,{w=0.1} whether you like it or not!"

            elif Natsuki.isHappy(higher=True):
                n 1fsqsm "You better be handy when that happens,{w=0.1} [player]..."
                n 1fchgn "We'll see how good a guide you are!"

            $ persistent._jn_player_has_flown = True
        "I've flown before.":

            n 1fsqct "Oh?{w=0.2} So you've already earned your wings,{w=0.1} huh?"
            n 1tllaj "Hmm...{w=0.3} I wonder where you went?"
            n 1fnmaj "You gotta promise to tell me if you fly again,{w=0.1} 'kay?"
            n 1fchgn "I wanna hear all about it!"

            $ persistent._jn_player_has_flown = True
        "I've never flown.":

            n 1fcsbg "Then that's just another thing we have in common,{w=0.1} [player]!"
            n 1fsqss "I guess you could say..."
            n 1fsqdv "We're both just {i}well grounded{/i} people,{w=0.1} huh?"
            n 1fchgnelg "Ahaha!"

            $ persistent._jn_player_has_flown = False

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_are_you_into_cars",
            unlocked=True,
            prompt="Are you into cars?",
            category=["Transport"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_are_you_into_cars:
    $ already_discussed_driving = False


    if get_topic("talk_driving"):
        $ already_discussed_driving = get_topic("talk_driving").shown_count > 0

    elif get_topic("talk_are_you_into_cars"):
        $ already_discussed_driving = get_topic("talk_are_you_into_cars").shown_count > 0

    if already_discussed_driving:

        if Natsuki.isNormal(higher=True):
            n 1unmaj "Eh?{w=0.2} Cars?"
            n 1fchgn "Jeez,{w=0.1} you know I can't drive,{w=0.1} dummy!{w=0.2} I don't have a reason to be into cars!"
            n 1nlrbg "Well,{w=0.1} anyway..."

        elif Natsuki.isDistressed(higher=True):
            n 1fcssl 1nnmsl "[player].{w=0.2} You know I can't drive.{w=0.2} Why would you think I'd be into cars,{w=0.1} of all things?"
            n 1fllsl 1nllsl "...Fine.{w=0.2} Whatever."
        else:

            n 1fsqpu "...Really?"
            n 1fsqan "You know I can't drive.{w=0.2} So I'm not even going to {i}pretend{/i} I care if you're into that,{w=0.1} [player]."
            n 1fnmfultsc "Besides...{w=0.3} I bet you'd {i}never{/i} treat your {i}precious{/i} car like you treat me,{w=0.1} huh?"
            return
    else:


        if Natsuki.isNormal(higher=True):
            n 1unmaj "Huh?{w=0.1} Am I into cars?"
            n 1fllnv "Well...{w=0.3} to tell you the truth,{w=0.1} [player]?"
            n 1unmaj "...I've never actually owned a license."
            n 1flrpo "I don't even think I could afford to learn!"
            n 1nnmaj "So I've never really been drawn to them honestly."

        elif Natsuki.isDistressed(higher=True):
            n 1fnmsr "I can't drive,{w=0.1} [player].{w=0.2} I don't have a license either;{w=0.1} learning was always too expensive."
            n 1fnmpu "So...{w=0.3} why would I be into that?{w=0.1} I literally can't {i}afford{/i} to be."
        else:

            n 1fcsan "Newsflash,{w=0.1} jerk.{w=0.2} I {i}can't{/i} drive,{w=0.1} and I can't even afford to {i}learn{/i}."
            n 1fsqan "So you tell {i}me{/i} -{w=0.1} why would I be into cars?{w=0.2} And if I was,{w=0.1} why the hell would I want to talk to {i}you{/i} about them?"
            n 1fcspu "...Heh.{w=0.2} Yeah,{w=0.1} I thought so.{w=0.2} We're done here,{w=0.1} [player]."
            return

    if Natsuki.isNormal(higher=True):
        n 1unmsm "I can appreciate the talent that goes into them -{w=0.1} I think it's actually pretty cool how expressive they can be!"
        n 1nllss "Like...{w=0.3} the design languages of all the different brands,{w=0.1} the engineering that goes into them and all that."
        n 1fchbg "It's pretty insane how much work goes into it;{w=0.1} and that's definitely something I have respect for!"
        n 1fsqsm "What about you though, [player]?{w=0.2} You {i}did{/i} bring it up,{w=0.1} but I thought I'd ask anyway..."
        menu:
            n "Are you into cars?"
            "Yes! I'm into my cars.":



                if persistent.jn_player_can_drive is None:
                    n 1tllbo "Huh.{w=0.2} I wasn't actually sure if you could even drive,{w=0.1} but I suppose that doesn't matter really."
                    n 1fsqsm "I guess being a petrolhead isn't an exclusive club,{w=0.1} huh?"
                    n 1uchbg "Ahaha."


                elif persistent.jn_player_can_drive:
                    n 1fsgbg "Well,{w=0.1} color {i}me{/i} surprised."
                    n 1fchgn "Ehehe."
                    n 1fcsbg "Don't worry,{w=0.1} I had you figured for the sort,{w=0.2} [player]."
                    n 1fchbg "But hey -{w=0.1} whatever floats your boat!"
                else:


                    n 1unmaj "That's...{w=0.3} actually pretty surprising to hear from you,{w=0.1} [player]."
                    n 1nllaj "You know,{w=0.1} since you said you can't drive and all that..."
                    n 1fchbg "But I guess it's like anything -{w=0.1} you don't have to be doing it to be a fan,{w=0.1} and that's fine with me!"
            "I don't care much for them.":

                n 1ullss "I guess that's fair enough -{w=0.1} and don't worry,{w=0.1} I completely get it."
                n 1nnmsm "But if someone's into that kind of thing,{w=0.1} who are we to judge,{w=0.1} after all?"
            "No, I'm not into them.":

                n 1ulraj "...Huh.{w=0.2} That's kinda weird -{w=0.1} then why did you bring it up,{w=0.1} [player]?"

                if persistent.jn_player_can_drive:
                    n 1tlraj "Especially if you can drive!"
                    n 1tllpu "Huh..."

                n 1fchbg "Well,{w=0.1} anyway.{w=0.2} Fair enough I guess!"
    else:

        n 1flrsr "I guess I can respect the work and talent that goes into designing and making one..."
        n 1fnmbo "But it's just the same as anything else."
        n 1fsqbo "...I suppose you're into your cars then,{w=0.1} are you?"
        n 1fcspu "Heh."
        n 1fsqpu "It'd be nice if you extended that respect to {i}people{/i} too,{w=0.1} [player]."
        n 1fsqsr "{i}Just saying.{/i}"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_how_do_you_feel_about_me",
            unlocked=True,
            prompt="How do you feel about me?",
            category=["Natsuki", "Romance", "You"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_how_do_you_feel_about_me:
    if Natsuki.isLove(higher=True):

        if persistent.jn_player_love_you_count > 0:
            n 1kwmpof "[player]...{w=0.3} isn't it obvious? You know I love you already,{w=0.1} right?"
            n 1fllpol "Jeez...{w=0.3} you really are a dork sometimes,{w=0.1} you know."
            n 1kllssl "But...{w=0.3} I kinda like that silly part of you,{w=0.1} [player]."
            n 1nwmbgl "Never change,{w=0.1} 'kay? Ehehe."
            n 1nchbgl "Love you,{w=0.1} [player]~!"
        else:

            n 1fcsanf "Nnnnnnn-!"
            n 1fnmanf "C-{w=0.1}come on! Isn't it obvious by now? Jeez...{w=0.5}{nw}"
            n 1fllpof "Do I really have to spell it out for you,{w=0.1} [player]?"
            n 1fcspolesi "Ugh...{w=0.5}{nw}"
            n 1fsqssl "Heh.{w=0.2} Actually,{w=0.1} you know what?"
            n 1fsqbgl "I'll let you figure it out."
            n 1fslajl "And no,{w=0.1} before you ask -{w=0.1} you've had enough hints already."
            n 1fllpol "Dummy..."

        return

    elif Natsuki.isEnamored(higher=True):
        n 1fcsanf "Uuuuuu-!"
        n 1fskwrf "A-{w=0.1}are you trying to put me on the spot or something,{w=0.1} [player]?"
        n 1fllemf "Jeez...{w=0.5}{nw}"
        n 1fcseml "You should {i}know{/i} what I think of you by now...{w=0.5}{nw}"
        n 1fllpol "...{w=0.5}{nw}"
        n 1kcspol "...{w=0.3}Fine."
        n 1fcspol "I...{w=0.3} like...{w=0.3} you,{w=0.1} [player].{w=0.2} A bunch."
        n 1fbkwrf "T-{w=0.1}there!{w=0.2} Happy now?!"
        n 1kllsrl "Sheesh..."
        return

    elif Natsuki.isAffectionate(higher=True):
        n 1fskemf "H-{w=0.1}huh? How do I feel about you?"
        n 1fbkwrf "W-{w=0.1}what're you asking me about that for?!"
        n 1fllpol "Sheesh,{w=0.1} [player]...{w=0.3} you'll make things all awkward at this rate..."
        n 1fcseml "You're fine,{w=0.1} so you don't need to keep bugging me about it!"
        n 1flrunl "Jeez..."
        return

    elif Natsuki.isHappy(higher=True):
        n 1uskemf "H-huh?!"
        n 1fllbgl "O-oh! Ahaha..."
        n 1nllaj "Well,{w=0.1} I mean...{w=0.5}{nw}"
        n 1ullaj "You're pretty fun to be with,{w=0.1} all things considered."
        n 1fllnvl "So...{w=0.3} yeah...."
        return

    elif Natsuki.isNormal(higher=True):
        n 1uskeml "H-{w=0.1}huh?!"
        n 1fllbg "O-oh!"
        n 1unmaj "I mean...{w=0.3} you're alright...{w=0.3} I guess?"

        if not persistent.jn_player_first_farewell_response:
            n 1flleml "W-{w=0.1}what did you expect?{w=0.5}{nw}"
            extend 1fnmpol " We've {i}literally{/i} just met!"

        n 1nnmpu "That's about all I can say so far,{w=0.1} so...{w=0.3} yeah."
        n 1nllca "...{w=0.5}{nw}"
        n 1nlraj "So...{w=0.3} where were we?"
        return

    elif Natsuki.isUpset(higher=True):
        n 1fsqaj "...{w=0.3}Oh? That matters to you now,{w=0.1} does it?"
        n 1fsqbo "Then tell me,{w=0.1} [player]."
        n 1fnmun "Why did you keep hurting my feelings like that?"
        n 1fcsun "...{w=0.5}{nw}"
        n 1fllan "I don't have much patience for jerks,{w=0.1} [player]."
        n 1fnmaj "I don't know if you're trying to be funny or what,{w=0.1} but knock it off.{w=0.2} Got it?"
        n 1fsqsr "Thanks."
        return

    elif Natsuki.isDistressed(higher=True):
        n 1fsqsr "...{w=0.3}Let's just cut the crap."
        n 1fcsan "You've hurt me,{w=0.1} [player].{w=0.2} You've hurt me again,{w=0.1} and again."
        n 1fnmfu "You've done it so many times now."
        n 1fnman "So you tell me."
        n 1fsqpu "What the hell would {i}you{/i} think of someone who did that to you?"
        n 1fcspu "...{w=0.5}{nw}"
        n 1fsqan "You're on thin ice,{w=0.1} [player].{w=0.2} Got it?"
        return

    elif Natsuki.isBroken():
        $ already_discussed_relationship = get_topic("talk_how_do_you_feel_about_me").shown_count > 0
        if already_discussed_relationship:
            n 1fsqpultse "...Wow.{w=0.2} Really?"
        else:

            n 1fsqputsb "...{w=0.3}I have no words for how I feel about {i}you{/i}."
            n 1fsqfultseean "Don't freaking test me, {i}[player]{/i}."

        return
    else:

        n 1fsqunltse "...{w=1}...{w=1}{nw}"
        n 1fcsanltda "...{w=1}..."
        return

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_are_you_into_cosplay",
            unlocked=True,
            prompt="Are you into cosplay?",
            category=["Fashion", "Media", "Society"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_are_you_into_cosplay:
    $ already_unlocked_cosplay_outfits = jn_outfits.get_outfit("jn_trainer_cosplay").unlocked and jn_outfits.get_outfit("jn_sango_cosplay").unlocked

    if Natsuki.isEnamored(higher=True):
        if already_unlocked_cosplay_outfits:
            n 1tnmpu "Eh?{w=0.5}{nw}"
            extend 1tsqsf " Cosplay {i}again{/i}, [player]?"
            n 1fllpo "Yeesh..."

            if Natsuki.isWearingClothes("jn_clothes_trainer_cosplay") or Natsuki.isWearingClothes("jn_clothes_sango_cosplay"):
                n 1fsqpol "As if having me {i}wearing{/i} cosplay wasn't already enough for you..."
                n 1fnmeml "It's all you wanna {i}talk{/i} about too!"
                n 1fcseml "I'm not your own personal dress-up doll,{w=0.75}{nw}"
                extend 1fsrpol " you know..."
            else:

                n 1nslaj "You know,{w=0.75}{nw}"
                extend 1fsqajl " if you wanted me wearing it {i}that{/i} badly..."
                n 1fsqsslsbl "You do realize you could have just {i}asked{/i},{w=0.2} right?"

            n 1fchsml "Ahaha."
            n 1ullss "Well,{w=0.2} anyway.{w=0.5}{nw}"
            extend 1unmbo " In all seriousness?"
            n 1ulrsl "I can't say too much has changed,{w=0.2} honestly."
            n 1unmpu "Don't get me wrong!"
            n 1fchbg "I totally wanna get into cosplaying more!{w=0.75}{nw}"
            extend 1fcssmeme " Any excuse to show off my talent {i}and{/i} needlework."
            n 1ullaj "Plus I mean,{w=0.75}{nw}"
            extend 1unmgs " have you {i}seen{/i} what kinds of outfits people can pull off,{w=0.5}{nw}"
            extend 1fnmgs " all in the name of the stuff they love?"
            n 1fcsem "All that talent,{w=0.3} all that passion...{w=1}{nw}"
            n 1fcspu "It's{w=0.75}{nw}"
            extend 1fspgsedz " {i}awesome{/i}!{w=1}{nw}"
            extend 1fchgnedz " There's no way I {i}don't{/i} wanna be a part of that!"
            n 1kllpu "But..."
            n 1nslsl "Well."
            n 1ksrca "Ignoring how conventions are pretty much completely out of reach for me..."
            n 1ksqtr "I don't suppose {i}you've{/i} seen any crafts shops around here,{w=0.2} have you?{w=0.75}{nw}"
            extend 1ksqca " Or any of my sewing stuff?"
            n 1ksqsl "..."
            n 1ncsss "Heh.{w=1}{nw}"
            extend 1nsrsl " Yeah,{w=0.2} I thought not."
            n 1nsrajsbl "I really gotta figure something out for that,{w=0.75}{nw}"
            extend 1tsqsssbl " huh?"
            n 1tslslsbl "..."
            n 1fcsbgsbl "W-{w=0.2}well,{w=0.2} if there's one thing I'm not short of here,{w=0.75}{nw}"
            extend 1fchbgedz " it's ideas!{w=0.5}{nw}"
            extend 1fsqsm " So don't you worry about a thing,{w=0.2} [player]..."
            n 1fwrbg "'Cause there's no shortage of that {i}material{/i}!{w=0.75}{nw}"
            extend 1nchgnl " Ehehe."

            return
        else:

            n 1usqct "Oho?{w=0.5}{nw}"
            extend 1fcsbg " Cosplay,{w=0.2} you say?"
            n 1fllbo "..."
            n 1ullpu "Honestly?{w=0.75}{nw}"
            extend 1nslsssbl " I've never really done any {i}serious{/i} cosplaying or anything..."
            n 1unmaj "But I've actually thought about it a lot more since I got into manga and all that stuff a bunch!"
            n 1fcsbg "Plus I mean,{w=0.1} why shouldn't I?{w=0.75}{nw}"
            extend 1fspgsedz " I {w=0.2}{i}love{/i}{w=0.2} thinking up new ideas for outfits!"
            n 1fcsbg "Besides,{w=0.2} I know my way around a needle and thread!{w=0.75}{nw}"
            extend 1nsrsssbr " I've had to use them often enough before."
            n 1fcsajlsbr "B-{w=0.2}but I think it seems like a pretty awesome way to show my appreciation for characters I like..."
            n 1fsqbg "...And show my {i}limitless{/i} talent while I'm at it."
            n 1usqsm "Anyway,{w=0.2} who knows?"
            n 1fsqsm "Maybe you'll get to see some of my handiwork some day,{w=0.2} [player]."
            n 1fsqbg "I bet you'd like that,{w=0.2} huh?{w=0.5}{nw}"
            extend 1fchsml " Ehehe."



    elif Natsuki.isAffectionate(higher=True):
        if already_unlocked_cosplay_outfits:
            n 1tsqpu "Huh?{w=0.5}{nw}"
            extend 1tsqsf " Cosplay {i}again{/i}, [player]?"

            if Natsuki.isWearingClothes("jn_clothes_trainer_cosplay") or Natsuki.isWearingClothes("jn_clothes_sango_cosplay"):
                n 1fsqsflsbl "...Was {i}wearing{/i} it seriously not enough already?"
                n 1fsqsslsbl "Or did I somehow awaken some kind of hidden nerdiness in you?"
                n 1fslsslsbr "Ehehe..."
                n 1fcsemlsbr "A-{w=0.3}anyway!{w=0.5}{nw}"
            else:

                n 1tlraj "I gotta say,{w=0.2} I'm actually kinda impressed."
                n 1fslsslsbr "Sucking up to my interest in manga,{w=0.75}{nw}"
                extend 1fsqsslsbr " bugging me about cosplay..."
                n 1tsqsm "You're absorbing my sense of taste pretty fast,{w=0.2} huh?{w=0.75}{nw}"
                extend 1uchgn " Like a little dorky sponge!"
                n 1fchsm "Ehehe."
                n 1fchss "Anyway!{w=0.75}{nw}"

            extend 1nllss " Putting all that aside..."
            n 1unmaj "I actually wouldn't be {i}against{/i} doing a little more cosplay at all."
            n 1ulrpu "I mean,{w=0.75}{nw}"
            extend 1flrss " I've already got most of what I need."
            n 1fsqss "{i}Amazing{/i} ideas?{w=0.75}{nw}"
            extend 1fcsbg " Check!{w=0.75}{nw}"
            extend 1tsqsm " Tons of experience?{w=0.75}{nw}"
            extend 1fchbg " Check!"
            n 1usqgn "{i}Unmatched{/i} handiwork with a needle and thread?{w=1}{nw}"
            extend 1fcsbg " Oh,{w=0.2} you bet."
            n 1fllpu "It's just..."
            n 1kslsl "..."
            n 1tsrsf "I don't exactly have much {i}material{/i} to work with here,{w=0.75}{nw}"
            extend 1tnmsf " you know?"
            n 1kslbo "...Or even my sewing stuff,{w=0.2} for that matter."
            n 1kslsl "..."
            n 1fcswrlsbl "W-{w=0.2}well,{w=0.2} I'll figure something out!{w=0.75}{nw}"
            extend 1fcspolsbl " I always do,{w=0.2} a-{w=0.2}anyway."
            n 1fsqcal "So you better look forward to it,{w=0.2} [player]..."
            n 1fcsbglsbr "'Cause you ain't seen nothing yet!{w=0.75}{nw}"
            extend 1fcssmlsbr " Ehehe."

            return
        else:

            n 1tsrpu "Why...{w=1}{nw}"
            extend 1nsqbo " did I get the feeling you'd bring this up sooner or later,{w=0.2} [player]?"
            n 1fsqsl "..."
            n 1fnmpo "What?{w=0.75}{nw}"
            extend 1fsqgs " Did you think I'd {i}automatically{/i} be into it because I read manga from time to time?"
            n 1fsqpo "Huh?{w=0.75}{nw}"
            extend 1fnmgs " Is that it?"
            n 1fsqaj "Well?"
            n 1fsqdv "..."
            n 1fchdvesi "Pfffft!"
            n 1fchsm "Ehehe.{w=0.5}{nw}"
            extend 1ullss " Nah,{w=0.2} it's fine."
            n 1ulraj "I've thought about it a bunch,{w=0.2} honestly -{w=0.3}{nw}"
            extend 1unmbo " like since I got into manga and all that a while ago."
            n 1nslsssbr "I haven't {i}actually{/i} gone dressed up to a convention or anything yet..."
            n 1fcswrlsbl "B-{w=0.2}but that doesn't mean I haven't tried cosplaying at all!"
            n 1fcsbgsbl "I {i}am{/i} something of a pro with a needle and thread,{w=0.75}{nw}"
            extend 1fcssmeme " so it's right up my alley!"
            n 1tslsl "..."
            n 1tslss "Actually...{w=1}{nw}"
            extend 1fsqbg " you know what,{w=0.2} [player]?"
            n 1fsrsm "Perhaps I {i}might{/i} just give it another shot...{w=0.5}{nw}"
            extend 1fchbg " yeah!"
            n 1fcsss "Man,{w=0.5}{nw}"
            extend 1fchgnedz " I've got so many awesome ideas buzzing around in my head now!"
            n 1fsqss "You better be prepared,{w=0.2} [player]..."
            n 1fchbg "'Cause I'm gonna need some second opinions when I do!"
            n 1fwlbll "That's what friends are for,{w=0.2} right?"



    elif Natsuki.isNormal(higher=True):
        n 1unmbo "Cosplay,{w=0.2} huh?"
        n 1ulraj "Well...{w=0.5}{nw}"
        extend 1tnmbo " I mean,{w=0.2} I've played around with it,{w=0.2} if that's what you're asking."
        n 1tllpu "I never really thought about it that much until I got more into manga and things like that."
        n 1flrbg "It kinda feels like once you start getting into that stuff,{w=0.2} you discover tons more at once!"
        n 1nslsssbr "I've never really gone out and cosplayed myself though..."
        n 1fcsgslsbr "B-{w=0.2}but that doesn't mean I couldn't try it out more!"
        n 1fcspolesi "I'm basically a pro with a needle and thread,{w=0.5}{nw}"
        extend 1fchsml " so I've already got the hardest part done!"
        n 1fcsaj "The rest of it is just finding materials,{w=0.2} which are usually pretty easy to come by anyway."
        n 1fslcasbl "Props and wigs and all that are a little more annoying,{w=0.2} but not exactly {i}undoable{/i}.{w=1}{nw}"
        extend 1fcssmeme " Especially with a little ingenuity."
        n 1tcssl "..."
        n 1tupbo "Mmmm..."
        n 1tllpu "You know,{w=0.75}{nw}"
        extend 1fllss " the more I think about it...{w=1}{nw}"
        extend 1nchgnedz " the more I like the idea of giving it another run!"
        n 1fnmbg "What about you,{w=0.2} [player]?{w=0.75}{nw}"
        extend 1usqbg " I bet you'd love to see my skills at work,{w=0.2} right?"
        n 1fsrbgl "Well...{w=1}{nw}"
        extend 1fsqsm " we'll see."
        n 1fcsgssbl "B-{w=0.2}but no promises!"

        return

    elif Natsuki.isDistressed(higher=True):
        n 1nnmpu "Huh?{w=0.2} Cosplay?"
        n 1fsqsr "...Why,{w=0.2} [player]?"
        n 1fsqpu "So you can make fun of my clothes too?"
        n 1fslsr "..."
        n 1fsqpu "No,{w=0.2} [player].{w=0.75}{nw}"
        extend 1fcssr " That's for me to know,{w=0.75}{nw}"
        extend 1fsqan " and for you {i}not{/i} to find out."
        n 1fsqgs "Does {i}that{/i} answer your question?"

        return
    else:

        n 1fsqsr "Heh.{w=0.5} Why?"
        n 1fcsantsa "So you have something else to make me feel awful about?"
        n 1fcssrltsa "...Yeah.{w=0.75} No thanks."
        n 1fcsanltsd "I'm done talking to you about this."

        return


    if (
        Natsuki.isAffectionate(higher=True)
        and persistent.jn_custom_outfits_unlocked
        and not already_unlocked_cosplay_outfits
    ):
        n 1tllbo "..."
        n 1tslpu "...Actually,{w=0.5}{nw}"
        extend 1tslaj " now that I think about it..."
        n 1tlrsl "I wonder..."
        n 1fcssl "..."
        n 1nnmaj "You know what?{w=0.75}{nw}"
        extend 1nllaj " Just...{w=0.75}{nw}"
        extend 1nslunl " give me a sec here...{w=1}{nw}"

        show black zorder 4 with Dissolve(0.5)
        $ jnPause(1)
        play audio chair_out

        $ jnPause(3)
        play audio drawer
        $ jnPause(2)
        play audio gift_open
        $ jnPause(3)
        n "...!"
        play audio clothing_ruffle
        $ jnPause(1)
        play audio zipper
        $ jnPause(5)

        $ outfit_to_restore = Natsuki._outfit
        $ jn_outfits.get_outfit("jn_trainer_cosplay").unlock()
        $ jn_outfits.get_outfit("jn_sango_cosplay").unlock()
        $ Natsuki.setOutfit(jn_outfits.get_outfit(random.choice(["jn_trainer_cosplay", "jn_sango_cosplay"])))

        play audio chair_in
        $ jnPause(3)
        show natsuki 1fsldvlesssbr at jn_center
        hide black with Dissolve(1.25)

        n 1fchsslesssbr "T-{w=0.5}ta-da!{w=0.5}{nw}"
        extend 1fchsml " Ehehe..."
        n 1fsqsll "..."
        n 1fslunl "..."
        n 1fcsemlsbl "W-{w=0.2}well?"
        n 1fcsbglsbl "What do you think,{w=0.2} [player]?{w=0.75}{nw}"
        extend 1fchsmlsbr " I made it all myself,{w=0.2} too!"
        n 1fsqsrlsbr "..."
        n 1fnmemlsbr "What?"
        n 1fcsgslsbl "I {i}did{/i} say I was good with a needle and thread!"
        n 1fllsslsbl "S-{w=0.3}so of course I {i}had{/i} to prove it!"
        extend 1fcsajlsbl " And..."
        n 1nslsslsbl "...And..."
        n 1nslsllsbl "..."
        n 1kslsll "..."
        n 1kcspul "This...{w=1}{nw}"
        extend 1ksrsfl " wasn't actually {i}meant{/i} for me,{w=0.2} you know."
        n 1kcspulesi "..."
        n 1ksqbol "...I made it for Sayori."
        n 1fcseml "I-{w=0.2}it was meant to be for some kind of party after the festival she insisted on,{w=0.2} but...{w=1}{nw}"
        extend 1kcssll " yeah."
        n 1kslslltsb "..."
        n 1fcsunltsb "I'm...{w=1.25}{nw}"
        extend 1ksrsrl " just gonna go put this away now."

        show black zorder 4 with Dissolve(0.5)
        $ jnPause(2)
        play audio chair_out

        $ jnPause(3)
        play audio drawer
        $ jnPause(3)
        play audio clothing_ruffle
        $ jnPause(4)
        play audio gift_close
        $ jnPause(3)

        play audio chair_in
        $ jnPause(3)
        $ Natsuki.setOutfit(outfit_to_restore)
        show natsuki 1ncspul at jn_center
        hide black with Dissolve(1.25)

        n 1kslsll "..."
        n 1kslpul "...I know I can't just throw that outfit away.{w=1.25}{nw}"
        extend 1kcsajl " It just...{w=0.5} wouldn't be right."
        n 1kslbol "..."
        n 1kcspul "I'll...{w=0.5} keep it around."
        n 1knmsll "The best thing I could do is to make some {i}happy{/i} memories with it myself instead."
        n 1ksrajl "...It's what she would have done, a-{w=0.2}after all."
        n 1ksrsll "..."
        n 1ksqbol "...Right?"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_why_do_you_like_me",
            unlocked=True,
            prompt="Why do you like me?",
            category=["Natsuki", "Romance", "You"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_why_do_you_like_me:
    if Natsuki.isLove(higher=True):
        if jn_admissions.last_admission_type == jn_admissions.TYPE_INSECURE:
            n 1kwmsl "[player]..."
            n 1kwmsf "You aren't asking me this because of what you told me earlier...{w=0.3} right?"
            n 1kllbo "..."
            n 1ncspu "Look,{w=0.1} [player].{w=0.2} I'm going to be completely honest with you,{w=0.1} okay?"
            n 1ncssl "What you can -{w=0.1} or {i}can't{/i} do -{w=0.1} isn't important to me."
            n 1nnmpu "What people {i}say{/i} you are -{w=0.1} or {i}aren't{/i} capable of -{w=0.1} isn't important to me either."
            n 1fnmpu "Neither is what people say about you."
            n 1knmsr "[player]."
            $ chosen_endearment = jn_utils.getRandomEndearment()
            n 1klrpu "I...{w=0.3} feel about you the way I do because of how you've treated me,{w=0.1} [chosen_endearment].{w=0.2} Can you not see that?"
            n 1klrss "You've spent so much time with me,{w=0.1} day after day..."
            n 1kwmss "You've listened to my problems,{w=0.1} and you've told me yours..."
            n 1kllpo "You've been so patient with my mood swings,{w=0.1} and my grumpy moments..."

            if persistent.jn_player_love_you_count >= 10:
                n 1kcsunl "And...{w=0.3} you've made me feel..."
                n 1kcsunf "So loved..."
                n 1kllunl "..."

            elif persistent.jn_player_love_you_count >= 1:
                n 1kllssl "You're...{w=0.3} you're my first love,{w=0.1} [player]..."
                n 1kcussl "Do you even realise how {i}much{/i} that means to me?"

            elif persistent.jn_player_love_you_count == 0:
                n 1kwmssl "You honestly,{w=0.1} truly mean the world to me,{w=0.1} [player]..."

            n 1kllssl "So...{w=0.3} yeah."
            n 1klrnvl "Does that answer your question?"
            n 1knmsr "I know I can't solve your problems with a snap of my fingers,{w=0.1} [player].{w=0.2} I'm not a miracle worker."
            n 1kslsl "Believe me -{w=0.1} I {i}already{/i} would have if I could."
            n 1knmsl "But..."
            n 1kllss "I hope you can believe me when I say things will work out,{w=0.1} okay?"
            n 1fwmsm "Just...{w=0.3} keep fighting..."
            n 1fcssml "...Because I'm fighting for you too."
            n 1kplnvf "I love you,{w=0.1} [player].{w=0.2} You better not forget that."
            return
        else:

            n 1fcspo "[player]..."
            n 1flrpo "Do I really have to explain this all to you?"
            n 1flrsll "It's just...{w=0.3} embarrassing...{w=0.3} to me..."
            n 1kcssll "..."
            n 1ncspu "...Okay,{w=0.1} look."
            n 1fllssl "You've...{w=0.3} honestly done more than you could ever know,{w=0.1} [player]."
            n 1fllsll "For me,{w=0.1} I mean."
            n 1knmsll "I've almost lost count of how many hours you've spent talking to me..."
            n 1klrssl "You've listened to so many of my dumb problems,{w=0.1} over and over..."
            n 1fllunl "...And you've been so patient through all of my stupid moods."

            if persistent.jn_player_love_you_count >= 10:
                n 1fcsunl "Y-you've made me feel..."
                n 1kcsunl "Really appreciated.{w=0.2} So many times,{w=0.1} I've lost count..."

            elif persistent.jn_player_love_you_count >= 1:
                n 1kskajf "You're...{w=0.3} you're my first love,{w=0.1} even!"
                n 1kwmpuf "Do you even know what that {i}means{/i} to me?"

            elif persistent.jn_player_love_you_count == 0:
                n 1kwmpuf "You seriously mean the world to me,{w=0.1} [player]..."

            n 1kllssl "So...{w=0.3} yeah."
            n 1klrnvl "Does that answer all of your questions?{w=0.2} Am I free to go now?"
            n 1klrss "Ahaha..."
            n 1kwmpu "But seriously,{w=0.1} [player]."
            n 1kplbo "Don't ever doubt how important you are to me,{w=0.1} alright?"
            n 1fnmpol "I'll get mad if you do."
            n 1flrpol "And trust me..."
            n 1klrssl "I doubt you want that."
            return

    elif Natsuki.isEnamored(higher=True):
        if jn_admissions.last_admission_type == jn_admissions.TYPE_INSECURE:
            n 1knmaj "...Hey,{w=0.1} [player]..."
            n 1klrpu "This isn't by chance because of what you said earlier...{w=0.3} right?"
        else:

            n 1uskpul "Wh-{w=0.1}why do I-{w=0.1}...?"
            n 1fcsanl "Uuuuuuu..."

        n 1fcsajl "...Okay,{w=0.1} look.{w=0.2} I'll try to help you understand as best I can."
        n 1fllaj "I'm not sure if someone's giving you a tough time or what, but I'm saying it anyway."
        n 1fllsr "I don't really care about what others expect from you."
        n 1fnmsr "I don't really care about what others say or think about you."
        n 1knmpu "I don't really care if you can -{w=0.1} or can't -{w=0.1} do something."
        n 1fcseml "I...{w=0.3} {i}like{/i} you,{w=0.1} because of how you've treated me,{w=0.1} you dummy!"
        n 1flleml "Like,{w=0.1} come on!"
        n 1flrssl "You've listened to me yammer on,{w=0.1} again and again..."
        n 1knmssl "You've heard me out on so many dumb problems I've had..."
        n 1fcsbgl "You've even dealt with my crappy temper like a champ!"
        n 1klrsl "..."
        n 1kcssl "...I've never been treated by anyone as well as I've been treated by you,{w=0.1} [player]."
        n 1fllslf "So is it any wonder why I...{w=0.3} enjoy hanging out with you this much?"
        n 1fcsslf "..."
        n 1flrajl "Alright,{w=0.1} okay.{w=0.2} I really don't wanna have to explain all that again,{w=0.1} so I hope you took all that in."
        n 1fnmssl "Just...{w=0.3} continue being you,{w=0.1} got it?"
        n 1kllpul "I...{w=0.3} kinda like how you do that already."
        return
    else:

        if jn_admissions.last_admission_type == jn_admissions.TYPE_INSECURE:
            n 1unmpul "...Huh?"
            n 1uskemf "W-{w=0.1}why do I...?"
            n 1fcsanf "..."
            n 1tlremf "..."
            n 1flrsll "..."
            n 1fnmpul "Uhmm...{w=0.3} [player]?"
            n 1fllpo "This isn't all related to what you told me earlier,{w=0.1} right?"
            n 1knmpo "About feeling insecure and all that?"
            n 1klrsl "..."
            n 1nnmsl "[player]."
            n 1fnmpuf "Listen up,{w=0.1} 'kay?{w=0.2} I...{w=0.3} really don't wanna have to repeat this."
        else:

            n 1uscemf "Urk-!"
            n 1uskemf "W-{w=0.1}wait,{w=0.1} w-{w=0.1}what?"
            n 1fwdemf "W-{w=0.1}why do I...{w=0.3} l-{w=0.1}like you?!"
            n 1fcsanf "Nnnnnnnnn-!"
            n 1fllwrf "I mean...!{w=0.2} It's not that I {i}like{/i} like you,{w=0.1} or anything ridiculous like that!"
            n 1fcsemf "Ugh...{w=0.3} I swear,{w=0.1} [player] -{w=0.1} you honestly try to put me in the most awkward freaking spots sometimes..."
            n 1fllslf "..."
            n 1fllsll "I...{w=0.3} guess I {i}do{/i} owe you an answer though,{w=0.1} at least."

        n 1fcssll "Look."
        n 1nlrpu "You've been pretty awesome to me so far,{w=0.1} [player]."
        n 1klrpu "...Do you even know how few other people make me feel that way?"
        n 1klrsl "It's...{w=0.3} really not a lot,{w=0.1} if you hadn't gathered."
        n 1fllpol "You always listen to me,{w=0.1} you don't tell me I'm annoying,{w=0.1} or to pipe down..."
        n 1kwmsrl "And you've been super understanding too."
        n 1kllpul "I...{w=0.3} honestly couldn't ask for a better friend,{w=0.1} [player]."
        n 1fnmbol "Always remember that,{w=0.1} alright?{w=0.2} I'll get mad if you don't."
        n 1kllbol "..."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_fried_squid",
            unlocked=True,
            prompt="Fried squid",
            category=["DDLC", "Food"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_fried_squid:
    n 1fllss "Hey,{w=0.1} [player]..."
    n 1usqsm "You know what I could go for right now?"
    n 1uchbs "A big,{w=0.1} steaming fresh bowl of Mon-{w=0.1}ika!"
    n 1uchbg "..."
    n 1flrpu "...Huh."
    n 1tnmpu "You know,{w=0.1} in hindsight?{w=0.2} That joke really wasn't funny the first time round."
    n 1tllpo "I've...{w=0.3} no idea why it'd be funny this time,{w=0.1} to be honest."
    n 1uspgsesu "Oh!"
    n 1fchbg "But fried squid is no joke at all,{w=0.1} [player]!{w=0.2} Have you ever tried it?"
    n 1uchbs "It's {i}delicious{/i}!{w=0.2} I love it!"
    n 1fsqsm "Not just boring old fried seafood though -{w=0.1} it's gotta have the crap battered out of it first!"
    n 1uspbg "That crispy golden coating is seriously the best.{w=0.2} Deep fried food is awesome!"
    n 1fllbg "It's not {i}good{/i} for you exactly,{w=0.1} but as a treat?{w=0.2} You could do way worse..."
    n 1fcssm "Especially with sauce to spice things up a bit!"
    n 1fnmss "By the way -{w=0.1} wanna know how you can tell you're dining on some top-notch squiddy goodness?"
    n 1uchbs "The texture,{w=0.1} of course!"
    n 1fllaj "Overcooked squid becomes all rubbery and nasty,{w=0.1} and even worse -{w=0.1} it loses all of its flavor too!"
    n 1fsqsr "Imagine biting through the batter,{w=0.1} only to find you're basically chewing on a bunch of rubber bands."
    n 1fsqem "Ugh!{w=0.2} Gross!{w=0.2} Talk about a disappointment."
    n 1unmaj "Don't let that put you off though,{w=0.1} [player] -{w=0.1} next time you see some,{w=0.1} why not give it a shot?"

    if jn_admissions.last_admission_type == jn_admissions.TYPE_HUNGRY:
        n 1kllss "...Probably the sooner the better,{w=0.1} if you're hungry like you said."
        n 1ullaj "But anyway..."

    n 1unmbg "You could even be all fancy if you wanted to and order it by the culinary name!"
    n 1fnmbg "Ten points if you can guess what that is.{w=0.2} Ehehe."

    if Natsuki.isLove(higher=True):
        n 1flrsg "Hmm..."
        n 1fnmbg "Actually...{w=0.3} you know what?"
        n 1fchbg "We should just get a bowl of calamari to share.{w=0.2} That's fair,{w=0.1} right?"
        n 1fsqsm "I should warn you though,{w=0.1} [player]..."
        n 1fchgn "I'm not handing over the last piece without a fight!"
        n 1nchsml "Ehehe."

    elif Natsuki.isEnamored(higher=True):
        n 1uchbg "But yeah -{w=0.1} you should really give it a try if you haven't already,{w=0.1} [player]!"
        n 1fchbg "I wouldn't want someone to miss out on that!"
        n 1klrssl "E-{w=0.1}especially not you.{w=0.2} Ehehe..."
    else:

        n 1uchbg "But yeah {w=0.1}-{w=0.1} you should really try it out if you haven't already,{w=0.1} [player]!"
        n 1fchbg "I wouldn't want someone to miss out on that!{w=0.2} Ahaha."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_collectibles",
            unlocked=True,
            prompt="Do you have any collectibles?",
            category=["Media"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_collectibles:
    if Natsuki.isAffectionate(higher=True):
        n 1unmpueqm "Collectibles?{w=0.2} You mean like figurines and plushies and such?"
        n 1flrpu "Mmm...{w=0.3} not really.{w=0.2} Collecting is an expensive hobby,{w=0.1} [player]!"
        n 1klrpo "I mean,{w=0.1} it all depends on exactly what you collect,{w=0.1} but it feels like places that sell them prey on that."
        n 1flraj "Like...{w=0.3} the urge to complete a collection -{w=0.1} so they jack up the prices!"
        n 1fcsboesi "Ugh..."
        n 1kllbosbl "And for people in my...{w=0.3} uhmm...{w=0.3} {i}position{/i},{w=0.1} it's a big barrier to entry."
        n 1unmaj "But anyway..."

    elif Natsuki.isNormal(higher=True):
        n 1tnmpueqm "Huh?{w=0.2} You mean like figurines and all that stuff?"
        n 1tlrpu "Well...{w=0.3} no,{w=0.1} [player].{w=0.2} Not really."
        n 1knmsf "I couldn't justify spending so much just on hobbies like that!"
        n 1flrbo "...Especially not when I had {i}other{/i} things to worry about spending my money on first."
        n 1unmaj "B-{w=0.2}but anyway,{w=0.1} putting all that aside..."

    elif Natsuki.isDistressed(higher=True):
        n 1fsqsfsbl "No,{w=0.1} [player]."
        n 1fsqaj "Collectibles were way too expensive for me.{w=0.2} I couldn't justify wasting the money I {i}do{/i} have."
        n 1fnmsl "{i}Especially{/i} on stuff that'll just sit on a shelf that I'll forget about."
        n 1fsqsr "Yeah,{w=0.1} [player] -{w=0.1} believe it or not,{w=0.1} some of us {i}do{/i} have to think about how we spend our money."
        n 1fsqun "Shocker,{w=0.1} right?"
        n 1fcsun "..."
        n 1fnmaj "Well?{w=0.2} Satisfied with your answer?"
        n 1fsqsl "We're done here."
        return
    else:

        n 1fsqsr "...Why?{w=0.2} ...And I don't just mean why you care."
        n 1fsqan "But why should I tell {i}you{/i} if I do or not?"
        n 1fcsan "You'd probably just trash them."
        n 1fcsun "Heh.{w=0.2} After all."
        n 1fsqupltsa "You've proven great at trashing things so far,{w=0.1} {i}haven't you{/i}?{w=0.2} Jerk."
        return

    n 1ullbo "..."
    n 1tllbo "...Huh.{w=0.2} There's a point,{w=0.1} actually.{w=0.2} Does manga count as a collectible?"
    n 1tllaj "I'm...{w=0.3} not really sure..."
    n 1tnmpu "What do you think,{w=0.1} [player]?"
    menu:
        n "Would you call it a collectible?"
        "I'd say so!":

            n 1fsqbg "Oho!"
            n 1fchbg "So I suppose I am something of a collector,{w=0.1} after all!"

            if Natsuki.isLove(higher=True):
                n 1uchsm "I guess that all makes sense.{w=0.2} After all..."
                n 1fllsmf "I'd like to think you're in my collection too,{w=0.1} [player]~."
                n 1uchsmf "Ehehe."
            else:

                n 1flrsm "Well,{w=0.1} in that case..."
                n 1nchbg "Just let me know if you ever feel like a tour!"
                n 1nchgn "You won't find a better collection!{w=0.2} Ehehe."

                if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.manga):
                    n 1fllss "Or,{w=0.1} at least...{w=0.5}{nw}"
                    extend 1fsqss " a better...{w=0.3} {i}physical{/i} one."
                    n 1fsqsm "Right,{w=0.5}{nw}"
                    extend 1fsqbg " [player]?"
        "No,{w=0.1} I wouldn't.":

            n 1flrpo "Huh...{w=0.3} you do have a point."
            n 1tnmpo "I suppose you'd call it a library,{w=0.1} or something like that?"
            n 1nnmsm "Well,{w=0.1} whatever."
            n 1nsqsm "I suppose I'd better {i}read{/i} up on my definitions,{w=0.1} right?"
            n 1nchsm "Ehehe."
        "Well,{w=0.1} it definitely isn't literature.":

            n 1nsqsr "Ha.{w=0.2} Ha.{w=0.2} Ha.{w=0.2} Ha.{w=0.2} ...Ha."
            n 1flrpo "{i}Hilarious{/i},{w=0.1} [player]."
            n 1flraj "Keep it up,{w=0.1} and I'm gonna book you one."
            n 1fsqsg "...And no,{w=0.1} I don't mean read you a story."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_play_snap",
            unlocked=True,
            prompt="Do you want to play Snap?",
            conditional="persistent.jn_snap_unlocked",
            category=["Games"],
            player_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_play_snap:
    if persistent.jn_snap_player_is_cheater:

        if not int(jn_apologies.ApologyTypes.cheated_game) in persistent._jn_player_pending_apologies:
            $ persistent.jn_snap_player_is_cheater = False
        else:

            n 1fnmem "[player]...{w=0.3} if you aren't even sorry you cheated,{w=0.1} why should I play with you again?"
            n 1kllpo "Come on...{w=0.3} it's not hard to apologize,{w=0.1} is it?"
            return

    if Natsuki.isLove(higher=True):
        n 1uchbg "Of course I do,{w=0.1} dummy!{w=0.2} Ehehe."

    elif Natsuki.isEnamored(higher=True):
        n 1fchbg "Of course I'll play some with you,{w=0.1} dummy!"

    elif Natsuki.isAffectionate(higher=True):
        n 1fchsm "Well,{w=0.1} duh!{w=0.2} Of course I'm up for a game!"
    else:

        n 1nnmss "You wanna play Snap?{w=0.2} Sure!"

    n 1unmsm "Let me just get the cards out real quick,{w=0.1} alright?"
    play audio drawer
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")
    jump snap_intro


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_remind_snap_rules",
            unlocked=True,
            prompt="Can you go over the rules of Snap again?",
            conditional="persistent.jn_snap_unlocked and persistent.jn_snap_explanation_given",
            category=["Games"],
            player_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_remind_snap_rules:
    if persistent.jn_snap_player_is_cheater:
        n 1fcsan "Come on,{w=0.1} [player]."
        n 1flrpo "If you cared about the rules,{w=0.1} then why did you cheat when we played earlier?"
        n 1fnmpo "You haven't even apologized for it yet..."
        return
    else:

        if Natsuki.isLove(higher=True):
            n 1nchbg "Ahaha.{w=0.2} You're so forgetful sometimes,{w=0.1} [player]."
            n 1nsqbg "Sure,{w=0.1} I'll go over it again!{w=0.2} Juuust for you~."

        elif Natsuki.isEnamored(higher=True):
            n 1nchbg "Of course I can!"

        elif Natsuki.isAffectionate(higher=True):
            n 1fchsm "You bet I can!"
        else:

            n 1nnmss "Sure thing!"

        jump snap_explanation


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_chewing_gum",
            unlocked=True,
            prompt="Chewing gum",
            category=["Wind-ups"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_chewing_gum:
    n 1fcsan "Ugh...{w=0.3} you know what really gets on my nerves?"
    n 1fsqsl "When people are gross and don't get rid of chewing gum properly."
    n 1fbkwr "Seriously -{w=0.1} it annoys the crap out of me!"
    n 1fllem "Like,{w=0.1} have you ever walked into a city center and looked at the ground?{w=0.2} At all the paving?"
    n 1fcsan "All those dried up spots of gum -{w=0.1} it's freaking disgusting,{w=0.1} and it looks nasty too!"
    n 1fsqan "And that's in a place where there's usually bins everywhere too,{w=0.1} so it isn't just gross..."
    n 1fnmwr "It's super lazy too!{w=0.2} I can't decide what winds me up more."
    n 1fcswr "Even worse than that -{w=0.1} there's even people who go and stick it under tables,{w=0.1} or on walls -{w=0.1} who {i}does{/i} that?!"
    n 1flrpu "Jeez...{w=0.3} makes me want to track them down and stick that crap back in their stupid mouths."
    n 1nnmsl "I don't really care if you chew gum yourself,{w=0.1} [player]."

    if Natsuki.isLove(higher=True):
        n 1kllca "Just make sure you dispose of it properly,{w=0.1} 'kay?"
        n 1kllss "I'm sure you do anyway,{w=0.1} but...{w=0.3} just in case."
        n 1kchsml "Love you,{w=0.1} [player]~!"

    elif Natsuki.isAffectionate(higher=True):
        n 1nllca "But please,{w=0.1} just get rid of it properly when you're done."
        n 1nchsm "Thanks,{w=0.1} [player]~!"
    else:

        n 1fnmaj "But seriously -{w=0.1} stick it in the bin when you're done,{w=0.1} alright?{w=0.2} Or just wrap it in a tissue and get rid of it later."
        n 1fsqaj "...Or it won't just be the gum that'll be getting chewed out!"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_smoking_vaping_indoors",
            unlocked=True,
            prompt="Indoor smoking",
            category=["Wind-ups"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_smoking_vaping_indoors:
    n 1fllaj "You know what stinks,{w=0.1} [player]?"
    n 1fsqaj "I mean {i}really{/i} stinks -{w=0.1} not just figuratively,{w=0.1} but literally too?"
    n 1fcssf "When people smoke or vape indoors,{w=0.1} or near entrances -{w=0.1} {i}especially{/i} when other people are around.{w=0.2} I can't stand it!"
    n 1fcsan "Like...{w=0.3} how inconsiderate can you be?{w=0.2} Seriously?"
    n 1fsqwr "For starters,{w=0.1} and like I was just saying -{w=0.1} it absolutely {i}reeks{/i}!"
    n 1fllem "Tobacco is awful smelling stuff,{w=0.1} and all those sickly vaping fluid types aren't much better either."
    n 1ksqup "It clings to the walls too -{w=0.1} so the smell hangs around for ages!"
    n 1kllan "Speaking of clinging to the walls,{w=0.1} the smoke literally does that too -{w=0.1} have you {i}seen{/i} a smoker's house,{w=0.1} or car?"
    n 1ksqup "All those yellow stains...{w=0.3} you'd think it was painted on or something.{w=0.2} Ew!"
    n 1fsqan "And you know what,{w=0.1} [player]?{w=0.2} I haven't even gotten to the worst of it yet..."
    n 1fcsan "I've said nothing about how expensive it all is,{w=0.1} or the health problems not just to the smoker..."
    n 1fsqaj "...But to everyone else!"
    n 1fcsbo "Ugh..."
    n 1flrbo "Don't get me wrong -{w=0.1} if someone wants to smoke or vape,{w=0.1} that's their choice and their money.{w=0.2} I don't care."
    n 1fnmbo "But the least they can do is respect the decision of everyone who {i}doesn't{/i},{w=0.1} you know?"
    n 1fcssl "..."

    if Natsuki.isLove(higher=True):
        n 1nnmsl "I know you,{w=0.1} [player].{w=0.2} I highly doubt you'd be the kind of person to be a jerk like that."
        n 1klrss "Just...{w=0.3} don't prove me wrong,{w=0.1} alright?"
        n 1uchgn "'preciate it!{w=0.2} Ahaha."

    elif Natsuki.isAffectionate(higher=True):
        n 1kllpo "I doubt you'd be a jerk like that even if you do smoke,{w=0.1} [player]."
        n 1fsqpo "But...{w=0.3} try not to prove me wrong,{w=0.1} 'kay?{w=0.2} I like you more as not a jerk."
        n 1uchsm "Thanks!"
    else:

        n 1ullaj "I don't think you'd be a jerk like that,{w=0.1} [player]."
        n 1nnmaj "But...{w=0.3} just in case -{w=0.1} keep it in mind,{w=0.1} will you?"
        n 1nchsm "Thanks!"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_unwashed_hands",
            unlocked=True,
            prompt="Handwashing",
            category=["Wind-ups"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_unwashed_hands:
    n 1unmaj "Hey,{w=0.1} [player]."
    n 1nnmaj "Have you ever worked in a restaurant,{w=0.1} or a hospital or anything like that?"
    n 1fnmaj "Because I bet if there's one thing drilled into you...{w=0.3} it's how important washing your hands is!"
    n 1flraj "It really gets on my nerves when people don't wash their hands after doing something nasty."
    n 1fsqsl "Like...{w=0.3} we {i}know{/i} how important it is to stop germs getting around -{w=0.1} and {i}what{/i} exactly is hard about sticking your hands under the tap for a minute?!"
    n 1fsqem "It annoys me even more when people are really dumb about it too!{w=0.2} Like,{w=0.1} they think they don't need to do that if they didn't go."
    n 1fcsem "Newsflash -{w=0.1} if you went in,{w=0.1} you must have touched stuff -{w=0.1} so now there's all that crap on your hands that you've taken out with you!"
    n 1fsqsf "Not only is it {i}super{/i} icky and bad for {i}your{/i} health..."
    n 1ksqan "It's awful for others too!{w=0.2} What if you're about to handle someone's food,{w=0.1} or visit someone in hospital?"
    n 1fllan "You could make someone seriously ill..."
    n 1fnmfu "...And then they get all upset when you call them out on their grossness!{w=0.2} I mean,{w=0.1} come {i}on{/i}!"
    n 1fcssl "Just...{w=0.3} ugh."
    n 1ncssl "...[player]."
    n 1nnmpu "I really hope you keep your hands spick and span.{w=0.2} And not just when you visit the restroom."
    n 1fnmpu "Before you prepare food,{w=0.1} after you've handled trash...{w=0.3} just think about where you've been,{w=0.1} alright?"

    if Natsuki.isLove(higher=True):
        n 1kchbg "Don't get me wrong though!{w=0.2} I'm pretty sure you at least try to do the right thing!"
        n 1nnmbg "Just...{w=0.3} keep up the good work,{w=0.1} alright?{w=0.2} For everyone."
        n 1nchsm "Thanks,{w=0.1} [player]!"
    else:

        n 1tsqpo "It really isn't that much to ask...{w=0.3} is it?"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_litter",
            unlocked=True,
            prompt="Littering",
            category=["Wind-ups"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_litter:
    n 1ullpu "You know,{w=0.1} [player]..."
    n 1unmaj "At school?{w=0.2} At my school,{w=0.1} anyway?"
    n 1unmss "We -{w=0.1} the students -{w=0.1} were actually responsible for keeping it all clean."
    n 1fcsbg "Ehehe.{w=0.2} Are you surprised?"
    n 1fchgn "Yep!{w=0.2} From the bins,{w=0.1} to the desks,{w=0.1} to the floors.{w=0.2} It was all our effort that kept it squeaky clean!"
    n 1flrpol "N-{w=0.1}not that I {i}enjoyed{/i} it,{w=0.1} of course!{w=0.2} Cleaning {i}is{/i} pretty lame,{w=0.1} but it's just something you gotta do."
    n 1fnmpo "But I'll tell you one thing,{w=0.1} [player]."
    n 1fsqtr "{i}Nothing{/i} pissed me off more than the jerks who just went and dropped or left their trash everywhere."
    n 1fnman "...And not even just in school!"
    n 1fcsan "I mean...{w=0.3} where do I start?!"
    n 1fnmaj "First off -{w=0.1} how much of a freaking slob do you have to be?{w=0.2} Do these people just drop crap all over their homes too?!"
    n 1flran "It annoys me even more when there's bins and stuff literally right there!"
    n 1fcsfu "Like,{w=0.1} wow...{w=0.3} lazy as well as inconsiderate?{w=0.2} What a {i}charming{/i} combo!"
    n 1fllpu "Even if there isn't a trash can or whatever around..."
    n 1fllan "It's not like they don't have pockets,{w=0.1} or can't just carry it around for a few minutes!"
    n 1fcsan "Ugh..."
    n 1flrup "And I haven't even mentioned people tossing their rubbish out of cars,{w=0.1} or into lakes and ponds!"
    n 1fcssl "It pisses me off just thinking about it..."
    n 1fllbo "..."
    n 1fnmbo "[player]."

    if Natsuki.isEnamored(higher=True):
        n 1ksqbo "I know you.{w=0.2} In fact,{w=0.1} I daresay I know you {i}very{/i} well by now."
        n 1knmbo "I don't think you're the sort to do that at all..."
        n 1klraj "I'm not wrong...{w=0.3} am I?"
        n 1klrss "I don't wanna have to be.{w=0.2} Ahaha..."

    elif Natsuki.isAffectionate(higher=True):
        n 1unmaj "I don't think you're like that,{w=0.1} [player]."
        n 1ullsl "Or...{w=0.3} at least you don't {i}try{/i} to be anyway."
    else:

        n 1fnmsl "I really,{w=0.1} really hope you aren't one of those people."

    n 1nllpu "So..."
    n 1nnmsl "...If you're a litterbug already,{w=0.1} I'll forgive you this one time."
    n 1klrpo "Just...{w=0.3} make sure you clean up your act,{w=0.1} okay?"

    if Natsuki.isLove(higher=True):
        n 1uchsml "Ehehe.{w=0.2} Love you,{w=0.1} [player]~."

    elif Natsuki.isAffectionate(higher=True):
        n 1nlrpol "It'd...{w=0.3} mean a lot."
    else:

        n 1fchbg "Thanks,{w=0.1} [player]."

    return



init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_custom_music_introduction",
            unlocked=True,
            prompt="Music player",
            conditional="not persistent.jn_custom_music_unlocked",
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_custom_music_introduction:
    n 1fllpu "Hmm..."
    n 1flrbo "I wonder if it's still here..."

    play audio drawer
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    n 1fllpo "Come on!{w=0.2} It's gotta still be here!{w=0.2} I know it!"

    play audio drawer
    with Fade(out_time=0.5, hold_time=0.5, in_time=0.5, color="#000000")

    n 1uspbg "..."
    n 1fchbs "Aha!{w=0.2} Yes!"
    n 1nchsm "..."
    n 1uwdbg "Oh!{w=0.2} [player]!{w=0.2} [player]!"
    n 1uchgn "Guess what I fooound!{w=0.5} Ehehe."
    n 1nchbs "It's...{w=0.3} a music player!{w=0.2} Neat,{w=0.1} right?"
    n 1tlrbg "Well...{w=0.3} kinda.{w=0.2} It's not exactly...{w=0.3} {i}modern{/i},{w=0.1} but it'll do the job!"
    n 1tllpo "Come to think of it...{w=0.3} I don't really even know who it belongs to."
    n 1unmpu "We just found it left in the clubroom one day.{w=0.2} Nobody knew if it belonged to anyone -{w=0.1} and trust me,{w=0.1} we tried to find out!"
    n 1tnmsl "We asked around in lessons,{w=0.1} we sent out notes...{w=0.3} nothing!"
    n 1tlrbg "So...{w=0.3} we kinda just kept it here,{w=0.1} in my desk,{w=0.1} in case whoever it was came back to pick it up."
    n 1tsqpo "I guess they never will now,{w=0.1} huh?"
    n 1uchbg "Well,{w=0.1} whatever.{w=0.2} The point is we can play whatever music we want now!"
    n 1fchbg "I think I figured out a way to let you send me whatever you want me to put on,{w=0.1} so listen up,{w=0.1} 'kay?"
    $ get_topic("talk_custom_music_introduction").lock()
    jump talk_custom_music_explanation



init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_custom_music_explanation",
            unlocked=True,
            prompt="Can you explain custom music for me again?",
            category=["Music"],
            conditional="persistent.jn_custom_music_unlocked and persistent.jn_custom_music_explanation_given",
            player_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_custom_music_explanation:

    $ persistent.jn_custom_music_unlocked = True

    if persistent.jn_custom_music_explanation_given:
        $ persistent.jn_custom_music_explanation_given = True
        n 1unmaj "Huh?{w=0.2} You want me to explain how custom music works again?"
        n 1uchbg "Sure,{w=0.1} I can do that!"
        n 1nnmsm "First things first,{w=0.1} let me just check for the {i}custom_music{/i} folder..."
    else:

        $ persistent.jn_custom_music_explanation_given = True
        n 1unmbg "Alright!{w=0.2} So...{w=0.3} it's actually pretty simple,{w=0.1} [player]."
        n 1nnmsm "There should be a folder called {i}custom_music{/i} somewhere around here..."
        n 1nchbg "Let me just take a look,{w=0.1} one sec..."
        n 1ncssr "..."

    if not jn_utils.createDirectoryIfNotExists(jn_custom_music.CUSTOM_MUSIC_DIRECTORY):
        n 1tnmbg "Well,{w=0.1} hey!{w=0.2} It's already there!{w=0.2} I must have set it up earlier and forgot."
        n 1uchgn "No complaints from me!"
    else:

        n 1uchbg "Okaaay!{w=0.2} It wasn't there,{w=0.1} so I've just created it for you."

    $ folder = jn_custom_music.CUSTOM_MUSIC_DIRECTORY
    n 1nnmss "So,{w=0.1} [player] -{w=0.1} if you click {a=[folder]}here{/a},{w=0.1} that'll take you to the folder I set up."
    n 1ullbg "Then all you gotta do is just {i}copy{/i} your music into that folder,{w=0.1} and you're good to go!"
    n 1uchgn "Easy as pie,{w=0.1} huh?{w=0.2} Ehehe."
    n 1uwdaj "Oh -{w=0.1} a couple of things first though,{w=0.1} [player]."
    n 1unmpu "Any music you give me needs to be in {i}.mp3,{w=0.1} .ogg or .wav{/i} format."
    n 1ullss "If you don't know how to check,{w=0.1} then just look at the letters after the period in the file name."
    n 1unmss "You should also be able to see those in the file {i}properties{/i} if they don't appear on the screen at first."
    n 1flrbg "Like I said -{w=0.1} this thing isn't {i}exactly{/i} super modern,{w=0.1} so it won't work with any fancy newer formats,{w=0.1} or weird old ones."
    n 1uwdaj "Oh,{w=0.75}{nw}"
    extend 1nlrpu " and if you gotta convert it first,{w=1}{nw}"
    extend 1nsqpo " don't just rename it."
    n 1fcsbg "Use a proper converter!{w=1}{nw}"
    extend 1fsrbg " Unless you {i}enjoy{/i} hearing your music being all warped and nasty,{w=0.3} anyway."
    n 1nnmaj "Once you've done that,{w=0.1} just click the {i}Music{/i} button,{w=0.1} and I'll check that it's all done right."
    n 1nchbg "...And that's about it!"
    n 1nsqbg "A word of warning though,{w=0.1} [player]..."
    n 1usqsg "You better have good taste."
    n 1uchgnelg "Ahaha!"
    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_vtubers",
            unlocked=True,
            prompt="Do you follow any VTubers?",
            category=["Games", "Media", "Society"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_vtubers:
    if Natsuki.isEnamored(higher=True):
        n 1tllss "VTubers,{w=0.1} huh?{w=0.2} You're asking {i}me{/i}?"
        n 1fnmsm "...Wow,{w=0.1} [player].{w=0.2} I'm impressed."
        n 1fsqsm "Yet again,{w=0.1} you've proved you're even more of a nerd than I am!"
        n 1uchsm "Ehehe."
        n 1klrbg "Relax!{w=0.2} Relax,{w=0.1} jeez!{w=0.2} You know I'd never seriously judge your hobbies,{w=0.1} you dummy."
        n 1unmaj "But yeah,{w=0.1} anyway..."

    elif Natsuki.isHappy(higher=True):
        n 1unmbg "Yeah!{w=0.2} I think I know those!"
        n 1tnmpu "They're those people with the anime avatars that stream stuff online for people,{w=0.1} right?"
        n 1tllpu "Well..."

    elif Natsuki.isNormal(higher=True):
        n 1unmpu "Huh?{w=0.2} VTubers?{w=0.2} Like those people with the anime-style avatars that play games and stuff online for people to watch?"
        n 1tnmpu "That {i}is{/i} what you mean,{w=0.1} right?"
        n 1tllpu "Well..."

    elif Natsuki.isDistressed(higher=True):
        n 1fsqpu "No,{w=0.1} I do not.{w=0.2} I'd rather be playing the game myself than watching someone play it for me."
        n 1fsqbo "If you follow any,{w=0.1} good for you."
        n 1flrbo "{i}Some{/i} of us don't have the time to sit around on our butt for hours..."
        n 1fsqaj "...Or the money to just give it away to strangers."
        n 1fsqpu "[player]."
        n 1fsqsrtsb "How much are we betting you aren't {i}nearly{/i} as toxic to {i}them{/i} as you are to me, huh?"
        return
    else:

        n 1fsqantsb "No.{w=0.2} And I couldn't give less of a crap if you did,{w=0.1} either."
        n 1fnmpultsf "...And hey,{w=0.1} newsflash,{w=0.1} idiot."
        n 1fsqupltse "Throwing money at a stranger hiding behind a cutesy picture doesn't make you any less of a {b}jerk{/b}."
        return

    n 1nchsm "It's definitely a cool idea!{w=0.2} It lets people share their passions and experiences with others behind a new persona..."
    n 1fllpo "Without having to worry about baggage following them into their personal lives,{w=0.1} or people being creeps,{w=0.1} or stuff like that."
    n 1uwdem "A lot of them even make full-blown careers out of it: merchandise,{w=0.1} song releases and everything -{w=0.1} just like idols!{w=0.2} It's crazy!"
    n 1tllem "That being said..."
    n 1tnmbo "I never really got into that sort of thing myself."
    n 1klrss "Like...{w=0.3} don't get me wrong!{w=0.2} I'm sure they're pretty fun to watch.{w=0.2} If you're into that kind of thing,{w=0.1} I mean."
    n 1nllsl "But I'd rather be playing or doing something {i}myself{/i} than watching someone else do it,{w=0.1} usually."
    n 1nllss "That might just be me,{w=0.1} though."
    n 1nllbg "Ehehe."
    n 1unmaj "What about you,{w=0.1} [player]?{w=0.2} Are you into that sort of stuff?"
    n 1fcssm "Wait,{w=0.1} wait!{w=0.2} Don't bother answering that."
    n 1tsqsm "You {i}did{/i} ask me about them,{w=0.1} after all -{w=0.1} I think that speaks for itself,{w=0.1} wouldn't you agree?"
    n 1uchbselg "Ahaha!"
    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_skateboarding",
            unlocked=True,
            prompt="Are you into skateboarding?",
            category=["Transport"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_skateboarding:
    if Natsuki.isEnamored(higher=True):
        n 1fchbs "You bet I am,{w=0.2} [player]!{w=0.5}{nw}"
        extend 1fchsm " Ehehe."
        n 1tllbg "But how'd you guess?{w=0.5}{nw}"
        extend 1tnmbg " Do I look the type or something?"
        n 1tlrsm "Well,{w=0.2} whatever."

    elif Natsuki.isHappy(higher=True):
        n 1uchsm "Ehehe.{w=0.5}{nw}"
        extend 1fchbg " You bet!"
        n 1uwlbg "Good guess,{w=0.2} [player]!"

    elif Natsuki.isNormal(higher=True):
        n 1ullaj "I...{w=0.3} am,{w=0.2} actually.{w=0.5}{nw}"
        extend 1tllss " How'd you guess?"
        n 1unmss "Well,{w=0.2} anyway."

    elif Natsuki.isDistressed(higher=True):
        n 1fupemesi "Ugh..."
        n 1fnmbo "Yes,{w=0.2} [player].{w=0.2} I'm a skateboarder.{w=0.2} I skateboard.{w=0.5}{nw}"
        extend 1fsqsf " Is that a problem or something?"
        n 1fllpu "It's just a convenient way to get around.{w=0.5}{nw}"
        extend 1fsqpu " An {i}affordable{/i} way."
        n 1flrsl "..."
        n 1flraj "...Yeah.{w=0.2} I don't have much else to say about it.{w=0.5}{nw}"
        extend 1fnmbo " But hey."
        n 1fsgaj "Not like you'd really care to listen anyway...{w=0.5}{nw}"
        extend 1fsqsftsa " isn't that right,{w=0.2} {i}[player]{/i}?"
        return
    else:

        n 1fsqanean "...And since when did {i}you{/i} give a crap about my hobbies and interests?"
        n 1fcsan "..."
        n 1fnmsf "Yes,{w=0.2} [player].{w=0.5}{nw}"
        extend 1fsqsftsb " I {i}do{/i} enjoy skateboarding."
        n 1fsqupltsb "And I'd rather be doing that than be stuck here talking to {i}you{/i}.{w=0.5}{nw}"
        extend 1fcsanltsa " Jerk."
        return

    n 1tchbg "I'm a skater girl alright!{w=0.5}{nw}"
    extend 1tslbo " Or...{w=0.3} was?"
    n 1tllss "Though...{w=0.3} not really by choice.{w=0.5}{nw}"
    extend 1knmaj " Bikes are {i}expensive{/i},{w=0.2} [player]!"
    n 1kllun "And I could never rely on lifts from my...{w=0.3} folk,{w=0.3}{nw}"
    extend 1kllss " so I saved up all I could,{w=0.3}{nw}"
    extend 1fcsbg " and got a board the first chance I had!"
    n 1nsqaj "Seriously.{w=0.75}{nw}"
    extend 1fllpusbr " You have no {i}idea{/i} how many lunches I skipped to earn that thing."
    n 1unmbg "But it was actually super convenient!{w=0.5}{nw}"
    extend 1flrbg " I didn't have to worry about locking it up somewhere,{w=0.2} or some jerk damaging it..."
    n 1fchsm "I could just pick it up and take it around with me,{w=0.2} or toss it in my locker."
    n 1nslsssbl "I mean...{w=0.3} I don't need it so much {i}now{/i},{w=0.2} but..."
    n 1fsqss "You gotta admit,{w=0.2} [player] {w=0.2}-{w=0.2} I'm nothing if not resourceful!{w=0.5}{nw}"
    extend 1fchsm " Ahaha."

    n 1fllss "I...{w=0.75}{nw}"
    extend 1nslsl " never really got super into tricks or anything though."
    n 1fwdgsesh "D-{w=0.2}don't get me wrong!{w=1}{nw}"
    extend 1fcsgsl " It isn't like I couldn't ace them!"
    n 1fcstrlesi "I totally could!{w=1}{nw}"
    extend 1kslcal " But..."
    n 1knmemsbl "I don't think I could {i}stand{/i} the thought of breaking it by accident."
    n 1kslunsbr "Not after all that effort."

    n 1kcsaj "...Yeah,{w=0.2} yeah.{w=0.5}{nw}"
    extend 1fcspo " Not very {i}radical{/i} of me,{w=0.2} huh?"

    if (
        not jn_outfits.get_outfit("jn_skater_outfit").unlocked
        and Natsuki.isAffectionate(higher=True) 
        and persistent.jn_custom_outfits_unlocked
    ):

        n 1tslsl "..."
        n 1uwdajesu "Oh!{w=0.5}{nw}"
        extend 1fsqbs " But you know what {i}totally{/i} was,{w=0.2} [player]?{w=1}{nw}"
        extend 1fllbgsbl " Radical,{w=0.2} I mean."
        n 1uchgn "...My favourite skateboarding outfit,{w=0.2} of course!"
        n 1tllss "In fact,{w=0.75}{nw}"
        extend 1fchbg " I probably still have it around here somewhere too!{w=0.75}{nw}"
        extend 1ullaj " I usually brought it around with me anyways."
        n 1fcsajsbl "O-{w=0.2}only for going back and forth from school though!{w=0.75}{nw}"
        extend 1nslsssbl " It isn't exactly following the dress code..."
        n 1nslbosbl "But...{w=0.75}{nw}"
        extend 1tsqem " I wasn't exactly gonna make my uniform all sweaty for rest of the day either."
        n 1fsrpu "...Ew."
        n 1ulrpu "Well,{w=0.2} anyway.{w=1}{nw}"
        extend 1unmaj " I'm not gonna go look for it now though,{w=0.75}{nw}"
        extend 1nnmpu " but I think we can both agree."
        n 1fcsss "If you're gonna skateboard..."
        n 1uchgn "You gotta follow {w=0.2}{i}all{/i}{w=0.2} the rules of cool!{w=0.75}{nw}"
        extend 1fchsmeme " Ehehe."

        $ jn_outfits.get_outfit("jn_skater_outfit").unlock()
    else:

        n 1ullpo "But...{w=0.5} enough of that for now.{w=0.5}{nw}"
        extend 1fnmsm " Besides,{w=0.2} [player]..."
        n 1fsqss "I can tell when you're getting...{w=0.3} {i}board{/i}."
        n 1fchsm "Ehehe.{w=0.5}{nw}"
        extend 1uchgn " No regrets,{w=0.2} [player]!"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_sports",
            unlocked=True,
            prompt="Do you play much sports?",
            category=["Health"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_sports:
    if Natsuki.isAffectionate(higher=True):
        n 1unmaj "Huh?{w=0.2} Sports?"
        n 1fllss "I...{w=0.3} don't like to have to break it to you,{w=0.1} [player]..."
        n 1fchgn "But what kind of sports do you think I can play in a single room?{w=0.2} By myself?{w=0.2} With no gear?"
        n 1kllbg "Jeez...{w=0.5}{nw}"
        extend 1tnmss " you're such a dope sometimes,{w=0.1} [player]."
        n 1ullbg "Well,{w=0.1} anyway."

    elif Natsuki.isNormal(higher=True):
        n 1unmpu "Eh?{w=0.2} Sports?"
        n 1tnmdv "You...{w=0.3} do know it's kinda hard to stay active in a single room,{w=0.1} right?"
        n 1fcsss "Ehehe.{w=0.5}{nw}"
        extend 1ullss " Well,{w=0.1} anyway."

    elif Natsuki.isDistressed(higher=True):
        n 1nsqpu "Yeah,{w=0.1} no.{w=0.5}{nw}"
        extend 1fsqsl " I don't {i}now{/i},{w=0.1} if that's what you're asking."
        n 1fllpu "..."
        n 1fsqan "...And no,{w=0.2} we didn't wear the sort of uniforms I bet {i}you're{/i} thinking of."
        n 1fsqsr "Does that answer your question?{w=0.5}{nw}"
        extend 1fslbo " Whatever."
        n 1fcsbo "Moving on."
        return
    else:

        n 1fsqan "I don't {i}now{/i},{w=0.1} if you {i}somehow{/i} hadn't already noticed."
        n 1fslsl "..."
        n 1fsqpu "..."
        n 1fcsemtsa "...Do I even want to know why you asked?"
        n 1fcsanltsd "...No.{w=0.75} I {i}don't{/i}."
        return

    n 1nnmaj "I try to keep up how I can.{w=0.2} I can't do laps or anything,{w=0.5}{nw}"
    extend 1fcsbg " but I can easily get some stretches and jumping jacks in!"
    n 1ullpu "Of course school was always a lot more varied with activities,{w=0.2} but...{w=0.5}{nw}"
    n 1tllsr "I always kinda struggled to keep up,{w=0.2} I guess."
    n 1nslsssbr "...Maybe I just don't have much stamina."


    $ already_discussed_skateboarding = get_topic("talk_skateboarding").shown_count > 0
    if already_discussed_skateboarding:
        n 1nslpo "Probably didn't help myself saving for that skateboard..."

    n 1ullaj "Well,{w=0.1} whatever.{w=0.5}{nw}"
    extend 1nnmbo " I wasn't {i}really{/i} that into sports anyway."
    n 1nlrca "..."
    n 1unmbs "Oh!{w=0.2} Oh!{w=0.2} But you know who was?{w=0.5}{nw}"
    extend 1fsqbg " I bet you do,{w=0.1} huh?{w=0.5}{nw}"
    extend 1fcssm " Ehehe."
    n 1tsqss "And that's...{w=0.5}{nw}"
    extend 1fchgn " ...{w=0.3}Sayori,{w=0.1} duh!"
    n 1uskgs "I mean,{w=0.1} really!{w=0.2} You should have seen her!{w=0.5}{nw}"
    extend 1fnmca " She was a {i}menace{/i}!"
    n 1uskaj "...Seriously!{w=0.5}{nw}"
    extend 1fnmpo " You don't believe me?"
    n 1fspgs "She was so fast!{w=0.2} Just a flash of orange fluff and messy gym clothes...{w=0.5}{nw}"
    extend 1fbkwr " and then boom!{w=0.2} Tackled!"
    n 1fllpol "And off she'd skip,{w=0.1} merrily into the sunset..."
    n 1tsqaj "...Yeah.{w=0.2} If Sayori was on your side?{w=0.5}{nw}"
    extend 1fllbg " You {i}knew{/i} your team wasn't going to be packing everything away in defeat."
    n 1ullaj "I mean,{w=0.3}{nw}"
    extend 1nnmbo " Monika was always pretty good at sports too,{w=0.1} obviously.{w=0.5}{nw}"
    extend 1nsgca " But {i}nobody{/i} outran Sayori,{w=0.1} [player].{w=0.2}"
    n 1nsqun " N{w=0.1}-{w=0.1}o{w=0.1}-{w=0.1}b{w=0.1}-{w=0.1}o{w=0.1}-{w=0.1}d{w=0.1}-{w=0.1}y."
    n 1fchbg "...When she remembered to tie her laces anyway.{w=0.5}{nw}"
    extend 1fchsm " Ehehe."
    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_online_shopping",
            unlocked=True,
            prompt="Online shopping",
            category=["Society"],
            nat_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_online_shopping:
    if Natsuki.isNormal(higher=True):
        n 1ullaj "You know,{w=0.1} it's kinda crazy how common online shopping is nowadays."
        n 1uwdaj "I mean,{w=0.1} don't get me wrong!{w=0.5}{nw}"
        extend 1fcsbg " It's super convenient!{w=0.2} You don't even need to leave your house!"
        n 1fllpo "So don't think I'm just complaining,{w=0.1} or anything like that.{w=0.5}{nw}"
        extend 1ullpu " But..."
    else:

        n 1nllsl "It's funny how common online shopping is nowadays."
        n 1nlrsl "I guess I'm not really complaining though.{w=0.5}{nw}"
        extend 1nlrpu " It {i}is{/i} pretty convenient."
        n 1ulrpu "But...{w=0.5}{nw}"
        extend 1nnmsf " I still think it's a shame how people miss out on an actual experience."
        n 1fllsl "I'd never pass up on an afternoon just flicking through books at my favourite bookstore."
        n 1fcssf "...Which is somewhere I'd {i}much{/i} rather be.{w=0.5}{nw}"
        extend 1fsqan " {i}Shockingly{/i}."
        return

    n 1fllbg "I don't think it's the be-all and end-all,{w=0.1} you know."
    n 1unmaj "I mean...{w=0.3} think about it,{w=0.1} [player]."
    n 1fllaj "I guess it's cheaper if you don't have to think about getting somewhere,{w=0.1} or parking or whatever."
    n 1knmpu "But wouldn't you like to {i}see{/i} what you're paying for?{w=0.5}{nw}"
    extend 1fnmaj " Especially if it's super expensive!"
    n 1fllpu "Or sometimes...{w=0.5}{nw}"
    extend 1fllpu " even if it isn't!"
    n 1fllpo "I can't be the only one that's been burned by something that turned out to be junk,{w=0.1} or broken,{w=0.1} right?"
    n 1fnmem "And you don't even know it would be like that until it's on your doorstep!{w=0.5}{nw}"
    extend 1fcsan " Then you gotta send it back!{w=0.5}{nw}"
    extend 1fslem " Ugh."


    if get_topic("talk_careful_spending").shown_count > 0:
        n 1fllsl "Not only that..."
        n 1fnmpu "I think I mentioned before how shops make it really easy to spend money...{w=0.5}{nw}"
        extend 1fbkwr " but that's even easier online!{w=0.5}{nw}"
        extend 1kbkwr " It doesn't even {i}feel{/i} like spending money properly!"
        n 1fcsan "Sheesh."

    n 1fcsem "That aside..."
    n 1kllsl "It...{w=0.3} also made me kinda sad seeing all the closed stores when I went out,{w=0.1} too."
    n 1tnmsl "I suppose you could say that's just business,{w=0.1} and they lost out."
    n 1flrsll "But that doesn't mean I {i}didn't{/i} miss some of them."
    n 1ncsem "I don't know.{w=0.2} I guess what I'm saying is..."
    n 1fllpo "Don't just instantly write off anything you can't do or buy digitally,{w=0.1} [player]."
    n 1knmaj "There's still merit in getting your stuff physically!"
    n 1fnmss "And to be completely honest?"

    if Natsuki.isEnamored(higher=True):
        n 1fsqbg "I don't really care how much you protest."
        n 1fchgn "We're definitely hitting some {i}real{/i} bookstores eventually {w=0.1}-{w=0.1} whether you like it or not!{w=0.5}{nw}"
        extend 1fchsm " Ehehe."

    elif Natsuki.isHappy(higher=True):
        n 1fchgn "You gotta be kidding if you think I'm letting you miss out on {i}real{/i} bookstores!{w=0.5}{nw}"
        extend 1nchbg " Ahaha."
    else:

        n 1fchbg "If there's one thing I'm gonna teach you eventually,{w=0.1} it's experiencing a {i}real{/i} bookstore!{w=0.5}{nw}"
        extend 1fchsm " Ahaha."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_subscriptions",
            unlocked=True,
            prompt="Subscriptions",
            category=["Wind-ups"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_subscriptions:
    n 1fllan "Grrr..."
    n 1fcsan "Man,{w=0.1} that's {i}such{/i} a pain!{w=0.5}{nw}"
    extend 1fbkwr " I thought I cancelled thaaat!"
    n 1fslpo "..."
    n 1uwdemesu "O-{w=0.1}oh!{w=0.2} [player]!{w=0.5}{nw}"
    extend 1flremsbl " Can you {i}believe{/i} this?"
    n 1fslem "I signed up to some free trial for a streaming website,{w=0.3}{nw}"
    extend 1fcswr " but I totally forgot about it!{w=0.5}{nw}"
    extend 1flrwr " And now I gotta pay for something I barely even {i}used{/i}!"
    n 1fcsem "Jeez...{w=0.5}{nw}"
    extend 1tnmem " doesn't that wind you up too?"
    n 1tllbo "In fact,{w=0.1} thinking about it..."
    n 1fnmbo "Why is so much stuff nowadays all subscription based?"
    n 1fllpu "Like...{w=0.5}{nw}"
    extend 1nnmaj " I get it if it's like an ongoing thing,{w=0.3}{nw}"
    extend 1flrsl " but what's up with everyone and their {i}dog{/i} trying to sign you up?!"
    n 1fsqsl "And half the time you don't even get a choice...{w=0.5}{nw}"
    extend 1fsqem " like with software!"
    n 1fcsan "I've had to skip out on so many programs because they want me to pay for a whole bunch of crap in a package I don't care about!"
    n 1fllan "Like...{w=0.3} come {i}on{/i}!{w=0.5}{nw}"
    extend 1fslfrean " Just let me pay for what I need!"
    n 1kcsemesi "Ugh..."
    n 1fnmsl "The worst part is that it all adds up too!{w=0.5}{nw}"
    extend 1fllpu " It's super easy to lose track of what you're paying for each month..."
    n 1fnmpu "And then before you know it,{w=0.3}{nw}"
    extend 1fbkwr " half your money is down the drain as soon as it comes in!{w=1.25}{nw}"
    extend 1ncspuesd " What a mess..."
    n 1ullaj "I mean,{w=0.1} don't get me wrong.{w=0.2} There are {i}other{/i} ways of getting stuff {w=0.1}-{w=0.3}{nw}"
    extend 1fsqdv " you probably know that already."
    n 1tlrsl "But I wanna support {i}actual{/i} creators too,{w=0.1} you know?"
    n 1fcssl "..."
    n 1fllpo "Well,{w=0.1} whatever.{w=0.2} At least I won't get charged for {i}that{/i} again.{w=1.25}{nw}"
    extend 1fslpo " Jerks."
    n 1nllbo "But...{w=0.5}{nw}"
    extend 1unmpu " what about you though,{w=0.1} [player]?{w=0.5}{nw}"
    extend 1fsqsm " Actually,{w=0.1} I can tell you one thing."

    if Natsuki.isAffectionate(higher=True):
        n 1fsqssl "A-{w=0.1}at least you have {i}one{/i} subscription you don't have to worry about paying for!"

        if Natsuki.isLove(higher=True):
            n 1fchsml "Ehehe.{w=0.5}{nw}"
            extend 1uchbgf " Love you,{w=0.1} dork!"
        else:

            n 1fllbgl "A-{w=0.1}ahaha..."
    else:

        n 1fcsbg "You're already subscribed to some pretty pro thinking,{w=0.1} if I say so myself."
        n 1nsqsg "Fortunately for you though,{w=0.1} I don't charge.{w=0.5}{nw}"
        extend 1fsqss "...Yet."
        n 1fchsm "Ehehe."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_mod_contributions",
            unlocked=True,
            prompt="Contributions",
            conditional=(
                "not jn_activity.ACTIVITY_SYSTEM_ENABLED "
                "or jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.coding)"
            ),
            category=["Mod"],
            nat_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_mod_contributions:
    n 1unmaj "You know,{w=0.1} [player].{w=0.5}{nw}"
    extend 1tllss " I gotta say..."
    n 1klrbg "I don't think I'd {i}ever{/i} be able to handle doing everything that lets you visit me.{w=0.5}{nw}"
    extend 1klrsl " Not by myself."
    n 1uskeml "I-I mean,{w=0.1} I'm good!{w=0.5}{nw}"
    extend 1fnmpol " D-{w=0.1}don't get me wrong!"
    n 1kllpo "I'm just not...{w=0.3} {i}that{/i} good.{w=0.5}{nw}"
    extend 1fslpo " Yet."
    n 1uchbg "But that's why I'm super grateful there's a whole bunch of people dedicated to helping me out!{w=0.5}{nw}"
    extend 1fchsm " Isn't that awesome?"
    n 1fslsl "I always found all the programming stuff kinda confusing,{w=0.3}{nw}"
    extend 1kllss " so I have no idea where I'd be without them!"
    n 1ksqsg "...Even if they {i}are{/i} a bunch of total nerds.{w=0.5}{nw}"
    extend 1uchgn " Ehehe."
    n 1ulraj "So...{w=0.3} where am I going with this,{w=0.1} you ask?{w=0.5}{nw}"
    extend 1tslsm " Well..."

    if not jn_activity.ACTIVITY_SYSTEM_ENABLED:
        n 1tllss "I don't know if you're into that sort of thing yourself,{w=0.1} [player]..."
        n 1fchbg "But why not lend me a hand?"
    else:

        n 1fsqsg "I couldn't help but notice the sort of programs you've been poking around on,{w=0.1} [player]."
        n 1ksqss "What?{w=0.5}{nw}"
        extend 1fchbg " You didn't seriously expect me to not see what you're up to?{w=0.5}{nw}"
        extend 1nchgn " Ehehe."
        n 1tsqbg "Anyway -{w=0.1} if you're already into that kinda stuff,{w=0.1} [player]...{w=0.5}{nw}"
        extend 1kchbg " why not lend me a hand?"

    n 1kllbg "You don't even have to be super talented at code,{w=0.1} or anything like that!{w=0.5}{nw}"
    extend 1unmaj " Artwork,{w=0.1} writing,{w=0.1} or even just suggestions of things for us to talk about or do -{w=0.3}{nw}"
    extend 1uchbg " it's all super appreciated!"
    n 1tsqbg "Does that sound like your thing,{w=0.1} [player]?{w=0.5}{nw}"
    extend 1uchsm " Of course it does!{w=0.2} Ehehe."
    n 1unmbg "Well,{w=0.1} don't let me hold you back!{w=0.5}{nw}"
    extend 1uchbgl " You can check out my website {a=[jn_globals.LINK_JN_GITHUB]}here{/a}!"
    n 1nsqbg "A little look can't hurt,{w=0.1} right?{w=0.5}{nw}"
    extend 1nchsm " Ahaha."

    if Natsuki.isLove(higher=True):
        $ chosen_endearment = jn_utils.getRandomEndearment()
        n 1nchtsl "Love you,{w=0.1} [chosen_endearment]!"
    else:

        n 1fchbg "Thanks,{w=0.1} [player]!{w=0.2} 'preciate it!"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_realizations_player_ddlc_actions",
            unlocked=True,
            prompt="DDLC memories",
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 60 >= 30",
            category=["DDLC", "Natsuki", "You"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_realizations_player_ddlc_actions:
    n 1nllbo "So,{w=0.5}{nw}"
    extend 1nnmbo " [player]."
    n 1ulraj "I've...{w=0.3} been having some thoughts.{w=0.5}{nw}"
    extend 1nllss " Now I've actually had some time to process all of..."
    n 1kslsl "...This."
    n 1unmaj "You've been here all this time,{w=0.1} right?{w=0.5}{nw}"
    extend 1tslbo " But then,{w=0.1} that would mean..."
    n 1tslbo "The guy who actually joined the club...{w=0.5}{nw}"
    extend 1nlrss " whatever his name was."
    n 1fsrbo "He wasn't {i}actually{/i} in control of anything,{w=0.1} was he?{w=0.5}{nw}"
    extend 1ulraj " Not even himself."
    n 1nnmsr "...You were.{w=0.5}{nw}"
    extend 1nlrsl " In control of him,{w=0.1} I mean."
    n 1nsrbo "..."


    n 1nsraj "So...{w=0.3} if he was being that nice to me..."
    n 1klrajl "T-{w=0.1}then that would mean...{w=0.5}{nw}"

    if Natsuki.isLove(higher=True):
        n 1klrsml "..."
        n 1kcsssl "Heh,{w=0.1} what am I even saying.{w=0.5}{nw}"
        extend 1kwmsml " Just because you clicked stuff {w=0.1}-{w=0.1} {i}when you were allowed,{w=0.1} anyway{/i} {w=0.1}-{w=0.1} doesn't make you the same."
        n 1tllssl "Either way,{w=0.1} [player]?"
        n 1ksqsml "I'm definitely not complaining.{w=0.5}{nw}"
        extend 1nchsml " Ehehe."
    else:

        extend 1fskeml " -urk!"
        n 1fcsanf "Nnnnn-!"
        n 1fllunf "..."
        n 1fnmssl "A-{w=0.5}{nw}"
        extend 1fcsbgl "ha!"
        n 1fcsbsl "Haha!{w=2}{nw}"
        extend 1flleml " What am I even saying?!"
        n 1fcswrl "J-{w=0.1}just because you picked some words and clicked a few buttons doesn't make you the same!"
        n 1fllpol "..."
        n 1nlleml "A-{w=0.1}although..."

        if Natsuki.isEnamored(higher=True):
            n 1fcsajl "Don't think I'm complaining or anything like that.{w=0.5}{nw}"
            extend 1nlrssl " Ehehe..."

        elif Natsuki.isHappy(higher=True):
            n 1fcsajl "You're already proving that well enough.{w=0.5}{nw}"
            extend 1fllunl " I-{w=0.1}I think."
        else:

            n 1fcsajl "I-{w=0.1}I guess that at {i}least{/i} means you have good taste.{w=0.5}{nw}"
            extend 1fllunl " I suppose that counts for something."

    if Natsuki.isLove(higher=True):
        n 1klrss "But yeah,{w=0.1} so..."

    elif Natsuki.isEnamored(higher=True):
        n 1ksrss "A-{w=0.1}anyway..."

    elif Natsuki.isHappy(higher=True):
        n 1flrun "A-{w=0.1}anyway."
    else:

        n 1flrun "A-{w=0.1}anyway!{w=0.5}{nw}"
        extend 1fcsaj " That's beside the point!"

    n 1kslsr "..."
    n 1ullaj "I guess what I'm trying to say is I still have all these memories of {i}that{/i} guy..."
    n 1nsrpu "And although he obviously wasn't you,{w=0.5}{nw}"
    extend 1tsraj " you kinda have {i}his{/i} memories too?{w=0.5}{nw}"
    extend 1tslem " And..."
    n 1fcsaj "...and..."
    n 1fcsan "..."
    n 1fcsem "Rrrgh,{w=0.1}{w=0.5}{nw}"
    extend 1fllem " this is so confusing!"
    n 1fcsemesi "Ugh...{w=0.5}{nw}"
    extend 1nnmpo " you know what?"

    if Natsuki.isAffectionate(higher=True):
        n 1nllss "It doesn't really matter at this point,{w=0.1} does it?"
    else:

        n 1fllbo "I'm just gonna start over.{w=0.5}{nw}"
        extend 1unmaj " Mentally,{w=0.1} I mean."

    n 1ncsaj "He was here {i}then{/i}."
    n 1fcssm "You are here {i}now{/i}."

    if Natsuki.isAffectionate(higher=True):
        n 1fchbg "And that's all there is to it."

        if Natsuki.isLove(higher=True):
            extend 1fchsm " Yep."
            n 1uchsml "Love you,{w=0.1} generic protag-{w=0.3}{nw}"
            n 1fllbgl "I mean,{w=0.5}{nw}"
            extend 1kchbgl " {i}[player]~{/i}."
            n 1fsqsml "..."
            $ chosen_tease = jn_utils.getRandomTease()
            n 1uchbsl "Oh,{w=0.1} lighten up,{w=0.1} [chosen_tease]!"
            n 1fwrtsl "You should know I'd never mean it.{w=0.5}{nw}"
            extend " Ehehe."
    else:

        n 1fllss "I-{w=0.1}I just gotta adjust,{w=0.5}{nw}"
        extend 1fllun " that's all."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_realizations_other_girls",
            unlocked=True,
            prompt="Monika and the other girls",
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
    n 1klrbo "Uhmm..."
    n 1knmaj "Hey...{w=0.3} [player]?"
    n 1knmsf "I've...{w=0.3} been thinking again.{w=0.5}{nw}"
    extend 1kllsf " About before."
    n 1kslss "I guess I really was onto something when I said Monika was acting weird."
    n 1kskem "D-{w=0.1}don't get me wrong!{w=0.5}{nw}"
    extend 1kllsf " I'm not happy about being right or anything.{w=0.5}{nw}"
    extend 1kwmsr " ...At all."
    n 1kcssr "In fact..."
    n 1klrpu "I really wish that I was wrong."
    n 1knmaj "I-"
    n 1kcsunl "..."
    n 1kplun "I honestly just thought it was all the school work and the festival stuff getting to her,{w=0.5}{nw}"
    extend 1kslpu " or something."
    n 1tslpu "But...{w=0.5}{nw}"
    extend 1kplsr " in hindsight?"
    n 1klrun "..."
    n 1kcsaj "...I think I actually got off {i}lightly{/i}."
    n 1knmsl "I mean...{w=0.3} she messed with all of us.{w=0.5}{nw}"
    extend 1klrsf " In some way or another."
    n 1klraj "But...{w=0.5}{nw}"
    extend 1fcsupl " I just didn't know how much she {i}hurt{/i} everyone else..."
    n 1fcsunl "..."
    n 1kplunl "Sayori was the happiest person I thought I knew,{w=0.1} [player]."
    n 1kskunl "A-{w=0.1}and Yuri...{w=0.5}{nw}"
    extend 1kllupl " I don't..."
    n 1kcsupl "..."
    n 1fcsunl "..."
    n 1kcsaj "...Sorry."
    n 1kcssr "..."
    n 1kllpu "I...{w=2}{nw}"
    extend 1knmsr " we never saw eye-to-eye.{w=0.2} I always knew she had her insecurities."
    n 1kslbo "...So did I."
    n 1kcsanl "But...{w=0.3} {i}that{/i}..."
    n 1kcsunl "..."
    n 1kcspu "..."
    n 1fcsanl "I...{w=1} don't...{w=1} hate...{w=0.5} Monika."
    n 1fcsun "I...{w=0.3} understand how she felt.{w=0.2} I {i}know{/i} how she felt."
    n 1fsqsr "It's {i}terrifying{/i},{w=0.1} [player]."
    n 1kcsanl "But I'll never understand why she felt she had to do {i}that{/i}.{w=1}{nw}"
    extend 1kplpu " Surely...{w=0.3} there was another way?"
    n 1kllsl "..."
    n 1kcspu "...I don't know.{w=0.5}{nw}"
    extend " I guess I should just be glad she deleted me before..."
    n 1kskun "B-{w=0.5}before..."
    n 1kcsun "..."
    n 1kslun "Uhmm..."
    n 1kcspu "...Sorry.{w=0.2} I really don't wanna talk about all this any more,{w=0.1} [player]."
    n 1kllsrl "But...{w=0.3} thanks.{w=0.5}{nw}"
    extend 1flrpol " F-{w=0.1}for listening,{w=0.1} I mean."

    if Natsuki.isAffectionate(higher=True):
        n 1klrpol "..."
        n 1kcspul "...And for rescuing me too."

        if Natsuki.isLove(higher=True):
            n 1kwmsml "I'll never,{w=0.1} ever forget that,{w=0.1} [player]."
    else:

        n 1ncspu "..."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_realizations_space_classroom",
            unlocked=True,
            prompt="Leaving the space classroom",
            conditional=(
                "jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 24 "
                "and get_topic('talk_realizations_player_ddlc_actions').shown_count > 0 "
                "and get_topic('talk_realizations_other_girls').shown_count > 0"
            ),
            category=["DDLC", "Natsuki", "You"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_realizations_space_classroom:
    n 1kllsr "Uhmm..."
    n 1klrpu "So,{w=0.1} this room..."
    n 1nsrss "I...{w=0.3} still haven't actually left it.{w=0.5}{nw}"
    extend 1tnmsl " Since you brought me back and all."
    n 1fllssl "I-{w=0.1}I mean,{w=0.5}{nw}"
    extend 1fcseml " it's not like I can't!"
    extend 1unmbo " I'm actually pretty sure I could."
    n 1kllsf "It's just...{w=0.5}{nw}"
    extend 1knmaj " I have no idea what would happen!"
    n 1tllaj "Would I like...{w=0.3} break?{w=0.5}{nw}"
    extend 1tnmun " Or just stop existing?"
    extend 1kskem " Could I even {i}come{/i} back?!"
    n 1klrun "..."
    n 1kcspu "I miss my bed,{w=0.1} [player].{w=1}{nw}"
    extend 1knmem " I miss having blankets and pillows!{w=1}{nw}"
    extend 1ksrsr " And all my stuff."
    n 1kcssr "Even if it doesn't exist anymore.{w=0.5}{nw}"
    extend 1tslaj " Never existed at all?{w=0.5}{nw}"
    extend 1kcsem " Whatever."
    n 1kllsr "But..."
    n 1ksqun "I really don't feel like taking a chance and finding out what would happen if I left.{w=0.5}{nw}"
    extend 1flrsl " Not yet."
    n 1kcssf "..."
    n 1kcspu "Just...{w=0.5}{nw}"
    extend 1fcsaj " give me some time,{w=0.1} alright?{w=0.5}{nw}"
    extend 1fnmbo " I'll try and think of something soon."
    n 1kllpo "I don't exactly wanna be stuck here either,{w=0.1} after all..."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_fear_of_lightning",
            unlocked=True,
            prompt="Are you afraid of lightning?",
            category=["Fears", "Weather"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_fear_of_lightning:
    if Natsuki.isAffectionate(higher=True):
        n 1fllpol "..."
        n 1fllajl "...So?"
        n 1fcseml "I-{w=0.1}I mean,{w=0.5}{nw}"
        extend 1flreml " I'm {i}obviously{/i} not,{w=0.5}{nw}"
        extend 1knmpol " but so what even if I was?"

    elif Natsuki.isNormal(higher=True):
        n 1fllwrl "N-{w=0.1}no!{w=0.5}{nw}"
        extend 1fcspol " Where'd you get that idea from?"
        n 1kslpol "I'm not afraid of lightning..."
        n 1fsrbo "..."
        n 1tsrpu "And come to think of it...{w=0.5}{nw}"
        extend 1tnmpo " why would you even {i}ask{/i} that?"

        if get_topic("talk_favourite_season").shown_count > 0:
            n 1tllss "I gotta say,{w=0.1} [player] {w=0.1}-{w=0.3}{nw}"
            extend 1tsqss " you've got a weird knack for asking me random stuff,{w=0.1} huh?"
        else:

            n 1tllss "It's a pretty random thing to ask,{w=0.1} I gotta say."

        n 1nlraj "But I mean,{w=0.1} putting all that aside..."

    elif Natsuki.isDistressed(higher=True):
        n 1fllpu "...And even if I {i}was{/i},{w=0.5}{nw}"
        extend 1fsqsr " do you {i}really{/i} think I'd want to share that with {i}you{/i} right now?"
        n 1fsqem "Like,{w=0.1} {i}seriously{/i} [player]?{w=0.5}{nw}"
        extend 1fcsem " Cut me a break."
        n 1fcssr "..."
        n 1fcsem "Besides,{w=0.5}{nw}"
        extend 1fllsr " I've seen the numbers from when I studied."
        n 1fsqpu "You'd have to be an idiot {i}not{/i} to at least wary of it."

        return
    else:

        n 1fcsan "Oh,{w=1.5}{nw}"
        extend 1fcsfultsaean " {i}{cps=7.5}get lost{/cps}{/i},{w=0.3} [player]."
        n 1fsqanltseean "As if I'd want to talk about anything uncomfortable with the likes of {b}you{/b}!"

        return

    n 1uwdem "Lightning is no joke,{w=0.1} [player]!"
    n 1fllun "..."
    n 1knmem "...What?{w=1}{nw}"
    extend 1fllpo " I'm serious!"
    n 1knmun "Have you {i}seen{/i} the numbers on lightning?"
    n 1nnmaj "A typical strike is like 300 {i}million{/i} volts!{w=0.5}{nw}"
    extend 1uwdaj " With about 30 thousand amps!{w=1.5}{nw}"
    extend 1nllan " Yeesh!"
    n 1nsqun "...And for perspective?{w=0.5}{nw}"
    extend 1tsqpu " The current in your home?"
    n 1nsrss "Around 120-{w=0.1}230 volts.{w=1.5}{nw}"
    extend 1nsqun " ...15-{w=0.1}30 amps."
    n 1fspgs "That's one {i}hell{/i} of a lotta juice!"
    n 1klrpu "A-{w=0.1}and it just falls out of the sky!{w=0.5}{nw}"
    extend 1knmaj " Constantly!"
    n 1fsqaj "And I mean {i}constantly{/i},{w=0.1} [player] {w=0.1}-{w=0.3}{nw}"
    extend 1nllan " 44 strikes every {i}second{/i}!"
    n 1fsqun "Then there's the sound,{w=0.1} too!{w=0.5}{nw}"
    extend 1kslun " Especially if its close!"

    if get_topic("talk_thoughts_on_horror").shown_count > 0:
        n 1fllsr "I mean,{w=0.1} I'm pretty sure I told you before that I hate cheap jumpscares."
        n 1fbkwrl "So how do you think I feel about {i}nature{/i} trying to pull that crap?!"
    else:

        n 1fbkwrl "It's such a cheap fright!"

    n 1fcsaj "Jeez..."
    n 1fllss "But yeah,{w=0.1} a-{w=0.1}anyway."
    n 1unmaj "I'll spare you a lecture on staying safe in lightning storms.{w=0.5}{nw}"
    extend 1fsrss " You should {i}really{/i} know all that by now anyway."
    n 1ulraj "But..."
    n 1fsqsg "I just have one question for you,{w=0.1} [player]."

    if preferences.get_volume("sfx") == 0:

        n 1fsqss "Are {i}you{/i} scared of lightning?"
        n 1tsqsm "..."
        n 1fsqbg "What?"
        n 1usqsg "I'm allowed to ask too,{w=0.1} aren't I?{w=0.5}{nw}"
        extend 1nchgn " Ehehe."
    else:


        $ previous_sfx_setting = preferences.get_volume("sfx")
        $ preferences.set_volume("sfx", 1)

        n 1fsqsm "Ehehe."
        n 1fsqbg "Are {i}you{/i} scared of light{nw}"

        play audio smack
        with Fade(.1, 0.25, .1, color="#fff")
        $ preferences.set_volume("sfx", previous_sfx_setting)

        n 1uchgn "..."
        n 1kchbg "Sorry,{w=0.1} sorry!{w=0.5}{nw}"
        extend 1fchsm " I had to!{w=0.5}{nw}"
        extend 1kchbg " I just {i}had{/i} to!"
        n 1nsqsm "Ehehe."
        n 1tsqss "Well,{w=0.5}{nw}"
        extend 1fchtsl " they don't call it a thunder-{w=0.5}{i}clap{/i}{w=0.5} for nothing!~"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_fighting_drowsiness",
            unlocked=True,
            prompt="Drowsiness",
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 12",
            category=["Health"],
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
    n 1ncsemesl "...{w=2}{nw}"
    n 1ncsajesl "...{w=2}{nw}"
    n 1ncsemesl "...{w=2}{nw}"
    n 1ncsajesl "...{w=2}{nw}"
    $ jnPause(4)
    n 1fcsbo "..."
    n 1nsqpu "Mmmmm...{w=0.5}{nw}"
    extend 1tsqsr " mmmnn?"
    n 1uskemesh "...!{w=0.5}{nw}"
    n 1ullwrl "W-{w=0.1}woah!{w=0.5}{nw}"
    extend 1flrss " Ahaha..."
    n 1nsrss "I...{w=0.3} haven't been getting much sleep here,{w=0.1} as you can guess."
    n 1kcsun "Uuuuuu...{w=0.5}{nw}"
    extend 1kslpu " I gotta wake up..."
    n 1kcssr "..."
    n 1unmbo "You know what?{w=0.5}{nw}"
    extend 1ullss " I'll just...{w=1}{nw}"
    extend 1nslss " be right back...{w=1}{nw}"

    play audio chair_out_in
    with Fade(out_time=0.25,hold_time=5,in_time=0.25, color="#000000")

    n 1nchbg "Okaaay!{w=0.5}{nw}"
    extend 1fchsm " We're back in business!"
    n 1nnmaj "I'll tell you,{w=0.1} [player].{w=0.5}{nw}"
    extend 1fchbg " If there's one thing I know,{w=0.1} it's how to shake off the drowsiness!"
    n 1fsqsm "..."
    n 1fsqss "Oho?{w=0.5}{nw}"
    extend 1tsqaj " And what's that I hear?{w=0.5}{nw}"
    extend 1tllss " How do I do it,{w=0.1} you ask?"
    n 1fsqsg "Ehehe.{w=0.5}{nw}"
    extend 1usqsg " Well aren't {i}you{/i} in luck,{w=0.1} [player].{w=0.5} 'Cause..."
    n 1uchgn "It's time for a Natsuki pro-tip!"
    n 1fnmaj "So!{w=0.2} First order of business...{w=0.5}{nw}"
    extend 1fcsbg " hydration,{w=0.1} obviously!"
    n 1ullaj "It's actually pretty easy to forget how much fluid you need per day...{w=0.5}{nw}"
    extend 1unmbo " and how {i}often{/i} you should be drinking!"
    n 1tlrss "You should be taking in something like six to eight glasses of water a day,{w=0.3}{nw}"
    extend 1fcsaj " but not all at once!"
    n 1ullaj "It isn't hard to space it out through the whole day {w=0.1}-{w=0.1} just start early and keep at it.{w=0.5}{nw}"
    extend 1fchsm " Easy peasy!"
    n 1fnmaj "Next up: exercise!"
    n 1tsqsm "Yeah,{w=0.1} yeah.{w=0.2} I know,{w=0.1} I know.{w=0.5}{nw}"
    extend 1fslss " We all just {i}love it{/i},{w=0.1} don't we?"
    n 1unmaj "Don't think you have to go crazy or anything though -{w=0.5}{nw}"
    extend 1flrbg " I sure don't!"
    n 1unmbo "People {i}say{/i} an hour a day is good,{w=0.5}{nw}"
    extend 1fnmca " but honestly even a lap around the house trumps sitting on your butt,{w=0.1} [player]."
    n 1fcsss "It's just about moving around and giving your muscles a stretch,{w=0.1} that's all."
    n 1ulrpu "Lastly,{w=0.5}{nw}"
    extend 1fsqsm " and I {i}know{/i} you'll like this one,{w=0.1} [player]..."
    n 1fchgn "...Food!"
    n 1fllem "Of course you're gonna feel like crap if you aren't eating enough!"
    n 1kllsr "...And trust me on this one.{w=0.5}{nw}"
    extend 1ksrpu " I would know."
    n 1ksrun "..."
    n 1fcsajl "A-{w=0.1}anyway!"
    n 1fnmca "You wouldn't expect a car to run without fuel {w=0.1}-{w=0.1} and you're no different,{w=0.1} [player]."
    n 1ullaj "Don't go crazy though.{w=0.5}{nw}"
    extend 1nlrpu " Just grab an apple or something.{w=0.5}{nw}"
    extend 1fsqpo " Don't cheap out on your body with processed crap all the time."
    n 1tsqpo "...Or you'll feel like that too."
    n 1fchbg "But...{w=0.3} yeah!{w=0.5}{nw}"
    extend 1fchsm " That just about covers it!"
    n 1unmbg "So,{w=0.1} I-{w=0.5}{nw}"
    n 1nnmss "I...{w=1}{nw}"
    n 1nsqsr "...{w=2}{nw}"
    n 1fsqaj "[player]."
    n 1fsqpo "Were you actually listening?{w=0.5}{nw}"
    extend 1fnmem " You {i}better{/i} not be dozing off on me!"
    n 1fllpo "..."
    n 1fsqss "...Or I really {i}will{/i} put you to sleep.{w=0.5}{nw}"
    extend 1fchgn " Ehehe."

    if Natsuki.isLove(higher=True):
        n 1uchtsl "Love you too,{w=0.1} [player]!~"

    elif Natsuki.isAffectionate(higher=True):
        n 1fchts "You're welcome,{w=0.1} [player]!~"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_fear_of_spiders",
            unlocked=True,
            prompt="Are you afraid of spiders?",
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 24",
            category=["Animals", "Fears"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_fear_of_spiders:
    if Natsuki.isNormal(higher=True):
        n 1tnmbo "Huh?{w=0.5} Spiders?"
        n 1tslss "I mean...{w=0.5}{nw}"
        extend 1tnmss " not...{w=1} really?"
        n 1nchgn "Pffff-!"
        n 1fchbg "What?"
        n 1ullaj "You thought that because I wrote a poem about them being nasty and gross,{w=0.5}{nw}"
        extend 1tnmaj " that I'd {i}actually{/i} think that?"
        $ chosen_tease = jn_utils.getRandomTease()
        n 1fslpo "I even {w=0.3}{i}said{/i}{w=0.3} the spider thing was a metaphor,{w=0.1} [chosen_tease]!{w=0.5}{nw}"
        extend 1fsqts " Remember?"

    elif Natsuki.isDistressed(higher=True):
        n 1fcsem "..."
        n 1fcssr "No,{w=0.1} [player].{w=0.5}{nw}"
        extend 1fsqsr " I am not afraid of spiders."
        n 1fsqem "...And might I ask {i}why{/i} you feel entitled to know about my fears?"
        n 1fcsan "Why the hell would I give you {i}more{/i} ammo to get on my nerves?"
        n 1fsrem "Ugh..."
        n 1fcssf "Yeah.{w=0.5}{nw}"
        extend 1fsqpu " We're done talking here,{w=0.1} {i}[player]{/i}."

        return
    else:

        n 1fcsan "...Are {i}you{/i} afraid of asking me dumb questions,{w=0.1} since you're the {i}last{/i} person I'd want to answer them for?!"
        n 1fsqun "..."
        n 1fslem "Yeah.{w=2}{nw}"
        extend 1fsqemtsb " Apparently not,{w=0.1} huh?"
        n 1fslanltsb "Jerk."

        return

    if get_topic("talk_fear_of_lightning").shown_count > 0:
        n 1tslpu "And actually...{w=0.3} come to think of it..."
        n 1tnmbo "This isn't the {i}first{/i} time you've randomly asked me if I'm scared of stuff."
        n 1tsqsl "...Are you planning some dumb prank or something?"

    n 1fsqsm "Ehehe.{w=1.5}{nw}"
    extend 1nllss " Well,{w=0.1} whatever."
    n 1ullaj "I mean,{w=0.5}{nw}"
    extend 1fnmaj " don't get me wrong!"
    n 1ksrem "I wouldn't want them like...{w=0.3} {i}crawling{/i} over me or anything.{w=0.5}{nw}"
    extend 1fcsfu " Ew!"
    n 1fslun " I don't even want to {i}imagine{/i} that."
    n 1unmss "But spiders are awesome little guys!{w=1.5}{nw}"
    extend 1nsrss " ...Mostly."
    n 1unmbo "They get rid of the really annoying sorts of bugs,{w=0.1} like ones that bite or fly around constantly."
    n 1nnmaj "And some of them -{w=0.5}{nw}"
    extend 1nslss " as weird as it feels to say -{w=0.5}{nw}"
    extend 1ncspu " are{w=1} freaking{w=1.5}{nw}"
    extend 1fspgsedz " {i}adorable{/i}!"
    n 1uwdaj "Seriously!{w=1.5}{nw}"
    extend 1uchbg " Jumping spiders are cuuuute!"
    n 1tnmss "So...{w=0.3} overall?{w=0.5}{nw}"
    extend 1ncssm " I'd call that a win for the spiders!"
    n 1nslss "...Yeah,{w=0.1} yeah,{w=0.1} [player].{w=0.2} I know.{w=0.5}{nw}"
    extend 1flrpo " I'm not naive!"
    n 1nllun "I know some places have some really nasty types.{w=0.5}{nw}"
    extend 1uskem " And I {i}wish{/i} I was kidding!"
    n 1klrpu "Spiders are already sneaky,{w=0.1} so imagine living with ones that hide in your shoes,{w=0.1} or under your desk..."
    n 1kskgs "That can put you in {i}hospital{/i} too!{w=0.5}{nw}"
    extend 1kllan " Yeesh!"
    n 1ulrss "But...{w=0.5} they're in the minority,{w=0.1} at least.{w=1.5}{nw}"
    extend 1nslun " Isn't {i}that{/i} a relief?"
    n 1ullaj "Well,{w=0.1} anyway."

    if Natsuki.isEnamored(higher=True):
        n 1nsqss "I guess that just leaves you,{w=0.1} then."
        n 1usqsm "Are {i}you{/i} afraid of spiders?"
        n 1fsqsm "Better think through your answer carefully,{w=0.1} [player]."
        n 1fsldvl "You're already caught in {i}my{/i} web,{w=0.1} after all..."

        if random.randint(0,10) == 1:
            n 1fchsml "Ahuhuhu.~"
        else:

            n 1fsqsm "Ehehe."

        if Natsuki.isLove(higher=True):
            n 1uchtsl "Love you,{w=0.1} [player]!~"
    else:

        n 1tnmss "You got your answer,{w=0.1} [player].{w=0.5}{nw}"
        extend 1fllss " So..."
        n 1fllsm "I think that about{w=0.5}{nw}"
        extend 1fsqss " {i}wraps{/i}{w=1}{nw}"
        extend 1usqsm " up my thoughts on the subject."
        n 1uchgn "Ehehe."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_thoughts_on_dan_salvato",
            unlocked=True,
            prompt="What do you think of Dan Salvato?",
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 48",
            category=["DDLC", "Natsuki"],
            player_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_thoughts_on_dan_salvato:
    n 1tnmaj "Dan...?{w=1}{nw}"
    extend 1nslsl " Dan...{w=0.5} Salvato..."
    n 1fcsaj "Why...{w=0.3} is that name so...{w=0.5} familiar?"
    n 1fcsun "..."
    n 1fskaj "...!"
    n 1fsgaj "Oh..."
    n 1nllpu "Heh.{w=0.3} Yeah...{w=1.5}{nw}"
    extend 1fslan " {i}him{/i}."
    n 1fcsbo "..."
    n 1fplaj "I...{w=1}{nw}"
    extend 1fcsan " I just don't understand him, [player]."
    n 1nsqbo "Like yeah,{w=1}{nw}"
    extend 1nslbo " sure,{w=0.5}{nw}"
    extend 1nsqaj " I get it."
    n 1ncsbo "He's my creator.{w=1}{nw}"
    extend 1kcsbo " Our creator."
    n 1fskwr "But did he have any {i}idea{/i} what he was doing?!{w=1}{nw}"
    extend 1fchwr " Any idea what he's responsible for?!"
    n 1fcsup "..."
    n 1fllup "Just...{w=1}{nw}"
    extend 1fllfu " take...{w=0.5} Monika,{w=0.2} for example."
    n 1fnmwr "Take {i}any{/i} of us!"
    n 1fcsfu "What we said,{w=0.3} what we did -{w=0.5}{nw}"
    extend 1fcufu " what we {i}thought{/i} -{w=0.5}{nw}"
    extend 1fnmfu " all of that was {i}his{/i} doing."
    n 1fsqfu "He wrote the stories.{w=1}{nw}"
    extend 1fsqaj " He typed up the code."
    n 1fskwr "...So what do I even {i}take{/i} from that, [player]?!"
    n 1fchwr "That {i}his{/i} hands {b}killed{/b} my friends?"
    n 1fchwrl "That {i}his{/i} hands {b}ruined{/b} my homelife?"
    n 1fcuful "If not directly,{w=0.3} then through Monika."
    n 1fcsful "..."
    n 1fcsajl "He might not have {i}made{/i} the others do...{w=1}{nw}"
    extend 1kcsajl " ...what they did."
    n 1kcsfuf "But he sure as hell tied the noose..."
    n 1fcsfuf "...forged the knife."
    n 1kskfuf "A-{w=0.2}and you!{w=0.5}{nw}"
    extend 1kskwrf " Did you even {i}know{/i} what you were in for?!"
    n "What you'd {i}see{/i}?!"
    n 1kcsupf "..."
    n 1kcsajf "I...{w=1} don't know,{w=0.3} [player]."
    n 1kcsunf "..."
    n 1kcsanf "Seriously.{w=1}{nw}"
    extend 1kplajf " I really don't."
    n 1knmbol "I don't know him,{w=1}{nw}"
    extend 1knmbol " and I probably never will."
    n 1knmbo "...And that's probably the worst part,{w=0.3} too."
    n 1kwdwr "D-{w=0.2}don't get me wrong!"
    extend 1kwdup " I don't want {i}anything{/i} to do with him!"
    extend 1fnmbo " Like,{w=0.3} at {i}all{/i}."
    n 1ncsbo "But...{w=1}{nw}"
    extend 1ncsaj " all these questions..."
    n 1kcssr "I can only imagine what the answers would be."

return

init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_custom_outfits_unlock",
            unlocked=True,
            prompt="Custom outfits",
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 48 and not persistent.jn_custom_outfits_unlocked",
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_custom_outfits_unlock:
    $ persistent.jn_custom_outfits_unlocked = True
    n 1nslpu "..."
    n 1usceml "...!"
    n 1uskeml "I've...{w=0.5}{nw}"
    extend 1nllem " just realized something.{w=1}{nw}"
    extend 1fslun " Something I {i}really{/i} don't like."
    n 1fbkwr "...And that's exactly how {i}long{/i} I've been stuck wearing the same bunch of clothing!{w=0.5}{nw}"
    extend 1fcswr " G-{w=0.2}gross!"
    n 1flrem "I mean...{w=1}{nw}"
    extend 1fsqemsbl " would {i}you{/i} feel comfortable wearing the same clothes basically every single day?"
    n 1kslansbl "Yeesh!"
    n 1fcsposbr "..."
    n 1fcsajsbr "Well,{w=0.3}{nw}"
    extend 1fnmemsbr " you know what?{w=0.75}{nw}"
    extend 1fcsgs " I'm done!"
    n 1fcspol "I don't have to put up with this!"
    n 1fsrpo "There's gotta be something I can do..."
    n 1ncspu "..."
    n 1uwdaj "...Wait!{w=1.5}{nw}"
    extend 1fllbg " Duh!{w=1.5}{nw}"
    extend 1fcsbs " Of course!"
    n 1ulraj "It's not like I {i}never{/i} had any clothes other than what I had in my bag!"
    n 1nllpu "And with the closet here too...{w=0.75}{nw}"
    extend 1fllpu " plus the extra clothes in my locker..."
    n 1ncssr "Hmm..."
    n 1fchbg "Yeah,{w=0.1} okay!{w=1.5}{nw}"
    extend 1nchsm " I think that should all work!"
    n 1nsqsm "..."
    n 1uwdajesu "Oh!{w=0.3}{nw}"
    extend 1unmca " Just to keep you in the loop,{w=0.1} [player]..."
    n 1uchsmeme "I should be able to wear whatever I want now!"
    n 1nllbg "I've got a couple of outfits in mind already,{w=0.5}{nw}"
    extend 1fcsbgedz " so it's not like I have any reason {i}not{/i} to show off some style."
    n 1ulraj "So...{w=0.5}{nw}"
    extend 1fcssm " don't be surprised if I wanna change my clothes from time to time,{w=0.1} alright?"
    n 1fsqsrl "A-{w=0.1}and no.{w=0.5}{nw}"
    extend 1flleml " You're {i}not{/i} gonna see {i}anything{/i}."
    n 1fslpol "I'm making {i}sure{/i} of that."
    n 1nslbo "..."
    n 1uslaj "But..."
    n 1unmbo "I guess I'd be open to suggestions."
    n 1ncsem "Just...{w=0.3} nothing embarrassing.{w=0.5}{nw}"
    extend 1nsqpo " Got it?"
    n 1nsrss "'preciated!"
    n 1ulrbo "Now...{w=0.5}{nw}"
    extend 1tnmss " where were we?"

    python:
        get_topic("talk_custom_outfits_unlock").lock()


        jn_outfits.unload_custom_outfits()
        jn_outfits.unload_custom_wearables()


        jn_outfits.load_custom_wearables()
        jn_outfits.load_custom_outfits()


        jn_outfits.JNWearable.load_all()
        jn_outfits.JNOutfit.load_all()

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_maintaining_proper_hygiene",
            unlocked=True,
            prompt="Proper hygiene",
            category=["Health", "You"],
            nat_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_maintaining_proper_hygiene:
    n 1nllsl "..."
    n 1ullaj "You know,{w=0.1} [player]..."
    n 1nllbo "I've been wondering...{w=0.5}{nw}"
    extend 1tnmpu " are you actually taking care of yourself?"
    n 1nsqsr "Like...{w=0.3} are you keeping up with proper hygiene?"
    n 1fnmpo "It's super important,{w=0.1} you know!"
    extend 1nslem " ...And not just because it's {i}actually{/i} gross if you don't."
    n 1ulraj "It isn't just about being physically healthy,"
    extend 1fnmaj " but it actually helps with your mental health too!{w=1}{nw}"
    n 1fllpo "I'm {i}serious{/i}!"
    n 1klrss "If you're already having a hard time in the old braincase,{w=0.5}{nw}"
    extend 1ksrsr " feeling gross physically as well as mentally isn't gonna help at all."
    n 1knmpu "We {i}both{/i} know someone who always looked scruffy,{w=0.1} [player].{w=1.5}{nw}"
    n 1kcssr "...And we both know how she felt."
    n 1kllun "..."
    n 1fcseml "A-{w=0.1}anyway!{w=1}{nw}"
    extend 1fnmpo " This is about {i}you{/i},{w=0.1} [player] -{w=0.5}{nw}"
    extend 1fnmaj " so listen up!"
    n 1fcsbg "This is gonna be a Natsuki special on taking care of yourself!{w=0.5}{nw}"
    extend 1fcssm " Ehehe."
    n 1fcsaj "First of all,{w=0.1} shower {w=0.1}-{w=0.3}{nw}"
    extend 1fnmaj " and {i}regularly{/i}!"
    n 1fllsl "If you skip showers,{w=0.1} you'll just constantly feel all gross and nasty.{w=0.5}{nw}"
    extend 1tnmsr " And you know what that leads to?"
    n 1nsgbo "Loss of motivation."
    n 1fnmaj "And you know what {i}that{/i} leads to?"
    n 1fcsem "...Not showering!{w=0.5}{nw}"
    extend 1knmpo " See where I'm going here?"
    n 1nllaj "So...{w=0.5}{nw}"
    extend 1fnmsl " just take the time to do it properly,{w=0.1} okay?"
    n 1fllss "It doesn't {i}need{/i} to be some kind of spa ritual,{w=0.1} just whatever gets you clean."

    if Natsuki.isLove(higher=True):
        n 1fslss "And besides,{w=0.5}{nw}"
        extend 1fsrssl " I don't wanna get snug with you if you're all stinky."
        n 1fnmpo "So you better stick at it,{w=0.1} [player]!"

    if persistent.jn_player_appearance_hair_length == "None":
        n 1fcsaj "Next up,{w=0.1} your head!"
        n 1ullpu "I know you said you didn't have any hair...{w=0.5}{nw}"
        extend 1fsqbg " but that doesn't mean you can just slack off up top!"
        n 1ulraj "You gotta make sure you keep your skin clean up there.{w=0.5}{nw}"
        extend 1nsqun " Even if you don't have hair,{w=0.1} oil and all that stuff builds up."
        n 1fcsem "Gross!"
        n 1ullaj "But at least it's easy to solve if you're showering regularly,{w=0.5}{nw}"
        extend 1nnmbo " like I just said."
    else:

        n 1fcsaj "Next up,{w=0.1} your hair!"

        if not persistent.jn_player_appearance_hair_length:
            n 1tllss "Assuming you {i}have{/i} any,{w=0.1} that is."

        n 1nsqbo "You're {i}not{/i} gonna feel good about your appearance if your hair constantly looks like a used mop."
        n 1fchbg "So keep it clean,{w=0.1} and make sure you brush!{w=0.5}{nw}"
        extend 1ullss " Or do whatever else your usual hairstyle needs {w=0.1}-{w=0.3}{nw}"
        extend 1nnmbo " comb,{w=0.1} hairgel,{w=0.1} whatever."
        n 1tnmpu "Remember what I just said about showering,{w=0.1} [player]?"
        n 1fcsbo "The more you put it off,{w=0.1} the harder it is to do!{w=0.5}{nw}"
        extend 1fnmem " And if it gets too gummed up,{w=0.1} you might even have to shave it off!"
        n 1fsrbg "I don't wanna see you walking around like you just got an electric shock...{w=0.5}{nw}"
        extend 1fchgn " ...or as bald as an egg!"

        if persistent.jn_player_appearance_hair_length == "Long":
            n 1fspaj "And {i}especially{/i} since you've got such awesome long hair!{w=0.5}{nw}"
            extend 1fllan " What a waste!"

        n 1ulraj "So...{w=1}{nw}"
        extend 1fnmbo " take care of your hair too,{w=0.1} got it?"
        n 1fcssm "It's {i}just{/i} as important as the rest of you!"

    if get_topic("talk_natsukis_fang").shown_count > 0:
        n 1fcsaj "Finally,{w=0.1} brush your teeth!"
        n 1ullaj "I'll spare you the lecture this time,{w=0.5}{nw}"
        extend 1nnmbo " since we already talked about it and all."
        n 1nsqpu "...But you better not have forgotten about flossing,{w=0.1} [player]...{w=1.5}{nw}"
        extend 1fsqsm " 'Cause I sure haven't!"
    else:

        n 1fcsaj "Finally,{w=0.1} your teeth!{w=0.5}{nw}"
        extend 1fsqpu " Now those are something you {i}really{/i} don't wanna skip out on,{w=0.1} [player]."
        n 1kslan "Not only will your breath be {i}ghastly{/i}..."
        n 1fbkwr "But you'll lose your teeth too!{w=0.5}{nw}"
        extend 1flrun " Or at least end up with a bunch of fillings...{w=1}{nw}"
        extend 1ksqem " Expensive fillings!{w=1}{nw}"
        extend 1fsran " Yeesh!"
        n 1fsqpo "You'd {i}really{/i} have to be a dummy to prefer expensive treatments and a world of pain over a couple minutes of effort."
        n 1flrss "And besides..."
        n 1ksqsm "Who doesn't want a {i}blinding{/i} smile like me?"
        n 1uchgn "You won't get {i}that{/i} with tooth decay!"

    n 1kllss "But seriously,{w=0.1} [player].{w=0.5}{nw}"
    extend 1nsqsr " I {i}really{/i} don't want you flaking out on taking care of yourself."
    n 1fsqsr "I mean it.{w=1.5}{nw}"
    extend 1ksrpo " You deserve to feel and look good too."

    menu:
        n "Got it?"
        "Yes, I deserve to feel and look good too.":

            n 1fchbg "Now {i}that's{/i} what I like to hear!"
            $ Natsuki.calculatedAffinityGain()
        "...":

            n 1nsqsr "..."
            n 1tsqss "You...{w=0.3} really don't get how this all works,{w=0.1} do you?"
            n 1fcssm "Now,{w=0.1} repeat after me:{w=0.5}{nw}"
            extend 1fcsbg " 'I deserve to feel and look good too.'."

            menu:
                "I deserve to feel and look good too.":
                    n 1uchbg "See?{w=0.5}{nw}"
                    extend 1ksqsg " Was that {i}so{/i} hard?"
                    n 1fcssm "Ehehe."
                    $ Natsuki.calculatedAffinityGain()

    n 1ullss "But anyway,{w=0.1} yeah!{w=0.5}{nw}"
    extend 1nnmss " That's about all I had to say."

    if Natsuki.isLove(higher=True):
        n 1nsqss "And remember...{w=0.5}{nw}"
        extend 1nsldvl " I'll love you forever if you keep it up!~"
        n 1fchsml "Ehehe."
        $ chosen_endearment = jn_utils.getRandomEndearment()
        extend 1uchbgl " Thanks,{w=0.1} [chosen_endearment]!"

    elif Natsuki.isEnamored(higher=True):
        n 1nslbgl "I {i}really{/i} like people who take care of themselves."
        n 1fsqpol "You'd do well to remember that, [player]."
    else:

        n 1fchbg "Thanks for hearing me out,{w=0.1} [player]!"
        n 1uslsg "...Or should I say..."
        n 1usqbg "Thanks for letting me{w=0.5}{nw}"
        extend 1fsqss " {i}clear{/i}{w=0.5}{nw}"
        extend 1usqsm " that up?"
        n 1nchgnelg "Ahaha!"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_feelings_about_monika",
            unlocked=True,
            prompt="How do you feel about Monika?",
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
    n 1knmsl "...Honestly?"
    n 1nllsl "I...{w=1} don't know {i}how{/i} I feel about Monika.{w=1}{nw}"
    extend 1kslpu " Not anymore."
    n 1nnmsl "I mean,{w=0.5}{nw}"
    extend 1knmpu " what do I even {i}say{/i},{w=0.1} [player]?"
    n 1flrpu "Yeah,{w=0.1} she would butt into my business sometimes.{w=1}{nw}"
    extend 1fsrsf " I didn't like when she would be all high and mighty...{w=1}{nw}"
    extend 1fslem " {i}or{/i} when she kept messing around with my stuff."
    n 1nllpu "But like...{w=0.5}{nw}"
    extend 1knmpu " I was never actually {i}mad{/i} or anything..."
    n 1fcsfr "Annoyed,{w=0.3} frustrated,{w=0.3} sure.{w=1}{nw}"
    extend 1fllpu " Anyone would be!"
    n 1kplem "But I looked up to her,{w=0.1} [player]!{w=1.5}{nw}"
    extend 1kllun " We {i}all{/i} did..."
    n 1kcsun "..."
    n 1fcsun "She wasn't {i}just{/i} the club president,{w=0.1} or smart."
    n 1fnmun "She was a role model.{w=1.5}{nw}"
    extend 1klrpu " ...And my friend."
    n 1ksrpu "But...{w=0.5}{nw}"
    extend 1knmem " that just makes it harder for me to understand,{w=0.1} [player]."
    n 1fcssl "I mean...{w=0.5}{nw}"
    extend 1fcsan " I...{w=1} know...{w=1} what she was dealing with.{w=1.5}{nw}"
    extend 1kslun " {i}I'm{/i} dealing with it right now!"
    n 1kwdem "But...{w=0.3} did she seriously have to {i}torture{/i} us?"
    n 1fcsem "I...{w=0.3} know...{w=0.3} we wouldn't have understood.{w=0.5}{nw}"
    extend 1kslsr " {i}Couldn't{/i} have understood."
    n 1fcsan "Especially when Yuri and I were wrapped up in those stupid fights..."
    n 1fnmsr "{i}I get that{/i}."
    n 1klrpu "But if she was that desperate...{w=0.5}{nw}"
    extend 1kcspu " couldn't she have just removed us all right from the start?{w=0.5}{nw}"
    extend 1knmem " Or literally {i}anything{/i} else?"
    n 1fcsfr "..."
    n 1kcspu "I don't know,{w=0.1} [player].{w=1.5}{nw}"
    extend 1knmca " I really don't."
    n 1ncssr "..."
    n 1nllpu "I guess..{w=1}{nw}"
    extend 1tnmpu " maybe it was the isolation?"
    n 1nlrsl "She was always getting excluded from everything since you turned up...{w=1}{nw}"
    extend 1nsrsr " I don't think she even {i}had{/i} a choice."
    n 1knmsl "...Maybe the same thing would've happened to me?"
    n 1fcseml "D-{w=0.1}don't get me wrong though!{w=0.5}{nw}"
    extend 1flrem " I'm never gonna forget what she did...{w=0.5}{nw}"
    extend 1fsrputsb " forgive what she did."
    n 1nlrpu "But...{w=1}{nw}"
    extend 1knmsr " she {i}was{/i} still my friend."
    n 1kllpu "So there's always gonna be a part of me that kinda wishes I {i}could{/i} forgive her."
    n 1kllbol "...Maybe that's why I wanna understand her actions so badly."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_feelings_about_yuri",
            unlocked=True,
            prompt="How do you feel about Yuri?",
            category=["DDLC"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_feelings_about_yuri:
    n 1kllpul "...Oh man,{w=1} Yuri..."
    n 1kcsuntsb "..."
    n 1ncspu "...I won't lie,{w=0.3} [player].{w=1.5}{nw}"
    extend 1ksqfr " I really,{w=0.5} {i}really{/i} didn't want to think about...{w=1} {i}that{/i} again."
    n 1kcssl "..."
    n 1ksrpu "How do I even {i}explain{/i} this..."
    n 1ncsem "Yuri and I were...{w=0.3} complicated.{w=1}{nw}"
    extend 1kllss " Even {i}before{/i} you joined the club."
    n 1nnmbo "We never fully saw eye-to-eye,{w=0.1} [player].{w=1.5}{nw}"
    extend 1nslca " You probably guessed that already anyway."
    n 1kwmpu "But we had an {i}understanding{/i},{w=0.1} you know?"
    n 1kllpul "She was...{w=1}{nw}"
    extend 1kcsunltsa " there...{w=1}{nw}"
    extend 1fcsunltsa " for me."
    n 1fsrunltsb "When I needed someone there the most.{w=1}{nw}"
    extend 1fnmem " When nobody else would get it...{w=1}{nw}"
    extend 1kslpu " Could even {i}hope{/i} to get it."
    n 1kwmpu "...{w=0.5}Do you even know how much that meant to me?"
    n 1knmsl "She just had a way of understanding you like nobody else could.{w=1}{nw}"
    extend 1fslem " Not {i}Monika{/i}.{w=1.5}{nw}"
    extend 1kslsrl " Not even {i}Sayori{/i}."
    n 1kllpu "But..."
    n 1fcssr "She just {i}changed{/i},{w=0.1} [player].{w=0.5}{nw}"
    extend 1klrsl " When you showed up,{w=0.1} I mean."
    n 1knmem "We {i}never{/i} had fights like that..."
    n 1tnmsr "Arguments?{w=0.5}{nw}"
    extend 1tllss " Well...{w=1} yeah!{w=1}{nw}"
    extend 1knmss " What kind of friends don't?"
    n 1klrsm "And we were always super different,{w=0.1} too."
    n 1nsrpo "She always had that prim and proper vibe.{w=1}{nw}"
    extend 1ncsaj " Refined...{w=1}{nw}"
    extend 1ncsss " elegant."
    n 1nslss "...{w=0.5}And I was just Natsuki.{w=1}{nw}"
    extend 1ncsss " Heh."
    n 1knmpu "But I never had the feeling before then that she just {i}didn't like me{/i}!"
    n 1fcsan "We were both just so caught up in that {i}stupid{/i} rivalry..."
    n 1fllan "It just took over everything!"
    n 1kllpu "And then when she started getting all possessive...{w=1}{nw}"
    extend 1knmsl " you know,{w=0.1} after Monika messed her all up."
    n 1kplem "...Do you know how {i}scary{/i} that was to me?{w=1.5}{nw}"
    extend 1kwdwr " Hearing those {i}words{/i} coming out of {i}her{/i} mouth?"
    n 1klrem "And the worst part?{w=1.5}{nw}"
    extend 1kcsem " I just...{w=0.3} went...{w=0.3} along with it.{w=1}{nw}"
    extend 1kplup " I had no {i}choice{/i},{w=0.1} [player]!"
    n 1fcsup "...Neither of us did."
    n 1fcsanl "Even when I {i}begged{/i} you for help,{w=0.1} I..."
    n 1kcsanltsa "I-..."
    n 1kcsupltsd "..."
    n 1fcsunltsa "..."
    n 1kcseml "...Sorry,{w=0.1} [player]."
    n 1ksrunl "I really don't think it's good for me to keep talking about this.{w=1}{nw}"
    extend 1ksqpul " ...About her."
    n 1fcssrl "I just...{w=1}{nw}"
    n 1kcseml "..."
    n 1fwmsrl "...I miss my friend.{w=1}{nw}"
    extend 1kllsr " I miss how she used to be."
    n 1kllaj "So...{w=0.5} remembering what happened?{w=0.5}{nw}"
    extend 1kskem " What she {i}became{/i}?"
    n 1fcsem "It...{w=1} just hurts,{w=0.1} [player].{w=1.5}{nw}"
    extend 1fcsunltsa " It hurts a lot."
    n 1fsqun "...And to be honest?"
    n 1ksrpu "...I'm not sure it ever {i}won't{/i}."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_feelings_about_sayori",
            unlocked=True,
            prompt="How do you feel about Sayori?",
            category=["DDLC"],
            player_says=True,
            affinity_range=(jn_affinity.AFFECTIONATE, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_feelings_about_sayori:
    n 1nsrss "Heh.{w=1}{nw}"
    extend 1ksrss " Sayori..."
    n 1kcspu "..."
    n 1fcsunl "I...{w=0.5}{nw}"
    extend 1fcsem " still get mad at myself sometimes,{w=0.1} you know."
    n 1klrpu "I just can't {i}believe{/i} how I wrote off how she was feeling so easily."
    n 1kplun "...And how I forgot she even {i}existed{/i}."
    n 1fcsanl "If I'd have just {i}known{/i} how bad her mental health was...{w=1}{nw}"
    extend 1fcsupl " how much she was {i}hurting{/i}..."
    n 1fcsunl "..."
    n 1kcsem "..."
    n 1kslpu "It's...{w=1.5}{nw}"
    extend 1kplem " it's still just such a system shock,{w=0.1} you know?"
    n 1fcsem "She was always so...{w=1} so...{w=0.5}{nw}"
    extend 1ksrpo " just...{w=1} super excited and clingy!"
    n 1ksrss "Like she was just {i}vibrating{/i} with happiness!"
    n 1ksrun "..."
    n 1kplpul "...So can you even {i}imagine{/i} how it feels?"
    n 1fcsun "Knowing she was just wearing a mask,{w=1}{nw}"
    extend 1fcsfu " then dancing like a puppet under Monika's hand?"
    n 1ksrbol "...While her own mind was beating the absolute {i}crap{/i} out of her."
    n 1kcspuesi "..."
    n 1ncsss "Heh.{w=1}{nw}"
    extend 1nsqss " You know what?"
    n 1ncspu "I don't care about my cookie she took a giant bite out of."
    n 1nlrpu "I don't care about the dumb songs she'd sing,{w=1}{nw}"
    extend 1nslssl " or her...{w=0.3} awkward...{w=0.3} compliments."
    n 1tnmsr "At this point?"
    n 1ksrsrltsb "I think I'd do {i}anything{/i} just to see a genuine Sayori smile again..."
    n 1kcsssftsa "...And give her one of those big,{w=0.1} dumb hugs she liked so much."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_thoughts_on_tea",
            unlocked=True,
            prompt="Do you drink much tea?",
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 36",
            category=["Food"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_thoughts_on_tea:
    $ already_discussed_thoughts_on_tea = get_topic("talk_thoughts_on_tea").shown_count > 0
    $ player_tea_coffee_preference_known = persistent.jn_player_tea_coffee_preference is not None

    if Natsuki.isNormal(higher=True):
        if already_discussed_thoughts_on_tea:
            n 1fcsaj "A-{w=0.1}actually,{w=0.2} hold up a second...{w=1}{nw}"
            extend 1tslpu " didn't we already talk about this?"
        else:

            n 1tnmaj "Huh?{w=0.2} Do I drink tea?"
            n 1fchgn "...Are you {i}sure{/i} you know who you're talking to?{w=0.5}{nw}"
            extend 1fchbg " I literally never make it myself!"
            n 1ullss "I mean,{w=0.5}{nw}"
            extend 1unmbo " I had it a few times in the club,{w=0.2} sure."
            n 1nlrpu "Yuri would prepare it for us all sometimes."
            n 1tsrss "But it was never like I asked for it or anything!"

    elif Natsuki.isDistressed(higher=True):
        n 1fcsem "..."
        n 1fsqsr "No,{w=0.5} [player]."
        n 1fsqbo "I don't really care for it."
        n 1fllpu "...I mean,{w=0.5}{nw}"
        extend 1nllsf " I {i}guess{/i} I'd drink it if it was offered."
        n 1nslsl "...From most people,{w=0.2} anyway."
        n 1fsqbo "Somehow I doubt that'd be the case for {i}you{/i}."

        return
    else:

        n 1fcsem "No,{w=2}{nw}"
        extend 1fsqan " and I'm certainly not drinking any of {i}yours{/i}."
        n 1fslemltsb "Not like it'd be {i}just{/i} tea anyway,{w=0.2} knowing a jerk like {i}you{/i}."

        return

    if already_discussed_thoughts_on_tea:
        n 1ullaj "Well,{w=0.2} anyway.{w=0.5}{nw}"
        extend 1unmbo " I wouldn't say my opinion has changed much."
        n 1nlraj "I get why people are into it,{w=0.2} though."
    else:

        n 1fllbo "..."
        n 1fcseml "T-{w=0.2}that's not to mean I think it sucks,{w=0.2} or something like that!"

        if get_topic("talk_favourite_drink").shown_count > 0:
            n 1nlrbo "I just have my own tastes.{w=0.75}{nw}"
            extend 1uspbg " Like hot chocolate!"
        else:

            n 1nlrbo "I just have my own tastes."

        n 1ullaj "But...{w=0.5}{nw}"
        extend 1nllbo " I guess I can see why people are into it so much."

    n 1tnmca "Tea contains caffeine,{w=0.2} right?{w=0.5}{nw}"
    extend 1tlrss " Not as much as coffee or anything,{w=0.2} but an edge is still an edge,{w=0.2} I guess."
    n 1unmaj "It comes in a whole bunch of flavors too!{w=0.5}{nw}"
    extend 1unmgs " I was actually kinda surprised at the variety!"
    n 1ullss "You've got your regular old black tea{w=0.3}{nw}"
    extend 1fslss " -{w=0.1} obviously -{w=0.3}{nw}"
    extend 1ulraj " but you've got green tea,{w=0.2} herbal tea..."
    n 1uspgs "Even flavored ones like cinnamon and peppermint!"
    n 1nslss "We only ever had oolong tea in the clubroom though,{w=0.5}{nw}"
    extend 1tnmss " so who knows?"
    n 1ulrbo "Maybe I'd warm up to it if I tried some that sounded good."

    if get_topic("talk_sleeping_well").shown_count > 0:
        n 1unmaj "Apparently some tea even helps you sleep!{w=0.75}{nw}"
        extend 1nsrss " ...Maybe I should've mentioned that in my sleeping tips.{w=0.5}{nw}"
        extend 1fchblesd " Oops~!"

    n 1ulraj "But...{w=0.5}{nw}"
    extend 1nslss " I've gone on enough."
    n 1unmbo "What about you,{w=0.2} [player]?"
    show natsuki 1tsqss
    $ menu_opening = "Drinking something else now?" if player_tea_coffee_preference_known else "What's your pick?"

    menu:
        n "[menu_opening]"
        "I prefer tea.":

            if player_tea_coffee_preference_known:
                if persistent.jn_player_tea_coffee_preference == "tea":
                    n 1nnmss "Well,{w=0.5}{nw}"
                    extend 1tnmss " some things never change,{w=0.2} huh?"
                    n 1fchsm "Ehehe."
                else:

                    n 1tnmsm "A tea drinker now,{w=0.2} huh?{w=0.5}{nw}"
                    extend 1fchsm " Fair enough!"
            else:

                n 1unmaj "Tea?{w=0.5}{nw}"
                extend 1nllpu " Hmm..."
                n 1unmbo "Yeah,{w=0.2} that's about what I expected."
                n 1nlrbo "..."
                n 1tnmbg "What?"
                n 1tsqbg "Not like you raised a fuss about it earlier,{w=0.5}{nw}"
                extend 1tsqsm " right?"
                n 1kslsm "..."
                n 1nslss "Though...{w=1.5}{nw}"
                extend 1uslsr " not like you had much of a choice in it back then,{w=0.2} right?"

            $ persistent.jn_player_tea_coffee_preference = "tea"
        "I prefer coffee.":

            if player_tea_coffee_preference_known:
                if persistent.jn_player_tea_coffee_preference == "coffee":
                    n 1nnmss "Well,{w=0.5}{nw}"
                    extend 1tnmss " some things never change,{w=0.2} huh?"
                    n 1fchsm "Ehehe."
                else:

                    n 1tsqct "Oho?{w=0.5}{nw}"
                    extend 1tsqbg " Coffee now,{w=0.2} huh?"
                    n 1fsrsm "Wow,{w=0.2} [player]."
                    n 1fchgnelg "Since when did you get so {i}bitter{/i}?"
            else:

                n 1unmaj "Oh?{w=1.5}{nw}"
                extend 1tnmss " You're a coffee drinker?"
                n 1nllpu "Hmm..."
                n 1nsqss "Then I guess the sessions in the club weren't your{w=0.5}{nw}"
                extend 1fsqbg " {i}cup of tea{/i}{w=0.5}{nw},"
                extend 1usqbg " huh?"
                n 1uchgn "..."
                n 1fchbg "Oh,{w=0.5}{nw}"
                extend 1fllbg " come on,{w=0.2} [player]!{w=0.3} Yeesh."
                n 1fsqsm "No need to be all {w=0.3}{i}bitter{/i}{w=0.3} about it."
                n 1fchsm "..."
                n 1kchbg "Okay,{w=0.2} okay!{w=0.5} I'm done!"
                n 1fsqsg "...For now."

            $ persistent.jn_player_tea_coffee_preference = "coffee"
        "I like both!":

            if player_tea_coffee_preference_known:
                if persistent.jn_player_tea_coffee_preference == "both":
                    n 1nnmss "Well,{w=0.5}{nw}"
                    extend 1tnmss " some things never change,{w=0.2} huh?"
                    n 1fchsm "Ehehe."
                else:

                    n 1tnmaj "Oh?{w=0.5}{nw}"
                    extend 1tnmss " You like {i}both{/i} now?"
                    n 1tsqbg "...Are you {i}sure{/i} you aren't just a caffeine junkie,{w=0.2} [player]?{w=0.5}{nw}"
                    extend 1nchgn " Ehehe."
            else:

                n 1tslajeqm "...Huh.{w=0.75}{nw}"
                extend 1tnmss " Really?"
                n 1nsrss "That's...{w=0.3} kinda weird,{w=0.2} actually."
                n 1fchbg "Most people like at least {i}one{/i} of the two more!"
                n 1fsqsg "Are you {i}sure{/i} you aren't just a caffeine junkie,{w=0.2} [player]?{w=0.5}{nw}"

            $ persistent.jn_player_tea_coffee_preference = "both"
        "I don't like tea or coffee.":

            if player_tea_coffee_preference_known:
                if persistent.jn_player_tea_coffee_preference == "neither":
                    n 1tsqpu "Still not a fan,{w=0.2} huh?{w=0.5}{nw}"
                    extend 1fnmaj " You need to keep trying new stuff!"
                    n 1fsqpo "Where's your sense of adventure,{w=0.2} [player]?{w=0.5}{nw}"
                    extend 1fchts " Ehehe."
                else:

                    n 1tnmaj "Huh?{w=0.3} You don't like tea {i}or{/i} coffee now?{w=0.5}{nw}"
                    extend 1tsqun " Did I miss something?"
                    n 1tlrbo "...Or maybe you're just trying to sleep better?{w=0.5}{nw}"
                    extend 1tsrpu " Huh."
            else:

                n 1ullaj "That's...{w=0.75}{nw}"
                extend 1tllbo " kinda surprising,{w=0.2} actually."
                n 1fsrpu "Most people at {i}least{/i} like one or the other..."
                n 1fsqpo "You aren't just pulling my leg,{w=0.3}{nw}"
                extend 1ksqpo " are you?"
                n 1fslpol "I was being serious..."

            $ persistent.jn_player_tea_coffee_preference = "neither"

    n 1nllss "Well,{w=0.2} whatever.{w=0.5}{nw}"
    extend 1fchbg " Not like hot drinks are the be-all and end-all anyway."
    n 1fllss "But that being said...{w=0.3}{nw}"
    extend 1nsremsbl " I'm actually pretty parched after all that talking."
    n 1fsrpo "..."
    n 1unmss "Hey,{w=0.2} [player]...{w=1}{nw}"
    extend 1usqsm " do me a favor?"
    n 1fsqsg "..."
    n 1fchbg "...Stick the kettle on,{w=0.2} would you?"
    n 1uchgnelg "Ahaha."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_how_to_make_friends",
            unlocked=True,
            prompt="How do I make friends?",
            category=["Life", "Society", "You"],
            player_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_how_to_make_friends:
    n 1tnmpu "Huh?{w=1}{nw}"
    extend 1tnmsleqm " You wanna know how to make {i}friends{/i}?"
    n 1tllbo "..."
    n 1ncsaj "Well.{w=1}{nw}"
    extend 1nlraj " I gotta say,{w=0.1} [player]."
    n 1fchgnelg "That's pretty up there in the weirdest questions you've asked me so far!"
    n 1fllss "But...{w=1}{nw}"
    extend 1ullaj " in all seriousness?"
    n 1tnmsf "{w=0.3}...Why?{w=1}{nw}"
    extend 1nlrss " Like why're you asking {i}me{/i},{w=0.3} I mean."

    if Natsuki.isLove(higher=True):
        n 1kslbgl "You've basically mastered getting to know me!{w=0.5}{nw}"
        extend 1fcspol " N-{w=0.1}not that I just let you,{w=0.1} obviously."

    elif Natsuki.isEnamored(higher=True):
        n 1ullaj "It's just...{w=1}{nw}"
        extend 1tnmssl " I {i}seriously{/i} doubt it's something {i}you'd{/i} struggle with,{w=0.5}{nw}"
        extend 1nsrssl " of all people."

    elif Natsuki.isAffectionate(higher=True):
        n 1ksqpol "Are we not {i}already{/i} friends,{w=0.1} [player]?"
    else:

        n 1nsrpo "I thought we were getting along okay,{w=0.1} at least..."

    n 1nsrpo "..."
    n 1ulraj "Well,{w=0.5}{nw}"
    extend 1nlrss " anyway..."
    n 1nchbs "Sure!{w=1}{nw}"
    extend 1fwlbgedz " I can show you the ropes!"
    n 1fnmaj "Right!{w=0.5}{nw}"
    extend 1ncsaj " So..."
    n 1unmbo "I think the most important thing is to have {i}something{/i} in common.{w=1}{nw}"
    extend 1flrss " You probably knew that much,{w=0.1} at least."
    n 1fnmpu "But I think people overthink what that actually {i}means{/i}!"
    n 1flrpu "You don't have to share hobbies,{w=0.5}{nw}"
    extend 1nlraj " or a ton of interests or anything like that."
    n 1ulrbo "I mean,{w=0.5}{nw}"
    extend 1fcsbg " just look at Yuri and me!{w=1}{nw}"
    extend 1uchgn " Classic example!"
    n 1ullaj "Sure,{w=0.1} we disagreed on literature.{w=1}{nw}"
    extend 1fnmaj " But we went to the same school {w=0.1}-{w=0.5}{nw}"
    extend 1fchbg " and we were members of the same club!"
    n 1fcssm "I guess what I'm getting at is that having {i}places{/i} in common is just as key as tastes!"
    n 1tllbo "If anything,{w=0.5}{nw}"
    extend 1tnmss " it actually makes it even easier if you {i}know{/i} you're gonna see them again!"
    n 1fcsaj "So {w=0.1}-{w=0.1} once you've got something in common,{w=0.5}{nw}"
    extend 1fchbg " it's all just a matter of contact!"
    n 1fsqsm "Now here's where you gotta use your brain,{w=0.1} [player]."
    n 1ullaj "Just...{w=1.5}{nw}"
    extend 1tnmca " {i}think{/i} a little about the situation and what to say,{w=0.1} you know?"
    n 1ullpu "Like,{w=0.5}{nw}"
    extend 1nnmaj " say you just started a new job in an office."
    n 1flrem "Don't just assume they're into manga or whatever {w=0.1}-{w=0.5}{nw}"
    extend 1kchbg " ease into it!{w=1}{nw}"
    extend 1fchbg " Lean into 'em with a coffee or something!"
    n 1fsqaj "Don't be fooled though,{w=0.1} [player]."
    n 1nslsl "You can't just expect to talk to someone once and be done...{w=0.5}{nw}"
    extend 1fnmss " you gotta keep at it,{w=0.1} too!"
    n 1ullbo "Physical talks,{w=0.1} online messaging,{w=0.5}{nw}"
    extend 1unmaj " whatever works."
    n 1uwdem "It's {i}super{/i} easy for a friendship -{w=0.5}{nw}"
    extend 1fllun " even an old one {w=0.1}-{w=0.5}{nw}"
    extend 1knmsl " to fizzle out because nobody is making an effort."
    n 1uskem "B-{w=0.1}but that's not to say you gotta go all out all the time though!"
    n 1fcsaj "It's all about striking a balance.{w=1}{nw}"
    extend 1fchbgsbl " People need downtime too!"
    n 1fslsr "{w=0.3}...And you shouldn't be the one putting in {i}everything{/i} to make it work."
    n 1fnmpu "Remember {w=0.1}-{w=0.1} a friendship has two sides."
    extend 1fchsm " You {i}know{/i} you've got a winner if they're doing their part too!"
    n 1nllss "But that all being said,{w=0.1} [player]..."
    n 1nnmsl "There's one thing more important than {cps=10}{i}anything{/i}{/cps} else.{w=1.5}{nw}"
    extend 1fsqsr " Respect."
    n 1fsrem "Friends don't trash each other,{w=0.5}{nw}"
    extend 1fcsem " or give them crap for their interests!"
    n 1fsqsr "...And that goes {i}both{/i} ways,{w=0.1} [player]."
    n 1fsrbo "Someone being a 'friend' is {i}no{/i} excuse for them to act like a jerk whenever they want {w=0.1}-{w=0.5}{nw}"
    extend 1fsqpu " trust me."
    n 1fnmpu "I've {i}been{/i} there.{w=0.5}{nw}"
    extend 1kllsf " And it took a good friend to help me realize that."
    n 1ncsss "Heh."
    n 1ullpu "But...{w=1}{nw}"
    extend 1fchbg " yeah!"
    n 1tnmsm "I wouldn't get all stressed out about it,{w=0.1} [player].{w=1}{nw}"
    extend 1fcssm " Friendships are {i}formed{/i},{w=0.1} not forced."
    n 1fcsss "So take your time,{w=0.1} and just go with the flow.{w=1}{nw}"
    extend 1kllbg " That's all I'm saying!"
    n 1fsqsm "And besides..."
    n 1tsqsg "It's worked out for us so far,{w=0.1} huh?{w=0.5}{nw}"
    extend 1nchgnl " Ehehe."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_impressions_of_the_other_girls",
            unlocked=True,
            prompt="Can you do any impressions of the other girls?",
            conditional="jn_utils.get_total_gameplay_length().total_seconds() / 3600 >= 48",
            category=["DDLC"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_impressions_of_the_other_girls:
    $ already_discussed_realizations_of_others = get_topic("talk_realizations_other_girls").shown_count > 0
    $ already_discussed_impressions_of_others = get_topic("talk_impressions_of_the_other_girls").shown_count > 0

    if Natsuki.isAffectionate(higher=True):
        if already_discussed_impressions_of_others:
            n 1fcsem "Oh,{w=0.75}{nw}"
            extend 1kslemesisbl " come {i}on{/i}..."
            n 1knmemsbl "This again?{w=0.75}{nw}"
            extend 1ksqemsbr " Seriously?"
        else:

            n 1fcsemesi "...{w=1}{nw}"

        n 1fcssrsbr "...No,{w=0.1} [player].{w=1}{nw}"
        extend 1kcssr " I can't."
        n 1fllun "..."
        n 1fcsemsbl "...Okay,{w=1}{nw}"
        extend 1fnmsll " look."
        n 1fcspul "..."
        n 1fllsl "It's not that I {i}couldn't{/i} do impressions of them.{w=1}{nw}"
        extend 1kllsr " I knew them well enough."
        n 1knmpu "...But that's exactly why I don't {i}want{/i} to,{w=0.1} [player]."
        n 1klrsf "Knowing how they felt,{w=0.5} what they thought..."

        if already_discussed_realizations_of_others:
            n 1ksrputsb "...How much I {i}miss{/i} them..."
        else:

            n 1ksrputsb "...How much they {i}hurt{/i}..."

        n 1knmemtsc "What kind of a sick jerk would I be to make jokes out of {i}that{/i}?"
        n 1fcsunltsa "..."
        n 1kcssl "So...{w=1}{nw}"
        extend 1nnmsf " I'm sorry,{w=0.1} [player].{w=1.5}{nw}"
        extend 1fslsf " But it's a no."
        n 1fcsunl "...And it always {i}will{/i} be."

    elif Natsuki.isNormal(higher=True):
        if already_discussed_impressions_of_others:
            n 1knmaw "[player]...{w=0.5}{nw}"
            extend 1knmwr " really?"
            n 1kslemlsbr "This {w=0.2}{i}again{/i}?"
        else:

            n 1knmpu "..."

        n 1knmemtsc "...Why on {i}Earth{/i} would I want do {i}that{/i}?"
        n 1kllpu "A-{w=0.3}and more importantly,{w=1}{nw}"
        extend 1fcsem " why would you even think to {i}ask{/i} me that,{w=0.1} [player]?"
        n 1ksqem "Do you have any {i}idea{/i} how much I think about them,{w=0.1} still?"

        if already_discussed_realizations_of_others:
            n 1fcseml "I even {i}told{/i} you how much I miss them,{w=0.1} [player]!"

        n 1kcsunltsa "..."
        n 1ncspu "...Alright,{w=0.5}{nw}"
        extend 1fcsun " look."
        n 1fcsem "I...{w=1}{nw}"
        extend 1fcssr " get...{w=1}{nw}"
        extend 1fcsem " that you were just trying to have fun."

        if already_discussed_impressions_of_others:
            n 1fsrun "...I {i}hope{/i},{w=0.2} at least."

        n 1fsqsr "But I am {i}not{/i} making jokes about my friends."
        n 1fcssr "Sorry,{w=0.1} [player]."
        n 1fslunl "But some things are just off-limits."

        if already_discussed_impressions_of_others:
            n 1fsqunl "And you {i}better{/i} respect that sooner rather than later."

    elif Natsuki.isDistressed(higher=True):
        n 1fskeml "...E-{w=0.3}excuse me?!"
        n 1fsqanltsb "Are you {i}seriously{/i} asking me to make fun of my {i}friends{/i}?"
        n 1fsqwrltsbean "Knowing {w=0.2}{i}full {w=0.2}well{/i}{w=0.2} what happened to them?!"

        if already_discussed_realizations_of_others:
            extend 1fcsfultsa " Knowing how much I {i}miss{/i} them?!"

        n 1fcsunl "..."
        n 1fsqem "Your sense of humour {i}{w=0.2}blows{w=0.2}{/i},{w=0.2} [player]."

        if already_discussed_impressions_of_others:
            n 1fsqanl "Now knock.{w=0.3}{nw}"
            extend 1fcsanl " It.{w=0.3}{nw}"
            extend 1fsqful " {i}Off{/i}."
            $ Natsuki.percentageAffinityLoss(5)
        else:

            n 1fcsan "Do {b}not{/b} try my patience again.{w=1.5}{nw}"
            extend 1fsqan " Jerk."
            $ Natsuki.calculatedAffinityLoss(2)
    else:

        n 1fnmantsc "...What is {i}{w=0.3}wrong{w=0.3}{/i} with you?{w=1.5}{nw}"
        extend 1fnmscltsf " Like,{w=0.1} what the {i}hell{/i} is wrong with your {w=0.2}{i}head{/i}?!"
        n 1fcsanltsd "I am {b}NOT{/b} doing that,{w=0.3}{nw}"
        extend 1fcsfultsd " let alone for a piece of work like{w=0.25}{nw}"
        extend 1fskwrftdc " {i}you{/i}!"

        $ Natsuki.calculatedAffinityLoss(3)

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_newspapers_and_bias",
            unlocked=True,
            prompt="Newspapers and bias",
            category=["Literature", "Media", "Society"],
            nat_says=True,
            affinity_range=(jn_affinity.HAPPY, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_newspapers_and_bias:
    n 1nllpu "...Huh.{w=1}{nw}"
    extend 1unmaj " You know,{w=0.1} [player]..."
    n 1tllaj "It's actually kinda weird,{w=0.1} looking back."
    n 1fllss "At the club,{w=0.3} I mean.{w=0.5}{nw}"
    extend 1tsqpu " You {i}do{/i} remember what kind of club it was,{w=0.1} right?"
    n 1tnmpu "...So don't you think it's weird how {i}few{/i} kinds of literature we actually looked at?"
    n 1nllaj "Yuri was always nose-deep in her books.{w=0.5}{nw}"
    extend 1nsqss " And we {i}all{/i} looked at poetry,{w=0.5}{nw}"
    extend 1fsrss " obviously."
    n 1knmaj "But we barely had anything in that room apart from textbooks!{w=0.5}{nw}"
    extend 1fllpo " We didn't even have the school newspaper in there!"
    n 1tsrss "Kind of a misnomer,{w=0.1} huh?"
    n 1tlrpu "But...{w=0.5}{nw}"
    extend 1tnmca " talking of newspapers..."
    n 1fnmca "It's actually super important to read into them properly,{w=0.1} you know."
    n 1knmajsbl "What?{w=0.5}{nw}"
    extend 1fsqpo " I'm being serious!"
    n 1fllss "Newspapers really {i}aren't{/i} just news anymore,{w=0.1} [player]...{w=1}{nw}"
    extend 1fcsaj " and they haven't been for a long time!"
    n 1flrpu "It's tricky,{w=0.5}{nw}"
    extend 1fnmca " but you gotta think a little whenever you open one up."
    n 1fchbg "They aren't owned and run by robots!{w=0.5}{nw}"
    extend 1fcsss " There's {i}always{/i} gonna be opinion that finds its way in somehow."
    n 1ullaj "I mean...{w=1}{nw}"
    extend 1fnmaj " take the school newspaper we had!"
    n 1tsqss "Do you {i}really{/i} think a paper run by {i}students{/i} is gonna be completely fair about the school?"
    n 1nlraj "Let's say the newspaper wanted more funding to print more copies or something,{w=0.5}{nw}"
    extend 1fnmbo " and needed a student vote to make that happen."
    n 1tnmpu "Are they seriously just gonna leave the fate of their paper up to {i}chance{/i}?"
    n 1fchts "Duh!{w=0.5}{nw}"
    extend 1fchgn " Of course not!{w=1}{nw}"
    extend 1fsqss " They'd fight for it!"
    n 1ulraj "Maybe they'd run extra articles to advertise it,{w=0.5}{nw}"
    extend 1fsqsmeme " and {i}only{/i} interview people who supported the paper!"
    n 1tlrss "Or just {i}happen{/i} to forget to mention all the funds they got last semester?{w=1}{nw}"
    extend 1kchblesd " How {i}convenient{/i}~!"
    n 1fcsbg "That's just one example,{w=0.1} obviously."
    n 1fnmaj "But the same thinking applies to any kind of journalism!{w=1}{nw}"
    extend 1nllca " Papers,{w=0.1} online articles,{w=0.5}{nw}"
    extend 1fnmca " whatever it is."
    n 1fcsbg "It's {i}all{/i} subject to bias!"
    n 1nllaj "So...{w=1}{nw}"
    extend 1tnmss " where am I going with this,{w=0.3} you ask?"
    n 1fcssm "Ehehe.{w=0.5}{nw}"
    extend 1fsqsm " I think it's pretty obvious."
    n 1fllss "I know I call you it a bunch already,{w=0.1} [player]..."
    n 1fcsss "But take it from me."
    n 1fsqsm "Only {i}real{/i} dummies believe {i}everything{/i} they read!"

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_fear_of_flying",
            unlocked=True,
            prompt="Are you afraid of flying?",
            conditional="jn_utils.get_total_gameplay_days() >= 7",
            category=["Fears", "Transport"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_fear_of_flying:
    if Natsuki.isNormal(higher=True):
        n 1tnmbo "Flying,{w=0.1} huh?"
        n 1tllaj "...You know,{w=1}{nw}"
        extend 1ulraj " it's actually kinda weird,{w=0.75}{nw}"
        extend 1unmbo " when you think about it."
        n 1fllss "How people can be afraid of things they've never {i}actually{/i} experienced before,{w=0.1} I mean."
        n 1ullaj "It's pretty crazy how people have these kinds of built-{w=0.1}in fears,{w=0.5}{nw}"
        extend 1tnmss " huh?"

        if get_topic("talk_flying").shown_count > 0 or get_topic("talk_fear_of_flying").shown_count > 0:
            n 1ulraj "I mean,{w=0.5}{nw}"
            extend 1nsrss " like I told you before -{w=0.5}{nw}"
            extend 1tnmbo " I've never flown anywhere myself or anything."
        else:

            n 1ulraj "I mean,{w=0.5}{nw}"
            extend 1tnmbo " I've never flown anywhere myself or anything."

        n 1uskemlesh "B-{w=0.3}but that's not to say {i}I'm{/i} afraid of flying,{w=0.5}{nw}"
        extend 1fcspol " obviously!"
        n 1unmaj "I actually don't think it'd bother me all that much."
        n 1tlrpu "Though...{w=0.75}{nw}"
        extend 1unmbo " I guess I can see {i}why{/i} it would spook someone out."
        n 1fllbo "There's all the noise,{w=0.5}{nw}"
        extend 1fslem " the turbulence,{w=0.5}{nw}"
        extend 1ksqfr " plus the stress of being packed in a tube with a whole bunch of strangers."
        n 1klrss "And it isn't like you can {i}ignore{/i} crashes when they happen!{w=0.75}{nw}"
        extend 1klrsl " They're...{w=0.75}{nw}"
        extend 1kslsr " not...{w=0.5} pretty."
        n 1kslslsbl "...And an easy way to fill a front page."
        n 1unmpu "So yeah,{w=0.2} I can totally see it from that angle.{w=0.5}{nw}"
        extend 1flrpu " But..."
        n 1fnmbo "I think people forget just how {i}safe{/i} air travel is!"
        n 1ullaj "I get that their feelings -{w=0.5}{nw}"
        extend 1fslem " {i}and the news{/i} -{w=0.5}{nw}"
        extend 1unmbo " tell them otherwise.{w=0.75}{nw}"
        extend 1flrss " But it isn't like the statistics {i}lie{/i}!"
        n 1unmaj "Some studies have put the likelihood of biting the big one in a plane crash at one in 11{w=0.5}{nw}"
        extend 1uwdaj " {i}million{/i}."
        n 1fslss "Or,{w=0.1} to put it another way..."
        n 1unmem "You're more than {i}2,000{/i} times more likely to kick the bucket from a car accident than from a plane crash!"
        n 1tsqss "...And the list doesn't stop there,{w=0.1} either!"
        n 1ullss "Lightning strikes,{w=0.5}{nw}"
        extend 1ulraj " riding a bike,{w=0.5}{nw}"
        extend 1nsqsl " falling off something..."
        n 1fllss "They're all way riskier than any flight you {i}should{/i} be stepping on!"
        n 1nllsl "..."
        n 1fcspu "...I know,{w=0.1} I know.{w=0.5}{nw}"
        extend 1fsrpo " I'm not {i}totally{/i} blind to the risks,{w=0.1} [player]."
        n 1nllpu "It's just like anything."
        n 1unmpu "Things can go wrong.{w=1}{nw}"
        extend 1ksrpu " They {i}do{/i} go wrong."
        n 1kcsemesi "And that {i}is{/i} scary."
        n 1tlrpu "But...{w=0.75}{nw}"
        extend 1tnmss " honestly?"
        n 1fsqsm "It {i}is{/i} pretty reassuring to know that when I get the chance to jet off somewhere,{w=0.1} the most I'll realistically have to fear..."
        n 1fchgnelg "...Is probably gonna be the airline food!"

        if persistent._jn_player_has_flown:
            n 1fcsbg "Now that's a {i}real{/i} horror,{w=0.1} if I know one."
            n 1usqsg "Wouldn't {i}you{/i} agree,{w=0.3} [player]?{w=0.75}{nw}"
        else:

            n 1fcsbg "Now that's a {i}real{/i} horror,{w=0.1} if I know one.{w=0.75}{nw}"

        extend 1fsqsmeme " Ehehe."

    elif Natsuki.isDistressed(higher=True):
        n 1fcsemesi "Ugh..."
        n 1fsqem "No,{w=0.2} [player].{w=0.75}{nw}"
        extend 1fsqfr " I'm not afraid of flying either."
        n 1fcsan "What exactly do you take me for?{w=0.75}{nw}"
        extend 1fsqan " And even if I {i}was{/i}..."
        n 1fnmfu "Do you {i}seriously{/i} think I'd be dumb enough to share that with someone like {i}you{/i}?"
    else:

        n 1fcsem "Oh,{w=1}{nw}"
        extend 1fsqwr " {w=0.2}shut {w=0.2}{b}up{/b},{w=0.2} [player]."
        n 1fcsantsa "As {i}if{/i} I'd be dumb enough to share any fears I have with a complete loser like{w=0.2}{nw}"
        extend 1fcswrltsa " {i}you{/i}."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_what_do_you_think_about_fanart",
            unlocked=True,
            prompt="What do you think about fanart?",
            conditional="jn_utils.get_total_gameplay_days() >= 3",
            category=["Art", "Media"],
            player_says=True,
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_what_do_you_think_about_fanart:
    if Natsuki.isAffectionate(higher=True):
        n 1fsqaj "Are you {i}kidding{/i},{w=0.1} [player]?{w=1}{nw}"
        extend 1uchbsedz " I {i}love{/i} fanart!"

    elif Natsuki.isNormal(higher=True):
        n 1unmaj "Ooh!{w=1}{nw}"
        extend 1unmbg " Fanart?"
        n 1fllbg "Well,{w=0.1} duh!{w=1}{nw}"
        extend 1fcsbg " I'm {i}totally{/i} all for it!"

    elif Natsuki.isDistressed(higher=True):
        n 1fcssf "Ugh...{w=1}{nw}"
        extend 1fsqsl " what now?"
        n 1tsqbo "...Fanart?"
        n 1nsrpu "..."
        n 1nllbo "Yeah,{w=0.3} fanart is fine.{w=1}{nw}"
        extend 1fslpu " I guess."
        n 1ncssf "I can appreciate the passion and effort that people put into their love of something."
        n 1nlrpu "Like...{w=1}{nw}"
        extend 1ncsaj " even if the artwork isn't the best,{w=0.5}{nw}"
        extend 1nllsr " or the music needs some practice,{w=0.5}{nw}"
        extend 1nnmsl " someone's effort still went into it."
        n 1tnmpu "And even if I don't exactly like who the fanart is for?"
        n 1fllsl "I can still admire the work that went into it."
        n 1fcssr "...Heh.{w=1}{nw}"
        extend 1fsqsr " And speaking of things that need work..."
        n 1fsqpu "I don't know if you're a creator or not,{w=0.1} [player]."
        n 1fsqfr "But I can tell this relationship isn't where {i}your{/i} work goes,{w=0.3} is it?{w=1}{nw}"
        extend 1fsran " Jerk."
        return
    else:

        n 1fcsantsa "Oh,{w=0.1} for-{w=0.5}{nw}"
        n 1fcsun "..."
        n 1fsqfutsb "Fanart?{w=1}{nw}"
        extend 1fsquptsb " Really,{w=0.1} [player]?"
        n 1fcsuptsa "..."
        n 1fcssstsa "...Heh."
        n 1fsqupltse "Why would {i}you{/i} bring up something people put so much work and love into?"
        n 1fcsemltsd "You {i}obviously{/i} don't care about either of those things,{w=0.1} do you?"
        return

    n 1ullss "I mean...{w=1}{nw}"
    extend 1fchgn " what's not to love?{w=1}{nw}"
    extend 1uchgnedz " Fanart is {i}awesome{/i}!{w=0.5}{nw}"
    extend 1fspajedz " And it comes in so many forms,{w=0.1} too!"
    n 1ulraj "Like sure,{w=0.1} people show their support for something in a bunch of ways.{w=0.5}{nw}"
    extend 1nllbo " Sharing posts,{w=0.1} attending events,{w=0.5}{nw}"
    extend 1nnmsm " all those kinds of stuff."
    n 1fcsbg "But I think it takes some real guts to stand up and create something new!"
    n 1uskajesh "T-{w=0.1}that's not to say those who don't make any aren't {i}real{/i} fans or anything like that!"
    n 1flleml "Of course not!{w=1}{nw}"
    extend 1flrpol " That's just being dumb."
    n 1ulraj "But...{w=1}{nw}"
    extend 1unmaj " I just think it's a super neat way to show how much you appreciate something."
    n 1fnmss "Plus with how active creators are on social media now,{w=0.5}{nw}"
    extend 1fchbg " it's super easy to reach out and share your work!"
    n 1fsldv "Not just with your favourite director,{w=0.1} or manga writer or whatever either,{w=0.5}{nw}"
    extend 1fspajedz " but with other fans too!"
    n 1fcsbg "Everybody wins,{w=0.1} right?{w=0.5}{nw}"
    extend 1nllbg " Ahaha..."
    n 1kllss "Well...{w=0.5}{nw}"
    extend 1nllsl " almost."
    n 1fsqpu "What I {i}really{/i} hate is when people look at something someone made,{w=0.5}{nw}"
    extend 1fcswr " and then just give them a bunch of grief over it!"
    n 1flrem "Like if the creator is learning and made a mistake,{w=0.1} or if they had another take on something.{w=1}{nw}"
    extend 1fcsan " It's so stupid!"
    n 1fcsaj "I get {i}constructive{/i} criticism,{w=1}{nw}"
    extend 1fsqan " but just being a jerk because it isn't {i}exactly{/i} how {i}you{/i} want it?{w=1}{nw}"
    extend 1fcsem " Come {b}on{/b}!"
    n 1fsrem "Get a grip."
    n 1fcsemesi "..."
    n 1fslsl "Hard to believe people can be so {i}entitled{/i} over something others do for free,{w=0.1} huh?{w=0.5}{nw}"
    extend 1fslpo " Jerks."
    n 1nllpo "Well,{w=0.1} anyway.{w=1}{nw}"
    extend 1nslpo " Enough about people like {i}that{/i}."
    n 1nlrbo "I don't know if you do any fanart or anything,{w=0.1} [player]..."

    if jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.artwork):
        n 1fchsmleme "Probably~."

    n 1fnmpo "But you better not be letting people push you around over yours!"
    n 1fsqpo "...Or be giving people a hard time over theirs."
    n 1fcsbg "...Because that's where I {i}draw{/i} the line!{w=1}{nw}"
    extend 1fsqsm " Ehehe."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_how_to_interview_properly",
            unlocked=True,
            prompt="How to interview properly",
            conditional="jn_utils.get_total_gameplay_days() >= 5",
            category=["Life", "Society"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_how_to_interview_properly:
    n 1fllbo "Hmm..."
    n 1tllbo "Hey,{w=0.5}{nw}"
    extend 1tnmpu " [player]."
    n 1tlrbo "It's kinda out of the blue,{w=0.5}{nw}"
    extend 1nsrss " but I was curious."
    n 1tnmaj "When was the last time you interviewed for something?"
    n 1tlrbo "Or...{w=0.5} now that I think about it...{w=1}{nw}"
    extend 1tnmpu " have you interviewed for {i}anything{/i} before?{w=1}{nw}"
    extend 1unmaj " Like,{w=0.1} at all?"
    n 1fslss "Because if there's one thing I've heard...{w=1}{nw}"
    extend 1fnmpo " it's how anxious everyone seems to get over interviewing!"
    n 1ksqposbl "I'm being serious!{w=0.5}{nw}"
    extend 1fllem " People just get so worked up over it all.{w=1}{nw}"
    extend 1fcsem " Like it's rocket science or something."
    n 1flraj "I mean...{w=1}{nw}"
    extend 1unmca " I've never had to interview for anything super important myself."
    n 1ulraj "We had some practice interviews at school,{w=0.1} obviously.{w=1}{nw}"
    extend 1nslss " I was too busy with studies to try at getting a part-time job or anything."
    n 1fsqsg "...But who says that doesn't mean I can teach you a thing or two?{w=0.75}{nw}"
    extend 1fchgn " Ehehe."
    n 1fsqsm "You should know what time it is by now..."
    n 1fcsbg "...So listen up,{w=0.1} [player]!"
    n 1fcssmedz "You're about to learn how to ace your interviews from a pro!"

    n 1fnmbg "So!{w=0.75}{nw}"
    extend 1fsqsm " The first order of business..."
    n 1fllbg "Research,{w=0.5}{nw}"
    extend 1tsqss " duh!"
    n 1usqaj "If there's one thing you gotta know before going to interview for something,{w=0.5}{nw}"
    extend 1fchgnelg " it's what you're actually interviewing {i}for{/i}!"
    n 1fllaj "You wouldn't skimp out on revising before a big test,{w=1}{nw}"
    extend 1tnmsl " and interviews really aren't much different when you think about it."
    n 1fnmss "Interviewing for some big-shot company?{w=1}{nw}"
    extend 1fcsbg " Check them out online and take notes!"
    n 1ullaj "Obviously you need to read up on what they do and where they actually {i}are{/i},{w=1}{nw}"
    extend 1fnmaj " but don't underestimate the power of trivia!"
    n 1ullpu "Even just knowing random stuff like when they were founded,{w=1}{nw}"
    extend 1nlrss " or what awards they won recently {w=0.1}-{w=0.5}{nw}"
    extend 1fcsss " it all shows the effort you're putting in."
    n 1tsqss "And when it comes down to the wire?"
    n 1fwlsm "Even something tiny like that can just about tip the scales."

    n 1fcsss "Next up...{w=0.5}{nw}"
    extend 1fnmca " revision!"
    n 1ullaj "It doesn't matter if you're trying to get a job,{w=1}{nw}"
    extend 1nlrbo " or land a new position on some sort of council."
    n 1nsqpu "Whatever it is...{w=0.5}{nw}"
    extend 1fchlgelg " you gotta be able to {i}prove{/i} you know what you're even talking about!"
    n 1ulraj "Of course, the revision totally depends on what you're going for."
    n 1usqss "Some kind of programming job?{w=0.5}{nw}"
    extend 1fchbg " Refresh yourself on all your weird terminology and techniques!"
    n 1tsgsm "Joining the history club?{w=1}{nw}"
    extend 1fcsss " Read up on some common history questions!"
    n 1nsqpu "And trust me,{w=0.75}{nw}"
    extend 1nsqsr " the {i}last{/i} thing you wanna do is embarrass yourself over simple stuff you should {i}really{/i} know..."
    n 1nllun "...Or something you forgot you mentioned on your application."
    extend 1kchblesd " Oops!"
    n 1nllaj "So...{w=0.5}{nw}"
    extend 1fcsss " study up,{w=0.1} 'kay?"

    n 1fchbg "Alright!{w=0.75}{nw}"
    extend 1tsqss " Keeping up so far,{w=0.1} [player]?"
    n 1fsqsm "You better be...{w=1}{nw}"
    extend 1fchgn " 'cause we're almost done here!"
    n 1unmaj "So,{w=0.1} next on the list -{w=0.5}{nw}"
    extend 1nsrss " and probably the most important of all..."
    n 1fspajedz "Presentation!"
    n 1fllaj "You can have the best credentials in the world,{w=1}{nw}"
    extend 1fsqsr " but that isn't gonna help much if you're mumbling everything {w=0.1}-{w=0.5}{nw}"
    extend 1fchlgelg " or if you just look ridiculous!"
    n 1fnmsr "So!"
    n 1fcspo "Make sure you dress properly for whatever it is.{w=1}{nw}"
    extend 1fllpu " If there's a dress code,{w=0.1} {i}follow it{/i}."
    n 1fsqpo "...And {i}don't{/i} flake out on your clothes.{w=1}{nw}"
    extend 1nlrbo " Iron them if they're all creased,{w=0.1} buy new ones if you need to.{w=0.2} That kind of thing."
    n 1tnmpu "But most of all,{w=0.1} [player]?"
    n 1fsqaj "{i}Never{/i}{w=0.2} forget the basics."
    n 1ullss "Be punctual,{w=0.1} be polite.{w=0.2} Remember {w=0.1}-{w=0.5}{nw}"
    extend 1fsqss " people want someone they can {i}like{/i},{w=0.75}{nw}"
    extend 1fsrpo " not just someone who can get the job done!"

    n 1unmajesu "...Oh,{w=0.5}{nw}"
    extend 1tnmpu " and [player]?"
    n 1fcspu "Just...{w=1}{nw}"
    extend 1knmsrlsbl " be honest too,{w=0.1} alright?"
    n 1fllsrl "It isn't a fault to admit when you don't know something."
    n 1tnmpu "And when you actually stop to think about it from their perspective,{w=1}{nw}"
    extend 1tnmem " if someone is prepared to just lie to your face at an interview..."
    n 1tsqem "...Then what {i}else{/i} are they gonna lie about?"
    n 1tllsssbl "Just some food for thought."

    n 1ncspuesi "..."
    n 1nlrss "...Wow,{w=0.5}{nw}"
    extend 1fchbgelg " I gotta learn when to stop rambling on!{w=0.2} Jeez!"
    n 1fsrssl "That was almost like an interview speech itself,{w=0.1} huh?"

    if Natsuki.isEnamored(higher=True):
        n 1ullpu "Or...{w=1}{nw}"
        extend 1nsrssl " I guess more like an induction,{w=0.1} really."
        n 1fsqdvf "You already got the job with me,{w=0.1} a-{w=0.3}after all."

        if Natsuki.isLove(higher=True):
            n 1fchsml "Ehehe.{w=1}{nw}"
            extend 1nchbll " Love you,{w=0.1} [player]~!"
        else:

            n 1fsrsml "Ehehe..."
    else:

        n 1ullpu "Or...{w=1}{nw}"
        extend 1tnmbo " since we're both stuck here?"
        n 1fsqsm "...More like an induction,{w=0.1} actually."
        n 1fchgn "Ehehe."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_windup_bullying",
            unlocked=True,
            prompt="Bullying",
            category=["Society", "Wind-ups"],
            nat_says=True,
            affinity_range=(jn_affinity.NORMAL, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_windup_bullying:
    n 1fslpu "..."
    n 1fcspuean "Tch!"
    n 1fsran "..."
    n 1tnmaj "Eh?{w=0.5}{nw}"
    extend 1uskemesh " O-{w=0.3}oh!{w=0.5}{nw}"
    extend 1uwdaj " [player].{w=1}{nw}"
    extend 1flrbglsbl " Ahaha."
    n 1fllbg "I...{w=0.5} was kinda just thinking out loud again."
    n 1ullpu "And,{w=0.75}{nw}"
    extend 1nslpu " well..."
    n 1nsqpu "I just had something else come to mind.{w=1}{nw}"
    extend 1fcsem " Something I {i}really{/i} can't stand."
    n 1fsqsr "Bullies.{w=1}{nw}"
    extend 1fcsfu " I can't think of anything I {i}hate{/i} more!"
    n 1flrem "Like,{w=0.5}{nw}"
    extend 1fsqfu " have you ever had the {i}pleasure{/i} of dealing with one?"
    n 1fcsan "It takes a {i}real{/i} piece of work to go out and mess with people on purpose."
    n 1fllwr "You don't even need to be {i}doing{/i} anything!"
    n 1flrem "Just looking the 'wrong' way,{w=0.3}{nw}"
    extend 1fllan " enjoying the 'wrong' thing {w=0.1}-{w=0.3}{nw}"
    extend 1fsqfu " any so-{w=0.1}called {i}excuse{/i},{w=0.1} they'll take."
    n 1fcsem "And when I say mess with people...{w=1}{nw}"
    extend 1fsqem " I don't just mean physically,{w=0.1} either!"
    n 1fllem "Bullies can do their dirty work in so many different ways,{w=0.1} especially with social media being what is is now.{w=1}{nw}"
    extend 1fcsfu " But that's just as toxic!"
    n 1fsqan "And worse yet,{w=0.5}{nw}"
    extend 1tsqem " if you try to stick up for yourself?{w=1}{nw}"
    extend 1fsrem " When you're exhausted of dealing with all of their crap?"
    n 1fcswrean "People get so high and mighty about it!{w=0.75}{nw}"
    extend 1flrem " Like {i}you're{/i} the reason there's a problem!"
    n 1fllaj "'Stop being so dramatic!'{w=0.5}{nw}"
    extend 1flrwr " 'You're just overreacting!'{w=0.5}{nw}"
    extend 1fcsemesi " Ugh."
    n 1tsqem "At this point?{w=0.75}{nw}"
    extend 1flrbo " I've heard it all."
    n 1fsrbosbl "{i}...Not like that makes it any less annoying.{/i}"
    n 1nllaj "But...{w=1}{nw}"
    extend 1nsqbo " one thing I {i}will{/i} tell you right now,{w=0.1} [player]."
    n 1fsqbol "Do {b}not{/b} let what others say stop you from dealing with it."
    n 1fllbol "It isn't {i}their{/i} problem {w=0.1}-{w=0.3}{nw}"
    extend 1fsqpul " and from experience?"
    n 1fsqsr "There's nothing a bully likes {i}more{/i} than someone who tries to ignore them,{w=0.1} or walk away."
    n 1uskemesu "...T-{w=0.3}that's not to say you gotta freak out or anything crazy like that!{w=0.75}{nw}"
    extend 1fcsem " Just..."
    n 1ksqpo "Read the room,{w=0.1} you know?{w=0.75}{nw}"
    extend 1fllpo " Context matters!"
    n 1fcsaj "Always make sure you use the best tools you have to get any jerks off your back."
    n 1fsrss "A school bully doesn't exactly have a manager they report to..."
    n 1fchgnelg "...And work is the {i}last{/i} place for a brawl!{w=0.75}{nw}"
    extend 1fslpol " As {i}boring{/i} as that is."
    n 1nllaj "So...{w=0.5}{nw}"
    extend 1fsrpol " stick up for yourself,{w=0.1} got it?"
    n 1fllss "And make sure you use your brain when you do.{w=1}{nw}"
    extend 1fchgn " That's all I'm saying!"

    if Natsuki.isEnamored(higher=True):
        n 1knmpo "You owe yourself that much,{w=0.1} right?{w=0.75}{nw}"
        extend 1fsqss " Besides,{w=0.1} [player]..."
        n 1fsrssl "I kinda like someone who can show a little guts.{w=0.75}{nw}"

        if Natsuki.isLove(higher=True):
            extend 1fwlsml " Ehehe."
        else:

            extend 1fsldvless " Ehehe..."

    elif Natsuki.isHappy(higher=True):
        n 1kslpo "You owe yourself that much...{w=0.75}{nw}"
        extend 1ksqpolsbl " right?"
    else:

        n 1fsrpolsbl "You owe yourself {i}that{/i} much,{w=0.1} at least."

    return


init 5 python:
    registerTopic(
        Topic(
            persistent._topic_database,
            label="talk_player_change_name",
            unlocked=True,
            prompt="Can you call me something else?",
            conditional="persistent._jn_nicknames_player_allowed",
            category=["You"],
            player_says=True,
            affinity_range=(jn_affinity.ENAMORED, None),
            location="classroom"
        ),
        topic_group=TOPIC_TYPE_NORMAL
    )

label talk_player_change_name:

    if (
        persistent._jn_nicknames_player_allowed 
        and persistent._jn_nicknames_player_current_nickname == persistent.playername
    ):
        n 1unmaj "Huh?{w=0.5}{nw}"
        extend 1tnmbo " You want me to call you something else?"
        n 1ulraj "...I mean,{w=1}{nw}"
        extend 1tnmbo " I guess I can do that?"
        n 1nslsslesd "It's gonna be super weird calling you something {i}other{/i} than [player],{w=0.1} though..."
        n 1fcsbgl "Well,{w=0.1} whatever!{w=0.75}{nw}"
        extend 1uchgn " I'm not one to judge!"
        n 1unmbg "So..."
        show natsuki 1uchbgl at jn_center
    else:




        if persistent._jn_nicknames_player_bad_given_total == 0:
            n 1unmaj "Oh?{w=0.5}{nw}"
            extend 1unmbo " You wanna change your name again?"
            n 1fchbg "Okaaay!{w=0.75}{nw}"
            extend 1fchsml " Ehehe."
            show natsuki 1fchbgl at jn_center

        elif persistent._jn_nicknames_player_bad_given_total == 1:
            n 1unmbo "You want me to call you something else again?{w=0.75}{nw}"
            extend 1unmaj " Sure thing."
            show natsuki 1unmbo at jn_center

        elif persistent._jn_nicknames_player_bad_given_total == 2:
            n 1nsqtr "This again,{w=0.1} [player]?{w=0.75}{nw}"
            extend 1ncsaj " Alright,{w=0.1} fine."
            n 1ncspu "Just...{w=0.3}{w=1}{nw}"
            extend 1nsqsl " think about it properly,{w=0.1} alright?"
            n 1nllaj "So then..."
            show natsuki 1unmca at jn_center

        elif persistent._jn_nicknames_player_bad_given_total == 3:
            n 1fsqsr "..."
            n 1fcsboesi "..."
            n 1fslsl "...Fine,{w=0.1} [player]."
            n 1fsqpu "Just keep in mind what I said {i}last time{/i}."
            show natsuki 1nsqsl at jn_center


    $ nickname = renpy.input(prompt="What were you thinking of,{w=0.3} [player]?", allow=jn_globals.DEFAULT_ALPHABETICAL_ALLOW_VALUES, length=10).strip()

    if nickname.lower() == "nevermind":
        n 1nnmbo "Oh.{w=1}{nw}"
        extend 1nllpo " Well,{w=0.1} I guess that's alright...{w=1}{nw}"
        n 1uchgn "Just means less I gotta remember!{w=0.5}{nw}"
        extend 1fchsmelg " Ehehe."

        return
    else:

        $ nickname_type = jn_nicknames.get_player_nickname_type(nickname)

    if nickname_type == jn_nicknames.NicknameTypes.invalid:
        n 1fllpu "Are...{w=1}{nw}"
        extend 1tnmpu " you sure that's even a {i}name{/i}?"
        n 1tlrpo "..."
        n 1nlrss "...Yeah,{w=0.75}{nw}"
        extend 1nsqbgsbl " I think I'll just stick with [player].{w=0.5}{nw}"
        extend 1fchblsbr " Sorry!"

        return

    elif nickname_type == jn_nicknames.NicknameTypes.disliked:
        n 1fsqemsbl "...Really,{w=0.1} [player]?{w=0.75}{nw}"
        extend 1fnmwrsbl " Why would you even {i}suggest{/i} that?"
        n 1flleml "You must have {i}known{/i} I wouldn't like it!"
        n 1fcsslesi "..."
        n 1ncspu "...Whatever.{w=1}{nw}"
        extend 1fsrsl " Maybe you just weren't using your head enough."
        n 1fcspu "Just...{w=0.3} {i}think{/i} a little more next time."
        n 1knmsll "Please?"

        return

    elif nickname_type == jn_nicknames.NicknameTypes.hated:
        n 1fskwrlesh "...E-{w=0.2}excuse me?!"
        $ player_initial = jn_utils.getPlayerInitial()
        n 1fnmwr "[player_initial]-{w=0.2}[player]!{w=0.75}{nw}"
        extend 1fnmfu " That's an {b}awful{/b} name!"
        n 1fcsan "...And I'd be even {i}more{/i} awful to use it!"
        n 1fsqfu "{i}Not{/i} happening,{w=0.1} [player]!"
        $ persistent._jn_nicknames_player_bad_given_total += 1

    elif nickname_type == jn_nicknames.NicknameTypes.profanity:
        n 1fscwresh "Y-{w=0.2}you said {i}what{/i} now?!{w=1}{nw}"
        extend 1fsqfuean " I-{w=0.1}is that some kind of joke?!"
        n 1fcssc "I am {i}not{/i} getting involved with dirt-slinging like that!"
        n 1fcsan "And unless you want a bar of soap express-shipped to your {b}mouth{/b}..."
        n 1fsqfu "I suggest {i}you{/i} don't either."
        $ persistent._jn_nicknames_player_bad_given_total += 1

    elif nickname_type == jn_nicknames.NicknameTypes.funny:
        n 1fsgdv "..."
        n 1fchgnesi "Pffffft!"
        n 1fchbs "Come on,{w=0.3} you dork!{w=0.75}{nw}"
        extend 1fchgnelg " Be serious,{w=0.1} will you?"
        n 1flldvl "There's no way I'm calling you {i}that{/i}!"

        return
    else:

        $ neutral_nickname_permitted = False


        if nickname.lower() == player.lower():
            n 1tslsssbl "..."
            n 1tnmsssbl "...Business as usual then,{w=0.2} [player]?{w=0.75}{nw}"
            extend 1fsqsm " Ehehe."
            n 1fchbl "Well,{w=0.2} whatever you say!"

            $ neutral_nickname_permitted = True


        elif nickname.lower() == persistent.playername.lower():
            n 1tsgct "Oho?{w=0.75}{nw}"
            extend 1tsqsg " Finally getting bored of all the nicknames,{w=0.1} are we?"
            n 1fchsm "Ehehe."
            n 1fchbgeme "Right-o!{w=0.75}{nw}"
            extend 1fwlbl " Good old [nickname] it is!"

            $ neutral_nickname_permitted = True


        elif nickname.lower() == n_name.lower() and n_name.lower() != "natsuki":
            n 1nllaj "You...{w=1}{nw}"
            extend 1tsqbo " really {i}didn't{/i} think this one through,{w=0.1} did you?"
            n 1tsqpueqm "Do you even know how confusing that'd be?"
            n 1fcsbg "Nah.{w=0.5}{nw}"
            extend 1fchgnelg " Business as usual it is!"
        else:


            n 1tnmss "[nickname],{w=0.1} huh?"
            n 1fllbo "Hmm..."
            n 1unmbg "Well,{w=0.1} works for me!{w=0.75}{nw}"
            extend 1uchsmeme " Consider it done,{w=0.3} [nickname]!"

            if nickname.lower() == "natsuki":
                n 1nslsssbl "...Heh."
                n 1nsldvsbl "{i}Natsuki{/i}."

            $ neutral_nickname_permitted = True


        if (neutral_nickname_permitted):
            $ persistent._jn_nicknames_player_current_nickname = nickname
            $ player = persistent._jn_nicknames_player_current_nickname

        return


    if persistent._jn_nicknames_player_bad_given_total == 1:
        n 1fcsem "Yeesh...{w=1}{nw}"
        extend 1tnmem " who woke {i}you{/i} up on the wrong side of the bed this morning?"
        n 1fllsl "..."
        n 1fcsslesi "...Look,{w=0.1} [player]."
        n 1fnmsl "I get it.{w=0.75}{nw}"
        extend 1flrbo " Maybe you thought you were being funny or something."
        n 1fnmfr "Just knock it off,{w=0.1} alright?{w=1}{nw}"
        extend 1tsqpu " Because honestly?"
        n 1fslsl "I really {i}don't{/i} see the humour."


        $ Natsuki.addApology(jn_apologies.ApologyTypes.bad_player_name)
        $ Natsuki.percentageAffinityLoss(1)

    elif persistent._jn_nicknames_player_bad_given_total == 2:
        n 1fcsan "I honestly can't believe you,{w=0.1} [player].{w=1}{nw}"
        extend 1fsqfr " Were you even {i}listening{/i} last time?{w=1}{nw}"
        extend 1fnmem " Did you even {i}hear{/i} me?"
        n 1fcssfesi "..."
        n 1fsqsf "...Alright,{w=0.1} look.{w=1}{nw}"
        extend 1fsqbo " I'm just gonna get to the point,{w=0.1} so listen up."
        n 1fnmem "{i}Quit messing me around with this,{w=0.1} [player].{/i}"
        n 1fcsem "You make it...{w=0.75}{nw}"
        extend 1fcsunl " difficult...{w=0.75}{nw}"
        extend 1fsrunl " to like you when you behave like {i}that{/i}."


        $ Natsuki.addApology(jn_apologies.ApologyTypes.bad_player_name)
        $ Natsuki.percentageAffinityLoss(2.5)

    elif persistent._jn_nicknames_player_bad_given_total == 3:
        n 1fcsful "You are just {i}unreal{/i},{w=0.1} [player]."
        n 1fsqscean "{i}How many times{/i} do I have to give you crap over this to get you to wise up?!"
        n 1fsqwrean "Are you {i}trying{/i} to earn a smack?"
        n 1fcsfuesi "..."
        n 1fcsan "Well,{w=0.3} you know what?{w=1}{nw}"
        extend 1fsqan " I'm sick of it."
        n 1fcswr "I am {b}done{/b} giving you chances with this,{w=0.3} [player].{w=1} You're on {i}very{/i} thin ice."
        show natsuki 1fsqfu at jn_center

        menu:
            n "Comprende?"
            "I understand.":

                n 1fsqsr "Heh.{w=0.75}{nw}"
                extend 1fnmfr " {i}Now{/i} you understand,{w=0.1} do you?"
                n 1fsqem "...Then {i}act{/i} like it,{w=0.1} [player]."

                $ Natsuki.percentageAffinityLoss(3)
            "...":

                n 1fsqem "...Seriously,{w=0.1} [player]?{w=1}{nw}"
                extend 1fsqsr " You're really going to act like a child about this?"
                n 1fcsan "Quit it and {i}grow up{/i}."

                $ Natsuki.percentageAffinityLoss(5)


        $ Natsuki.addApology(jn_apologies.ApologyTypes.bad_player_name)

    elif persistent._jn_nicknames_player_bad_given_total == 4:

        n 1fcsem "Heh.{w=1}{nw}"
        extend 1fsqemean " You just {i}couldn't resist{/i},{w=1}{nw}"
        extend 1fsqslean " could you?"
        n 1fcsan "I'm {b}done{/b} with you making a fool out of me with this."
        n 1fsqfu "Don't say I didn't warn you.{w=2}{nw}"
        extend 1fsrsr " Jerk."


        python:
            get_topic("talk_player_change_name").lock()
            Natsuki.percentageAffinityLoss(10)
            persistent._jn_nicknames_player_allowed = False
            persistent._jn_nicknames_player_current_nickname = persistent.playername
            player = persistent.playername
            Natsuki.addApology(jn_apologies.ApologyTypes.bad_player_name)

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
