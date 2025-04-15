from PIL import Image, ImageDraw

# Define as coordenadas
coordenadas = [
    {"point": [779, 121]},
    {"point": [781, 278]},
    {"point": [781, 348]},
    {"point": [716, 392]},
    {"point": [716, 578]},
    {"point": [782, 578]},
    {"point": [784, 635]},
    {"point": [785, 693]},
    {"point": [788, 749]},
    {"point": [788, 809]},
    {"point": [798, 859]},
    {"point": [861, 861]},
    {"point": [861, 919]},
    {"point": [812, 923]}
]

# Carrega a imagem
imagem = Image.open("FC6_0.png") # Substitua "image.png" pelo caminho da sua imagem

# Cria um objeto ImageDraw para desenhar na imagem
desenho = ImageDraw.Draw(imagem)

# Desenha as linhas conectando as coordenadas
for i in range(len(coordenadas) - 1):
    x1, y1 = coordenadas[i]["point"]
    x2, y2 = coordenadas[i+1]["point"]
    desenho.line((x1, y1, x2, y2), fill="red", width=50)  # Desenha uma linha vermelha com espessura 2

# Salva a imagem modificada
imagem.save("imagem_desenhada.png") # Salva como um novo arquivo