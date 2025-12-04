Bancos de dados são conjuntos de tabelas 
Tabelas são conjuntos de registros
Registros são compostos por campos
#---------------------------------


#DDL: Data definition language = linguagem de definição de dados
#eles são para definição de dados


#DML: Data manipulation language = linguagem de manipulação de dados
#eles são para manipulação de dados


#criando banco de dados
create database cadastro
default character set utf8 
default  collate utf8_general_ci;

#criando tabela
create table pessoas(
	id int not null auto_increment,
	nome varchar(30) not null,
	nascimento date,
	sexo enum('F','M'),
	peso decimal(5,2),
	altura decimal(3,2),
	nacionalidade varchar(20) default 'Brasil',
	primary key (id)
) default  charset = utf8;

#para ver a tabela
describe pessoas;

#inserindo dados na tabela pessoas
insert into pessoas (nome, nascimento, sexo, peso, altura, nacionalidade) value 
('Juan Rozas', '2005-04-20', 'M', '75.90', '1.83', 'Brasil');

#ou

#desta  maneira se os dados inseridos estiverem na mesma ordem que os campos, não é necessario colocar os campos
#porém para evitar erro, é indicado que use da maneira acima para que não ocorra erro. 
insert into pessoas values
(default, 'Juan Carlos', '2000-12-11', 'M', '95.220', '1.78', default);
#id     ,  nome        ,  nascimento , sexo, peso   , altura,  nacionalidade

#alterando o peso do id 5 na tabela pessoas 
update pessoas 
set peso = '98.00'
where id = 2 

#selecionando todos os dados da tabela pessoas
select * from pessoas;