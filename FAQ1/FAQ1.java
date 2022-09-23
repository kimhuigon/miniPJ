public class FAQ1 {
    public static void main(String[] args) {
        int var1=5;
        int var2=2;
        double var3=var1%var2;
        System.out.println(var3);

        int var4=(int)(var3*var1);
        System.out.println(var4);
    }
}


//var3의 값은 1이 필요하다 그래서 /로 단순히 나누는 것이 아니라 %를 이용하여 나머지를 구해주고 var4에서 var3 * var1은 1 * 5 = 5가 되므로
//
//var3 부분을 %로 바꿔야한다