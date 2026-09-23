import pandas as pd

def limpar_dados_automatico(ficheiro_entrada, ficheiro_saida):
    # Lê o ficheiro de dados original
    df = pd.read_csv(ficheiro_entrada)
    
    # Remove linhas duplicadas automaticamente
    df = df.drop_duplicates()
    
    # Preenche valores em falta com um indicador padrão
    df = df.fillna("Não Registado")
    
    # Guarda o novo ficheiro limpo
    df.to_csv(ficheiro_saida, index=False)
    print(f"Sucesso! Dados tratados guardados em: {ficheiro_saida}")

# Exemplo de chamada da função:
# limpar_dados_automatico('vendas_brutas.csv', 'vendas_tratadas.csv')
