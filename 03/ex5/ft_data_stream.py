from collections.abc import Iterator
import random

PLAYERS = [
    "alice",
    "bob",
    "charlie",
    "dylan",
]

ACTIONS = [
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "climb",
    "swim",
    "release",
    "use",
]

def gen_event() -> Iterator[tuple[str, str]]:
    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (name, action)

def consume_event(events: list[tuple[str, str]]) -> Iterator[tuple[str, str]]:
    while len(events) > 0:
        index = random.randint(0, len(events) - 1)
        event = events.pop(index)
        yield event

def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_generator = gen_event()

    for i in range(1000):
        
        player, action = next(event_generator)
        print(f"Event {i}: Player {player} did action {action}")

    events: list[tuple[str, str]] = []

    for i in range(10):
        events.append(next(event_generator))

    print(f"Built list of 10 events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")

if __name__ == "__main__":
    main()
