from typing import Dict, List
from Page import Page
from Option import Option

"""
Book does the following
holds the current stats and page number
"""


class Book:
    def __init__(self):
        self.pages:List[Page] = []
        self.stats:Dict[str, int] = dict()
        self.stats["page"] = 0

    def get_text(self) -> str:
        return self.current_page().get_text(self.stats)

    def add_page(self, page, page_number):
        self.pages.append(page)
        self.pages.insert(page_number, page)

    def set_pages(self, pages: List[Page]):
        page_count = 0
        for page in pages:
            self.add_page(page, page_count)
            page_count += 1


    def apply_option(self, option:Option):
        self.stats = option.action(self.stats)

    def get_valid_options(self) -> List[Option]:
        options = []
        for option in self.current_page()._options:
            if (option.predicate(self.stats)):
                options.append(option)
        return options

    def current_page(self) -> Page:
        return self.pages[self.stats["page"]]
