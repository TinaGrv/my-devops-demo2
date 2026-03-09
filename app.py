"""Tiny demo app used for CI/CD and monitoring practice."""

import argparse
import json
from datetime import datetime, timezone


def get_messages():
    return [
        "Hello, DevOps!",
        "Full loop: code -> Git -> CI -> Docker.",
    ]


def health_check():
    return {
        "status": "ok",
        "service": "my-devops-demo2",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


def log_event(level, event, **fields):
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "level": level,
        "event": event,
        **fields,
    }
    print(json.dumps(payload))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--health", action="store_true", help="print health JSON and exit")
    args = parser.parse_args()

    if args.health:
        print(json.dumps(health_check()))
        return

    log_event("INFO", "app_start")
    for index, message in enumerate(get_messages(), start=1):
        log_event("INFO", "message_printed", message_index=index, message=message)
        print(message)
    log_event("INFO", "app_complete", total_messages=len(get_messages()))


if __name__ == "__main__":
    main()
