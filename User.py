# 1. Create a file with the User class, including the __init__ and make_deposit methods
class User: 

    def __init__( self, fN, lN ):
        # Attributes
        self.firstName = fN
        self.lastName = lN
        self.balance = 0


    def make_deposit( self, balance ):
        self.balance += balance
   

# 2. Add a make_withdrawal method to the User class
    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print( "We cannot process your withdrawal." )
            print( f"You currently have {self.balance}." )
            print( f"And you are trying to withdraw {amount}." )


# 3. Add a display_user_balance method to the User class
    def display_user_balance( self ):
        print(f"User: {self.firstName}  {self.lastName}, Balance: {self.balance}")

# BONUS: Add a transfer_money method (method's definition)
    def validateFunds(self, amount):
        if self.balance > amount:
            return True
        else:
            return False

    def transfer( self, user, amountToTransfer ):
        if self.validateFunds( amountToTransfer ):
            self.withdrawal( amountToTransfer )
            user.make_deposit( amountToTransfer )
        else:
            print( "You don't have enough funds to transfer." )

# 4.   Create 3 instances of the User class
jose = User( "Jose", "Rodriguez" )
keilor = User("Keilor", "Rodriguez")
natalia = User("Natalia", "Castillo")

jose.display_user_balance()
keilor.display_user_balance()
natalia.display_user_balance()

# 5. Have the first user make 3 deposits and 1 withdrawal and then display their balance
jose.make_deposit( 1000 )
jose.make_deposit( 1000 )
jose.make_deposit( 1000 )

jose.withdrawal( 2000 )

jose.display_user_balance()

# 6. Have the second user make 2 deposits and 2 withdrawals and then display their balance
keilor.make_deposit( 1000 )
keilor.make_deposit( 1000 )

keilor.withdrawal( 1500 )
keilor.withdrawal( 500 )

keilor.display_user_balance()

# 7. Have the third user make 1 deposits and 3 withdrawals and then display their balance
natalia.make_deposit( 8500 )

natalia.withdrawal( 5000 )
natalia.withdrawal( 500 )
natalia.withdrawal( 1500 )

natalia.display_user_balance()


# BONUS: Have the first user transfer money to the third user 
# and then print both users' balances

jose.transfer(natalia, 500)

jose.display_user_balance()
natalia.display_user_balance()

