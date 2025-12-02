# 🚀 Math Blaster: Dog vs Meteors

Um jogo educativo estilo "TuxMath" desenvolvido em Python. O jogador controla uma nave (pilotada por um cão) e deve destruir meteoros resolvendo operações matemáticas antes que eles atinjam a Terra.

## 📋 Pré-requisitos

Para rodar este projeto, você precisa ter instalado:
* **Python 3.x** (Recomendado 3.10 ou superior)
* **Biblioteca Pygame CE** (Community Edition)

## 🛠️ Instalação

Abra seu terminal na pasta do jogo e execute:

```# 🚀 Math Blaster: Dog vs Meteors

Um jogo educativo estilo "TuxMath" desenvolvido em Python. O jogador controla uma nave (pilotada por um cão) e deve destruir meteoros resolvendo operações matemáticas antes que eles atinjam a Terra.

---

## 📋 Pré-requisitos

Para rodar este projeto, você precisa ter instalado:
1.  **Python 3.x** (Recomendado 3.10 ou superior)
2.  **Biblioteca Pygame CE** (Community Edition)

## 🛠️ Instalação Rápida

Abra seu terminal na pasta do jogo e execute o comando abaixo para instalar a biblioteca gráfica necessária (isso corrige erros comuns de instalação):

```bash
pip install pygame-ce
(Nota: Se o comando pip não funcionar, tente python -m pip install pygame-ce)

🎮 Como Jogar
Iniciar o Jogo: No terminal, digite:

Bash

python math_blaster.py
Objetivo: Destruir os meteoros resolvendo a conta matemática que aparece neles.

Controles:

Teclado Numérico: Digite o resultado da conta.

ENTER: Dispara o tiro. Se acertar o resultado, o meteoro explode.

BACKSPACE: Apaga o número se você errar a digitação.

Regras:

Acerto: +10 Pontos.

Erro de digitação: Nada acontece (apenas apague e tente de novo).

Meteoro caiu: -1 Vida.

Game Over: Quando suas 3 vidas acabarem.

🧪 Testes de Software (QA)
Este projeto segue boas práticas de engenharia e contém testes automatizados para validar a matemática e as regras do jogo.

Para rodar os testes, execute:

Bash

python test_math_blaster.py
Resultado esperado: Uma mensagem OK indicando que a lógica de pontuação e geração de perguntas está funcionando corretamente.

🎨 Personalização (Imagens)
O jogo roda nativamente com gráficos gerados por código (para facilitar o teste sem baixar arquivos). Se quiser usar imagens reais:

Salve seus arquivos (ex: nave.png, meteoro.png) na mesma pasta do script.

Abra o arquivo math_blaster.py.

Procure a seção --- CARREGAMENTO/CRIAÇÃO DE IMAGENS ---.

Substitua pygame.Surface(...) por pygame.image.load('nome_do_arquivo.png').

Arquivos do Projeto:

math_blaster.py (O Jogo)

test_math_blaster.py (O Teste)

README.md (Este arquivo)
pip install pygame-ce

