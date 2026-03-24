import streamlit as st
from docx import Document
from io import BytesIO

# 1. Configurazione base
st.set_page_config(page_title="Assistente Legale", layout="centered")
st.title("⚖️ Assistente Legale Scuola")

# 2. Accesso
password = st.sidebar.text_input("Inserisci Password", type="password")

if password == "Scuola2026":
    st.success("Accesso Autorizzato")
    
    # 3. Campi di inserimento
    nome = st.text_input("Nome e Cognome del Docente")
    fatti = st.text_area("Descrivi i fatti (la tua difesa)", height=200)
    
    # 4. IL TASTO (Assicurati che tutto sia allineato qui sotto!)
    if st.button("🚀 CREA IL DOCUMENTO WORD"):
        if nome and fatti:
            # Creazione effettiva del Word
            doc = Document()
            doc.add_heading('MEMORIA DIFENSIVA', 0)
            doc.add_paragraph(f"Il sottoscritto {nome} espone quanto segue:")
            doc.add_paragraph(fatti)
            doc.add_paragraph("\nSi richiede l'archiviazione del procedimento.")
            
            # Salvataggio in memoria
            buffer = BytesIO()
            doc.save(buffer)
            buffer.seek(0)
            
            # 5. IL TASTO DI SCARICAMENTO (Appare solo DOPO il click)
            st.download_button(
                label="📥 CLICCA QUI PER SALVARE IL FILE",
                data=buffer,
                file_name=f"Difesa_{nome}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
            st.balloons()
        else:
            st.error("Per favore, inserisci sia il Nome che i Fatti!")
else:
    st.info("Inserisci la password a sinistra per iniziare.")
