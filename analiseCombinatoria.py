def fatorial(numero):
  if (numero-1)>0:
    return numero*fatorial(numero-1)
  else:
    return numero
  
def permutacao(permuta, *args):
  dividendo = fatorial(permuta)
  divisor = 1
  if len(args)>0:
    for y in args:
      divisor *= fatorial(y)
  return dividendo/divisor
 
def arranjo(permuta, tamanho, rep=False):
  if rep:
    return permuta**tamanho
  else:
    return fatorial(permuta)/fatorial(permuta-tamanho)
  
def combinacao(permuta, tamanho, rep =False):
  if rep:
    return fatorial(permuta+tamanho-1)/(fatorial(tamanho)*fatorial(permuta-1))
  else:
    return fatorial(permuta)/(fatorial(tamanho)*fatorial(permuta-tamanho))