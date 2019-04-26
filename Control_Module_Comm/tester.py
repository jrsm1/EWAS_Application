import Control_Module_Comm.serial_interface as serial_interface
import Control_Module_Comm.instruction_manager as instruction_manager

def test_listen():
    tester = serial_interface.serial_interface('COM6')
    line = "a"
    while line != '\\xAA\\xBB\\xAA\\xBB':
        line = tester.listen()
        line = str(line)
        print(line)
        line = line[2:len(line)-5]
        print(line)
    print("done")
    
def test_send():
    tester = serial_interface.serial_interface('COM6')
    line = tester.send_string('test')
    print(line)
    
def test_send_byte():
    tester = serial_interface.serial_interface('COM6')
    line = tester.send_byte(b'\x81')
    print(line)
    
def test_compare_byte():
    tester = serial_interface.serial_interface('COM6')
    line = tester.listen()
    line = line.strip(b'\r\n')
    if line == b'\x80': print("comparison succesful: x80 == x80")
    if line != b'\x81': print("comparison succesful: x80 != x81")
    print(line)
    
def test_send_configuration():
    tester = instruction_manager.instruction_manager('COM6')
    # tester.init(1)
    bool = tester.send_set_configuration("set dmmy configuration text")
    if bool:
        print("send configuration test sucessful")
    
def test_request_configuration():
    tester = instruction_manager.instruction_manager('COM6')
    # tester.init(1)
    line = tester.send_request_configuration()
    #print("line is " + str(line))
    if line:
        print("request configuration succesful")
        print("microntroller output is: " + str(line))
    else:
        print("test failed")
    
def test_request_start():
    tester = instruction_manager.instruction_manager('COM6')
    # tester.init(1)
    bool = tester.send_request_start()
    if bool:
        print("request start succesful")

def test_request_number_of_modules_connected():
    tester = instruction_manager.instruction_manager('COM6')
    # tester.init(1)
    line = tester.send_request_number_of_mods_connected()
    print("type of them are" + str(type(line[0])))
    if line:
        print("request number of modules successful")
        print("modules connected: " + str(line))
    
def test_send_live_stream_request():
    tester = instruction_manager.instruction_manager('COM6')
    # tester.init(1)
    tester.send_live_stream_request(1, 1, 2)
    
def test_request_live_bytes():
    tester = instruction_manager.instruction_manager('COM6')
    # tester.init(1)
    line = tester.send_request_live_bytes()
    if line:
        print("request live bytes successful")
        print("live bytes are " + str(line))
    
def test_send_cancel():
    tester = instruction_manager.instruction_manager('COM6')
    # tester.init(1)
    bool = tester.send_cancel_request()
    if bool:
        print("cancel request successful")
    
def test_request_all_data():
    tester = instruction_manager.instruction_manager('COM6')
    # tester.init(1)
    line = tester.send_request_all_data()
    if line:
        print("request all data successful")
        print("microntroller output is: " + str(line))
    
def test_gps_data_request():
    tester = instruction_manager.instruction_manager('COM6')
    # tester.init(1)
    line = tester.send_gps_data_request()
    if line:
        print("request gps data successful")
        print("microntroller output is: " + str(line))
        
def test_sync_gps_request():
    tester = instruction_manager.instruction_manager('COM6')
    # tester.init(1)
    bool = tester.send_gps_sync_request()
    if bool:
        print("request gps sync succesful")
        
def test_diagnose_request():
    tester = instruction_manager.instruction_manager('COM6')
    # tester.init(1)
    line = tester.send_diagnose_request()
    if line:
        print("request diagnode successful")
        print("microntroller output is: " + str(line))
        
def test_request_status():
    tester = instruction_manager.instruction_manager('COM6')
    # tester.init(1)
    line = tester.send_request_status()
    if line:
        print("request status successful")
        print("microntroller output is: " + str(line))
    
def test_request_configuration_validity():
    tester = instruction_manager.instruction_manager('COM6')
    # tester.init(1)
    line = tester.send_request_configuration_validity()
    if line:
        print("request configuration validity successful")
        print("microntroller output is: " + str(line))

        """
def test_instruction_existante():
    test_send_configuration()
    test_request_configuration()
    test_request_start()
    test_request_number_of_modules_connected()
    test_send_live_stream_request()
    test_send_cancel()
    tester = serial_interface.serial_interface()
    tester.send_string('test')
    print("--sent test--")
    line = tester.listen()
    line = line.strip(b'\r\n')
    if line == b'\xFE': print("wrong instruction succesful")
    """
def test_wrong_instruction_acknowledge():
    tester = serial_interface.serial_interface()
    tester.send_string('test')
    print("--sent test--")
    line = tester.listen()
    line = line.strip(b'\r\n')
    if line == b'\xFE': print("wrong instruction succesful")

def test_specific_daq(daq):
    tester = instruction_manager.instruction_manager('COM6')
    line = tester.send_request_data(daq)
    print("recieved line " + str(line))
    
    
# if __name__ == "__main__":
test_specific_daq(1)
# test_listen()
# test_send()
# test_send_byte()
# test_compare_byte()
# -----------------------------------------------------
# test_send_configuration()
# test_request_configuration()
# test_request_start()
#test_request_number_of_modules_connected()
# test_request_live_bytes()
# test_send_cancel()
# test_request_all_data()
# test_listen()
# test_gps_data_request()
# test_sync_gps_request()
# test_diagnose_request()
# test_request_status()
# test_request_configuration_validity()
# test_wrong_instruction_acknowledge()
    