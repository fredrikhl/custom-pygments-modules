# encoding: utf-8
""" Empty base style.

Style cheat sheet
-----------------

* ``[no]bold``
* ``[no]italic``
* ``[no]underline``
* ``bg:`` (transparent background)
* ``bg:#000000``
* ``border:`` (no border)
* ``border:#ffffff``
* ``#ff0000`` (foreground color)
* ``noinherit`` (do not inherit from parent Token)

Multiple styles can be applied, e.g.: '#ffffff bg:#000000 underline'


ANSI-colors
-----------

ANSI colors can be specified by using the special color '#ansi<name>', where
<name> is one of (0-15):

    black, darkred, darkgreen, brown, darkblue, purple, teal,
    lightgray, darkgray, red, green, yellow, blue, fuchsia,
    turquoise, white

"""
from pygments.style import Style
from pygments.token import (
    Comment,
    Escape,
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


class Empty(Style):
    """ Empty, template style class.

    This class contains some of the most common Tokens.
    """

    default_style = ''

    background_color = ''
    highlight_color = ''

    styles = {
        Text:                          '',
        Text.Whitespace:               '',
        Escape:                        '',
        Error:                         '',
        Other:                         '',

        Keyword:                       '',
        Keyword.Constant:              '',
        Keyword.Declaration:           '',
        Keyword.Namespace:             '',
        Keyword.Pseudo:                '',
        Keyword.Reserved:              '',
        Keyword.Type:                  '',

        Name:                          '',
        Name.Attribute:                '',
        Name.Builtin:                  '',
        Name.Builtin.Pseudo:           '',
        Name.Class:                    '',
        Name.Constant:                 '',
        Name.Decorator:                '',
        Name.Entity:                   '',
        Name.Exception:                '',
        Name.Function:                 '',
        Name.Function.Magic:           '',
        Name.Property:                 '',
        Name.Label:                    '',
        Name.Namespace:                '',
        Name.Other:                    '',
        Name.Tag:                      '',
        Name.Variable:                 '',
        Name.Variable.Class:           '',
        Name.Variable.Global:          '',
        Name.Variable.Instance:        '',
        Name.Variable.Magic:           '',

        Literal:                       '',
        Literal.Date:                  '',

        Literal.String:                '',
        Literal.String.Affix:          '',
        Literal.String.Backtick:       '',
        Literal.String.Char:           '',
        Literal.String.Delimiter:      '',
        Literal.String.Doc:            '',
        Literal.String.Double:         '',
        Literal.String.Escape:         '',
        Literal.String.Heredoc:        '',
        Literal.String.Interpol:       '',
        Literal.String.Other:          '',
        Literal.String.Regex:          '',
        Literal.String.Single:         '',
        Literal.String.Symbol:         '',

        Literal.Number:                '',
        Literal.Number.Bin:            '',
        Literal.Number.Float:          '',
        Literal.Number.Hex:            '',
        Literal.Number.Integer:        '',
        Literal.Number.Integer.Long:   '',
        Literal.Number.Oct:            '',

        Operator:                      '',
        Operator.Word:                 '',

        Punctuation:                   '',

        Comment:                       '',
        Comment.Hashbang:              '',
        Comment.Multiline:             '',
        Comment.Preproc:               '',
        Comment.PreprocFile:           '',
        Comment.Single:                '',
        Comment.Special:               '',

        Generic:                       '',
        Generic.Deleted:               '',
        Generic.Emph:                  '',
        Generic.Error:                 '',
        Generic.Heading:               '',
        Generic.Inserted:              '',
        Generic.Output:                '',
        Generic.Prompt:                '',
        Generic.Strong:                '',
        Generic.Subheading:            '',
        Generic.Traceback:             '',
    }
