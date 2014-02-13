# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: YOUR NAME HERE
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons
import random

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    
    A = []
    i = 0
    while i<len(dna):
        A.append(dna[i:i+3])
        i = i+3
    for i in range (len(A)):
        for k in range (len(codons)):
            if A[i] in codons[k]:
                A[i] = aa[k]
    return A

def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
    dna = "ATGTTT"
    print coding_strand_to_AA(dna)
    
#coding_strand_to_AA_unit_tests()

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    newDna = ""
    for i in range(len(dna)):
        if dna[i] =='A':
            newDna += ("T")
        elif dna[i] =="C":
            newDna += ("G")
        elif dna[i] =="G":
            newDna += ("C")
        elif dna[i]=="T":
            newDna += ("A")
   
             
    return newDna
    
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
    dna = "ATGATCA"    
    print get_reverse_complement(dna)
    
    
#get_reverse_complement_unit_tests()
    
      
      
        

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    D = []
    returnD = []
    i = 0
    while i<len(dna):
        D.append(dna[i:i+3])
        i = i+3
    for j in range (len(D)):
        if D[j] in codons[10]:
            break
        returnD.append(D[j])
    stringD = collapse(returnD)
    return stringD
        
    
def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
    dna = "ATGATAGTCTAATGACGT"        
    print rest_of_ORF(dna)

#rest_of_ORF_unit_tests()
        
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    i=0
    D = []
    allOrfs = []
    while i<len(dna):
       D.append(dna[i:i+3])
       i = i+3
    for j in range (len(D)):
        if D[j] == codons[3][0]:
            N = rest_of_ORF(dna[j*3:len(dna)])
            allOrfs.append(N)
            j += len(N)/3
    return allOrfs
              
                    
                
            
    
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function 
    """
    dna = "ATGATTGTCATACCTGATAATGATTAAATGAACTAA"
    print find_all_ORFs_oneframe(dna)

#find_all_ORFs_oneframe_unit_tests()

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    Orfs = find_all_ORFs_oneframe(dna)
    data = list(dna)
    del data[0]
    data = collapse(data)
    
    Orfs.extend(find_all_ORFs_oneframe(data))
    data = list(data)
    del data[0]
    data = collapse(data)
    
    Orfs.extend(find_all_ORFs_oneframe(data))
    
    return Orfs
        
    

def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
    dna = "ATGATTGTCATACCTGATAATGATTAAATGAACTAA"
    print find_all_ORFs(dna)

#find_all_ORFs_unit_tests()    
    

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    ORFs = find_all_ORFs(dna)
    data = get_reverse_complement(dna)
    ORFs.extend(find_all_ORFs(data))
    
    return ORFs

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """
    dna = "ATGATTGTCATACCTGATAATGATTAAATGAACTAA"
    print find_all_ORFs_both_strands(dna)
#find_all_ORFs_both_strands_unit_tests()

    

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""

    return max(find_all_ORFs_both_strands(dna), key=len)  #roommate is claire, shameless borrowing of idea

def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    dna = "ATGATTGTCATACCTGATAATGATTAAATGAACTAA"
    print longest_ORF(dna)

#longest_ORF_unit_tests()

def longest_ORF_noncoding(dna,num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    ORFs = []
    for i in range (num_trials):
    
        data = list(dna)
        random.shuffle(data)
        data = collapse(data)
    
        ORFs.extend(longest_ORF(data))
    return len(max(ORFs,key=len))



def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    ORFs = find_all_ORFs_both_strands(dna)
    i = 0
    longORFs = []
    while i <= len(ORFs):
        i += 1
        if len(ORFs(i))>=threshold:
            longORFs.append(coding_strand_to_AA(ORFs(i)))
    return longORFs
            
 