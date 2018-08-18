#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Helper utilities to format javascript snippets.
"""
import re

ALWAYS = 'always'
NEVER = 'never'


def get_option(snip, option, default=None):
    return snip.opt('g:ultisnips_javascript["{}"]'.format(option), default)


def semi(snip):
    option = get_option(snip, 'semi', ALWAYS)

    if option == NEVER:
        ret = ''
    elif option == ALWAYS:
        ret = ';'
    else:
        ret = ';'
    return ret


def space_before_function_paren(snip):
    option = get_option(snip, 'space-before-function-paren', NEVER)

    if option == NEVER:
        ret = ''
    elif option == ALWAYS:
        ret = ' '
    else:
        ret = ''
    return ret


def keyword_spacing(snip):
    option = get_option(snip, 'keyword-spacing', ALWAYS)

    if option == NEVER:
        ret = ''
    elif option == ALWAYS:
        ret = ' '
    else:
        ret = ''
    return ret

def comment(snip, COMMENT_SIGN):
    lines = snip.v.text.split('\n')[:-1]
    first_line = lines[0]
    spaces = ''

    # Get the first non-empty line
    for idx, l in enumerate(lines):
        if l.strip() != '':
            first_line = lines[idx]
            sp = re.search(r'\s+', first_line)
            spaces = sp.group()

    if first_line.strip().startswith(COMMENT_SIGN):
        result = [f'{line.replace(COMMENT_SIGN, "", 1)}' if line.strip() else line for line in lines]
    else:
        result = [f'{spaces}{COMMENT_SIGN}{line[len(spaces):]}' if line.strip() else line for line in lines ]

    if result:
        return '\n'.join(result)
    else:
        return ''

