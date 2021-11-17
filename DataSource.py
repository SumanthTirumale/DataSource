import sys

# filepath
file_name = "DataSource.txt"


class DataSource:
    """DataSource class to get file data from data source and parse it 
    and return the data in list format by nesting data in dictionary type
    """

    def __init__(self, file_path):
        """Datasource constructor

        Args:
            file_path (str): datasource file path
        """
        self.file_path = file_path
        self.raw_file_data = self.get_file_data()
        self.main_list = self.parse_data()

    def get_file_data(self):
        """Method to get data from file and return it in list data type

        Returns:
            list: raw data
        """
        try:
            with open(self.file_path, 'r') as f:
                return f.readlines()
        except FileNotFoundError:
            print("{} file is not exists !!!".format(self.file_path))
            sys.exit(1)

    def parse_data(self):
        """Method to parse data from datasource

        Returns:
            list: data
        """
        # main list 
        main_list = list()

        # header list 
        # if additional headers added code will automatically add extra key in dictionary
        dictionary_headers = list()

        # loop the raw data 
        for data in self.raw_file_data:
            
            # if dictionary_headers add first loop data as a header data
            if not len(dictionary_headers) > 0:
                # split method returns the data in list format so list extend method is used
                dictionary_headers.extend(data.strip().split("\t"))
            else:
                # create temprovary dictionary to hold the values
                temp_dict = dict()
                for index, dict_head in enumerate(dictionary_headers):
                    
                    # if header column not matching with row print the message and exit the code
                    if len(dictionary_headers) != len(data.strip().split("\t")):
                        print("Header data column is not matching with row data !!! Please check the {} file".format(self.file_path))
                        sys.exit(1)

                    # using list index and value append the keys and values to temp_dict
                    try:
                        temp_dict[dict_head] = data.strip().split("\t")[index]
                    except IndexError:
                        # If header is mentioned and data is not provided then this error handler will handles the error
                        print("{} header data is not available".format(dict_head))
                
                # append the temp_dict values to main_list
                main_list.append(temp_dict)
        # return main_list
        return main_list


list_data = DataSource(file_name).main_list

print(list_data)