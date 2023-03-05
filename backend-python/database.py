import pymongo
import sys


class MyDB:
    def __init__(self):
        try:
            self.client = pymongo.MongoClient(
                "mongodb+srv://testuser:testuserpasscode@appdb.w5lrki7.mongodb.net/?retryWrites=true&w=majority")

            # return a friendly error if a URI error is thrown
        except pymongo.errors.ConfigurationError:
            print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
            sys.exit(1)

            # use a database named "AppDB"

        self.db = self.client.AppDB
        print(self.db.name)


# MyDB()