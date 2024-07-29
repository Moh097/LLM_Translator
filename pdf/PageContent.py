class PageContent:
    def __init__(self, header: str, footer: str, page_number: int, paragraphs: list):
        """
        Represents the content of a PDF page.

        :param header: The header text of the page.
        :param footer: The footer text of the page.
        :param page_number: The page number.
        :param paragraphs: A list of paragraphs in the page.
        """
        self.header = header
        self.footer = footer
        self.page_number = page_number
        self.paragraphs = paragraphs
