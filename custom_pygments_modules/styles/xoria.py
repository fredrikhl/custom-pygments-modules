# encoding: utf-8
""" Pygments port of the xoria256 colorscheme for VIM.

See: http://www.vim.org/scripts/script.php?script_id=2140
"""
from pygments.style import Style
from pygments.token import (
    Comment,
    # Escape,
    Error,
    Generic,
    Keyword,
    Literal,
    Name,
    Operator,
    Other,
    Punctuation,
    Text,
)


class Xoria256(Style):
    """ pygments xoria256 style. """

    background_color = '#272822'
    highlight_color = '#49483e'

    styles = {
        Text:                          '#eee',
        Text.Whitespace:               '',
        # Escape:                        '',
        Error:                         '#c33 underline',
        Other:                         '',

        Keyword:                       '#87afd7',  # blue (for, if, try)
        Keyword.Constant:              '',
        Keyword.Declaration:           '',
        Keyword.Namespace:             '#afd787',  # imports (import, from)
        Keyword.Pseudo:                '',
        Keyword.Reserved:              '',
        Keyword.Type:                  '',

        Name:                          '#f8f8f2',
        Name.Attribute:                '#a6e22e',
        Name.Builtin:                  '#d7afd7',  # functions (range, etc..)
        Name.Builtin.Pseudo:           '',
        Name.Class:                    '#a6e22e',
        Name.Constant:                 '#66d9ef',
        Name.Decorator:                '#a6e22e',
        Name.Entity:                   '',
        Name.Exception:                '#a6e22e',
        Name.Function:                 '#d7afd7',  # custom function names
        # Name.Function.Magic:           '',
        Name.Property:                 '',
        Name.Label:                    '',
        Name.Namespace:                '',
        Name.Other:                    '#a6e22e',
        Name.Tag:                      '#f92672',
        Name.Variable:                 '',
        Name.Variable.Class:           '',
        Name.Variable.Global:          '',
        Name.Variable.Instance:        '',
        # Name.Variable.Magic:           '',

        Literal:                       '#ae81ff',
        Literal.Date:                  '#e6db74',

        Literal.String:                '#ffa',  # yellow-ish
        # Literal.String.Affix:          '',
        Literal.String.Backtick:       '',
        Literal.String.Char:           '',
        Literal.String.Delimiter:      '',
        Literal.String.Doc:            '',
        Literal.String.Double:         '',
        Literal.String.Escape:         '#eaa',   # red-ish
        Literal.String.Heredoc:        '',
        Literal.String.Interpol:       '#ad8',
        Literal.String.Other:          '',
        Literal.String.Regex:          '#ffe',   # brighter
        Literal.String.Single:         '',
        Literal.String.Symbol:         '',

        Literal.Number:                '#d7af87',
        Literal.Number.Bin:            '',
        Literal.Number.Float:          '',
        Literal.Number.Hex:            '',
        Literal.Number.Integer:        '',
        Literal.Number.Integer.Long:   '',
        Literal.Number.Oct:            '',

        Operator:                      '#bbb',
        Operator.Word:                 '',

        Punctuation:                   '#f8f8f2',

        Comment:                       '#808080',
        # Comment.Hashbang:              '',
        Comment.Multiline:             '',
        Comment.Preproc:               '',
        # Comment.PreprocFile:           '',
        Comment.Single:                '',
        Comment.Special:               '',

        Generic:                       '',
        Generic.Deleted:               '#f92672',
        Generic.Emph:                  'italic',
        Generic.Error:                 '#c33',
        Generic.Heading:               '#d99 underline',
        Generic.Inserted:              '#a6e22e',
        Generic.Output:                '',
        Generic.Prompt:                '',
        Generic.Strong:                'bold',
        Generic.Subheading:            '#d99',
        Generic.Traceback:             '#aaa',
    }
