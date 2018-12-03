

def prepReviewData():
    df = pandas.read_csv("Data/reviews_small.csv", encoding="latin1", header=None)
    df.columns = ["reviews"]


    #TODO remove stop words, correct misspelled ones,convert sentence in an array of cleaned words

    # Begin cleaning code


    # End cleaning code

    df = df.reset_index(drop=True)
    return df