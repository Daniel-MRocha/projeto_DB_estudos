# projeto_DB_estudos

  Programa para geração de lista de nome e sobrenomes para laboratório
em banco de dados,consiste em duas tuplas, uma com nomes e  outras com
sobrenomes, que serão embaralhadas, e escritas em um arquivo de texto.
  Como o intuito deste programa foi gerar conteúdo para serem colocados em
um banco de dados mysql, note que além das duas tuplas citadas, o programa
ainda inseri na linha mais dois valores, que é o correspondente a clube,
que seria 1 ou 2, e o outro valor é a idade, que varia de 7 a 97.
  É possível ainda definir o numero de linhas desejadas.
É um programa bem simples, talvez melhore ele no futuro, colocando mais nomes
ou deixando mais legível, fato é que serviu ao propósito e fiz muitos
experimentos de joins, funções, consultas, enfim, espero que seja utíl a 
outros estudantes.

#Funcionamento:

No Prompt (tem que ter python instalado na maquina), navegue até a pasta que contém o arquivo nomeDB1.py

Escreva:
python3 nomeDB1.py e digite enter.

Será apresentado a quantidade de nomes e sobrenomes que o programa tem nas suas tuplas.

Informe a quantidade de linhas que deseja para  o arquivo e dibite enter novamente.

agora, na mesma pasta do arquivo nomeDB1.py , aparecera um novo arquivo de nome DBnomes.txt , que 
possue a quantidade de registros informados pelo usuário anteriormente, bastando copiar e colar, 
antecedido pelos comandos do banco,exemplo:

insert into tabela(nome,idade,clube) values 
cole abaixo as linhas do arquivo


