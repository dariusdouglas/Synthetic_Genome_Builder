import re

'''
Finds all proteins on forward and reverse strand on synthetic genome
To search for proteins on a particular frame, use tests in Genome_Test_Functions.py
'''

# genome to test
scrambled_genome = "853820299010315606484453330004853820118022582961023913000853820773250132927758120391439992853820999101958668698322160002"

numNucleotideTypes = 9
codonLength = 3

# all possible starts in sequence
# 's' which corresponds to 10, is the first letter in all synthetic proteins, so all possible starts must sum to 10
possibleStarts = '019|028|037|046|055|064|073|082|091|109|118|127|136|145|154|163|172|181|190|208|217|226|235|244|' \
                 '253|262|271|280|307|316|325|334|343|352|361|370|406|415|424|433|442|451|460|505|514|523|532|541|' \
                 '550|604|613|622|631|640|703|712|721|730|802|811|820|901|910'

possibleStops = '000|999'

codonMap = {1: 'q', 2: 'j', 3: 'v',
            4: 'p', 5: 'g', 6: 'w',
            7: 'u', 8: 'l', 9: 'r',
            10: 's', 11: 'i', 12: 'a',
            13: 'e', 14: 't', 15: 'o',
            16: 'n', 17: 'h', 18: 'd',
            19: 'c', 20: 'm', 21: 'f',
            22: 'y', 23: 'b', 24: 'k',
            25: 'x', 26: 'z', 0: '', 27: ''}

# All frames to be checked
transcript_with_frames = {'1': [], '2': [], '3': [], '-1': [], '-2': [], '-3': []}


# translates a strand of dna/genome into all frames
# input is a dna string (number string)
# output is a list of the first possible protein encoded in each frame (frames not labelled)
def translate_DNA_to_protein_all_possible_frames(strandDNA):
    # read forward strand
    test_regex_iter_all(strandDNA, '+')
    reverseComplement = reverse_complement(strandDNA)
    # read reverse strand
    test_regex_iter_all(reverseComplement, '-')
    proteinsList = []
    for frame in transcript_with_frames:
        for l in transcript_with_frames[frame]:
            temp = proteinify(l)
            proteinsList.append(temp)
            print(temp)


# PRE: String, String
# Plus is '+' if reading on forward strand
# Plus is '-' if reading on minus strand
def test_regex_iter_all(genome, plus):
    global transcript_with_frames
    starts = []
    stops = []

    # find all possible starts in genome by matching genome values with all possibleStarts values
    for codon in re.finditer(possibleStarts, genome):
        starts.append(codon.start())

    # find all possible stops in genome by matching genome values with all possibleStops values
    for codon in re.finditer(possibleStops, genome):
        stops.append(codon.start())

    # search genome beginning at all starts

    numStops = len(stops)
    for start in starts:
        foundStop = False
        stopIter = 0
        while foundStop is False:
            # if stop appears after current start
            if stops[stopIter] > start and stops[stopIter] % codonLength == start % codonLength:
                if plus == '+':
                    transcript_with_frames[str(start % 3 + 1)].append(genome[start:stops[stopIter]])
                else:
                    transcript_with_frames['-' + str(start % 3 + 1)].append(genome[start:stops[stopIter]])
                foundStop = True
            # next stop
            stopIter = stopIter + 1
            if stopIter == numStops - 1:
                foundStop = True


# PRE: String
# POST: list of all six frames
def load_frames(strandDNA):
    retFrames = []
    for codon in range(codonLength):
        retFrames.append(strandDNA[codon:len(strandDNA)])
    reverseComplement = reverse_complement(strandDNA)
    for frame in range(codonLength):
        retFrames.append(reverseComplement[frame:len(reverseComplement)])
    return retFrames


# transcribes a strand regardless of orientation into its RNA complement
# input is a string dna
# output is a string rna
def RNAify(strandDNA):
    RNAifiedStrand = ''
    for segment in strandDNA:
        tempNucleotide = abs(int(segment) - numNucleotideTypes)
        RNAifiedStrand += str(tempNucleotide)
    return RNAifiedStrand


# finds the reverse complement of a Strand of DNA
# input is a string dna
# output is a string dna, reveresed and complemented
def reverse_complement(strandDNA):
    reverseComplement = ''
    for segment in strandDNA:
        tempNucleotide = abs(int(segment) - numNucleotideTypes)
        reverseComplement += str(tempNucleotide)
    reverseComplement = reverseComplement[::-1]
    return reverseComplement


# transcribes a strand of RNA into protein
# input is a string rna
# output is string polypeptide
def proteinify(strandRNA):
    tempCodon = 0
    polypeptide = ''

    # reading from 3' end
    while len(strandRNA) % codonLength != 0:
        strandRNA = strandRNA[0:-1]

    # turning mRNA to protein
    for n in range(0, len(strandRNA), codonLength):
        for k in range(codonLength):
            tempCodon = tempCodon + int(strandRNA[n + k])
        polypeptide += codonMap[tempCodon]
        tempCodon = 0
    return polypeptide


# find proteins on synthetic genome
translate_DNA_to_protein_all_possible_frames((scrambled_genome))
