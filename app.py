import streamlit as st
from docx import Document
from io import BytesIO

# Configurazione Pagina
st.set_page_config(page_title="Assistente Legale Scuola", layout="wide")

st.title("⚖️ Assistente Legale Scuola")
st.write("Generatore automatico di Memorie Difensive e Deleghe")

# BARRA LATERALE - PROTEZIONE
st.sidebar.header("Area Riservata")
password = st.sidebar.text_input("Inserisci Password Accesso", type="password")

# --- CONTROLLO PASSWORD ---
if password == "Scuola2026":
    st.sidebar.success("✅ Accesso Autorizzato")
    
    # 1. DATI DOCENTE
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome e Cognome Docente")
        codice_fiscale = st.text_input("Codice Fiscale")
    with col2:
        data_contestazione = st.date_input("Data ricezione contestazione")
        scadenza = st.info(f"Termine ultimo invio: 15 giorni dalla ricezione.")

    # 2. DESCRIZIONE FATTI
    fatti = st.text_area("Descrivi brevemente i fatti accaduti (saranno inseriti nella memoria):", height=200)

    # 3. GENERAZIONE DOCUMENTO
    if st.button("🚀 GENERA MEMORIA DIFENSIVA"):
        if nome and fatti:
            # Creazione file Word in memoria
            doc = Document()
            doc.add_heading(f'Memoria Difensiva - {nome}', 0)
            doc.add_paragraph(f'Il sottoscritto {nome}, nato il..., residente a...')
            doc.add_paragraph(f'\nOGGETTO: Controdeduzioni alla contestazione del {data_contestazione}')
            doc.add_heading('ESPOSIZIONE DEI FATTI', level=1)
            doc.add_paragraph(fatti)
            doc.add_paragraph('\nCon osservanza, \nFirma __________________')

            # Preparazione download
            bio = BytesIO()
            doc.save(bio)
            
            st.download_button(
                label="📥 SCARICA MEMORIA (WORD)",
                data=bio.getvalue(),
                file_name=f"Memoria_{nome.replace(' ', '_')}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
            st.balloons()
        else:
            st.error("⚠️ Inserisci almeno il Nome e i Fatti per procedere.")

else:
    # Cosa vede l'utente se la password è vuota o sbagliata
    st.warning("🔒 Inserisci la password corretta nella barra laterale per sbloccare le funzioni.")
    st.image("https://img.icons8.com/clouds/200/law.png")
