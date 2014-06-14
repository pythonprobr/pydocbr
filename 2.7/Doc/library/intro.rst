
.. _library-intro:

************
Introdução
************

A "Biblioteca Python" contém vários tipos diferentes de componentes.

Ela contém tipos de dados que normalmente seriam considerados parte do
"núcleo" de uma linguagem, como números e listas. Para esses tipos, o núcleo
da linguagem Python define a forma dos literais e impõe algumas restrições em
suas semânticas, mas sem definí-las totalmente. (Por outro lado, o núcleo da
linguagem define propriedades sintáticas como a escrita e as prioridades dos
operadores.)

A biblioteca também contém funções embutidas e exceções --- objetos que podem
ser usados por qualquer código Python sem a necessidade de uma instrução
:keyword:`import`. Algumas delas são definidas pelo núcleo da linguagem, mas
muitas não são essenciais para a semântica principal e são descritas apenas
neste manual.

Entretanto, a maior parte da biblioteca é composta por uma coleção de módulos.
Existem várias maneiras de dissecar esta coleção. Alguns módulos são escritos
em linguagem C e estão embutidos no interpretador Python; outros são escritos
em Python e importados na forma de código fonte. Alguns módulos fornecem
interfaces que são muito específicas para o Python, como imprimir um traceback
(situação da pilha de execução); alguns fornecem interfaces que são
específicas para um sistema operacional em particular, como o acesso a um
hardware específico; outros fornecem interfaces que são específicas para um
domínio de aplicação, como a Web. Alguns módulos estão disponíveis em todas as
versões e implementações de Python; outros só estão disponíveis quando o
sistema em questão os suporta ou necessita deles; outros módulos, ainda, estão
disponíveis apenas quando uma determinada opção de configuração foi escolhida
quando o Python estava sendo compilado e instalado.

Esse manual está organizado "de dentro para fora": primeiro descreve os tipos
de dados embutidos, depois as funções e exceções embutidas, e finalmente os
módulos, agrupados em capítulos de módulos relacionados. A ordem dos
capítulos, assim como a ordem dos módulos dentro de cada capítulo é geralmente
do mais relevante para o menos importante.

Isso significa que se você começar a ler esse manual desde o princípio, e
pular para o próximo capítulo quando ficar chato, terá uma visão geral bem
razoável dos módulos disponíveis e das áreas de aplicação que são suportadas
pela biblioteca do Python. Naturalmente, não é *necessário* lê-lo como um
romance --- é possível navegar pelo índice (no início do manual), ou procurar
uma função específica, módulo ou termo no índice remissivo (no final). E,
finalmente, se gostar de aprender sobre assuntos aleatórios, escolha uma
página ao acaso (veja o módulo :mod:`random`) e leia uma ou duas seções.
Independente da ordem que esse manual for lido, seria útil se começasse pelo
capítulo :ref:`built-in-funcs`, já que todo o restante do material pressupõe
familiaridade com essa seção.

Vamos começar o show!

