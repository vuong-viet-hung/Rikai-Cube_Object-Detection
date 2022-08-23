import json
from pathlib import Path


ANNOTATIONS_PATH = Path("annotations.json")


def main() -> None:
    with open(ANNOTATIONS_PATH, "r", encoding="utf-8") as annotations_file:
        annotations = json.load(annotations_file)
        print(annotations[0]["kp-1"])


if __name__ == "__main__":
    main()
