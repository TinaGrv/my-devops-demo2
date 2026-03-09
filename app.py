"""Tiny demo app used for CI/CD practice."""


def get_messages():
    return [
        "Hello, DevOps!",
        "Full loop: code -> Git -> CI -> Docker.",
    ]


def main():
    for message in get_messages():
        print(message)


if __name__ == "__main__":
    main()
