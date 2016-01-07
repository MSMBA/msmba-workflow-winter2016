'''
The Order Taker User Interface for the coffee bar workflow (Winter Intensives Lab 5)

This is where you define the fields that appear on the screen (application) the order
taker sees and tell WMP how this application (user interface) fits into the overall
workflow.

Note:  the comments here assume you have already read through the comments
in CoffeeBackend.py and made your edits there.
'''

# these next few lines import some of the WMP functions we will
# use in this file.
from frontend.roleApplication import RoleApplication
from frontend.form import Type
from CarRental.CarRentalConstants import theflowname
from datetime import datetime


class CashierApplication(RoleApplication):
    '''
    The CashierApplication "class" is a collection of the "methods" (functions) that 
    define the elements of the order taker application.  
    
    An application will always include the method __init__ and at least one
    method to define a form that the user of this application will use.
    '''

    def __init__(self):
        '''
        Declare this application to be part of a given work flow and specify its role in that workflow.
        '''
        # Declare this application to be part of a given workflow, and responsible for a given role:
        # !!! Modify the following to use the actual role name you need...
        super(CashierApplication, self).__init__(theflowname, "Cashier") 
        # Declare any tasks that this role is able to perform:
        # !!! Modify to use actual name for this task...
        self.register_transition_step("CardReceipt", self.card_info_form_creator, name_fields=["sequence", "ID", "TypeOfCar"])

    def card_info_form_creator(self, stepname, form):
        '''
        This method does the actual work of building the user interface.
        '''
        datestart = form.task.get_field("Start")
        dateend = form.task.get_field("End")
        totaldays = self.bill_charge_from_creator(datestart,dateend)
        typeofcar = form.task.get_field("TypeOfCar")
        totalfee = 0
        if(typeofcar == "Luxury ($100/day)"):
            totalfee = totaldays*100
        elif(typeofcar == "Family ($60/day)"):
            totalfee = totaldays*60
        elif(typeofcar == "Truck ($100/day)"):
            totalfee = totaldays*100
        elif(typeofcar == "Sport ($150/day)"):
            totalfee = totaldays*150
        else: #Economy
            totalfee = totaldays*40
        
        # !!! improve this text... 
        form.add_html_label("<img src='http://www.credit-card-logos.com/images/multiple_credit-card-logos-1/credit_card_logos_10.gif'>") 
        form.add_static_label('')
        form.add_static_label('You are renting a ' + form.task.get_field("TypeOfCar")+ " car for " + str(totaldays) + " days")
        form.add_static_label('Your fee is going to be: $' + str(totalfee))
        form.add_static_label('Enter Credit Card information:') 
        # !!! Add at least two fields here, along with any additional static labels you need...
        form.add_static_label('Customer Name: ' + form.task.get_field("Name"))
        form.add_field(Type.CHOICE, "Type", labeltext="Type of Card", choices=['Visa', 'Master Card', 'Amex'], initial='Visa')
        form.add_field(Type.SHORTSTRING, "CardNo", labeltext="Enter Card No")
        form.add_field(Type.SHORTSTRING, "Expiration Date", labeltext="Expiration Date", initial="MM/YY") 
        form.add_field(Type.SHORTSTRING, "CVC", labeltext="Code")
        
        
        #self.register_source_step("Fee", self.bill_charge_from_creator)
    
    
    def bill_charge_from_creator(self, datestart, dateend):
        '''
        This is something something spam spam.
        '''
        #form.add_static_label('Calculate fee')
        d1 = datetime.strptime(datestart, "%Y-%m-%d")
        d2 = datetime.strptime(dateend, "%Y-%m-%d")
        #form.add_field(Type.INTEGER, "CVC", labeltext=abs((d2-d1).days))
        return abs((d2-d1).days)


if __name__ == '__main__':
    #starts up the CashierApplication:
    app = CashierApplication()
    #Start interacting with the user:
    app.MainLoop()