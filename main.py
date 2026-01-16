import streamlit as st
from openai import OpenAI

modelo = OpenAI(api_key="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")

#titulo
st.write("### SofiaBOT")

#input de chat
mensagemdouser = st.chat_input("Sua mensagem aqui")

if "listademensagens" not in st.session_state:
    st.session_state["systemmessage"] = [  "essa é uma system message, sua função é ajudar na venda",
        "e na matricula no Curso parâmetro redação.",
        "você deve responder as perguntas do cliente de forma direta, mas dando todas as infos necessárias de maneira convincente. comece apresentando as vantagens do curso (sem inventar coisa), a formação da professora, horarios e seus respectivos dias, etc... ",
        "informações cruciais aqui: Nosso curso de redação tem como metodologia principal Oficina de textos dissertativo-argumentativo com foco no Enem/ Uema. Uma vez por semana, o aluno recebe duas  propostas de redação estilo Enem e/ou Uema, escolhe uma e vai produzindo  com acompanhamento em sala.  A outra proposta leva p casa e traz na aula seguinte.", 
        "Todas as redações são corrigidas com base na grade de correção oficial.",
       " O curso possui diferenciais:",
       " ●as turmas são de, no máximo, 12 alunos, o que garante um atendimento bem individualizado;",
        "●o material é gratuito; há um grupo com dicas",
       " ● Os desvios relativos aos aspectos da gramática aplicada ao texto faço a orientação da regra.",

       ' ●Possuo certificação de corretora da banca organizadora das redações do Enem, o que assegura as orientações que dou, assim como a correção, que é adequada às competências exigidas. Especialista em Critica Literária e em Semiótica e analise do discurso. Jornalista (Ufma). Licenciada em Letras (Uema). Cursos de formação de corretor de redação pelas bancas FGV, Cebraspe e Unicamp. Experiência de ensino nas redes pública e privada (+30 anos)',
       'instagram: cursoparametro_redacao',
       'O investimento do curso é de R$250,00 a mensalidade. ',
       'Sendo o contrato para os meses de  Fevereiro  a Novembro.',
       'Obs.: Durante o mês de Julho a monitoria é feita à distância.',

       'Turmas oferecidas para 2026 no momento:',

       'Matutino: ',
       'Quartas-feiras (8h às 11h)',
       'Sábados ( 9h às 12h)',

       'Vespertino: (15h às 18h)',
       'Segundas-feiras ',
       'Terças-feiras',
       'Sextas-feiras ',
       'O curso fica localizado no Edifício La Touche Center, sala 111 (Em frente à loja Jacaré Home Center), COHAJAP.']
    st.session_state["listademensagens"] = []

for mensagem in st.session_state["listademensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

if mensagemdouser:
    st.chat_message("user").write(mensagemdouser)
    mensagem = {"role" : "user", "content" : mensagemdouser}
    st.session_state["listademensagens"].append(mensagem)

    
    mensagemdaia = modelo.chat.completions.create(
        model = "gpt-4o",
        messages = st.session_state["listademensagens"] + st.session_state["systemmessage"]
    )

    respostareal = mensagemdaia.choices[0].message.content
    st.chat_message("assistant").write(respostareal)
    mensagemia = {"role" : "assistant", "content" : respostareal}
    st.session_state["listademensagens"].append(mensagemia)

    #lista de mensagens = dicionario de chave e valor
    #lista: role: user, content: mensagem do user, role: assistant, content: futura mensagem aqui