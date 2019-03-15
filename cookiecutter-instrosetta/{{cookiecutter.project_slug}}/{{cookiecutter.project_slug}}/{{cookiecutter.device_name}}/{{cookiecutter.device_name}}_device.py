
class {{cookiecutter.device_name.split("_")|map("title")|join("")}}Device():
    def __init__(self, *args, **kwargs):
        ''' Default signature to support directly accepting 
            an rpc message content that may include unused arguments.
        '''

    #FIXME: add communication with physical device here
    # Default access pattern is properties.