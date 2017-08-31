package busca.binaria;

public class Principal {

	public static void main(String[] args){
		
		int [] array = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19};
		
		System.out.println("Para realizar a busca binaria foram realizados " + buscaBinaria(array, 16) + " passos");

	}
	
	public static int buscaBinaria(int[] array, int valor){
	        
			int esq = 0;
	        int dir = array.length - 1;
	        int valorMeio;
	        int c = 0;
	        
	        while(esq < dir){
	                c++;
	        		valorMeio = esq + ((dir - esq)/2);
	                if (array[valorMeio] < valor){
	                        esq = valorMeio + 1;
	                        System.out.println("1");
	                } else if(array[valorMeio] > valor){
	                        dir = valorMeio - 1;
	                        System.out.println("2");
	                } else {
	                        return valorMeio;
	                }
	        }
	        return c;
	        // por que tinha o -1 como return? era um criterio de parada? para que eu poderia vir a usa-lo?
	        // nao precisa usar o -1, porque ele significa quando o inicio passa do fim (esq > dir), NUNCA ACONTECE
	}
	
}
