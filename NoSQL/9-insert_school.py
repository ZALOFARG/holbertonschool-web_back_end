#!/usr/bin/env python3

"""Creates a new document in a collectino"""


def insert_school(mongo_collection, **kwargs):
    """Insert a new doc in a collect

    Args:
        mongo_collection: collection
        kwargs: key-value args

    Returns:
        _id
    """
    inserted = mongo_collection.insert_one(kwargs)
    return inserted


if __name__ == '__main__':
    insert_school(mongo_collection, **kwargs)
