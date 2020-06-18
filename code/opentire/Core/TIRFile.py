from __future__ import print_function

__author__ = 'henningo'

from opentire import OpenTire
import os

class TIRFile():

    def __init__(self, *args, **kwargs):
        self.template_file = 'TIR'
        self.tire_model = None
        self.Coefficients = dict()
        self.Descriptions = dict()
        self.Comments = ""

    def load(self, fname, output=False):

        # Load a TIR-file and build a dictionary of parameters
        f = open(fname, 'r')
        tir_data = f.readlines()
        f.close()

        for line in tir_data:
            if "=" in line:  # This means we have a parameter on the line
                name, value, description = self.ProcessParameterLine(line)
                self.Coefficients[name] = value
                self.Descriptions[name] = description

            elif "!" in line: # This we have a comment
                self.Comments += line


        if output is True:
            print(self.Comments)
            print(self.Coefficients)

        # Create the model based on type in TIR file
        opentire = OpenTire()
        self.Coefficients['PROPERTY_FILE_FORMAT'] = self.Coefficients['PROPERTY_FILE_FORMAT'].replace("'", "")
        print(self.Coefficients['PROPERTY_FILE_FORMAT'])
        tm = opentire.createmodel(self.Coefficients['PROPERTY_FILE_FORMAT'])
        print(tm)

        if tm == None:
            print("Model could not be recognized")
            return None

        # Assign parameters to the model
        for parameter_name in self.Coefficients:  # Loop over the parameters we found

            if parameter_name in tm.Coefficients:  # See if it exists in tire model
                tm.Coefficients[parameter_name] = float(self.Coefficients[parameter_name])  # Assign the value

            else:
                if output is True:
                    print("Could not map parameter: " + str(parameter_name))

        return tm

    def ProcessParameterLine(self, linedata):

        parameter_name = "Parameter"
        parameter_value = "0.0"
        parameter_description = "No Description Available"

        # We need to extract the parameter name, the value and the description
        linedata = linedata.split("=")
        parameter_name = linedata[0]

        if "$" in linedata[1]:  # Means we have a comment
            parameter_value = linedata[1].split("$")[0]
            parameter_description = linedata[1].split("$")[1]

        else:
            parameter_value = linedata[1]

        # Return line data with leading/trailing spaces "stripped" (.strip())
        return parameter_name.strip(), parameter_value.strip(), parameter_description.strip()

    def save(self, tire_model, fname, overwrite_file=True):

        if overwrite_file is True:  # This means we need to start from a template

            # Find what type of tire model
            model_type = tire_model.ModelInfo['Name']
            subfolder = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
            template_filename = subfolder + '\\Templates\\' + model_type + '.tir'
            print("Using TIR template")

        else:  # Load the resulting file
            # TODO: check if it is a real TIR file
            template_filename = fname

        # Load a TIR-file and build a dictionary of parameters
        f = open(template_filename, 'r')
        tir_data = f.readlines()
        print(len(tir_data))
        f.close()

        f = open(fname, 'wb')

        for line in tir_data:
            if "=" in line:  # This means we have a parameter on the line
                name, value, description = self.ProcessParameterLine(line)
                if name in tire_model.Coefficients:
                    value = tire_model.Coefficients[name]

                    # Then we have to re-create the line, using somewhat standard TIR layout
                    new_line = name.ljust(25) + '= ' + str(value)
                    new_line = new_line.ljust(50) + '$' + description + '\n'

                    f.writelines(new_line)

                else: # We should probably write this line as well, even though we don't have this coefficient
                    f.writelines(line)

            else: # This means it is a normal line, we will write it
                    f.writelines(line)
        f.close()
