import streamlit as st
from docx import Document
from io import BytesIO
from datetime import datetime

# Configurazione Pagina
st.set_page_config(page_title="Assistente Legale Scuola", layout="wide")
st.title("⚖️ Assistente Legale Scuola (Docenti e ATA)")

# --- ACCESSO ---
password = st.sidebar.text_input("Inserisci Password Accesso", type="password")

if password == "Scuola2026":
    st.sidebar.success("✅ Accesso Autorizzato")
    
    # --- 1. SEZIONE CARICAMENTO ATTI (FOTO/PDF) ---
    st.header("📂 1. Carica gli Atti del Procedimento")
    st.info("Trascina qui la contestazione o scatta una foto per averla come riferimento.")
    file_caricati = st.file_uploader("Scegli i file (PDF, JPG, PNG)", accept_multiple_files=True)
    
    if file_caricati:
        for f in file_caricati:
            st.write(f"✔️ File pronto: **{f.name}**")

    st.markdown("---")

    # --- 2. SEZIONE COMPILAZIONE DIFESA ---
    st.header("✍️ 2. Compila la tua Memoria")
    
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome e Cognome")
        profilo = st.selectbox("Qualifica / Profilo:", 
                             ["-- Seleziona --", 
                              "ATA - Collaboratore Scolastico", 
                              "ATA - Assistente Amministrativo", 
                              "ATA - Assistente Tecnico", 
                              "ATA - DSGA",
                              "Docente - Infanzia/Primaria", 
                              "Docente - Secondaria"])
    with col2:
        scuola = st.text_input("Istituto Scolastico")
        data_c = st.date_input("Data della contestazione")

    st.subheader("🔍 La tua versione dei fatti")
    fatti = st.text_area("Scrivi qui le tue giustificazioni:", height=250)

    # --- 3. TASTO PER GENERARE IL WORD ---
    if st.button("🚀 GENERA E SCARICA DOCUMENTO"):
        if nome and fatti and profilo != "-- Seleziona --":
            # Creazione Documento Word
            doc = Document()
            doc.add_heading('MEMORIA DIFENSIVA', 0)
            doc.add_paragraph(f"Al Dirigente Scolastico del {scuola}")
            doc.add_paragraph(f"\nIl sottoscritto {nome}, profilo {profilo}, espone quanto segue:")
            doc.add_paragraph(fatti)
            doc.add_paragraph("\nSi richiede l'archiviazione del procedimento.")
            
            # Preparazione per il download
            buffer = BytesIO()
            doc.save(buffer)
            buffer.seek(0)
            
            # Tasto per il download effettivo
            st.download_button(
                label="📥 CLICCA QUI PER SCARICARE IL WORD",
                data=buffer,
                file_name=f"Difesa_{nome}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
            st.balloons()
        else:
            st.error("⚠️ Compila Nome, Fatti e seleziona il Profilo!")

else:
    st.warning("🔒 Inserisci la password 'Scuola2026' nella barra laterale.")
