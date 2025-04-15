from PIL import Image, ImageDraw

# Carregar imagem de fundo existente
background = Image.open('FC6_0.png')  # Altere para o nome da sua imagem
draw = ImageDraw.Draw(background)

# Ler e processar o arquivo
with open('salas_M0.txt', 'r') as f:
    content = f.read().split('LIGACOES')

# Processar pontos
pontos = {}
pontos_raw = content[0].strip().split('\n')[1:]  # Assume cabeçalho nos pontos
for linha in pontos_raw:
    partes = linha.split()
    nome = partes[0]
    x = int(partes[1])
    y = int(partes[2])
    pontos[nome] = (x, y)

# Processar ligações (corrigido)
ligacoes = []
ligacoes_raw = content[1].strip().split('\n')  # SEM [1:] para não pular linha
for linha in ligacoes_raw:
    if linha.strip():  # Ignorar linhas vazias se houver
        a, b = linha.split(' - ')
        ligacoes.append((a.strip(), b.strip()))

# Função para desenhar conexões com destaque
def desenhar_conexoes():
    for a, b in ligacoes:
        if a in pontos and b in pontos:
            start = pontos[a]
            end = pontos[b]
            draw.line([start, end], fill='red', width=3)

# Desenhar e salvar
desenhar_conexoes()
background.save('mapa_com_ligacoes.png')
print('Mapa atualizado salvo como: mapa_com_ligacoes.png')