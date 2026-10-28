class Customer:
    def __init__(self, id, user_id, first_name, last_name, national_id, phone=None):
        self.id = id
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.national_id = national_id
        self.phone = phone
