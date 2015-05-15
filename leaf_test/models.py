from leaf.models import Page


class TestPageInline():
    pass


class TestInline():
    pass


class TestInline2():
    pass


class PageClass(Page):
    identifier = 'example-page'
    template = 'example.html'


class PageClass2(Page):
    admin_page_inline = TestPageInline
    admin_inlines = [TestInline, 'leaf_test.models.TestInline2']
    identifier = 'example-page2'
    template = 'example.html'


class PageClass3(Page):
    admin_page_inline = 'leaf_test.models.TestPageInline'
    identifier = 'example-page3'
    template = 'example.html'
