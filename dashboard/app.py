import streamlit as st
import pandas as pd
import joblib
import os
from pathlib import Path

MODELS_PATH = Path(__file__).parent.parent / "models"

@st.cache_resource
def load_assets():

    model = joblib.load(os.path.join(MODELS_PATH, 'modelo_viral.pkl'))
    scaler = joblib.load(os.path.join(MODELS_PATH, 'scaler.pkl'))
    features = joblib.load(os.path.join(MODELS_PATH, 'features_list.pkl'))

    return model, scaler, features

model, scaler, features_list = load_assets()

st.set_page_config(page_title='Viral Predictor', layout='wide')

st.title("Dashboard de Predição: Viral Insights")

col1, col2 = st.columns([1, 2])

with col1:
    st.header("Parâmetros do Vídeo")
    
    st.subheader("Perfil")
    avg_views = st.number_input("Média de Views do Canal", min_value=0, value=5000, step=500)
    tier = st.selectbox("Tier do Criador", ["Micro", "Mid", "Macro", "Star"])
    
    st.subheader("Conteúdo")
    platform = st.radio("Plataforma", ["TikTok", "YouTube"])
    duration = st.slider("Duração do Vídeo (seg)", 5, 60, 15)
    title_len = st.slider("Tamanho do Título (caracteres)", 1, 100, 30)
    has_emoji = st.checkbox("O título possui emojis?", value=True)
    
    st.subheader("Timing")
    post_hour = st.slider("Hora da Postagem", 0, 23, 18)
    is_weekend_input = st.checkbox("Postar no Final de Semana?")

    import numpy as np
    hour_sin = np.sin(2*np.pi*post_hour/24)
    hour_cos = np.cos(2*np.pi*post_hour/24)

    btn_prever = st.button("Simular Viralização", use_container_width=True)

with col2:
    st.header("Resultado da Análise")
    
    if btn_prever:
        tier_map = {'Micro': 0, 'Mid': 1, 'Macro': 2, 'Star': 3}
        platform_map = {'TikTok': 0, 'YouTube': 1}
        
        input_dict = {
            'platform_encoded': platform_map[platform],
            'duration_sec': duration,
            'creator_avg_views': avg_views,
            'completion_rate': 0.50,         
            'title_length': title_len,
            'has_emoji_encoded': 1 if has_emoji else 0,
            'is_weekend': 1 if is_weekend_input else 0,
            'hour_sin': hour_sin,
            'hour_cos': hour_cos,
            'creator_tier_encoded': tier_map[tier],
            'like_rate': 0.05,               
            'share_rate': 0.01,              
            'engagement_per_1k': 50.0        
        }

        input_df = pd.DataFrame([input_dict])[features_list]

        with st.spinner('A IA está analisando os padrões de engajamento...'):

            input_scaled = scaler.transform(input_df)
            
            probabilidade = model.predict_proba(input_scaled)[0][1]
            
            peso_autoridade = model.coef_[0][features_list.index('creator_avg_views')]

        st.markdown("---")
        
        st.metric(
            label="Probabilidade Estimada de Viralização", 
            value=f"{probabilidade:.1%}",
            delta=f"{probabilidade - 0.25:.1%} em relação à média"
        )

        if probabilidade > 0.5:
            st.balloons()
            st.success("✨ **Alto Potencial!** Este conteúdo tem características de vídeos que furam a bolha.")
        elif probabilidade > 0.3:
            st.info("⚖️ **Potencial Moderado.** O vídeo deve ter uma performance estável, mas pode precisar de um 'empurrão' externo.")
        else:
            st.warning("⚠️ **Baixo Potencial de Viralização.** O modelo sugere que as métricas base não são ideais para o algoritmo atual.")

        st.subheader("💡 Insights do Modelo")
        st.write(f"O fator mais decisivo para o seu perfil é a **Autoridade do Criador** (Peso: {peso_autoridade:.2f}).")
        
        st.caption("""
            *Nota técnica: Este modelo possui um ROC AUC de 0.55. 
            Isso significa que ele é um guia de tendências, não uma garantia de resultados, 
            visto que a viralização possui componentes imprevisíveis.*
        """)