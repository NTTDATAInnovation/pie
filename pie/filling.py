from pie.config import API_KEY
from langchain.llms import OpenAI

####################
# LLM
####################

LLM = OpenAI(
    openai_api_key=API_KEY,
    verbose=True,
    model="text-davinci-003",
    temperature=0.1,  # default: .7
    cache=None,
    callbacks=None,
    callback_manager=None,
    tags=None,
    metadata=None,
    client=None,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    n=1,
    best_of=1,
    # model_kwargs = dict,
    openai_api_base=None,
    openai_organization=None,
    openai_proxy=None,
    batch_size=20,
    request_timeout=None,
    # logit_bias = dict,
    max_retries=6,
    streaming=False,
    # allowed_special = set(),
    disallowed_special="all",
    tiktoken_model_name=None,
)
