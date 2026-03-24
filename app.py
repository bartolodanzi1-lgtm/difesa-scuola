import streamlit as st
from docx import Document
from io import BytesIO
from datetime import datetime

st.set_page_config(page_title="Assistente Legale Scuola", layout="wide")
st.title("⚖️ Assistente Legale Personale Scuola (Docenti e ATA)")

# --- ACCESSO ---
password = st.sidebar.text_input("Inserisci Password", type="password")

if password == "Scuola2026":
    st.sidebar.success("✅ Accesso Autorizzato")
    
    st.header("📝 Dati per la Memoria Difensiva")
    
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome e Cognome")
        # Menu di selezione migliorato
        ruolo = st.selectbox("Seleziona il tuo Profilo:", 
                            ["-- Seleziona --", "Personale ATA (Collaboratore Scolastico)", "Personale ATA (Assistente Amm.vo/Tecnico)", "Docente Infanzia/Primaria", "Docente Secondaria", "DSGA"])
        scuola = st.text_input("Istituto Scolastico di appartenenza")
    
    with col2:
        protocollo = st.text_input("N. Protocollo Contestazione")
        data_c = st.date_input("Data della Contestazione")
        data_odierna = datetime.now().strftime("%d/%m/%Y")

    st.subheader("🔍 La tua Difesa")
    fatti_utente = st.text_area("Scrivi qui i fatti e le tue giustificazioni:", height=300, placeholder="Esempio: In merito all'addebito contestato, preciso che...")

    # --- GENERAZIONE ---
    if st.button("🚀 GENERA DOCUMENTO"):
        if nome and fatti_utente and ruolo != "-- Seleziona --":
            doc = Document()
            
            # Intestazione
            p = doc.add_paragraph()
            p.add_run(f"Al Dirigente Scolastico del {scuola}\n").bold = True
            p.add_run("Ufficio Procedimenti Disciplinari\n\n")
            
            doc.add_heading('MEMORIA DIFENSIVA EX ART. 55-BIS D.LGS. 165/2001', level=1)
            
            # Testo formale
            doc.add_paragraph(f"Il/La sottoscritto/a {nome}, in servizio presso codesto Istituto con il profilo di {ruolo}, "
                              f"in relazione alla contestazione di addebito prot. n. {protocollo} del {data_c}, "
                              "espone quanto segue a propria difesa:")
            
            doc.add_heading('ESPOSIZIONE DEI FATTI', level=2)
            doc.add_paragraph(fatti_utente)
            
            doc.add_paragraph("\nIl sottoscritto ribadisce la propria correttezza operata nel rispetto del CCNL Comparto Istruzione e Ricerca.")
            
            doc.add_heading('CONCLUSIONI', level=2)
            doc.add_paragraph("Si richiede formalmente l'archiviazione del procedimento disciplinare per insussistenza degli addebiti.")
            
            doc.add_paragraph(f"\nData: {data_odierna}")
            doc.add_paragraph("\n\nFirma: ___________________________")

            # Buffer per il download
            bio = BytesIO()
            doc.save(bio)
            bio.seek(0)
            
            # TASTO DI DOWNLOAD CHE APPARE ORA
            st.download_button(
                label="📥 CLICCA QUI PER SCARICARE IL FILE WORD",
                data=bio,
                file_name=f"Memoria_{nome.replace(' ', '_')}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
            st.balloons()
        else:
            st.error("⚠️ Attenzione: Inserisci il Nome, i Fatti e seleziona il Profilo (ATA o Docente)!")

else:
    st.warning("🔒 Inserisci la password 'Scuola2026' nella barra a sinistra.")
