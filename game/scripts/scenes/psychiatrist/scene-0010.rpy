# AUTHOR: PERALTA GAMES
# SCOPE: PORAO, ATAQUE DA PSIQUIATRA AO SERIAL KILLER

label scene_0010:
    scene black

    tln "13/05/2022 - 22:02h | PORÃO"

    # LIMPA A TELA E MOSTRA O AMBIENTE DO PORAO
    scene basement
    with dissolve

    $ narrative_image("skr", right, None, skr, "Pensei que quando abrisse a porta você estaria gritando")
    $ narrative_image("psi sad", left, None, psi, "Não darei tal prazer")
    $ narrative_image("skr", right, None, skr, "Doutora, certo? Dei uma pesquisada em você, famosa...")
    $ narrative_image("skr", right, None, skr, "Intrigante como alguém do seu porte, está tão longe de onde mora")
    $ narrative_image("psi sad", left, None, psi, "Pensei em dar uma mudada de ambiente")
    $ narrative_image("skr", right, None, skr, "Acredita mesmo que seja coincidência? Pois eu acho que...")

    scene black
    with Pause(2)

    play sound stab
    with Pause(2)

    play sound gunfire
    with Pause(1)

    $ narrative_image("psi sad", left, None, psi, "Ah, que dor")

    pause 5

    return
