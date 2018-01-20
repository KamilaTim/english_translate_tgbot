from kamilas_lib import case_of_error

assert case_of_error(403) == "some error...with error code"
assert case_of_error("403") == "another mistake"
assert case_of_error(False) == "another mistake"
