from abc import ABCMeta, abstractmethod
from abstract_data_cleaner import DataCleaner
from chunk_parser import ChunkParser
import dc_util
from nltk.corpus import conll2000


class Edx(DataCleaner):
    def __init__(self,
                 binary=False,
                 collapse_numbers=False,
                 extract_noun_phrases=False,
                 upweight_first_sentence=False):
        self.binary = binary
        self.collapse_numbers = collapse_numbers
        self.extract_noun_phrases = extract_noun_phrases
        self.upweight_first_sentence = upweight_first_sentence
        train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
        self.chunker = ChunkParser(train_sents)

    @abstractmethod
    def labels(self):
        pass

    def process_doc(self, document):
        document = document.lower()
        if self.collapse_numbers:
            document = dc_util.collapse_numbers(document)
        if self.extract_noun_phrases:
            document = dc_util.extract_noun_phrases(document, self.chunker)
        if self.upweight_first_sentence:
            document = dc_util.upweight_first_sentence(document)
        return document

	@abstractmethod
	def process_records(self, records):	
		pass
