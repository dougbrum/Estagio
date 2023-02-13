/*
E8
Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem),e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser,
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
FROM max_vendas AS mvdd


/*
E9
Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro. */

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
FROM max_produto AS mprod



/*

E10
A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 

Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído. As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao.
O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal. */

WITH dados_basicos AS (

		SELECT 	ven.qtd AS quantidade,
				ven.vrunt AS valor_unitario,
				(ven.qtd * ven.vrunt) AS total_de_vendas,
				(vdd.perccomissao *0.01) AS percvv,
				vdd.nmvdd AS vendedor,
				SUM((ven.qtd * ven.vrunt)) AS valor_total_de_vendas

		
		FROM tbvendas AS ven
		INNER JOIN tbvendedor AS vdd
		ON vdd.cdvdd = ven.cdvdd 
		WHERE status = 'Concluído'
		GROUP by vendedor

) 

SELECT  db.vendedor AS vendedor,
		db.valor_total_de_vendas AS valor_total_vendas,
		Round(db.valor_total_de_vendas *db.percvv,2) AS comissao

FROM dados_basicos AS db
ORDER BY comissao DESC



/*
E11
Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.*/

WITH gastos AS (

SELECT cdcli,
		nmcli,
		SUM(qtd * vrunt) AS soma_dos_gastos
		
FROM tbvendas 
GROUP BY cdcli
ORDER by soma_dos_gastos DESC
)

SELECT gas.cdcli,
		gas.nmcli,
		MAX(gas.soma_dos_gastos) AS gasto
FROM gastos AS gas

/*
E12
Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.
Observação: Apenas vendas com status concluído. */


WITH vendas_brutas AS (

		SELECT 	ven.qtd AS quantidade,
				ven.vrunt AS valor_unitario,
				(ven.qtd * ven.vrunt) AS total_de_vendas,
				vdd.cdvdd,
				SUM((ven.qtd * ven.vrunt))as valor_total_vendas
		
				
		FROM tbvendas AS ven
		INNER JOIN tbvendedor AS vdd
		ON vdd.cdvdd = ven.cdvdd 
		WHERE status = 'Concluído'
		GROUP BY vdd.cdvdd

) , valor_bruto_min AS (
		
		SELECT 	dep.cddep, 
				dep.nmdep, 
				dep.dtnasc,
				MIN( vb.valor_total_vendas) AS valor_bruto_min
		
		FROM vendas_brutas AS vb
		LEFT JOIN tbdependente AS dep
			ON vb.cdvdd = dep.cdvdd
		WHERE vb.valor_total_vendas IS NOT NULL

)

SELECT 	cddep, 
		nmdep, 
		dtnasc,
		valor_bruto_min AS valor_total_vendas

FROM valor_bruto_min

/*
E13
Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.*/


SELECT  cdpro,
		nmcanalvendas,
		nmpro,
		SUM(qtd) AS quantidade_vendas
FROM tbvendas 
WHERE status = 'Concluído'
GROUP BY cdpro, nmcanalvendas 
ORDER BY quantidade_vendas
LIMIT 10


/*
E14
Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.
Observação: Apenas vendas com status concluído.*/

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


/*
E15
Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.*/


SELECT cdven
FROM tbvendas 
WHERE deletado = 1
ORDER BY cdven 


/*
E16
Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. Considere arredondar o valor da coluna quantidade_media na quarta casa decimal.
Ordene os resultados pelo estado (1º) e nome do produto (2º).

Obs: Somente vendas concluídas.*/

WITH calculo_media AS (
		SELECT 
				estado,
				nmpro,
				qtd,
				COUNT(qtd) AS contagem_produto,
				sum(qtd) AS total_produto
		FROM tbvendas 
		WHERE status = 'Concluído'
		GROUP BY estado,nmpro  

)

SELECT estado,
		nmpro,
		ROUND(1.0 * total_produto/contagem_produto, 4) AS quantidade_media
		
FROM calculo_media
ORDER BY estado, nmpro






