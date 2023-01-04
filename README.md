Hello, I am Samuel Hanneson, this is a project that was given to me by a friend as a test for my skills.

Before this project I had just completed the intro to python3 course on Codecademy so this was quite the leap to complete but I have done it so here is the real readme.

Fisher Iris Data Set Analysis

This project is an analysis of the Fisher Iris Data Set, which is a classic dataset in the field of machine learning. It consists of 150 records of iris plants, including the sepal length and width, petal length and width, and class (one of three types of iris plants). The data was collected by Edgar Anderson and published in the paper "The use of multiple measurements in taxonomic problems" by Ronald Fisher in 1936.

Data Set Summary
The data set contains the following variables:

  * sepal_length: the length of the sepal, in centimeters.
  * sepal_width: the width of the sepal, in centimeters.
  * petal_length: the length of the petal, in centimeters.
  * petal_width: the width of the petal, in centimeters.
  * class: the class of the iris plant, one of three types (Iris-setosa, Iris-versicolor, Iris-virginica).


Analysis
The analysis.py program performs the following actions:

  * Downloads the Fisher Iris Data Set from the UCI Machine Learning Repository.
  * Outputs a summary of each variable to a single text file called summary.txt. The summary includes the name of the column, data type, number of missing values, number   of unique values, minimum value, and maximum value.
  * Plots histograms of all variables and saves the plots to png files with names in the format {column_name}_histogram.png.
  * Plots scatterplots of all pairs of variables and saves the plots to png files with names in the format {column_name_1}_{column_name_2}_scatterplot.png.
  
Running the Code
To run the analysis.py program, follow these steps:

  * Make sure that you have Python 3 installed on your machine.
  * Download or clone the project repository.
  * Navigate to the project directory in the terminal.
  * Run the command python analysis.py.
  
References
Fisher, R. A. (1936). The use of multiple measurements in taxonomic problems. Annals of Eugenics, 7(2), 179-188.
UCI Machine Learning Repository: Iris Data Set. (n.d.). Retrieved from http://archive.ics.uci.edu/ml/datasets/Iris
