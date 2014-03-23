SimilarityChecker
=================

Malayalam similarity checker using ngrams



The project:

    Propose an algorithm for plagiarism detection in the Indian language,
    Malayalam using a modified n-gram model. 
    The idea of w-shingling enhances the accuracy and reduces the processing time involved.
    Propose an algorithm to handle inflection and to do suffix stripping.
    It is a new algorithm based on more than 250 rules identified .
    This would serve as a pre-processing step for the standardization of the document.



More details:

A plagiarism detection system for Malayalam text
passages based on the modified n-gram model is proposed in
this model. There are two modules namely, the standardizer
and the similarity checker as shown . The input to the
standardizer is two Malayalam text documents. The
standardized outputs of the standardizer are given as inputs to
the similarity checker. If the degree of similarity is above a
given threshold, then the given document is considered as the
copy of the reference document.


A. Standardizer


		The documents are standardized
		The hyphenation is handled and the punctuation marks are removed.
		The output is given to a suffix stripper to handle inflection
		
B. Similarity checker

		The ngrams of the standardized is calculated and the w-shingling is performed  . 
		The similarity is calculated. 
		If the similarity value is greater than a threshold then the given document is considered
		as the plagiarized copy of the other
