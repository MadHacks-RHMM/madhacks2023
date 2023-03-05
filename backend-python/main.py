import datetime as dt
from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import MyDB, UserData
from plaidapi import PlaidData, LinkData
from plaid.model.products import Products
from plaid.model.country_code import CountryCode
import uvicorn


class FastApp:
    def __init__(self):
        self.app = FastAPI()
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*']
        )
        self.user = None


def main():
    fastapp = FastApp()
    database = MyDB()
    plaid = PlaidData('Development')

    @fastapp.app.get('/')
    async def root():
        return {'message': 'Fetch Connection Successful'}

    @fastapp.app.post('/login')
    async def login(email: str = "", name: str = ""):
        print("DEBUG")
        user = database.get_user(email)
        user = UserData() if user is None else user
        user.email = email
        user.name = name if user.name == "" else user.name

        fastapp.user = user
        return {'message': 'Login Successful', 'banks_exist': True if len(user.banks) > 0 else False}

    @fastapp.app.get('/get_last_roundup')
    async def get_last_roundup():
        if (fastapp.user is None):
            return {'message': 'User Not Found'}
        else:
            return {"message": "Last Roundup Found", "last_roundup": fastapp.user.last_roundup}

    @fastapp.app.get('/set_roundup')
    async def set_roundup():
        if (fastapp.user is None):
            return {'message': 'User Not Found'}
        else:
            fastapp.user.last_roundup = str(datetime(datetime.now()))
            database.set_user(fastapp.user)
            return {"message": "Last Roundup Updated"}

    @fastapp.app.post('/update_donations')
    async def update_donations(donation: float):
        if (fastapp.user is None):
            return {'message': 'User Not Found'}
        else:
            fastapp.user.total_donations += donation
            fastapp.user.current_goal_donations += donation
            database.set_user(fastapp.user)
            return {"message": "Donations Updated"}

    @fastapp.app.get('/get_donations')
    async def get_donations():
        if (fastapp.user is None):
            return {'message': 'User Not Found'}
        else:
            return {"message": "Donations Found", "total_donations": fastapp.user.total_donations, "current_goal_donations": fastapp.user.current_goal_donations}

    @fastapp.app.get('/clear_goal_donations')
    async def clear_goal_donations():
        if (fastapp.user is None):
            return {'message': 'User Not Found'}
        else:
            fastapp.user.current_goal_donations = 0
            database.set_user(fastapp.user)
            return {"message": "Current Goal Donations Cleared"}

    @fastapp.app.get('/get_transactions')
    async def get_transactions():
        if (fastapp.user is None):
            return {'message': 'User Not Found'}
        else:
            return {"message": "Transactions Found", "transactions": plaid.get_transactions(fastapp.user)}

    @fastapp.app.post('/link_success_data')
    async def get_client_id(link_data: LinkData):
        user = database.get_user(link_data.email)
        user = plaid.make_account(
            link_data) if user is None else plaid.update_account(link_data, user)
        database.set_user(user)

        fastapp.user = user

        return {'message': 'Link Success Data Received', 'client_id': link_data.accounts['id']}

    @fastapp.app.post('/create_link_token')
    async def create_link_token():
        configs = {
            "user": {
                "client_user_id": 'user-id'
            },
            "client_name": "Plaid Quickstart",
            "products": [Products("auth"), Products("transactions")],
            "country_codes": [CountryCode("US")],
            "language": "en",
            "redirect_uri": "",
            "android_package_name": "",
        }
        response = plaid.client.link_token_create(configs)
        return response['data']

    uvicorn.run(fastapp.app, host='localhost')


if __name__ == '__main__':
    main()
