init -50 python:
    import store
    import store.jn_outfits as jn_outfits
    import store.jn_utils as jn_utils
    from Enum import Enum

    JN_NATSUKI_ZORDER = 3

    _JN_NATSUKI_BASE_SPRITE_PATH = "mod_assets/natsuki/"
    _JN_TABLE_SPRITE = "table_normal"

    class JNPose(Enum):
        sitting = 1
        
        def __str__(self):
            return self.name

    class JNBlush(Enum):
        full = 1
        light = 2
        
        def __str__(self):
            return self.name

    class JNMouth(Enum):
        agape = 1
        ajar = 2
        angry = 3
        awe = 4
        big = 5
        big_smile = 6
        bored = 7
        caret = 8
        catty = 9
        devious = 10
        embarrassed = 11
        frown = 12
        furious = 13
        gasp = 14
        glub = 15
        grin = 16
        laugh = 17
        nervous = 18
        pout = 19
        pursed = 20
        scream = 21
        serious = 22
        shock = 23
        slant = 24
        small = 25
        small_frown = 26
        small_smile = 27
        smile = 28
        smirk = 29
        smug = 30
        tease = 31
        triangle = 32
        uneasy = 33
        upset = 34
        worried = 35
        blep = 36
        drink = 37
        focus = 38
        flat_smile = 39
        
        def __str__(self):
            return self.name

    class JNEyes(Enum):
        baka = 1
        circle_tears = 2
        closed_happy = 3
        closed_sad = 4
        cute = 5
        normal = 6
        pleading = 7
        scared = 8
        shocked = 9
        smug = 10
        sparkle = 11
        squint = 12
        unamused = 13
        warm = 14
        wide = 15
        wink_left = 16
        wink_right = 17
        look_left = 18
        look_right = 19
        squint_left = 20
        squint_right = 21
        doubt = 22
        down = 23
        pained = 24
        up = 25
        
        def __str__(self):
            return self.name

    class JNEyebrows(Enum):
        normal = 1
        up = 2
        knit = 3
        furrowed = 4
        think = 5
        
        def __str__(self):
            return self.name

    class JNTears(Enum):
        double_stream_closed = 1
        double_stream_narrow = 2
        double_stream_regular = 3
        dried = 4
        single_pooled_closed = 5
        single_pooled_narrow = 6
        single_pooled_regular = 7
        single_stream_closed = 8
        single_stream_narrow = 9
        single_stream_regular = 10
        spritz = 11
        wink_pooled_left = 12
        wink_pooled_right = 13
        
        def __str__(self):
            return self.name

    class JNEmote(Enum):
        affection = 1
        anger = 2
        dazzle = 3
        dread = 4
        exclamation = 5
        idea = 6
        merry = 7
        question_mark = 8
        sad = 9
        sigh = 10
        shock = 11
        sleepy = 12
        somber = 13
        speech = 14
        surprise = 15
        laughter = 16
        sweat_drop = 17
        sweat_spritz = 18
        sweat_small = 19
        
        def __str__(self):
            return self.name

    class JNSweat(Enum):
        bead_left = 1
        bead_right = 2
        
        def __str__(self):
            return self.name

    def jn_generate_natsuki_sprite(
        pose,
        eyebrows,
        eyes,
        mouth,
        blush=None,
        tears=None,
        emote=None,
        sweat=None
    ):
        """
        Generates sprites for Natsuki based on outfit, expression, pose, etc.
        """
        lc_args = [
            (1280, 740), 
            (0, 0), _JN_NATSUKI_BASE_SPRITE_PATH + "desk/chair_normal.png", 
            (0, 0), "{0}{1}/hair/[Natsuki._outfit.hairstyle.reference_name]/back.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, pose), 
            (0, 0), "{0}{1}/base/body.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, pose), 
            (0, 0), "{0}{1}/clothes/[Natsuki._outfit.clothes.reference_name]/{1}.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, pose), 
        ]
        
        
        necklace = Null() if not Natsuki._outfit.necklace else "{0}{1}/necklace/[Natsuki._outfit.necklace.reference_name]/{1}.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, pose)
        lc_args.extend([
            (0, 0), necklace
        ])
        
        
        lc_args.extend([
            (0, 0), "{0}{1}/base/head.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, pose),
        ])
        
        
        if blush:
            lc_args.extend([
                (0, 0), "{0}{1}/face/blush/{2}.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, pose, blush)
            ])
        
        
        lc_args.extend([
            (0, 0), "{0}{1}/face/mouth/{2}.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, pose, mouth),
            (0, 0), "{0}{1}/face/nose/nose.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, pose),
            (0, 0), "{0}{1}/hair/[Natsuki._outfit.hairstyle.reference_name]/bangs.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, pose),
        ])
        
        
        accessory = Null() if not Natsuki._outfit.accessory else "{0}{1}/accessory/[Natsuki._outfit.accessory.reference_name]/{1}.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, pose)
        lc_args.extend([
            (0, 0), accessory
        ])
        
        
        lc_args.extend([
            (0, 0), "{0}{1}/face/eyes/{2}.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, pose, eyes), 
        ])
        
        
        if tears:
            lc_args.extend([
                (0, 0), "{0}{1}/face/tears/{2}.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, pose, tears)
            ])
        
        
        if sweat:
            lc_args.extend([
                (0, 0), "{0}{1}/face/sweat/{2}.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, pose, sweat)
            ])
        
        
        headgear = Null() if not Natsuki._outfit.headgear else "{0}{1}/headgear/[Natsuki._outfit.headgear.reference_name]/{1}.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, pose)
        lc_args.extend([
            (0, 0), headgear
        ])
        
        
        eyewear = Null() if not Natsuki._outfit.eyewear else "{0}{1}/eyewear/[Natsuki._outfit.eyewear.reference_name]/{1}.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, pose)
        lc_args.extend([
            (0, 0), eyewear
        ])
        
        
        if emote:
            lc_args.extend([
                (0, 0), "{0}{1}/emote/{2}.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, pose, emote)
            ])
        
        
        lc_args.extend([
            (0, 0), "{0}{1}/face/eyebrows/{2}.png".format(_JN_NATSUKI_BASE_SPRITE_PATH, pose, eyebrows), 
            (0, 0), _JN_NATSUKI_BASE_SPRITE_PATH + "/desk/{0}.png".format(_JN_TABLE_SPRITE) 
        ])
        
        
        return renpy.display.layout.LiveComposite(
            *lc_args
        )

init 1 python:
    import store

    POSE_MAP = {
        "1": JNPose.sitting
    }

    EYEBROW_MAP = {
        "n": JNEyebrows.normal,
        "u": JNEyebrows.up,
        "k": JNEyebrows.knit,
        "f": JNEyebrows.furrowed,
        "t": JNEyebrows.think
    }

    EYE_MAP = {
        "bk": JNEyes.baka,
        "ct": JNEyes.circle_tears,
        "ch": JNEyes.closed_happy,
        "cs": JNEyes.closed_sad,
        "cu": JNEyes.cute,
        "dt": JNEyes.doubt,
        "dw": JNEyes.down,
        "ll": JNEyes.look_left,
        "lr": JNEyes.look_right,
        "nm": JNEyes.normal,
        "pa": JNEyes.pained,
        "pl": JNEyes.pleading,
        "sc": JNEyes.scared,
        "sk": JNEyes.shocked,
        "sg": JNEyes.smug,
        "sp": JNEyes.sparkle,
        "sq": JNEyes.squint,
        "sl": JNEyes.squint_left,
        "sr": JNEyes.squint_right,
        "un": JNEyes.unamused,
        "up": JNEyes.up,
        "wm": JNEyes.warm,
        "wd": JNEyes.wide,
        "wl": JNEyes.wink_left,
        "wr": JNEyes.wink_right
    }

    MOUTH_MAP = {
        "aj": JNMouth.ajar,
        "an": JNMouth.angry,
        "aw": JNMouth.awe,
        "bg": JNMouth.big,
        "bs": JNMouth.big_smile,
        "bl": JNMouth.blep,
        "bo": JNMouth.bored,
        "ca": JNMouth.caret,
        "ct": JNMouth.catty,
        "dr": JNMouth.drink,
        "dv": JNMouth.devious,
        "em": JNMouth.embarrassed,
        "fo": JNMouth.focus,
        "fr": JNMouth.frown,
        "fs": JNMouth.flat_smile,
        "fu": JNMouth.furious,
        "gs": JNMouth.gasp,
        "gn": JNMouth.grin,
        "lg": JNMouth.laugh,
        "nv": JNMouth.nervous,
        "po": JNMouth.pout,
        "pu": JNMouth.pursed,
        "sc": JNMouth.scream,
        "sr": JNMouth.serious,
        "sk": JNMouth.shock,
        "sl": JNMouth.slant,
        "sm": JNMouth.smile,
        "sf": JNMouth.small_frown,
        "ss": JNMouth.small_smile,
        "sg": JNMouth.smug,
        "ts": JNMouth.tease,
        "tr": JNMouth.triangle,
        "un": JNMouth.uneasy,
        "up": JNMouth.upset,
        "wr": JNMouth.worried
    }

    BLUSH_MAP = {
        "f": JNBlush.full,
        "l": JNBlush.light
    }

    TEARS_MAP = {
        "tda": JNTears.double_stream_closed,
        "tdb": JNTears.double_stream_narrow,
        "tdc": JNTears.double_stream_regular,
        "tdr": JNTears.dried,
        "tsa": JNTears.single_pooled_closed,
        "tsb": JNTears.single_pooled_narrow,
        "tsc": JNTears.single_pooled_regular,
        "tsd": JNTears.single_stream_closed,
        "tse": JNTears.single_stream_narrow,
        "tsf": JNTears.single_stream_regular,
        "tsz": JNTears.spritz,
        "twl": JNTears.wink_pooled_left,
        "twr": JNTears.wink_pooled_right
    }

    EMOTE_MAP = {
        "eaf": JNEmote.affection,
        "ean": JNEmote.anger,
        "edz": JNEmote.dazzle,
        "edr": JNEmote.dread,
        "eex": JNEmote.exclamation,
        "eid": JNEmote.idea,
        "elg": JNEmote.laughter,
        "eme": JNEmote.merry,
        "eqm": JNEmote.question_mark,
        "esd": JNEmote.sad,
        "esi": JNEmote.sigh,
        "esh": JNEmote.shock,
        "esl": JNEmote.sleepy,
        "eso": JNEmote.somber,
        "esp": JNEmote.speech,
        "esu": JNEmote.surprise,
        "esd": JNEmote.sweat_drop,
        "esz": JNEmote.sweat_spritz,
        "ess": JNEmote.sweat_small
    }

    SWEAT_MAP = {
        "sbl": JNSweat.bead_left,
        "sbr": JNSweat.bead_right
    }

    def _parse_exp_code(exp_code):
        """
        Parses the given expression code and returns the **kwargs to create the sprite if it is valid

        THROWS:
            ValueError if the expression is invalid due to length (too short)
            KeyError if the expression is invalid due to invalid parts
        """
        
        if len(exp_code) < 6:
            raise ValueError("Invalid expression code: {0}".format(exp_code))
        
        
        pose = exp_code[0]
        exp_code = exp_code[1:]
        
        
        eyebrows = exp_code[0]
        exp_code = exp_code[1:]
        
        
        eyes = exp_code[:2]
        exp_code = exp_code[2:]
        
        
        mouth = exp_code[:2]
        exp_code = exp_code[2:]
        
        blush = None
        tears = None
        emote = None
        sweat = None
        
        
        while exp_code:
            if exp_code[0] in BLUSH_MAP:
                exp_part = exp_code[0]
                exp_code = exp_code[1:]
                blush = exp_part
            
            else:
                if exp_code[:3] in TEARS_MAP:
                    tears = exp_code[:3]
                    exp_code = exp_code[3:]
                
                elif exp_code[:3] in EMOTE_MAP:
                    emote = exp_code[:3]
                    exp_code = exp_code[3:]
                
                elif exp_code[:3] in SWEAT_MAP:
                    sweat = exp_code[:3]
                    exp_code = exp_code[3:] 
                
                
                else:
                    raise ValueError(
                        "Invalid optional expression part: '{0}'. (All optional parts must follow mandatory ones)".format(exp_code)
                    )
        
        return {
            "pose": POSE_MAP[pose],
            "eyebrows": EYEBROW_MAP[eyebrows],
            "eyes": EYE_MAP[eyes],
            "mouth": MOUTH_MAP[mouth],
            "blush": BLUSH_MAP.get(blush),
            "tears": TEARS_MAP.get(tears),
            "emote": EMOTE_MAP.get(emote),
            "sweat": SWEAT_MAP.get(sweat)
        }

    def _generate_image(exp_code):
        """
        Internal function to generate the image from the given expression code
        """
        
        disp = jn_generate_natsuki_sprite(**_parse_exp_code(exp_code))
        
        
        _existing_attr_list = renpy.display.image.image_attributes["natsuki"]
        
        
        renpy.display.image.images[("natsuki", exp_code)] = disp
        
        
        if exp_code not in _existing_attr_list:
            _existing_attr_list.append(exp_code)

    def _find_target_override(self):
        """
        This method tries to find an image by its reference. It can be a displayable or tuple.
        If this method can't find an image and it follows the pattern of Natsuki's sprites, it'll try to generate one.

        Main change to this function is the ability to auto generate displayables

        IN:
            - self - Reference to the calling narration statement, so we can access its args (name and spritecode)
        """
        name = self.name
        
        if isinstance(name, renpy.display.core.Displayable):
            self.target = name
            return True
        
        
        if not isinstance(name, tuple):
            name = tuple(name.split())
        
        def error(msg):
            """
            Sets the image target to a displayable (text) for a missing image.

            IN:
                - msg - The message to display for the fallback displayable
            """
            self.target = renpy.text.text.Text(
                msg,
                color=(255, 0, 0, 255),
                xanchor=0,
                xpos=0,
                yanchor=0,
                ypos=0
            )
            
            if renpy.config.debug:
                raise Exception(msg)
        
        args = [ ]
        
        while name:
            
            
            
            
            target = renpy.display.image.images.get(name, None)
            
            if target is not None:
                break
            
            args.insert(0, name[-1])
            name = name[:-1]
        
        if not name:
            
            if (
                isinstance(self.name, tuple)
                and len(self.name) == 2
                and self.name[0] == "natsuki"
            ):
                
                name = self.name
                
                _generate_image(name[1])
                
                target = renpy.display.image.images[name]
            
            else:
                
                error("Image '%s' not found." % ' '.join(self.name))
                return False
        
        try:
            a = self._args.copy(name=name, args=args)
            self.target = target._duplicate(a)
        
        except Exception as e:
            if renpy.config.debug:
                raise
            
            error(str(e))
        
        
        new_transform = self.target._target()
        
        if isinstance(new_transform, renpy.display.transform.Transform):
            if self.old_transform is not None:
                new_transform.take_state(self.old_transform)
            
            self.old_transform = new_transform
        
        else:
            self.old_transform = None
        
        return True


    renpy.display.image.ImageReference.find_target = _find_target_override

    if Natsuki.isLove(higher=True):
        _JN_TABLE_SPRITE = "table_love"

    elif Natsuki.isEnamored(higher=True):
        _JN_TABLE_SPRITE = "table_enamored"

    elif Natsuki.isAffectionate(higher=True):
        _JN_TABLE_SPRITE = "table_affectionate"

    elif Natsuki.isUpset(higher=True):
        _JN_TABLE_SPRITE = "table_normal"

    elif Natsuki.isDistressed(higher=True):
        _JN_TABLE_SPRITE = "table_distressed"

    elif Natsuki.isBroken(higher=True):
        _JN_TABLE_SPRITE = "table_broken"

    elif Natsuki.isRuined(higher=True):
        _JN_TABLE_SPRITE = "table_ruined"



















image natsuki gaming:
    block:
        choice:
            "natsuki 1fdwfosbl"
            pause 3
            "natsuki 1fcsfosbl"
            pause 0.1
        choice:

            "natsuki 1fdwpusbr"
            pause 3
        choice:

            "natsuki 1fdwslsbl"
            pause 3
            "natsuki 1fcsslsbl"
            pause 0.1
        choice:

            "natsuki 1fdwcaesssbr"
            pause 3
        choice:

            "natsuki 1fdwsssbl"
            pause 3
            "natsuki 1fcssssbl"
            pause 0.1

    repeat


image natsuki idle = ConditionSwitch(
    "Natsuki.isEnamored(higher=True)", "natsuki idle enamored",
    "Natsuki.isAffectionate(higher=True)", "natsuki idle affectionate",
    "Natsuki.isHappy(higher=True)", "natsuki idle happy",
    "Natsuki.isNormal(higher=True)", "natsuki idle normal",
    "Natsuki.isDistressed(higher=True)", "natsuki idle distressed",
    "True", "natsuki idle ruined",
    predict_all = True
)


image natsuki idle enamored:
    block:
        choice:
            "natsuki 1nchsmf"
            pause 10
        choice:

            "natsuki 1kwmsmf"
            pause 5
            "natsuki 1kcssmf"
            pause 0.1
            "natsuki 1kwmsmf"
            pause 5
            "natsuki 1kcssmf"
            pause 0.1
        choice:

            "natsuki 1kllsmf"
            pause 5
            "natsuki 1kcssmf"
            pause 0.1
            "natsuki 1kllsmf"
            pause 5
            "natsuki 1kcssmf"
            pause 0.1
        choice:

            "natsuki 1klrsmf"
            pause 5
            "natsuki 1kcssmf"
            pause 0.1
            "natsuki 1klrsmf"
            pause 5
            "natsuki 1kcssmf"
            pause 0.1
        choice:

            "natsuki 1knmsmf"
            pause 5
            "natsuki 1kcssmf"
            pause 0.1
            "natsuki 1knmsmf"
            pause 5
            "natsuki 1kcssmf"
            pause 0.1
        choice:

            "natsuki 1kcssmf"
            pause 10
        choice:

            "natsuki 1kcssgf"
            pause 10
        choice:

            "natsuki 1kllsmf"
            pause 2
            "natsuki 1kcssmf"
            pause 0.1
            "natsuki 1knmsmf"
            pause 3
            "natsuki 1fsqsmf"
            pause 3
            "natsuki 1fchblf"
            pause 1
            "natsuki 1fchgnf"
            pause 2
            "natsuki 1klrsmf"
            pause 2
            "natsuki 1kcssmf"
            pause 0.1
        choice:

            "natsuki 1kcssmf"
            pause 3
            "natsuki 1kcsssf"
            pause 3
            "natsuki 1kcssmf"
            pause 5
        choice:

            "natsuki 1nlrpul"
            pause 3
            "natsuki 1ncspul"
            pause 0.1
            "natsuki 1flrpul"
            pause 3
            "natsuki 1ncspul"
            pause 0.1
            "natsuki 1tnmpul"
            pause 1
            "natsuki 1unmpulesu"
            pause 1.5
            "natsuki 1fcspul"
            pause 0.1
            "natsuki 1flldvfsbl"
            pause 4
            "natsuki 1fcsdvf"
            pause 0.1
        choice:

            "natsuki 1uchsmfedz"
            pause 7
        choice:

            "natsuki 1nchsmfeme"
            pause 7

        repeat


image natsuki idle affectionate:
    block:
        choice:
            "natsuki 1ullsml"
            pause 5
            "natsuki 1ucssml"
            pause 0.1
            "natsuki 1ullsml"
            pause 5
            "natsuki 1ucssml"
            pause 0.1
        choice:

            "natsuki 1ulrsml"
            pause 5
            "natsuki 1ucssml"
            pause 0.1
            "natsuki 1ulrsml"
            pause 0.25
            "natsuki 1ucssml"
            pause 0.1
            "natsuki 1ulrsml"
            pause 5
            "natsuki 1ucssml"
            pause 0.1
        choice:

            "natsuki 1unmsml"
            pause 5
            "natsuki 1ucssml"
            pause 0.1
            "natsuki 1unmsml"
            pause 5
            "natsuki 1ucssml"
            pause 0.1
        choice:

            "natsuki 1nnmsgl"
            pause 5
            "natsuki 1ncssgl"
            pause 0.1
            "natsuki 1nnmsgl"
            pause 5
            "natsuki 1ncssgl"
            pause 0.1
        choice:

            "natsuki 1nllbol"
            pause 4
            "natsuki 1fllbol"
            pause 4
            "natsuki 1fcsbol"
            pause 0.1
            "natsuki 1tnmbol"
            pause 4
            "natsuki 1tcsbol"
            pause 0.1
            "natsuki 1fsqsml"
            pause 4
            "natsuki 1fwlsml"
            pause 0.5
            "natsuki 1flldvl"
            pause 2
            "natsuki 1fcsdvl"
            pause 0.1
        choice:

            "natsuki 1nllpul"
            pause 3
            "natsuki 1ncspul"
            pause 0.1
            "natsuki 1fllpul"
            pause 5
            "natsuki 1ncspul"
            pause 0.1
            "natsuki 1tnmpul"
            pause 4
            "natsuki 1tcspul"
            pause 0.1
            "natsuki 1flrdvless"
            pause 4
            "natsuki 1fcsdvl"
            pause 0.1

        repeat


image natsuki idle happy:
    block:
        choice:
            "natsuki 1ullbo"
            pause 4
            "natsuki 1ucsbo"
            pause 0.1
            "natsuki 1ullbo"
            pause 4
            "natsuki 1ucsbo"
            pause 0.1
        choice:

            "natsuki 1ulrbo"
            pause 4
            "natsuki 1ucsbo"
            pause 0.1
            "natsuki 1ulrbo"
            pause 4
            "natsuki 1ucsbo"
            pause 0.1
        choice:

            "natsuki 1ullfs"
            pause 4
            "natsuki 1ucsfs"
            pause 0.1
            "natsuki 1ullfs"
            pause 4
            "natsuki 1ucsfs"
            pause 0.1
        choice:

            "natsuki 1ulrfs"
            pause 4
            "natsuki 1ucsfs"
            pause 0.1
            "natsuki 1ulrfs"
            pause 4
            "natsuki 1ucsfs"
            pause 0.1
        choice:

            "natsuki 1ullca"
            pause 4
            "natsuki 1ucsca"
            pause 0.1
            "natsuki 1tllca"
            pause 4
            "natsuki 1tcsca"
            pause 0.1
            "natsuki 1tllca"
            pause 2
            "natsuki 1tnmpu"
            pause 2
            "natsuki 1tcspu"
            pause 0.1
            "natsuki 1unmpul"
            pause 2
            "natsuki 1ucspul"
            pause 0.1
            "natsuki 1fcspolsbl"
            pause 4
        choice:

            "natsuki 1tslca"
            pause 4
            "natsuki 1tcsca"
            pause 0.1
            "natsuki 1tslca"
            pause 1
            "natsuki 1tcsca"
            pause 0.1
            "natsuki 1tsqca"
            pause 2
            "natsuki 1unmpul"
            pause 2
            "natsuki 1ucspul"
            pause 0.1
            "natsuki 1fslsmlsbl"
            pause 3
            "natsuki 1fcssmlsbl"
            pause 0.1
        choice:

            "natsuki 1ulrcal"
            pause 4
            "natsuki 1ucscal"
            pause 0.1
            "natsuki 1ulrcal"
            pause 4
            "natsuki 1ucscal"
            pause 0.1
        choice:

            "natsuki 1nnmca"
            pause 4
            "natsuki 1ncsca"
            pause 0.1
            "natsuki 1nnmca"
            pause 4
            "natsuki 1ncsca"
            pause 0.1
        choice:

            "natsuki 1ullfs"
            pause 4
            "natsuki 1ucsfs"
            pause 0.1
            "natsuki 1ulrfs"
            pause 4
            "natsuki 1ucsfs"
            pause 0.1

        repeat


image natsuki idle normal:
    block:
        choice:
            "natsuki 1nllbo"
            pause 4
            "natsuki 1ncsbo"
            pause 0.1
            "natsuki 1nllbo"
            pause 4
            "natsuki 1ncsbo"
            pause 0.1
        choice:

            "natsuki 1nlrbo"
            pause 4
            "natsuki 1ncsbo"
            pause 0.1
            "natsuki 1nlrbo"
            pause 4
            "natsuki 1ncsbo"
            pause 0.1
        choice:

            "natsuki 1nllpu"
            pause 4
            "natsuki 1ncspu"
            pause 0.1
            "natsuki 1nllpu"
            pause 4
            "natsuki 1ncspu"
            pause 0.1
        choice:

            "natsuki 1nlrpu"
            pause 4
            "natsuki 1ncspu"
            pause 0.1
            "natsuki 1nlrpu"
            pause 4
            "natsuki 1ncspu"
            pause 0.1
        choice:

            "natsuki 1nllca"
            pause 4
            "natsuki 1ncsca"
            pause 0.1
            "natsuki 1nllca"
            pause 4
            "natsuki 1ncsca"
            pause 0.1
        choice:

            "natsuki 1nlrca"
            pause 4
            "natsuki 1ncsca"
            pause 0.1
            "natsuki 1nlrca"
            pause 4
            "natsuki 1ncsca"
            pause 0.1
        choice:

            "natsuki 1nnmca"
            pause 4
            "natsuki 1ncsca"
            pause 0.1
            "natsuki 1nnmca"
            pause 4
            "natsuki 1ncsca"
            pause 0.1
        choice:

            "natsuki 1nllpu"
            pause 4
            "natsuki 1ncspu"
            pause 0.1
            "natsuki 1nlrpu"
            pause 4
            "natsuki 1ncspu"
            pause 0.1

        repeat


image natsuki idle distressed:
    block:
        choice:
            "natsuki 1fllsl"
            pause 3
            "natsuki 1fcssl"
            pause 0.1
        choice:

            "natsuki 1flrsl"
            pause 3
            "natsuki 1fcssl"
            pause 0.1
        choice:

            "natsuki 1kcssl"
            pause 8
        choice:

            "natsuki 1kcssf"
            pause 8
        choice:

            "natsuki 1fcssf"
            pause 8
        choice:

            "natsuki 1fllsf"
            pause 3
            "natsuki 1fcssf"
            pause 0.1
        choice:

            "natsuki 1flrsf"
            pause 3
            "natsuki 1fcssf"
            pause 0.1
        choice:

            "natsuki 1fsqca"
            pause 3
            "natsuki 1fcsca"
            pause 0.1

        repeat


image natsuki idle ruined:
    block:
        choice:
            "natsuki 1fcsuntsa"
        choice:
            "natsuki 1fcsantsa"
        choice:
            "natsuki 1fslantsb"
        choice:
            "natsuki 1fcssrtsa"
        choice:
            "natsuki 1kcssrtsa"
        choice:
            "natsuki 1ksrsrtsb"
        choice:
            "natsuki 1fsrantse"

        pause 4
        repeat


image natsuki idle introduction:
    block:
        choice:
            "natsuki 1kllsr"
        choice:
            "natsuki 1klrsr"
        choice:
            "natsuki 1klrpu"
        choice:
            "natsuki 1kllpu"
        choice:
            "natsuki 1kcspu"
        choice:
            "natsuki 1kcssr"
        choice:
            "natsuki 1kcsun"
        choice:
            "natsuki 1kllun"
        choice:
            "natsuki 1klrun"
        pause 10
        repeat

init python:
    def show_natsuki_talk_menu():
        """
        Hack to work around renpy issue where the sprite is not refreshed when showing again
        """
        if Natsuki.isEnamored(higher=True):
            renpy.show("natsuki talk_menu_enamored", at_list=[jn_left])
        
        elif Natsuki.isAffectionate(higher=True):
            renpy.show("natsuki talk_menu_affectionate", at_list=[jn_left])
        
        elif Natsuki.isHappy(higher=True):
            renpy.show("natsuki talk_menu_happy", at_list=[jn_left])
        
        elif Natsuki.isNormal(higher=True):
            renpy.show("natsuki talk_menu_normal", at_list=[jn_left])
        
        elif Natsuki.isDistressed(higher=True):
            renpy.show("natsuki talk_menu_distressed", at_list=[jn_left])
        
        else:
            renpy.show("natsuki talk_menu_ruined", at_list=[jn_left])


image natsuki talk_menu_enamored:
    block:
        choice:
            "natsuki 1nchbgl"
        choice:
            "natsuki 1nnmbgl"
        choice:
            "natsuki 1uchssl"
        choice:
            "natsuki 1unmssl"
        choice:
            "natsuki 1uwltsl"


image natsuki talk_menu_affectionate:
    block:
        choice:
            "natsuki 1unmsm"
        choice:
            "natsuki 1unmbg"
        choice:
            "natsuki 1uchbg"
        choice:
            "natsuki 1nchbg"


image natsuki talk_menu_happy:
    block:
        choice:
            "natsuki 1unmss"
        choice:
            "natsuki 1unmfs"
        choice:
            "natsuki 1tnmfs"
        choice:
            "natsuki 1ullaj"
        choice:
            "natsuki 1unmbo"


image natsuki talk_menu_normal:
    block:
        choice:
            "natsuki 1unmss"
        choice:
            "natsuki 1unmaj"
        choice:
            "natsuki 1ulraj"
        choice:
            "natsuki 1ullaj"
        choice:
            "natsuki 1unmca"


image natsuki talk_menu_distressed:
    block:
        choice:
            "natsuki 1fcsun"
        choice:
            "natsuki 1fslun"
        choice:
            "natsuki 1fsrbo"
        choice:
            "natsuki 1fcsbo"
        choice:
            "natsuki 1fcsaj"


image natsuki talk_menu_ruined:
    block:
        choice:
            "natsuki 1fcsantsb"
        choice:
            "natsuki 1fsluntse"
        choice:
            "natsuki 1fcssrtse"
        choice:
            "natsuki 1fnmantdr"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
