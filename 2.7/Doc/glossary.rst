.. _glossary:

***********
Glossário
***********

.. OBS: se você adicionar novos verbetes, mantenha-os em ordem alfabética!

.. glossary::

   ``>>>``
      O prompt padrão do shell interativo do Python.  Normalmente visto em
      exemplos de código que podem ser executados interativamente no
      interpretador.

   ``...``
      O prompt padrão do shell interativo do Python ao se digitar código em um
      bloco indentado ou dentro de um par de delimitadores direita-esquerda   .. XXX: concordam com "delimitadores direita-esquerda"?
      (como parênteses, colchetes ou chaves).      

   2to3
      Uma ferramenta que tenta converter código Python 2.x para código Python 3.x
      tratando a maioria das incompatibilidades que podem se detectadas com análise   .. XXX: permanece "detectadas" ou "detetadas" pela nova ortografia?
      do código-fonte e navegação na árvore sintática.

      O 2to3 está disponível na biblioteca padrão como :mod:`lib2to3`; um ponto de   .. XXX: concordam com: "ponto de entrada"?
      entrada é disponibilizado como :file:`Tools/scripts/2to3`.  Veja
      :ref:`2to3-reference`.

   classe base abstrata
      Classes base abstratas complementam a :term:`tipagem pato`
      disponibilizando uma forma de definir interfaces quando a aplicação de
      outras técnicas, como o uso de :func:`hasattr`, for um tanto quanto
      estranha ou mesmo errônea (por exemplo, com :ref:`métodos mágicos
      <new-style-special-lookup>`).  Classes base abstratas também introduzem
      subclasses virtuais, que são classes que não herdam de uma classe mas
      ainda assim são reconhecidas por :func:`isinstance` e :func:`issubclass`;
      veja a documentação do módulo :mod:`abc`.  Python já vem com diversas
      classes base abstratas predefinidas para estruturas de dados (no módulo
      :mod:`collections`), para números (no módulo
      :mod:`numbers`) e streams (no módulo :mod:`io`).  Você pode criar suas   .. XXX: traduzir ou manter "streams"?
      próprias classes base abstratas a partir do módulo :mod:`abc`.

   argumento
      Um valor passado para uma função ou método, que é atribuído a uma variável
      local nomeada no corpo da função.  Uma função ou método pode ter tanto
      argumentos posicionais quanto argumentos nomeados em sua definição.  
      A quantidade de argumentos posicionais e nomeados pode ser variável: ``*``
      aceita ou passa (se estiver na definição ou na chamada da função) diversos
      argumentos posicionais numa lista, enquanto que ``**`` faz o mesmo para
      argumentos nomeados em um dicionário.

      Qualquer expressão pode ser usada dentro de uma lista de argumentos, sendo
      que seu valor avaliado é passado para uma variável local.

   atributo
      Um valor associado com um objeto que é referenciado por nome utilizando-se
      expressões com ponto.  Por exemplo, se um objeto *o* tem um atributo *a*,  .. XXX: alguma sugestão para "expressões com ponto"?
      ele deve ser referenciado como *o.a*.

   BDFL
      Iniciais para Benevolent Dictator For Life, ou ditador benevolente
      vitalício.  Uma referência ao `Guido van Rossum
      <http://www.python.org/~guido/>`_, o criador do Python.

   bytecode
      O código-fonte Python é compilado para bytecode, a representação interna
      de um programa em Python no interpretador CPython.  O bytecode também é
      mantido em cache em arquivos ``.pyc`` e ``.pyo``, de forma que executar
      um mesmo arquivo é mais rápido na segunda vez (a recompilação dos fontes
      para bytecode não é necessária).  Esta "linguagem intermediária" é
      adequada para execução em uma :term:`máquina virtual`, que executa o
      código de máquina correspondente para cada bytecode.  Tenha em mente que
      não se espera que bytecodes sejam executados entre máquinas virtuais
      Python diferentes, nem que se mantenham estáveis entre versões de Python.

      Uma lista de instruções bytecode pode ser encontrada na documentação
      para :ref:`o módulo dis <bytecodes>`.

   classe
      Um modelo para criação de objetos definidos pelo usuário.  Definições de
      classe normalmente contém definições de métodos que operam sobre
      instâncias da classe.

   classe clássica
      Qualquer classe que não herda de :class:`object`.  Veja
      :term:`classe de estilo novo`.  Classes clássicas serão removidas no
      Python 3.0.

   coerção
      A conversão implícita de uma instância de um tipo em outro durante uma
      operação que envolve dois argumentos do mesmo tipo.  Por exemplo,
      ``int(3.15)`` converte o número de ponto flutuante no inteiro ``3``, mas
      em ``3+4.5``, cada argumento é de um tipo diferente (um é inteiro e o
      outro de ponto flutuante) e ambos devem ser convertidos para o mesmo tipo
      antes de serem adicionados, ou senão será levantado um ``TypeError``.  A
      coerção entre dois operandos pode ser executada por meio da função interna
      ``coerce``; assim, ``3+4.5`` é equivalente a chamar
      ``operator.add(*coerce(3, 4.5))`` que resulta na chamada
      ``operator.add(3.0, 4.5)``.  Sem coerção, todos os argumentos, mesmo de
      tipos compatíveis, precisariam ser convertidos para o mesmo tipo pelo
      programador, p.ex.,``float(3)+4.5`` ao invés de apenas ``3+4.5``.

   número complexo
      Uma extensão ao familiar sistema de números reais em que todos os números
      são expressos como uma soma de uma parte real e uma parte imaginária.  
      Números imaginários são múltiplos reais da unidade imaginária (a raiz
      quadrada de ``-1``), normalmente escrita como ``i`` em matemática ou
      ``j`` em engenharia.  O Python tem suporte nativo para números complexos,
      que são escritos com esta última notação; a parte imaginária escrita com
      um sufixo ``j``, p.ex., ``3+1j``.  Para ter acesso aos equivalentes para
      números complexos do módulo :mod:`math`, utilize :mod:`cmath`.  O uso de
      números complexos é uma funcionalidade matemática bastante avançada.  Se
      você não sabe se irá precisar deles, é quase certo que você pode
      ignorá-los sem problemas.

   gerenciador de contexto
      Um objeto que controla o ambiente visto numa instrução :keyword:`with`
      por meio da definição dos métodos :meth:`__enter__` e :meth:`__exit__`.
      Veja :pep:`343`.

   CPython
      A implementação canônica da linguagem de programação Python, como
      disponibilizada pelo `python.org <http://python.org>`_.  O termo
      "CPython" é quando for necessário distinguir esta implementação de outras
      como Jython ou IronPython.

   decorador
      Uma função que devolve outra função, normalmente aplicada como uma   .. XXX: "função...função...função"
      função de transformação usando-se a sintaxe ``@wrapper``.  Exemplos
      comuns de decorators são :func:`classmethod` e :func:`staticmethod`.

      A sintaxe de um decorator é apenas açúcar sintático.  As duas definições
      de função a seguir são semanticamente equivalentes::

         def f(...):
             ...
         f = staticmethod(f)

         @staticmethod
         def f(...):
             ...

      O mesmo conceito existe para classes, mas é utilizado menos
      frequentemente.  Consulte a documentação e
      :ref:`definições de função <function>` e
      :ref:`definições de classe <class>` para mais detalhes sobre decoradores.   .. XXX: vai quebrar "ref: function definitions e class definitions"?

   descritor
      Qualquer objeto *new-style* que define os métodos :meth:`__get__`,   .. XXX: traduzir ou manter "objeto *new-style*"?
      :meth:`__set__`, ou :meth:`__delete__`.  Quando um atributo de classe é   .. XXX: revisar contexto
      um descritor, seu comportamento especial associado é disparado no acesso
      a um atributo.  Normalmente, ao se utilizar *a.b* para se obter, atribuir
      ou excluir um atributo dispara uma busca no objeto chamado *b* no
      dicionário de classe de *a*, mas se *b* for um descritor, o respectivo
      método descritor é chamado.  Compreender descritores é a chave para um 
      profundo entendimento de Python pois eles ão a base de muitas
      funcionalidades incluindo funções, métodos, propriedades, métodos de
      classe, métodos estáticos e referências para superclasses.

      Para mais informação sobre métodos descritores, veja :ref:`descriptors`.   .. XXX: não sei para onde aponta e optei por deixar como estava.

   dicionário
      Um array associativo em que chaves arbitrárias são mapeadas para valores.
      As chaves podem ser quaisquer objetos que possuam os métodos
      :meth:`__hash__` e :meth:`__eq__`. Dicionários são estruturas chamadas
      de hash na linguagem Perl.

   docstring
      Uma string literal que aparece como primeira expressão numa classe,
      função ou módulo.  Ainda que sejam ignoradas quando a suíte é executada,
      é reconhecida pelo compilador que a coloca no atributo :attr:`__doc__` da
      classe, função ou módulo que a encapsula.  Como ficam disponíveis por
      meio de introspecção, docstrings são o lugar canônico para documentação
      do objeto.

   duck-typing
   tipagem pato
      Um estilo de programação que não verifica o tipo do objeto para determinar
      se ele possui a interface correta; em vez disso, o método ou atributo é
      simplesmente chamado ou utilizado ("Se se parece com um pato e grasna como
      um pato, então deve ser um pato.")  Enfatizando interfaces ao invés de
      tipos específicos, o código bem desenvolvido aprimora sua flexibilidade
      por permitir substituição polimórfica.  Tipagem pato evita necessidade de
      testes que usem :func:`type` ou :func:`isinstance`.  (Note, porém, que a
      a tipagem pato pode ser complementada com o uso de
      :term:`classes base abstratas <abstract base class>`.)  Ao invés
      disso, são normalmente empregados testes :func:`hasattr` ou programação
      :term:`EAFP`.

   EAFP
   MFPPP
      Iniciais da expressão em inglês "easier to ask for forgiveness than
      permission" que significa "é mais fácil perdir perdão que permissão".
      Este estilo de codificação comum em Python assume a existência de chaves
      ou atributos válidos e captura exceções caso essa premissa se prove falsa.
      Este estilo limpo e rápido se caracteriza pela presença de várias
      declarações :keyword:`try` e :keyword:`except`.  A técnica diverge do
      estilo :term:`LBYL`, comum em outras linguagens como C, por exemplo.

   expressão
      Uma parte da sintaxe que pode ser avaliada para produzir algum valor. 
      Em outras palavras, uma expressão é uma composição de elementos de 
      expressão como literais, nomes, atributos de acesso, operadores ou 
      chamadas de função que, juntos, têm um valor.  Diferentemente de algumas
      outras linguagens, nem todas as construções em Python são expressões. 
      Existem ainda :term:`instrução` que não podem ser usadas como expressões, 
      tais como :keyword:`print` ou :keyword:`if`.  Atribuições também são
      declarações, não expressões.

   extension module
   módulo de extensão
      Um módulo escrito em C ou C++, usando a API C de Python para interagir
      tanto com código de usuário quanto do núcleo.

   file object
   objeto arquivo
      Um objeto que expõe uma API orientada a arquivos (com métodos tais como
      :meth:`read()` ou :meth:`write()`) para um recurso subjacente.  
      Dependendo da maneira como foi criado, um objeto arquivo pode mediar o
      acesso a um arquivo real no disco ou outro tipo de dispositivo de
      armazenamento ou de comunicação (por exemplo a entrada/saída padrão,
      buffers em memória, sockets, pipes, etc.).  Objetos arquivo também são
      chamados de :dfn:`file-like objects` ou :dfn:`streams`.

      Atualmente há três categorias de objetos arquivo: arquivos binários raw,   .. XXX: sugestões para "raw" e "bufferizados"?
      arquivos binários bufferizados e arquivos texto.  Suas interfaces estão
      definidas no módulo :mod:`io`.  A forma canônica de se criar um objeto
      arquivo é por meio da função :func:`open`.

   objeto semelhante a arquivo
      Um sinônimo para :term:`objeto arquivo`.

   finder
      Um objeto que tenta encontrar o :term:`loader` para um módulo.  Ele deve   .. XXX: manter ou traduzir "finder"?
      implementar um método chamado :meth:`find_module`.  Veja :pep:`302` para
      mais detalhes.

   floor division
   divisão pelo piso
      Divisão matemática que arredonda para baixo para o inteiro mais próximo.
      O operador de divisão pelo piso é ``//``.  Por exemplo, a expressão
      ``11 // 4`` retorna o valor ``2`` ao invés de ``2.75``, que seria
      retornado pela divisão de ponto flutuante.  Note que ``(-11) // 4`` é
      ``-3`` porque é ``-2.75`` arredondado *para baixo*.  Consulte a
      :pep:`238`.

   função
      Um conjunto de instruções que devolve algum valor para quem a invoca.  
      Uma função pode receber zero ou mais argumentos que podem ser usados na
      execução do corpo.  Veja também :term:`argumento` e :term:`método`.

   __future__
      Um pseudo-módulo o qual os programadores podem usar para habilitar novas
      funcionalidades da linguagem que não são compatíveis com o interpretador
      atual.  Por exemplo, a expressão ``11/4`` atualmente é avaliada com o
      valor ``2``.  Se o módulo no qual esta expressão estiver sendo executada
      tiver habilitado a *divisão verdadeira* tendo executado::

         from __future__ import division

      então a expressão ``11/4`` deverá ser avaliada como ``2.75``.  Ao 
      importar o módulo :mod:`__future__` e avaliar suas variáveis, você pode
      ver quando uma nova funcionalidade foi adicionada pela primeira vez à
      linguagem e quando ela se tornará padrão::

         >>> import __future__
         >>> __future__.division
         _Feature((2, 2, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 8192)

   garbage collection
   coleta de lixo
      O processo de liberação de memória quando ela não está mais sendo usada.
      O Python executa coleta de lixo por meio da contagem de referências e um
      coletor de lixo cíclico é capaz de detectar e quebrar referências
      cíclicas.

      .. index:: single: generator

   generator
   gerador
      Uma função que retorna um iterador.  É parecida com uma função normal,
      exceto pelo fato de conter instruções :keyword:`yield` para produzir uma
      série de valores que podem ser usados em um laço for ou que podem ser
      obtidos um de cada vez com a função :func:`next`.  Cada :keyword:`yield`
      suspende temporariamente o processamento, memorizando o estado da
      execução local (incluindo variáveis locais e declarações try pendentes).
      Quando o generator retorna, ele se recupera do último ponto onde estava
      (em contrapartida a funções que iniciam a execução nova a cada vez que
      são invocadas).

      .. index:: single: generator expression

   generator expression
   expressão geradora
      Uma expressão que retorna um iterador.  É semelhante a uma expressão que
      é seguida por uma expressão :keyword:`for` que define uma variável de um
      laço, um intervalo e uma expressão :keyword:`if` opcional.  A expressão
      combinada gera valores para a função onde está contida::

         >>> sum(i*i for i in range(10))         # soma dos quadrados 0, 1, 4, ... 81
         285

   GIL
      Veja :term:`trava global do interpretador`.

   global interpreter lock
   trava global do interpretador
      O mecanismo utilizado pelo interpretador :term:`CPython` para garantir
      que apenas uma thread execute o :term:`bytecode` Python por vez.  Isto
      simplifica a implementação do CPython ao fazer com que o modelo de
      objetos (incluindo tipos internos críticos como o :class:`dict`) ganhem
      segurança implícita contra acesso concorrente.  Travar todo o
      interpretador facilita que o interpretador em si seja multitarefa, às
      custas de muito do paralelismo já provido por máquinas multiprocessador.

      No entanto, alguns módulos de extensão, tanto da biblioteca padrão quanto
      de terceiros, são desenvolvidos de forma a liberar o GIL ao realizar
      tarefas computacionalmente muito intensas, como compactação ou cálculos
      de hash.  Além disso, o GIL é sempre liberado nas operações de E/S.

      No passado, esforços para criar um interpretador que lidasse plenamente
      com threads (travando dados compartilhados numa granularidade bem mais
      fina) não foram bem sucedidos devido a queda no desempenho ao serem
      executados em processadores de apenas um núcleo.  Acredita-se que superar
      essa questão de desempenho acabaria tornando a implementação muito mais
      complicada e bem mais difícil de manter.

   hashable
   hasheável
      Um objeto é *hasheável* se tem um valor de hash que nunca muda durante
      seu ciclo de vida (precisa ter um método :meth:`__hash__`) e se pode
      ser comparado com outros objetos (precisa ter um método 
      :meth:`__eq__` ou :meth:`__cmp__`).  Objetos hasheáveis que são
      comparados como iguais devem ter o mesmo valor de hash.

      A hashabilidade faz com que um objeto possa ser usado como chave de um
      dicionário e como membro de um conjunto, pois estas estruturas de dados
      utilizam os valores de hash internamente.

      Todos os objetos imutáveis nativos de Python são hasheáveis, enquanto
      que nenhum dos containers mutáveis (como listas e dicionários) é.
      Objetos que são instâncias de classes definidas pelo usuário são
      hasheáveis por padrão; todos eles são considerados como diferentes e
      seus valores de hash é dado pela função :func:`id`.

   IDLE
      Um ambiente de desenvolvimento integrado para Python.  IDLE é um editor
      básico e um ambiente interpretador que vem junto com a distribuição 
      padrão do Python.

   imutável
      Um objeto que possui um valor fixo.  Objetos imutáveis incluem números,
      strings e tuplas.  Estes objetos não podem ser alterados.  Um novo objeto
      deve ser criado se um valor diferente tiver de ser armazenado.  Objetos
      imutáveis têm um papel importante em lugares onde um valor constante de
      hash seja necessário, como por exemplo uma chave em um dicionário.

   divisão inteira
      Divisão matemática que desconsidera os restos.  Por exemplo, a expressão
      ``11/4`` resulta em ``2`` ao invés do valor ``2.75`` retornado pela 
      divisão de ponto flutuante.  Também chamada de *floor division*.  Ao se
      dividirem dois números inteiros o resultado será sempre um outro inteiro
      (com a função floor aplicada a ele).  No entanto, se um dos operandos for
      de outro tipo numérico (como um :class:`float`), o resultado sofrerá
      :term:`coerção`) para um tipo comum.  Por exemplo, um inteiro dividido 
      por um número de ponto flutuante resultará também num número de ponto
      flutuante, possivelmente contendo uma fração decimal.  A divisão inteira
      pode ser forçada utilizando-se o operador ``//`` ao invés de ``/``.  Veja
      também :term:`__future__`.

   importer
      Um objeto que tanto procura quanto carrega um módulo; sendo um objeto
      :term:`finder` e um :term:`loader` ao mesmo tempo.

   interativo
      Python tem um interpretador interativo, o que significa que você pode
      digitar comandos e expressões no prompt do interpretador, executá-los
      imediatamente e ver seus resultados.  Apenas execute ``python`` sem
      argumentos (possivelmente selecionando-o a partir do menu de aplicações
      de seu sistema operacional).  O interpretador interativo é uma maneira
      poderosa de testar novas ideias ou aprender mais sobre módulos e pacotes
      (lembre-se do comando ``help(x)``).

   interpretado
      Python é uma linguagem interpretada, em oposição àquelas que são
      compiladas, embora esta distinção possa ser nebulosa devido à presença do
      compilador de bytecode.  Isto significa que os arquivos-fontes podem ser
      executados diretamente sem necessidade explícita de se criar um arquivo
      executável.  Linguagens interpretadas normalmente têm um ciclo de
      desenvolvimento/depuração mais curto que as linguagens compiladas, apesar
      de seus programas geralmente serem executados mais lentamente.  Veja
      também :term:`interativo`.

   iterável
      Um objeto capaz de retornar seus membros um de cada vez.  Exemplos de
      iteráveis incluem todos os tipos de sequência (tais como
      :class:`list`, :class:`str` e :class:`tuple`) e alguns outros tipos, como
      o :class:`dict` e :class:`file`, além dos objetos de quaisquer classes
      que você definir com um método :meth:`__iter__` ou :meth:`__getitem__`.
      Iteráveis podem ser usados em um laço :keyword:`for` e em vários outros
      lugares em que uma sequência possa ser usada (:func:`zip`, :func:`map`,
      ...).  Quando um objeto iterável é passado como argumento para a função
      nativa :func:`iter`, ela retorna um iterador para o objeto.  Este 
      iterador é adequado para se varrer todo o conjunto de valores.  Ao usar
      iteráveis, normalmente não é necessário chamar :func:`iter` ou lidar com
      os objetos iteradores em si.  O comando ``for`` faz isso automaticamente
      para você, criando uma variável temporária para armazenar o iterador 
      durante a execução do laço.  Veja também :term:`iterator`,
      :term:`sequence` e :term:`generator`.

   iterador
      Um objeto que represent um fluxo de dados.  Repetidas chamadas ao método
      :meth:`next` de um iterador vão retornar itens sucessivos do fluxo.  
      Quando não houver mais dados disponíveis uma exceção :exc:`StopIteration`
      será levantada.  Neste ponto, o objeto iterador se esgotou e quaisquer 
      chamadas subsequentes a seu método :meth:`next` vão apenas levantar a 
      exceção :exc:`StopIteration` novamente.  Iteradores precisam ter um 
      método :meth:`__iter__` que retorne o objeto iterador em si, de forma que
      todo iterador também é iterável e pode ser usado na maioria dos lugares
      em que um iterável é requerido.  Uma notável exceção é código que tenta
      realizar passagens em múltiplas iterações.  Um objeto container (como um
      :class:`list`) produz um novo iterador a cada vez que você passar pela
      função :func:`iter` ou a utilizá-la em um laço :keyword:`for`.  Tentar
      isso com o mesmo iterador apenas iria retornar o mesmo objeto iterador
      esgotado já utilizado na iteração anterior, como se fosse um conteiner
      vazio.

      Mais informações podem ser encontradas em :ref:`typeiter`.

   key function
      Uma função chave ou função colação é algo que retorna um valor utilizado
      para ordenação ou classificação.  Por exemplo, :func:`locale.strxfrm` é
      usada para produzir uma chave de ordenação que leva o locale em 
      consideração para fins de ordenação.

      Uma porção de ferramentas em Python aceitam funções chave para controlar
      como os elementos são ordenados ou agrupados.  Algumas delas incluem
      :func:`min`, :func:`max`, :func:`sorted`, :meth:`list.sort`,
      :func:`heapq.nsmallest`, :func:`heapq.nlargest` e
      :func:`itertools.groupby`.

      Há várias maneiras de se criar funções chave.  Por exemplo, o método
      :meth:`str.lower` pode servir como uma função chave para ordenações
      insensíveis à caixa.  Alternativamente, uma função chave ad-hoc pode ser
      construída a partir de uma expressão :keyword:`lambda`, como
      ``lambda r: (r[0], r[2])``.  Além disso, o módulo :mod:`operator` dispõe
      de três construtores para funções chave: :func:`~operator.attrgetter`,
      :func:`~operator.itemgetter` e o :func:`~operator.methodcaller`.  
      Consulte o :ref:`Sorting HOW TO <sortinghowto>` para ver exemplos de como
      criar e utilizar funções chave.

   keyword argument
      (**pt-br**: argumento nomeado) Argumentos que são precedidos de 
      ``nome_de_variavel=`` na chamada.  O nome da variável designa o nome 
      local na função ao qual o valor será atribuído.  ``**`` é usado para
      aceitar argumentos nomeados arbitrários (não pre-definidos) na forma
      de um dicionário. Veja também :term:`argumento`.

   lambda
      Uma função anônima consistindo de uma única :term:`expressão` que é
      avaliada quando a função é chamada.  A sintaxe para criar uma função
      lambda é ``lambda [argumentos]: expressão``

   LBYL
      Iniciais da expressão em inglês "look before you leap", que significa
      algo como "olhe antes de pisar".  Este estilo de codificação testa as
      pré-condições explicitamente antes de fazer chamadas ou buscas.  Este
      estilo contrasta com a abordagem :term:`EAFP` e é caracterizada pela
      presença de muitos comandos :keyword:`if`.

      In a multi-threaded environment, the LBYL approach can risk introducing a
      race condition between "the looking" and "the leaping".  For example, the
      code, ``if key in mapping: return mapping[key]`` can fail if another
      thread removes *key* from *mapping* after the test, but before the lookup.
      This issue can be solved with locks or by using the EAFP approach.

   lista
      Uma estrutura de dados de :term:`sequência` que é nativa em Python.  Ao
      contrário do que seu nome faz supor, é uma estrutura mais parecida com um
      array em outras linguagens de programação do que com uma lista encadeada
      uma vez que o acesso a seus elementos tem complexidade O(1).

   list comprehension
      Uma maneira compacta de processar todos ou parte dos elementos de uma
      sequência e retornar os resultados em uma lista.
      ``result = ["0x%02x" % x for x in range(256) if x % 2 == 0]`` gera uma
      lista de strings contendo números hexadecimais (0x..) no intervalo de 0 a
      255.  A cláusula :keyword:`if` é opcional.  Se omitida, todos os
      elementos no ``range(256)`` serão processados.

   loader
      Um objeto que carrega um módulo.  Deve definir um método chamado 
      :meth:`load_module`.  Um loader é normalmente devolvido por um 
      :term:`finder`.  VEja :pep:`302` para detalhes.

   mapping
      Um objeto conteiner que suporta buscas por chaves arbitrárias e
      implementa os métodos especificados em :class:`~collections.Mapping` ou
      :class:`~collections.MutableMapping`
      :ref:`abstract base classes <collections-abstract-base-classes>`.  
      Exemplos incluem :class:`dict`, :class:`collections.defaultdict`,
      :class:`collections.OrderedDict` e :class:`collections.Counter`.

   metaclasse
      A classe de uma classe.  Definições de classe criam um nome de classe,
      um dicionário de classe e uma lista de classes base.  A metaclasse é
      responsável por receber estes três argumentos e criar a classe.  A 
      maioria das linguagens de programação orientadas a objetos provê uma
      implementação default.  O que torna o Python especial é o fato de ser
      possível criar metaclasses personalizadas.  A maioria dos usuários nunca
      vai precisar deste recurso, mas quando houver necessidade, metaclasses
      possibilitam soluções poderosas e elegantes.  Metaclasses têm sido
      utilizadas para gerar registros de acesso a atributos, para incluir
      proteção contra acesso concorrente, rastrear a criação de objetos,
      implementar singletons, dentre muitas outras tarefas.

      Mais informações podem ser encontradas em :ref:`metaclasses`.

   método
      Uma função que é definida dentro do corpo de uma classe. Se chamada como
      um atributo de uma instância daquela classe, o método receberá a
      instância do objeto como seu primeiro :term:`argumento` (que comumente
      é chamado de ``self``). Veja :term:`função` e :term:`nested scope`.

   method resolution order
      Ordem de resolução de métodos é a ordem em que os membros de uma classe
      base são buscados durante a pesquisa.  Veja `A ordem de resolução de
      métodos do Python 2.3
      <http://www.python.org/download/releases/2.3/mro/>`_.

   MRO
      Veja :term:`method resolution order`.

   mutável
      Objeto mutável é aquele que pode modificar seus valor mas manter
      seu :func:`id`.  Veja também :term:`immutable`.

   tupla nomeada
      Qualquer classe semelhante a uma tupla cujos elementos indexados também
      sejam acessíveis por meio de atributos nomeados (como exemplo, tem-se o
      :func:`time.localtime` que devolve um objeto semelhante à uma tupla em
      que o *ano* é acessível tanto através de um índice, como ``t[0]``, quanto
      por um atributo nomeado como ``t.tm_year``).

      Uma tupla nomeada pode ser um tipo nativo como :class:`time.struct_time`,
      ou pode ser criado com uma definição de classe normal.  Uma tupla nomeada
      também pode ser criada com a função fábrica
      :func:`collections.namedtuple`.  Esta última abordagem também provê
      automaticamente alguns recursos extras, como uma representação
      autodocumentada como ``Empregado(nome='jones', cargo='programador')``.

   namespace
      O lugar em que uma variável é armazenada.  Namespaces são implementados
      como dicionários.  Existem os namespaces local, global e nativo, bem como
      namespaces aninhados em objetos (em métodos).  Namespaces suportam
      modularidade ao previnir conflitos de nomes.  Por exemplo, as funções
      :func:`__builtin__.open` e :func:`os.open` são diferenciadas por seus
      namespaces.  Namespaces também auxiliam na legibilidade e na
      manutenibilidade ao torar mais claro quais módulos implementam uma
      função.  Escrever :func:`random.seed` ou :func:`itertools.izip`, por
      exemplo, deixa claro que estas funções são implementadas pelos módulos
      :mod:`random` e :mod:`itertools` respectivamente.
      
.. XXX: A definição de nested scope abaixo tem problemas conceituais e precisa
        ser revista.     

   nested scope
      A habilidade de se referir a uma variável em um definição mais
      abrangente.  Por exemplo, uma função definida dentro de uma outra função 
      também pode se referir às variáveis da função mais externa.  Note que
      escopos aninhados, por padrão, funcionam apenas com as variáveis da
      função mais externa.  Atente ainda que escopos aninhados também funcionam
      por padrão apenas para referência e não para atribuição.  Variáveis locais
      leem e escrevem no escopo mais interno.  De forma semelhante, variáveis
      globais leem e escrevem no namespace global.  A palavra-chave 
      :keyword:`nonlocal` nos permite escrever em escopos mais externos.

   new-style class
      Qualquer classe que herda de :class:`object`.  Isto inclui todos os tipos
      nativos como :class:`list` e :class:`dict`.  Apenas as classes new-style
      podem usar os recursos mais novos e versáteis de Python, como
      :attr:`__slots__`, descritores, properties e :meth:`__getattribute__`.

      Mais informações podem ser encontradas em :ref:`newstyle`.

   objeto
      Qualquer dado com estado (atributos ou valores) e comportamento definido
      (métodos).  Também é a classe base primordial de qualquer
      :term:`new-style class`.

   argumentos posicionais
      Os argumentos associados com nomes locais dentro de uma função ou método,
      determinados pela ordem em que eles são fornecidos na chamada.  ``*`` é
      usado tanto para aceitar mútiplos argumentos posicionais (quando na
      definição da função ou método) quanto para passar vários argumentos como
      uma lista para uma função.  Veja :term:`argumento`.

   Python 3000
      Apelido para a versão da série Python 3.x (termo cunhado há muito tempo,
      quando o lançamento de uma versão 3 soava como algo num futuro muito
      distante).  Também abreviado como "Py3k".

   Pythônico
      Uma ideia ou trecho de código que segue estritamente a maioria dos
      idiomas da linguagem Python, ao invés de implementar código usando
      conceitos comuns em outras linguagens.  Por exemplo, um idioma comum em
      Python é varrer todos os elementos de um iterável usando-se um comando
      :keyword:`for`.  Muitas outras linguagens não possuem este tipo de
      construção, de forma que as pessoas ainda não familiarizadas com Python
      algumas vezes utilizam contadores numéricos::

          for i in range(len(comida)):
              print comida[i]

      Em oposição à forma Pythônica, mais clara e legível::

         for pedaco in comida:
             print pedaco

   contador de referências
      O número de referências para um objeto.  Quando o contador de referência
      de um objeto chega a zero, então o objeto é desalocado.  O contador de
      referências geralmente não é visível para o código Python, mas é um
      elemento chave da implementação :term:`CPython`.  O módulo :mod:`sys`
      define uma função :func:`~sys.getrefcount` que os programadores podem
      chamar para devolver o contador de referências de um dado objeto.

   __slots__
      Uma declaração dentro de uma :term:`new-style class` que economiza
      memória ao pré-declarar espaço para atributos de instância e eliminar
      dicionários de instância.  Apesar de popular, esta técnica é complicada
      de se fazer funcionar corretamente, de forma que ela é mais adequada a
      alguns casos raros em que há grande quantidade de instâncias numa
      aplicação com restrições de memória.

   sequência
      Um :term:`iterable` que dá suporte a acesso a seus elementos de maneira
      eficiente utilizado-se índices inteiros por meio do método especial 
      :meth:`__getitem__`  e define um método :meth:`len` que retorna o
      comprimento da sequência.  Alguns tipos de sequências nativas são 
      :class:`list`, :class:`str`, :class:`tuple` e :class:`unicode`.  Tenha em
      mente que :class:`dict` também possui os métodos :meth:`__getitem__` e
      :meth:`__len__` mas é considerado um mapping ao invés de uma sequência
      porque suas pesquisas utilizam chaves :term:`imutável` ao invés de
      inteiros.

   fatia
      Um objeto que normalmente contém uma parte de uma :term:`sequence`.  Uma
      fatia é criada usando-se notação de subscrito, ``[]`` com dois-pontos
      entre os números quando vários são dados, como em
      ``nome_de_variavel[1:3:5]``.  A notação de colchetes (subscrito) utiliza
      objetos :class:`slice` internamente (ou, em versões mais antigas, os
      métodos :meth:`__getslice__` e :meth:`__setslice__`).

   método especial
      Um método que é chamado implicitamente pelo Python para executar uma
      certa operação em um tipo, como uma adição.  Tais métodos têm nomes que
      começam e terminal com dois underscores.  Os métodos especiais estão
      documentados em :ref:`specialnames`.

   instrução
      Uma instrução é parte de uma suíte (um "bloco" de código).  Uma instrução
      pode ser tanto uma :term:`expressão` ou uma das diversas construções com
      uma palavra-chave, tais como :keyword:`if`, :keyword:`while` ou
      :keyword:`for`.

   sequência estruturada
      Uma tupla com elementos nomeados.  Sequências estruturadas expôem uma
      interface semelhante a de uma :term:`tupla nomeada` em que os elementos
      podem ser acessados tanto por índice quando por um atributo.  No entanto,
      elas não têm nenhum dos métodos das tuplas nomeadas, como 
      :meth:`~collections.somenamedtuple._make` ou
      :meth:`~collections.somenamedtuple._asdict`.  Exemplos de sequências
      estruturadas incluem :data:`sys.float_info` e o valor de retorno de
      :func:`os.stat`.

   string de aspas triplas
      Uma string que é delimitada por três caracteres ou de aspas (") ou de
      apóstrofes (').  Apesar de não proverem nenhuma funcionalidade que já
      não esteja disponível nas strings delimitadas por aspas únicas, elas
      são úteis por diversas razões.  Elas permitem que você inclua aspas
      simples e duplas não escapadas e ainda podem se estender por várias
      linhas sem necessidade de caracteres de continuação, o que as torna
      especialmente úteis na escrita de docstrings.

   tipo
      O tipo de objeto Python determina de que natureza este objeto é; cada
      objeto tem um tipo.  O tipo de um objeto é acessível por seu atributo
      :attr:`__class__` ou pode ser obtido com ``type(obj)``.

   view
      Os objetos retornados pelos métodos :meth:`dict.viewkeys`, 
      :meth:`dict.viewvalues` e :meth:`dict.viewitems` são chamados de visões
      dicionários.  São sequências que verão as alterações no dicionário
      correspondente.  Para forçar as visões dicionários a se tornarem listas
      de fato utilize ``list(dictview)``.  Veja :ref:`dict-views`.

   máquina virtual
      Um computador definido inteirmente em software. A máquina virtual do
      Python executa :term:`bytecode` gerado pelo compilador de bytecode.

   Zen do Python
      Uma listagem dos princípios e filosofias de desenvolvimento que são úteis
      na compreensão e utilização da linguagem.  A listagem pode ser consultada
      digitando-se "``import this``" no prompt interativo.

