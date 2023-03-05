from plaid.api import plaid_api
from plaid.model.transactions_sync_request import TransactionsSyncRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.processor_stripe_bank_account_token_create_request import ProcessorStripeBankAccountTokenCreateRequest
from database import UserData
from pydantic import BaseModel
import plaid

PLAID_CLIENT_ID = "6403cf9acca1db0012448611"
PLAID_SECRET_ID_SANDBOX = "03f8cb25a85a0d46070aea16b08122"
PLAID_SECRET_ID_DEVELOPMENT = "ce796b1f5343a3fce5c0c9b792260d"


class LinkData(BaseModel):
    def __init__(self, public_token="", accounts="", institution="", linkSessionId="", email="") -> None:
        self.public_token = public_token
        self.accounts = accounts
        self.institution = institution
        self.linkSessionId = linkSessionId
        self.email = email


class PlaidData:
    def __init__(self, host) -> None:
        self.host = plaid.Environment.Sandbox if host == 'Sandbox' else plaid.Environment.Development

        self.configuration = plaid.Configuration(
            host=host,
            api_key={
                'clientId': PLAID_CLIENT_ID,
                'secret': PLAID_SECRET_ID_SANDBOX if host == 'Sandbox' else PLAID_SECRET_ID_DEVELOPMENT,
                'plaidVersion': '2020-09-14'
            }
        )

        self.api_client = plaid.ApiClient(self.configuration)
        self.client = plaid_api.PlaidApi(self.api_client)

    def make_account(self, link_data: LinkData) -> UserData:
        exchange_request = ItemPublicTokenExchangeRequest(
            public_token=link_data.public_token
        )

        exchange_response = self.client.item_public_token_exchange(
            exchange_request)
        user_data = UserData()
        user_data.email = link_data.email

        access_token = exchange_response['access_token']

        user_data.access_tokens.update(
            {link_data.institution['id']: access_token})
        user_data.bank_ids.append(link_data.institution['id'])
        user_data.banks.append(link_data.institution['name'])
        user_data.account_ids[link_data.institution['id']] = [
        ] if user_data.account_ids[link_data.institution['id']] is None else user_data.account_ids[link_data.institution['id']]
        user_data.bank_account_tokens[link_data.institution['id']] = {
        } if user_data.bank_account_tokens[link_data.institution['id']] is None else user_data.bank_account_tokens[link_data.institution['id']]
        for account_id in link_data.accounts:
            user_data.account_ids[link_data.institution['id']].append(
                account_id)
            request = ProcessorStripeBankAccountTokenCreateRequest(
                access_token=access_token,
                account_id=account_id,
            )
            stripe_response = self.client.processor_stripe_bank_account_token_create(
                request)
            bank_account_token = stripe_response['stripe_bank_account_token']
            user_data.bank_account_tokens[link_data.institution['id']].update(
                account_id, bank_account_token)

        return user_data

    def update_account(self, link_data: LinkData, user: UserData) -> UserData:
        exchange_request = ItemPublicTokenExchangeRequest(
            public_token=link_data.public_token
        )

        exchange_response = self.client.item_public_token_exchange(
            exchange_request)
        user_data = user

        access_token = exchange_response['access_token']

        user_data.access_tokens.update(
            {link_data.institution['id']: access_token})
        user_data.bank_ids.append(link_data.institution['id'])
        user_data.banks.append(link_data.institution['name'])
        user_data.account_ids[link_data.institution['id']] = [
        ] if user_data.account_ids[link_data.institution['id']] is None else user_data.account_ids[link_data.institution['id']]
        user_data.bank_account_tokens[link_data.institution['id']] = {
        } if user_data.bank_account_tokens[link_data.institution['id']] is None else user_data.bank_account_tokens[link_data.institution['id']]
        for account_id in link_data.accounts:
            user_data.account_ids[link_data.institution['id']].append(
                account_id)
            request = ProcessorStripeBankAccountTokenCreateRequest(
                access_token=access_token,
                account_id=account_id,
            )
            stripe_response = self.client.processor_stripe_bank_account_token_create(
                request)
            bank_account_token = stripe_response['stripe_bank_account_token']
            user_data.bank_account_tokens[link_data.institution['id']].update(
                account_id, bank_account_token)

        return user_data

    def get_account_transactions(self, user: UserData) -> list[dict]:
        transactions = []

        for bank in user.bank_ids:
            for user_id in user.account_ids[bank]:
                transactions += self.get_transactions(user, bank, user_id)

        return transactions

    def get_transactions(self, user: UserData, bank_id: str, account_id: str):
        request = TransactionsSyncRequest(
            access_token=user.access_tokens[bank_id],
            account_ids=[account_id],
        )
        response = self.client.transactions_sync(request)
        return response['transactions']
