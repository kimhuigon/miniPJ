public class Bus{

    int nowPeople;
    int busNo;

    int maxPeople = 30;
    static String status = "driving";
    static String status1 = "Pit in";
    int price = 1000;
    int fuel = 100;

    public static void main(String[] args) {
        // 버스 2대 생성
//         **Bus** - 2대 생성
//         **출력 Bus**
//         각 Bus 번호 다른지 확인
        Bus bus1 = new Bus();
        bus1.busNo = 1;
        Bus bus2 = new Bus();
        bus2.busNo = 2;

        //각 버스 번호 다른지 확인
        System.out.println(bus1.busNo);
        System.out.println(bus2.busNo);
        System.out.println(bus1.busNo == bus2.busNo);

        //
        Bus newBus = new Bus();
        //승객 두명 태움
        int nowPeople = newBus.nowPeople = 2;
        // 승객이 두 명 타서 최대 좌석에서 탄 승객 수 만큼 빼줌
        int buPeople = newBus.maxPeople - nowPeople;
        int price = newBus.price * nowPeople;
        System.out.println("출력");
        System.out.println("1. 탑승 승객 수 " + nowPeople);
        System.out.println("2. 잔여 승객수 " + buPeople );
        System.out.println("3. 요금 확인 " + price);
        // 기름 떨어짐
        int nowfuel = 100;

        int lastfuel = nowfuel -50;
        System.out.println("현재 기름 량 " + lastfuel);

        // 행선지
        System.out.println(status1);
        // 기름 패움
        int addfuel = lastfuel +10;
        System.out.println("현제 연료량 " + addfuel);
        // 행선지 변경
        System.out.println(status);
        // 승객 45명 추가 - 거부
        int addpeople = 45;
        int buPeople2 = buPeople - addpeople;
        System.out.println("정원 초과. 탑승 거부" + buPeople2);
        // 다음 승객
        int addpeople1 = 5;
        int nowpeople1 = newBus.maxPeople - addpeople1;
        int price1 = newBus.price * nowpeople1;
        System.out.println("출력");
        System.out.println("1. 탑승 승객 수 " + addpeople1);
        System.out.println("2. 잔여 승객수 " + nowpeople1 );
        System.out.println("3. 요금 확인 " + price1);
        // 기름 떨어짐
        System.out.println("기름량 -55");
        int nowfuel1 = addfuel -55;
        System.out.println("기름량 " + nowfuel1);
        System.out.println("차고지행");
        System.out.println("주유필요" + nowfuel1);
    }

}
