#!/usr/bin/env python
# coding: utf-8
from setuptools import setup
from setuptools import find_packages


FILTERS = {
    'md_heading': 'filters:MarkdownHeadingText',
    'md_code_indent': 'filters:MarkdownCodeFenceIndent',
}

STYLES = {
    'xoria256': 'styles:Xoria',
    'onedark': 'styles:OneDark',
}


def get_packages():
    """ List of (sub)packages to install. """
    return find_packages('.', include=('custom_pygments_modules', ))


def get_requirements(filename):
    """ Read requirements from file. """
    with open(filename, 'r') as reqfile:
        for req_line in reqfile.readlines():
            req_line = req_line.strip()
            if req_line:
                yield req_line


def get_textfile(filename):
    """ Get contents from a text file. """
    with open(filename, 'rU') as fh:
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
            'pygments.filters': [
                '{0} = custom_pygments_modules.{1}'.format(k, v)
                for k, v in FILTERS.items()],
            'pygments.formatters': [
                # 'foo = custom_pygments_modules.formatters:TerminalFormatter',
            ],
            'pygments.lexers': [],
            'pygments.styles': [
                '{0} = custom_pygments_modules.{1}'.format(k, v)
                for k, v in STYLES.items()],
        },
    )


if __name__ == "__main__":
    setup_package()
