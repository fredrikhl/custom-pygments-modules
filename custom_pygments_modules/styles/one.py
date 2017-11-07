# encoding: utf-8
""" Pygments port of the default style for the Atom text editor.  """
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
    # Other,
    # Punctuation,
    # Text,
)


class OneDark(Style):
    """ onedark style. """

    # default_style = ''

    background_color = "#1c1c1c"
    highlight_color = "#a626a4 bg:#fafafa"

    styles = {
        # Text:                          '',
        # Text.Whitespace:               '',
        # Escape:                        '',
        Error:                         '#e45649',
        # Other:                         '',

        Keyword:                       '#e45649',
        Keyword.Constant:              '#87d787',
        Keyword.Declaration:           '#a626a4',
        # Keyword.Namespace:             '',
        Keyword.Pseudo:                '#986801',
        Keyword.Reserved:              '#0184bc',
        Keyword.Type:                  '#c18401',

        # Name:                          '',
        Name.Attribute:                '#e2964a',
        Name.Builtin:                  '#4fb6c3',
        Name.Builtin.Pseudo:           '#999',
        Name.Class:                    '#e2964a bold',
        Name.Constant:                 '#4fb6be',
        Name.Decorator:                '#4fb6be',
        Name.Entity:                   '#e2964a',  # ?
        Name.Exception:                '#a626a4',
        Name.Function:                 '#52a5eb bold',
        # Name.Function.Magic:           '',
        # Name.Property:                 '',
        # Name.Label:                    '',
        Name.Namespace:                '#a626a4',
        # Name.Other:                    '',
        Name.Tag:                      '#de5442',  # ?
        Name.Variable:                 '#de5442',  # ?
        Name.Variable.Class:           '#008080',
        Name.Variable.Global:          '#008080',
        Name.Variable.Instance:        '#008080',
        # Name.Variable.Magic:           '',

        # Literal:                       '',
        # Literal.Date:                  '',

        Literal.String:                '#87d787',
        # Literal.String.Affix:          '',
        Literal.String.Backtick:       '#87d787',
        Literal.String.Char:           '#87d787',
        # Literal.String.Delimiter:      '',
        Literal.String.Doc:            '#87d787',
        Literal.String.Double:         '#87d787',
        Literal.String.Escape:         '#87d787',
        Literal.String.Heredoc:        '#87d787',
        Literal.String.Interpol:       '#87d787',
        Literal.String.Other:          '#87d787',
        Literal.String.Regex:          '#0184bc',
        Literal.String.Single:         '#87d787',
        Literal.String.Symbol:         '#0184bc',  # ?

        Literal.Number:                '#986801',
        # Literal.Number.Bin:            '',
        Literal.Number.Float:          '#986801',
        Literal.Number.Hex:            '#986801',
        Literal.Number.Integer:        '#986801',
        Literal.Number.Integer.Long:   '#986801',
        Literal.Number.Oct:            '#986801',

        Operator:                      '#526fff',  # or #a626a4
        # Operator.Word:                 '',

        # Punctuation:                   '',

        Comment:                       '#5c6370',
        # Comment.Hashbang:              '',
        # Comment.Multiline:             '',
        # Comment.Preproc:               '',
        # Comment.PreprocFile:           '',
        # Comment.Single:                '',
        # Comment.Special:               '',

        # Generic:                       '',
        Generic.Deleted:               '#e06c75',
        Generic.Emph:                  'bold',
        Generic.Error:                 '#be5046',
        Generic.Heading:               '#e45649',
        Generic.Inserted:              '#98c379',
        Generic.Output:                '#888',  # ?
        Generic.Prompt:                '#555',  # ?
        Generic.Strong:                'bold',
        Generic.Subheading:            '#e45649',
        Generic.Traceback:             '#a00',  # ?
    }
