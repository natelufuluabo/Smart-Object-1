import pymongo
from datetime import datetime, date

client = pymongo.MongoClient(
    "mongodb+srv://Nathan:77Tq4TiUYt0xKl9c@cluster0.l0rmu9c.mongodb.net/?retryWrites=true&w=majority"
)


def add_action(action):
    client = pymongo.MongoClient(
                     "mongodb+srv://Nathan:77Tq4TiUYt0xKl9c@cluster0.l0rmu9c.mongodb.net/?retryWrites=true&w=majority")

    now = datetime.now()

    db = client.get_database("Projet1")

    collection = (
        db["actions"]
        if len(db.list_collection_names()) > 0
        else db.create_collection("action")
    )

    collection.insert_one(
            {"time": now.strftime("%H:%M"), "date": now.strftime("%d-%m-%Y"), "action": action}
    )


def get_records():
    client = pymongo.MongoClient(
        "mongodb+srv://Nathan:77Tq4TiUYt0xKl9c@cluster0.l0rmu9c.mongodb.net/?retryWrites=true&w=majority")

    db = client.get_database("Projet1")

    collection = db["actions"]

    return list(collection.find().sort([("_id", pymongo.DESCENDING)]).limit(20))
