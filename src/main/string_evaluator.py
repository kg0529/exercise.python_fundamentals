# Created by Leon Hunter at 3:57 PM 10/23/2020
class StringManipulator(object):
    def get_hello_world(self):
        temp_hello = "Hello World"
        return temp_hello

    def concatenate(self, value_to_be_added_to, value_to_add):
        return value_to_be_added_to + value_to_add

    def substring_inclusive(self, string_to_fetch_from, starting_index, ending_index):
        temp_inclusive = string_to_fetch_from[starting_index:ending_index+1]
        return temp_inclusive

    def substring_exclusive(self, string_to_fetch_from, starting_index, ending_index):
        temp_exclusive = string_to_fetch_from[starting_index+1:ending_index]
        return temp_exclusive

    def compare(self, first_value, second_value):
        return first_value == second_value

    def get_middle_character(self, string_to_fetch_from):
        mid_index = len(string_to_fetch_from)
        return string_to_fetch_from[mid_index]

    def get_first_word(self, string_to_fetch_from):
        temp_string_first = string_to_fetch_from.split(" ")
        return temp_string_first[0]

    def get_second_word(self, string_to_fetch_from):
        temp_string_second = string_to_fetch_from.split(" ")
        return temp_string_second[1]

    def reverse(self, string_to_be_reversed):
        return string_to_be_reversed[::-1]