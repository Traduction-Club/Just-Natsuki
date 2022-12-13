default persistent.jn_ui_style = "default"

init python in jn_preferences.weather:
    from Enum import Enum
    import store

    class JNWeatherSettings(Enum):
        disabled = 1
        random = 2
        real_time = 3
        
        def __int__(self):
            return self.value

init python in jn_preferences.random_topic_frequency:
    from Enum import Enum
    import store

    NEVER = 0
    RARELY = 1
    SOMETIMES = 2
    FREQUENT = 3
    OFTEN = 4

    _RANDOM_TOPIC_FREQUENCY_COOLDOWN_MAP = {
        0: 999,
        1: 30,
        2: 15,
        3: 5,
        4: 2,
    }

    _RANDOM_TOPIC_FREQUENCY_DESC_MAP = {
        0: "Never",
        1: "Rarely",
        2: "Sometimes",
        3: "Frequent",
        4: "Often",
    }

    def get_random_topic_frequency_description():
        """
        Gets the descriptor for the random topic frequency, as given by the current frequency.
        """
        return _RANDOM_TOPIC_FREQUENCY_DESC_MAP.get(store.persistent.jn_natsuki_random_topic_frequency)

    def get_random_topic_cooldown():
        """
        Gets the cooldown (in minutes) between topics prompted by Natsuki, as given by the current frequency.
        """
        return _RANDOM_TOPIC_FREQUENCY_COOLDOWN_MAP.get(store.persistent.jn_natsuki_random_topic_frequency)


default persistent.jn_natsuki_random_topic_frequency = jn_preferences.random_topic_frequency.SOMETIMES


default persistent.jn_natsuki_repeat_topics = True


default persistent._jn_weather_setting = int(jn_preferences.weather.JNWeatherSettings.disabled)


default persistent._jn_notify_conversations = True


default persistent._jn_notify_activity = True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
