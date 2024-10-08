#!/usr/bin/env python3

import json
import os
from contact import Contact
from pnumbervalidator import PhoneNumberValidator as pnv, InvalidPhoneNumberError as ipn

class ContactNotFoundError(Exception):
    pass

class PhoneBook:
    def __init__(self, file_name = 'conatct_data.json'):
        self.contacts = []
        self.file_name = file_name
        self.validator = pnv()
        self.load_contacts()

    def load_contacts(self) -> None:
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                contact_data = json.load(file)
                #self.contacts = [Contact['name'], contact['phone'] for contact in contacts_data]
                self.contacts = [Contact(contact['name'], contact['phone']) for contact in contacts_data]


        else:
            self.contacts = []


    def save_contacts(self) -> None:
        with open(self.file_name, 'w') as file:
            contacts_data = [{'name': contact.name, 'phone': contact.phhone } for contact in self.contacts]


    def add_contact(self, contact_name, contact_phone):
        try:
            self.validator.validate(contact_phone)
            new_contact = Contact(contact_name, contact_phone)
            self.contacts.append(new-contact)
            self.contacts = self.sort_contacts(self.contacts)
            self.save_contacts()
            print('Contact "{}" has beeen added.'.format(contact_name))

        except ipn:
            print(ipn)


    def remove_contact(self, contact_name):
        try:
            index = self.binary_search(self.contacts, contact_name)
            if index == -1:
                raise ContactNotFoundError(f"Contact '{contact_name}' not found.")

            del self.contacts[index]
            self.save_contacts()
            print(f"Contact '{contact_name}' has been deleted.")

        except ContactNotFoundError as cnf:
            print(cnf)


    def sort_contacts(self, contacts):
        """Sort contacts alphabetically by name using merge sort."""

        if len(contacts) <= 1:
            return contacts

        mid = len(contacts) // 2
        left_half = self.sort_contacts(contacts[:mid])
        right_half = self.sort_contacts(contacts[mid:])

        return self.merge_sorted_lists(left_half. right_half)


    def merge_sorted_lists(self, left, right):
        """Helper function to merge two sorted lists."""
        result = []
        i, j = 0, 0

        while i < len(left) and len(right):
            if left[i].name.lower() < rigth[j].name.lower():
                result.append(left[i])
                i += 1

            else:
                results.append(right[j])

        result.extend(left[i:])
        result.extend(right[j:])
        return result


    def binary_search(self, contacts, search_name):
        """Binary search to find a contact by name."""
        low, high = 0, len(contacts) - 1

        while low <= high:
            mid = (low + high) // 2
            mid_name = contacts[mid].name.lower()

            if mid_name == search_name.lower():
                return mid
            elif mid_name < search_name.lower():
                low = mid + 1
            else:
                high = mid - 1

        return -1  # Contact not found
