from langchain.text_splitter import RecursiveCharacterTextSplitter


def ready_splitter(
    chunk_size=500,
    chunk_overlap=0,
    length_function=len,
    is_separator_regex=[". ", ".. ", "? "],
    **kwargs,
):
    """A function to ready a splitter for use in the pie.
    This analogy is really falling apart."""

    return RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=length_function,
        is_separator_regex=is_separator_regex,
        **kwargs,
    )
