public class Day9 {
    static class BankAccount {
        private String name;
        private double balance;

        public BankAccount(String name, double balance) {
            this.name = name;
            this.balance = balance;
        }

        public void deposit(double amount) {
            balance += amount;
        }

        public void withdraw(double amount) {
            if (amount <= balance)
                balance -= amount;
            else
                System.out.println("Insufficient balance!");
        }

        public void display() {
            System.out.println("Account: " + name + " | Balance: ₹" + balance);
        }
    }

    public static void main(String[] args) {
        BankAccount acc = new BankAccount("Sahasrika", 1000);
        acc.deposit(500);
        acc.withdraw(300);
        acc.display();
    }
}
