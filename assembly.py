
class kmer_assembler:
    def __init__(self, kmer_fasta_input_path):
        self.input_file_path = kmer_fasta_input_path
        # the overhang we are currently using
        self.current_k = 1
        self.kmer_fasta_as_list = self._init_kmer_fasta_as_list()
        self.kmer_name_to_kmer_seq_dict = self._init_kmer_name_to_kmer_seq_dict()
        self._check_current_kmer_list_is_unique()


    def _init_kmer_fasta_as_list(self):
        """read in the kmer file and have each line as an item in the list"""
        with open(self.input_file_path, 'r') as f:
            kmer_fasta_as_list = [line.rstrip() for line in f]
        return kmer_fasta_as_list

    def _init_kmer_name_to_kmer_seq_dict(self):
        # create a dictionary where key is name of kmer and value is actual kmer sequence
        kmer_name_to_kmer_seq_dict = {}
        for i in range(0, len(self.kmer_fasta_as_list), 2):
            kmer_name_to_kmer_seq_dict[self.kmer_fasta_as_list[i][1:]] = self.kmer_fasta_as_list[1 + 1]
    
    def _check_current_kmer_list_is_unique(self):
        # check current kmer list is unique
        list_of_kmer_sequences = list(kmer_name_to_kmer_seq_dict.values())
        if len(list_of_kmer_sequences) != len(set(list_of_kmer_sequences)):
            raise RuntimeError('kmers contains multiple entries of kmer')
        else:
            pass


#TODO consider if each kmer can be used more than once?