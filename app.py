import streamlit as st
from docx import Document
from io import BytesIO
from datetime import datetime

st.set_page_config(page_title="Assistente Legale Scuola", layout="wide")
st.title("⚖️ Generatore Memoria Difensiva Scolastica")

# --- ACCESSO ---
password = st.sidebar.text_input("Password", type="password")
if password == "Scuola2026":
    
    st.header("📝 Compila i dati della Difesa")
    
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome e Cognome Docente/ATA")
        qualifica = st.selectbox("Qualifica", ["Docente Infanzia", "Docente Primaria", "Docente Secondaria", "Personale ATA"])
        scuola = st.text_input("Istituto Scolastico di servizio")
    with col2:
        protocollo = st.text_input("N. Protocollo Contestazione")
        data_c = st.date_input("Data della Contestazione")
        data_odierna = datetime.now().strftime("%d/%m/%Y")

    st.subheader("🔍 Esposizione dei Fatti e Difesa")
    fatti_utente = st.text_area("Inserisci qui la tua versione dei fatti e le tue giustificazioni:", height=300)

    if st.button("🚀 GENERA DOCUMENTO LEGALE"):
        if nome and fatti_utente:
            doc = Document()
            
            # --- INTESTAZIONE FORMALE ---
            p = doc.add_paragraph()
            p.add_run(f"Al Dirigente Scolastico del {scuola}\n").bold = True
            p.add_run("Ufficio Procedimenti Disciplinari\n\n")
            
            doc.add_heading('MEMORIA DIFENSIVA EX ART. 55-BIS D.LGS. 165/2001', level=1)
            
            # --- CORPO DEL TESTO ---
            doc.add_paragraph(f"Il/La sottoscritto/a {nome}, in servizio presso codesto Istituto in qualità di {qualifica}, "
                              f"con riferimento alla contestazione di addebito prot. n. {protocollo} del {data_c}, "
                              "rassegna le seguenti controdeduzioni:")
            
            doc.add_heading('IN FATTO E IN DIRITTO', level=2)
            doc.add_paragraph(fatti_utente) # Qui incolla quello che scrivi tu
            
            doc.add_paragraph("\nSi evidenzia che la condotta dello scrivente è stata sempre improntata ai doveri di "
                              "correttezza e diligenza previsti dal CCNL Comparto Istruzione e Ricerca.")
            
            doc.add_heading('CONCLUSIONI', level=2)
            doc.add_paragraph("Alla luce di quanto sopra esposto, si richiede l'archiviazione del procedimento disciplinare "
                              "per infondatezza degli addebiti contestati o, in subordine, l'applicazione della sanzione minima.")
            
            doc.add_paragraph(f"\nData: {data_odierna}")
            doc.add_paragraph("\n\nFirma: ___________________________")

            # --- DOWNLOAD ---
            bio = BytesIO()
            doc.save(bio)
            st.download_button(
                label="📥 SCARICA LA MEMORIA COMPLETA (WORD)",
                data=bio.getvalue(),
                file_name=f"Difesa_{nome.replace(' ', '_')}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
            st.balloons()
        else:
            st.error("Inserisci Nome e Descrizione dei fatti!")
