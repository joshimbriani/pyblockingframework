# pyblockingframework
Python blocking framework for Advanced Database class

----------------------
Token Blocking and Attribute Clustering
----------------------
Navigate to the correct directory and run the following command

python runner.py "data/movies_imdb.csv" "data/movies_movielens.csv" "NameOfAlgorithm"

Replacing the two data files with your data files and "NameOfAlgorithm" with the name of the algorithm you want to run

----------------------
BSL - In a python IDE
----------------------
On line #36 in the dedupeBSL.py file, insert your csv filename in the input_file section

Run the code and in the shell and answer (y)yes or (n)no to the comparisons until finished, and answer (f)finished

After this the file will create a training set and reload this file to the program

Final Output: A csv file with pair comparisons and comparison scores

----------------------
Adding new Algorithm
----------------------
This framework is designed to be easily extended. New algorithms can be added as follows:

Add lines to runner.py that have the following lines:
elif comparisonToRun == "blockingTokens":
		result.runBlockingTokens()
but with blockingTokens replaced with the name of the algorithm

Import the algorithm into the comparer.py file and add the method runX where X is replaced with the name of your algorithm. 

Make a file with the name of your algorithm that has a function in it that has the same name and takes two arguments (data1 and data2)
