import parser.parser as parser

data, header = parser.parse_file('N-2.edf')
parser.save_to_csv(data, header, 'N-2.csv')