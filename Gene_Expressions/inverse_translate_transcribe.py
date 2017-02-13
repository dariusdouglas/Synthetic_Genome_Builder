genome = "2437667211031378736163240002437660703133112085900893435295999072437664173013036644841072496882599599912" \
         "4376674422467909234530007424376671206198687572390045252993199924376640638140593040012907145284499924376" \
         "6523920794112901744961901999"

sum_to_letter = {1: "q", 2: "j", 3: "v", 4: "p", 5: "g", 6: "w", 7: "u", 8: "l", 9: "r", 10: "s", 11: "i",
                 12: "a",
                 13: "e", 14: "t", 15: "o", 16: "n", 17: "h", 18: "d", 19: "c", 20: "m", 21: "f", 22: "y",
                 23: "b",
                 24: "k", 25: "x", 26: "z"}


def build_transcription_dict():
    """

    :return:
    """
    return {str(i): 9 - i for i in range(1, 10)}


def build_translation_dict():
    """

    :return:
    """
    codon_dictionary = {}
    for i in range(1, 999):
        codon = '{0:03d}'.format(i)
        codon_sum = sum(int(num) for num in codon)
        codon_dictionary[codon] = codon_sum

    return codon_dictionary


def build_start_codon_set():
    """

    :return:
    """
    start_codons = set()
    for number in range(1, 999):
        codon = "{0:03d}".format(number)
        codon_sum = sum(int(num) for num in codon)
        if codon_sum == 10:
            start_codons.add(codon)

    return start_codons


def build_stop_codon_set():
    return set(['000', '999'])


if __name__ == "__main__":
    print(build_start_codon_set())
