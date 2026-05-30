import java.util.Scanner;

public class SimpleATM {

    public static void main(String[] args) {
        // Predefined PIN and initial balance
        final int PIN = 1234;
        int balance = 1000;
        Scanner scanner = new Scanner(System.in);

        // User authentication
        System.out.print("Enter PIN: ");
        int enteredPin = scanner.nextInt();

        if (enteredPin == PIN) {
            boolean exit = false;
            while (!exit) {
                // Display main menu
                System.out.println("\nATM Main Menu:");
                System.out.println("1. Check Balance");
                System.out.println("2. Deposit Money");
                System.out.println("3. Withdraw Money");
                System.out.println("4. Exit");
                System.out.print("Choose an option: ");
                int choice = scanner.nextInt();

                switch (choice) {
                    case 1:
                        // Check Balance
                        System.out.println("Your balance is: $" + balance);
                        break;
                    case 2:
                        // Deposit Money
                        System.out.print("Enter amount to deposit: ");
                        int deposit = scanner.nextInt();
                        if (deposit > 0) {
                            balance += deposit;
                            System.out.println("Amount deposited successfully. New balance: $" + balance);
                        } else {
                            System.out.println("Invalid amount. Please enter a positive number.");
                        }
                        break;
                    case 3:
                        // Withdraw Money
                        System.out.print("Enter amount to withdraw: ");
                        int withdraw = scanner.nextInt();
                        if (withdraw > 0) {
                            if (withdraw <= balance) {
                                balance -= withdraw;
                                System.out.println("Amount withdrawn successfully. New balance: $" + balance);
                            } else {
                                System.out.println("Insufficient balance.");
                            }
                        } else {
                            System.out.println("Invalid amount. Please enter a positive number.");
                        }
                        break;
                    case 4:
                        // Exit
                        System.out.print(Are you sure you want to exit?: ");
                        scanner.nextLine(); // consume newline
                        String response = scanner.nextLine();
                        if (response.equalsIgnoreCase("no")) {
                            exit = true;
                            System.out.println("Thank you for using the ATM. Goodbye!");
                        } else {
                            System.out.println("Returning to main menu.");
                        }
                        break;
                    default:
                        // Handle invalid choices
                        System.out.println("Invalid choice. Please try again.");
                }
            }
        } else {
            System.out.println("Incorrect PIN. Access denied.");
        }
        scanner.close();
    }
}
