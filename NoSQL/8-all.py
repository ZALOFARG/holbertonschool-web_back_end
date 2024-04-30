#!/usr/bin/env python3

"""List all documents in a collection"""


def list_all(mongo_collection):
    """Func that list all doc in a collect

    Args:
        mongo_collection: collection
    """
    all_docs = mongo_collection.find({})
    if all_docs:
        return all_docs
    else:
        return []


if __name__ == '__main__':
    list_all(mongo_collection)
