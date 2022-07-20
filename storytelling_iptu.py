import streamlit as st 
from PIL import Image
import pandas as pd
import numpy as np
st.cache(suppress_st_warning=True)
df = pd.read_csv('tresanoscorreto.csv')

image1 = Image.open('C:/Users/WINDOWS/Documents/GitHub/desafios/labfaz.jpg')
st.image(image1)
image = Image.open('C:/Users/WINDOWS/Documents/GitHub/desafios/rio.jpg')
st.image(image, caption='Rio de Janeiro')
st.title('O Rio sob a òtica do IPTU',color='Blue')
st.text('Ao olhar para um cartão postal do Rio é possível ver um contraste belo entre o verde, mata atlântica, o azul, o mar, e o cinza, as edificações')
st.text('Esta é uma das marcas mais cativantes do Rio. Mas como conciliar esses três aspectos? Veremos isso por meio do IPTU do Rio.')
st.write()
st.header('Você sabe o que é o IPTU?')
st.text('O IPTU é a sigla para Imposto Predial e Territorial Urbano. (Fonte: Lei 5.172/66)')
st.text(' Conforme a Lei,o imposto é de responsabilidade dos Municípios.')
st.text('O IPTU é coordenado pela Secretaria Municipal de Fazenda e Planejamento - SMFP')
st.header('Como é calculado o IPTU?')
st.text('')
st.latex(r'''IPTU\ = Valor_{venal} \ x\ Alíquota''')
st.header('Conforme o Rio cresce o IPTU também cresce...')
st.text('O Valor venal é constituído de cinco compomentes.')
st.text('E leva em conta a àrea edificada, isto é, a parte o acinzentado das fotos')
st.markdown('_**20 mil novas construções surgiram nos últimos 3 anos no Rio**_')
mapa = df[['lat','lon']]
st.map(mapa)


