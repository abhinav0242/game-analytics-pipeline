import json
import random
from faker import Faker

fake = Faker()
events = ["login", "purchase", "logout", "level_up"]
with open("game_logs.json", "w") as f:
    for _ in range(10000):  # Generate 10,000 events
        event = {
            "player_id": fake.uuid4(),  # Unique player ID
            "event_type": random.choice(events),  # Random event
            "timestamp": fake.iso8601(),  # Realistic timestamp
            "value": random.randint(1, 100) if "purchase" in events else None  # Purchase amount
        }
        f.write(json.dumps(event) + "\n")  # JSON Lines format
print("Generated 10,000 game telemetry events in game_logs.json")