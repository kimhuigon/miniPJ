public class FAQ2 {
    public static void main(String[] args) {

        int x=10;
        int y=20;
        int z = (++x) + (y--);

        System.out.println(++x);
        System.out.println(y--);
        System.out.println(z);
    }
}


//+는 2개까지 증가가 가능하지만 -는 --가 있어야 하나가 낮아 진다 그러므로 z = 12 + 19이기 때문에 답은 31이다