class loadPromptsFromCsv:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path

    def load_prompts(self):
        prompt = []
        with open (self.csv_file_path, 'r') as file:
            for line in file:
                prompt.append(line.strip())

        return prompt
