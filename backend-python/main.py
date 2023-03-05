from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from plaid.api import plaid_api
from plaid.model.transactions_sync_request import TransactionsSyncRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
import uvicorn
import plaid


PLAID_CLIENT_ID = "6403cf9acca1db0012448611"
PLAID_SECRET_ID_SANDBOX = "03f8cb25a85a0d46070aea16b08122"
PLAID_SECRET_ID_DEVELOPMENT = "ce796b1f5343a3fce5c0c9b792260d"


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

    host = plaid.Environment.Sandbox

    configuration = plaid.Configuration(
        host=host,
        api_key={
            'clientId': PLAID_CLIENT_ID,
            'secret': PLAID_SECRET_ID_SANDBOX,
            'plaidVersion': '2020-09-14'
        }
    )

    api_client = plaid.ApiClient(configuration)
    client = plaid_api.PlaidApi(api_client)

    uvicorn.run(fastapp, host='localhost')


if __name__ == '__main__':
    main()
