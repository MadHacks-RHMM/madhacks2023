from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from flask import jsonify
from plaid.api import plaid_api
from plaid.model.transactions_sync_request import TransactionsSyncRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.products import Products
from plaid.model.country_code import CountryCode
import uvicorn
import plaid
import pymongo


PLAID_CLIENT_ID = "6403cf9acca1db0012448611"
PLAID_SECRET_ID_SANDBOX = "03f8cb25a85a0d46070aea16b08122"
PLAID_SECRET_ID_DEVELOPMENT = "ce796b1f5343a3fce5c0c9b792260d"


class ClientInfo:
    client_id = ""
    access_token = ""
    item_id = ""

    def __init__(self, client_id="", access_token="", item_id=""):
        self.client_id = client_id
        self.access_token = access_token
        self.item_id = item_id


def main():
    fastapp = FastAPI()
    fastapp.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )

    client_info = ClientInfo()

    @fastapp.get('/')
    async def root():
        return {'message': 'Fetch Connection Successful'}

    @fastapp.post('/get_client_id')
    async def get_client_id(**kwargs):
        client_info.client_id = kwargs['client_id']
        return {'message': 'Client ID Received', 'client_id': client_info.client_id}

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

    @fastapp.post('/create_link_token')
    async def create_link_token():
        request = LinkTokenCreateRequest(
            products=[Products("auth")],
            client_name="Plaid Test App",
            country_codes=[CountryCode('US')],
            redirect_uri='https://domainname.com/oauth-page.html',
            language='en',
            webhook='https://webhook.example.com',
            user=LinkTokenCreateRequestUser(
                    client_user_id=client_info.client_id
            )
        )
        response = client.link_token_create(request)

        return jsonify(response.to_dict())

    uvicorn.run(fastapp, host='localhost')


if __name__ == '__main__':
    main()
