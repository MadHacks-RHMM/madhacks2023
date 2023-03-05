import pymongo
from datetime import datetime
import sys


class UserData:
    def __init__(self) -> None:
        self.access_tokens: dict[str, str] = {}
        self.account_ids: dict[str, list[str]] = []
        self.banks: list[str] = []
        self.bank_ids: list[str] = []
        self.bank_account_tokens: dict[str, dict[str, str]] = []
        self.last_rounded: datetime = None
        self.name: str = ""
        self.email: str = ""


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

    def get_user(self, email: str) -> UserData:
        pass


# MyDB()
