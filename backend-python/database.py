import pymongo
import datetime as dt
from datetime import datetime
import sys


class UserData:
    def __init__(self) -> None:
        self.access_tokens: dict[str, str] = {}
        self.account_ids: dict[str, list[str]] = []
        self.banks: list[str] = []
        self.bank_ids: list[str] = []
        self.bank_account_tokens: dict[str, dict[str, str]] = []
        self.last_rounded: str = str(datetime(dt.MINYEAR, 1, 1))
        self.name: str = ""
        self.email: str = ""
        self.total_donations: float = 0.0
        self.current_goal_donations: float = 0.0

    def __iter__(self):
        for key in self.__dict__:
            yield key, getattr(self, key)

    def __init__(self, data: dict):
        if data is None:
            self = None
            return
        self.access_tokens = data['access_tokens']
        self.account_ids = data['account_ids']
        self.banks = data['banks']
        self.bank_ids = data['bank_ids']
        self.bank_account_tokens = data['bank_account_tokens']
        self.last_rounded = data['last_rounded']
        self.name = data['name']
        self.email = data['email']


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

    def get_user(self, email: str) -> UserData | None:
        return UserData(self.db.find({"email": email}))

    def set_user(self, user: UserData) -> None:
        return None if self.db.update_one({"email": user.email}, {
            "$set": dict(user)}, upsert=True) else None


print(MyDB().db.list_collection_names())
