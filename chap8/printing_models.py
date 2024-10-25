"""
This file uses functions from printing_functions.py to manage car model printing.
"""

from printing_functions import print_models, show_completed_models

unprinted_designs = ['model A', 'model B', 'model C']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
