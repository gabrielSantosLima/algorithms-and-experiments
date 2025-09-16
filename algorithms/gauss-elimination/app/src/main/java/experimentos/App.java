package experimentos;

// Experimento de Matemática Básica - Software
public class App {
    public static void main(String[] args) {
        Double[][] matriz = {
                {900d, 260d, 500d},
                {0.5, 0.9, 0.7},
                {1000d, 600d, 1000d}
        };
        MetodoGauss metodoGauss = new MetodoGauss(matriz);
        metodoGauss.solucao();
    }
}
