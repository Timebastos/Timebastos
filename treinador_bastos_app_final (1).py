
import streamlit as st

# Título do app
st.title("Treinador Bastos - Agente de Prescrição de Corrida")

# Modo de planejamento
tipo_modo = st.radio("Como deseja montar seu planejamento?", ["Automático", "Manual"])

# Coleta de informações iniciais
st.subheader("📝 Triagem do Corredor")

idade = st.number_input("Idade:", min_value=10, max_value=100, step=1)
peso = st.number_input("Peso (kg):", min_value=30.0, max_value=200.0, step=0.1)

atividade_outros = st.selectbox("Você pratica alguma outra modalidade física atualmente?", ["Não", "Sim, com frequência leve", "Sim, com frequência moderada/alta"])

pergunta1 = st.radio("Você já consegue correr por 30 minutos sem parar?", ["Não", "Sim, com dificuldade", "Sim, de forma confortável"])
pergunta2 = st.radio("Você já participou de alguma prova de corrida (5k, 10k, etc)?", ["Nunca", "Já, mas foi mais por experiência", "Já participei e busco melhorar meu tempo"])
pergunta3 = st.radio("Com que frequência você corre por semana atualmente?", ["Nenhuma", "1 a 2 vezes", "3 ou mais vezes"])
pergunta4 = st.radio("Há quanto tempo você corre?", ["Estou começando agora", "Há alguns meses", "Há mais de 1 ano"])

# Determinação do perfil
respostas = [pergunta1, pergunta2, pergunta3, pergunta4]
pontuacao = sum([0 if r.startswith("Não") or r.startswith("Nunca") or r.startswith("Estou") else 1 if "dificuldade" in r or "alguns" in r or "1 a 2" in r else 2 for r in respostas])
if atividade_outros == "Sim, com frequência moderada/alta":
    pontuacao += 1
elif atividade_outros == "Sim, com frequência leve":
    pontuacao += 0.5

if pontuacao <= 3:
    perfil = "Iniciante Sedentário"
elif pontuacao <= 5:
    perfil = "Iniciante Ativo"
elif pontuacao <= 7:
    perfil = "Iniciante Avançado"
else:
    perfil = "Intermediário ou Superior"

st.markdown(f"### 🏃 Perfil identificado: **{perfil}**")

# Macrociclos
macrociclos = {
    "Linear": "Progressão simples de volume e intensidade. Ideal para iniciantes.",
    "Ondulatório": "Alternância de foco semanal. Bom para intermediários.",
    "Blocos": "Cada fase trabalha uma capacidade (ex: base, ritmo, VO₂). Indicado para avançados.",
    "Polarizado": "80% do volume em baixa intensidade (Z1/Z2) e 20% em alta (Z4/Z5). Eficaz para quem treina muito.",
    "Contemporâneo": "Você monta livremente com base na sua experiência e contexto."
}

# Mesociclos
mesociclos = {
    "Transição": "Pré-temporada ou retorno após lesão. Volume e intensidade reduzidos.",
    "Base": "Construção da base aeróbica, técnica e resistência geral.",
    "Desenvolvimento": "Progressão de carga, ritmo e intensidade moderada.",
    "Choque": "Alta carga concentrada. Exige recuperação posterior.",
    "Competitivo": "Foco em ritmo de prova, precisão e especificidade.",
    "Tapering": "Polimento. Redução estratégica da carga antes da prova."
}

# Microciclos
microciclos = {
    "Adaptação": "Semana inicial leve, foco em técnica e assimilação da carga.",
    "Carga": "Aumento do volume ou intensidade. Estímulo mais exigente.",
    "Estável": "Manutenção da carga da semana anterior. Consolidação.",
    "Choque": "Alta carga concentrada. Exige recuperação na semana seguinte.",
    "Recuperação": "Redução planejada da carga. Recuperação ativa e regeneração.",
    "Polimento": "Semana leve pré-prova. Foco em frescor físico e mental."
}

# Definições automáticas
if tipo_modo == "Automático":
    if "Intermediário" in perfil:
        tipo_macro = "Ondulatório"
    elif "Superior" in perfil:
        tipo_macro = "Blocos"
    else:
        tipo_macro = "Linear"
    tipo_meso = "Base"
    tipo_micro = "Adaptação"
    st.success(f"🧠 Modo automático ativado: {tipo_macro} > {tipo_meso} > {tipo_micro}")
else:
    tipo_macro = st.selectbox("Tipo de macrociclo:", list(macrociclos.keys()))
    st.markdown(f"🔍 **{tipo_macro}:** {macrociclos[tipo_macro]}")

    tipo_meso = st.selectbox("Tipo de mesociclo:", list(mesociclos.keys()))
    st.markdown(f"🧭 **{tipo_meso}:** {mesociclos[tipo_meso]}")

    tipo_micro = st.selectbox("Tipo de microciclo:", list(microciclos.keys()))
    st.markdown(f"📌 **{tipo_micro}:** {microciclos[tipo_micro]}")

# Dias de treino
dias_treino = st.slider("Quantos dias por semana o atleta pode treinar?", 2, 14, 3)

dia_forte = st.selectbox("Dia preferido para o treino mais intenso:", ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"])
dia_longao = st.selectbox("Dia preferido para o treino longo:", ["Sábado", "Domingo"])

# Geração do plano
if st.button("Gerar Plano de Treino da Semana"):
    st.subheader("📋 Plano de Treino Sugerido")
    plano = []
    if perfil.startswith("Iniciante") and tipo_meso in ["Base", "Transição"] and tipo_micro == "Adaptação":
        if dias_treino <= 2:
            plano = [
                "Dia 1: Corrida intervalada leve (4x2min corrida + 3min caminhada)",
                "Dia 2: Técnica de corrida + mobilidade articular"
            ]
        elif dias_treino == 3:
            plano = [
                "Dia 1: Corrida contínua leve 20 min Z2",
                "Dia 2: Técnica + educativo (2x30m skip + dribbling)",
                "Dia 3: Mobilidade leve + respiração nasal"
            ]
        elif dias_treino == 4:
            plano = [
                "Dia 1: Intervalado leve (5x1min corrida + 2min caminhada)",
                "Dia 2: Técnica + força leve (peso corporal)",
                "Dia 3: Corrida contínua 25min Z1-Z2",
                "Dia 4: Mobilidade ativa + relaxamento"
            ]
        else:
            plano = [
                "Dia 1: Corrida leve 20min + core leve",
                "Dia 2: Técnica de corrida + educativos",
                "Dia 3: Intervalado leve",
                "Dia 4: Cross training (bike leve 30min)",
                "Dia 5: Força funcional leve",
                "Dia 6: Corrida contínua + mobilidade",
                "Dia 7: Livre (bike ou alongamento)"
            ]
    else:
        plano = ["Plano detalhado em breve para esse perfil e microciclo."]

    for treino in plano:
        st.markdown(f"- {treino}")
