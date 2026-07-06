import re


class loadPromptsFromCsv:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path

    def load_prompts(self):
        with open(self.csv_file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        prompts = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]

        return prompts
