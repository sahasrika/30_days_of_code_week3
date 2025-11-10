// Day15.java - Demonstrating Method Overriding in Java

class Vehicle {
    void start() {
        System.out.println("The vehicle is starting...");
    }
}

class Car extends Vehicle {
    @Override
    void start() {
        System.out.println("The car starts with a key ignition.");
    }
}

public class Day15 {
    public static void main(String[] args) {
        Vehicle myVehicle = new Vehicle();
        Vehicle myCar = new Car();

        myVehicle.start(); // Calls Vehicle's start()
        myCar.start();     // Calls Car's overridden start()
    }
}
