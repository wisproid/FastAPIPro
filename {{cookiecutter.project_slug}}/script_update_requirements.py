import configparser

def extract_requirements_from_setup_cfg(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)

    requirements = []
    if 'options' in config and 'install_requires' in config['options']:
        requirements = config['options']['install_requires'].strip().split('\n')

    return requirements

def write_requirements_to_txt(requirements, output_path):
    with open(output_path, 'w') as f:
        for requirement in requirements:
            f.write(requirement + '\n')

# Example usage
setup_cfg_path = 'setup.cfg'
requirements_txt_path = 'requirements.txt'

requirements = extract_requirements_from_setup_cfg(setup_cfg_path)
write_requirements_to_txt(requirements, requirements_txt_path)

print(f'Requirements have been exported to {requirements_txt_path}')