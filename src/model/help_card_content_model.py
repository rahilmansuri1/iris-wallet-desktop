# pylint: disable=line-too-long, too-few-public-methods
"""This module contains the HelpCardContentModel class,
which represents the all models for help card content model.
"""
from __future__ import annotations

from pydantic import BaseModel
from pydantic import HttpUrl


class HelpCardModel(BaseModel):
    """Model for a single help card."""
    title: str
    detail: str
    links: list[HttpUrl]


class HelpCardContentModel(BaseModel):
    """Content for the help cards."""
    card_content: list[HelpCardModel]

    @classmethod
    def create_default(cls):
        """Factory method to create a default instance of HelpCardContentModel"""
        card_content = [
            HelpCardModel(
                title='Why can I get TESTNET Bitcoins?',
                detail='You can get Testnet Bitcoin by using one of the many available faucets. Below are a few linked examples, but you can always find more using a search engine:',
                links=[
                    'https://testnet-faucet.mempool.co/',
                    'https://bitcoinfaucet.uo1.net/',
                    'https://coinfaucet.eu/en/btc-testnet/',
                    'https://testnet-faucet.com/btc-testnet/',
                ],
            ),
            HelpCardModel(
                title="Why do I see outgoing Bitcoin transactions that I didn't authorize?",
                detail='You can get Testnet Bitcoin by using one of the many available faucet, below are few linked examples but you can always find more using a search engine:',
                links=[
                    'https://testnet-faucet.mempool.co/',
                    'https://bitcoinfaucet.uo1.net/',
                    'https://coinfaucet.eu/en/btc-testnet/',
                    'https://testnet-faucet.com/btc-testnet/',
                ],
            ),
        ]
        return cls(card_content=card_content)
