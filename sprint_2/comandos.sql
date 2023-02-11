--E1
--Apresente a query para listar todos os livros publicados após 2014. 
--Ordenar pela coluna cod, em ordem crescente, as linhas.
--Atenção às colunas esperadas no resultado final:
-- cod, titulo, autor, editora, valor, publicacao, edicao, idioma

SELECT *
FROM livro 
WHERE publicacao >= '2015-01-01'
ORDER BY cod 

--E2
/*Apresente a query para listar os 10 livros mais caros.
 Ordenar as linhas pela coluna valor, em ordem decrescente. 
  Atenção às colunas esperadas no resultado final:  titulo, valor. */

SELECT 	titulo,
		valor
FROM livro 
ORDER BY valor DESC 
LIMIT 10

/* E3 
 Apresente a query para listar as 5 editoras com mais livros na biblioteca.
 O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. 
 Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente. */

SELECT 	COUNT(livro.titulo) AS quantidade,
		ed.nome AS nome,
		en.estado,
		en.cidade
FROM livro 
INNER JOIN editora AS ed ON livro.editora = ed.codeditora 
INNER JOIN endereco AS en ON ed.endereco  = en.codendereco 
GROUP BY nome
ORDER BY quantidade DESC
LIMIT 5

/* E4
 Apresente a query para listar a quantidade de livros publicada por cada autor.
 Ordenar as linhas pela coluna nome (autor), em ordem crescente.
  Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).*/

SELECT 	autor.codautor,
		autor.nome,
		autor.nascimento,
		COUNT(livro.titulo) AS quantidade
FROM autor 
LEFT JOIN livro 
	ON autor.codautor = livro.autor 
GROUP BY autor.nome 
ORDER BY nome

/*
E5
Apresente a query para listar o nome dos autores que publicaram livros através de 
editoras NÃO situadas na região sul do Brasil. 
Ordene o resultado pela coluna nome, em ordem crescente. */


SELECT 	autor.nome AS nome
		
FROM autor 
LEFT JOIN livro ON autor.codautor = livro.autor 
LEFT JOIN editora AS ed ON ed.codeditora = livro.editora 
LEFT JOIN endereco AS en ON en.codendereco = ed.endereco 
WHERE estado NOT IN ('PARANÁ', 'SANTA CATARINA', 'RIO GRANDE DO SUL')
ORDER BY nome


/*
E6
Apresente a query para listar o autor com maior número de livros publicados. 
O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.*/

WITH quant_livros AS (

		SELECT 	autor.codautor,
				autor.nome,
				autor.nascimento,
				COUNT(livro.titulo) AS quantidade
		FROM autor 
		LEFT JOIN livro 
			ON autor.codautor = livro.autor 
		GROUP BY autor.nome 
		ORDER BY nome

)

SELECT 	q.codautor,
		q.nome,
		MAX(q.quantidade) as quantidade_publicacoes
FROM  quant_livros AS q
		
/*
E7
Apresente a query para listar o nome dos autores com nenhuma publicação. 
Apresentá-los em ordem crescente. */

WITH quant_livros AS (

		SELECT 	autor.codautor,
				autor.nome,
				autor.nascimento,
				COUNT(livro.titulo) AS quantidade
		FROM autor 
		LEFT JOIN livro 
			ON autor.codautor = livro.autor 
		GROUP BY autor.nome 
		ORDER BY nome

)

SELECT q.nome
FROM quant_livros AS q
WHERE q.quantidade = 0
ORDER BY q.nome 

------------------------------------------SEÇÃO4-----------------------------------------------


/*
E8
Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem),
e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser,
portanto, cdvdd e nmvdd.*/



WITH max_vendas AS (
		SELECT 	vendedor.cdvdd,
				vendedor.nmvdd,
				vendas.qtd,
				COUNT(*) 
		FROM tbvendas AS vendas
		LEFT JOIN tbvendedor AS vendedor 
			ON vendas.cdvdd = vendedor.cdvdd 
		WHERE vendas.status = 'Concluído'
)

SELECT 	mvdd .cdvdd,
		mvdd .nmvdd
FROM max_vendas as mvdd


/*
E9
Apresente a query para listar o código e nome do produto mais vendido entre as 
datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. 
As colunas presentes no resultado devem ser cdpro e nmpro. */

WITH max_produto AS (
		SELECT 	cdpro,
				nmpro,
				qtd,
				COUNT(*) 
		FROM tbvendas 
		WHERE status = 'Concluído' AND 
				dtven BETWEEN '2014-02-03' AND '2018-02-02'
			  
)


SELECT	mprod.cdpro,
		mprod.nmpro
FROM max_produto as mprod




/*

E10
A comissão de um vendedor é definida a partir de um percentual 
sobre o total de vendas (quantidade * valor unitário) por ele realizado. 
O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 

Com base em tais informações, calcule a comissão de todos os vendedores, 
considerando todas as vendas armazenadas na base de dados com status concluído.

As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao.
 O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal. */


with dados_basicos as (
select 	ven.qtd AS quantidade,
		ven.vrunt AS valor_unitario,
		(ven.qtd * ven.vrunt) AS total_de_vendas,
		(vdd.perccomissao *0.01) as percvv,
		vdd.nmvdd as vendedor,
		SUM((ven.qtd * ven.vrunt))as valor_total_de_vendas

		
from tbvendas as ven
inner join tbvendedor as vdd
on vdd.cdvdd = ven.cdvdd 
where status = 'Concluído'
GROUP by vendedor

) 

select db.vendedor as vendedor,
		db.valor_total_de_vendas as valor_total_vendas,
		Round(db.valor_total_de_vendas *db.percvv,2) as comissao

from dados_basicos as db
order by comissao desc



/*
E11
Apresente a query para listar o código e nome cliente com maior gasto na loja. 
As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última 
representando o somatório das vendas (concluídas) atribuídas ao cliente.*/

with gastos as (

SELECT cdcli,
		nmcli,
		SUM(qtd * vrunt) as soma_dos_gastos
		
from tbvendas 
group by cdcli
ORDER by soma_dos_gastos DESC
)

select gas.cdcli,
		gas.nmcli,
		MAX(gas.soma_dos_gastos) as gasto
from gastos as gas

/*
 E12
Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor
com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado 
devem ser cddep, nmdep, dtnasc e valor_total_vendas.

Observação: Apenas vendas com status concluído. */


with vendas_brutas as (
select 	ven.qtd AS quantidade,
		ven.vrunt AS valor_unitario,
		(ven.qtd * ven.vrunt) AS total_de_vendas,
		vdd.cdvdd,
		SUM((ven.qtd * ven.vrunt))as valor_total_vendas

		
from tbvendas as ven
inner join tbvendedor as vdd
on vdd.cdvdd = ven.cdvdd 
where status = 'Concluído'
GROUP by vdd.cdvdd

) , valor_bruto_min as (

SELECT 	dep.cddep, 
		dep.nmdep, 
		dep.dtnasc,
		MIN( vb.valor_total_vendas) as valor_bruto_min

from vendas_brutas as vb
left join tbdependente as dep
	on vb.cdvdd = dep.cdvdd
where vb.valor_total_vendas is not null

)

SELECT 	cddep, 
		nmdep, 
		dtnasc,
		valor_bruto_min as valor_total_vendas

from valor_bruto_min



--E14
--Apresente a query para listar o gasto médio por estado da federação.
-- As colunas presentes no resultado devem ser estado e gastomedio.
-- Considere apresentar a coluna gastomedio arredondada na segunda casa decimal
-- e ordenado de forma decrescente.

--Observação: Apenas vendas com status concluído.

WITH gasto_medio AS (

		SELECT estado,
				SUM (qtd * vrunt) AS gasto,
				COUNT (qtd) AS contagem_produto
		FROM tbvendas 
		WHERE status = 'Concluído'
		GROUP BY estado
)

SELECT 	estado, 
		ROUND (1.0 * gasto/contagem_produto, 2) AS gastomedio
FROM gasto_medio
ORDER BY gastomedio DESC




--E15
--Apresente a query para listar os códigos das vendas identificadas como deletadas.
-- Apresente o resultado em ordem crescente.



SELECT cdven
from tbvendas 
WHERE deletado = 1
ORDER BY cdven 



--E16
--Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação.
--As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. 
--Considere arredondar o valor da coluna quantidade_media na quarta casa decimal.
-- Ordene os resultados pelo estado (1º) e nome do produto (2º).

--Obs: Somente vendas concluídas.
WITH calculo_media as (
		SELECT 
				estado,
				nmpro,
				qtd,
				COUNT(qtd) AS contagem_produto,
				sum(qtd) AS total_produto
		FROM tbvendas 
		where status = 'Concluído'
		group by estado,nmpro  

)

select estado,
		nmpro,
		ROUND(1.0 * total_produto/contagem_produto, 4) as quantidade_media
		
from calculo_media
order by estado, nmpro






