# AUTHOR: PERALTA GAMES
# SCOPE: DEFINIR E INICIALIZAR TODAS AS VARIAVEIS QUE SERAO USADAS DURANTE O JOGO QUE NAO SEJAM LOCAIS
label game_variables:
    # VARIAVEIS
    $ narrativa=-1                                                                  # ARMAZENA O VALOR DA NARRATIVA ESCOLHIDO PELO JOGADOR
    $ pais="Lisarb"
    $ estado="Oluap"
    $ cidade="Abiu Ciparac"
    $ bairro="Aierroc"
    $ jornal=[0, 0, 0, 0]                                                           # ARMAZENA O JORNAL LIDO
    $ revista=[0, 0, 0, 0]                                                          # ARMAZENA A REVISTA LIDA
    $ inventario=[0, 0, 0]
    $ item_description = 0
    $ layer_folder = 1
    $ niveis_suspeitos=["Testemunha", "Suspeito", "Vítima", "Inocente", "Culpado"]  # NIVEIS DE SUSPEITA
    $ personagens_sus=[0, 0, 0, 0, 0, 0, 0, 0]                                      # NIVEL DE SUSPEITA DE CADA PERSONAGEM DA LISTA DE PERSONAGEM VISTAS [0- TESTEMUNHA, 1- SUSPEITO, 2- VITIMA, 3- INOCENTE, 4- CULPADO]
    $ locais_visitados=[0, 0, 0, 0, 0]                                              # LOCAIS VISITADOS PELOS DETETIVES
    $ personagens_vistos=[0, 0, 0, 0, 0, 0, 0, 0]                                   # PERSONAGENS RELEVANTES PARA O INVESTIGADOR
    $ bebida="Vodka"

    # ESCOLHAS PSIQUIATRA
    $ psi_001=-1    # DECISAO: PACIENTE 01 SOBRE A FILHA DELE [PROTECAO/INDEPENDENCIA]
    $ psi_002=-1    # DECISAO:
    $ psi_003=-1    # DECISAO:
    $ psi_004=-1    # DECISAO:
    $ psi_005=-1    # DECISAO:

    # ESCOLHAS INVESTIGACAO
    $ inv_001=-1    # DECISAO:
    $ inv_002=-1    # DECISAO:
    $ inv_003=-1    # DECISAO:
    $ inv_004=-1    # DECISAO:
    $ inv_005=-1    # DECISAO:

    # NOMES
    $i01_nome="[Investigador] Vinicius"         # INVESTIGADOR 01
    $i02_nome="[Investigador] Welligton"        # INVESTIGADOR 02
    $psi_nome="[Psiquiatra] Rosana"             # PSIQUIATRA
    $p01_nome="[Paciente] Douglas"              # PACIENTE 01
    $p02_nome="[Paciente] Ricardo"              # PACIENTE 02
    $p03_nome="[Paciente] Camila"               # PACIENTE 03
    $seg_nome="[Segurança] Souza"               # SEGURANCA PREDIO PSIQUIATRA
    $rev_nome="Revista"                         # REVISTA
    $jor_nome="Jornal"                          # JORNAL
    $com_nome="Informações da Internet"         # ARTIGO DA INTERNET
    $a01_nome="[Comentário Internet] Geraldo"   # COMENTARISTA DA INTERNET 01
    $a02_nome="[Comentário Internet] Fernando"  # COMENTARISTA DA INTERNET 02
    $a03_nome="[Comentário Internet] Neide"     # COMENTARISTA DA INTERNET 03
    $bmn_nome="[Barista] Carlos"                # BARISTA
    $skr_nome="Lector"                          # SERIAL KILLER
    $adv_nome="[Advogado] Gustavo"              # ADVOGADO PACIENTE 01
    $dlg_nome="[Delegado] Flavio"               # DELEGADO
    $gar_nome="[Gari] Pedro"                    # GARI
    $atm_nome="[Recepcionista] Jessica"         # ATENDENTE MOTEL
    $acp_nome="[Modelo] Veronica"               # ACOMPANHANTE DO BAR
    $leg_nome="[Legista] Bruno"                 # LEGISTA
    $cop_nome="[Policial] Felipe"               # POLICIA, RESGATE PSIQUIATRA

    return
