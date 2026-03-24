import streamlit as st
from docx import Document
from io import BytesIO

# Configurazione Pagina
st.set_page_config(page_title="Assistente Legale Scuola", layout="wide")

st.title("⚖️ Assistente Legale Scuola")
st.write("Generatore automatico di Memorie Difensive e Gestione Documenti")

# BARRA LATERALE - PROTEZIONE
st.sidebar.header("Area Riservata")
password = st.sidebar.text_input("Inserisci Password Accesso", type="password")

# --- CONTROLLO PASSWORD ---
if password == "Scuola2026":
    st.sidebar.success("✅ Accesso Autorizzato")
    
    # --- SEZIONE 1: CARICAMENTO DOCUMENTI ---
    st.header("📂 1. Carica Documenti (Foto o PDF)")
    uploaded_files = st.file_uploader("Trascina qui i documenti o scatta una foto", accept_multiple_files=True)
    
    if uploaded_files:
        st.success(f"Hai caricato {len(uploaded_files)} file.")
        for file in uploaded_files:
            st.write(f"📄 Ricevuto: **{file.name}**")

    st.markdown("---")

    # --- SEZIONE 2: DATI DOCENTE ---
    st.header("✍️ 2. Compila la Difesa")
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome e Cognome Docente")
        codice_fiscale = st.text_input("Codice Fiscale")
    with col2:
        data_contestazione = st.date_input("Data ricezione contestazione")
        st.info("Termine ultimo invio: 15 giorni dalla ricezione.")

    # DESCRIZIONE FATTI
    fatti = st.text_area("Descrivi i fatti (saranno inseriti nella memoria):", height=200, placeholder="Esempio: In data 10/03/2026, durante l'ora di lezione...")

    # --- SEZIONE 3: GENERAZIONE E DOWNLOAD ---
    if st.button("🚀 GENERA E SCARICA PACCHETTO"):
        if nome and fatti:
            # Creazione file Word
            doc = Document()
            doc.add_heading(f'MEMORIA DIFENSIVA', 0)
            doc.add_paragraph(f'Il sottoscritto/a {nome}, nato/a il..., residente a...')
            doc.add_paragraph(f'\nOGGETTO: Controdeduzioni alla contestazione del {data_contestazione}')
            doc.add_heading('ESPOSIZIONE DEI FATTI', level=1)
            doc.add_paragraph(fatti)
            doc.add_paragraph('\nCon osservanza, \n\nFirma __________________')

            # Preparazione download
            bio = BytesIO()
            doc.save(bio)
            
            st.download_button(
                label="📥 CLICCA QUI PER SCARICARE IL WORD",
                data=bio.getvalue(),
                file_name=f"Difesa_{nome.replace(' ', '_')}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
            st.balloons()
        else:
            st.error("⚠️ Inserisci almeno il Nome e i Fatti per generare il documento.")

else:
    # Schermata di blocco
    st.warning("🔒 Inserisci la password nella barra laterale per sbloccare le funzioni.")
    st.info("Suggerimento: La sezione documenti apparirà solo dopo l'accesso.")
