import csv

class PartsProcessor:
    def __init__(self, data_base_path=None, csv_file=None, out_dir=None, out_file=None):
        self.data_base_path = data_base_path
        self.csv_file = csv_file
        self.out_dir = out_dir
        self.out_file = out_file
        self.all_parts = set()

    def set(self, data_base_path=None, csv_file=None, out_dir=None, out_file=None):
        self.data_base_path = data_base_path
        self.csv_file = csv_file
        self.out_dir = out_dir
        self.out_file = out_file

    def clear_set(self):
        self.all_parts = set()

    def process_csv(self):
        with open(self.data_base_path + self.csv_file, mode="r") as fh:
            csv_reader = csv.reader(fh, delimiter=',')

            # skip the column names
            next(csv_reader)

            # process each row
            for row in csv_reader:
                # grab the list of parts
                partsID = self.get_parts(row[4])
                # add the parts to the set
                self.all_parts |= set(partsID)
        print(self.all_parts, len(self.all_parts))

    def get_parts(self, in_string: str):
        # probably doable with JSON module but meh
        # need to get rid of the double quotation marks and the square brackets
        # split by comma
        # get rid of quotation in string
        return [part[1:-1] for part in in_string[1:-1].split(", ")]

    def write_parts(self):
        with open(self.out_dir + self.out_file, mode="w") as fh:
            fh.writelines("%s\n" % part for part in self.all_parts)


def main():
    path = '../../../Dataset/Labelling/crowdsourcing-annotations-lego-master/Data/Input/Datasets/Berend/CSV/'
    file_name = 'labelsAll.csv'

    tool = PartsProcessor(path, file_name, './', 'BerendPartsList')
    tool.process_csv()
    tool.write_parts()


if __name__ == "__main__":
    main()