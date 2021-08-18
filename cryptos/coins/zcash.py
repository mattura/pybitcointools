from .bitcoin import BaseCoin
from ..explorers import sochain


class ZCash(BaseCoin):
    coin_symbol = "ZEC"
    display_name = "ZCash"
    segwit_supported = False
    magicbyte = 0x1CB8
    script_magicbyte = 0x1CBD
    to_wif = 0x80
    hd_path = 133
    explorer = sochain
    xpriv_prefix = 0x0488ADE4
    xpub_prefix = 0x0488B21E
    testnet_overrides = {
        'display_name': "ZCash Testnet",
        'coin_symbol': "ZEC",
        'wif_prefix': 0xef,
        'magicbyte': 0x1D25,
        'script_magicbyte': 0x1CBA,
        'xpriv_prefix': 0x04358394,
        'xpub_prefix': 0x043587CF
    }
