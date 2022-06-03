# AUTHOR: PERALTA GAMES
# SCOPE: CONSULTORIO, PACIENTE 03 CONTANDO SOBRE A INFANCIA

label scene_0007:
    scene black

    tln "03/07/2020 - 17:32h | CLINICA PSIQUIATRICA"

    # LIMPA A TELA E MOSTRA O AMBIENTE CONSULTORIO
    scene clinic
    with dissolve

    $ narrative_image("psi", left, None, psi, "E como era sua relação com seu primo?")
    $ narrative_image("p03", right, None, p03, "Éramos bem próximos, brincávamos muito juntos")
    $ narrative_image("psi", left, None, psi, "Algo fez mudar isso?")
    $ narrative_image("p03", right, None, p03, "Sim, durante uma brincadeira com a piscina, a gente jogou alguns produtos químicos para assustar a mãe dele")
    $ narrative_image("p03", right, None, p03, "A água começou a ficar verde após um tempo e quando estavamos brincando de pega-pega, ele acabou esbarrando em mim e caímos juntos na piscina")
    $ narrative_image("p03", right, None, p03, "Eu saí e pensei que ele havia saído, se não fosse o pai dele...")
    $ narrative_image("p03", right, None, p03, "Não sei o que teria ocorrido.")
    $ narrative_image("psi", left, None, psi, "Desde então vocês não se viram mais?")
    $ narrative_image("p03", right, None, p03, "Sim")
    $ narrative_image("psi", left, None, psi, "Você acredita que a cor verde esteja associada a esse trauma?")
    $ narrative_image("p03", right, None, p03, "Nunca tinha notado isso")
    $ narrative_image("psi", left, None, psi, "Descreva para mim os sentimentos que fica quando pensa sobre...")

    return
