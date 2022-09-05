from thingsboard_gateway.connectors.converter import Converter, log    # Import base class for the converter and log ("converter.log" in logs directory).


class CustomSerialUplinkConverter(Converter):    # Definition of class.
    def __init__(self, config):    # Initialization method
        self.__config = config    # Saving configuration to object variable
        self.result_dict = {
            'deviceName': config.get('name', 'CustomSerialDevice'),
            'deviceType': config.get('deviceType', 'default'),
            'attributes': [],
            'telemetry': []
        }    # template for a result dictionary.
    def convert(self, config, data: bytes):    # Method for conversion data from device format to ThingsBoard format.
        keys = ['attributes', 'telemetry']    # Array used for looking data for data processing.
        for key in keys:    # Data processing loop for parameters in keys array.
            self.result_dict[key] = []    # Clean old data.
            if self.__config.get(key) is not None:    # Checking the parameter from the keys in the config.
                for config_object in self.__config.get(key):    # The loop for checking whether there is data that interests us.
                    data_to_convert = data    # data for conversion.
                    if config_object.get('delimiter') is not None:    # Checking some parameter from configuration file.
                        index = config_object.get('position');
                        data_to_convert = data.split(config_object.get('delimiter').encode('UTF-8'))[index]


                    # if config_object.get('untilDelimiter') is not None:    # Checking some parameter from configuration file.
                    #     data_to_convert = data.split(config_object.get('untilDelimiter').encode('UTF-8'))[0]    # if "utilDelimiter" parameter in configuration file - get data from incoming data to delimiter position in received string.
                    # if config_object.get('fromDelimiter') is not None:    # Checking some parameter from configuration file.
                    #     data_to_convert = data.split(config_object.get('fromDelimiter').encode('UTF-8'))[1]    # if "fromDelimiter" parameter in configuration file - get data from incoming data from delimiter position in received string.
                    # if config_object.get('toByte') is not None:    # Checking some parameter from configuration file.
                    #     to_byte = config_object.get('toByte')    #     # if "toByte" parameter in configuration file - get data from incoming data to byte number from a parameter "toByte" in configuration file.
                    #     if to_byte == -1:    # Checking some parameter from configuration file.
                    #         to_byte = len(data) - 1    # If parameter == -1 - we will take data to the end.
                    #     data_to_convert = data_to_convert[:to_byte]    # saving data to variable for sending
                    # if config_object.get('fromByte') is not None:    # Checking some parameter from configuration file
                    #     from_byte = config_object.get('fromByte')    # if "fromByte" parameter in configuration file - get data from incoming data from byte number from a parameter "fromByte" in configuration file.
                    #     data_to_convert = data_to_convert[from_byte:]    # saving data to variable for sending.
                    converted_data = {config_object['key']: data_to_convert.decode('UTF-8')}    # Adding data from temporary variable to result string.
                    self.result_dict[key].append(converted_data)    # Append result string to result dictionary.
        return self.result_dict    # returning result dictionary after all iterations.