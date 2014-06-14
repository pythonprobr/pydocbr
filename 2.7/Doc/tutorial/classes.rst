.. _tut-classes:

*******
Classes
*******

Em comparação com outras linguagens, o mecanismo de classes de Python introduz
a programação orientada a objetos sem acrescentar muitas novidades de sintaxe
ou semântica. É uma mistura de mecanismos equivalentes encontrados em C++ e
Modula-3. As classes em Python oferecem todas as características tradicionais
da programação a orientada a objetos: o mecanismo de herança permite múltiplas
classes base (herança múltipla), uma classe derivada pode sobrescrever
quaisquer métodos de uma classe ancestral, e um método pode invocar outro
método homônimo de uma classe ancestral. Objetos podem armazenar uma
quantidade arbitrária de dados de qualquer tipo. Assim como acontece com os
módulos, as classes fazem parte da natureza dinâmica de Python: são criadas em
tempo de execução, e podem ser alteradas após sua criação.

Usando a terminologia de C++, todos os membros de uma classe (incluindo dados)
são públicos, e todos as funções membro são virtuais. Como em Modula-3, não
existem atalhos para referenciar membros do objeto de dentro dos seus métodos.
Um método (função definida em uma classe) é declarado com um primeiro
argumento explícito representando o objeto (instância da classe), que é
fornecido implicitamente pela invocação. Como em Smalltalk, classes são
objetos. Isso fornece uma semântica para importar e renomear. Ao contrário de
C++ ou Modula-3, tipos pré-definidos podem ser utilizados como classes base
para extensões de usuário por herança. Como em C++, mas diferentemente de
Modula-3, a maioria dos operadores (aritméticos, indexação,etc) podem ser
redefinidos para instâncias de classe.

(Na falta de uma terminologia universalmente aceita para falar sobre classes,
ocasionalmente farei uso de termos comuns em Smalltalk ou C++. Eu usaria
termos de Modula-3, já que sua semântica é mais próxima a de Python, mas creio
que poucos leitores já ouviram falar dessa linguagem.)


.. _tut-object:

Uma palavra sobre nomes e objetos
=================================

Objetos têm individualidade, e vários nomes (inclusive em diferentes escopos)
podem estar vinculados a um mesmo objeto. Isso é chamado de *aliasing* em
outras linguagens. (N.d.T. *aliasing* é, literalmente, "apelidamento": um
mesmo objeto pode ter vários apelidos.) À primeira vista, esta característica
não é muito apreciada, e pode ser seguramente ignorada ao lidar com tipos
imutáveis (números, strings, tuplas). Entretanto, aliasing pode ter um efeito
inesperado sobre a semântica de código Python envolvendo objetos mutáveis como
listas, dicionários e a maioria dos outros tipos. Isso pode ser usado em
benefício do programa, porque os *aliases* (apelidos) funcionam de certa forma
como ponteiros. Por exemplo, passar um objeto como argumento é barato, pois só
um ponteiro é passado na implementação; e se uma função modifica um objeto
passado como argumento, o invocador verá a mudança --- isso elimina a
necessidade de ter dois mecanismos de passagem de parâmetros como em Pascal.

N.d.T. Na terminologia de C++ e Java, o que o parágrafo acima denomina
"apelidos" são identificadores de referências (variáveis de referência), e os
ponteiros são as próprias referências. Se uma variável ``a`` está associada a
um objeto qualquer, informalmente dizemos que a variável "contém" o objeto,
mas na realidade o objeto existe independente da variável, e o conteúdo da
variável é apenas uma referência (um ponteiro) para o objeto. O *aliasing*
ocorre quando existem diversas variáveis, digamos ``a``, ``b`` e ``c``,
apontando para o mesmo objeto.

.. _tut-scopes:

Escopos e *namespaces*
======================

Antes de introduzir classes, é preciso falar das regras de escopo em Python.
Definições de classe fazem alguns truques com *namespaces* (espaços de nomes).
Portanto, primeiro é preciso entender claramente como escopos e *namespaces*
funcionam. Esse conhecimento é muito útil para o programador avançado em
Python.

Vamos começar com algumas definições.

Um *namespace* (ou espaço de nomes) é um mapeamento que associa nomes a
objetos. Atualmente, são implementados como dicionários em Python, mas isso
não é perceptível (a não ser pelo desempenho), e pode mudar no futuro.
Exemplos de espaços de nomes são: o conjunto de nomes pré-definidos (funções
como :func:`abs` e as exceções embutidas); nomes globais em um módulo; e nomes
locais na invocação de uma função. De uma certa forma, os atributos de um
objeto também formam um espaço de nomes. O mais importante é saber que não
existe nenhuma relação entre nomes em espaços distintos. Por exemplo, dois
módulos podem definir uma função de nome ``maximize`` sem confusão ---
usuários dos módulos devem prefixar a função com o nome do módulo para evitar
colisão.

A propósito, utilizo a palavra *atributo* para qualquer nome depois de um
ponto. Na expressão ``z.real``, por exemplo, ``real`` é um atributo do objeto
``z``. Estritamente falando, referências para nomes em módulos são atributos:
na expressão ``nomemod.nomefunc``, ``nomemod`` é um objeto módulo e
``nomefunc`` é um de seus atributos. Neste caso, existe um mapeamento direto
entre os os atributos de um módulo e os nomes globais definidos no módulo:
eles compartilham o mesmo espaço de nomes! [#]_

Atributos podem ser somente para leitura ou para leitura e escrita. No segundo
caso, é possível atribuir um novo valor ao atributo. (N.d.T. Também é possível
criar novos atributos.) Atributos de módulos são passíveis de atribuição: você
pode escrever ``nomemod.a_reposta = 42``. Atributos que aceitam escrita também
podem ser apagados através do comando :keyword:`del`. Por exemplo, ``del
nomemod.a_reposta`` remove o atributo :attr:`a_resposta` do objeto
referenciado por ``nomemod``.

Espaços de nomes são criados em momentos diferentes e possuem diferentes
ciclos de vida. O espaço de nomes que contém os nomes embutidos é criado
quando o interpretador inicializa e nunca é removido. O espaço de nomes global
de um módulo é criado quando a definição do módulo é lida, e normalmente duram
até a terminação do interpretador. Os comandos executados pela invocação do
interpretador, pela leitura de um script com programa principal, ou
interativamente, são parte do módulo chamado :mod:`__main__`, e portanto
possuem seu próprio espaço de nomes. (Os nomes embutidos possuem seu
próprio espaço de nomes no módulo chamado :mod:`__builtin__`.).

O espaço de nomes local de uma função é criado quando a função é invocada, e
apagado quando a função retorna ou levanta uma exceção que não é tratada na
própria função. (Na verdade, uma forma melhor de descrever o que realmente
acontece é que o espaço de nomes local é "esquecido" quando a função termina.)
Naturalmente, cada invocação recursiva de uma função tem seu próprio espaço de
nomes.

Um *escopo* (*scope*) é uma região textual de um programa Python onde um
espaço de nomes é diretamente acessível. Aqui, "diretamente acessível"
significa que uma referência sem um prefixo qualificador permite o acesso ao
nome.

Ainda que escopos sejam determinados estaticamente, eles são usados
dinamicamente. A qualquer momento durante a execução, existem no mínimo três
escopos diretamente acessíveis:

* o escopo mais interno (que é acessado primeiro) contendo nomes locais;
* os escopos das funções que envolvem a função atual, que são acessados a
  partir do escopo mias próximo, contém nomes não-locais mas também
  não-globais;
* o penúltimo escopo contém os nomes globais do módulo atual;
* e o escopo mais externo (acessado por último) contém os nomes das funções
  embutidas e demais objetos pré-definidos do interpretador.

Se um nome é declarado no escopo global, então todas as referências e
atribuições valores vão diretamente para o escopo intermediário que contém os
nomes globais do módulo. Caso contrário, todas as variáveis encontradas fora
do escopo mais interno são apenas para leitura (a tentativa de atribuir
valores a essas variáveis irá simplesmente criar uma *nova* variável local, no
escopo interno, não alterando nada na variável de nome idêntico fora dele).

Normalmente, o escopo local referencia os nomes locais da função corrente no
texto do programa. Fora de funções, o escopo local referencia os nomes do
escopo global: espaço de nomes do módulo. Definições de classes adicionam um
outro espaço de nomes ao escopo local.

É importante perceber que escopos são determinados estaticamente, pelo texto
do código fonte: o escopo global de uma função definida em um módulo é o
espaço de nomes deste módulo, sem importar de onde ou por qual apelido a
função é invocada. Por outro lado, a busca de nomes é dinâmica, ocorrendo
durante a execução. Porém, a evolução da linguagem está caminhando para uma
resolução de nomes estática, em "tempo de compilação" (N.d.T. quando um módulo
é carregado ele é compilado em memória), portanto não conte com a resolução
dinâmica de nomes! (De fato, variáveis locais já são resolvidas
estaticamente.)

Uma peculiaridade de Python é que atribuições ocorrem sempre no escopo mais
interno, exceto quando o comando :keyword:`global` é usado. Atribuições não
copiam dados, apenas associam nomes a objetos. O mesmo vale para remoções: o
comando ``del x`` remove o vínculo de ``x`` do espaço de nomes do escopo
local. De fato, todas as operações que introduzem novos nomes usam o escopo
local. Em particular, instruções :keyword:`import` e definições de funções
associam o nome módulo ou da função ao escopo local. (A palavra reservada
:keyword:`global` pode ser usada para indicar que certas variáveis residem no
escopo global ao invés do local.)


.. _tut-firstclasses:

Primeiro contato com classes
============================

Classes introduzem novidades sintáticas, três novos tipos de objetos, e também
alguma semântica nova.


.. _tut-classdefinition:

Sintaxe de definição de classe
------------------------------

A forma mais simples de definir uma classe é::

   class NomeDaClasse:
       <instrução-1>
       .
       .
       .
       <instrução-N>

Definições de classes, assim como definições de funções (instruções
:keyword:`def`), precisam ser executados antes que tenham qualquer efeito.
(Por exemplo, você pode colocar uma definição de classe dentro de teste
condicional :keyword:`if` ou dentro de uma função.)

Na prática, as instruções dentro da definição de uma classe em geral serão
definições de funções, mas outras instruções são permitidas, e às vezes são
bem úteis --- voltaremos a este tema depois. Definições de funções dentro da
classe normalmente têm um lista peculiar de parâmetros formais determinada
pela convenção de chamada a métodos --- isso também será explicado mais tarde.

Quando se inicia a definição de classe, um novo namespace é criado, e usado
como escopo local --- assim, todas atribuições a variáveis locais ocorrem
nesse namespace. Em particular, funções definidas aqui são vinculadas a nomes
nesse escopo.

Quando o processamento de uma definição de classe é completado (normalmente,
sem erros), um *objeto classe* é criado. Este objeto encapsula o conteúdo do
espaço de nomes criado pela definição da classe; aprenderemos mais sobre
objetos classe na próxima seção. O escopo local que estava vigente antes da
definição da classe é reativado, e o objeto classe é vinculado ao
identificador da classe nesse escopo (no exemplo acima, :class:`NomeDaClasse`
é o identificador da classe).


.. _tut-classobjects:

Objetos classe
--------------

Objetos classe suportam dois tipos de operações: *referências a atributos* e
*instanciação*.

*Referências a atributos* de classe utilizam a sintaxe padrão utilizada para
quaisquer referências a atributos em Python: ``obj.nome``. Atributos válidos
são todos os nomes presentes dentro do namespace da classe quando o objeto
classe foi criado. Portanto, se a definição da classe foi assim::


   class MinhaClasse:
       """Um exemplo simples de classe"""
       i = 12345
       def f(self):
           return 'olá, mundo'

então ``MinhaClasse.i`` e ``MinhaClasse.f`` são referências válidas, que
acessam, respectivamente, um inteiro e um objeto função. É possível mudar os
valores dos atributos da classe, ou mesmo criar novos atributos, fazendo uma
atribuição simples assim: ``MinhaClasse.i = 10``. O nome ``__doc__``
identifica outro atributo válido da classe, referenciando a *docstring*
associada à ela: ``"Um exemplo simples de classe"``.

Para *instanciar* uma classe, usa-se a sintaxe de invocar uma função. Apenas
finja que o objeto classe do exemplo é uma função sem parâmetros, que devolve
uma nova instância da classe. Continuando o exemplo acima::

   x = MinhaClasse()

cria uma nova *instância* da classe e atribui o objeto resultante à variável
local ``x``.

A operação de instanciação ("invocar" um objeto classe) cria um objeto vazio.
Muitas classes preferem criar novos objetos com um estado inicial
predeterminado. Para tanto, a classe pode definir um método especial
chamado :meth:`__init__`, assim::

   def __init__(self):
       self.dados = []

Quando uma classe define um método :meth:`__init__`, o processo de
instanciação automaticamente invoca :meth:`__init__` sobre a instância recém
criada. Em nosso exemplo, uma nova instância já inicializada pode ser obtida
desta maneira::

   x = MinhaClasse()

Naturalmente, o método :meth:`__init__` pode ter parâmetros para maior
flexibilidade. Neste caso, os argumentos fornecidos na invocação da classe
serão passados para o método :meth:`__init__`. Por exemplo::

   >>> class Complexo:
   ...     def __init__(self, parte_real, parte_imag):
   ...         self.r = parte_real
   ...         self.i = parte_imag
   ...
   >>> x = Complexo(3.0, -4.5)
   >>> x.r, x.i
   (3.0, -4.5)


.. _tut-instanceobjects:

Instâncias
----------

Agora, o que podemos fazer com instâncias? As únicas operações reconhecidas
por instâncias são referências a atributos. Existem dois tipos de nomes de
atributos válidos: atributos de dados (*data attributes*) e métodos.

Atributos de dados correspondem a "variáveis de instância" em Smalltalk, e a
"data members" em C++. Atributos de dados não precisam ser declarados.
Assim como variáveis locais, eles passam a existir na primeira vez em que é
feita uma atribuição. Por exemplo, se ``x`` é uma instância da
:class:`MinhaClasse` criada acima, o próximo trecho de código irá exibir o
valor ``16``, sem deixar nenhum rastro na instância (por causa do uso de
:keyword:`del`)::

   x.contador = 1
   while x.contador < 10:
       x.contador = x.contador * 2
   print x.contador
   del x.contador

O outro tipo de referências a atributos são métodos. Um método é uma função
que "pertence" a uma instância. (Em Python, o termo método não é aplicado
exclusivamente a instâncias de classes definidas pelo usuário: outros tipos de
objetos também podem ter métodos. Por exemplo, listas possuem os métodos
append, insert, remove, sort, etc. Porém, na discussão a seguir usaremos o
termo método apenas para se referir a métodos de classes definidas pelo
usuário. Seremos explícitos ao falar de outros métodos.)


.. index:: object: method

Nomes de métodos válidos de uma instância dependem de sua classe. Por
definição, cada atributo de uma classe que é uma função corresponde a um
método das instâncias. Em nosso exemplo, ``x.f`` é uma referência de método
válida já que ``MinhaClasse.f`` é uma função, enquanto ``x.i`` não é, já que
``MinhaClasse.i`` não é uma função. Entretanto, ``x.f`` não é o mesmo que
``MinhaClasse.f``. A referência ``x.f`` acessa um objeto método (*method
object*), e a ``MinhaClasse.f`` acessa um objeto função.


.. _tut-methodobjects:


Objetos método
--------------

Normalmente, um método é invocado imediatamente após ser acessado::

   x.f()

No exemplo :class:`MinhaClasse` o resultado da expressão acima será a string
``'olá, mundo'``. No entanto, não é obrigatório invocar o método
imediatamente: como ``x.f`` é também um objeto (um objeto método), ele pode
atribuído a uma variável invocado depois. Por exemplo::

   xf = x.f
   while True:
       print xf()

Esse código exibirá o texto ``'olá, mundo'`` até o mundo acabar.

O que ocorre precisamente quando um método é invocado? Você deve ter notado
que ``x.f()`` foi chamado sem nenhum parâmetro, porém a definição da função
:meth:`f` especificava um parâmetro. O que aconteceu com esse parâmetro?
Certamente Python levanta uma exceção quando uma função que declara um
parâmetro é invocada sem nenhum argumento --- mesmo que o argumento não
seja usado no corpo da função...

Talvez você já tenha adivinhado a resposta: o que os métodos têm de especial é
que eles passam o objeto (ao qual o método está vinculado) como primeiro
argumento da função definida na classe. No nosso exemplo, a chamada ``x.f()``
equivale exatamente ``MinhaClasse.f(x)``. Em geral, chamar um método com uma
lista de *n* argumentos é equivalente a chamar a função na classe
correspondente passando a instância como o primeiro argumento antes dos demais
*n* argumentos.

Se você ainda não entendeu como métodos funcionam, talvez uma olhada na
implementação de Python sirva para clarear as coisas. Quando um atributo de
instância é referenciado e não é um atributo de dado, a busca continua na
classe. Se o nome indica um atributo de classe válido que é um objeto função,
um objeto método é criado pela composição da instância alvo e do objeto
função. Quando o método é invocado com uma lista de argumentos, uma nova lista
de argumentos é criada inserindo a instância na posição 0 da lista.
Finalmente, o objeto função --- empacotado dentro do objeto método --- é
invocado com a nova lista de argumentos.


.. _tut-remarks:

Observações aleatórias
======================

.. These should perhaps be placed more carefully...

Atributos de dados sobrescrevem atributos métodos homônimos. Para evitar
conflitos de nome acidentais, que podem gerar bugs de difícil rastreio em
programas extensos, é sábio adotar algum tipo de convenção que minimize a
chance de conflitos. Convenções comuns incluem: definir nomes de métodos com
inicial maiúscula, prefixar atributos de dados com uma string única (quem sabe
"_" [*underscore* ou sublinhado]), ou usar sempre verbos para nomear métodos
e substantivos para atributos de dados.

Atributos de dados podem ser referenciados por métodos da própria instância,
bem como por qualquer outro usuário do objeto (também chamados "clientes" do
objeto). Em outras palavras, classes não servem para implementar tipos
puramente abstratos de dados. De fato, nada em Python torna possível assegurar
o encapsulamento de dados --- tudo é convenção. (Por outro lado, a
implementação de Python, escrita em C, pode esconder completamente detalhes de
um objeto ou controlar seu acesso, se necessário; isto pode ser utilizado por
extensões de Python escritas em C.)

Clientes devem utilizar atributos de dados com cuidado, pois podem bagunçar
invariantes assumidas pelos métodos ao esbarrar em seus atributos de dados.
Note que clientes podem adicionar à vontade atributos de dados a uma instância
sem afetar a validade dos métodos, desde que seja evitado o conflito de nomes.
Novamente, uma convenção de nomenclatura poupa muita dor de cabeça.

.. LR: inverti a ordem dos dois próximos parágrafos para falar primeiro do
   self e poder mencioná-lo explicitamente no parágrafo seguinte.

Frequentemente, o primeiro argumento de um método é chamado ``self``. Isso não
passa de uma convenção: o identificador ``self`` não é uma palavra reservada
nem possui qualquer significado especial em Python. Mas note que, ao seguir
essa convenção, seu código se torna legível por uma grande comunidade de
desenvolvedores Python e é possível que alguma *IDE* dependa dessa convenção
para analisar seu código.

Não existe atalho para referenciar atributos de dados (ou outros métodos!) de
dentro de um método: sempre é preciso fazer referência explícita ao ``self.``
para acessar qualquer atributo da instância. Em minha opinião isso aumenta a
legibilidade dos métodos: não há como confundir uma variável local com um
atributo da instância quando lemos rapidamente um método desconhecido.

Qualquer objeto função que é atributo de uma classe, define um método para as
instâncias desta classe. Não é necessário que a definição da função esteja
textualmente embutida na definição da classe. Atribuir um objeto função a uma
variável local da classe é válido. Por exemplo::


   # Função definida fora da classe
   def f1(self, x, y):
       return min(x, x+y)

   class C:
       def g(self):
           return 'olá mundo'
       h = g

   C.f = f1

Agora ``f``, ``g`` e ``h`` são todos atributos da classe :class:`C` que
referenciam funções, e consequentemente são todos métodos de instâncias da
classe :class:`C`, onde ``h`` é equivalente a ``g``. No entanto, essa prática
serve apenas para confundir o leitor do programa.

Métodos podem chamar outros métodos como atributos do argumento ``self``::

   class Saco:
       def __init__(self):
           self.data = []
       def adicionar(self, x):
           self.data.append(x)
       def adicionar2vezez(self, x):
           self.adicionar(x)
           self.adicionar(x)


Métodos podem referenciar nomes globais da mesma forma que funções comuns. O
escopo global associado a um método é o módulo contendo sua a definição de sua
classe (a classe propriamente dita nunca é usada como escopo global!). Ainda
que seja raro justificar o uso de dados globais em um método, há diversos usos
legítimos do escopo global. Por exemplo, funções e módulos importados no
escopo global podem ser usados por métodos, bem como as funções e classes
definidas no próprio escopo global. Provavelmente, a classe contendo o método
em questão também foi definida neste escopo global. Na próxima seção veremos
razões pelas quais um método pode querer referenciar sua própria classe.

Todo valor em Python é um objeto, e portanto tem uma *classe* (também
conhecida como seu tipo, ou *type*). A classe de um objeto pode ser
referenciada como ``objeto.__class__``.


.. _tut-inheritance:

Herança
=======

Obviamente, uma característica não seria digna do nome "classe" se não
suportasse herança. A sintaxe para uma classe derivada é assim::

   class NomeClasseDerivada(NomeClasseBase):
       <instrução-1>
       .
       .
       .
       <instrução-N>

O identificador :class:`NomeClasseBase` deve estar definido no escopo que
contém a definição da classe derivada. No lugar do nome da classe base, também
são aceitas outras expressões. Isso é muito útil, por exemplo, quando a classe
base é definida em outro módulo::


   class NomeClasseDerivada(nomemod.NomeClasseBase):

A execução de uma definição de classe derivada procede da mesma forma que a de
uma classe base. Quando o objeto classe é construído, a classe base é
lembrada. Isso é utilizado para resolver referências a atributos. Se um
atributo requisitado não for encontrado na classe, ele é procurado na classe
base. Essa regra é aplicada recursivamente se a classe base por sua vez for
derivada de outra.

Não há nada de especial sobre instanciação de classes derivadas.
``NomeClasseDerivada()`` cria uma nova instância da classe. Referências a
métodos são resolvidas da seguinte forma: o atributo correspondente é
procurado através da cadeia de classes base, e referências a métodos são
válidas desde se essa procura produza um objeto função.

Classes derivadas podem sobrescrever métodos das suas classes base. Uma vez
que métodos não possuem privilégios especiais quando invocam outros métodos
no mesmo objeto, um método na classe base que invocava um outro método da
mesma classe base, pode efetivamente acabar invocando um método sobreposto por
uma classe derivada. (Para programadores C++ isso significa que todos os
métodos em Python são realmente virtuais.)

Em uma classe derivada, um método que sobrescreva outro pode desejar na
verdade estender, ao invés de substituir, o método sobrescrito de mesmo nome
na classe base. A maneira mais simples de implementar esse comportamento é
chamar diretamente o método na classe base, passando explicitamente a
instância como primeiro argumento::

  NomeClasseBase.nomemetodo(self, argumento1, argumento2)

Às vezes essa forma de invocação pode ser útil até mesmo em código que apenas
usa a classe, sem estendê-la. (Note que para esse exemplo funcionar,
``NomeClasseBase`` precisa estar definida ou importada diretamente no escopo
global do módulo.)

Python tem duas funções embutidas que trabalham com herança:

* Use :func:`isinstance` para verificar o tipo de uma instância:
  ``isinstance(obj, int)`` será ``True`` somente se ``obj.__class__`` é
  a classe :class:`int` ou alguma classe derivada de :class:`int`.

* Use :func:`issubclass` para verificar herança entre classes:
  ``issubclass(bool, int)`` é ``True`` porque :class:`bool` é uma subclasse
  de :class:`int`.  Entretanto, ``issubclass(unicode, str)`` é ``False``
  porque :class:`unicode` não é uma subclasse :class:`str` (essas duas classes
  derivam da mesma classe base: :class:`basestring`).


.. _tut-multiple:

Herança múltipla
----------------

Python também suporta uma forma limitada de herança múltipla. Uma definição de
classe com várias classes base tem esta forma::


   class NomeClasseDerivada(Base1, Base2, Base3):
       <instrução-1>
       .
       .
       .
       <instrução-N>


A única regra que precisa ser explicada é a semântica de resolução para as
referências a atributos herdados. Em classes no estilo antigo (old-style
classes [#]_), a busca é feita em profundidade e da esquerda para a direita.
Logo, se um atributo não é encontrado em :class:`NomeClasseDerivada`, ele é
procurado em :class:`Base1`, e recursivamente nas classes bases de
:class:`Base1`, e apenas se não for encontrado lá a busca prosseguirá em
:class:`Base2`, e assim sucessivamente. (Para algumas pessoas a busca em
largura --- procurar antes em :class:`Base2` e :class:`Base3` do que nos
ancestrais de :class:`Base1` --- parece mais natural. Entretanto, seria
preciso conhecer toda a hierarquia de :class:`Base1` para evitar um conflito
com um atributo de :class:`Base2`. Na prática, a busca em profundidade não
diferencia entre atributos diretos ou herdados de :class:`Base1`.)

Em :term:`new-style classes <new-style class>`), a ordem de resolução de
métodos muda dinamicamente para suportar invocações cooperativas via
:func:`super`. Esta abordagem é conhecida em certas outras linguagens que têm
herança múltipla como *call-next-method* (invocar próximo método) e é mais
poderoso que o mecanismo de invocação via super encontrado em linguagens de
herança simples.

A ordenação dinâmica é necessária nas classes new-style, porque todos os casos
de herança múltipla apresentam uma ou mais estruturas de diamante (um
losango no grafo de herança, onde pelo menos uma das superclasses pode ser
acessada através de vários caminhos a partir de uma classe derivada). Por
exemplo, todas as classes new-style herdam de :class:`object`, portanto,
qualquer caso de herança múltipla envolvendo apenas classes new-style fornece
mais de um caminho para chegar a :class:`object`. Para evitar que uma classe
base seja acessada mais de uma vez, o algoritmo dinâmico lineariza a ordem de
pesquisa de uma maneira que:

* preserva a ordem da esquerda para a direita especificada em cada classe;

* acessa cada classe base apenas uma vez;

* é monotônica (significa que uma classe pode ser derivada sem que isso
  afete a ordem de precedência de suas classes base).

Juntas, essas características tornam possível criar classes confiáveis e
extensíveis usando herança múltipla. Para mais detalhes, veja `The Python 2.3
Method Resolution Order`_

.. _The Python 2.3 Method Resolution Order: http://www.python.org/download/releases/2.3/mro/


.. _tut-private:

Variáveis privadas
==================

Variáveis instância "privadas", que não podem ser acessados ​​exceto em
métodos do próprio objeto não existem em Python. No entanto, existe uma
convenção que é seguida pela maioria dos programas em Python: um nome
prefixado com um sublinhado (por exemplo: ``_spam`` ) deve ser tratado como
uma parte não-pública da API (seja ele uma função, um método ou um atributo de
dados). Tais nomes devem ser considerados um detalhe de implementação e
sujeito a alteração sem aviso prévio.

Uma vez que existe um caso de uso válido para a definição de atributos
privados em classes (especificamente para evitar conflitos com nomes definidos
em subclasses), existe um suporte limitado a identificadores privados em
classes, chamado :dfn:`name mangling` (literalmente: desfiguração de nomes).
Qualquer identificador no formato ``__spam`` (no mínimo dois underscores ``_``
no prefixo e no máximo um sufixo) é substituído por ``_nomeclasse__spam``,
onde ``nomeclasse`` é o nome da classe corrente (exceto quando o nome da classe
é prefixado com um ou mais underscores ``_``; nesse caso eles são omitidos).
Essa desfiguração independe da posição sintática do identificador, desde que
ele apareça dentro da definição de uma classe.

A desfiguração de nomes é útil para que subclasses possam sobrescrever métodos
sem quebrar invocações de métodos dentro de outra classe. Por exemplo::


   class Mapping:
       def __init__(self, iterable):
           self.items_list = []
           self.__update(iterable) # referencia ao nome privado

       def update(self, iterable): # parte da API, pode ser sobrescrito
           for item in iterable:
               self.items_list.append(item)

       __update = update   # nome privado do método update

   class MappingSubclass(Mapping):

       def update(self, keys, values):
           # altera a assinatura de update()
           # mas não quebra o __init__() original
           for item in zip(keys, values):
               self.items_list.append(item)

Note que as regras de desfiguração de nomes foram projetadas para evitar
acidentes; ainda é possível acessar e alterar intencionalmente variáveis
protegidas por esse mecanismo. De fato isso pode ser útil em certas
circunstâncias, por exemplo, durante uma sessão com o :mod:`pdb`, o
depurador interativo do Python.

Código passado para ``exec``, ``eval()`` ou ``execfile()`` não considera o
nome da classe que invocou como sendo a classe corrente; isso é semelhante ao
funcionamento da declaração :keyword:`global`, cujo efeito se aplica somente
ao código que é byte-compilado junto. A mesma restrição se aplica as funções
``getattr()``, ``setattr()`` e ``delattr()``, e quando acessamos diretamente o
``__dict__`` da classe: lá as chaves já estão desfiguradas.


.. _tut-odds:

Miscelânea
==========

Às vezes, é útil ter um tipo semelhante ao "record" de Pascal ou ao "struct"
de C, para agrupar alguns itens de dados. Uma definição de classe vazia
funciona bem para este fim::

   class Empregado:
       pass

   joao = Empregado() # Criar um registro de empregado vazio

   # Preencher campos do registrp
   joao.nome = u'João da Silva'
   joao.depto = u'laboratório de informática'
   joao.salario = 1000

Um trecho de código Python que espera um tipo abstrato de dado em particular,
pode receber, ao invés disso, um objeto que emula os métodos que aquele tipo
suporta. Por exemplo, se você tem uma função que formata dados obtidos de um
objeto arquivo, pode passar como argumento para essa função uma instância de
uma classe que implemente os métodos :meth:`read` e :meth:`readline` que obtém
os dados lendo um buffer ao invés de ler um arquivo real. (N.d.T. isso é um
exemplo de "duck typing" [#]_\ .)


.. (Unfortunately, this technique has its limitations: a class can't define
   operations that are accessed by special syntax such as sequence subscripting
   or arithmetic operators, and assigning such a "pseudo-file" to sys.stdin will
   not cause the interpreter to read further input from it.)

Objetos método têm seus próprios atributos: ``m.im_self`` é uma referência à
instância vinculada ao método :meth:`m`, e ``m.im_func`` é o objeto função
(atributo da classe) que corresponde ao método.


.. _tut-exceptionclasses:

Exceções também são classes
===========================

Exceções definidas pelo usuário são identificadas por classes. Através deste
mecanismo é possível criar hierarquias extensíveis de exceções.

Há duas novas formas semanticamente válidas para o comando :keyword:`raise`::

   raise Classe, instancia

   raise instancia

Na primeira forma, ``instancia`` deve ser uma instância de :class:`Classe` ou
de uma classe derivada dela. A segunda forma é um atalho para::


   raise instancia.__class__, instancia


Em uma cláusula :keyword:`except`, uma classe é compatível com a exceção
levantada se é a mesma classe ou uma classe ancestral dela (mas não o
contrário: uma cláusula :keyword:`except` que menciona uma classe derivada
daquela que foi levantada não vai capturar tal exceção). No exemplo a seguir
será exibido B, C e D nessa ordem::


   class B:
       pass
   class C(B):
       pass
   class D(C):
       pass

   for c in [B, C, D]:
       try:
           raise c()
       except D:
           print "D"
       except C:
           print "C"
       except B:
           print "B"

Se a ordem das cláusulas fosse invertida (``except B`` no início), seria
exibido B, B, B --- somente a primeira cláusula :keyword:`except` compatível é
ativada.

No caso de uma exceção não tratada, quando a mensagem de erro é gerada, o nome
da classe da exceção é exibido, seguido de ``': '`` (dois pontos e um espaço),
e finalmente aparece a instância da exceção convertida para string através da
função embutida :func:`str`.


.. _tut-iterators:

Iteradores
==========

Você já deve ter notado que pode usar laços :keyword:`for` com a maioria das
coleções em Python::

   for elemento in [1, 2, 3]:
       print elemento
   for elemento in (1, 2, 3):
       print elemento
   for chave in {'one':1, 'two':2}:
       print chave
   for car in "123":
       print car
   for linha in open("myfile.txt"):
       print linha


Esse estilo de acesso é limpo, conciso e conveniente. O uso de iteradores
promove uma unificação ao longo de toda a linguagem. Nos bastidores, o comando
:keyword:`for` aplica a função embutida :func:`iter` à coleção. Essa função
devolve um iterador que define o método :meth:`next`, que acessa os elementos
da coleção em sequência, um por vez. Quando acabam os elementos, :meth:`next`
levanta uma exceção :exc:`StopIteration`, indicando que o laço :keyword:`for`
deve encerrar. Este exemplo mostra como tudo funciona::


   >>> s = 'abc'
   >>> it = iter(s)
   >>> it
   <iterator object at 0x00A1DB50>
   >>> it.next()
   'a'
   >>> it.next()
   'b'
   >>> it.next()
   'c'
   >>> it.next()
   Traceback (most recent call last):
     File "<stdin>", line 1, in ?
       it.next()
   StopIteration

Observando o mecanismo por trás do protocolo dos iteradores, fica fácil
adicionar esse comportamento às suas classes. Defina uma método
:meth:`__iter__` que devolve um objeto que tenha um método :meth:`next`. Se
uma classe já define :meth:`next`, então :meth:`__iter__` pode simplesmente
devolver ``self``::

   class Inversor:
       """Iterador para percorrer uma sequencia de trás para frente."""
       def __init__(self, data):
           self.data = data
           self.index = len(data)
       def __iter__(self):
           return self
       def next(self):
           if self.index == 0:
               raise StopIteration
           self.index = self.index - 1
           return self.data[self.index]

::

   >>> inv = Inversor('spam')
   >>> iter(inv)
   <__main__.Reverse object at 0x00A1DB50>
   >>> for car in inv:
   ...     print car
   ...
   m
   a
   p
   s


.. _tut-generators:

Geradores
=========

Funções geradoras (:term:`generator <generator>`) são uma maneira fácil e
poderosa de criar um iterador. Uma função geradora é escrita como uma função
normal, mas usa o comando :keyword:`yield` para produzir resultados. (N.d.T.
Quando invocada, a função geradora produz um objeto gerador.) Cada vez que
:meth:`next` é invocado, o gerador continua a partir de onde parou (ele mantem
na memória seus dados internos e a próxima instrução a ser executada). Um
exemplo mostra como geradores podem ser muito fáceis de criar::


   def inversor(data):
       for index in range(len(data)-1, -1, -1):
           yield data[index]

::

   >>> for char in inversor('golf'):
   ...     print char
   ...
   f
   l
   o
   g

N.d.T. Veja como a função geradora produz um objeto gerador, que implementa
o protocolo de iterador::

   >>> gerador = inversor('golf')
   >>> gerador
   <generator object inversor at 0xb7797a2c>
   >>> gerador.next()
   'f'
   >>> gerador.next()
   'l'
   >>> gerador.next()
   'o'
   >>> gerador.next()
   'g'
   >>> gerador.next()
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   StopIteration


Qualquer coisa feita com geradores também pode ser feita com iteradores
baseados numa classe, como descrito na seção anterior. O que torna geradores
tão compactos é que os métodos :meth:`__iter__` e :meth:`next` são criados
automaticamente.

Outro ponto chave é que as variáveis locais e o estado da execução são
preservados automaticamente entre as chamadas de :meth:`next`. Isto torna a
função mais fácil de escrever e muito mais clara do que uma implementação
usando variáveis de instância como ``self.index`` e ``self.data``.

Além disso, quando geradores terminam, eles levantam :exc:`StopIteration`
automaticamente. Combinados, todos estes aspectos tornam a criação de
iteradores tão fácil quanto escrever uma função normal.



.. _tut-genexps:

Expressões geradoras
====================

Alguns geradores simples podem ser escritos sucintamente como expressões
usando uma sintaxe similar a de abrangência de listas (*list comprehensions*),
mas com parênteses ao invés de colchetes. Essas expressões são destinadas a
situações em que o gerador é usado imediatamente como argumento para função.
Uma expressão geradora é mais compacta, porém menos versátil do que uma função
geradora, e tende a usar muito menos memória do que a abrangência de lista
equivalente.


Examplos::

   >>> sum(i*i for i in range(10))          # soma de quadrados
   285

   >>> xvec = [10, 20, 30]
   >>> yvec = [7, 5, 3]
   >>> sum(x*y for x,y in zip(xvec, yvec))  # produto escalar (dot product)
   260

   >>> from math import pi, sin
   >>> senos = dict((x, sin(x*pi/180)) for x in range(0, 91))

   >>> palavras_unicas = set(palavra for linha in pagina
   ...                               for palavra in linha.split())

   >>> melhor_aluno = max((aluno.media, aluno.nome) for aluno in formados)

   >>> data = 'golf'
   >>> list(data[i] for i in range(len(data)-1,-1,-1))
   ['f', 'l', 'o', 'g']



.. rubric:: Notas

.. [#] Exceto por um detalhe. Objetos módulo têm um atributo secreto apenas para
   leitura chamado :attr:`__dict__` que é uma referência ao dicionário usado para
   implementar o namespace do módulo; o nome :attr:`__dict__` é um atributo mas
   não um nome global. Obviamente, acessar esse atributo viola a abstração da
   implementação de namespaces, e é algo que só deve ser feito por ferramentas
   especiais, como depuradores "post-mortem".

.. [#] N.d.T. Os termos :term:`new-style class <new-style class>` e
   "old-style class" referem-se a duas implementações de classes que
   convivem desde o Python 2.2. A implementação mais antiga, "old-style
   classes" foi preservada até o Python 2.7 para manter a compatibilidade com
   bibliotecas e scripts antigos, mas deixou de existir a partir do Python
   3.0. As "new-style classes" suportam o mecanismo de descritores, usado para
   implementar propriedades (*properties*). Recomenda-se que todo código
   Python novo use apenas "new-style classes".

   Desde o Python 2.2, a forma de declarar uma classe determina se ela usa a
   implementação nova ou antiga. Qualquer classe derivada direta ou
   indiretamente de :class:`object` é uma classe "new-style". Objetos classe
   novos são do tipo ``type`` e objetos classe antigos são do tipo
   ``classobj``. Veja este exemplo::

      >>> class Nova(object):
      ...     pass
      ...
      >>> type(Nova)
      <type 'type'>
      >>> class Velha:
      ...     pass
      ...
      >>> type(Velha)
      <type 'classobj'>

   Note que a definição acima é recursiva. Em particular, uma classe
   que herda de uma classe antiga e de uma nova é uma classe "new-style",
   pois através da classe nova ela é uma subclasse indireta de :class:`object`.
   Não é uma boa prática misturar os dois estilos de classes, mas eis um
   exemplo para ilustrar esse ponto::

      >>> class Mista(Velha, Nova):
      ...     pass
      ...
      >>> type(Mista)
      <type 'type'>

   Para saber mais sobre as diferenças, veja `New Class vs Classic Class`_ no wiki
   do python.org ou artigo original de Guido van Rossum, `Unifying types and
   classes in Python 2.2`_.

.. _New Class vs Classic Class: http://wiki.python.org/moin/NewClassVsClassicClass
.. _Unifying types and classes in Python 2.2: http://www.python.org/download/releases/2.2.3/descrintro/

.. [#] N.d.T. Esse parágrafo descreve uma aplicação do conceito de "duck
   typing" (literalmente, "tipagem pato"), cuja ideia central é que os
   atributos e comportamentos de um objeto são mais importantes que seu tipo:
   "Quando vejo um pássaro que anda com um pato, nada como um pato, e grasna
   como um pato, chamo esse pássaro de pato." (James Whitcomb Riley). Segundo
   a Wikipedia_ (em inglês), a metáfora dos atributos de um pato no contexto
   de programação orientada a objetos foi usada pela primeira vez por
   Alex Martelli no grupo *comp.lang.python* em 26/jul/2000. O assunto da
   mensagem era polymorphism_.

.. _Wikipedia: http://en.wikipedia.org/wiki/Duck_typing#History
.. _polymorphism: http://groups.google.com/group/comp.lang.python/msg/e230ca916be58835
