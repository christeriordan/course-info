/* implement the BankAccount class here */
class BankAccount{
    constructor(name,balance){
        this.name = name;
        this.balance = balance;
        
        this.log = []
        
        

    }
    deposit(amount){
        let transaction = "deposit"
        let old_balance = this.balance;
        this.balance += amount;
        this.log.push(
            {transaction: transaction,
            name: this.name,
            date: new Date(),
            amount: amount,
            old_balance: old_balance,
            new_balance: this.balance,
            success: 1
            });
    };
    withdraw(amount){
        let old_balance = this.balance;
        let success = 0;
        let transaction = "withdraw"
        if (amount > this.balance){
            alert("You can not withdraw more than you have")
        }
        else{
            this.balance -= amount;
            success = 1;
        }
        this.log.push({
            transaction: transaction,
            name: this.name,
            date: new Date(),
            amount: amount,
            old_balance: old_balance,
            new_balance: this.balance,
            success: success

        });
        
    };
    printLog() {
        for (let i = 0; i < this.log.length; i++){
            console.log(this.log[i].date + 
                "\t" + this.log[i].transaction +
                "\t" + this.log[i].amount +
                "\t" + this.log[i].success +
                "\t" + this.log[i].old_balance +
                "\t" + this.log[i].new_balance)
        }
    }
    printTable(){
        document.write("<table><thead><tr>"
            + "<th>Date<th>"
            + "<th>Transaction<th>"
            + "<th>Amount<th>"
            + "<th>New Balance<th>"
            + "<th>Old Balance<th>"
            + "</tr></thead>");
        for (let i = 0; i < this.log.length; i++) {
            document.write("<tr class=\"success" + this.log[i].success + "\"><td>" + this.log[i].date + "</td>"
            + "<td>" + this.log[i].transaction + "</td>"
            + "<td>" + this.log[i].amount + "</td>"
            + "<td>" + this.log[i].old_balance + "</td>"
            + "<td>" + this.log[i].new_balance + "</td></tr>");
        }
        document.write("</table>");
    }
}