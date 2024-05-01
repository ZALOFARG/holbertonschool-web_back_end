#!/usr/bin/env python3

"""Returns a list of school having a topic"""


def schools_by_topic(mongo_collection, topic):
    """funct that returns the list of school having a topic

    Args:
        mongo_collection: pymongo collection
        topic: string searched
    """
    result = mongo_collection.find({"topics": topic})
    return list(result)


if __name__ == '__main__':
    schools_by_topic(mongo_collection, topic)
