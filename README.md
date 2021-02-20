# Quantify the polysemy of words in a list using WordNet

This bite-sized script may come in handy if you are a linguist and want to know whether some words are polysemous, and to what extent. It computes the Wu-Palmer Similarity score between all pairs of WordNet synsets of each word in your list, considers critically polysemous any pair having a score below 0.15 (based on the Wu-Palmer Similarity scores for the noun "bank"). Check the script for more details!

## Getting started

The script should run on Python 3.0+ and does not have to be installed. Runs fine on Python 3.8.2 in Ubuntu 20.10.

### Prerequisites

You need the following Python packages to make the script work:

    more-itertools==4.2.0
    nltk==3.5
    
To install these packages in Python 3, make sure you have installed pip3 and run:    
    
    pip3 install <package>
    
## Running the script

Just run the script with Python 3, results are printed in the terminal. You can modify the script to include your custom list of words, and also edit the part of speech (now it's verbs) and the language (now it's English).

## License

This project is licensed under the MIT License.

## Acknowledgments

Many thanks to the Stack Overflow community, for the many code snippets that saved me from frustration.

