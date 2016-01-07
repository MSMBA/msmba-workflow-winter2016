'''
The LS User Interface for the coffee bar workflow (Winter Intensives Lab 5)

This is where you define the fields that appear on the screen (application) the LS
sees and tell WMP how this application (user interface) fits into the overall workflow.

Note:  the comments here assume you have already read through the comments
in CoffeeBackend.py and OrderTakerApplication.py and made your edits there.
'''

from frontend.roleApplication import RoleApplication
from frontend.form import Type
from CarRental.CarRentalConstants import theflowname

class LSApplication(RoleApplication):
    '''
    The LSApplication "class" is a collection of the "methods" (functions) that 
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
        super(LSApplication, self).__init__(theflowname, "LS") 
        
        # Declare any tasks that this role is able to perform:
        # !!! Modify to use actual task name and name_fields:
        self.register_sink_step("ConfirmedRental", self.verify_id_form_creator, name_fields=["sequence", "ID", "TypeOfCar"])


    def verify_id_form_creator(self, stepname, form):
        '''
        Defines the data entry form for the LS application.
        This form appears once the LS selects one of the pending orders from a list.
        '''
        # !!! Use one or more fields from order to define label...
        form.add_static_label('Customer Name: ' + form.task.get_field("Name"))
        form.add_static_label('Customer ID: ' + form.task.get_field("ID"))
        form.add_static_label('Type of car: ' + form.task.get_field("TypeOfCar"))
        
        # !!! Add any static labels or fields you want to include in this form...
        form.add_field(Type.BOOLEAN, "Verify", labeltext="ID verified?")

if __name__ == '__main__':
    #starts up the LSApplication:
    app = LSApplication()
    #Start interacting with the user:
    app.MainLoop()