import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

datasets = [
    'ethereum',
    # 'ethereum-mainnet-us',
    'bitcoin'
    ]
dataframes = []

# Read BigQuery CSV data
for dataset in datasets:
    df = pd.read_csv(f'data/{dataset}-transactions.csv', index_col=0, parse_dates=True)
    df['dataset'] = dataset; # Adiciona uma nova coluna com o nome do dataset em cada linha
    dataframes.append(df) 


txn_df = pd.concat(dataframes)  # Concatena os datasets
txn_df.to_csv('./output/txt_df.csv')

# cria axis para controlar melhor elementos do grafico
fig, ax = plt.subplots()

# remove as bordas para melhor visualizacao
sns.despine(right=True, top=True, ax=ax)
sns.set_style('ticks')


sns.lineplot(x='timestamp1', y='txn_count', hue='dataset', data=txn_df, ax=ax, legend='brief')


ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1)) # Define o intervalo entre cada ponto do eixo x em 1 mês
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y')) # Configura o label do eixo x
plt.xticks(rotation=90, ha='right')

# Define o título e os labels dos eixos
ax.set_title('Número de transações diárias por criptomoeda')
ax.set_xlabel('Time')

# Define um limite pros dados, removendo espaços em branco.
ax.set_xlim(left=txn_df.index[0], right=txn_df.index[len(txn_df.index)-1])


ax.set_ylabel('Txn Count')
ax.set
ax.legend(ncol=1, frameon=False, fontsize=12)


plt.show()
fig.tight_layout()
fig.savefig('./output/experimentos.pdf') # Salva o gráfico como PDF