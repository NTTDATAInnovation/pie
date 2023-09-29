import re
import tqdm


ENT_PATTERN = re.compile(r"\{\w+\s?\w+\}")


def calculate_true_end(ex: dict, start: int, end: int) -> int:
    """Calculate the true end of the entity"""

    next_chars = ex["predicted"][end : end + 3]

    if not next_chars:
        return len(ex["text"])
    else:
        return ex["text"][start:].find(next_chars) + start


def format_predicted_entities(data: list) -> list:
    """Formats the predictions into prodigy format.
    Since the LLMs doesn't give us the indices of the predicted entities,
    we have to calculate them ourselves using the original text"""

    for ex in tqdm(data):
        ex["pred_entities"] = []
        for ent in ENT_PATTERN.finditer(ex["predicted"]):
            start = ent.start()
            end = ent.end()
            ent = ent.group()

            true_end = calculate_true_end(ex, start, end)

            ex["pred_entities"].append(
                {
                    "label": ent,
                    "start": start,
                    "end": true_end,
                    "text": ex["text"][start:true_end],
                }
            )
        yield ex
