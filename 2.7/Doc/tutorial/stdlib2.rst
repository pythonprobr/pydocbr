.. _tut-brieftourtwo:

****************************************************
Um breve passeio pela biblioteca padrão --- parte II
****************************************************

Este segundo passeio apresenta alguns módulos avançados que atendem
necessidades de programação profissional. Estes módulos raramente aparecem
em scripts pequenos.


.. _tut-output-formatting:

Formatando a saída
==================

O módulo :mod:`repr` oferece uma versão modificada da função :func:`repr` para
abreviar a exibição de coleções grandes ou profundamente aninhadas::

   >>> import repr
   >>> repr.repr(set('supercalifragilisticexpialidocious'))
   "set(['a', 'c', 'd', 'e', 'f', 'g', ...])"

O módulo :mod:`pprint` oferece um controle mais sofisticado na exibição tanto
de objetos embutidos quanto aqueles criados pelo usuário de maneira que fique
legível para o interpretador. Quando o resultado é maior que uma linha, o
"pretty printer" acrescenta quebras de linha e indentação para revelar as
estruturas de maneira mais clara::

   >>> import pprint
   >>> t = [[[['preto', 'ciano'], 'branco', ['verde', 'vermelho']],
   ...     [['magenta', 'amarelo'], 'azul']]]
   ...
   >>> pprint.pprint(t, width=30)
   [[[['preto', 'ciano'],
      'branco',
      ['verde', 'vermelho']],
     [['magenta', 'amarelo'],
      'azul']]]

O módulo :mod:`textwrap` formata parágrafos de texto para que caibam em uma
dada largura de tela::

   >>> import textwrap
   >>> doc = """O método wrap() funciona como o método fill() exceto pelo fato
   ... de devolver uma lista de strings ao invés de uma única string com
   ... quebras de linha para separar as linhas."""
   ...
   >>> print textwrap.fill(doc, width=40)
   O método wrap() funciona como o método
   fill() exceto pelo fato de devolver uma
   lista de strings ao invés de uma única
   string com quebras de linha para separar
   as linhas.

O módulo :mod:`locale` acessa uma base de dados de formatos específicos a
determinada cultura. O argumento ``grouping`` da função :func:`format` oferece
uma forma direta de formatar números com separadores de grupo::

   >>> import locale
   >>> locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
   'pt_BR.utf8'
   >>> conv = locale.localeconv()          # pega um dicionário das convenções
   >>> x = 1234567.8
   >>> locale.format("%d", x, grouping=True)
   '1.234.567'
   >>> locale.format_string("%s%.*f", (conv['currency_symbol'],
   ...                      conv['frac_digits'], x), grouping=True)
   'R$1.234.567,80'


.. _tut-templating:

Usando templates
================

O módulo :mod:`string` inclui a versátil classe :class:`Template` com uma
sintaxe simplificada, adequada para ser editada por usuários finais. Isso
permite que usuários personalizem suas aplicações sem a necessidade de alterar
a aplicação.

Em um template são colocadas marcações indicando o local onde o texto variável
deve ser inserido. Uma marcação é formada por ``$`` seguido de um
identificador Python válido (caracteres alfanuméricos e underscores).
Envolvendo-se o identificador da marcação entre chaves, permite que ele seja
seguido por mais caracteres alfanuméricos sem a necessidade de espaços.
Escrevendo-se ``$$`` cria-se um único ``$``::

   >>> from string import Template
   >>> t = Template('Os ${lugar}nos enviaram $$10 para $causa.')
   >>> t.substitute(lugar='Curitiba', causa='as obras de saneamento')
   'Os Curitibanos enviaram $10 para as obras de saneamento.'

O método :meth:`substitute` levanta uma exceção :exc:`KeyError` quando o
identificador de uma marcação não é fornecido em um dicionário ou em um
argumento nomeado (*keyword argument*). Para aplicações que podem receber
dados incompletos fornecidos pelo usuário, o método :meth:`safe_substitute`
pode ser mais apropriado --- deixará os marcadores intactos se os dados
estiverem faltando::

   >>> t = Template('Encontre o $item e volte para $lugar.')
   >>> d = dict(item='cálice')
   >>> print t.substitute(d)
   Traceback (most recent call last):
     . . .
   KeyError: 'lugar'
   >>> print t.safe_substitute(d)
   Encontre o cálice e volte para $lugar

Subclasses de Template podem especificar um delimitador personalizado. Por
exemplo, um utilitário para renomeação em lote de fotos pode usar o sinal
de porcentagem para marcações como a data atual, número sequencial da
imagem ou formato do aquivo::

   >>> import time, os.path
   >>> fotos = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
   >>> class RenomeiaLote(Template):
   ...     delimiter = '%'
   >>> fmt = raw_input('Estilo para o nome (%d-data %n-numseq %f-formato):  ')
   Estilo para o nome (%d-data %n-numseq %f-formato):  Ashley_%n%f

   >>> t = RenomeiaLote(fmt)
   >>> data = time.strftime('%d%b%y')
   >>> for i, nome_arquivo in enumerate(fotos):
   ...     base, ext = os.path.splitext(nome_arquivo)
   ...     novo_nome = t.substitute(d=data, n=i, f=ext)
   ...     print '{0} --> {1}'.format(nome_arquivo, novo_nome)

   img_1074.jpg --> Ashley_0.jpg
   img_1076.jpg --> Ashley_1.jpg
   img_1077.jpg --> Ashley_2.jpg

Outra aplicação para templates é separar a lógica da aplicação dos detalhes de
múltiplos formatos de saída. Assim é possível usar templates personalizados
para gerar arquivos XML, relatórios em texto puro e relatórios web em HTML.


.. _tut-binary-formats:

Trabalhando com formatos binários de dados
==========================================

O módulo :mod:`struct` oferece as funções :func:`pack` e :func:`unpack` para
trabalhar com registros binários de tamanho variável. O exemplo a seguir
mostra como iterar através do cabeçalho de informação num aquivo ZIP sem usar
o módulo :mod:`zipfile`. Os códigos de empacotamento ``"H"`` e ``"I"``
representam números sem sinal de dois e quatro bytes respectivamente. O
``"<"`` indica que os números têm tamanho padrão e são little-endian (bytes
menos significativos primeiro)::

   import struct

   data = open('myfile.zip', 'rb').read()
   start = 0
   for i in range(3):          # mostra o cabeçalho dos 3 primeiros arquivos
       start += 14
       fields = struct.unpack('<IIIHH', data[start:start+16])
       crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

       start += 16
       filename = data[start:start+filenamesize]
       start += filenamesize
       extra = data[start:start+extra_size]
       print filename, hex(crc32), comp_size, uncomp_size

       start += extra_size + comp_size     # avança para o próximo cabeçalho


.. _tut-multi-threading:

Multi-threading
===============

O uso de threads é uma técnica para desacoplar tarefas que não são
sequencialmente dependentes. Threads podem ser usadas para melhorar o tempo de
resposta de aplicações que aceitam entradas do usuário enquanto outras tarefas
são executadas em segundo plano. Um caso relacionado é executar ações de
entrada e saída (I/O) em uma thread paralelamente a cálculos em outra thread.

O código a seguir mostra como o módulo de alto nível :mod:`threading` pode
executar tarefas em segundo plano enquanto o programa principal continua
a sua execução::

   import threading, zipfile

   class AsyncZip(threading.Thread):
       def __init__(self, infile, outfile):
           threading.Thread.__init__(self)
           self.infile = infile
           self.outfile = outfile
       def run(self):
           f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
           f.write(self.infile)
           f.close()
           print 'Terminei de zipar em segundo plano o arquivo: ', self.infile

   background = AsyncZip('mydata.txt', 'myarchive.zip')
   background.start()
   print 'O programa principal continua a sua execução em primeiro plano.'

   background.join()    # espera até que a tarefa em segundo plano termine
   print 'O programa principal esperou até a tarefa em segundo plano terminar.'

O principal desafio para as aplicações que usam múltiplas threads é coordenar
as threads que compartilham dados ou outros recursos. Para esta finalidade, o
módulo threading oferece alguns mecanismos primitivos de sincronização, como
travas (locks), eventos, variáveis de condição e semáforos.

Apesar dessas ferramentas serem poderosas, pequenos erros de projeto podem
resultar em problemas difíceis de serem reproduzidos. Então, a maneira
preferida de coordenar tarefas é concentrar todo o acesso a determinado
recurso em uma única thread e usar o módulo :mod:`Queue` para alimentar aquela
thread com requisições de outras threads. Aplicações usando objetos do tipo
:class:`Queue.Queue` para comunicação e coordenação inter-thread são mais
fáceis de implementar, mais legíveis e mais confiáveis.


.. _tut-logging:

Gerando logs
============

O módulo :mod:`logging` oferece um completo e flexível sistema de log. Da
maneira mais simples, mensagens de log são enviadas para um arquivo ou para
``sys.stderr``::

   import logging
   logging.debug('Informação de debug')
   logging.info('Mensagem informativa')
   logging.warning('Aviso:arquivo de configuração %s não encontrado',
                   'server.conf')
   logging.error('Um erro ocorreu')
   logging.critical('Erro crítico -- encerrando o programa.')

Isso produz a seguinte saída::

   WARNING:root:Aviso:arquivo de configuração server.conf não encontrado
   ERROR:root:Um erro ocorreu
   CRITICAL:root:Erro crítico -- encerrando o programa.

Por padrão, mensagens informativas e de depuração são suprimidas e a saída é
enviada para a saída de erros padrão (stderr). Outras opções de saída incluem
envio de mensagens através de correio eletrônico, datagramas, sockets ou para
um servidor HTTP. Novos filtros podem selecionar diferentes formas de envio de
mensagens, baseadas na prioridade da mensagem: :const:`DEBUG`, :const:`INFO`,
:const:`WARNING`, :const:`ERROR` e :const:`CRITICAL`.

O sistema de log pode ser configurado diretamente do Python ou pode ser
carregado a partir de um arquivo de configuração editável pelo usuário para
logs personalizados sem a necessidade de alterar a aplicação.


.. _tut-weak-references:

Referências fracas
==================

Python faz gerenciamento automático de memória (contagem de referências para a
maioria dos objetos e :term:`garbage collection <garbage collection>` [coleta
de lixo] para eliminar ciclos). A memória ocupada por um objeto é liberada
logo depois da última referência a ele ser eliminada.

Essa abordagem funciona bem para a maioria das aplicações, mas ocasionalmente
surge a necessidade de rastrear objetos apenas enquanto estão sendo usados por
algum outro. Infelizmente rastreá-los cria uma referência, e isso os fazem
permanentes. O módulo :mod:`weakref` oferece ferramentas para rastrear objetos
sem criar uma referência. Quando o objeto não é mais necessário, ele é
automaticamente removido de uma tabela de referências fracas e uma chamada
(*callback*) é disparada. Aplicações típicas incluem cacheamento de objetos
que são muito custosos para criar::

   >>> import weakref, gc
   >>> class A:
   ...     def __init__(self, value):
   ...             self.value = value
   ...     def __repr__(self):
   ...             return str(self.value)
   ...
   >>> a = A(10)                   # cria uma referência
   >>> d = weakref.WeakValueDictionary()
   >>> d['primary'] = a            # não cria uma referência
   >>> d['primary']                # pega o objeto se ele ainda estiver vivo
   10
   >>> del a                       # remove a única referência
   >>> gc.collect()                # roda o coletor de lixo logo em seguida
   0
   >>> d['primary']                # A entrada foi automaticamente removida
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
       d['primary']                # A entrada foi automaticamente removida
     File "C:/python26/lib/weakref.py", line 46, in __getitem__
       o = self.data[key]()
   KeyError: 'primary'


.. _tut-list-tools:

Ferramentas para trabalhar com listas
======================================

Muitas necessidades envolvendo estruturas de dados podem ser satisfeitas com o
tipo embutido lista. Entretanto, algumas vezes há uma necessidade por
implementações alternativas que sacrificam algumas facilidades em nome de
melhor desempenho.

O módulo :mod:`array` oferece uma classe :class:`array`, semelhante a uma
lista, mas que armazena apenas dados homogêneos e de maneira mais compacta. O
exemplo a seguir mostra um vetor de números armazenados como números binários
de dois bytes sem sinal (código de tipo ``"H"``) ao invés dos 16 bytes
usuais para cada item em uma lista de ``int``::

   >>> from array import array
   >>> a = array('H', [4000, 10, 700, 22222])
   >>> sum(a)
   26932
   >>> a[1:3]
   array('H', [10, 700])

O módulo :mod:`collections` oferece um objeto :class:`deque()` que comporta-se
como uma lista mas com *appends* e *pops* pela esquerda mais rápidos, porém
mais lento ao percorrer o meio da sequência. Esses objetos são adequados para
implementar filas e buscas de amplitude em árvores de dados (*breadth first
tree searches*)::

   >>> from collections import deque
   >>> d = deque(["tarefa1", "tarefa2", "tarefa3"])
   >>> d.append("tarefa4")
   >>> print "Tratando", d.popleft()
   Tratando tarefa1

   nao_buscados = deque([noh_inicial])
   def busca_em_amplitude(nao_buscados):
       noh = nao_buscados.popleft()
       for m in gen_moves(noh):
           if eh_objetivo(m):
	            return m
           nao_buscados.append(m)

Além de implementações alternativas de listas, a biblioteca também oferece
outras ferramentas como o módulo :mod:`bisect` com funções para manipulação
de listas ordenadas::

   >>> import bisect
   >>> pontos = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
   >>> bisect.insort(pontos, (300, 'ruby'))
   >>> pontos
   [(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]

O módulo :mod:`heapq` oferece funções para implementação de *heaps* baseadas
em listas normais. O valor mais baixo é sempre mantido na posição zero. Isso é
útil para aplicações que acessam repetidamente o menor elemento, mas não querem
reordenar a lista toda a cada acesso::

   >>> from heapq import heapify, heappop, heappush
   >>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
   >>> heapify(data)                      # re-arranja a lista numa ordem heap
   >>> heappush(data, -5)                 # adiciona um novo item
   >>> [heappop(data) for i in range(3)]  # recupera os três menores itens
   [-5, 0, 1]


.. _tut-decimal-fp:

Aritmética decimal com ponto flutuante
======================================

O módulo :mod:`decimal` oferece o tipo :class:`Decimal` para aritmética
decimal com ponto flutuante. Comparado a implementação embutida :class:`float`
que usa aritmética binária de ponto flutuante, a classe é especialmente útil
para:

* aplicações financeiras que requerem representação decimal exata,
* controle sobre a precisão,
* controle sobre arredondamento para satisfazer requisitos legais,
* rastreamento de casas decimais significativas, ou
* aplicações onde o usuário espera que os resultados sejam os mesmos que os
  dos cálculos feitos à mão.

Por exemplo, calcular um imposto de 5% sobre uma chamada telefônica de 70
centavos devolve diferentes resultados com aritmética de ponto flutuante
decimal ou binária. A diferença torna-se significativa se os resultados são
arredondados para o centavo mais próximo. ::

   >>> from decimal import *
   >>> x = Decimal('0.70') * Decimal('1.05')
   >>> x
   Decimal('0.7350')
   >>> x.quantize(Decimal('0.01'))  # arredonda para o centavo mais próximo
   Decimal('0.74')
   >>> round(.70 * 1.05, 2)         # o mesmo cálculo com float
   0.73

O resultado de :class:`Decimal` considera zeros à direita, automaticamente
inferindo quatro casas decimais a partir de multiplicandos com duas casas
decimais. O módulo :mod:`decimal` reproduz a aritmética como fazemos à mão e
evita problemas que podem ocorrer quando a representação binária do ponto
flutuante não consegue representar quantidades decimais com exatidão.

A representação exata permite à classe :class:`Decimal` executar cálculos de
módulo e testes de igualdade que não funcionam bem em ponto flutuante
binário::

   >>> Decimal('1.00') % Decimal('.10')
   Decimal('0.00')
   >>> 1.00 % 0.10
   0.09999999999999995

   >>> sum([Decimal('0.1')]*10) == Decimal('1.0')
   True
   >>> sum([0.1]*10) == 1.0
   False

O módulo :mod:`decimal` implementa a aritmética com tanta precisão quanto
necessária::

   >>> getcontext().prec = 36
   >>> Decimal(1) / Decimal(7)
   Decimal('0.142857142857142857142857142857142857')

