def cut_file_in_quarters(input_file, output_file):
    try:
        with open(input_file, 'rb') as f:
            data = f.read()

        quarter_length = len(data) // 9
        truncated_data = data[:quarter_length]

        with open(output_file, 'wb') as f:
            f.write(truncated_data)

        print(f"File {input_file} was successfully cut to a quarter and saved as {output_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Использование функции
# input_file = 'N-1.REC'
# output_file = 'output.REC'
# cut_file_in_quarters(input_file, output_file)
