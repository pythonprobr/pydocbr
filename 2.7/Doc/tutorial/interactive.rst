.. _tut-interacting:

*********************************************************
Edição interativa de entrada e substituição por histórico
*********************************************************

Algumas versões do interpretador Python suportam facilidades de edição e substituição
semelhantes às encontradas na shell Korn ou na GNU Bash. Isso é implementado
através da biblioteca `GNU Readline`_, que suporta edição no estilo Emacs ou vi.
Essa biblioteca possui sua própria documentação, que não será duplicada aqui. Porém
os fundamentos são fáceis de serem explicados. As facilidades aqui descritas estão
disponíveis nas versões Unix e Cygwin do interpretador.

Este capítulo *não* documenta as facilidades de edição do pacote PythonWin de
Mark Hammond, ou do ambiente IDLE baseado em Tk e distribuído junto com
Python. A recuperação de histórico da linha de comando do DOS ou NT e outros
sabores de DOS e Windows também são bichos diferentes.


.. _tut-lineediting:

Edição de linha
===============

Se instalada, a edição de linha está ativa sempre que o interpretador exibir
um dos prompts (primário ou secundário). A linha atual pode ser editada
usando comandos típicos do Emacs. Os mais importantes são: :kbd:`C-A`
(Control-A) move o cursor para o início da linha, :kbd:`C-E` para o fim,
:kbd:`C-B` move uma posição para à esquerda, :kbd:`C-F` para a direita.
:kbd:`Backspace` apaga o caractere à esquerda, :kbd:`C-D` apaga o da direita.
:kbd:`C-K` apaga do cursor até o resto da linha à direita, :kbd:`C-Y` cola a
linha apagada. :kbd:`C-underscore` desfaz a última alteração que você fez; e
pode ser repetido com efeito cumulativo.


.. _tut-history:

Substituição por histórico
==========================

Funciona da seguinte maneira: todas linhas não vazias são armazenadas em um
buffer de histórico, e ao digitar uma nova linha no prompt você está editando
a última linha deste buffer. :kbd:`C-P` retrocede uma linha no histórico,
:kbd:`C-N` avança uma linha. Qualquer linha desse histórico pode ser editada;
quando você faz isso, um astesrico aparece na frente do prompt. Pressionando
:kbd:`Enter` a linha atual é enviada para o interpretador. :kbd:`C-R` inicia
uma busca para trás no histórico, e :kbd:`C-S` faz uma busca para frente. [#]_


.. _tut-keybindings:

Definição de atalhos
====================

Atalhos de teclado e outros parâmetros da biblioteca Readline podem ser
personalizados colocando configurações no arquivo :file:`~/.inputrc`.
A definição de atalhos tem o formato ::

   nome-da-tecla: nome-da-funcao

ou ::

   "string": nome-da-funcao

e opções podem ser especificadas com ::

   set nome-da-opcao valor

Por exemplo::

   # Prefiro o estilo de edição do vi:
   set editing-mode vi

   # Edição em uma única linha:
   set horizontal-scroll-mode On

   # Redefinição de algumas teclas:
   Meta-h: backward-kill-word
   "\C-u": universal-argument
   "\C-x\C-r": re-read-init-file

Observe que a definição padrão para :kbd:`Tab` em Python é inserir um caractere
:kbd:`Tab` ao invés de completar o nome de um arquivo (padrão no Readline). Isto
pode ser reconfigurado de volta colocando:

   Tab: complete

em seu :file:`~/.inputrc`. Todavia, isto torna mais difícil digitar comandos
indentados em linhas de continuação se você estiver acostumado a usar :kbd:`Tab`
para isso.

.. index::
   module: rlcompleter
   module: readline

O preenchimento automático de nomes de variáveis e módulos estão opcionalmente
disponíveis. Para habilitá-los no modo interativo, adicione o seguinte ao seu
arquivo de inicialização: [#]_ ::

   import rlcompleter, readline
   readline.parse_and_bind('tab: complete')

Isso vincula a tecla :kbd:`Tab` para o preenchimento automático de nomes de
função. Assim, teclar :kbd:`Tab` duas vezes dispara o preenchimento,
procurando um determinado nome entre as variáveis locais e módulos
disponíveis. Para expressões terminadas em ponto, como em ``string.a``, a
expressão será avaliada até o último ``'.'`` quando serão sugeridos possíveis
complementos. Note que isso pode executar código da sua aplicação quando um
objeto que define o método :meth:`__getattr__` fizer parte da expressão.

Um arquivo de inicialização mais completo seria algo como esse exemplo. Note
que ele deleta os nomes que cria quando não são mais necessários; isso é feito
porque o arquivo de inicialização é executado no mesmo ambiente dos comandos
interativos, e remover os nomes evita criar efeitos colaterais no ambiente
interativo. Você pode achar conveniente manter alguns dos módulos importados,
como :mod:`os`, que acaba sendo necessário na maior parte das sessões com o
interpretador. ::

   # Adiciona autocompletar e um arquivo de histórico de comandos ao
   # interpretador interativo Python. Requer Python 2.0+ e Readline.
   # O autocompletar está associado, por padrão, à tecla Esc (você pode
   # alterar isso, veja a documentação do Readline)
   #
   # Salve o arquivo como ~/.pystartup e defina uma variável de ambiente
   # apontando para ele digitando no bash:
   #   $ export PYTHONSTARTUP=~/.pystartup

   import atexit
   import os
   import readline
   import rlcompleter

   historyPath = os.path.expanduser("~/.pyhistory")

   def save_history(historyPath=historyPath):
       import readline
       readline.write_history_file(historyPath)

   if os.path.exists(historyPath):
       readline.read_history_file(historyPath)

   atexit.register(save_history)
   del os, atexit, readline, rlcompleter, save_history, historyPath


.. _tut-commentary:

Alternativas para o interpretador interativo
============================================

Essa facilidade representa um enorme passo em comparação com versões
anteriores do interpretador. Todavia, ainda há desejos não atendidos. Seria
interessante se a indentação apropriada fosse sugerida em linhas de
continuação, pois o parser sabe se um token de indentação é necessário. O
mecanismo de autocompletar poderia utilizar a tabela de símbolos do
interpretador. Também seria útil um comando para verificar (ou até mesmo
sugerir) o balanceamento de parênteses, aspas, etc.

Um poderoso interpretador interativo alternativo que tem sido bastante
utilizado já há algum tempo é o IPython_, que possui recursos de
autocompletar, exploração de objetos e avançado gerenciamento de histórico.
Ele também pode ser personalizado e incorporada em outras aplicações. Outro
poderoso ambiente interativo similar é o bpython_.


.. rubric:: Footnotes

.. [#] N.d.T: Algumas vezes, o :kbd:`C-S` pode conflitar com a controle de
    fluxo XON/XOFF (no Konsole por exemplo). Como essa pesquisa é um
    característica da GNU Readline, você pode associa-lá a outra tecla.
    Contudo, é melhor e mais simples simplesmente desativar o XON/XOFF
    executando o seguinte comando: "stty -ixon" no shell. Além disso, é
    necessário que a opção mark-modified-lines da GNU Readline esteja
    ativa para que o asterisco apareça quando uma linha do histórico é
    alterada.

.. [#] Python executará o conteúdo do arquivo identificado pela variável de
   ambiente :envvar:`PYTHONSTARTUP` quando se inicia o interpretador no modo
   interativo. Para personalizar Python no modo não-interativo,
   veja :ref:`tut-customize`.


.. _GNU Readline: http://tiswww.case.edu/php/chet/readline/rltop.html
.. _IPython: http://ipython.scipy.org/
.. _bpython: http://www.bpython-interpreter.org/
