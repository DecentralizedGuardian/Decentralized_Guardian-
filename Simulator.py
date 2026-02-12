import random
import time
import json
from datetime import datetime

class SensorSimulator:
    def __init__(self, node_id="guardian_01"):
        self.node_id = node_id

    def read_water(self):
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "node_id": self.node_id,
            "ph": round(random.uniform(6.5, 8.5), 2),
            "tds": random.randint(150, 450),
            "contaminant": random.choices([0, 1], weights=[0.97, 0.03])[0]
        }

    def run(self):
        while True:
            data = self.read_water()
            print(json.dumps(data))
            time.sleep(5)

if __name__ == "__main__":
    sim = SensorSimulator()
    sim.run()
