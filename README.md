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
  * Algorítimo de resolução
 
## Plano de Trabalho

* Etapa 1 (4 semana): Estudo de técnicas de segmentação de imagens
  
  - Buscar referências sobre detecção de bordas de objetos e _slicing_.
  - Implementação do algorítimo que destaca a face do cubo na imagem.

* Etapa 2 (4 semanas): Estudo de técnicas de detecção de cores.
  
  - Buscar referências sobre percepção das cores da imagem.
  - Implementação do algorítimo que descrimina a cor de cada um dos quadrados de cada face.
     
* Etapa 3 (2 semanas): Codificação e Testes.
  
  - Desenvolvimento de um código capaz de resolver o cubo mágico a partir das filtragens das etapas anteriores.
  - Testes e validação.

* Etapa 4 (2 semanas): Documentação final.
 
  - Elaboração do relatório e apresentação do projeto.

## Referências Bibliográficas
* [Two Phase Algorithm](http://kociemba.org/cube.htm)
* [Open CV](https://opencv.org/)
* Processamento de Imagens Digitais - R. Gonzalez
