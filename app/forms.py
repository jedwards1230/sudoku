from django import forms


class PuzzleForm():
    def __init__(self, puzzle, edits):
        self.formset = []
        l = len(puzzle)
        
        for i, row in enumerate(puzzle):
            self.formset.append('<tr>')
            for j, spot in enumerate(row):
                if edits[i][j] == 1:
                    table_hidden = f'   <input type="hidden" value=\'editable\' name="_{i}_col_{j}">'
                    if spot == 0:
                        table_td = f'   <td><input type="number" min="1" max="{l}" name="form-{i}-col_{j}" value="" required></td>\n'
                    else:
                        table_td = f'   <td><input type="number" min="1" max="{l}" name="form-{i}-col_{j}" value="{spot}" required></td>\n'
                else:
                    table_hidden = f'   <input type="hidden" value=\'\' name="_{i}_col_{j}">'
                    table_td = f'   <td><input type="number" min="1" max="{l}" name="form-{i}-col_{j}" value="{spot}" readonly id="preset" class="preset_value"></td>\n'
                self.formset.append(table_hidden)
                self.formset.append(table_td)
            self.formset.append('</tr>')
        
    def get_formset(self):
        return self.formset
    
    def print_formset(self):
        print(self.formset)