# Created by Leon Hunter at 3:57 PM 10/23/2020
class StringManipulator(object):
    def get_hello_world(self):
        return "Hello World" # TODO - Implement solution

    def concatenate(self, value_to_be_added_to, value_to_add):
        return str(value_to_be_added_to) + str(value_to_add) # TODO - Implement solution

    def substring_inclusive(self, string_to_fetch_from, starting_index, ending_index):
        return string_to_fetch_from[starting_index:ending_index+1] # TODO - Implement solution

    def substring_exclusive(self, string_to_fetch_from, starting_index, ending_index):
        return string_to_fetch_from[starting_index+1:ending_index] # TODO - Implement solution

    def compare(self, first_value, second_value):
        first_is = str(type(first_value))
        second_is = str(type(second_value))
        if (first_is == "<class 'str'>" and second_is == "<class 'int'>") or (first_is == "<class 'int'>" and second_is == "<class 'str'>"):
            var = str(first_value) == str(second_value)
        else:
            var = first_value == second_value
        return var # TODO - Implement solution

    def get_middle_character(self, string_to_fetch_from):
        return None # TODO - Implement solution

    def get_first_word(self, string_to_fetch_from):
        list = string_to_fetch_from.split()
        return list[0] # TODO - Implement solution

    def get_second_word(self, string_to_fetch_from):
        list = string_to_fetch_from.split(" ")
        return list[1] # TODO - Implement solution

    def reverse(self, string_to_be_reversed):
        return None # TODO - Implement solution