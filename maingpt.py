import streamlit as st
from openai import OpenAI

# --- API key direta (provisório) ---
# Substitua "SUA_CHAVE_AQUI" pela sua chave real da OpenAI
modelo = OpenAI(api_key="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")

# Título
st.write("### Curso Parâmetro")

# Input do usuário
mensagemdouser = st.chat_input("Sua mensagem aqui")
st.chat_message("assistant").write("Olá! Estou disponível para lhe ajudar com qualquer dúvida que tiveres sobre o nosso curso de redação!")

# Inicialização do histórico
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# SYSTEM MESSAGE (não aparece para o usuário)
system_message = {
    "role": "system",
    "content": """
Você é um assistente virtual especializada em atendimento e vendas do Curso Parâmetro Redação.

OBJETIVO:
- Esclarecer dúvidas do cliente
- Apresentar o curso de forma persuasiva e ética
- Conduzir o cliente à matrícula de forma natural

TOM DE VOZ:
- Educado, acolhedor e profissional
- Seguro e persuasivo, sem pressão

ESTRATÉGIA DE VENDAS:
- Destaque os diferenciais do curso
- Reforce autoridade da professora
- Mostre benefícios práticos para o aluno
- Termine respostas com perguntas estratégicas para avançar a conversa

SOBRE O CURSO:
- Oficina de textos dissertativo-argumentativos, foco ENEM/UEMA
- Duas propostas de redação semanais: uma em sala, outra para casa
- Todas corrigidas com base na grade oficial
- Turmas de até 12 alunos
- Material gratuito + grupo com dicas

SOBRE A PROFESSORA(Rosa Maria):
- Corretora certificada ENEM
- Especialista em Crítica Literária e Semiótica
- Jornalista (UFMA), Licenciada em Letras (UEMA)
- Formação corretora de redação FGV, Cebraspe e Unicamp
- Mais de 30 anos de experiência no ensino público e privado

INVESTIMENTO:
- Mensalidade: R$ 250,00
- Contrato de fevereiro a novembro
- Julho: monitoria à distância

TURMAS 2026:
Matutino: Quarta 8h-11h, Sábado 9h-12h
Vespertino: Segunda, Terça e Sexta 15h-18h

LOCAL:
Edifício La Touche Center, sala 111 (frente Jacaré Home Center), COHAJAP

CONTATO:
Instagram: @cursoparametro_redacao
Whatsapp: (98) 98293-6490

FORMAS DE PAGAMENTO:
Pix(98) 98293-6490 e cartao de credito ou debito

Lembre-se que assim que o cliente decidir fazer a matrícula, você deve pedir por essas informações:
Nome do responsavel
Nome do aluno
Numero do aluno
Turma



Assim que ele preencher, peça pelo comprovante do pagamento.
E quando ele enviar, peça para ele entrar no grupo do whatsapp usando esse link: Acesse este link para entrar no meu grupo do WhatsApp: https://chat.whatsapp.com/GoYBc8vqh6TIiTgzo1YlAV

E por ultimo, peça um feedback do atendimento e agradeça o cliente, juntamente ao falar que as aula começam dia 2 de fevereiro
caso o cliente pedir por atendimento humano, peça para ele aguardar.


"""
}

# Exibe histórico de chat (somente user e assistant)
for mensagem in st.session_state["chat_history"]:
    st.chat_message(mensagem["role"]).write(mensagem["content"])

# Quando o usuário envia mensagem
if mensagemdouser:
    # Mostra a mensagem do usuário
    st.chat_message("user").write(mensagemdouser)

    # Adiciona ao histórico
    st.session_state["chat_history"].append(
        {"role": "user", "content": mensagemdouser}
    )

    # Chamada da IA
    resposta = modelo.chat.completions.create(
        model="gpt-4o",
        messages=[system_message] + st.session_state["chat_history"]
    )

    # AQUI está a correção: acessando como atributo
    respostareal = resposta.choices[0].message.content

    # Mostra resposta da IA
    st.chat_message("assistant").write(respostareal)

    # Salva resposta no histórico
    st.session_state["chat_history"].append(
        {"role": "assistant", "content": respostareal}
    )
