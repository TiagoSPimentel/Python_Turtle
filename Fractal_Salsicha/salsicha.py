import turtle

janela = turtle.Screen()
t = turtle.Turtle()
t.speed(0) #velocidade
t.penup() #levanta caneta
t.goto(-370, 0) #posição inicial
t.pendown() #abaixa a centa
t.pensize(3) #espessura da caneta
cores = ["blue", "red"]
print("entre com sua ordem que desejar")
ordem = int(input("ordem: "))
tamanho = 400
angulos =  [90, -90, -90, 0, 90, 90,-90, 0] #vetor de angulas que a cobra se moverá

def salsicha_minkowski(t, ordem, tamanho, cores):
    
    if ordem == 0:
        t.forward(tamanho)
    else:
        for i in angulos: #percorre os angulos
            if tamanho == 400:
                cores.reverse() #muda a cor a quando o tamanho for igual a 400
            t.pencolor(cores[0]) #muda para a cor azul
            salsicha_minkowski(t, ordem-1, tamanho/3, cores) #chama a função recursivamente
            t.left(i) #Rotaciona o Turtle à esquerda pelo ângulo


salsicha_minkowski(t, ordem, tamanho, cores)

janela.mainloop()



