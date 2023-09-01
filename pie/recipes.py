from langchain.prompts import PromptTemplate


TAG_LIST = [
    "{{NAME}}",
    "{{EMAIL}}",
    "{{PHONE}}",
    "{{CPR NUMBER}}",
    "{{ORGANIZATION}}",
    "{{SCHOOL}}",
    "{{CITY}}",
    "{{STREET}}",
    "{{LOCATION}}",
    "{{ZIP CODE}}",
]

TEMPLATE_PROMPT = (
    "Replace the PII (names, locations, phone numbers etc.)"
    + "in the following Danish text with the appropriate PII tag.\n"
    + f"Choose only between the following tags: {TAG_LIST}\n"
    + "Text:\n\n"
)

TEMPLTE_PROMPT_ENDING = (
    "\n\nWrite the exact text in full with the PII replaced.\n"
    + "Don't replace pronouns or nouns. "
    + "Do not add or remove any other text.\n"
    + "Text with PII replaced:\n\n'"
)


def ready_template(template=TEMPLATE_PROMPT, template_ending=TEMPLTE_PROMPT_ENDING):
    """A function to ready a template for use in the prompt"""
    return PromptTemplate.from_template(template + "'{input_text}'" + template_ending)
