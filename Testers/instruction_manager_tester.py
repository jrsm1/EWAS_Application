from Control_Module_Comm import serial_interface, instruction_manager


def test_listen():
    tester = serial_interface.serial_interface()
    line = tester.listen()
    line = str(line)
    line = line[2:len(line) - 5]
    print(line)


def test_send():
    tester = serial_interface.serial_interface()
    line = tester.send_string('test')
    print(line)


def test_send_byte():
    tester = serial_interface.serial_interface()
    line = tester.send_byte(b'\x81')
    print(line)


def test_compare_byte():
    tester = serial_interface.serial_interface()
    line = tester.listen()
    line = line.strip(b'\r\n')
    if line == b'\x80': print("comparison succesful: x80 == x80")
    if line != b'\x81': print("comparison succesful: x80 != x81")
    print(line)


def test_send_configuration():
    tester = instruction_manager.instruction_manager()
    tester.init(1)
    tester.send_set_configuration("what")


def test_request_configuration():
    tester = instruction_manager.instruction_manager()
    tester.init(1)
    tester.send_request_configuration()


def test_request_start():
    tester = instruction_manager.instruction_manager()
    tester.init(1)
    tester.send_request_start()


def test_request_number_of_modules_connected():
    tester = instruction_manager.instruction_manager()
    tester.init(1)
    line = tester.send_request_number_of_mods_connected()
    print("modules connected: " + str(line))


def test_send_live_stream_request():
    tester = instruction_manager.instruction_manager()
    tester.init(1)
    tester.send_live_stream_request(1, 1, 2)


def test_send_cancel():
    tester = instruction_manager.instruction_manager()
    tester.init(1)
    tester.send_cancel_request()


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


if __name__ == "__main__":
    # test_listen()
    # test_send()
    # test_send_byte()
    # test_compare_byte()
    test_instruction_existante()
    # test_request_number_of_modules_connected()
