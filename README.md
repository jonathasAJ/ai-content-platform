# 🚀 Viral Insights: Content Performance Predictor

## 📌 Visão Geral
Este projeto nasceu da necessidade de entender os padrões por trás do sucesso de vídeos em plataformas de conteúdo curto. O objetivo é fornecer uma ferramenta capaz de analisar metadados de um vídeo e simular seu potencial de alcance antes mesmo da postagem.

O **Viral Insights** transforma variáveis complexas (como métricas de autoridade, timing e tendências) em uma probabilidade acionável para criadores e estrategistas de conteúdo.

## 🎯 O Problema
No atual cenário das redes sociais, a viralização é o maior ativo de crescimento. No entanto, o processo de distribuição de conteúdo é frequentemente visto como uma "caixa preta". 

Este projeto propõe uma abordagem orientada a dados para:
* Identificar quais fatores estruturais realmente correlacionam-se com picos de visualizações.
* Simular cenários de postagem (melhor horário, duração ideal, impacto do histórico do perfil).
* Oferecer um dashboard intuitivo onde o usuário pode testar diferentes configurações para seu conteúdo.

## 🛠️ Tecnologias
- **Python:** Coração da análise e modelagem.
- **Streamlit:** Interface de simulação em tempo real.
- **Scikit-Learn:** Inteligência por trás da predição.
- **Pandas & Seaborn:** Processamento e visualização de dados.

## 📂 Organização do Projeto
```text
├── api/         # Planejado para integração
├── configs/     # Parâmetros de configuração do projeto
├── dashboard/   # Interface do Simulador (Streamlit)
├── data/        # Datasets e logs de predição
├── models/      # Modelos treinados e scalers (.pkl)
├── notebooks/   # Notebooks de EDA e Modelagem
├── src/         # Lógica central e funções de processamento
└── tests/       # Testes do projeto
```

## 🚀 Como Testar o Projeto

Siga os passos abaixo para configurar o ambiente e executar a aplicação:

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/seu-projeto.git](https://github.com/seu-usuario/seu-projeto.git)
   cd ai-content-platform

2. **Ative o ambiente virtual**
   Escolha o comando de acordo com o seu sistema operacional:

  * **Windows (PowerShell/CMD):**
      ```bash
      .\venv\Scripts\activate
      ```
  
  * **Linux / macOS:**
      ```bash
      source venv/bin/activate
      ```
  
  > [!TIP]
  > Caso o ambiente ainda não exista, crie-o primeiro com: `python -m venv venv`

3. **Instale as dependências:**
   Com o ambiente virtual já ativado, execute o comando abaixo para instalar todas as bibliotecas necessárias de uma só vez:
  
  ```bash
  pip install streamlit pandas joblib scikit-learn numpy
  ```

4. **Inicie o Dashboard:**
   Com as dependências instaladas, execute o comando abaixo para lançar a interface da plataforma:

  ```bash
  streamlit run dashboard/app.py
  ```
