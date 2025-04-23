import streamlit as st

# Título do app
st.title("Treinador Bastos - Agente de Prescrição de Corrida")

# Coleta de informações iniciais
titulo = st.subheader("📝 Triagem do Corredor")

idade = st.number_input("Idade:", min_value=10, max_value=100, step=1)
peso = st.number_input("Peso (kg):", min_value=30.0, max_value=200.0, step=0.1)

atividade_outros = st.selectbox("Você pratica alguma outra modalidade física atualmente?", ["Não", "Sim, com frequência leve", "Sim, com frequência moderada/alta"])

pergunta1 = st.radio("Você já consegue correr por 30 minutos sem parar?", ["Não", "Sim, com dificuldade", "Sim, de forma confortável"])
pergunta2 = st.radio("Você já participou de alguma prova de corrida (5k, 10k, etc)?", ["Nunca", "Já, mas foi mais por experiência", "Já participei e busco melhorar meu tempo"])
pergunta3 = st.radio("Com que frequência você corre por semana atualmente?", ["Nenhuma", "1 a 2 vezes", "3 ou mais vezes"])
pergunta4 = st.radio("Há quanto tempo você corre?", ["Estou começando agora", "Há alguns meses", "Há mais de 1 ano"])

# Função para determinar perfil
respostas = [pergunta1, pergunta2, pergunta3, pergunta4]
pontuacao = sum([0 if r.startswith("Não") or r.startswith("Nunca") or r.startswith("Estou") else 1 if "dificuldade" in r or "alguns" in r or "1 a 2" in r else 2 for r in respostas])

# Ajuste por nível de atividade física
if atividade_outros == "Sim, com frequência moderada/alta":
    pontuacao += 1
elif atividade_outros == "Sim, com frequência leve":
    pontuacao += 0.5

# Classificação do perfil
if pontuacao <= 3:
    perfil = "Iniciante Sedentário"
elif pontuacao <= 5:
    perfil = "Iniciante Ativo"
elif pontuacao <= 7:
    perfil = "Iniciante Avançado"
else:
    perfil = "Intermediário ou Superior"

st.markdown(f"### 🏃 Perfil identificado: **{perfil}**")

# Dias de treino disponíveis
dias_treino = st.slider("Quantos dias por semana o atleta pode treinar?", 2, 7, 3)

# Dia preferido para treino forte
dia_forte = st.selectbox("Dia preferido para o treino mais intenso:", ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"])

# Dia preferido para o longão
dia_longao = st.selectbox("Dia preferido para o treino longo:", ["Sábado", "Domingo"])

# Botão para gerar o plano
if st.button("Gerar Plano de Treino da Semana"):
    st.subheader("📋 Plano de Treino Sugerido")
    st.write(f"**Perfil:** {perfil}")
    st.write(f"**Idade:** {idade} anos | **Peso:** {peso} kg")
    st.write(f"**Dias de treino:** {dias_treino} por semana")
    st.write(f"**Treino mais forte:** {dia_forte}")
    st.write(f"**Longão:** {dia_longao}")

    plano = []
    if perfil.startswith("Iniciante"):
        if dias_treino == 2:
            plano = [
                "Dia 1: 4x(2 min trote leve + 3 min caminhada) + 5 min caminhada inicial/final",
                "Dia 2: 20 min corrida contínua leve com pausas livres + 2x30m skip alto"
            ]
        elif dias_treino == 3:
            plano = [
                "Dia 1: 4x(2 min trote leve + 3 min caminhada)",
                "Dia 2: Técnica: 2x30m joelho alto + 2x saltitos + 15 min leve",
                "Dia 3: 30 min Z2 com pausas se necessário"
            ]
        else:
            plano = [
                "Dia 1: 5x(1 min corrida leve + 2 min caminhada)",
                "Dia 2: Técnica de corrida + circuito leve de mobilidade",
                "Dia 3: 20 min contínuo com foco em cadência",
                "Dia 4: 30 min Z1/Z2 com foco em respiração e conforto"
            ]
    else:
        plano = ["Plano detalhado em breve para perfis mais avançados."]

    for treino in plano:
        st.markdown(f"- {treino}")
