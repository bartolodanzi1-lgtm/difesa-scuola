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
    
    # --- 1. CARICAMENTO DOCUMENTI ---
    st.header("📂 1. Caricamento Documenti Procedimento")
    st.info("Qui puoi caricare la contestazione ricevuta (Foto o PDF) per averla sottomano.")
    uploaded_files = st.file_uploader("Trascina qui i file o scatta una foto", accept_multiple_files=True)
    
    if uploaded_files:
        for file in uploaded_files:
            st.write(f"✅ Documento caricato: **{file.name}**")

    st.markdown("---")

    # --- 2. COMPILAZIONE DATI ---
    st.header("✍️ 2. Dati per la Memoria Difensiva")
    
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome e Cognome")
        ruolo = st.selectbox("Qualifica / Profilo Professionale:", 
                            ["-- Seleziona --", 
                             "ATA - Collaboratore Scolastico", 
                             "ATA - Assistente Amministrativo", 
                             "ATA - Assistente Tecnico", 
                             "ATA - DSGA",
                             "Docente - Infanzia/Primaria", 
                             "Docente - Secondaria I/II grado"])
        scuola = st.text_input("Istituto Scolastico di Servizio")
    
    with col2:
        protocollo = st.text_input("N. Protocollo Contestazione")
        data_c = st.date_input("Data della Contestazione")
        data_odierna = datetime.now().strftime("%d/%m/%Y")

    st.subheader("🔍 Esposizione della Difesa")
    fatti_utente = st.text_area("Descrivi i fatti e le tue controdeduzioni:", height=250, 
                                placeholder="Esempio: In merito a quanto contestato, si precisa che la condotta tenuta...")

    # --- 3. GENERAZIONE E DOWNLOAD ---
    if st.button("🚀 GENERA MEMORIA DIFENSIVA"):
        if nome and fatti_utente and ruolo != "-- Seleziona --" and scuola:
            doc = Document()
            
            # Intestazione formale
            header = doc.add_paragraph()
            header.add_run(f"Al Dirigente Scolastico del {scuola}\n").bold = True
            header.add_run("Ufficio Procedimenti Disciplinari\n\n")
            
            doc.add_heading('MEMORIA DIFENSIVA EX ART. 55-BIS D.LGS. 165/2001', level=1)
            
            # Corpo del testo
            doc.add_paragraph(f"Il/La sottoscritto/a {nome}, in servizio presso codesto Istituto in qualità di {ruolo}, "
                              f"con riferimento alla contestazione di addebito prot. n. {protocollo} del {data_c}, "
                              "rassegna le seguenti controdeduzioni a propria difesa:")
            
            doc.add_heading('MOTIVAZIONI E FATTI', level=2)
            doc.add_paragraph(fatti_utente)
            
            doc.add_paragraph("\nLo scrivente ribadisce di aver sempre operato nel pieno rispetto dei doveri d'ufficio "
                              "e delle disposizioni del CCNL Comparto Istruzione e Ricerca.")
            
            doc.add_heading('CONCLUSIONI', level=2)
            doc.add_paragraph("Tutto ciò premesso, si richiede l'archiviazione del procedimento disciplinare "
                              "per insussistenza degli addebiti contestati.")
            
            doc.add_paragraph(f"\nData: {data_odierna}")
            doc.add_paragraph("\n\nFirma: ___________________________")

            # Preparazione download
            bio = BytesIO()
            doc.save(bio)
            bio.seek(0)
            
            st.download_button(
                label="📥 SCARICA ORA LA MEMORIA (WORD)",
                data=bio,
                file_name=f"Difesa_{nome.replace(' ', '_')}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
            st.balloons()
        else:
            st.error("⚠️ Errore: Compila tutti i campi obbligatori (Nome, Scuola, Fatti) e seleziona il profilo (ATA/Docente).")

else:
    st.warning("🔒 Inserisci la password 'Scuola2026' nella barra laterale per sbloccare l'app.")
