import getpass
def verificar_senha(senha):
  ponto = 0

  if len (senha) >= 8:
    ponto +=1

    if any(c.isupper() for c in senha) and any(c.islower() for c in senha):
        ponto +=3

    if any(c.isalnum() for c in senha):
      ponto +=2

      if any(c.isdigit() for c in senha):
         ponto +=3
    
    return ponto
  
def main():
  print("Bem vindo ao Verificador de Senha! :)")
  senha = getpass.getpass(prompt=("Digite sua senha: "))

  ponto = verificar_senha(senha)

  print("\nAnalisando a força da senha...")
  print(f"A senha \"{senha}\" recebeu a pontuação {ponto}/10.")

  if ponto >= 8:
    print("Sua senha é forte!")

  elif ponto >= 5:
    print("Sua senha e média!")

  else:
    print("Sua senha é fraca!")

  repetir = input ("Deseja verificar outra senha? (sim/não): ")
  if repetir.lower() == "sim":
          main()
  else:
    print("\nObrigada por verificar sua senha! :)")

if __name__ == "__main__":
    main()