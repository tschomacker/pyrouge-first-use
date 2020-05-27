from pyrouge import Rouge155

r = Rouge155()
r.system_dir = 'system/'
r.model_dir = 'C:\Users\Thorben\Desktop/pyrouge/model/'
r.system_filename_pattern = 's_sum.(\d+).txt'
r.model_filename_pattern = 'm_sum.#ID#.txt'

output = r.convert_and_evaluate()
print(output)
output_dict = r.output_to_dict(output)