"""
dnatools.py

This module provides tools for working with DNA sequences. The main functionalities include:
- Calculating the length of a DNA sequence.
- Reading a DNA sequence from a file.
- Calculating the GC content of a DNA sequence.
- Checking the GC content level of a DNA sequence against specified thresholds.

Functions:
- get_seqlength(seqfile): Calculates the length of a DNA sequence.
- readseq(seqfile): Reads a DNA sequence from a file and returns it in uppercase.
- get_gc_content(seq): Calculates the GC content of a DNA sequence as a percentage.
- check_gc_content_level(seqfile, threshold_high=60.0, threshold_low=40.0): Checks the GC content level of a DNA sequence and categorizes it as high, low, or moderate.
"""

def get_seqlength(seqfile):
    """
    Calculate the length of a DNA sequence.

    Args:
        seqfile (str): The path to the sequence file.

    Returns:
        int: The length of the DNA sequence.
    """
    with open(seqfile, "r", encoding="utf-8") as fpin:
        seqlength = 0
        for line in fpin:
            if not line.startswith(">"):
                seqlength += len(line.strip())
    return seqlength

def readseq(seqfile):
    """
    Read a DNA sequence from a file and return it in uppercase.

    Args:
        seqfile (str): The path to the sequence file.

    Returns:
        str: The DNA sequence in uppercase.
    """
    with open(seqfile, "r", encoding="utf-8") as fpin:
        seq = ""
        for line in fpin:
            if not line.startswith(">"):
                seq += line.strip()
    return seq.upper()

def get_gc_content(seq):
    """
    Calculate the GC content of a DNA sequence as a percentage.

    Args:
        seq (str): The DNA sequence.

    Returns:
        float: The GC content percentage of the DNA sequence.
    """
    return (seq.count('G') + seq.count('C')) / len(seq) * 100

def check_gc_content_level(seqfile, threshold_high=60.0, threshold_low=40.0):
    """
    Check the GC content level of a DNA sequence and categorize it as high, 
    low, or moderate based on specified thresholds.

    Args:
        seqfile (str): The path to the sequence file.
        threshold_high (float, optional): The threshold for high GC content. Default is 60.0.
        threshold_low (float, optional): The threshold for low GC content. Default is 40.0.

    Returns:
        str: A message indicating the GC content percentage and its level (high, low, or moderate).
    """
    seq = readseq(seqfile)
    gc_content = get_gc_content(seq)
    if gc_content >= threshold_high:
        return f"The GC content of the sequence from {seqfile} is {gc_content:.2f}%, level is high"
    elif gc_content <= threshold_low:
        return f"The GC content of the sequence from {seqfile} is {gc_content:.2f}%, level is low"
    else:
        return f"The GC content of the sequence from {seqfile} is {gc_content:.2f}%, level is moderate"
