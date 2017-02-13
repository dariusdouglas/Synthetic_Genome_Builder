'''
@author: Darius
TESTS TO CHECK WHICH PROTEINS ARE ON A PARTICULAR STRAND
TO TEST FOR PROTEINS WITHOUT SPECIFYING A STRAND, USE REVERSE_FORWARD_TESTING_GENOME.PY
'''

# SYNTHETIC GENOME
scrambled_genome = \
    "2437667211031378736163240002437660703133112085900893435295999072437664173013036644841072496882599599912" \
    "4376674422467909234530007424376671206198687572390045252993199924376640638140593040012907145284499924376" \
    "652392079411290174496190999"

sum_to_letter = {1: 'q', 2: 'j', 3: 'v', 4: 'p', 5: 'g', 6: 'w', 7: 'u', 8: 'l', 9: 'r', 10: 's', 11: 'i', 12: 'a', 13:
                 'e', 14: 't', 15: 'o', 16: 'n', 17: 'h', 18: 'd', 19: 'c', 20: 'm', 21: 'f', 22: 'y', 23: 'b', 24: 'k', 25: 'x',
                 26: 'z'}


# PRE: LIST OF INTS
# POST: NUM CONSISTING OF ALL NUMBERS IN LIST
def list_to_int(numList):
    num = ''.join(map(str, numList))
    return int(num)


# Finds the compliment of any numbers entered (what makes the number 9)
# PRE: STRING
# POST: STRING
# EXAMPLE: INPUT OF 5 returns 4
# EXAMPLE: INPUT OF 7 returns 2
# TRANSCRIPTION FUNCTION
def transcribe(genome):
    mRNA = []
    genome = str(genome)
    # FIND COMPLEMENT OF ALL NUMBERS
    for gene in genome:
        gene = int(gene)
        mRNA += str(9 - gene)
    return mRNA


# finds all start codons (codons that add up to 10)
# Pre: list of ints
# post: all codons in given frame where sum is 10
# EXAMPLE: 316 IS CAPTURED
# EXAMPLE: 550 IS CAPTURED
# EXAMPLE 910 IS CAPTURED
def find_start_codon(strand_5_to_3, frame):
    # STRAND REFERS TO A SECTION OF THE SYNTHETIC GENOME
    segments_in_strand = []
    strand_5_to_3 = str(strand_5_to_3)
    start_codon = 10
    frame_index = 0
    all_start_codons = []
    index = 0
    neg = False

    # CONVERT EACH CODON IN STRAND (SECTION OF GENOME) TO STRING
    for segment in strand_5_to_3:
        segments_in_strand += str(segment)

    if frame > 0 and frame <= 3:
        frame_index = frame - 1

    # CHECK IF FRAME IS NEGATIVE
    # REVERSE STRAND IF IT'S NEGATIVE
    if frame < 0 and frame >= -3:
        neg = True
        segments_in_strand.reverse()
        if frame == -1:
            frame = 1
        if frame == -2:
            frame = 2
        if frame == -3:
            frame = 3

    # WHILE ENTIRE STRAND HAS NOT BEEN CHECKED
    # CAPTURE NEXT 3 CODONS AND SEE IF THEY SUM TO 10--> MAKING THEM A START CODON
    while index < len(strand_5_to_3):
        for segment in segments_in_strand:
            current_frame = segments_in_strand[frame_index: frame_index + 3]
            if len(current_frame) == 3:
                if int(current_frame[0]) + int(current_frame[1]) + int(current_frame[2]) == start_codon and not neg:
                    all_start_codons += current_frame
                    print("start 5' to 3': " + str(current_frame) + "beginning at index " + str(index))
                else:
                    if int(current_frame[0]) + int(current_frame[1]) + int(current_frame[2]) == start_codon:
                        all_start_codons += current_frame
                        print("start 3' to 5' backward: " + str(current_frame) + "beginning at index " + str(index))
                index += 3
                frame_index += 3
        index += 1
    return all_start_codons


# finds all stop codons (codons that add up to 0 or 27)
# Pre: list of ints
# post: all codons in given frame where sum is 0 or 27
# EXAMPLE: 000 IS CAPTURED
# EXAMPLE: 999 IS CAPTURED
def find_stop_codons(strand_5_to_3, frame):
    segments_in_strand = []
    strand_5_to_3 = str(strand_5_to_3)
    stop_codon = [0, 27]
    frame_index = 0
    all_stop_codons = []
    index = 0
    neg = False

    for segment in strand_5_to_3:
        segments_in_strand += str(segment)

    # CHECK IF ON FORWARD OR REVERSE STRAND
    # IF ON A NEGATIVE FRAME, REVERSE AND GO TO FIRST FRAME
    if 0 < frame <= 3:
        frame_index = frame - 1
    if 0 > frame >= -3:
        neg = True
        segments_in_strand.reverse()
        if frame == -1:
            frame = 1
        if frame == -2:
            frame = 2
        if frame == -3:
            frame = 3

    # WHILE ENTIRE STRAND HAS NOT BEEN CHECKED
    # STEP THROUGH SEQUENCE AND CAPTURE 3 CODONS TO SEE IF THEY SUM TO 10--> MAKING THEM A START CODON
    while index < len(strand_5_to_3):
        for segment in segments_in_strand:
            current_frame = segments_in_strand[frame_index: frame_index + 3]
            if len(current_frame) == 3:
                if int(current_frame[0]) + int(current_frame[1]) + int(current_frame[2]) == stop_codon[0] and not neg \
                        or int(current_frame[0]) + int(current_frame[1]) + int(current_frame[2]) == stop_codon[
                            1] and not neg:
                    all_stop_codons += current_frame
                    print("Stop 5' to 3': " + str(current_frame) + "beginning at index " + str(index))

                else:
                    if int(current_frame[0]) + int(current_frame[1]) + int(current_frame[2]) == stop_codon[0] \
                            or int(current_frame[0]) + int(current_frame[1]) + int(current_frame[2]) == stop_codon[1]:
                        all_stop_codons += current_frame
                        print("Stop 3' to 5' backward: " + str(current_frame) + "beginning at index " + str(index))
                index += 3
                frame_index += 3
        index += 1
    return all_stop_codons


# READ ALL NUCLEOTIDES ON FRAME
# gets sum of codons in given frame
# PRE: STRING, INT
# post: STRING
def get_frame(genome, frame):
    parts_of_genome = []
    genome = str(genome)
    frame_number = 1
    index = 0
    frame_index = 0
    all_letters = []

    for part in genome:
        parts_of_genome += part

    # CHECK IF ON FORWARD OR REVERSE STRAND
    # IF ON REVERSE STRAND, REVERSE NUCLEOTIDE SEQUENCE
    if 0 < frame <= 3:
        frame_index = frame - 1
    if 0 > frame >= -3:
        parts_of_genome.reverse()
        if frame == -1:
            frame = 1
        if frame == -2:
            frame = 2
        if frame == -3:
            frame = 3

    # find sum of every codon and add it to amino acid sequence
    # check entire sequence in codons (groups of 3)
    while index < len(genome):
        current_frame = parts_of_genome[frame_index: frame_index + 3]

        # only check groups of 3 to avoid index out of bounds error
        if len(current_frame) == 3:
            protein_code = int(current_frame[0]) + int(current_frame[1]) + int(current_frame[2])
            all_letters += translate(protein_code)
        else:
            break

        frame_index += 3
        index += 1
        frame_number += 1

    all_letters = ''.join(all_letters)

    return all_letters


# PRINT AMINO ACID SEQUENCE BASED ON FRAME
# PRE: STRING, INT
# POST: STRING (PRINTED OUTPUT FOR TESTING)
def to_string(genome, frame):
    all_words = []
    word = []
    letters = get_frame(genome, frame)
    stop_codon_found = False

    # IF A S IS FOUND, BEGIN PRINTING UNTIL A STOP CODON IS FOUND
    for letter in letters:
        if letter is 's':
            word += letter
            stop_codon_found = False
        elif letter is '\n':
            all_words.append(word)
            word = ""
            stop_codon_found = True
        elif stop_codon_found is False:
            word += letter
    for word in all_words:
        print(word)


# finds letter in list that corresponds to given number
# pre: string
# post: string
# 10 returns s
# 000 or 27 return ::
# 8 returns l
def translate(genome):
    proteins = ""
    if genome == 0 or genome == 27:
        proteins += "\n"
    else:
        proteins += sum_to_letter[genome]
    proteins = ''.join(proteins)
    proteins = proteins[::-1]
    return proteins


# TEST
# PRINT ALL PROTEINS ON SPECIFIED FRAME
for frame in range(1, 3):
    print("Frame " + str(frame))
    print(to_string(scrambled_genome, frame))
    print("here")
