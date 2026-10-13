from pathlib import Path

import streamlit as st
from resumelens.core.pipeline import process
from resumelens.dsl.parser import CandidateProfileValidationError

st.set_page_config(page_title="ResumeLens", page_icon="📄", layout="wide")
st.title("📄 ResumeLens")
st.caption("Formal Language-Based Resume Screening")

SAMPLES_DIR = Path(__file__).resolve().parent / "data" / "samples"
sample_files = {
    "Full Stack Developer": "full_stack.txt",
    "Machine Learning Engineer": "machine_learning.txt",
    "Backend Developer": "backend.txt",
    "Data Scientist": "data_scientist.txt",
}
input_mode = st.selectbox(
    "Choose a résumé sample or paste your own",
    ["Paste my own résumé", *sample_files],
)
if input_mode == "Paste my own résumé":
    default_text = """Wednesday Addams
3 years of experience developing web applications.
Email: wednesday@example.com
Technical Skills: JS, React.js, NodeJS, Postgres, Git.
Education: Computer Science.
"""
else:
    default_text = (SAMPLES_DIR / sample_files[input_mode]).read_text(encoding="utf-8")

text = st.text_area("Résumé text", value=default_text, height=260)
if st.button("Process résumé", type="primary"):
    try:
        result = process(text)
    except CandidateProfileValidationError as exc:
        st.error(str(exc))
        st.stop()
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
            with st.expander(f"{item.profile}: {'ACCEPTED' if item.accepted else 'REJECTED'}"):
                st.caption(item.explanation)
                st.markdown("**Required DFA sequence**")
                st.code(" → ".join(item.required), language="text")
                st.markdown("**Detected normalized sequence**")
                st.write(" → ".join(item.sequence) if item.sequence else "None")
                st.markdown("**Required qualifications found**")
                matched = [qualification for qualification in item.required if qualification not in item.missing]
                st.write(", ".join(matched) if matched else "None")
                if item.missing:
                    st.markdown("**Missing required qualifications**")
                    st.write(", ".join(item.missing))
    st.caption(
        "Classification is based on each profile's required qualification sequence. "
        "Contact details, education, and experience are extracted for the report but "
        "do not affect acceptance in the current model."
    )
    st.subheader("Stage 4 — Candidate DSL")
    st.code(result.dsl_text, language="text")
    st.subheader("Visualization")
    st.components.v1.html(result.html, height=650, scrolling=True)
