/*Criação do Banco*/
CREATE DATABASE pastelaria_db_equipe07_Integrador;

USE pastelaria_db_equipe07_Integrador;

CREATE TABLE tb_cliente (
   id_cliente int auto_increment,
   nome varchar(100) not null,
   cpf char(11) not null unique,
   telefone char(11) not null,  
   compra_fiado tinyint,
	 senha varchar(200),
	 dia_fiado int,
   primary key (id_cliente)
);

CREATE TABLE tb_funcionario (
   id_funcionario int auto_increment,
   nome varchar(100) not null,
	 cpf char(11) not null unique,
	 telefone char(11)not null,
   senha varchar(200) not null,
   matricula char(10) not null unique,
   grupo tinyint,
   primary key (id_funcionario)
);

CREATE TABLE tb_produto (
   id_produto int auto_increment,
   nome varchar(100) not null,
   descricao varchar(200) not null,
   foto blob,
   valor_unitario decimal(11,2),
   primary key (id_produto)
);

CREATE TABLE tb_empresa (   
   taxa_juro_diario decimal(11,2),
   multa_atraso decimal(11,2)
   
);

CREATE TABLE tb_comanda (
   id_comanda int auto_increment,
   comanda varchar(100) not null,
   data_assinatura_fiado date null default null,
   data_hora datetime,
   status_pagamento tinyint,
   status_comanda tinyint,
   funcionario_id int,
   cliente_id int,	 
   primary key (id_comanda),
   constraint FK_FuncionarioComanda
   foreign key (funcionario_id)
   references tb_funcionario(id_funcionario),
   constraint FK_ClienteComanda
   foreign key (cliente_id)
   references tb_cliente(id_cliente)
);

CREATE TABLE tb_comanda_produto (
   funcionario_id int,
   produto_id int,
   comanda_id int,
   quantidade int,
   valor_unitario decimal(11,2),
   constraint FK_ComandaProduto
   foreign key (comanda_id)
   references tb_comanda(id_comanda),
   constraint FK_ProdutoComanda
   foreign key (produto_id)
   references tb_produto(id_produto),
   constraint FK_FuncionarioProduto
   foreign key (funcionario_id)
   references tb_funcionario(id_funcionario)
);

CREATE TABLE tb_recebimento (
   id_recebimento int auto_increment,
   total_comandas int,
   valor_total decimal(11,2),
   desconto decimal(11,2),
   data_hora datetime,
   tipo tinyint,
   primary key (id_recebimento)
);

CREATE TABLE tb_comanda_recebimento (
   recebimento_id int,
   comanda_id int,
   constraint FK_ComandaRecebimento
   foreign key (comanda_id)
   references tb_comanda(id_comanda),
   constraint FK_RecebimentoComanda
   foreign key (recebimento_id)
   references tb_recebimento(id_recebimento)
);



