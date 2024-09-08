import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://www.imdb.com/chart/top/')

posicoes = []
titulos = []
anos = []
duracao = []
categorias = []
pontuacoes = []

items = driver.find_elements(By.CSS_SELECTOR, 'ul.ipc-metadata-list li')
for index, item in enumerate(items):
    print(f"Percorrendo item {index}")
    tituloHeader = item.find_element(By.CSS_SELECTOR, 'div.ipc-title a').text
    posicao = tituloHeader.split(".")[0].strip()
    titulo = tituloHeader.split(".", 1)[1].strip()
    ano = item.find_elements(By.CSS_SELECTOR, 'div.sc-b189961a-7 span')[0].text
    tempo = item.find_elements(By.CSS_SELECTOR, 'div.sc-b189961a-7 span')[1].text
    try:
        categoria = item.find_elements(By.CSS_SELECTOR, 'div.sc-b189961a-7 span')[2].text
    except IndexError:
        categoria = None
    pontuacao = item.find_element(By.CSS_SELECTOR, 'span.ipc-rating-star--rating').text

    posicoes.append(posicao)
    titulos.append(titulo)
    anos.append(ano)
    duracao.append(tempo)
    categorias.append(categoria)
    pontuacoes.append(pontuacao)

df = pd.DataFrame({
    'Hanking': posicoes,
    'Título': titulos,
    'Ano': anos,
    'Duração': duracao,
    'Categoria': categorias,
    'Score': pontuacoes
})
# print(len(items))

df.to_excel('C:\\Users\\arthu\Documents\\power bi\\filmes\\imdb_titulos_e_categorias.xlsx', index=False)
print(df)
# input("Pressione Enter para fechar o navegador...")

