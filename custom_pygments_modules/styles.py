# encoding: utf-8
""" custom cheat sheat stylesheet.  """
from pygments.style import Style
from pygments.token import (
    Comment,
    Error,
    Generic,
    Keyword,
    Literal,
    Name,
    Number,
    Operator,
    Other,
    Punctuation,
    String,
    Text,
    Whitespace,
)


class Xoria(Style):

    background_color = "#272822"
    highlight_color = "#49483e"

    styles = {
        # No corresponding class for the following:
        Text:                      "#eee",
        Whitespace:                "",
        Error:                     "#c33 underline",
        Other:                     "",

        Comment:                   "#808080",
        Comment.Multiline:         "",
        Comment.Preproc:           "",
        Comment.Single:            "",
        Comment.Special:           "",

        Keyword:                   "#87afd7",  # blue (for, if, try)
        Keyword.Constant:          "",
        Keyword.Declaration:       "",
        Keyword.Namespace:         "#afd787",  # imports (import, from)
        Keyword.Pseudo:            "",
        Keyword.Reserved:          "",
        Keyword.Type:              "",

        Operator:                  "#bbb",
        Operator.Word:             "",

        Punctuation:               "#f8f8f2",

        Name:                      "#f8f8f2",
        Name.Attribute:            "#a6e22e",
        Name.Builtin:              "#d7afd7",  # functions (range, etc..)
        Name.Builtin.Pseudo:       "",
        Name.Class:                "#a6e22e",
        Name.Constant:             "#66d9ef",
        Name.Decorator:            "#a6e22e",
        Name.Entity:               "",
        Name.Exception:            "#a6e22e",
        Name.Function:             "#d7afd7",  # custom function names
        Name.Property:             "",
        Name.Label:                "",
        Name.Namespace:            "",
        Name.Other:                "#a6e22e",
        Name.Tag:                  "#f92672",
        Name.Variable:             "",
        Name.Variable.Class:       "",
        Name.Variable.Global:      "",
        Name.Variable.Instance:    "",

        Number:                    "#d7af87",
        Number.Float:              "",
        Number.Hex:                "",
        Number.Integer:            "",
        Number.Integer.Long:       "",
        Number.Oct:                "",

        Literal:                   "#ae81ff",
        Literal.Date:              "#e6db74",

        String:                    "#ffa",  # yellow-ish
        String.Backtick:           "",
        String.Char:               "",
        String.Doc:                "",
        String.Single:             "",
        String.Double:             "",
        String.Escape:             "#eaa",   # red-ish
        String.Heredoc:            "",
        String.Interpol:           "#ad8",
        String.Other:              "",
        String.Regex:              "",
        String.Symbol:             "",

        Generic:                   "",
        Generic.Deleted:           "#f92672",
        Generic.Emph:              "italic",
        Generic.Error:             "#c33",
        Generic.Heading:           "#d5c",
        Generic.Inserted:          "#a6e22e",
        Generic.Output:            "",
        Generic.Prompt:            "",
        Generic.Strong:            "bold",
        Generic.Subheading:        "#d5c",
        Generic.Traceback:         "#aaa",
    }
