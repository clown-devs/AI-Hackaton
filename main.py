import parser.parser as parser

data,header = parser.parse_file('N-1.edf')
parser.save_to_csv(data, header, 'N-1.csv')