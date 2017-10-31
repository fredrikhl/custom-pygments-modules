# encoding: utf-8
""" custom lexers for pygments. """

from pygments.lexer import do_insertions
from pygments.lexers.markup import MarkdownLexer
from pygments.token import Text, String
from pygments.util import ClassNotFound


class CustomMarkdownLexer(MarkdownLexer):
    """ Bugfix for pygments issue #1389. """

    def _handle_codeblock(self, match):
        """
        match args: 1:backticks, 2:lang_name, 3:newline, 4:code, 5:backticks
        """
        from pygments.lexers import get_lexer_by_name

        # section header
        yield match.start(1), String, match.group(1)
        yield match.start(2), String, match.group(2)
        yield match.start(3), Text, match.group(3)

        # lookup lexer if wanted and existing
        lexer = None
        if self.handlecodeblocks:
            try:
                lexer = get_lexer_by_name(match.group(2).strip())
            except ClassNotFound:
                pass
        code = match.group(4)

        # no lexer for this language. handle it like it was a code block
        if lexer is None:
            yield match.start(4), String, code
        else:
            for item in do_insertions([], lexer.get_tokens_unprocessed(code)):
                yield item

        yield match.start(5), String, match.group(5)
