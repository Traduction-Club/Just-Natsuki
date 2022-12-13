# Nickname data
default persistent.jn_player_nicknames_allowed = True
default persistent.jn_player_nicknames_current_nickname = "Natsuki"
default persistent.jn_player_nicknames_bad_given_total = 0

init 0 python in jn_nicknames:
    import store.jn_globals as jn_globals
    import store.jn_utils as jn_utils
    
    # Nickname types
    TYPE_INVALID = 0
    TYPE_LOVED = 1
    TYPE_NEUTRAL = 2
    TYPE_DISLIKED = 3
    TYPE_HATED = 4
    TYPE_PROFANITY = 5
    TYPE_FUNNY = 6
    TYPE_NOU = 7
    
    # Natsuki loves these nicknames; awarding them awards affinity/trust
    NICKNAME_LOVED_LIST = {
        "bebé",
        "genial",
        "angel",
        "babygirl",
        "baby",
        "pastelillo",
        "hermosa",
        "bestgirl",
        "media naranja",
        "boo",
        "bunbun",
        "bun-bun",
        "bombón",
        "conejita",
        "buttercup",
        "butterscotch",
        "dulce",
        "galleta",
        "cupcake",
        "cuteypie",
        "cutey",
        "cutiepie",
        "cutie",
        "darlin",
        "querida",
        "doll",
        "dollface",
        "dove",
        "gem",
        "gorgeous",
        "heartstring",
        "heart-string",
        "heartthrob",
        "heart-throb",
        "cielo",
        "flor",
        "honeybun",
        "hun",
        "ki",
        "gatita",
        "migatita",
        "amor",
        "mi",
        "miflor",
        "miamor",
        "miquerida",
        "miprincesa",
        "mireina",
        "mirosa",
        "natnat",
        "nat",
        "nat-nat",
        "natsu",
        "natsukitten",
        "natsukitty",
        "natty",
        "nattykins",
        "numberone",
        "preciosa",
        "princesa",
        "qtpie",
        "qt",
        "reina",
        "snooki",
        "snookums",
        "especial",
        "squeeze",
        "starlight",
        "starshine",
        "su",
        "sugar",
        "sugarlump",
        "sugarplum",
        "'suki",
        "suki",
        "verano",
        "sunny",
        "brillante",
        "sweetcakes",
        "sweetpea",
        "sweetheart",
        "linda",
        "sweetness",
        "sweety",
        "bestdoki"
    }

    # Natsuki dislikes these nicknames; no penalty given but name will not be permitted
    NICKNAME_DISLIKED_LIST = {
        "papá",
        "papa",
        "padre",
        "lily",
        "moni",
        "monika",
        "monikins",
        "monmon",
        "mon-mon",
        "sayo",
        "sayori",
        "yori",
        "yuri",
        "weeb"
        "otaku"
    }

    # Natsuki hates these (non-profanity) nicknames; awarding them detracts affinity/trust
    NICKNAME_HATED_LIST={
        "arrogante",
        "bestia",
        "inútil",
        "estupida",
        "brat",
        "malcriada",
        "tabla",
        "bully",
        "tramposa",
        "niña",
        "payasa",
        "tabla de planchar",
        "demonio",
        "imbécil",
        "sucia",
        "asquerosa",
        "perro",
        "tonta",
        "mocosa",
        "dumbo",
        "dunce",
        "enana",
        "dweeb",
        "egoista",
        "ególatra",
        "malvada",
        "falla",
        "falsa",
        "gorda",
        "fatso",
        "fatty",
        "plana",
        "flatso",
        "flatty",
        "gilf",
        "gremlin",
        "grosera",
        "hobbit",
        "pitufo",
        "half-pint",
        "halfwit",
        "desalmada",
        "infierno",
        "hideous",
        "horrible",
        "horrid",
        "hambrienta",
        "idiota",
        "ignoramus",
        "ignorante",
        "imbecil",
        "imp",
        "mesa",
        "niñita",
        "lesbiana",
        "lesbi",
        "midget",
        "moron",
        "narcisista",
        "nasty",
        "cuello roto",
        "neck-crack",
        "necksnap",
        "neck-snap",
        "nerd",
        "nimrod",
        "nuisance",
        "peste",
        "juguete"
        "saco",
        "punch-bag",
        "punchingbag",
        "punching-bag",
        "marioneta",
        "podrida",
        "pequeña",
        "shortstuff",
        "shorty",
        "enferma",
        "simp",
        "simplona",
        "skinny",
        "esclava",
        "apetosa",
        "soil",
        "muerta de hambre",
        "starving",
        "stinky",
        "stuckup"
        "stuck-up",
        "stupid",
        "teabag",
        "thot",
        "tiny",
        "toy",
        "twerp",
        "twit",
        "useless",
        "maquina expendedora",
        "vomito",
        "muro",
        "bruja",
        "wretch",
        "zombie"
    }

    # Natsuki finds these nicknames funny
    NICKNAME_FUNNY_LIST = {
        "catsuki",
        "preciosa",
        "sexy",
        "hotstuff",
        "hottie",
        "nyatsuki",
        "mama",
        "mom",
        "mami",
        "mamá",
        "mum",
        "mummy",
        "sexi",
        "smol",
        "snack",
        "chiquita"
    }

    NICKNAME_NOU_LIST = {
        "rara",
        "baka",
        "booplicate",
        "booplic8",
        "booplik8",
        "boopliqeeb",
        "boopliqeb",
        "dummy",
        "qab",
        "qeb",
        "qeeb",
        "qebqeb",
        "qebweb",
        "qib",
        "qob",
        "qoob",
        "qub",
        "web",
        "webqeb",
        "woob",
        "wob"
    }

    def get_nickname_type(nickname):
        """
        Returns the nickname type for a given string nickname, defaulting to TYPE_NEUTRAL

        IN:
            nickname - The nickname to test
        OUT:
            Nickname type, integer as defined in constant list
        """

        if not isinstance(nickname, basestring):
            return TYPE_INVALID
        
        else:
            nickname = nickname.lower().replace(" ", "")

            if nickname in NICKNAME_LOVED_LIST:
                return TYPE_LOVED

            elif nickname in NICKNAME_DISLIKED_LIST:
                return TYPE_DISLIKED

            elif nickname in NICKNAME_HATED_LIST:
                return TYPE_HATED

            elif jn_utils.get_string_contains_profanity(nickname):
                return TYPE_PROFANITY

            elif nickname in NICKNAME_FUNNY_LIST:
                return TYPE_FUNNY

            elif nickname in NICKNAME_NOU_LIST:
                return TYPE_NOU

            else:
                return TYPE_NEUTRAL
