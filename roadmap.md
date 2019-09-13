# To-do

## 1. Desenhar retângulo a partir de dois pontos (Carol):
Dado dois pontos, desenhar um retângulo


## 2. Transformação gráfica (mapeamento) (Hector):
Mapear o desenho realizado na janela principal em uma janela menor.
Definir o tamanho de forma relativa ao tamanho da janela principal, por exemplo, 17%.


## 3. Estrutura de Dados para Armazenar Desenhos realizados (João):
Imagino que deverá ter dois tipos de estruturas:

- A primeira que armazena os desenhos realizados pelo usuário em uma pilha, onde será possível desfazer o último 
desenho realizado, recuperar 
qual desenho está mais "acima" e está sobrepondo outro desenho. (mais importante para agora)

Existem duas formas diferentes de "desfazer" uma ação:
- A primeira é "pintar" a figura com a mesma cor de fundo da janela.
Essa opção é mais rápida, porém tem a deficiência de apagar também uma figura que estivesse sobreposta

- A segunda seria redesenhar tudo, que não apagaria alguma figura sobreposta, mas seria mais lento.

- A segunda que armazena os desenhos hierarquicamente, onde você tem uma figura, que é composta por camadas e as 
camadas são compostas por tipos primitivos.
Ela será útil para redesenhar toda a figura novamente e para exportar para xml. (menos importante agora)


## 4. Suportar desenho com clique do mouse (João):
Desenhar os tipos primitivos com clique de mouse. Por ora, é suficiente que seja possível desenhar somente quando o 
segundo clique é realizado, descartando a reta, circulo e retangulo elásticos.
Deverá implementar:
- Desenho de reta
- Desenho de círculo
- Desenho de retângulo


## 5. Desfazer / Refazer ação (Carol):
O equivalente ao ctrl+z e o ctrl+y, que desfaz e refaz os últimos desenhos. Utilizar pilha.



## 6. Janela com interface gráfica (Hector):
 
A janela deverá ser de um tamanho fixo e que não poderá ser alterado. Além disto, ela deverá ter:
* Um botão de fechar
- Uma barra lateral na esquerda, contendo:
  
  * Um botão para desenhar reta
  * Um botão para desenhar circulo
  * Um botão para desenhar retangulo
  * Um botão de desfazer
  * Uma mini janela de visualização da área de trabalho
- Uma área de trabalho (onde os desenhos serão feitos)

Ressaltando, que esta tarefa não precisa implementar as ações, apenas os botões e os elementos.

## 7. Exportar e importar desenho através de XML.
