# getting data from a text box
from pyscript import display, document

def get_name(e):
    document.getElementById('div1').innerHTML = ' '
    varsity_students = ['ZHAIMER MAMACOTAO', 'VITO DE GUZMAN', 'SUKHJAAN SINGH', 'SEBASTIAN UCLARAY', 'PAULO LIWAG', 'LUIS BACAY', 'LIAM NOLASCO', 'KHAIL RESURRECCION','JUAN PIANSAY','JOAQUIN TABIJE', 'JAMSED JUNAID']

    full_name = f"{document.getElementById('Fname').value} {document.getElementById('Lname').value}".upper().strip()
    name_checker = full_name in varsity_students # True(1) or False(0)
    
    display_message = ('Sorry, your name is not found in the list.', f'{full_name} is a member of the OBMC mens basketball team.')  # Sets message for True or False
    display(display_message[name_checker], target='div1') # displays message



