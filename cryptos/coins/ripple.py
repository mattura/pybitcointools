from .bitcoin import BaseCoin
from ..explorers import sochain

'''
NOTE: Ripple addresses use a DIFFERENT base58 dictionary:
https://xrpl.org/base58-encodings.html
'''

class Ripple(BaseCoin):
    coin_symbol = "XRP"
    display_name = "Ripple"
    segwit_supported = False
    magicbyte = 0x00        #as bitcoin
    #script_magicbyte = 5    #as bitcoin
    #to_wif = 0x80           
    #wif_prefix = 0x80
    hd_path = 144
    #explorer = ripple
    #xpriv_prefix = 0x0488ADE4
    #xpub_prefix = 0x0488B21E
    testnet_overrides = {
        'display_name': "Ripple Testnet",
        'coin_symbol': "XRP",
    #    'wif_prefix': 0xef,
    #    'magicbyte': 0x1D25,
    #    'script_magicbyte': 0x1CBA,
    #    'xpriv_prefix': 0x04358394,
    #    'xpub_prefix': 0x043587CF
    }
