select NUMERO,
       QUANTIDADE,
       PRECO,
       QUANTIDADE * PRECO as valor_total
from itens_notas_fiscais;


select NUMERO,
       count(*)                          as total_itens,
       round(sum(QUANTIDADE * PRECO), 2) as valor_total
from itens_notas_fiscais
group by NUMERO
;


with total_vendas as (select NUMERO,
                             count(*)                          as total_itens,
                             round(sum(QUANTIDADE * PRECO), 2) as valor_total
                      from itens_notas_fiscais
                      group by NUMERO),
     notas as (select nf.DATA_VENDA as data,
                      tc.NOME       as nome_cliente,
                      tv.NOME       as nome_vendedor,
                      nf.NUMERO     as numero_nota,
                      nf.IMPOSTO    as imposto
               from notas_fiscais as nf
                        join tabela_de_clientes as tc
                             on nf.CPF = tc.CPF
                        join tabela_de_vendedores as tv
                             on nf.MATRICULA = tv.MATRICULA)

select n.data,
       n.nome_cliente,
       n.nome_vendedor,
       n.numero_nota,
       v.total_itens,
       v.valor_total,
       n.imposto,
       round(v.valor_total * n.imposto / 100, 2)                   as valor_imposto,
       round(v.valor_total - (v.valor_total * n.imposto / 100), 2) as valor_final

from total_vendas as v
         join notas as n
              on v.NUMERO = n.numero_nota
