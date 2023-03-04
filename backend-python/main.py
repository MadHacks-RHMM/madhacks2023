from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from plaid.api import plaid_api
from plaid.model.transactions_sync_request import TransactionsSyncRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
import uvicorn
import plaid


def main():
    fastapp = FastAPI()
    fastapp.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )

    @fastapp.get('/')
    def root():
        return {'message': 'Fetch Connection Successful'}

    uvicorn.run(fastapp, host='localhost')


if __name__ == '__main__':
    main()
