SELECT * FROM autor au 
SELECT * FROM  editora ed 
SELECT * FROM  endereco en 
SELECT * FROM  livro lv 

-- E1
SELECT * FROM  livro lv 
WHERE lv.publicacao > '2014-12-31' 
order by lv.cod  

-- E2
SELECT lv.titulo, lv.valor  
FROM  livro lv 
order by lv.valor DESC  
LIMIT 10

-- E3
SELECT COUNT(*) AS quantidade, e.nome, end.estado, end.cidade
FROM livro l
JOIN editora e ON l.editora = e.codEditora
JOIN endereco end ON e.endereco = end.codEndereco
GROUP BY l.editora, e.nome, end.estado, end.cidade
ORDER BY quantidade DESC
LIMIT 5;

-- E4
SELECT 
	a.nome,
    a.codAutor,
    a.nascimento,
    (
        SELECT COUNT(*)
        FROM livro l
        WHERE l.autor = a.codAutor
    ) AS quantidade
FROM autor a
ORDER BY a.nome;

-- E5
SELECT DISTINCT a.nome
FROM livro l
JOIN autor a ON l.autor = a.codAutor
JOIN editora e ON l.editora = e.codEditora
JOIN endereco end ON e.endereco = end.codEndereco
WHERE end.estado NOT IN ('PARANÁ', 'SANTA CATARINA', 'RIO GRANDE DO SUL')
ORDER BY a.nome;

-- E6
SELECT a.codAutor, a.nome, COUNT(*) AS quantidade_publicacoes
FROM livro l
JOIN autor a ON l.autor = a.codAutor
GROUP BY a.codAutor, a.nome
ORDER BY quantidade_publicacoes DESC
LIMIT 1;

-- E7
SELECT nome
FROM autor
WHERE codAutor NOT IN (SELECT autor FROM livro)
ORDER BY nome;