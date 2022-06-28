import random

pnome = ('Ana','Anelize','Andre','Antonio','Alcides','Aline','Ariane','Acacio','Adelina','Aristides','Abigail','Abner','Amanda','Agnaldo','Alice','Arthur','Arlete','Armando',
'Antonieta','Amaro','Alana','Alberto','Amélia','Alexandre','Alessandra','Bernadete','Bira','Betina','Bertoldo','Bela','Bartolomeu','Berto','Berila','Basílio','Bartina','Bebeto','Bethania','Bidula','Carlo','Carla','Cantinflas','Carina','Carlote','Caca','Cassio','Cassiane','Cesar','Céila','Célso','Cézina','Celine','Ciana','Cenésio','Creusa','Claiton','Clairton','Cleson'
,'Dani','Diogo','Darcy','Dandara','Denise','Donato','Dinara','Débora','Dilson','Donizete','Darla','Denilson','Danilo','Dercy','Dorival','Duduca','Dilma','Diney','Delcia'
,'Eliezer','Eliza','Elsa','Elizandro','Emilia','Estevan','Elmir','Ellen','Evelize','Elena','Filipe','Filipa','Florinda','Floripio','Fáfa','Fabio','Fabia','Fabiula','Felicia','Fabrício'
,'Gil','Gilmara','Gilmar','Gabriela','Grabriele','Glenda','Gabriel','Gelso','Gilda','Gildo','Gênesio','Gênésia','Genivalda','Geni','Gênivaldo','Gentil','Horacio','Hera','Hortolino','Heraldo'
,'Heraci','Heros','Hildo','Heralda','Hemilio','Herminio','Helena','Helenalda','Hélio','Heuvacir','Heitor','Hector','Holina','Ildo','Ivan','Ivana','Ivanildo','Ivacir','Isla','Ione'
,'Iona','Ismael','Ivanir','Inajara','Inaia','Irene','Ireno','Itamar','Italo','Itala','Imair','Joana','João','Joanir','Jocasta','Jonas','jurema','Juremir','Jussara','Juracy'
,'Jane','jeni','jilmara','Joelma','Juma','Juceline','Juca','Joel','Joelmir','jeremias','Karine','Karina','Keuler','Kenon','Kellen','Keilan','Kira','Leila','Leocir','Leorio','Leonora'
,'Lia','Leco','Leidynara','Lucas','Lara','Leoncio','Lucia','Luciano','Luci','Lúcio','Lica','Laurecy','Lúcia','Luciana','Lena','Leno','Lira','Layla','Leunice','Lena','Letícia','Leroy'
,'Mario','Maiara','Miro','Marisol','Milton','Marcel','Marcela','Melissa','Mariano','Milka','Miraldo','Maria','Marivalda','Murilo','Madara','Marçal','Miroslau','Mary','Matilde','Mumu','Mikaela','Marciano','Mel','Marieta','Marlize','Marco','Nadir','Nilson','Nestor','Natanael','Nilva','Natalino','Natalina','Natanael','Niraldo','Noa','Naty','Niracy','Nilton','Niversi','Nailin','Neca','Neco','Natan','Narismar','Osmar','Olinda','Otávio','Olivia','Omar','Odissia','Otáviano','Olimar','Ortelino','Omara','Odete','Omiro','Patricia','PatriK','Paula','Paulo','Paloma','Péricles','Paty','Pedro','Pietro','Pietra','Priscila','Perla','Pedrita','Portos','Queila','Quelson','Pamela','Quellen','Quenilson','Quayla','Raziel','Rafaela','Rafael','Ricarda','Ricardo','Renê','Rufus','Roberto','Roberta','Riva','Rebeca','Renato','Renata','Reina','Reinaldo','Ravi','Rita','Raiane','Ronaldo','Roni','Rona','Silvia','Silvia','Silvano','Silvana','Saul','Sara','Sarita','Salazar','Sávio','Selene','Selenir','Sula','Samantha','Samara','Samaria','Senor','Simaria','Saulo','Seumar','Silvar','Savana','Tânia','Tamires','Tano','Telmo','Telma','Teumar','Tito','Tilemar','Tela','Tomas','Taumir','Thomas','Toniel','Talita','Tamaris','Tetel','Túlio','Uriel','Ursula','Ursulino','Uma','Ulimar','Ugo','Urdênio','Undina','Ubiracy','Unohana','Urahara','Vera','Veron','Vilma','Vilmar','Valmor','Valderléia','Valdirene','Volmir','Vanderlei','Virginia','Vica','Valdinei','Valdir','Venceslau','Vitório','Vitória','Vitorino','Vitorina','Valdeci','Valdic','Veridiana','Xena','Xaviel','Xilomar','Xica','Xexeu','Zila','Zaqueu','Zoroaldo','Zimas','Zita')

snome = ('Amaral','Alcides','Abravanel','Alves','Artanos','Ausenhall','Bastos','Bertolussi','Bortolassi','Baçano','Bustonesse','Baungartem','Bertoldo','Berdinaze','Cardinale','Crisam','Castor','Andrade','Celem','Czar','Donizete','Demetriam','Deoliveira','Diniz','Dodória','Detaflan','Ducatty','Dalcim','Deodato','Elifan','Elder','Escarlats','Emirar','Elivamir','Facomir','Falcão','Ferreira','Freitas','Fleck','Fortine','Fararrar','Gorbat','Girardy','Geralmster','Ginga','Gutstembar','Galtimas','Gallion','Girth','Helmster','Helmer','Harmon','Harrisom','Heartbreak','Hibrain','Hutson','Hectorim','Dorfman','Imaculada','Irilam','Iwman','Ingran','Islatam','Jungman','Jelivam','Jaspian','Jordan','Jacaranda','Jirolanda','Jetamen','Kent','Keirim','Katsu','Leiva','Lenim','Lacart','Lindoval','Leal','Lincs','Legionar','Machado','Mark','Meridian','Motaro','Muligan','Nagal','Nisplant','Natsunaga','Nereu','Nixon','Orleans','Oneil','Ordin','Osaka','Otoman','Odissan','Oligar','Pereira','Paris','Hilton','Pedreira','Petras','Petraquios','Potrim','Pelvim','Pelican','Port','Quentyn','QueensLive','Quarry','Scotfield','Fieldgarden','Rocha','Rasmon','Richson','Routerson','Peterson','Raigam','Real','Rhealsin','Jetson','Silveira','Silverado','Santos','Santi','Tambórium','Tukson','Taison','Teigra','Tangamandapiu','Tiroless','Unomom','Ukratis','Untaro','Udine','Valverde','Vilasboas','Vennety','Zanquety','Voldmor','Vairoment','Vicasa','Vanhellsing','Xeon','Xenogears','Strife','Zion','Zulu','Zenebatos','Zalquia')

#Informação das tuplas de nome e sobrenome
print('Número de nomes na base {}'.format(len(pnome)))
print('Número de sobrenomes na base {}'.format(len(snome)))

linhasTotais = int(input('Ensira o número de linhas que contera o arquivo :'))
ponteiro = 0
while ponteiro < linhasTotais:
    n = random.randint(0,(len(pnome)-1))
    nome = pnome[n]
    n = random.randint(0,(len(snome)-1))
    sobrenome =snome[n]
    n = random.randint(1,2)
    i = random.randint(7,97)
    linha = str("('{} {}',{},{}),\n".format(nome,sobrenome,i,n))
    with open('DBnomes.txt','a',encoding ='utf-8') as texto:
        texto.write(str(linha))
    ponteiro = ponteiro + 1


