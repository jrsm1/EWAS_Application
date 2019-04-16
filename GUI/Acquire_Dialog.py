from GUI import GUI_Handler
from Control_Module_Comm import instruction_manager


def show_dialog(message: str):
    # Set progress  # TODO LEARN

    # Show Dialog & Set Message
    GUI_Handler.show_progress_dialog('Acquiring ' + message)

    # Enable Main Window when done.  # FIXME Change to correct function.
    GUI_Handler.enable_main_window()



"""
Sends signal to Control Module to cancel all recording, storing, sending, synchronizing and/or
any other process the system might be doing. 

Called by user when CANCEL action is desired.
"""
def action_cancel_everything():
    im = instruction_manager.instruction_manager()
    im.send_cancel_request()
