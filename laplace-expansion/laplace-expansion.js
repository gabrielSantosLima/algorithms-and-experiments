/*
Teorema de Laplace: cálculo do determinante de uma matriz quadrada de ordem n.

1. Escolher uma das filas (linha ou coluna)
2. Somar o produto dos elementos por seus respectivos cofatores

Ex:
Seja A =|a11,a12,a13|
        |a21,a22,a23|
        |a31,a32,a33|
det(A) = a11 * A11 + a12 * A12 + a13 * A13 
sendo Aij = (-1)^(i+j) * Dij
*/

const matriz = [
  [1,2,3,4,5,6],
  [11,12,31,31,4,5],
  [1,3,55,6,3,554],
  [4,5,4,11,43,3],
  [35,5,6,8,25,3],
  [35,56,80,0,8,4],
]

function matrizCofator(matriz = [], i = 0, j = 0){
  let novaMatriz = []
  for(let linha = 0; linha < ordem(matriz); linha++){
    for(let coluna = 0; coluna < ordem(matriz); coluna++){
      if(linha !== i && coluna !== j){
        novaMatriz.push(matriz[linha][coluna])
      }
    }
  }
  let novaOrdem = Math.sqrt(novaMatriz.length) 
  return novaMatriz.reduce((lista, valorAtual, indice) => {
    if(indice % novaOrdem === 0) return lista.concat([[valorAtual]])
    else if(!lista.length) return [[lista, valorAtual]]
    const lastArray = lista.pop()
    return [...lista, lastArray.concat(valorAtual)]
  })
}

function cofator(matriz = [], i = 0, j = 0){
  return Math.pow(-1, i + j) * det(matrizCofator(matriz, i, j))
}

function ordem(matriz = []){
  return matriz.length
}

function det(matriz = []){
  if(ordem(matriz) == 0) return undefined
  if(ordem(matriz) === 1) return matrix[0][0]
  if(ordem(matriz) === 2){
    const diagonalPrincipal = matriz[0][0] * matriz[1][1]
    const diagonalSecundaria = matriz[0][1] * matriz[1][0]
    return diagonalPrincipal + diagonalSecundaria
  }
  if(ordem(matriz) === 3){
    return (matriz[0][0] * matriz[1][1] * matriz[2][2] + 
      matriz[0][1] * matriz[1][2] * matriz[2][0] + 
      matriz[0][2] * matriz[1][0] * matriz[2][1]) - 
      (matriz[0][1] * matriz[1][0] * matriz[2][2] + 
      matriz[0][0] * matriz[1][2] * matriz[2][1] + 
      matriz[0][2] * matriz[1][1] * matriz[2][0]) 
  }

  let determinante = 0
  for(let linha = 0; linha < ordem(matriz); linha++){
    const elemento = matriz[linha][0]
    const cofatorAij = cofator(matriz, linha, 0)
    determinante += elemento * cofatorAij
  }
  return determinante
}

console.log(det(matriz))