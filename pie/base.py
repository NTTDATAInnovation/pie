from typing import Iterable, Generator
from langchain.llms.base import BaseLLM
from langchain.prompts import PromptTemplate
from loguru import logger

from pie.recipes import make_template, EXAMPLES, TAG_LIST
from pie.slice import TextSplitter
from pie.filling import LLM
from pie.easy_bake import easy_bake
from pie.toppings import apply_toppings


class Pie:
    def __init__(
        self,
        llm: BaseLLM = LLM,
        prompt_template=make_template(),
        text_splitter=TextSplitter(),
    ):
        self.llm: BaseLLM = llm
        self.template: PromptTemplate = prompt_template
        self.text_splitter: TextSplitter = text_splitter
        self.examples = "\n\n".join(EXAMPLES)

    @easy_bake
    def bake(self, query: str) -> str:
        # chunks: list = self.text_splitter.split_text(query)
        # response: str = " ".join([*self._bake(chunks)])
        response: str = self._bake(query)
        return apply_toppings(response)  # tasty regex toppings

    def _bake(self, query: str) -> str:
        # for chunk in chunks:
        prompt: str = self.template.format(
            tag_list=TAG_LIST,
            examples=self.examples,
            input_text=query,
        )
        logger.debug(prompt)
        pred = self.llm.predict(prompt).strip("\n").strip("'")
        logger.debug(pred)
        return pred

    def bake_many(self, queries: Iterable, **kwargs) -> Generator[str, None, None]:
        for query in queries:
            yield self.bake(query, **kwargs)
