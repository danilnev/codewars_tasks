def validate_pin(pin: str):
    if pin.isdigit() and len(pin) in [4, 6]:
        return True
    return False
