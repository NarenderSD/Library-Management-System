# Copyright (c) 2024, Narender Singh and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class LibraryMember(Document):

    def before_save(self):
        self.full_name = f'{self.first_name} {self.last_name or ""}'
# Path: library-bench/apps/library_management/library_management/library_management/doctype/library_member/library_member.py
# first name and last name are the fields of the library member doctype
