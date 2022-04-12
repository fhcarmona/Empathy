# AUTHOR: PERALTA GAMES
# SCOPE:

label scene_0200(caminho):

    if caminho==0:
        scene black

        tln "17/04/2022 - 11:37h | SALA DE INTERROGATORIO"

        # LIMPA A TELA E MOSTRA O AMBIENTE
        scene interrogation-room
        with dissolve

        #
        i01 "Olá [p01_nome], acredito que lembre de nós"
        i01 "Iremos fazer algumas perguntas em relação ao ocorrido"
        i02 "Poderia nos contar como foi no dia do ocorrido?"
        p01 "Agora desejam que eu fale? Para que irei falar, se irão usar contra mim."
        i01 "O seu caso já tem uma determinação, apenas estamos tentando preencher umas papeladas"
        i02 "Colaborar com a investigação pode ser benéfico para você"
        p01 "Qual seria esse benefício?"
        i02 "Dependendo do quanto colaborar poderemos ajudar em sua sentença"
        p01 "Entendo, então para isso, desejo meu advogado"
        i02 "Iremos contactar ele"

        scene black

        tln "17/04/2022 - 14:11h | SALA DE INTERROGATORIO"

        # LIMPA A TELA E MOSTRA O AMBIENTE
        scene interrogation-room
        with dissolve

        adv "Com isso podemos começar"
        i02 "Está certo"
        i01 "Continuando... Poderia nos contar como foi no dia do ocorrido?"
        p01 "Bom... Naquele dia eu estava na festa de aniversário de uma amiga da minha filha"
        p01 "Ela foi convidada e como minha mulher estava trabalhando, eu acompanhei ela na festa"
        i01 "Antes do ocorrido, o que você estava fazendo?"
        p01 "Eu estava na mesa de comida, fazendo um prato para minha filha"
        i02 "E após isso, você viu algo quando olhou para a filha?"
        p01 "Exato, ele a estava machucando..."
        i02 "Como exatamente ele a estava machucando?"
        p01 "Machucou seu braço, ela começou a chorar"
        i02 "E depois que você notou isso? O que aconteceu?"
        p01 "Eu não me recordo... Lembro que fiquei furioso e apaguei"
        p01 "Quando me dei conta, estava sendo imobilizado por vocês"
        i01 "É comum o senhor apagar desta forma?"
        p01 "Não, eu estava para mudar minha prescrição"
        i01 "Entendo, bom, acredito que terminamos por hora"
        i02 "Muito obrigado pela colaboração"

        scene black

        tln "17/04/2022 - 16:47h | ENTRADA DA DELEGACIA"

        # LIMPA A TELA E MOSTRA O AMBIENTE
        scene police-street
        with dissolve

        i02 "Finalmente uma pausa"
        i01 "Fazer papelada burocrática é a pior parte do nosso trabalho"
        i02 "Depois que houve a troca de delegado tudo parece ter piorado"
        i01 "Disseram no comunicado que é um afastamento temporário, até que termine a investigação da corregedoria"
        i01 "Não acho que ele tenha feito por mal, mas a população caiu em cima"
        i02 "Por causa do caso do Serial Killer?"
        i01 "Exato, talvez até alguns policiais seriam afastados"
        i02 "O delegado puxou a responsabilidade para ele"

        menu:
            "Visitar a psiquiatra?"

            "Sim":
                i01 "Bom, vamos finalizar a pausa e dar uma passada na psiquiatra"
                i02 "Está certo, vou pegar o bloco de anotações"

                # ENTRA NOVAMENTE NO CENA 0200 AFIM DE INVESTIGAR A PSIQUIATRA
                call scene_0200(1)

            "Não":
                i02 "Bom, vamos voltar para a delegacia"
                i01 "Sim, tem algumas coisas para finalizar ainda"

    elif caminho==1:
        scene black

        tln "18/04/2022 - 9:03h | CLINICA PSIQUIATRICA"

        # LIMPA A TELA E MOSTRA O AMBIENTE
        scene clinic-reception
        with dissolve

        i01 "Bom dia Doutora [psi_nome], somos os agentes [a01_nome] e este é o [a02_nome], somos responsáveis pelo caso de um de seus pacientes"
        i01 "Poderia nos ajudar com algumas questões?"
        psi "Somente com ordem judicial"
        i02 "Sem problemas, aqui está"
        psi "Vejo que é sobre o paciente [p01_nome]"
        psi "Entre comigo, vamos ao consultório"

        # LIMPA A TELA E MOSTRA O AMBIENTE
        scene clinic
        with dissolve

        i01 "A quanto tempo estava tratando o paciente [p01_nome]?"
        psi "Três meses aproximadamente"
        i01 "Conseguiria descrever a última sessão do [p01_nome]?"
        psi "Claro, ele estava me descrevendo os sonhos do dia anterior"
        psi "É uma rotina que temos quando ele os tem"
        i02 "Poderia descrever esses sonhos?"
        psi "Na descrição que me foi passada, ele descrevia que estava impotente em não conseguir ajudar sua filha"
        i01 "Entendo..."
        i02 ""
        psi "Surto? O que aconteceu?"

        if psi_001==0:
            i01 "Ele começou a ficar agressivo e agrediu um homem na festa de uma amiga da filha"
            i01 "Só conseguiram conter a agressão depois de algum tempo"
            i02 "Infelizmente o homem se encontra internado, foi determinado a prisão do [paciente]"
        else:
            i01 "Ele começou a ficar agressivo e quase agrediu um homem na festa de uma amiga da filha"
            i01 "Começou a ficar agressivo após ver a filha no colo do pai da aniversariante"
            i02 "Por sorte o surto dele foi controlado, mas isso infligiu a determinação jurídica e ele voltará a prisão"

        psi "Nossa..."
        i01 "E por determinação do delegado estamos aqui para entender melhor sobre o caso dele"
        i02 "Esse surto é incomum para quem está em tratamento, certo?"
        psi "Certo..."
        i02 "Algum medicamento poderia ter causado o surto?"
        psi "O que está querendo sugerir com isso? Que indiquei tratamento errado de propósito?"
        i02 "Não se ofenda doutora, estamos apenas investigando. Poderia causar um surto?"
        psi "Não, de forma nenhuma."
        psi "A prescrição controla os surtos"
    return
