Nota1 = int(input("Digite a sua nota primeiro bimestre: "));
Nota2 = int(input("Digite a sua nota segundo bimestre: "));

media = (Nota1 + Nota2) / 2;

if media >= 6:
     print("Bem vindo, você passou. Sua média é:", media);
else:
     pontosFaltantes = 6 - media;
print("Você ainda não atingiu a média. Faltam", pontosFaltantes, "pontos para passar.");






