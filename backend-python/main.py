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


def main():
    fastapp = FastApp()

    @fastapp.app.get('/')
    async def root():
        return {'message': 'Fetch Connection Successful'}

    @fastapp.app.post('/link_success_data')
    async def get_client_id(link_data: LinkData):
        return {'message': 'Link Success Data Received', 'client_id': link_data.accounts['id']}

    uvicorn.run(fastapp.app, host='localhost')


if __name__ == '__main__':
    main()
