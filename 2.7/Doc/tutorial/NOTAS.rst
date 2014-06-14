
.. _notas-tradutores:

########################################
Notas para os tradutores da versão pt-br
########################################

Convenções
==========

Siga fielmente a marcação ReST dos arquivos originais.

Não traduza os nomes dos links (ex. ``_tut-exceptions``), pois as referências
cruzadas dependem disso para funcionar.

Limite as linhas de texto a 80 colunas, pois isso facilita a revisão com duas
versões do texto lado a lado, e também torna mais fácil analizar diffs.

Leia :ref:`documenting-index` para saber mais sobre as convenções usadas na
documentação oficial de Python.


Uso de maiúsculas e minúsculas
================================

Critérios de caixa alta/baixa nos títulos
------------------------------------------

Vamos usar caixa alta apenas para a primeira palavra do título e nomes próprios,
portanto::

  Using the Python Interpreter
  ============================

fica assim (note que "interpretador" está em minúsculas)::

  Usando o interpretador Python
  =============================

A vantagem de usar caixa alta só na primeira palavra e nomes próprios é
diminuir inconsistências e dilemas sobre quais palavras devem ter caixa alta.
Por exemplo, artigos, pronomes, conjunções etc. Por isso é uma boa prática
adotada em muitas editoras escrever tudo em minúsculas, deixando iniciais
maísculas só para o início da frase e nomes próprios.


Palavras a grafar em minúsculas
-------------------------------

Em português, nomes de dias da semana, meses do ano, idiomas e nacionalidades
são escritos em minúsculas (sim, o corretor ortográfico do Word está errado).


Estilo
======

Procure usar construções simples e diretas
-------------------------------------------

Para traduzir:

  The equal sign (``'='``) is used to assign a value to a variable.

Isto é melhor:

  O sinal de igual (``'='``) é usado para atribuir um valor a uma variável.

do que isto:

  O sinal de igual (``'='``) é utilizado para atribuição de um valor a uma variável.


Outro exemplo:

  O código de escape \u0020 indica a inserção do caractere Unicode na posição...

fica melhor assim:

  O código de escape \u0020 insere o caractere Unicode na posição...


Mais alguns exemplo:

  Here is -> Eis (em vez de "Aqui está")

  provides access -> dá acesso (em vez de "provê acesso")

  To convert -> Para converter (em vez de "Para se converter")

  For instance, we can write... -> Por exemplo, podemos escrever...
  (em vez de "A título de exemplificação, nós podemos escrever...")


Evite o uso excessivo de pronomes
---------------------------------

Pronomes são sempre obrigatórios em inglês, mas em português eles são
dispensáveis em muitos casos.

Por exemplo:

  If you want to include special characters in the string, you can do so...

Eis uma tradução literal:

  Se você desejar incluir caracteres especiais na string, você pode fazê-lo...

Uma mais elegante:

  Se desejar incluir caracteres especiais na string, pode fazê-lo...

Outro exemplo:

  Of course, we can use Python for...

Fica melhor assim:

  Naturalmente, podemos usar Python para...

em vez de:

  Naturalmente, nós podemos utilizar Python para...

Isso x isto
-----------

Conforme Thais Nicoleti de Camargo, consultora de língua portuguesa e
colunista da Folha:

  Usam-se as formas com "ss" para remeter àquilo que já foi dito e as formas com
  "st" para apontar para o que será dito posteriormente. Assim: "Ouça isto:
  nunca me decepcione!" e "Que nunca a decepcionasse. Foi isso o que ela lhe
  pediu".

Exemplo em datastructures.rst::

     >>> transposta = []
     >>> for i in range(len(matriz[0])):
     ...     transposta.append([linha[i] for linha in matriz])
     ...
     >>> transposta
     [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

  e isso, por sua vez, faz o mesmo que isto::

     >>> transposta = []
     >>> for i in range(len(matriz[0])):
     ...     # as próximas 3 linhas implementam a listcomp aninhada
     ...     linha_transposta = []
     ...     for linha in matriz:
     ...         linha_transposta.append(linha[i])
     ...     transposta.append(linha_transposta)
     ...
     >>> transposta
     [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


"looks like this"
-----------------

Essa é uma expressão idiomática, e sua tradução literal soa muito mal: "se
parece com isso" (não é natural em português, parece uma tradução automática).
Alternativas melhores: "é assim" ou "tem esta forma". Exemplo:

   A class definition with multiple base classes looks like this:

pode ser traduzido assim:

   Uma definição de classe que com várias classes base tem esta forma:


Mais informações
----------------

Use sempre "consulte x para mais informações" em vez de "consulte x para
maiores informações".

.. _traducoes-adotadas:

Traduções adotadas para termos específicos
==========================================

Veja também :ref:`terminologia` (traduções adotadas para o glossário).

arrow
  seta

asterisk
  asterisco (cf. dicionário Houaiss)

backslash
   contrabarra (no Google, "contra-barra" tem 3x mais ocorrências que "barra
   invertida"; pela lógica da nova ortografia, o hífen neste caso não é mais
   usado)

blank line
  linha em branco (em vez de linha nula)

built-in function
  função embutida

character
  caractere (e não "caracter", que não consta no Houaiss nem no Aulete)

container objects
  coleções

current
  atual (e não "corrente", que é um falso cognato)

extension
  extensão (com 'x' e 's')

extend
  estender (com 's') uma classe, ou prolongar -- uma lista, por exemplo

indent, indented
  indentar, indentação (conforme o dicionário Aulete)

file objects
  objetos arquivo (e não "objetos de arquivo")

float
  float (quando se refere ao tipo) ou ponto flutuante (o conceito
  abstrato; sem hífen)

keyword
  palavra reservada (sem hífen)

keyword argument
  argumento nomeado

multi-line
  multi-linha (mais claro e tão comum quando "multi linha" no
  Google, e tem o dobro de ocorrências que multilinha)

parameter
  parâmetro formal (em declarações de funções) ou argumento (os
  valores passados na invocação)

parser
  parser ou analisador sintático

performance
  desempenho

print
  exibir (exceto quando realmente se tratar de imprimir em papel)

return
  devolver (quando se refere a função que devolve um valor) ou retornar
  (quando se refere ao fluxo de execução)

raise
   levantar, no sentido de "levantar uma exceção" ("lançar uma exceção"
   é mais frequente que "levantar uma exceção" segundo o Google, mas isso
   é porque em Java, JavaScript e PHP o comando chama-se "throw", que
   é lançar; em Python usamos "raise", que é levantar [pense em um
   bandeirinha sinalizando uma falta no futebol])

shell
  console ou shell, conforme o contexto: ao tratar do interpretador
  interativo, usar sempre "console", evitando confusão com o shell do
  sistema operacional

significant
  significativo (e nao "significante")

stack trace
  v. traceback

statement
  instrução (termo melhor e mais genérico) ou alternativamente, comando
  (quando se trata comandos de controle de fluxo ou o print) ou declaração
  (como ``class``, ``def``, ``global``); [#]_

traceback
  traceback (situação da pilha de execução), desse jeito mesmo, com a
  tradução entre parênteses quando for a primeira ocorrência do termo [#]_

triple-quote
  aspas triplas (em vez de "aspas tríplices"; em nome da simplicidade)

try
  experimentar ou tentar (depende do contexto: "Let's try some..." significa
  "vamos experimentar alguns...")

use, using
  uso, usar, usando (em vez de "utilização", "utilizar", "utilizando"; em
  nome da simplicidade)

wildcard
  curinga (e não "coringa"; verificado nos dicionários Aulete e Houaiss)


Referências
============

Dicionário Aulete Digital
  http://aulete.uol.com.br/site.php?mdl=aulete_digital

Dicionário Houaiss da Língua Portuguesa (exige login no UOL)
  http://houaiss.uol.com.br/busca.jhtm

Isto, isso e aquilo: uma conversa sobre pronomes demonstrativos
  http://www1.folha.uol.com.br/folha/colunas/noutraspalavras/ult2675u20.shtml

Estender e extensão
  http://www.dicionarioweb.com.br/artigo/estender-ou-extender

.. rubric:: Meta-notas

.. [#] No fundo, em Python não há instruções meramente declarativas pois
  tudo se dá em tempo de execução. ``def`` é um comando que cria uma função
  e atribui seu nome a uma variável no escopo atual. ``import`` executa o
  módulo e cria variáveis no escopo global etc. Por isso o termo genérico
  instrução é melhor que comando ou declaração

.. [#] Não usamos N.d.T. quando se trata apenas de colocar o termo equivalente
   em português entre parênteses (ou vice-versa, há casos em que introduzimos um
   termo em português e colocamos o original em inglês, que pode ser mais familiar
   para alguns leitores, entre parênteses). Além disso, somente colocamos os
   parênteses na primeira ocorrência em cada capítulo. Ou seja, se um termo assim
   aparece em vários capítulos, o termo entre parênteses será mostrado na primeira
   vez que for citado em cada um dos capítulos.


