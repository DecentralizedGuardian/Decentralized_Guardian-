import json
from web3 import Web3

class GuardianLogger:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider("https://rpc.sepolia.org"))

    def log(self, node_id, data):
        data_hash = Web3.keccak(text=json.dumps(data)).hex()
        return {
            "node_id": node_id,
            "data_hash": data_hash,
            "timestamp": self.w3.eth.get_block('latest')['timestamp'],
            "tx_hash": "0x" + "1" * 64,
            "chain": "sepolia (simulated)"
        }
