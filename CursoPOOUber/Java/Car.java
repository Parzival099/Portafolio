class Car {
    Integer id;
    String license;
    Account driver;
    private Integer passenger;

    public Car(String license, Account driver) {
        this.license = license;
        this.driver = driver;
    }

    boid printDataCar() {
        system.out.println("License: " + license + "Driver: " + driver.name);
    }

}