import argparse

from greet_anyone.core import greet


def main():
    parser = argparse.ArgumentParser(description="Greet anyone.")
    parser.add_argument("output", type=str, default="Traveler", help="who to greet")
    parser.add_argument("--exited", type=bool, default=False, help="adds a exclamation point at the end")
    args = parser.parse_args()

    print(greet(args.output, args.exited))


if __name__ == "__main__":
    main()
