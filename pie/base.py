from pie.recipes import ready_template
from pie.slice import TextSplitter
from pie.filling import LLM
from pie.easy_bake import easy_bake
from pie.toppings import apply_toppings


class Pie:
    def __init__(
        self,
        llm=LLM,
        prompt_template=ready_template(),
        text_splitter=TextSplitter(),
    ):
        self.llm: object = llm
        self.prompt_template: str = prompt_template
        self.text_splitter: object = text_splitter

    @easy_bake
    def bake(self, query: str) -> str:
        chunks: list = self.text_splitter.split_text(query)
        response: str = " ".join([*self._bake(chunks)])
        return apply_toppings(response)  # tasty regex toppings

    def _bake(self, chunks) -> str:
        for chunk in chunks:
            prompt: object = self.prompt_template.format(input_text=chunk)
            yield self.llm.predict(prompt).strip("\n").strip("'")

    def bake_many(self, queries: list, **kwargs) -> list:
        for query in queries:
            yield self.bake(query, **kwargs)
