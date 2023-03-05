from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from flask import jsonify
from database import MyDB, UserData
from plaidapi import PlaidData, LinkData
import uvicorn


class ClientInfo:
    client_id = ""
    access_token = ""
    item_id = ""
    password = ""

    def __init__(self, client_id="", access_token="", item_id="", password=""):
        self.client_id = client_id
        self.access_token = access_token
        self.item_id = item_id
        self.password = password


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

    @fastapp.get('/lg', response_class=HTMLResponse)
    async def lg_get():
        return " \
    <html>\
        <body>\
            <p>Enter your ID and Password</p>\
            <form action=\"/lg\" method=\"post\">\
                <input type=\"text\" name=\"id\" />\
                <input type=\"text\" name=\"password\" />\
                <button type=\"submit\">Submit</button>\
            </form>\
        </body>\
    </html>"""

    @fastapp.post('/lg', response_class=HTMLResponse)
    async def lg_post(id=Form(), password=Form()):
        client_info.client_id = id
        client_info.password = password
        return (
            f"""
    {client_info.client_id} \n {client_info.password}
    """)

    @fastapp.post('/get_client_id')
    async def get_client_id(**kwargs):
        client_info.client_id = kwargs['client_id']
        return {'message': 'Client ID Received', 'client_id': client_info.client_id}

    uvicorn.run(fastapp, host='localhost')


if __name__ == '__main__':
    main()
