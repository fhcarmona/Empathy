# AUTHOR: PERALTA GAMES
# SCOPE:
default caso_avaliado=-1
default relatorio_caso=""

label scene_1100:
    hide screen cluesUI

    scene black

    tln "28/05/2022 - 09:15h | GABINETE DO CHEFE DE POLÍCIA"

    # LIMPA A TELA E MOSTRA O AMBIENTE
    scene chiefs-room

    show screen cluesUI

    #
    $ narrative_image("dlg", right, None, dlg, "Bom dia senhores, amanhã teremos uma conferência para responder algumas perguntas dos repórteres e população civil.")
    $ narrative_image("dlg", right, None, dlg, "Eu farei uma apresentação com as evidências e conclusões finais.")
    $ narrative_image("dlg", right, None, dlg, "Quero que vejam as evidências e até o final desta tarde me entreguem o relatório para encerrar o caso.")

    hide screen cluesUI

    scene black

    tln "28/05/2022 - 09:37h | DELEGACIA"

    # LIMPA A TELA E MOSTRA O AMBIENTE
    scene police-station

    while caso_avaliado != 1:
        menu:
            "Ponto sem retorno. Defina as conexões dos personagem com o crime no inventário. Ao finalizar prossiga para encerrar o caso."

            "{color=#8A6D3E}-Reavaliar Caso-{/color}":
                $caso_avaliado = 0

                show screen cluesUI

                $ narrative_image("i01", left, None, i01, "Vamos reavaliar o caso")
                $ narrative_image("i02", left, None, i02, "Está certo")

                hide screen cluesUI
            "{color=#8A6D3E}-Encerrar Caso-{/color}":
                $caso_avaliado = 1

                $ narrative_image("i01", left, None, i01, "Acredito que o relatório esteja pronto")
                $ narrative_image("i02", left, None, i02, "Vamos entregar e ver como será amanhã")

                pass

    scene black

    tln "29/05/2022 - 10:30 | CONFERÊNCIA DE ENCERRAMENTO DO CASO"

    # LIMPA A TELA E MOSTRA O AMBIENTE
    scene police-conference

    $ narrative_image("dlg", right, None, dlg, "Bom dia a todos")
    $ narrative_image("dlg", right, None, dlg, "Baseado nas evidências que foram encontradas e das entrevistas de testemunhas, iremos definir o caso como encerrado")
    $ narrative_image("dlg", right, None, dlg, "O Serial Killer, conhecido como [skr_nome] agia por sadismo na busca de suas vítimas")
    $ narrative_image("dlg", right, None, dlg, "Ele foi encontrado sem vida no porão de sua casa, foram encontradas o mesmo líquido do pulmão das vítimas com um cultivo que existia em sua residência")

    # DEFINE SE A PSIQUIATRA SERA CONSIDERADA CULPADA OU VITIMA
    $ narrative_image("dlg", right, None, dlg, "A morte de [skr_nome] foi causada pela reação da Doutora [psi_nome] que se encontrava presa em seu porão.")

    if personagens_sus[6] == 4:
        $ narrative_image("dlg", right, None, dlg, "Inicialmente acreditávamos que fosse uma possível próxima vítima, porém, baseado nas evidências que conseguimos coletar.")
        $ narrative_image("dlg", right, None, dlg, "Conseguimos identificar que a [psi_nome] tinha como objetivo assassinar o [skr_nome].")
        $ narrative_image("dlg", right, None, dlg, "Um processo foi aberto e ela será indiciada por homícidio doloso.")
        $ narrative_image("dlg", right, None, dlg, "Ela atualmente se encontra no hospital, se recuperando dos ferimentos da luta.")
    else:
        $ narrative_image("dlg", right, None, dlg, "A vítima conseguiu se livrar do carcere, lutou contra o [skr_nome] e na tentativa de fugir foi atingida por um projetil")
        $ narrative_image("dlg", right, None, dlg, "Ela se encontra em estado estável no hospital da cidade.")
        $ narrative_image("dlg", right, None, dlg, "Graças a bravura da Doutora [psi_nome] e de toda a equipe da delegacia, podemos descansar novamente sabendo que o Serial Killer foi pego.")

    $ narrative_image("dlg", right, None, dlg, "Com isso encerramos o relatório final, agradecemos a presença de todos...")

    stop music fadeout 2.0

    scene black with dissolve

    centered "Caso Lector encerrado"

    play music ending volume 0.5

    $relatorio_caso = "RESULTADO GAMEPLAY:\n\n{color=#FFF7}"

    python:
        # PERCORRE A LISTA DE SUSPEITOS TENTANDO IDENTIFICAR OS ACERTOS
        for i, nivel_suspeito in enumerate(personagens_sus):
            # DEPARA DOS NOMES COM INDEX
            if i == 0:
                relatorio_caso+=acp_nome+": "
            elif i == 1:
                relatorio_caso+=atm_nome+": "
            elif i == 2:
                relatorio_caso+=bmn_nome+": "
            elif i == 3:
                relatorio_caso+=gar_nome+": "
            elif i == 4:
                relatorio_caso+=p01_nome+": "
            elif i == 5:
                relatorio_caso+=p03_nome+": "
            elif i == 6:
                relatorio_caso+=psi_nome+": "
            elif i == 7:
                relatorio_caso+=skr_nome+": "

            relatorio_caso+=niveis_suspeitos[int(personagens_sus[i])]+"\n"


    # MOSTRA O RESULTADO EM TELA
    centered "[relatorio_caso]{/color}"

    centered "ALGUM TEMPO DEPOIS"

    if personagens_sus[6] == 4:
        centered "Ao sair do hospital, Rosana foi presa por homícidio doloso e obstrução de justiça."
        centered "Baseado no testemunho de Bruno e da evidência do remédio encontrado no porão, foi possível estabelecer que Rosana foi intencionalmente ao encontro com o assassino."
        centered "\"... ela se utilizava de sua faceta de cidadã e sua empatia para manipular e agir de forma sociopata.\" - Psiquiatra Sobre Rosana"
        centered "Foi descoberto posteriormente que Rosana havia feito outras vítimas em seu passado, antes da chegada na cidade."
        centered "Após o julgamento ela foi transferida para um presídio feminino e ficará sob tratamento psiquiatrico durante todo processo."
    else:
        centered "Ao sair do hospital, Rosana foi entrevistada por diversos meios de reportagem."
        centered "Nenhuma acusação caiu sobre ela, o caso foi considerado como legítima defesa."
        centered "Anos depois lançou um livro contando mais sobre o ocorrido"

        play sound laugh
        with Pause(5)

    centered "Créditos\n\nArte\n{color=#FFF7}Daniel Claper Cundari Teixeira de Barros\nGabriel Oliveira Pereira dos Santos\nLissiane Trajano Pereira{/color}\n\nAúdio\n{color=#FFF7}Gabriel Oliveira Pereira dos Santos{/color}\n\nRoteiro\n{color=#FFF7}Fábio Henrique Carmona\nLissiane Trajano Pereira{/color}\n\nProgramação\n{color=#FFF7}Fábio Henrique Carmona{/color}\n\nQA\n{color=#FFF7}Helber Roberto dos Reis{/color}"
    centered "A equipe Peralta Games agradece por jogar!"

    return
