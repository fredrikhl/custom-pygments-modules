# encoding: utf-8
""" custom cheat sheat stylesheet.  """
from pygments.style import Style
from pygments.token import (
    Literal,
    Punctuation,
    Text,
)


class Test(Style):
    """ A minimal style for testing. """

    background_color = "#000000"
    highlight_color = "#ffffff"

    styles = {
        Text: "#0000ff",
        Punctuation.Indicator: "#ff0000",
        Literal.Scalar.Plain: "#00ff00",
    }
