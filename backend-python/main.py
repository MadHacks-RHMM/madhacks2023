from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import MyDB, UserData
from plaidapi import PlaidData, LinkData
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
    async def login(email: str = ""):
        user = database.get_user(email)
        if user is None:
            return {'message': 'User Not Found'}

        fastapp.user = user
        return {'message': 'Login Successful'}

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

    uvicorn.run(fastapp.app, host='localhost')


if __name__ == '__main__':
    main()
