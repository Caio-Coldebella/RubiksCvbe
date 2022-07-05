# RubicksCvbe

## Apresentação

O presente projeto foi originado no contexto das atividades da disciplina de graduação *EA979A - Introdução a Computação Gráfica e Processamento de Imagens*, 
oferecida no primeiro semestre de 2022, na Unicamp, sob supervisão da Profa. Dra. Paula Dornhofer Paro Costa, do Departamento de Engenharia de Computação e Automação (DCA) da Faculdade de Engenharia Elétrica e de Computação (FEEC).


 |Nome  | RA | Curso|
 |--|--|--|
 | Caio Ruiz Coldebella  | 232621  | Eng. de Computação|
 | Gustavo de Souza dos Reis  | 217425  | Eng. de Computação|

## Descrição do Projeto
Esse projeto tem como objetivo gerar o passo-a-passo da solução otimizada de um cubo mágico a partir de registros fotográficos de cada uma de suas faces embaralhadas e pré-definição da orientação espacial delas. Para isso, o projeto pode ser dividido em partes, sendo elas:

  * Processamento das imagens
    - Detecção do cubo
    - Detecção das cores
  * Algoritimo de resolução

O programa final é o notebook [RubiksCvbe.ipynb](/Notebooks/rubiks_cvbe.ipynb)
 
## Abordagem Adotada
Como base de dados utilizada, temos fotos de cada face do cubo. Essas fotos precisam seguir certos padrões a fim de poder ser interpretadas pelo programa. Primeiro, precisam ser fotos "chapadas" somente da face em questão do cubo alinhada na horizontal, tendo um plano escuro como fundo, preferencialmente preto. Para tirar as fotos, a face deve estar posicionada seguindo a seguinte referência espacial:

![Referencia de posicionamento relativo das faces](/Assets/referencia.png)

Além disso, os arquivos devem ser nomeados da seguinte forma: **XF.jpg**, sendo X a inicial da cor da fase em inglês (B,G,O,R,W ou Y). Vale ressaltar que as cores das faces são fixas e são definidas pelo quadrado no centro do cubo.

Segue um exemplo de uma foto adequada aos paramêtros indicados. A imagem em questão foi nomeada como **RF.jpg**.

Tais padrões são necessários pois o algoritimo espera a posição definida como relativa entre as faces, e não é possível identificar essa posição apenas com a foto de uma face. O alinhamento da face é necessário pois existe uma rotina pré-definida para o reconhecimento de cada quadradinho de uma face, a partir da sua localização na face definida.

![RF.jpg](/Assets/RF.jpg)

### Pipeline de Processamento

O primeiro processo na no processamento do banco de imagens é o de detectar a face do cubo na imagem. Para isso, é feita uma segmentação com threshold e é utilizada uma função de detectar bordas do OpenCV para encontrar as coordenadas da borda do cubo. A partir das coordenadas de cada face, é possível saber a posição de cada um dos 9 quadradinhos dela, e com essa posição, resta saber a cor de cada um.
Para isso, foi definida para cada uma das 9 cores um filtro HSV. Os valores de cada filtro foram definidos e testados manualmente utilizando uma ferramenta desenvolvida com esse propósito: [trackbars.py](/trackbars.py)
Sabendo a posição e a cor de cada quadradinho, podemos transformar cada face do cubo em um array, e aplicá-las no algoritimo de resolução [Two Phase Algorithm](http://kociemba.org/cube.htm), que soluciona o cubo com 20 movimentos em média.

## Resultados Finais

Como resultado final da execução, temos o passo a passo para montar o cubo, como no exemplo abaixo:

![resultado final](/Assets/passos.png)

Apesar de funcionar e apresentar a resolução correta, o programa possui algumas limitações, que serão discutidas na próxima seção.

## Discussão

De forma geral, o programa cumpre o previsto inicialmente, e o objetivo inicial foi alcançado. Porém, a abordagem adotada tem algumas limitações. Como apontado anteriormente, o algoritimo pressupõe diversos cuidados tomados pelo usuário com as imagens utilizadas. Caso alguma das intruções não seja seguida criteriosamente, o resultado é completamente errado. Podemos ver abaixo dois exemplos, um que tem a foto da face girada e outro com o contraste um pouco baixo. O contorno em vermelho é o que o software detectou como sendo a face do cubo a ser análisada.

![face virada](/Assets/cubovirado.jpg)
![face sem contraste](/Assets/errofundosemcontraste.jpg)

Uma das formas de resolver esse problema seria a de fazer um tratamento em todas as imagens antes de iniciar o pipeline de processamento. Esse tratamento usaria transformações que poderiam ser de intensidade dos valores de cores e também transformações geométricas.

Uma outra limitação do programa é quanto as cores dos quadrados. Essas cores têm tonalidades, que variam de cubo a cubo e até no mesmo cubo, dependendo de fatores como a iluminação do local na hora da foto. Dessa forma, uma dificuldade encontrada durante o desenvolvimento do projeto foi a de separar as cores amarelo, laranja e vermelho nos filtros utilizados, já que são cores com tonalidades muito próximas e que podem ser até difíceis de distinguir visualmente dependendo das condições. Uma forma de mitigar esse problema poderia ser uma calibragem inicial feita pelo próprio usuário antes do processamento das imagens com as mesmas trackbars utilizadas para criar as máscaras.

## Referências Bibliográficas
* [Two Phase Algorithm](http://kociemba.org/cube.htm)
* [Open CV](https://opencv.org/)
* Processamento de Imagens Digitais - R. Gonzalez
1
