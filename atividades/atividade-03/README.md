## Arquivo SQL gerado pelo aplicativo DB Browser (SQLite).
### Projeto Geo Localização
### Essa atividade será realizada em equipes. Será tomado como referencia o site https://pt.wikipedia.org/wiki/Lista_de_mesorregi%C3%B5es_e_microrregi%C3%B5es_do_Cear%C3%A1
### Nele estão contidos as mesorregiões e microrregiões do Estado do Ceará e o nome dos seus respectivos municipios. Esse dados estão coerentes com a classificação do IBGE.
### A atividade consistirá em cadastrar em uma tabela de um banco de dados todos os municípios do estado com as suas respectivas localizações feitas pelas coordenadas longitude(x) e latitude(y). 
### Esses valores serão obtidos pelo site https://epsg.io/map#srs=4326&x=-38.535962&y=-3.744408&z=15&layer=streets. 
### O site possui um recurso de navegação usando o mouse ou movendo o mapa.
### Etapas do Trabalho
### 1) Divisão das equipes com as suas respectivas meso regiões. Cada meso região é composta por micro regiões. E cada micro região é composta por municípios. Cada município será inserido na tabela TB_MUNICIPIOS com a a geolocalização da prefeitura (latitude e longitude). Esse trabalho será coordenado por cada líder de equipe.
### 2) Cada líder de equipe deve fazer o levantamento dos municípios que compõem as micro regiões
### 3) Cada membro da equipe deve coletar as coordenadas das prefeituras para o qual foi designado. 
### 4) Escrever um script SQL para inserção na tabela TB_MUNICIPIOS. Será informado o esquema da tabela posteriormente.
