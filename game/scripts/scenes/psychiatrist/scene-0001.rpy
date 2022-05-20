# AUTHOR: PERALTA GAMES
# SCOPE: DESENVOLVER A PRIMEIRA SESSAO DA PSIQUIATRA

label scene_0001:
    scene black

    tln "10/04/2022 - 14:43h | CONSULTÓRIO PSIQUIATRA"

    # LIMPA A TELA E MOSTRA O AMBIENTE CONSULTORIO
    scene clinic

    play music "audio/musics/psychiatrist.mp3"

    # TUTORIAL
    psi "Bom dia [p01_nome], como estamos hoje?"
    p01 "Seguindo doutora"
    psi "Conseguiu seguir as recomendações da última sessão?"
    p01 "Sim doutora, só não sei o quanto escrever o que penso pode me ajudar..."
    psi "Fique tranquilo [p01_nome], o importante é você seguir a risca as minhas orientações"
    psi "Vamos continuar, como estão suas noites?"
    p01 "Minhas noites?"
    p01 "Continuo a ter os mesmos sonhos"
    psi "Continua? Consegue descrevê-los?"
    p01 "Hm... Está certo"
    p01 "Havia um homem... ele estava... mexendo com minha filha..."
    psi "Entendo, esse homem, ele estava causando algum mal a ela?"
    p01 "Não sei dizer doutora, os sonhos são confusos, mas lembro que corri em direção a ele e derrepente, tudo ficou preto."
    p01 "Quando me dei conta, ela estava sangrando, nos meus braços..."
    p01 "Sangrando doutora, você pode acreditar? Meu coração se despedaça só de pensar no sofrimento da minha filha"
    psi "Entendo..."
    psi "O sonho, mesmo que ruim, é o resultado das conexões que fazemos do que retiramos no dia-a-dia"
    p01 "Tenho muito medo do que pode acontecer com ela"

    menu:
        "Proteção":
            $psi_001=0
            psi "É importante você estar lá por ela, você é um bom pai, só deseja ela bem"
            p01 "Exato doutora, tudo que faço é por ela."

        "Indepedência":
            $psi_001=1
            psi "Sua filha está crescendo, você precisa entender que a independência faz parte do processo"
            psi "É importante acompanhar o crescimento de perto, mas o seu medo pode causar sofrimento para sua filha"
            p01 "Entendo doutora, você tem razão"

        "[p01_nome] lembrará dessas palavras"

    return
