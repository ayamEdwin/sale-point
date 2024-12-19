import uuid
from datetime import datetime

class SalesTransactions:
    def __init__(self,  transaction_id, date, product_id, quantity_sold, total_amount, salesperson_id):
        self.transaction_id = transaction_id
        self.date = date
        self.product_id = product_id
        self.quantity_sold = quantity_sold
        self.total_amount = total_amount
        self.salesperson_id = salesperson_id

    # transaction id generator using the UUID module, truncated to a length of 8
    transaction_id = str(uuid.uuid4()).replace("-", "")[:12]

    #current date
    date = datetime.now()

    # random id generator using the UUID module, truncated to a length of 8
    product_id = str(uuid.uuid4()).replace("-", "")[:8]

    quantity_sold = 0
    total_amount = 0

    # salesperson id generator using the UUID module, truncated to a length of 8
    salesperson_id = str(uuid.uuid4())

    def recordSale():
        pass

print(SalesTransactions.product_id)
print(SalesTransactions.date)
print(SalesTransactions.transaction_id)
print(SalesTransactions.salesperson_id)