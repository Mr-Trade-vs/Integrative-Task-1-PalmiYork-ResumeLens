import streamlit as st
from resumelens.core.pipeline import process

st.set_page_config(page_title="ResumeLens", page_icon="📄", layout="wide")
st.title("📄 ResumeLens")
st.caption("Formal Language-Based Resume Screening")

sample = """Wednesday Addams\n3 years of experience developing web applications.\nEmail: wednesday@example.com\nTechnical Skills: JS, React.js, NodeJS, Postgres, Git.\nEducation: Computer Science.\n"""
text = st.text_area("Paste résumé text", value=sample, height=260)
if st.button("Process résumé", type="primary"):
    result = process(text)
    a, b, c = st.columns(3)
    with a:
        st.subheader("Stage 1 — Extraction")
        st.json(result.extraction.raw_matches)
    with b:
        st.subheader("Stage 2 — Normalization")
        st.write(result.normalization.mapping)
        st.write(result.normalization.normalized)
    with c:
        st.subheader("Stage 3 — Classification")
        for item in result.classifications:
            st.write(f"**{item.profile}: {'ACCEPTED' if item.accepted else 'REJECTED'}**")
            st.caption(item.explanation)
    st.subheader("Stage 4 — Candidate DSL")
    st.code(result.dsl_text, language="text")
    st.subheader("Visualization")
    st.components.v1.html(result.html, height=650, scrolling=True)
