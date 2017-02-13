import random
from math import floor


# dictionary: sum of codon = key, corresponding amino acid = value 
amino_acid_to_codon_sum = {"q": 1, "j": 2, "v": 3, "p": 4, "g": 5, "w": 6, "u": 7, "l": 8, "r": 9, "s": 10, "i": 11, "a": 12,
                    "e": 13, "t": 14, "o": 15, "n": 16, "h": 17, "d":18, "c": 19, "m": 20, "f": 21, "y": 22, "b": 23,
                    "k": 24, "x": 25, "z": 26}


# split amino acid into codon of 3 random, valid mRNA
# Example: 12 = [6,6,0]
# Example: 22 = [8,9,5]
# Example: 0 = [0,0,0]
def split_amino_acid_into_3_mRNA(amino_acid):
    mRNA_list = []
    first_mRNA = random.randint(0, amino_acid)
    second_mRNA = random.randint(0, amino_acid-first_mRNA)
    third_mRNA = amino_acid - first_mRNA-second_mRNA
    valid = False

    # valid if all values in the mRNA_list are less than <= 9
    while not valid:
        if first_mRNA > 9 or second_mRNA > 9 or third_mRNA > 9:
            first_mRNA = random.randint(0, amino_acid)
            second_mRNA = random.randint(0, amino_acid-first_mRNA)
            third_mRNA = amino_acid - first_mRNA-second_mRNA
        else:
            # all values mRNA are less <= 9
            valid = True
    mRNA_list.append(str(first_mRNA))
    mRNA_list.append(str(second_mRNA))
    mRNA_list.append(str(third_mRNA))
    return mRNA_list


# Convert proteins to appropriate format for synthetic genome
# EXAMPLE: bath returns 110100659215
# EXAMPLE: tomorrow returns 668456247492477765159878
# EXAMPLE: meaning returns 841500001554090347034
# * outputs are random
def convert_protein_to_nucleotide_sequence(potential_protein):
    protein_as_nucleotide_sequence = ""
    nums = []
    for letter in potential_protein:
        nums.append(amino_acid_to_codon_sum[letter])
    for number in nums:
        protein_as_nucleotide_sequence += "".join(split_amino_acid_into_3_mRNA((number)))

    return protein_as_nucleotide_sequence


# RETURNS 000 OR 999, THE STOP CODONS IN THE SYNTHETIC GENOME
# SEQUENCE DENOTES END OF PROTEIN
def get_stop_codon():
    stop_codon_list = ["000", "999"]
    stop_codon = random.choice(stop_codon_list)
    return stop_codon


# SHINE DALGARNO DENOTES THAT A PROTEIN IS NEAR
# RANDOMLY GENERATE SHINE DALGARNO SEQUENCE
def generate_shine_dalgarno():
    generated_shine_dalgarno_sequence = ""

    # LENGTH OF SHINE DALGARNO IS BETWEEN 5 AND 8
    length_of_shine_dalgarno = 6
    
    # APPEND NUCLEOTIDES TO SHINE DALGARNO SEQUENCE
    for i in range(0, length_of_shine_dalgarno):
        nucleotide = random.randint(0, 9)
        nucleotide = str(nucleotide)
        generated_shine_dalgarno_sequence += nucleotide
    return generated_shine_dalgarno_sequence


# SHINE DALGARNO DECLARED HERE SO IT WON'T BE NEWLY AND RANDOMLY GENERATED CONTINUOUSLY
# IF SHINE DALGARNO IS CONSTANTLY GENERATED RANDOMLY IT WILL NOT BE EASILY RECOGNIZABLE IN SYNTHETIC GENOME
shine_dalgarno_sequence = generate_shine_dalgarno()


# Begin placing proteins on frames--> Each frame function is separate despite redundancies in order to keep all frames
# independent of one another --> Important when adding functions that manipulate a particular frame, i.e. searching what
# frame a protein is on


# PRE: STRING, INT
# POST: STRING
# APPENDS PROTEIN TO FIRST FRAME ALONG WITH STOP CODON
def append_protein_to_first_frame(protein, frame):
    shine_dalgarno = shine_dalgarno_sequence
    front_step_nucleotide = ""
    back_step_nucleotide = ""
    stop_codon = get_stop_codon()

    # IF ON SECOND OR THIRD FRAME JUMP TO SECOND FRAME USING STEP NUCLEOTIDES
    # IF ON FIRST FRAME RETURN PROTEIN WITH STOP CODON, WITHOUT INVOLVING STEP NUCLEOTIDES 
    if frame == 3:
        step_nucleotide = random.randint(0, 9)
        front_step_nucleotide = str(step_nucleotide)
        for i in range(0, 2):
            back_step_nucleotide += str(random.randint(0, 9))
    elif frame == 2:
        for i in range(0, 2):
            front_step_nucleotide += str(random.randint(0, 9))
        back_step_nucleotide = random.randint(0, 9)
        back_step_nucleotide = str(back_step_nucleotide)
    else:
        return shine_dalgarno + protein+stop_codon

    # RETURN PROTEIN WITH STEP NUCLEOTIDES TO CHANGE FRAME AND STOP CODON APPENDED
    protein_on_first_strand = shine_dalgarno + front_step_nucleotide + protein + stop_codon + back_step_nucleotide

    return protein_on_first_strand


# PRE: STRING, INT
# POST: STRING
# APPENDS PROTEIN TO SECOND FRAME ALONG WITH STOP CODON
def append_protein_to_second_frame(protein, frame):
    shine_dalgarno = shine_dalgarno_sequence
    front_step_nucleotide = ""
    back_step_nucleotide = ""
    stop_codon = get_stop_codon()

    # IF ON FIRST OR THIRD FRAME JUMP TO SECOND FRAME USING STEP NUCLEOTIDES
    # IF ON SECOND FRAME RETURN PROTEIN WITH STOP CODON, WITHOUT INVOLVING STEP NUCLEOTIDES 
    if frame == 1:
        step_nucleotide = random.randint(0, 9)
        front_step_nucleotide = str(step_nucleotide)
        for i in range(0, 2):
            back_step_nucleotide += str(random.randint(0, 9))
    elif frame == 3:
        for i in range(0, 2):
            front_step_nucleotide += str(random.randint(0, 9))
        back_step_nucleotide = random.randint(0, 9)
        back_step_nucleotide = str(back_step_nucleotide)
    else:
        return shine_dalgarno + protein+stop_codon

    # RETURN PROTEIN WITH STEP NUCLEOTIDES TO CHANGE FRAME AND STOP CODON APPENDED
    protein_on_second_strand = shine_dalgarno + front_step_nucleotide + protein + stop_codon + back_step_nucleotide
    return protein_on_second_strand


# PRE: STRING, INT
# POST: STRING
# APPENDS PROTEIN TO FIRST FRAME ALONG WITH STOP CODON
def append_protein_to_third_frame(protein, frame):
    shine_dalgarno = shine_dalgarno_sequence
    # STEP NUCLEOTIDES ALLOW NAVIGATION BETWEEN FRAMES
    front_step_nucleotide = ""
    back_step_nucleotide = ""
    stop_codon = get_stop_codon()

    # IF ON FIRST OR SECOND FRAME JUMP TO SECOND FRAME USING STEP NUCLEOTIDES
    # IF ON THIRD FRAME RETURN PROTEIN WITH STOP CODON, WITHOUT INVOLVING STEP NUCLEOTIDES 
    if frame == 2:
        step_nucleotide = random.randint(0, 9)
        front_step_nucleotide = str(step_nucleotide)
        for i in range(0, 2):
            back_step_nucleotide += str(random.randint(0, 9))
    elif frame == 1:
        for i in range(0,2):
            front_step_nucleotide += str(random.randint(0, 9))
        back_step_nucleotide = random.randint(0, 9)
        back_step_nucleotide = str(back_step_nucleotide)
    else:
        return shine_dalgarno + protein + stop_codon

    # RETURN PROTEIN WITH STEP NUCLEOTIDES TO CHANGE FRAME AND STOP CODON APPENDED
    protein_on_third_strand = shine_dalgarno + front_step_nucleotide + protein + stop_codon + back_step_nucleotide
    return protein_on_third_strand


# PRE: STRING, INT
# POST: STRING
# APPENDS PROTEIN TO FIRST FRAME ON MINUS STRAND ALONG WITH STOP CODON
def append_protein_to_minus_one_frame(protein, frame):
    shine_dalgarno = shine_dalgarno_sequence
    # STEP NUCLEOTIDES ALLOW NAVIGATION BETWEEN FRAMES
    front_step_nucleotide = ""
    back_step_nucleotide = ""
    stop_codon = get_stop_codon()

    # IF ON MINUS TWO OR MINUS THREE FRAME JUMP TO MINUS ONE FRAME USING STEP NUCLEOTIDES
    # IF ON MINUS ONE FRAME RETURN PROTEIN WITH STOP CODON, WITHOUT INVOLVING STEP NUCLEOTIDES
    if frame == -2:
        step_nucleotide = random.randint(0, 9)
        front_step_nucleotide = str(step_nucleotide)
        for i in range(0, 2):
            back_step_nucleotide += str(random.randint(0, 9))
    elif frame == -3:
        for i in range(0, 2):
            front_step_nucleotide += str(random.randint(0, 9))
        back_step_nucleotide = str(random.randint(0, 9))
    else:
        return (protein+stop_codon)[::-1]

    # RETURN PROTEIN WITH STEP NUCLEOTIDES TO CHANGE FRAME AND STOP CODON APPENDED
    protein_on_minus_one_strand = front_step_nucleotide + protein + stop_codon + back_step_nucleotide + shine_dalgarno
    return protein_on_minus_one_strand[::-1]


# PRE: STRING, INT
# POST: STRING
# APPENDS PROTEIN TO SECOND FRAME ALONG REVERSE STRAND WITH STOP CODON
def append_protein_to_minus_two_frame(protein, frame):
    shine_dalgarno = shine_dalgarno_sequence
    # STEP NUCLEOTIDES ALLOW NAVIGATION BETWEEN FRAMES
    front_step_nucleotide = ""
    back_step_nucleotide = ""
    stop_codon = get_stop_codon()

    # IF ON MINUS ONE OR MINUS THREE FRAME JUMP TO MINUS TWO FRAME USING STEP NUCLEOTIDES
    # IF ON MINUS TWO FRAME RETURN PROTEIN WITH STOP CODON, WITHOUT INVOLVING STEP NUCLEOTIDES
    if frame == -1:
        for i in range(0, 2):
            front_step_nucleotide += str(random.randint(0, 9))
        back_step_nucleotide = str(random.randint(0, 9))
    elif frame == -3:
        for i in range(0, 2):
            back_step_nucleotide += str(random.randint(0, 9))
        front_step_nucleotide = random.randint(0, 9)
        front_step_nucleotide = str(front_step_nucleotide)
    else:
        return (protein + stop_codon)[::-1]

    # RETURN PROTEIN WITH STEP NUCLEOTIDES TO CHANGE FRAME AND STOP CODON APPENDED
    protein_on_minus_one_strand = front_step_nucleotide + protein + stop_codon + back_step_nucleotide + shine_dalgarno
    return protein_on_minus_one_strand[::-1]


# PRE: STRING, INT
# POST: STRING
# APPENDS PROTEIN TO THIRD FRAME ALONG REVERSE STRAND WITH STOP CODON
def append_protein_to_minus_three_frame(protein, frame):
    shine_dalgarno = shine_dalgarno_sequence
    # STEP NUCLEOTIDES ALLOW NAVIGATION BETWEEN FRAMES
    front_step_nucleotide = ""
    back_step_nucleotide = ""
    stop_codon = get_stop_codon()

    # IF ON MINUS ONE OR MINUS TWO FRAME JUMP TO MINUS ONE FRAME USING STEP NUCLEOTIDES
    # IF ON MINUS THREE FRAME RETURN PROTEIN WITH STOP CODON, WITHOUT INVOLVING STEP NUCLEOTIDES
    if frame == -1:
        step_nucleotide = random.randint(0, 9)
        front_step_nucleotide = str(step_nucleotide)
        for i in range(0, 2):
            back_step_nucleotide += str(random.randint(0, 9))
    elif frame == -2:
        for i in range(0, 2):
            front_step_nucleotide += str(random.randint(0, 9))
        back_step_nucleotide = random.randint(0, 9)
    else:
        return (str(protein)+str(stop_codon))[::-1]
    # RETURN PROTEIN WITH STEP NUCLEOTIDES TO CHANGE FRAME AND STOP CODON APPENDED
    protein_on_minus_one_strand = front_step_nucleotide + protein + stop_codon + back_step_nucleotide + shine_dalgarno
    return protein_on_minus_one_strand[::-1]


# PRE: STRING --> Potential Proteins from views.py
# POST: STRING
# READ IN FILE AND CONVERT ALL STRINGS IN FILE TO PROTEIN USING
def main(*args):
    # ALWAYS BEGIN ON FIRST FRAME WHEN CREATING SYNTHETIC GENOME
    frame = 1
    nucleotide_sequence = ""
    num_proteins_added = 0
    # Add every protein in protein list to synthetic genome
    for all_proteins in list(args):
        # CONVERT PROTEIN TO MRNA SEQUENCE THAT WILL BE USED IN GENOME
        for protein in all_proteins:
            # place half of proteins on forward strand and half on reverse strand
            if num_proteins_added < floor(len(all_proteins))/2:
                protein = convert_protein_to_nucleotide_sequence(protein)
                # RANDOMLY CHOOSE WHICH FRAME PROTEIN WILL BE PLACED ON
                frame_to_append_to = random.randint(1, 3)
                # APPEND PROTEIN TO APPROPRIATE FRAME AND CHANGE FRAME ACCORDINGLY
                if frame_to_append_to == 1:
                    nucleotide_sequence += append_protein_to_first_frame(protein, frame)
                    frame = 1
                elif frame_to_append_to == 2:
                    nucleotide_sequence += append_protein_to_second_frame(protein, frame)
                    frame = 2
                elif frame_to_append_to == 3:
                    nucleotide_sequence += append_protein_to_third_frame(protein, frame)
                    frame = 3
            else:
                frame = -1
                protein = convert_protein_to_nucleotide_sequence(protein)
                frame_to_append_to = random.randint(-3, -1)
                if frame_to_append_to == -1:
                    nucleotide_sequence += append_protein_to_minus_one_frame(protein, frame)
                    frame = -1
                elif frame_to_append_to == -2:
                    nucleotide_sequence += append_protein_to_minus_two_frame(protein, frame)
                    frame = -2
                elif frame_to_append_to == -3:
                    nucleotide_sequence += append_protein_to_third_frame(protein, frame)
                    frame = -3
            num_proteins_added += 1
    return nucleotide_sequence
