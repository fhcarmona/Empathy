# AUTHOR: PERALTA GAMES
# SCOPE: PORAO, ATAQUE DA PSIQUIATRA AO SERIAL KILLER

label scene_0010:
    # LIMPA A TELA E MOSTRA O AMBIENTE DO PORAO
    scene basement
    with dissolve

    skr "Pensei que quando abrisse a porta você estaria gritando"
    psi "Não darei tal prazer"
    skr "Doutora, certo? Dei uma pesquisada em você, famosa..."
    skr "Intrigante como alguém do seu porte, está tão longe de onde mora"
    psi "Pensei em dar uma mudada de ambiente"
    skr "Acredita mesmo que seja coincidência? Pois eu acho que..."

    scene black
    with Pause(2)

    play sound stab
    with Pause(2)

    play sound gunfire
    with Pause(1)

    psi "Ah, que dor"

    pause 5

    return
