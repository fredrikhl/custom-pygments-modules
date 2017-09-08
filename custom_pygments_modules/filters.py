from pygments.util import get_bool_opt
from pygments.token import Name
from pygments.filter import Filter

from pygments.token import (
    Comment,
    Error,
    Generic,
    Keyword,
    Name,
    Number,
    Operator,
    String,
    Token,
    Whitespace,
)


class MarkdownCodeFence(Filter):
    """ Track markdown code fence. """

    def filter(self, lexer, stream):
        # TODO: Implement custom formatter to handle bg-color?
        in_code_fence = False
        for ttype, value in stream:
            # TODO: Check ttype?
            if value == '```':
                in_code_fence = not in_code_fence
            yield ttype, value


class MarkdownHeadingText(Filter):
    """ Fix the markdown heading text token. """

    HEADING_TYPES = [Generic.Heading, Generic.Subheading]

    def filter(self, lexer, stream):
        prev_ttype = None
        prev_value = None
        for ttype, value in stream:
            if (prev_ttype in self.HEADING_TYPES and ttype is Token.Text):
                yield prev_ttype, value
            else:
                yield ttype, value
            prev_ttype, prev_value = ttype, value
