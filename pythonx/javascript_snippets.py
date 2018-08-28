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

def comment(snip, START="", END=""):
    lines = snip.v.text.split('\n')[:-1]
    first_line = lines[0]
    spaces = ''
    initial_indent = snip._initial_indent

    # Get the first non-empty line
    for idx, l in enumerate(lines):
        if l.strip() != '':
            first_line = lines[idx]
            sp = re.findall(r'^\s+', first_line)
            if len(sp):
                spaces = sp[0]
            break            

    # Uncomment
    if first_line.strip().startswith(START):
        result = [line.replace(START, "", 1).replace(END, "", 1) if line.strip() else line for line in lines]
    else:
        result = [f'{spaces}{START}{line[len(spaces):]}{END}' if line.strip() else line for line in lines ]

    # Remove initial indent
    if result[0] and initial_indent:
        result[0] = result[0].replace(initial_indent, '', 1)

    if result:
        return '\n'.join(result)
    else:
        return ''

def comment_inline(snip, START="/* ", END=" */"):
    text = snip.v.text
    lines = text.split('\n')[:-1]
    first_line = lines[0]
    initial_indent = snip._initial_indent
    spaces = ''

    # Get the first non-empty line
    for idx, l in enumerate(lines):
        if l.strip() != '':
            first_line = lines[idx]
            sp = re.findall(r'^\s+', first_line)
            if len(sp):
                spaces = sp[0]
            break            

    if text.strip().startswith(START):
        result = text.replace(START, '', 1).replace(END, '', 1)
    else:
        result = text.replace(spaces, spaces + START, 1).rstrip('\n') + END + '\n'

    if initial_indent:
        result = result.replace(initial_indent, '', 1)

    return result

