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

    # FACADA
    play sound stab
    with Pause(2)

    # TIRO
    play sound gunfire
    with Pause(3)

    $ narrative_image("psi sad", left, None, psi, "Meu abdômen...")

    scene black

    # DESMAIO
    play sound fall
    with Pause(2)

    stop music fadeout 2.0

    centered "O destino foi definido."

    play music "audio/musics/investigator.mp3"

    return
