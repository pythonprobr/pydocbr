.. _tut-errors:

****************
Erros e exceções
****************

Até agora mensagens de erro foram apenas mencionadas, mas se você testou os
exemplos, talvez tenha esbarrado em algumas. Existem pelo menos dois tipos
distintos de  erros: *erros de sintaxe* e *exceções*.


.. _tut-syntaxerrors:

Erros de sintaxe
================

Erros de sintaxe, também conhecidos como erros de parse, são provavelmente os
mais frequentes entre aqueles que ainda estão aprendendo Python::

   >>> while True print 'Olá mundo'
     File "<stdin>", line 1, in ?
       while True print 'Olá mundo'
                      ^
   SyntaxError: invalid syntax

O parser repete a linha inválida e apresenta uma pequena 'seta' apontando para
o ponto da linha em que o erro foi encontrado. O erro é causado (ou ao menos
detectado) pelo token que *precede* a seta: no exemplo, o erro foi detectado
na palavra reservada :keyword:`print`, uma vez que o dois-pontos (``':'``)
está faltando antes dela. O nome de arquivo e número de linha são exibidos
para que você possa rastrear o erro no texto do script.


.. _tut-exceptions:

Exceções
========

Mesmo que um comando ou expressão estejam sintaticamente corretos, talvez
ocorra um erro na hora de sua execução. Erros detectados durante a execução
são chamados *exceções* e não são necessariamente fatais: logo veremos como
tratá-las em programas Python. A maioria das exceções não são tratadas e
acabam resultando em mensagens de erro::

   >>> 10 * (1/0)
   Traceback (most recent call last):
     File "<stdin>", line 1, in ?
   ZeroDivisionError: integer division or modulo by zero
   >>> 4 + spam*3
   Traceback (most recent call last):
     File "<stdin>", line 1, in ?
   NameError: name 'spam' is not defined
   >>> '2' + 2
   Traceback (most recent call last):
     File "<stdin>", line 1, in ?
   TypeError: cannot concatenate 'str' and 'int' objects

A última linha da mensagem de erro indica o que aconteceu. Exceções surgem com
diferentes tipos, e o tipo é exibido como parte da mensagem: os tipos no
exemplo são :exc:`ZeroDivisionError`, :exc:`NameError` e :exc:`TypeError`. A
string exibida como sendo o tipo da exceção é o nome interno da exceção que
ocorreu. Isso é verdade para todas exceções pré-definidas em Python, mas não é
necessariamente verdade para exceções definidas pelo usuário (embora seja uma
convenção útil). Os nomes das exceções padrões são identificadores embutidos
(não palavras reservadas).

O resto da linha é um detalhamento que depende do tipo da exceção ocorrida e
sua causa.

A parte anterior da mensagem de erro apresenta o contexto onde ocorreu a
exceção. Essa informação é denominada *stack traceback* (situação da pilha de
execução). Em geral, contém uma lista de linhas do código fonte, sem
apresentar, no entanto, linhas lidas da entrada padrão.

:ref:`bltin-exceptions` lista as exceções pré-definidas e seus significados.


.. _tut-handling:

Tratamento de exceções
======================

É possível escrever programas que tratam exceções específicas. Observe o
exemplo seguinte, que pede dados ao usuário até que um inteiro válido seja
fornecido, ainda permitindo que o programa seja interrompido (utilizando
:kbd:`Control-C` ou seja lá o que for que o sistema operacional suporte); note
que uma interrupção gerada pelo usuário será sinalizada pela exceção
:exc:`KeyboardInterrupt`. ::

   >>> while True:
   ...     try:
   ...         x = int(raw_input("Por favor, informe um número: "))
   ...         break
   ...     except ValueError:
   ...         print "Oops!  Não foi um número válido.  Tente novamente..."
   ...

A instrução :keyword:`try` funciona da seguinte maneira:

* Primeiramente, a *cláusula try* (o conjunto de instruções entre as palavras
  reservadas :keyword:`try` e :keyword:`except` ) é executada.

* Se nenhuma exceção ocorrer, a *cláusula except* é ignorada e a execução da
  instrução :keyword:`try` é finalizada.

* Se ocorrer uma execução durante a execução da cláusula try, as instruções
  remanescentes na cláusula são ignoradas. Se o tipo da exceção ocorrida tiver
  sido previsto em algum :keyword:`except`, então essa cláusula será
  executada. Depois disso, a execução continua na próxima instrução após
  o conjunto *try/except*.

* Se a exceção levantada não foi prevista em nenhuma cláusula
  :keyword:`except` da cláusula :keyword:`try` em que ocorreu, então ela é
  entregue a uma instrução :keyword:`try` mais externa. Se não existir nenhum
  tratador previsto para tal exceção, será uma *exceção não tratada* e a
  execução do programa termina com uma mensagem de erro.

A instrução :keyword:`try` pode ter mais de uma cláusula :keyword:`except`
para especificar múltiplos tratadores para diferentes exceções. No máximo um
único tratador será ativado. Tratadores só são sensíveis às exceções
levantadas no interior da cláusula try, e não às que tenham ocorrido no
interior de outro tratador numa mesma instrução :keyword:`try`. Um tratador
pode ser sensível a múltiplas exceções, desde que as especifique em uma
tupla::

   ... except (RuntimeError, TypeError, NameError):
   ...     pass

A última cláusula :keyword:`except` pode omitir o nome da exceção, funcionando
como um curinga. Utilize esse recurso com extrema cautela, uma vez que isso
pode esconder erros do programador e do usuário! Também pode ser utilizado
para exibir uma mensagem de erro e então re-levantar a exceção (permitindo que
o invocador da função atual também possa tratá-la). ::

   import sys

   try:
       f = open('meuarquivo.txt')
       s = f.readline()
       i = int(s.strip())
   except IOError as (errno, strerror):
       print "I/O error({0}): {1}".format(errno, strerror)
   except ValueError:
       print "Não foi possível converter o dado para inteiro."
   except:
       print "Erro inesperado:", sys.exc_info()[0]
       raise

A construção :keyword:`try` ... :keyword:`except` possui uma *cláusula else*
opcional, que quando presente, deve ser colocada depois de todas as outras
cláusulas. É útil para um código que precisa ser executado se nenhuma exceção
foi levantada. Por exemplo::

   for arg in sys.argv[1:]:
       try:
           f = open(arg, 'r')
       except IOError:
           print 'não foi possível abrir', arg
       else:
           print arg, 'tem', len(f.readlines()), 'linhas'
           f.close()

Esse recurso é melhor do que simplesmente adicionar o código da cláusula
:keyword:`else` ao corpo da cláusula :keyword:`try`, pois mantém as exceções
levantadas no :keyword:`else` num escopo diferente de tratamento das exceções
levantadas na cláusula :keyword:`try`, evitando que acidentalmente seja
tratada uma exceção que não foi levantada pelo código protegido pela
construção  :keyword:`try` ... :keyword:`except`.

Quando uma exceção ocorre, ela pode estar associada a um valor chamado
*argumento* da exceção. A presença e o tipo do argumento dependem do tipo da
exceção.

A cláusula except pode especificar uma variável depois do nome (ou da tupla de
nomes) da exceção. A variável é associada à instância de exceção capturada,
com os argumentos armazenados em ``instancia.args``. Por conveniência, a
instância define o método :meth:`__str__` para que os argumentos possam ser
exibidos diretamente sem necessidade de acessar ``.args``.

Pode-se também instanciar uma exceção antes de levantá-la e adicionar qualquer
atributo a ela, conforme desejado. ::

   >>> try:
   ...    raise Exception('spam', 'eggs')
   ... except Exception as inst:
   ...    print type(inst) # a instância da exceção
   ...    print inst.args  # argumentos armazenados em .args
   ...    print inst       # __str__ permite exibir args diretamente
   ...    x, y = inst      # __getitem__ permite desempacotar args diretamente
   ...    print 'x =', x
   ...    print 'y =', y
   ...
   <type 'exceptions.Exception'>
   ('spam', 'eggs')
   ('spam', 'eggs')
   x = spam
   y = eggs

Se uma exceção possui argumento, ele é exibido ao final ('detalhe') da
mensagem de exceções não tratadas.

Além disso, tratadores de exceção são capazes de capturar exceções que tenham
sido levantadas no interior de funções invocadas (mesmo que indiretamente) na
cláusula try. Por exemplo::

   >>> def isso_falha():
   ...     x = 1/0
   ...
   >>> try:
   ...     isso_falha()
   ... except ZeroDivisionError as detalhe:
   ...     print 'Tratando erros em tempo de execução:', detalhe
   ...
   Tratando erros em tempo de execução: integer division or modulo by zero


.. _tut-raising:

Levantando exceções
===================

A instrução :keyword:`raise` permite ao programador forçar a ocorrência de um
determinado tipo de exceção. Por exemplo::

   >>> raise NameError('HiThere')
   Traceback (most recent call last):
     File "<stdin>", line 1, in ?
   NameError: HiThere

O argumento de :keyword:`raise` indica a exceção a ser levantada. Esse
argumento deve ser uma instância de exceção ou uma classe de exceção (uma
classe que deriva de :class:`Exception`)

Caso você precise determinar se uma exceção foi levantada ou não, mas não quer
manipular o erro, uma forma simples de instrução :keyword:`raise` permite que
você levante-a novamente::

   >>> try:
   ...     raise NameError('HiThere')
   ... except NameError:
   ...     print 'Uma exceção voou!'
   ...     raise
   ...
   Uma exceção voou!
   Traceback (most recent call last):
     File "<stdin>", line 2, in ?
   NameError: HiThere


.. _tut-userexceptions:

Exceções definidas pelo usuário
===============================

Programas podem definir novos tipos de exceções, através da criação de uma
nova classe (veja :ref:`tut-classes` para mais informações sobre classes
Python). Exceções devem ser derivadas da classe :exc:`Exception`, direta ou
indiretamente. Por exemplo::

   >>> class MeuErro(Exception):
   ...     def __init__(self, valor):
   ...         self.valor = valor
   ...     def __str__(self):
   ...         return repr(self.valor)
   ...
   >>> try:
   ...     raise MeuErro(2*2)
   ... except MeuErro as e:
   ...     print 'Minha exceção ocorreu, valor:', e.valor
   ...
   Minha exceção ocorreu, valor: 4
   >>> raise MeuErro('oops!')
   Traceback (most recent call last):
     File "<stdin>", line 1, in ?
   __main__.MeuErro: 'oops!'

Neste exemplo, o método padrão :meth:`__init__` da classe :class:`Exception`
foi redefinido. O novo comportamento simplesmente cria o atributo *valor*.
Isso substitui o comportamento padrão de criar o atributo *args*.

Classes de exceções podem ser definidas para fazer qualquer coisa que
qualquer outra classe faz, mas em geral são bem simples, frequentemente
oferecendo apenas alguns atributos que fornecem informações sobre o erro que
ocorreu. Ao criar um módulo que pode gerar diversos erros, uma prática comum é
criar uma classe base para as exceções definidas por aquele módulo, e as
classes específicas para cada condição de erro como subclasses dela::

   class Error(Exception):
       """Classe base para exceções dessa módulo"""
       pass

   class InputError(Error):
       """Exceções levantadas por erros na entrada

       Atributos:
           expr -- expressão da entrada onde o erro ocorreu
           msg  -- explicação do erro
       """

       def __init__(self, expr, msg):
           self.expr = expr
           self.msg = msg

   class TransitionError(Error):
       """Levantada quando uma operação tenta fazer uma transição de estado não
       permitida.

       Atributos:
           anterior -- estado do início da transição
           proximo -- novo estado
           msg  -- explicação do porquê a transação específica não é permitida
       """

       def __init__(self, anterior, proximo, msg):
           self.anterior = anterior
           self.proximo = proximo
           self.msg = msg

É comum que novas exceções sejam definidas com nomes terminando em "Error",
semelhante a muitas exceções embutidas.

Muitos módulos padrão definem novas exceções para reportar erros que ocorrem
no interior das funções que definem. Mais informações sobre classes aparecem
no capítulo :ref:`tut-classes`.


.. _tut-cleanup:

Definindo ações de limpeza
==========================

A instrução :keyword:`try` possui outra cláusula opcional, cuja finalidade é
permitir a implementação de ações de limpeza, que sempre devem ser executadas
independentemente da ocorrência de exceções. Como no exemplo::

   >>> try:
   ...     raise KeyboardInterrupt
   ... finally:
   ...     print 'Adeus, mundo!'
   ...
   Adeus, mundo!
   Traceback (most recent call last):
     File "<stdin>", line 2, in ?
   KeyboardInterrupt

Uma *cláusula finally* é sempre executada, ocorrendo ou não uma exceção.
Quando ocorre uma exceção na cláusula :keyword:`try` e ela não é tratada por
uma cláusula :keyword:`except` (ou quando ocorre em cláusulas
:keyword:`except` ou :keyword:`else`), ela é re-levantada depois que a
cláusula :keyword:`finally` é executada. A cláusula :keyword:`finally` é
executada "na saída" quando qualquer outra cláusula da instrução
:keyword:`try` é finalizada, mesmo que seja por meio de qualquer uma das
instruções :keyword:`break`, :keyword:`continue` ou :keyword:`return`. Um
exemplo mais completo::

   >>> def divide(x, y):
   ...     try:
   ...         resultado = x / y
   ...     except ZeroDivisionError:
   ...         print "divisão por zero!"
   ...     else:
   ...         print "resultado é", resultado
   ...     finally:
   ...         print "executando a cláusula finally"
   ...
   >>> divide(2, 1)
   resultado é 2
   executando a cláusula finally
   >>> divide(2, 0)
   divisão por zero!
   executando a cláusula finally
   >>> divide("2", "1")
   executando a cláusula finally
   Traceback (most recent call last):
     File "<stdin>", line 1, in ?
     File "<stdin>", line 3, in divide
   TypeError: unsupported operand type(s) for /: 'str' and 'str'

Como você pode ver, a cláusula :keyword:`finally` é executado em todos os
casos. A exceção :exc:`TypeError` levantada pela divisão de duas strings não é
tratada pela cláusula :keyword:`except` e portanto é re-levantada depois que a
cláusula :keyword:`finally` é executada.

Em aplicação do mundo real, a cláusula :keyword:`finally` é útil para liberar
recursos externos (como arquivos ou conexões de rede), independentemente do
uso do recurso ter sido bem sucedido ou não.


.. _tut-cleanup-with:

Ações de limpeza predefinidas
=============================

Alguns objetos definem ações de limpeza padrões para serem executadas quando o
objeto não é mais necessário, independentemente da operação que estava usando
o objeto ter sido ou não bem sucedida. Veja o exemplo a seguir, que tenta
abrir um arquivo e exibir seu conteúdo na tela. ::

   for linha in open("meuarquivo.txt"):
       print linha

O problema com esse código é que ele deixa o arquivo aberto um período
indeterminado depois que o código é executado. Isso não chega a ser problema
em scripts simples, mas pode ser um problema para grandes aplicações. A
palavra reservada :keyword:`with` permite que objetos como arquivos sejam
utilizados com a certeza de que sempre serão prontamente e corretamente
finalizados. ::

   with open("meuarquivo.txt") as a:
       for linha in a:
           print linha

Depois que a instrução é executada, o arquivo *a* é sempre fechado, mesmo se
ocorrer um problema durante o processamento das linhas. Outros objetos que
fornecem ações de limpeza predefinidas as indicarão em suas documentações.


