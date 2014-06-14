#!/usr/bin/env python
# coding: utf-8

import re
import sys

TERM_RE = re.compile(r'\s\s\s(\S[^\n]*)')

if len(sys.argv) != 2:
    print 'Usage: {0} <path/to/glossary.rst>'.format(__file__)
    sys.exit(1)

terms = []

with open(sys.argv[1]) as rst:
    for lin in rst:
        parts = TERM_RE.match(lin)
        if parts:
            terms.append(parts.group(1))

max_width = max(len(w) for w in terms)

width_preferred = 30
width_xlations = 60
fmt = '{0:{fill}<{mw}} {1:{fill}<{wp}} {2:{fill}<{wx}}'
width_args = dict(mw=max_width, wp=width_preferred, wx=width_xlations)

print
print '.. _terminologia:'
print
print '############'
print 'Terminologia'
print '############'
print
print '''A tabela abaixo relaciona todas as entradas do arquivo
``glossary.rst`` original (v. 2.7). A coluna central contém o termo adotado
na tradução brasileira e a última coluna contém traduções alternativas.

O termo adotado deve ser preferencialmente português, mas pode ser o termo
original quando nenhuma tradução é adequada ou quando o termo original já
está consagrado pelo uso (ex. string em vez de "cadeia de caracteres").

A última coluna pode estar em branco quando o termo adotado é uma tradução.
Se o termo adotado é o original em inglês, a última coluna deve
necessariamente conter uma ou mais traduções alternativas, sendo que a
primeira tradução deve ser a indicada para uso na primeira ocorrência
do texto em inglês em cada capítulo da documentação.
'''

print fmt.format('', '', '', fill='=', **width_args).rstrip()
print fmt.format('termo original', 'termo adotado', 'outras traduções', fill='', **width_args).rstrip()
print fmt.format('', '', '', fill='=', **width_args).rstrip()
for term in terms:
    print fmt.format(term, term+'?', '', fill='', **width_args).rstrip()
print fmt.format('', '', '', fill='=', **width_args).rstrip()
