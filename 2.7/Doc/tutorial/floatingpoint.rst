.. _tut-fp-issues:

*****************************************************
Aritmética de ponto flutuante: problemas e limitações
*****************************************************

.. sectionauthor:: Tim Peters <tim_one@users.sourceforge.net>


Números de ponto flutuante são representados no hardware do computador como frações binárias (base 2). Por exemplo, a fração decimal::

   0.125

tem o valor 1/10 + 2/100 + 5/1000, e da mesma maneira a fração binária::

   0.001

tem o valor 0/2 + 0/4 + 1/8.  Essas duas frações têm valores idênticos, a única
diferença real é que a primeira está representada na forma de frações base 10,
e a segunda na base 2.

Infelizmente, muitas frações decimais não podem ser representadas precisamente
como frações binárias. O resultado é que, em geral, os números decimais de
ponto flutuante que você digita acabam sendo armazenados de forma apenas
aproximada, na forma de números binários de ponto flutuante.

O problema é mais fácil de entender primeiro em base 10. Considere a fração
1/3. Podemos representá-la aproximadamente como uma fração base 10::

   0.3

ou melhor, ::

   0.33

ou melhor, ::

   0.333

e assim por diante. Não importa quantos dígitos você está disposto a escrever,
o resultado nunca será exatamente 1/3, mas será uma aproximação de cada vez
melhor de 1/3.

Da mesma forma, não importa quantos dígitos de base 2 você está disposto a
usar, o valor decimal 0.1 não pode ser representado exatamente como uma fração
de base 2. Em base 2, 1/10 é uma fração binária que se repete infinitamente::

   0.0001100110011001100110011001100110011001100110011...

Se limitamos a representação a qualquer número finito de bits, obtemos apenas
uma aproximação.

Em uma máquina típica rodando Python, há 53 bits de precisão disponível para
um ``float``, de modo que o valor armazenado internamente quando você digita
o número decimal ``0.1`` é esta fração binária::


   0.00011001100110011001100110011001100110011001100110011010

que chega perto, mas não é exatamente igual a 1/10.

É fácil esquecer que o valor armazenado é uma aproximação da fração decimal
original, devido à forma como floats são exibidos no interpretador interativo.
Python exibe apenas uma aproximação decimal do verdadeiro valor decimal da
aproximação binária armazenada pela máquina. Se Python exibisse o verdadeiro
valor decimal da aproximação binária que representa o decimal 0.1, teria
que mostrar::

   >>> 0.1
   0.1000000000000000055511151231257827021181583404541015625

Isso é bem mais dígitos do que a maioria das pessoas considera útil, então Python
limita o número de dígitos, apresentando em vez disso um valor arredondado::

   >>> 0.1
   0.1

É importante perceber que isso é, de fato, uma ilusão: o valor na máquina não
é exatamente 1/10, estamos simplesmente arredondando a exibição do verdadeiro
valor na máquina. Esse fato torna-se evidente logo que você tenta fazer
aritmética com estes valores::

   >>> 0.1 + 0.2
   0.30000000000000004

Note que esse é a própria natureza do ponto flutuante binário: não é um bug em
Python, e nem é um bug em seu código. Você verá o mesmo tipo de coisa em todas
as linguagens que usam as instruções de aritmética de ponto flutuante do
hardware (apesar de algumas linguagens não *mostrarem* a diferença, por
padrão, ou em todos os modos de saída).

Outras surpresas decorrem desse fato. Por exemplo, se tentar arredondar o
valor 2.675 para duas casas decimais, obterá esse resultado::

   >>> round(2.675, 2)
   2.67

A documentação da função embutida :func:`round` diz que ela arredonda para o
valor mais próximo, e em caso de empate opta pela aproximação mais distante de
zero. Uma vez que a fração decimal 2.675 fica exatamente a meio caminho entre
2.67 e 2.68, poderíamos esperar que o resultado fosse (uma aproximação binária
de) 2.68. Mas não é, porque quando a string decimal ``2.675`` é convertida em
um número de ponto flutuante binário, é substituída por uma aproximação
binária, cujo valor exato é::

   2.67499999999999982236431605997495353221893310546875

Uma vez que esta aproximação é ligeiramente mais próxima de 2.67 do que de
2.68, acaba sendo arredondada para baixo.

Se você estiver em uma situação onde precisa saber exatamente como esses
valores intermediários são arredondados, considere usar o módulo
:mod:`decimal`. Aliás, o módulo :mod:`decimal` também oferece uma boa maneira
de "ver" o valor exato que é armazenado em qualquer float em Python::

   >>> from decimal import Decimal
   >>> Decimal(2.675)
   Decimal('2.67499999999999982236431605997495353221893310546875')

Outra consequência é que, uma vez que 0.1 não é exatamente 1/10, somar 0.1 dez
vezes também não produz exatamente 1.0::

   >>> soma = 0.0
   >>> for i in range(10):
   ...     soma += 0.1
   ...
   >>> soma
   0.9999999999999999

A aritmética de ponto flutuante binário traz muitas surpresas como essas. O
problema do "0.1" é explicado em detalhes precisos abaixo, na seção `Erro de
Representação`_. Para uma descrição mais completa de outras surpresas comuns,
veja `The Perils of Floating Point <http://www.lahey.com/float.htm>`_\ .

Apesar de que os casos patológicos existem, na maioria dos usos cotidianos de
aritmética de ponto flutuante ao fim você verá o resultado esperado
simplesmente arredondando a exibição dos resultados finais para o número de
dígitos decimais que deseja. Para ter um bom controle sobre como um float é
exibido, veja os especificadores de formato do método :meth:`str.format` em
:ref:`formatstrings`.


.. _tut-fp-error:

Erro de representação
=====================

Esta seção explica o exemplo do "0,1" em detalhes, e mostra como você pode
realizar uma análise exata de casos semelhantes.  Assumimos que você tem uma
familiaridade básica com representação binária de ponto flutuante.

:dfn:`Erro de representação` refere-se ao fato de que algumas frações decimais
(a maioria, na verdade) não podem ser representadas exatamente como frações
binárias (base 2). Esta é a principal razão por que Python (ou Perl, C, C++,
Java, Fortran, e muitas outras) frequentemente não exibe o número decimal
exato que esperamos::

   >>> 0.1 + 0.2
   0.30000000000000004

Por que isso acontece? 1/10 e 2/10 não são representáveis exatamente ​​como
frações binárias. Quase todas as máquinas atuais (julho de 2010) usam
aritmética de ponto flutuante conforme a norma IEEE-754, e Python, em quase
todas as plataformas, representa um float como um "IEEE-754 double precision
float" ("float de precisão dupla IEEE-754"). Os tais "doubles IEEE-754" têm 53
bits de precisão, por isso na entrada o computador se esforça para converter
0.1 para a fração mais próxima que pode, na forma *J*/2**\ *N* onde *J* é um
número inteiro contendo exatamente 53 bits. Reescrevendo::


   1 / 10 ~= J / (2**N)

como ::

   J ~= 2**N / 10

e recordando que *J* tem exatamente 53 bits (é ``>= 2**52``, mas ``< 2**53``),
o melhor valor para *N* é 56::

   >>> 2**52
   4503599627370496
   >>> 2**53
   9007199254740992
   >>> 2**56/10
   7205759403792793

Ou seja, 56 é o único valor de *N* que deixa *J* com exatamente 53 bits.
O melhor valor possível para *J* então é aquele quociente arredondado::

   >>> q, r = divmod(2**56, 10)
   >>> r
   6

Uma vez que o resto é maior que a metade de 10, a melhor aproximação é obtida
arredondando para cima::

   >>> q+1
   7205759403792794

Portanto, a melhor aproximação possível de 1/10 como um "IEEE-754 double
precision" é aquele valor dividido por 2\*\* 56, ou::


   7205759403792794 / 72057594037927936

Note que, como arredondamos para cima, esse valor é de fato um pouco maior que
1/10; se não tivéssemos arredondado para cima, o quociente teria sido um pouco
menor que 1/10. Mas em nenhum caso ele pode ser *exatamente* 1/10!

Por isso, o computador nunca "vê" 1/10: o que ele vê é exatamente a fração
dada acima, a melhor aproximação "IEEE-754 double" possível::

   >>> .1 * 2**56
   7205759403792794.0

Se multiplicarmos essa fração por 10\*\*30, podemos ver o valor (truncado) de
seus 30 dígitos mais significativos::

   >>> 7205759403792794 * 10**30 // 2**56
   100000000000000005551115123125L

o que significa que o número exato armazenados no computador é aproximadamente
igual ao o valor decimal 0.100000000000000005551115123125. Em versões de
Python anteriores a 2.7 e 3.1, Python exibia esse valor arredondado para 17
dígitos significativos, produzindo '0.10000000000000001'. Nas versões atuais,
Python exibe a fração decimal mais curta que pode ser convertida para o
verdadeiro valor binário, o que resulta simplesmente em '0.1'.
