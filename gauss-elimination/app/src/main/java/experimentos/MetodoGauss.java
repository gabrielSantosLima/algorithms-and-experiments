package experimentos;

import java.text.DecimalFormat;
import java.util.Arrays;
import java.util.stream.Collectors;

public class MetodoGauss {
    private Double[][] matriz;

    public MetodoGauss(Double[][] matriz){
        this.matriz = matriz;
    }

    public void solucao(){
        Double[][] matrizTriangular = matriz.clone();

        for(int diagonal = 0; diagonal < matriz.length - 1; diagonal++){
            Double pivo = matrizTriangular[diagonal][diagonal];

            for(int linha = diagonal + 1; linha < matriz.length; linha++){
                Double multiplicador = matrizTriangular[linha][diagonal] / pivo;
                matrizTriangular[linha] = diminuiLinhas(
                        matrizTriangular[linha],
                        multiplicaLinha(matrizTriangular[diagonal], multiplicador)
                );
            }
        }

        imprimeMatriz(matrizTriangular);
    }

    private Double[] multiplicaLinha(Double[] linha, Double valor){
        Double[] linhaMultiplicada = new Double[linha.length];
        for(int count = 0; count < linha.length; count++){
            linhaMultiplicada[count] = valor * linha[count];
        }
        return linhaMultiplicada;
    }

    private Double[] diminuiLinhas(Double[] linha1, Double[] linha2){
        Double[] linhaDiminuidas = new Double[linha1.length];
        for(int count = 0; count < linha1.length; count++){
            linhaDiminuidas[count] = linha1[count] - linha2[count];
        }
        return linhaDiminuidas;
    }

    private void imprimeMatriz(Double[][] matriz){
        DecimalFormat df = new DecimalFormat("0.00");
        for(int i = 0; i < matriz.length; i++){
            System.out.println(Arrays.stream(matriz[i])
                    .map(df::format)
                    .collect(Collectors.joining(",\t"))
            );
        }
    }
}
