#!/usr/bin/env python3

"""Changes all topics of a collection based on its name"""


def update_topics(mongo_collection, name, topics):
    """funct that changes all topics of a school doc

    Args:
        mongo_collection: pymongo collect
        name: school name to upd
        topics: list of topics
    """
    res = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )


if __name__ == '__main__':
    update_topics(mongo_collection, name, topics)
