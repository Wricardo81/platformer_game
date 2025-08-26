# Platformer Game - PGZero

Um jogo simples estilo **plataforma 2D** feito em **Python + PGZero**.

## 🎮 Controles
- **Setas Esquerda/Direita**: mover o herói
- **Espaço**: pular
- **Mouse**: navegar no menu

## 📂 Estrutura
- `game.py`: código principal
- `images/`: sprites do herói, inimigos e botões (placeholders 32x32)
- `sounds/`: música (`music.wav`) e efeitos (`jump.wav`, `hit.wav`, `click.wav`)

## 🚀 Como rodar
1. Instale o PGZero:
   ```bash
   pip install pgzero
   ```
2. Rode o jogo:
   ```bash
   pgzrun game.py
   ```

## 📌 Funcionalidades
- Menu principal com botões clicáveis (Start, Sound ON/OFF, Exit).
- Música de fundo e efeitos sonoros.
- Herói e inimigos com animação de sprite (2 frames para idle/run).
- Inimigos patrulham seu território.
- Colisão com inimigos reinicia o herói.

## ✅ Requisitos atendidos
- Apenas `pgzero`, `math`, `random` e `Rect` do pygame usados.
- Sprites animados para movimento e idle.
- Sons e música com controle ON/OFF.
- Código simples, organizado e seguindo PEP8.
