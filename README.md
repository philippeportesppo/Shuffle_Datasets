# Shuffle_Datasets
Python scripts to split a global data set into a learning set, test and validation sets.

Syntax:
shuffle.py name_of_the_file_to_shuffle.tsv prefix_for_files_to_generate

Exanple:
shuffle Listbestbuy.tsv Listbestbuy

Will result in the creation of:
  Listbestbuy_learn.tsv
  Listbestbuy_test.tsv
  Listbestbuy_valid.tsv
  
_test and _valid only differs in valid having the 5star values so that the results of a learning algorithm on _test can be assessed.

The proportion between learn and test/valid is 60%/40%
