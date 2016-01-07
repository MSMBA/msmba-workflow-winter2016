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



class OrderTakerApplication(RoleApplication):
    '''
    The OrderTakerApplication "class" is a collection of the "methods" (functions) that 
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
        super(OrderTakerApplication, self).__init__(theflowname, "Agent") 
        # Declare any tasks that this role is able to perform:
        # !!! Modify to use actual name for this task...
        self.register_source_step("Rental", self.car_order_form_creator) 

    def car_order_form_creator(self, stepname, form):
        '''
        This method does the actual work of building the user interface.
        '''
        
        # !!! improve this text...
        form.add_static_label('') 
        form.add_static_label('Enter customer request details:') 
        # !!! Add at least two fields here, along with any additional static labels you need...
        form.add_field(Type.SHORTSTRING, "Name", labeltext="Customer Name", initial="Enter customer name")
        form.add_field(Type.SHORTSTRING, "ID", labeltext="Customer ID", initial="Enter customer ID")
        form.add_field(Type.DATE, "Start", labeltext="Start Date") 
        form.add_field(Type.DATE, "End", labeltext="End Date")
        form.add_field(Type.BOOLEAN, "Insurance", labeltext="Insurance")
        form.add_field(Type.CHOICE, "TypeOfCar", labeltext="Type of car", choices=['Luxury', 'Family', 'Truck', 'Economy','Sport'], initial='Luxury');

if __name__ == '__main__':
    #starts up the OrderTakerApplication:
    app = OrderTakerApplication()
    #Start interacting with the user:
    app.MainLoop()