/* implement the BankAccount class here */
class BankAccount{
    constructor(name,balance){
        this.name = name;
        this.balance = balance;

    }
    deposit(amount){
        this.balance += amount;
    };
    withdraw(amount){
        if (amount > this.balance){
            alert("You can not withdraw more than you have")
        }
        else{
            this.balance -= amount;
        }
        
    };
}