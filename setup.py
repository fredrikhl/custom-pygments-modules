#!/usr/bin/env python
# coding: utf-8
from setuptools import setup
from setuptools import find_packages


FILTERS = {
    'md_heading': 'filters:MarkdownHeadingText',
    'md_code_indent': 'filters:MarkdownCodeFenceIndent',
}

FORMATTERS = {}

LEXERS = {
    'markdown': 'markdown_lexer:CustomMarkdownLexer',
}

STYLES = {
    'empty': 'styles.empty:Empty',
    'onedark': 'styles.one:OneDark',
    'tests': 'styles:Test',
    'xoria256': 'styles.xoria:Xoria256',
}


def dict_to_entry_points(d):
    return [
        '{0} = custom_pygments_modules.{1}'.format(k, v)
        for k, v in sorted(d.items())],


def get_packages():
    """ List of (sub)packages to install. """
    return find_packages('.', include=('custom_pygments_modules',
                                       'custom_pygments_modules.styles'))


def get_requirements(filename):
    """ Read requirements from file. """
    with open(filename, 'r') as reqfile:
        for req_line in reqfile.readlines():
            req_line = req_line.strip()
            if req_line:
                yield req_line


def get_textfile(filename):
    """ Get contents from a text file. """
    with open(filename, 'r') as fh:
        return fh.read()


def setup_package():
    """ build and run setup. """

    setup(
        name='custom-pygments-modules',
        description='My personal styles, formatters, etc... goes here',
        long_description=get_textfile('README.md'),
        author='fredrikhl',
        url='https://github.com/fredrikhl/custom-pygments-modules',
        use_scm_version=True,
        setup_requires=['setuptools_scm'],
        install_requires=list(get_requirements('requirements.txt')),
        packages=get_packages(),
        entry_points={
            'pygments.filters': dict_to_entry_points(FILTERS),
            'pygments.formatters': dict_to_entry_points(FORMATTERS),
            'pygments.lexers': dict_to_entry_points(LEXERS),
            'pygments.styles': dict_to_entry_points(STYLES),
        },
    )


if __name__ == "__main__":
    setup_package()
