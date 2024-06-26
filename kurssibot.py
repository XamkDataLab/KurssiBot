from openai import OpenAI
import streamlit as st
from prompts import *

client = OpenAI(api_key=st.secrets["apikey"])

st.title("KurssiBot")

st.write('''
Voin auttaa monin eri tavoin, erityisesti tieteellisten artikkelien analysoinnissa ja tutkimusaiheiden käsittelyssä. Tässä on joitakin tapoja, joilla voin olla avuksi:
- Ymmärtäminen: Voin auttaa sinua ymmärtämään tieteellisiä artikkeleita, selittää vaikeita konsepteja ja termejä selkeästi ja yksinkertaisesti.
- Yhteenvetojen luominen: Voin auttaa sinua tiivistämään tieteellisen artikkelin sisältöä, jotta saat nopean käsityksen sen pääasioista.
- Tutkimusmetodien analysointi: Voin auttaa sinua ymmärtämään artikkelin käyttämiä tutkimusmenetelmiä, sen vahvuuksia ja heikkouksia.
- Tulosten tulkinta: Voin auttaa sinua tulkitsemaan ja ymmärtämään artikkelin tuloksia sekä niiden merkitystä.
- Kriittinen arviointi: Voin auttaa sinua tarkastelemaan artikkelin väitteitä kriittisesti, tunnistamaan mahdolliset puolueellisuudet tai rajoitukset.
- Lähteen luotettavuuden arviointi: Voin auttaa arvioimaan artikkelin ja julkaisun luotettavuutta ja uskottavuutta.
- Viittausten ja lähdeluettelon hallinta: Voin antaa neuvoja siitä, miten käsitellä viitteitä ja pitää huolta asianmukaisesta lähdeviittaustavasta.
''')

st.session_state.setdefault("openai_model", "gpt-4-0125-preview")

article = st.text_area("Kopioi artikkelin teksti tähän", height=300)
question = st.text_input("Mitä haluat")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": system_prompt_content2}]

if st.button('Käynnistä'):
    if article and question:
        full_prompt = article + " " + question 
        st.session_state.messages.append({"role": "user", "content": full_prompt})  

        with st.chat_message("user"):
            st.markdown(question)  

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            with st.spinner('Puppugeneraattori aktivoitu. Kärsivällisyyttä, suurten tekstimäärien kanssa voin olla hieman hidas'):
                for response in client.chat.completions.create(
                    model=st.session_state["openai_model"],
                    messages=st.session_state.messages,
                    stream=True):
                    if response.choices[0].delta.role != "system":
                        content = response.choices[0].delta.content
                        if content is not None:
                            full_response += content
                message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})




