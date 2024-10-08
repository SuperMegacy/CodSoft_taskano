class InvalidPhoneNumberError(Exception):
    pass


class PhoneNumberValidator:
    def validate(self, pnumber: int) -> bool:
        if len(pnumber) < 10 or not pnumber.isdigit():
            raise InvalidPhoneNumberError(f"Invalid Phone number: {pnumber}.")
        return True

