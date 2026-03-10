import datetime
from server.mitre_mapping import MITRE_TECHNIQUES

def log_event(event_type, details):

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    mitre = MITRE_TECHNIQUES.get(event_type, {})

    entry = {
        "time": timestamp,
        "event": event_type,
        "details": details,
        "mitre_id": mitre.get("id"),
        "mitre_name": mitre.get("name")
    }

    print(entry)

    with open("logs/events.log", "a") as f:
        f.write(str(entry) + "\n")