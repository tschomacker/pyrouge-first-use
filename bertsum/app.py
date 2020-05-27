from pyrouge import Rouge155

r = Rouge155()
r.system_dir = 'system/'
r.model_dir = 'model/'

r.system_filename_pattern = 'cnndm_step(\d+).candidate'
r.model_filename_pattern = 'cnndm_step#ID#.gold'

output = r.convert_and_evaluate()
print(output)
output_dict = r.output_to_dict(output)