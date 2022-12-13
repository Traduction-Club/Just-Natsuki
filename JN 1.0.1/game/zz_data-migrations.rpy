default persistent._jn_version = "0.0.1"

python early in jn_data_migrations:
    from enum import Enum
    import re
    import store
    import store.jn_utils as jn_utils







    UPDATE_FUNCS = dict()


    LATE_UPDATES = []



    VER_STR_PARSER = re.compile(r"^(?P<ver>\d+\.\d+\.\d+)(?P<suffix>.*)$")

    class MigrationRuntimes(Enum):
        """
        Enum for the times to run migration scripts.
        """
        INIT = 1
        RUNTIME = 2

    def migration(from_versions, to_version, runtime=MigrationRuntimes.INIT):
        """
        Decorator function to register a data migration function

        IN:
            from_versions: list of versions to migrate from
            to_version: version to migrate to
            during_runtime: whether the migration is run during runtime. If False, it is run during init 10
                (Default: MigrationRuntimes.INIT)

        OUT:
            the wrapper function
        """
        def wrap(_function):
            registerUpdateFunction(
                _callable=_function,
                from_versions=from_versions,
                to_version=to_version,
                runtime=runtime
            )
            return _function
        return wrap

    def registerUpdateFunction(_callable, from_versions, to_version, runtime=MigrationRuntimes.INIT):
        """
        Register a function to be called when the program is updated.

        IN:
            _callable: the function to run (Must take no arguments)
            from_versions: list of versions to migrate from
            to_version: version to migrate to
            during_runtime: whether the migration is run during runtime. If False, it is run during init 10
                (Default: MigrationRuntimes.INIT)
        """
        for from_version in from_versions:
            if from_version not in UPDATE_FUNCS:
                UPDATE_FUNCS[from_version] = dict()
            
            UPDATE_FUNCS[from_version][runtime] = (_callable, to_version)

    def verStrToVerList(ver_str):
        """
        Converts a version string to a list of integers representing the version.
        """
        match = VER_STR_PARSER.match(ver_str)
        if not match:
            raise ValueError("Invalid version string.")
        
        ver_list = match.group("ver").split(".")
        return [int(x) for x in ver_list]

    def compareVersions(ver_str1, ver_str2):
        """
        Compares two version strings.
        """
        match1 = VER_STR_PARSER.match(ver_str1)
        match2 = VER_STR_PARSER.match(ver_str2)
        
        if not match1 or not match2:
            raise ValueError("Invalid version string.")
        
        ver1 = verStrToVerList(match1.group("ver"))
        ver2 = verStrToVerList(match2.group("ver"))
        
        
        if len(ver1) > len(ver2):
            ver2 += [0] * (len(ver1) - len(ver2))
        elif len(ver1) < len(ver2):
            ver1 += [0] * (len(ver2) - len(ver1))
        
        
        for i in range(len(ver1)):
            if ver1[i] > ver2[i]:
                return 1
            elif ver1[i] < ver2[i]:
                return -1
        
        
        return 0

    def runInitMigrations():
        """
        Runs init time migration functions. Must be run after init 0
        """
        jn_utils.log("runInitMigrations START")
        
        if store.persistent._jn_version not in UPDATE_FUNCS:
            return
        
        
        from_version = store.persistent._jn_version
        
        
        
        while compareVersions(from_version, renpy.config.version) < 0:
            
            if MigrationRuntimes.RUNTIME in UPDATE_FUNCS[store.persistent._jn_version]:
                LATE_UPDATES.append(UPDATE_FUNCS[store.persistent._jn_version][MigrationRuntimes.RUNTIME])
            
            
            _callable, from_version = UPDATE_FUNCS[from_version][MigrationRuntimes.INIT]
            
            
            _callable()

    def runRuntimeMigrations():
        """
        Runs the runtime migration functions.
        """
        jn_utils.log("runRuntimeMigrations START")
        for _callable in LATE_UPDATES:
            _callable()


init 10 python:
    jn_utils.log("Current persisted version pre-mig check: {0}".format(store.persistent._jn_version))
    jn_data_migrations.runInitMigrations()


init python in jn_data_migrations:
    import store
    import store.jn_outfits as jn_outfits
    import store.jn_utils as jn_utils

    @migration(["0.0.0", "0.0.1", "0.0.2"], "1.0.0", runtime=MigrationRuntimes.INIT)
    def to_1_0_0():
        jn_utils.log("Migration to 1.0.0 START")
        
        if (
            store.persistent.jn_player_nicknames_allowed is not None
            and not store.persistent.jn_player_nicknames_allowed
        ):
            store.persistent._jn_nicknames_natsuki_allowed = False
            del store.persistent.jn_player_nicknames_allowed
            jn_utils.log("Migrated: persistent.jn_player_nicknames_allowed")
        
        
        if (
            store.persistent.jn_player_nicknames_current_nickname is not None
            and store.persistent.jn_player_nicknames_current_nickname != "Natsuki"
            and store.persistent._jn_nicknames_natsuki_allowed
        ):
            store.persistent._jn_nicknames_natsuki_current_nickname = store.persistent.jn_player_nicknames_current_nickname
            store.n_name = store.persistent._jn_nicknames_natsuki_current_nickname
            del store.persistent.jn_player_nicknames_current_nickname
            jn_utils.log("Migrated: persistent.jn_player_nicknames_current_nickname")
        
        if (
            store.persistent.jn_player_nicknames_bad_given_total is not None
            and store.persistent.jn_player_nicknames_bad_given_total > 0
        ):
            store.persistent._jn_nicknames_natsuki_bad_given_total = store.persistent.jn_player_nicknames_bad_given_total
            del store.persistent.jn_player_nicknames_bad_given_total
            jn_utils.log("Migrated: persistent.jn_player_nicknames_bad_given_total")
        
        
        if store.Natsuki.isLove(higher=True) and store.persistent.jn_player_love_you_count == 0:
            store.persistent.affinity = jn_affinity.AFF_THRESHOLD_LOVE -1
        
        
        store.persistent._apology_database = dict()
        
        store.persistent._topic_database["talk_i_love_you"]["conditional"] = None
        store.get_topic("talk_i_love_you").conditional = None
        
        store.persistent._topic_database["talk_mod_contributions"]["conditional"] = "not jn_activity.ACTIVITY_SYSTEM_ENABLED or jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.coding)"
        store.get_topic("talk_mod_contributions").conditional = "not jn_activity.ACTIVITY_SYSTEM_ENABLED or jn_activity.ACTIVITY_MANAGER.hasPlayerDoneActivity(jn_activity.JNActivities.coding)"
        
        jn_utils.log("Migrated: store.persistent._apology_database")
        jn_utils.log("""Migrated: store.persistent._topic_database["talk_i_love_you"]["conditional"]""")
        jn_utils.log("""Migrated: store.persistent._topic_database["talk_mod_contributions"]["conditional"]""")
        
        
        if (
            store.persistent.jn_activity_used_programs is not None
            and len(store.persistent.jn_activity_used_programs) > len(store.persistent._jn_activity_used_programs)
        ):
            store.persistent._jn_activity_used_programs = store.persistent.jn_activity_used_programs
            del store.persistent.jn_activity_used_programs
            jn_utils.log("Migrated: persistent.jn_activity_used_programs")
        
        if store.persistent.jn_notify_conversations is not None:
            store.persistent._jn_notify_conversations = store.persistent.jn_notify_conversations
            del store.persistent.jn_notify_conversations
            jn_utils.log("Migrated: persistent.jn_player_nicknames_bad_given_total")
        
        store.persistent._jn_version = "1.0.0"
        jn_utils.save_game()
        jn_utils.log("Migration to 1.0.0 DONE")
        return

    @migration(["1.0.0"], "1.0.1", runtime=MigrationRuntimes.INIT)
    def to_1_0_1():
        jn_utils.log("Migration to 1.0.1 START")
        
        
        jn_outfits.get_outfit("jn_nyatsuki_outfit").unlock()
        jn_outfits.get_wearable("jn_clothes_qeeb_sweater").unlock()
        jn_outfits.get_wearable("jn_clothes_qt_sweater").unlock()
        
        store.persistent._jn_version = "1.0.1"
        jn_utils.save_game()
        jn_utils.log("Migration to 1.0.1 DONE")
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
