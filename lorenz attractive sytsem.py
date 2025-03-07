import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib
matplotlib.use('TkAgg')  # Ou tente 'Qt5Agg'


#função que define o sistema de Lorenz
def lorenz(t, state, sigma, rho, beta):
    x, y, z = state
    dx_dt=sigma*(y-x)
    dy_dt=x*(rho-z) - y
    dz_dt=x*y-beta*z
    return [dx_dt, dy_dt, dz_dt]

#parametros
sigma = 10.0
rho = 28.0
beta = 8.0/3.0

#condições iniciais
initial_state = [1.0, 1.0, 1.0]

#intervalo de tempo e resolução
t_span = (0, 50) #de 0 a 50 segundos
t_eval = np.linspace(t_span[0], t_span[1], 10000) #10.000 pontos de amostragem

#resolver as equações diferenciais
solution = solve_ivp(
    lorenz,
    t_span,
    initial_state,
    t_eval=t_eval,
    args=(sigma, rho, beta)
)
#extrair as soluções
x, y, z = solution.y

#criar figura para animação
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(projection='3d')
ax.set_title('Lorenz attractor - Animation')
ax.set_xlim([np.min(x), np.max(x)])
ax.set_ylim([np.min(y), np.max(y)])
ax.set_zlim([np.min(z), np.max(z)])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

#linha para a tragetória
line, = ax.plot([], [], [], lw=2)
# Alterar a cor de fundo da figura (fundo geral) e eixo (grade)
fig.patch.set_facecolor('black')  # Fundo externo da figura para preto
ax.set_facecolor('black')  # Fundo da área de plotagem (grade) para preto

# Ajustar as cores dos ticks, rótulos e título
ax.tick_params(colors='white')  # Cor dos números/ticks dos eixos
ax.set_title("Lorenz Attractor - Animation", color='white')  # Título em branco
ax.set_xlabel("X", color='white')  # Rótulo do eixo X em branco
ax.set_ylabel("Y", color='white')  # Rótulo do eixo Y em branco
ax.set_zlabel("Z", color='white')  # Rótulo do eixo Z em branco

# Trajetória com uma cor que contrasta bem com o fundo preto
line, = ax.plot([], [], [], lw=1, color='cyan')  # Linha da trajetória em ciano


# Função de inicialização
def init():
    line.set_data([], [])
    line.set_3d_properties([])
    return line,


# Função de atualização do frame
def update(frame):
    line.set_data(x[:frame], y[:frame])
    line.set_3d_properties(z[:frame])
    return line,


# Criar a animação com maior velocidade (reduzir o intervalo para mais rápido)
ani = FuncAnimation(
    fig, update, frames=len(x), init_func=init, interval=1, blit=True  # Velocidade máxima
)

# Exibir a animação
plt.show()
#função de inicializar a animação
def init():
    line.set_data([], [])
    line.set_3d_properties([])
    return line,

#função para atualizar animação
def update(frame):
    line.set_data(x[:frame], y[:frame])
    line.set_3d_properties(z[:frame])
    return line,

# Criar a animação
ani = FuncAnimation(fig, update, frames=len(x), init_func=init, interval=1, blit=True)


# Exibir a animação
plt.show()# Alterar a cor de fundo da figura e do eixo
fig.patch.set_facecolor('black')  # Fundo da figura para preto
ax.set_facecolor('black')  # Fundo da área de plotagem para preto (eixo)

# Alterar as cores dos ticks, título e rótulos para melhorar a visibilidade
ax.tick_params(colors='white')  # Cor dos ticks
ax.set_title("Lorenz Attractor - Animation", color='white')  # Cor do título
ax.set_xlabel("X", color='white')  # Cor do rótulo X
ax.set_ylabel("Y", color='white')  # Cor do rótulo Y
ax.set_zlabel("Z", color='white')  # Cor do rótulo Z

# Linha para a trajetória na cor desejada
line, = ax.plot([], [], [], lw=0.5, color='cyan')  # Linha em ciano# Alterar a cor de fundo da figura (janela principal) e eixo (área de plotagem)
fig.patch.set_facecolor('black')  # Altera a cor de fundo do contorno da figura
ax.set_facecolor('black')  # Altera o fundo da área de plotagem (grade)

# Alterar as cores dos ticks, rótulos e título para branco para ter contraste
ax.tick_params(colors='white')  # Cor dos ticks (valores nos eixos X, Y e Z)
ax.set_title("Lorenz Attractor - Animation", color='white')  # Cor do título
ax.set_xlabel("X", color='white')  # Cor do rótulo do eixo X
ax.set_ylabel("Y", color='white')  # Cor do rótulo do eixo Y
ax.set_zlabel("Z", color='white')  # Cor do rótulo do eixo Z

# Atualizar a cor da linha para algo visível sobre o fundo preto
line, = ax.plot([], [], [], lw=2, color='cyan')  # Linha azul clara para contraste

# Criar a animação
ani = FuncAnimation(
    fig, update, frames=len(x), init_func=init, interval=10, blit=True
)

# Exibir a animação
plt.show()# Alterar a cor de fundo da figura (janela principal) e eixo (área de plotagem)
fig.patch.set_facecolor('black')  # Altera a cor de fundo do contorno da figura
ax.set_facecolor('black')  # Altera o fundo da área de plotagem (grade)

# Alterar as cores dos ticks, rótulos e título para branco para ter contraste
ax.tick_params(colors='white')  # Cor dos ticks (valores nos eixos X, Y e Z)
ax.set_title("Lorenz Attractor - Animation", color='white')  # Cor do título
ax.set_xlabel("X", color='white')  # Cor do rótulo do eixo X
ax.set_ylabel("Y", color='white')  # Cor do rótulo do eixo Y
ax.set_zlabel("Z", color='white')  # Cor do rótulo do eixo Z

# Atualizar a cor da linha para algo visível sobre o fundo preto
line, = ax.plot([], [], [], lw=2, color='cyan')  # Linha azul clara para contraste

# Criar a animação
ani = FuncAnimation(
    fig, update, frames=len(x), init_func=init, interval=10, blit=True
)

# Exibir a animação
plt.show()# Alterar a cor de fundo da figura (janela principal) e eixo (área de plotagem)
fig.patch.set_facecolor('black')  # Altera a cor de fundo do contorno da figura
ax.set_facecolor('black')  # Altera o fundo da área de plotagem (grade)

# Alterar as cores dos ticks, rótulos e título para branco para ter contraste
ax.tick_params(colors='white')  # Cor dos ticks (valores nos eixos X, Y e Z)
ax.set_title("Lorenz Attractor - Animation", color='white')  # Cor do título
ax.set_xlabel("X", color='white')  # Cor do rótulo do eixo X
ax.set_ylabel("Y", color='white')  # Cor do rótulo do eixo Y
ax.set_zlabel("Z", color='white')  # Cor do rótulo do eixo Z

# Atualizar a cor da linha para algo visível sobre o fundo preto
line, = ax.plot([], [], [], lw=2, color='cyan')  # Linha azul clara para contraste

# Criar a animação
ani = FuncAnimation(
    fig, update, frames=len(x), init_func=init, interval=10, blit=True
)

# Exibir a animação
plt.show()

# Alterar as cores dos ticks para branco
ax.tick_params(colors='white')

# Alterar o título e as cores do texto
ax.set_title("Lorenz Attractor - Animation", color='white')
ax.set_xlim([np.min(x), np.max(x)])
ax.set_ylim([np.min(y), np.max(y)])
ax.set_zlim([np.min(z), np.max(z)])
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Linha para a trajetória
line, = ax.plot([], [], [], lw=0.5, color='cyan')  # Linha na cor ciano

# Função para inicializar a animação
def init():
    line.set_data([], [])
    line.set_3d_properties([])
    return line,

# Função para atualizar a animação
def update(frame):
    line.set_data(x[:frame], y[:frame])
    line.set_3d_properties(z[:frame])
    return line,

# Criar a animação
ani = FuncAnimation(
    fig, update, frames=len(x), init_func=init, interval=5  # Intervalo rápido
)

# Exibir a animação
plt.show()


