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

    # Work in progress

    background_color = "#272822"
    highlight_color = "#49483e"

    styles = {
        # No corresponding class for the following:
        Text:                      "#eee",
        Whitespace:                "",
        Error:                     "#c33 underline",
        Other:                     "",

        Generic:                   "",
        Generic.Deleted:           "#f92672",
        Generic.Emph:              "italic",
        Generic.Error:             "#c33",
        Generic.Heading:           "#d99 underline",
        Generic.Inserted:          "#a6e22e",
        Generic.Output:            "",
        Generic.Prompt:            "",
        Generic.Strong:            "bold",
        Generic.Subheading:        "#d99",
        Generic.Traceback:         "#aaa",

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

        Literal:                   "#ae81ff",
        Literal.Date:              "#e6db74",

        Number:                    "#d7af87",
        Number.Float:              "",
        Number.Hex:                "",
        Number.Integer:            "",
        Number.Integer.Long:       "",
        Number.Oct:                "",

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
        String.Regex:              "#ffe",   # brighter
        String.Symbol:             "",
    }


class OneDarkVim(Style):

    # Work in progress

    background_color = "#1c1c1c"
    highlight_color = "#a626a4 bg:#fafafa"

    styles = {
        Error:                       "#e45649",
        # Text.Whitespace:             "#bbb",

        Generic.Deleted:             "#e06c75",
        Generic.Inserted:            "#98c379",
        Generic.Emph:                "bold",
        Generic.Error:               "#be5046",
        Generic.Heading:             "#e45649",
        Generic.Subheading:          "#e45649",
        Generic.Output:              "#888",  # ?
        Generic.Prompt:              "#555",  # ?
        Generic.Strong:              "bold",
        Generic.Traceback:           "#a00",  # ?

        Comment:                     "#5c6370",

        Keyword:                     "#e45649",
        Keyword.Constant:            "#87d787",
        Keyword.Declaration:         "#a626a4",
        Keyword.Pseudo:              "#986801",
        Keyword.Reserved:            "#0184bc",
        Keyword.Type:                "#c18401",

        Operator:                    "#526fff",  # or #a626a4

        Name.Attribute:              "#e2964a",
        Name.Builtin.Pseudo:         "#999",
        Name.Builtin:                "#4fb6c3",
        Name.Class:                  "#e2964a bold",
        Name.Constant:               "#4fb6be",
        Name.Decorator:              "#4fb6be",
        Name.Entity:                 "#e2964a",  # ?
        Name.Exception:              "#a626a4",
        Name.Function:               "#52a5eb bold",
        Name.Namespace:              "#a626a4",
        Name.Tag:                    "#de5442",  # ?
        Name.Variable:               "#de5442",  # ?
        Name.Variable.Class:         "#008080",
        Name.Variable.Global:        "#008080",
        Name.Variable.Instance:      "#008080",

        Literal.Number:              "#986801",
        Literal.Number.Float:        "#986801",
        Literal.Number.Hex:          "#986801",
        Literal.Number.Integer.Long: "#986801",
        Literal.Number.Integer:      "#986801",
        Literal.Number.Oct:          "#986801",

        Literal.String:              "#87d787",
        Literal.String.Backtick:     "#87d787",
        Literal.String.Char:         "#87d787",
        Literal.String.Doc:          "#87d787",
        Literal.String.Double:       "#87d787",
        Literal.String.Escape:       "#87d787",
        Literal.String.Heredoc:      "#87d787",
        Literal.String.Interpol:     "#87d787",
        Literal.String.Other:        "#87d787",
        Literal.String.Regex:        "#0184bc",
        Literal.String.Single:       "#87d787",
        Literal.String.Symbol:       "#0184bc",  # ?
    }


OneDark = OneDarkVim
