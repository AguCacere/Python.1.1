from base_clases.customer_name import Name

class Customer(Name):
    def __init__(self, customer_name, month, work, id, age):
        super().__init__(customer_name)
        self.monthyl_income = month
        self.work = work
        self.id = id
        self.age = age
    def description(self):
        print(f"El cliente {self.customer_name}, con el id {self.id} y un ingreso mensual de {self.monthyl_income} pesos. ")
    def year_income(self):
        return 12* self.monthyl_income
        
    