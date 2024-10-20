public class Main {
  public static double zapolnenie(double x, int z){ // метод для заполнения масива z1
	return switch (z) { //заполнение массива z1 в зависимости от значений массива z
	  case 5 -> Math.asin(Math.pow((x + 0.5) / 9, 2));
	  case 4,7,11,13,15,16,18 -> Math.tan(Math.tan(Math.sin(x)));
	  default -> Math.exp(Math.cbrt(Math.tan((x + 1) / 2)));
	};
  }
  public static void vivod(double[][] z1){ // метод для вывода масива z1
      for (int i = 0; i < 15; i++) {
			System.out.print("|"); // разделитель перед первым числом в строке
            for (int j = 0; j < 20; j++) {
                System.out.format("%9.5f",z1[i][j]); // вывод числа с точ. до 5 знаков после запятой + длина не менее 9 символов для красоты.
                System.out.print("|"); // разделитель между числами
            }
      System.out.println(); // перевод на новую строку.
        }
  }
  
    public static void main(String[] args) {
        int[] z = new int[15]; // создаем масив z с типом эл. int т.к. его мы заполним числами от 4 до 18
        double[] x = new double[20]; // создаем масив x с типом эл. double
        double[][] z1 = new double[15][20]; // создаем масив z1 с типом эл. double
        for (int i = 4; i <= 18; i++) { // заполнение массива z
            z[i - 4] = i;
        }

        for (int i = 0; i < 20; i++) { // заполнение массива x
            x[i] = Math.random() * 9 - 4;
        }
    
        for (int i = 0; i < 15; i++) { // заполнение массива z1 c помощью метода zapolnenie
            for (int j = 0; j < 20; j++) {
        z1[i][j] = zapolnenie(x[j],z[i]);
      }
    }
    vivod(z1); // вывод массива z1 c помощью метода vivod
    }
}
