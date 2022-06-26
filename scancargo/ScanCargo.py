## Learning BPMN 2nd Edition
## Service Tasks; Scan Cargo
## Sample code for how Erin might scaffold the Scan Cargo process with
## her team based on success criteria and potential failures

class ScanCargo:

    def __init__(self):
        self.scan_cargo()

    def scan_cargo(self):
        try:
            self.remove_cargo()
        except CargoDroppedError as e:
            # do something
            exit()
        except CargoGrabError as e:
            # do something
            exit()
        except CargoReleaseError as e:
            # do something
            exit()
        except CargoStorageEmptyError as e:
            # do something
            exit()

        try:
            self.scan_identifier()
        except CargoScanError as e:
            # do something
            exit()
        except CargoMismatchError as e:
            # do something
            exit()

        try:
            self.prepare_to_move()
        except CargoCommunicationError as e:
            # do something
            exit()

    def remove_cargo(self):
        # do something

    def scan_identifier(self):
        # do something

    def prepare_to_move(self):
        # do something
