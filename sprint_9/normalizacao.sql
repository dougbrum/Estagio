CREATE TABLE tb_cliente (
  idCliente       int primary key,
  nomeCliente     varchar(100),
  cidadeCliente   varchar(40),
  estadoCliente   varchar(40),
  paisCliente     varchar(40)
);

CREATE TABLE tb_carro (
  idCarro         int primary key,
  kmCarro         int,
  classiCarro     varchar(50),
  marcaCarro      varchar(80),
  modeloCarro     varchar(80),
  anoCarro        int
);

CREATE TABLE tb_combustivel (
  idcombustivel   int primary key,
  tipoCombustivel varchar(20)
);

CREATE TABLE tb_vendedor (
  idVendedor      int primary key,
  nomeVendedor    varchar(15),
  sexoVendedor    smallint,
  estadoVendedor  varchar(40)
);

CREATE TABLE tb_locacao_norm (
  idLocacao       int primary key,
  idCliente       int references tb_cliente(idCliente),
  idCarro         int references tb_carro(idCarro),
  idcombustivel   int references tb_combustivel(idcombustivel),
  dataLocacao     datetime,
  horaLocacao     time,
  qtdDiaria       int,
  vlrDiaria       decimal(18,2),
  dataEntrega     date,
  horaEntrega     time,
  idVendedor      int references tb_vendedor(idVendedor)
);


