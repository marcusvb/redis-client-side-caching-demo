import threading
from redis import Redis

r = Redis(host="localhost", port=6379, decode_responses=True)


def listen_for_foo_changes():
    pubsub = r.pubsub()

    # Listen to all SET events in DB 0
    pubsub.subscribe("__keyevent@0__:set")

    print("Listening for key updates...")

    for msg in pubsub.listen():
        # Ignore non-message events (subscribe confirmations, etc.)
        if msg["type"] != "message":
            continue

        key = msg["data"]  # this is the key name (e.g. "foo")

        print("MESSAGE [",  msg , "]")
        # client-side filtering
        if key == "foo":
            value = r.get("foo")
            print(f"[UPDATE] foo = {value}")


if __name__ == "__main__":
    t = threading.Thread(target=listen_for_foo_changes, daemon=True)
    t.start()

    # keep main thread alive
    while True:
        pass
