# AUTHOR: PERALTA GAMES
# SCOPE:

label scene_0200(caminho):

    if caminho==0:
        hide screen cluesUI

        scene black

        tln "17/04/2022 - 11:37h | SALA DE INTERROGATORIO"

        # LIMPA A TELA E MOSTRA O AMBIENTE
        scene interrogation-room
        with dissolve

        show screen cluesUI

        #
        $ narrative_image("i01", left, None, i01, "Olá [p01_nome], acredito que lembre de nós") # i01 "Olá [p01_nome], acredito que lembre de nós"
        $ narrative_image("i01", left, None, i01, "Iremos fazer algumas perguntas em relação ao ocorrido") # i01 "Iremos fazer algumas perguntas em relação ao ocorrido"
        $ narrative_image("i02", left, None, i02, "Poderia nos contar o que aconteceu naquele dia?") # i02 "Poderia nos contar o que aconteceu naquele dia?"
        $ narrative_image("p01", right, None, p01, "Agora desejam que eu fale? Para que irei falar, se irão usar contra mim.") # p01 "Agora desejam que eu fale? Para que irei falar, se irão usar contra mim."
        $ narrative_image("i01", left, None, i01, "O seu caso já tem uma sentença, queremos apenas preencher a papelada e dá-lo por encerrados") # i01 "O seu caso já tem uma sentença, queremos apenas preencher a papelada e dá-lo por encerrados"
        $ narrative_image("i02", left, None, i02, "Colaborar com a investigação pode ser benéfico para você") # i02 "Colaborar com a investigação pode ser benéfico para você"
        $ narrative_image("p01", right, None, p01, "Qual seria esse benefício?") # p01 "Qual seria esse benefício?"
        $ narrative_image("i02", left, None, i02, "Dependendo do quanto colaborar poderemos ajudar em sua sentença") # i02 "Dependendo do quanto colaborar poderemos ajudar em sua sentença"
        $ narrative_image("p01", right, None, p01, "Entendo, então para isso, desejo meu advogado") # p01 "Entendo, então para isso, desejo meu advogado"
        $ narrative_image("i02", left, None, i02, "Iremos contactar ele") # i02 "Iremos contactar ele"

        hide screen cluesUI

        scene black

        tln "17/04/2022 - 14:11h | SALA DE INTERROGATORIO"

        # LIMPA A TELA E MOSTRA O AMBIENTE
        scene interrogation-room
        with dissolve

        show screen cluesUI

        $ narrative_image("adv", right, None, adv, "Com isso podemos começar") # adv "Com isso podemos começar"
        $ narrative_image("i02", left, None, i02, "Está certo") # i02 "Está certo"
        $ narrative_image("i01", left, None, i01, "Continuando... Poderia nos contar como foi no dia do ocorrido?") # i01 "Continuando... Poderia nos contar como foi no dia do ocorrido?"
        $ narrative_image("p01", right, None, p01, "Bom... Naquele dia eu estava na festa de aniversário de uma amiga da minha filha") # p01 "Bom... Naquele dia eu estava na festa de aniversário de uma amiga da minha filha"
        $ narrative_image("p01", right, None, p01, "Ela foi convidada e como minha mulher estava trabalhando, eu acompanhei ela na festa") # p01 "Ela foi convidada e como minha mulher estava trabalhando, eu acompanhei ela na festa"
        $ narrative_image("i01", left, None, i01, "Antes do ocorrido, o que você estava fazendo?") # i01 "Antes do ocorrido, o que você estava fazendo?"
        $ narrative_image("p01", right, None, p01, "Eu estava na mesa de comida, fazendo um prato para minha filha") # p01 "Eu estava na mesa de comida, fazendo um prato para minha filha"
        $ narrative_image("i02", left, None, i02, "E após isso, você viu algo quando olhou para a filha?") # i02 "E após isso, você viu algo quando olhou para a filha?"
        $ narrative_image("p01", right, None, p01, "Exato, ele a estava machucando...") # p01 "Exato, ele a estava machucando..."
        $ narrative_image("i02", left, None, i02, "Como exatamente ele a estava machucando?") # i02 "Como exatamente ele a estava machucando?"
        $ narrative_image("p01", right, None, p01, "Machucou seu braço, ela começou a chorar") # p01 "Machucou seu braço, ela começou a chorar"
        $ narrative_image("i02", left, None, i02, "E depois que você notou isso? O que aconteceu?") # i02 "E depois que você notou isso? O que aconteceu?"
        $ narrative_image("p01", right, None, p01, "Eu não me recordo... Lembro que fiquei furioso e apaguei") # p01 "Eu não me recordo... Lembro que fiquei furioso e apaguei"
        $ narrative_image("p01", right, None, p01, "Quando me dei conta, estava sendo imobilizado por vocês") # p01 "Quando me dei conta, estava sendo imobilizado por vocês"
        $ narrative_image("i01", left, None, i01, "É comum o senhor apagar desta forma?") # i01 "É comum o senhor apagar desta forma?"
        $ narrative_image("p01", right, None, p01, "Não, eu estava para mudar minha prescrição") # p01 "Não, eu estava para mudar minha prescrição"
        $ narrative_image("i01", left, None, i01, "Entendo, bom, acredito que terminamos por hora") # i01 "Entendo, bom, acredito que terminamos por hora"
        $ narrative_image("i02", left, None, i02, "Muito obrigado pela colaboração") # i02 "Muito obrigado pela colaboração"

        hide screen cluesUI

        scene black

        tln "17/04/2022 - 16:47h | ENTRADA DA DELEGACIA"

        # LIMPA A TELA E MOSTRA O AMBIENTE
        scene police-street
        with dissolve

        show screen cluesUI

        $ narrative_image("i02", left, None, i02, "Finalmente uma pausa") # i02 "Finalmente uma pausa"
        $ narrative_image("i01", left, None, i01, "Fazer papelada burocrática é a pior parte do nosso trabalho") # i01 "Fazer papelada burocrática é a pior parte do nosso trabalho"
        $ narrative_image("i02", left, None, i02, "Depois que houve a troca de delegado tudo parece ter piorado") # i02 "Depois que houve a troca de delegado tudo parece ter piorado"
        $ narrative_image("i01", left, None, i01, "Disseram no comunicado que é um afastamento temporário, até que termine a investigação da corregedoria") # i01 "Disseram no comunicado que é um afastamento temporário, até que termine a investigação da corregedoria"
        $ narrative_image("i01", left, None, i01, "Não acho que ele tenha feito por mal, mas a população caiu em cima") # i01 "Não acho que ele tenha feito por mal, mas a população caiu em cima"
        $ narrative_image("i02", left, None, i02, "Por causa do caso do Serial Killer?") # i02 "Por causa do caso do Serial Killer?"
        $ narrative_image("i01", left, None, i01, "Exato, talvez até alguns policiais seriam afastados") # i01 "Exato, talvez até alguns policiais seriam afastados"
        $ narrative_image("i02", left, None, i02, "O delegado puxou a responsabilidade para ele") # i02 "O delegado puxou a responsabilidade para ele"

        menu:
            "Visitar a psiquiatra?"

            "Sim":
                $ narrative_image("i01", left, None, i01, "Bom, vamos finalizar a pausa e dar uma passada na psiquiatra") # i01 "Bom, vamos finalizar a pausa e dar uma passada na psiquiatra"
                $ narrative_image("i02", left, None, i02, "Está certo, vou pegar o bloco de anotações") # i02 "Está certo, vou pegar o bloco de anotações"

                # ENTRA NOVAMENTE NO CENA 0200 AFIM DE INVESTIGAR A PSIQUIATRA
                call scene_0200(1) from _call_scene_0200_1

            "Não":
                $ narrative_image("i02", left, None, i02, "Bom, vamos voltar para a delegacia") # i02 "Bom, vamos voltar para a delegacia"
                $ narrative_image("i01", left, None, i01, "Sim, tem algumas coisas para finalizar ainda") # i01 "Sim, tem algumas coisas para finalizar ainda"

    elif caminho==1:
        hide screen cluesUI

        scene black

        tln "18/04/2022 - 09:03h | CLINICA RECEPÇÃO"

        # LIMPA A TELA E MOSTRA O AMBIENTE
        scene clinic-reception
        with dissolve

        show screen cluesUI

        $ narrative_image("i01", left, None, i01, "Bom dia Doutora [psi_nome], somos os agentes [a01_nome] e este é o [a02_nome], somos responsáveis pelo caso de um de seus pacientes") # i01 "Bom dia Doutora [psi_nome], somos os agentes [a01_nome] e este é o [a02_nome], somos responsáveis pelo caso de um de seus pacientes"
        $ narrative_image("i01", left, None, i01, "Poderia nos ajudar com algumas questões?") # i01 "Poderia nos ajudar com algumas questões?"
        $ narrative_image("psi", right, None, psi, "Somente com ordem judicial") # psi "Somente com ordem judicial"
        $ narrative_image("i02", left, None, i02, "Sem problemas, aqui está") # i02 "Sem problemas, aqui está"
        $ narrative_image("psi", right, None, psi, "Vejo que é sobre o paciente [p01_nome]") # psi "Vejo que é sobre o paciente [p01_nome]"
        $ narrative_image("psi", right, None, psi, "Entre comigo, vamos ao consultório") # psi "Entre comigo, vamos ao consultório"

        hide screen cluesUI

        scene black

        tln "18/04/2022 - 09:11h | CLINICA CONSULTÓRIO"

        # LIMPA A TELA E MOSTRA O AMBIENTE
        scene clinic
        with dissolve

        show screen cluesUI

        $ narrative_image("i01", left, None, i01, "A quanto tempo estava tratando o paciente [p01_nome]?") # i01 "A quanto tempo estava tratando o paciente [p01_nome]?"
        $ narrative_image("psi", right, None, psi, "Três meses aproximadamente") # psi "Três meses aproximadamente"
        $ narrative_image("i01", left, None, i01, "Conseguiria descrever a última sessão do [p01_nome]?") # i01 "Conseguiria descrever a última sessão do [p01_nome]?"
        $ narrative_image("psi", right, None, psi, "Claro, ele estava me descrevendo os sonhos do dia anterior") # psi "Claro, ele estava me descrevendo os sonhos do dia anterior"
        $ narrative_image("psi", right, None, psi, "É uma rotina que temos quando ele os tem") # psi "É uma rotina que temos quando ele os tem"
        $ narrative_image("i02", left, None, i02, "Poderia descrever esses sonhos?") # i02 "Poderia descrever esses sonhos?"
        $ narrative_image("psi", right, None, psi, "Na descrição que me foi passada, ele descrevia que estava impotente em não conseguir ajudar sua filha") # psi "Na descrição que me foi passada, ele descrevia que estava impotente em não conseguir ajudar sua filha"
        $ narrative_image("i01", left, None, i01, "Entendo...") # i01 "Entendo..."
        $ narrative_image("i02", left, None, i02, "") # i02 ""
        $ narrative_image("psi", right, None, psi, "Surto? O que aconteceu?") # psi "Surto? O que aconteceu?"

        if psi_001==0:
            $ narrative_image("i01", left, None, i01, "Ele começou a ficar agressivo e agrediu um homem na festa de uma amiga da filha") # i01 "Ele começou a ficar agressivo e agrediu um homem na festa de uma amiga da filha"
            $ narrative_image("i01", left, None, i01, "Só conseguiram conter a agressão depois de algum tempo") # i01 "Só conseguiram conter a agressão depois de algum tempo"
            $ narrative_image("i02", left, None, i02, "Infelizmente o homem se encontra internado, foi determinado a prisão do [paciente]") # i02 "Infelizmente o homem se encontra internado, foi determinado a prisão do [paciente]"
        else:
            $ narrative_image("i01", left, None, i01, "Ele começou a ficar agressivo e quase agrediu um homem na festa de uma amiga da filha") # i01 "Ele começou a ficar agressivo e quase agrediu um homem na festa de uma amiga da filha"
            $ narrative_image("i01", left, None, i01, "Começou a ficar agressivo após ver a filha no colo do pai da aniversariante") # i01 "Começou a ficar agressivo após ver a filha no colo do pai da aniversariante"
            $ narrative_image("i02", left, None, i02, "Por sorte o surto dele foi controlado, mas isso infligiu a determinação jurídica e ele voltará a prisão") # i02 "Por sorte o surto dele foi controlado, mas isso infligiu a determinação jurídica e ele voltará a prisão"

        $ narrative_image("psi", right, None, psi, "Nossa...") # psi "Nossa..."
        $ narrative_image("i01", left, None, i01, "E por determinação do delegado estamos aqui para entender melhor sobre o caso dele") # i01 "E por determinação do delegado estamos aqui para entender melhor sobre o caso dele"
        $ narrative_image("i02", left, None, i02, "Esse surto é incomum para quem está em tratamento, certo?") # i02 "Esse surto é incomum para quem está em tratamento, certo?"
        $ narrative_image("psi", right, None, psi, "Certo...") # psi "Certo..."
        $ narrative_image("i02", left, None, i02, "Algum medicamento poderia ter causado o surto?") # i02 "Algum medicamento poderia ter causado o surto?"
        $ narrative_image("psi", right, None, psi, "O que está querendo sugerir com isso? Que indiquei tratamento errado de propósito?") # psi "O que está querendo sugerir com isso? Que indiquei tratamento errado de propósito?"
        $ narrative_image("i02", left, None, i02, "Não se ofenda doutora, estamos apenas investigando. Poderia causar um surto?") # i02 "Não se ofenda doutora, estamos apenas investigando. Poderia causar um surto?"
        $ narrative_image("psi", right, None, psi, "Não, de forma nenhuma.") # psi "Não, de forma nenhuma."
        $ narrative_image("psi", right, None, psi, "A prescrição controla os surtos") # psi "A prescrição controla os surtos"
    return
