import pandas as pd
import matplotlib.pyplot as plt

def summarize_data(df):
    # Output a summary of each variable to a single text file
    with open('summary.txt', 'w') as f:
        for col in df.columns:
            f.write(f'Column: {col}\n')
            f.write(f'Data type: {df[col].dtype}\n')
            f.write(f'Number of missing values: {df[col].isna().sum()}\n')
            f.write(f'Number of unique values: {df[col].nunique()}\n')
            f.write(f'Minimum value: {df[col].min()}\n')
            f.write(f'Maximum value: {df[col].max()}\n\n')

def plot_histograms(df):
    # Save a histogram of each variable to a png file
    for col in df.columns:
        plt.hist(df[col])
        plt.title(f'Histogram of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.savefig(f'{col}_histogram.png')
        plt.clf()  # Clear the plot for the next iteration

def plot_scatterplots(df):
    # Output a scatter plot of each pair of variables
    for col1, col2 in df.columns:
        plt.scatter(df[col1], df[col2])
        plt.title(f'Scatter plot of {col1} vs {col2}')
        plt.xlabel(col1)
        plt.ylabel(col2)
        plt.savefig(f'{col1}_{col2}_scatterplot.png')
        plt.clf()  # Clear the plot for the next iteration

def main():
    # Load the Fisher Iris Data Set into a Pandas dataframe
    df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
                     names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

    # Summarize the data and save the summary to a text file
    summarize_data(df)

    # Plot histograms of all variables and save the plots to png files
    plot_histograms(df)

    # Plot scatterplots of all pairs of variables and save the plots to png files
    plot_scatterplots(df)

if __name__ == '__main__':
    main()