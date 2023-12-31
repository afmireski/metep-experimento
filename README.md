# Instalando dependências
- [Instalar o pandas](https://pandas.pydata.org/docs/getting_started/install.html)
- [Instalar o matplotlib](https://matplotlib.org/stable/users/installing/index.html)
- [Instalar o seaborn](https://seaborn.pydata.org/installing.html)
```bash
# Arch
sudo pacman -S python-pandas

sudo pacman -S python-matplotlib

sudo pacman -S python-seaborn

# PyPi
pip install pandas

pip install matplotlib

pip install seaborn
```

# Obtendo os dados
Os gráficos são montados a partir do processamento de dois arquivos CSVs que contém o número de transações diárias das redes Ethereum e Bitcoin.
Esses arquivos foram gerados a partir da consulta em datasets públicos com dados das duas redes disponíveis no [Google BigQuery](https://console.cloud.google.com/bigquery).
No caso do Ethereum existem dois datasets, mas ambos geram o mesmo resultado, ou seja, são equivalentes.
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

-- Ethereum Mainnet Dataset
SELECT
  TIMESTAMP_TRUNC(block_timestamp, DAY) AS timestamp1, COUNT(1) AS txn_count
FROM
  bigquery-public-data.goog_blockchain_ethereum_mainnet_us.transactions
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

-- Dados até 2019, mais próximo do período do artigo
-- Contagem de Transações no Ethereum por dia
SELECT
  TIMESTAMP_TRUNC(block_timestamp, DAY) AS timestamp1, COUNT(1) AS txn_count
FROM
  bigquery-public-data.crypto_ethereum.transactions
WHERE
  block_timestamp BETWEEN CAST('2015-08-01 00:00:00+00' AS TIMESTAMP) AND CAST('2019-12-01 18:00:00+00' AS TIMESTAMP)
GROUP BY timestamp1
ORDER BY timestamp1
; 

-- Ethereum Mainnet Dataset
SELECT
  TIMESTAMP_TRUNC(block_timestamp, DAY) AS timestamp1, COUNT(1) AS txn_count
FROM
  bigquery-public-data.goog_blockchain_ethereum_mainnet_us.transactions
WHERE
  block_timestamp BETWEEN CAST('2015-08-01 00:00:00+00' AS TIMESTAMP) AND CAST('2019-12-01 18:00:00+00' AS TIMESTAMP)
GROUP BY timestamp1
ORDER BY timestamp1
;

-- Contagem de Transações no Bitcoin por dia
SELECT
  TIMESTAMP_TRUNC(block_timestamp, DAY) AS timestamp1, COUNT(1) AS txn_count
FROM
  bigquery-public-data.crypto_bitcoin.transactions
WHERE
  block_timestamp BETWEEN CAST('2015-08-01 00:00:00+00' AS TIMESTAMP) AND CAST('2019-12-01 18:00:00+00' AS TIMESTAMP)
GROUP BY timestamp1
ORDER BY timestamp1
;

```

# Rodando o experimento
1. Escolha quais CSVs deseja utilizar. Comente e descomente os elementos em `datasets`.
  1.1 Colocar um `2019` na frente de `transactions`, na linha 15, monta um gráfico com o período mais próximo daquele no artigo.
2. Execute `experimento.py` chamando `python ./experimento.py` ou use seu editor.
3. O resultado esperado é um gráfico com o número de transações diárias de cada dataset.

# Objetivos e conclusões
O objetivo desse experimento é replicar o gráfico da figura 3, presente no artigo de ABDULLAH A. ZARIR et.al. Os autores em teoria utilizaram os mesmos datasets disponíveis no Google BigQuery para desenvolver sua tese.

Porém o que observei foi uma grande discrepância no gráfico, para o mesmo período. Como os [dados originais](https://github.com/SAILResearch/suppmaterial-18-zarir-ethereum_gas_usage) utilizados pelos pesquisadores aparentemente não estão mais disponíveis fica difícil saber se a discrepância se dá por conta de mudanças no dataset ou por falha minha.
Em 2021 o Ethereum trocou seu mecanismo de consenso de uma base Proof-of-Work para uma Proof-of-Stake, num evento conhecido como [The Merge](https://ethereum.org/pt/roadmap/merge/), talvez essa troca tenha tido algum efeito como causa da discrepância dos dados, mas é só uma especulação, seria necessário uma análise mais afundo para afirmar qualquer coisa.

# Extras
- [Artigo](https://dl.acm.org/doi/10.1145/3431726)
