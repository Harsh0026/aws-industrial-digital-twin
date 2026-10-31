import json
import random
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


def main():
    inventory_path = Path(__file__).resolve().parent / "machines.json"
    inventory = json.loads(inventory_path.read_text(encoding="utf-8"))

    for machine in inventory["machines"]:
        event = {
            "schema_version": 1,
            "event_id": str(uuid4()),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "site_id": inventory["site_id"],
            "line_id": inventory["line_id"],
            "machine_id": machine["machine_id"],
            "machine_type": machine["machine_type"],
            "operating_state": "running",
            "measurements": {
                "temperature_c": round(random.uniform(40, 60), 2),
                "vibration_mm_s": round(random.uniform(1, 3), 2),
                "rpm": random.randint(1400, 1500),
            },
        }
        print(json.dumps(event), flush=True)


if __name__ == "__main__":
    main()
