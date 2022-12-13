init python in topic_handler:
    import store

    normal_topic_map = dict()


    TOPIC_CODE_MAP = {
        store.TOPIC_TYPE_GREETING: store.greetings.GREETING_MAP,
        store.TOPIC_TYPE_FAREWELL: store.jn_farewells.FAREWELL_MAP,
        store.TOPIC_TYPE_NORMAL: store.topics.TOPIC_MAP,
        store.TOPIC_TYPE_ADMISSION: store.jn_admissions.ADMISSION_MAP,
        store.TOPIC_TYPE_COMPLIMENT: store.jn_compliments.COMPLIMENT_MAP,
        store.TOPIC_TYPE_APOLOGY: store.jn_apologies.APOLOGY_MAP,
        store.TOPIC_TYPE_EVENT: store.jn_events.EVENT_MAP
    }

init 6 python in topic_handler:
    ALL_TOPIC_MAP = dict()


    for topic_map in TOPIC_CODE_MAP.values():
        ALL_TOPIC_MAP.update(topic_map)

init 6 python:
    import random

    def get_topic(topic_label):
        """
        Gets a Topic object by its label

        IN:
            topic_label - Topic.label representing the label of the topic we wish to get

        OUT:
            Topic if a topic with the
        """
        return store.topic_handler.ALL_TOPIC_MAP.get(topic_label, None)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
