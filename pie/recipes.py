from langchain.prompts import PromptTemplate

TAG_LIST = [
    "{{NAME}}",
    "{{EMAIL}}",
    "{{PHONE}}",
    "{{CPR NUMBER}}",
    "{{SCHOOL}}",
    "{{CITY}}",
    "{{STREET}}",
    "{{LOCATION}}",
    "{{DATE-OF-BIRTH}}",
    "{{ZIP CODE}}",
]

TEMPLATE_PROMPT = (
    "Replace the PII (names, locations, phone numbers etc.)"
    + "in the following Danish text with the appropriate PII tag.\n"
    + f"Choose between the following tags: {TAG_LIST}\n"
    + "Return the full text with the PII replaced. \n\n"
)


def ready_template(template=TEMPLATE_PROMPT):
    """A function to ready a template for use in the prompt"""
    return PromptTemplate.from_template(template + "'{input_text}'")
