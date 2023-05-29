-- Inserir dados na tabela tb_cliente
INSERT INTO tb_cliente (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao;

-- Inserir dados na tabela tb_carro
--INSERT INTO tb_carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro)
--SELECT DISTINCT idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro
--FROM tb_locacao;

-- Inserir dados na tabela tb_combustivel
INSERT INTO tb_combustivel (idcombustivel, tipoCombustivel)
SELECT DISTINCT idcombustivel, tipoCombustivel
FROM tb_locacao;

-- Inserir dados na tabela tb_vendedor
INSERT INTO tb_vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;

-- Inserir dados na tabela tb_locacao
INSERT INTO tb_locacao_norm  (idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor)
SELECT idLocacao, idCliente, idCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor
FROM tb_locacao;

INSERT INTO tb_carro (idCarro, kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro)
SELECT idCarro, MIN(kmCarro), MIN(classiCarro), MIN(marcaCarro), MIN(modeloCarro), MIN(anoCarro)
FROM tb_locacao
GROUP BY idCarro;

drop table tb_locacao; 