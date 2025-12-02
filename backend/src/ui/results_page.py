import streamlit as st
from src.ml.predictor import predict_all
from src.utils.explain_results import explain
from src.utils.charts import show_value_vs_range

def show_results():
    st.header("Predictions & Explanations")
    values = st.session_state.get("input_values", {})
    if not values:
        st.info("No input values found. Go to 'Manual Input' or 'Upload Report (OCR)' first.")
        return

    st.subheader("Input Values Used")
    st.write(values)

    preds = predict_all(values)
    st.subheader("Model Probabilities")
    for k, v in preds.items():
        prob = v.get("probability")
        error_or_missing = v.get("error")
        if prob is None:
            st.write(f"{k.title()}: Model not available or error ({error_or_missing})")
        else:
            st.metric(label=f"{k.title()} risk", value=f"{prob*100:.1f}%")
            if error_or_missing:
                st.warning(f"Missing features for {k}: {error_or_missing}")

    st.markdown("---")
    expl = explain(values, preds)
    st.subheader("Explanations")
    for k, msg in expl.items():
        st.write(f"- {msg}")

    st.markdown("---")
    st.subheader("Value vs Normal Range Charts")
    for k, val in values.items():
        try:
            show_value_vs_range(k, float(val))
        except Exception:
            pass
