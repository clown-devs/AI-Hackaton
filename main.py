import ai.ai as ai
import parser.parser as parser
import sys


# if len(sys.argv) != 3:
#     print("Usage: python main.py <input_file> <output_file>")
#     sys.exit(1)


# input_file = sys.argv[1]
# output_file = sys.argv[2]
# print(f"Converting {input_file} to {output_file}")

# data, header = parser.parse_file(input_file)
# parser.save_to_csv(data, header, output_file)

data, edf = parser.parse_file("N-1.REC")

res = ai.predict_result(data, "ai/my_model.keras")
#print(res)