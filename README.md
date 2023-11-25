# Instalando dependências
- [Instalar o pandas](https://pandas.pydata.org/docs/getting_started/install.html)
- [Instalar o matplotlib](https://matplotlib.org/stable/users/installing/index.html)
```bash
# Arch
sudo pacman -S python-pandas

sudo pacman -S python-matplotlib

# PyPi
pip install pandas

pip install matplotlib
```

# Obtendo os dados
Os gráficos são montados a partir do processamento de dois arquivos CSVs que contém o número de transações diárias das redes Ethereum e Bitcoin.
Esses arquivos foram gerados a partir da consulta em datasets públicos com dados das duas redes disponíveis no Google BigQuery.
O intervalo de consulta dos dados é o que está na condição das queries abaixo.

## Queries
```sql
-- Contagem de Transações no Ethereum por dia
SELECT
  TIMESTAMP_TRUNC(block_timestamp, DAY) AS timestamp1, COUNT(1) AS txn_count
FROM
  bigquery-public-data.crypto_ethereum.transactions
WHERE
  block_timestamp BETWEEN CAST('2015-08-01 00:00:00+00' AS TIMESTAMP) AND CAST('2023-11-23 18:00:00+00' AS TIMESTAMP)
GROUP BY timestamp1
ORDER BY timestamp1
; 

-- Contagem de Transações no Bitcoin por dia
SELECT
  TIMESTAMP_TRUNC(block_timestamp, DAY) AS timestamp1, COUNT(1) AS txn_count
FROM
  bigquery-public-data.crypto_bitcoin.transactions
WHERE
  block_timestamp BETWEEN CAST('2015-08-01 00:00:00+00' AS TIMESTAMP) AND CAST('2023-11-23 18:00:00+00' AS TIMESTAMP)
GROUP BY timestamp1
ORDER BY timestamp1
;
```

# Rodando o experimento
