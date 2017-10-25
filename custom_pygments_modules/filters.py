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
    Text,
    Token,
    Whitespace,
)


class MarkdownCodeFence(Filter):
    """ Track markdown code fence state. """

    def process_code(self, ttype, item, lineno, is_newline):
        yield ttype, item

    def enter_code_fence(self, ttype, value):
        return ttype, value

    def exit_code_fence(self, ttype, value):
        return ttype, value

    def filter(self, lexer, stream):
        in_code_fence = False
        is_newline = False
        lineno = 0

        for ttype, value in stream:
            if ttype == String and value.rstrip() == '```':
                in_code_fence = not in_code_fence

                if in_code_fence:
                    yield self.enter_code_fence(ttype, value)
                    is_newline = value.endswith('\n')
                    lineno = bool(is_newline)
                else:
                    yield self.exit_code_fence(ttype, value)

            elif in_code_fence:
                for item in value.splitlines(True) or [value, ]:
                    for sub_ttype, sub_item in self.process_code(
                            ttype, item, lineno, is_newline):
                        yield sub_ttype, sub_item
                    is_newline = item.endswith('\n')
                    lineno += bool(is_newline)
            else:
                yield ttype, value


class MarkdownCodeFenceIndent(MarkdownCodeFence):
    """ Indent code fence contents

    Also adds tokens to code fence, code fence type hints, and indents.
    """

    def enter_code_fence(self, ttype, item):
        # return Keyword.Namespace, item
        return String.Affix, ''

    def exit_code_fence(self, ttype, item):
        # return Keyword.Namespace, item
        return String.Affix, ''

    def process_code(self, ttype, item, lineno, is_newline):
        if ttype == String and item and lineno == 0:
            # type hint
            yield Comment, '    '
            yield Keyword.Namespace, item

        else:
            if is_newline and lineno > 0:
                # yield Comment, ' {:4d}'.format(lineno)
                yield Comment, '    '
                # pass
            yield ttype, item


class MarkdownHeadingText(Filter):
    """ Fix the markdown heading text token. """

    HEADING_TYPES = [Generic.Heading, Generic.Subheading]

    def filter(self, lexer, stream):
        prev_ttype = None
        prev_value = None
        for ttype, value in stream:
            if (prev_ttype in self.HEADING_TYPES and ttype is Token.Text):
                new_value = value.lstrip(' ')
                space = len(value) - len(new_value)
                if space:
                    yield Whitespace, ' ' * space
                yield prev_ttype, new_value
            elif ttype in self.HEADING_TYPES:
                # yield Comment, value
                # yield Token.Operator, value
                yield Token.Punctuation, value
            else:
                yield ttype, value
            prev_ttype, prev_value = ttype, value
