#8. Conversão de tempo
#Peça um valor em horas e mostre: minutos e segundos
print("Digite a hora que te mostrarei em minutos e segundos. ")
hora_digitada =  int(input("Digite a hora : "))
#A variável de minutos receberá valor da hora digitada multiplicado pela quantidade de minutos que tem em 1 hora=60 minutos
minutos=hora_digitada*60
#A variável de segundos receberá valor da hora digitada multiplicado pela quantidade de segundos que tem em 1 hora=3600segundos
segundos=hora_digitada*3600 
#Exibe os resultados formatados
print("Minutos:", minutos)
print("Segundos:", segundos)


