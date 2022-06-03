# AUTHOR: PERALTA GAMES
# SCOPE: INTRODUCAO DA PSIQUIATRA

label scene_0001:
    scene black

    tln "10/04/2022 - 14:43h | CONSULTÓRIO PSIQUIATRA"

    # LIMPA A TELA E MOSTRA O AMBIENTE CONSULTORIO
    scene clinic

    play music "audio/musics/psychiatrist.mp3"

    # TUTORIAL
    $ narrative_image("psi", left, None, psi, "Bom dia [p01_nome], como estamos hoje?")
    $ narrative_image("p01", right, None, p01, "Seguindo doutora")
    $ narrative_image("psi", left, None, psi, "Conseguiu seguir as recomendações da última sessão?")
    $ narrative_image("p01", right, None, p01, "Sim doutora, só não sei o quanto escrever o que penso pode me ajudar...")
    $ narrative_image("psi", left, None, psi, "Fique tranquilo [p01_nome], o importante é você seguir a risca as minhas orientações")
    $ narrative_image("psi", left, None, psi, "Vamos continuar, como estão suas noites?")
    $ narrative_image("p01", right, None, p01, "Minhas noites?")
    $ narrative_image("p01", right, None, p01, "Continuo a ter os mesmos sonhos")
    $ narrative_image("psi", left, None, psi, "Continua? Consegue descrevê-los?")
    $ narrative_image("p01", right, None, p01, "Hm... Está certo")
    $ narrative_image("p01", right, None, p01, "Havia um homem... ele estava... mexendo com minha filha...")
    $ narrative_image("psi", left, None, psi, "Entendo, esse homem, ele estava causando algum mal a ela?")
    $ narrative_image("p01", right, None, p01, "Não sei dizer doutora, os sonhos são confusos, mas lembro que corri em direção a ele e de repente, tudo ficou preto.")
    $ narrative_image("p01", right, None, p01, "Quando me dei conta, ela estava sangrando, nos meus braços...")
    $ narrative_image("p01", right, None, p01, "Sangrando doutora, você pode acreditar? Meu coração se despedaça só de pensar no sofrimento da minha filha")
    $ narrative_image("psi", left, None, psi, "Entendo...")
    $ narrative_image("psi", left, None, psi, "O sonho, mesmo que ruim, é o resultado das conexões que fazemos do que retiramos no dia-a-dia")
    $ narrative_image("p01", right, None, p01, "Tenho muito medo do que pode acontecer com ela")

    menu:
        "Proteção":
            $psi_001=0
            $ narrative_image("psi", left, None, psi, "É importante você estar lá por ela, você é um bom pai, só deseja ela bem")
            $ narrative_image("p01", right, None, p01, "Exato doutora, tudo que faço é por ela.")

        "Indepedência":
            $psi_001=1
            $ narrative_image("psi", left, None, psi, "Sua filha está crescendo, você precisa entender que a independência faz parte do processo")
            $ narrative_image("psi", left, None, psi, "É importante acompanhar o crescimento de perto, mas o seu medo pode causar sofrimento para sua filha")
            $ narrative_image("p01", right, None, p01, "Entendo doutora, você tem razão")

        "[p01_nome] lembrará dessas palavras"

    return
