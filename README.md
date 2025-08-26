# 🕹️ Platformer Game (PGZero)

Um pequeno jogo estilo **Platformer** criado com [PGZero](https://pygame-zero.readthedocs.io/en/stable/), seguindo os requisitos de tutoriais e projetos para iniciantes em Python.  

O objetivo é demonstrar o uso de **sprites animados**, **inimigos patrulhando**, **menu inicial**, **sons/música de fundo** e **lógica simples de colisão**.

---

## 🚀 Requisitos
- Python **3.8+**
- [PGZero](https://pygame-zero.readthedocs.io/)
- Módulos padrão: `math`, `random`
- (Opcional) `pygame.Rect` permitido

---

## 📦 Instalação

### Windows
1. **Clone este repositório** ou baixe como `.zip`:
   ```bash
   git clone https://github.com/Wricardo81/platformer-game.git
   cd platformer-game

2. Crie e ative o ambiente virtual:

py -3 -m venv venv
venv\Scripts\activate


3. Instale o PGZero:

pip install pgzero

---

▶️ Como Rodar
Método 1: Linha de comando

Na pasta do projeto, rode:

pgzrun game.py

Método 2: Arquivo .bat (mais fácil no Windows)

Dê dois cliques em run_game.bat

Ele cria o ambiente virtual (se não existir), instala as dependências e inicia o jogo.

---

🎮 Funcionalidades

Menu inicial com botões clicáveis:

Start Game
Sound ON/OFF
Exit
Herói animado (idle + movimento)
Inimigos com patrulha em território próprio
Colisão com inimigos → reinicia fase
Sons: pulo, colisão, clique
Música de fundo em loop

---

📂 Estrutura do Projeto
platformer_game/
│── game.py            # código principal do jogo
│── run_game.bat       # script para rodar no Windows
│── README.md          # este arquivo
│── sounds/            # sons do jogo
│── images/            # sprites (herói, inimigos, cenário)


---

👨‍💻 Autor

Projeto desenvolvido por Wildson Ricardo como desafio de criação de jogo em PGZero.
