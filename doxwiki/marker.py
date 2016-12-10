import mistune
import re
import copy
from mistune import Renderer, InlineGrammar, InlineLexer
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html


class WikiLinkInlineLexer(InlineLexer):
    def enable_wiki_link(self):
        # add wiki_link rules
        self.rules.wiki_link = re.compile(
            r'\[\['                   # [[
            r'([\s\S]+?\|[\s\S]+?)'   # Page 2|Page 2
            r'\]\](?!\])'             # ]]
        )

        # Add wiki_link parser to default rules
        # you can insert it some place you like
        # but place matters, maybe 3 is not good
        self.default_rules.insert(3, 'wiki_link')

    def output_wiki_link(self, m):
        text = m.group(1)
        alt, link = text.split('|')
        # you can create an custom render
        # you can also r{}urn the html if you like
        return '<a href="{}">{}</a>'.format(link, alt)


class MetaParseException(Exception):
    pass


class HighlightRenderer(mistune.Renderer):
    """
    Using pygments on code blocks.
    """
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)


class Marker:
    """
    Takes in text, and marks it up.
    """
    def __init__(self):
        self.renderer = HighlightRenderer()
        self.inline = WikiLinkInlineLexer(self.renderer)
        self.inline.enable_wiki_link()
        self.markdown = mistune.Markdown(renderer=self.renderer, inline=self.inline)

    def to_html(self, text):
        marked = self.markdown(text)
        return marked

if __name__ == '__main__':
    a = Marker().to_html("[[google-hey]]")
    print(a)
