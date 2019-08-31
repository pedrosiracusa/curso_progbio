import os 
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def numeroCamera(nomeCamera):
    return int(nomeCamera[3:])


def buscaRegistros( nomeCamera ):
    # parâmetro: o nome da câmera a ser buscada
    # retorna: uma lista com os nomes das espécies registradas
    camDir = './data/ctraps/'+nomeCamera
    l = []
    for reg in os.listdir(camDir):
        f=open(camDir+'/'+reg)
        sp = f.read()
        l.append(sp)
        f.close()
    return l


def criaGrid(n,m):
    # Seu código aqui
    l = []
    for i in range(n):
        l = l + [[]]
        for j in range(m):
            l[i] = l[i] + [0]
            
    return l


def camCoords(g,camNum):
    # Seu código aqui
    g_ncols= len(g[0])
    
    coord_linha = (camNum-1)//g_ncols
    coord_col = (camNum-1)%g_ncols
    
    return [ coord_linha, coord_col ]


def registraOcorrencia(grid,camNum):
    coords = camCoords(grid,camNum)
    grid[coords[0]][coords[1]] = 1


def ondeFoiRegistrado(especie):
    l = []
    for cam in os.listdir('./data/ctraps'):
        if especie in buscaRegistros(cam):
            l = l + [cam]
        
    return l


def criaMapa(especie):
    cameras = ondeFoiRegistrado(especie)
    g = criaGrid(10,10)
    for cam in cameras:
        camNum = numeroCamera(cam)
        registraOcorrencia(g,camNum)
    return g


def plotaFiguraMapa(mapa):
    cmap = ListedColormap( ((0,0,0,0),'maroon') )
    plt.figure(figsize=(10,10))

    pnb_img = plt.imread('./img/trapcams_diagram_original.png')

    plt.imshow(m,cmap=cmap, extent=[321,490,557,397])
    plt.imshow(plt.imread('./img/trapcams_diagram_original.png'), zorder=-1,extent=[0,850,667,0])

    plt.show()


if __name__ =='__main__':
    print("Olá! Vou te ajudar a plotar um mapa de ocorrência de espécies")
    while True:
        spNome = input("Qual o nome da espécie?\n")

        m = criaMapa(spNome)
        plotaFiguraMapa(m)
        
        to_continue = input("Quer gerar o mapa de outra espécie? (s/n) ")
        if to_continue not in ['s','S']:
            print("Ok, aperte [ENTER] para terminar.")
            input()
            break
