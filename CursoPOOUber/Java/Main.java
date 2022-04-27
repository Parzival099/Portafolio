class Main{
    public static void main(String[] args) {
        system.out.println("Hola mundo");
        Car car = new Car("QEW234", new Account("Andres Herrera", "AND123"));
        car.passenger = 4;
        system.out.println("Car license: " + car.license);
        car.printDataCar();

        Car car2 = new Car("QWE567", new Account("Andres Herrera", "AND123"));
        car2.passenger = 3;
        system.out.println("Car license: " + car2.license);
        car2.printDataCar();
    }

}