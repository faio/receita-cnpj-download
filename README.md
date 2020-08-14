# Receita Cnpj Download
Utilitário para fazer o download de todos os arquivos de CNPJ disponibilizado pela receita federal como dados abertos.

Link da receita federal com os dados abertos:
http://receita.economia.gov.br/orientacao/tributaria/cadastros/cadastro-nacional-de-pessoas-juridicas-cnpj/dados-publicos-cnpj


## Como funciona

O utilitário irá criar uma thread para cada arquivo a ser baixado, com isso reduzindo bastante o tempo de download e melhorando a performance.

## Motivação

A receita tem muita limitação para fazer esses downloads, como limite de velocidades, quedas contantes entre outras, sempre tive problemas em utilizar o curl ou wget para fazer os downloads, para resolver esses problema criei o utilitário para melhorar a performance e resolver esse problema, como solução, ganhei performance, em um processo de download que eu chegava a demorar mais de 1 dia, consigo fazer algo em menos de 3 horas.

## Observação

O utilizado utiliza python3 e foi testado no python 3.8, não depende de bibliotecas externas, apenas as libs padrões do python

## Execução

python download.py
