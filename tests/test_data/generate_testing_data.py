import json
from pathlib import Path
from itertools import chain


def load_test_data(dir="data/test_data/", format="json") -> list:
    """Load test data from directory"""
    for file in Path(dir).glob(f"*.{format}"):
        with open(file) as f:
            yield json.load(f)["annotations"]


def build_entity_map() -> dict:
    """Map entities to their respective tags"""
    monty = {
        ("{PER}",): "{NAME}",
        ("{LOC}", "{STREET}", "{CITY}"): "{LOCATION}",
        ("{ORG}", "{SCHOOL}"): "{ORGANIZATION}",
        ("{CPR}",): "{CPR NUMBER}",
        ("{EMAIL}",): "{EMAIL}",
        ("{PHONE}",): "{PHONE NUMBER}",
        ("{LINK}",): "{LINK}",
        ("{DATE}",): "{DATE-OF-BIRTH}",
        ("{ZIP CODE}",): "{ZIP CODE}",
    }

    working_monty = {}
    for k, v in monty.items():
        for key in k:
            working_monty[key] = v

    return working_monty


def reformat_to_prodigy(data, working_monty) -> list:
    """Reformat data to prodigy format"""
    new_data = []
    for example in data:
        inner = []

        if example[1]["entities"]:
            for entity in example[1]["entities"]:
                start, end, label = entity
                inner.append(
                    {
                        "label": working_monty[label],
                        "start": start,
                        "end": end,
                    }
                )

        new_data.append({"text": example[0].strip("\r").strip(), "entities": inner})

    return new_data


def remove_duplicates(data) -> list:
    new_fmt = []
    temp_texts = []
    for example in data:
        if example["text"] not in temp_texts:
            new_fmt.append(example)
            temp_texts.append(example["text"])

    return new_fmt


data = list(chain.from_iterable(load_test_data()))
entity_map = build_entity_map()
new_data = reformat_to_prodigy(data, entity_map)
new_data = remove_duplicates(new_data)


with Path("data/gold_data.json").open("w", encoding="utf8") as f:
    json.dump(data, f, ensure_ascii=False)
