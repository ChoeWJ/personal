import inspect
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
class Inspector:
    """A utility class to inspect Python objects."""
    
    @staticmethod
    def get_signature(obj):
        """Get the signature of a function or method."""
        try:
            return inspect.signature(obj)
        except ValueError:
            return "Signature not available for this object."

    @staticmethod
    def get_source(obj):
        """Get the source code of an object."""
        try:
            return inspect.getsource(obj)
        except (OSError, TypeError):
            return "Source code not available."

    @staticmethod
    def get_doc(obj):
        """Get the docstring of an object."""
        return inspect.getdoc(obj) or "No docstring available."

    @staticmethod
    def get_parameters(obj):
        """Get parameters and their details for a callable."""
        try:
            sig = inspect.signature(obj)
            params = []
            for name, param in sig.parameters.items():
                params.append({
                    "name": name,
                    "default": param.default,
                    "kind": param.kind
                })
            return params
        except ValueError:
            return "Parameters not available for this object."

    @staticmethod
    def is_class(obj):
        """Check if the object is a class."""
        return inspect.isclass(obj)

    @staticmethod
    def is_function(obj):
        """Check if the object is a function."""
        return inspect.isfunction(obj)

    @staticmethod
    def is_method(obj):
        """Check if the object is a method."""
        return inspect.ismethod(obj)

    @staticmethod
    def list_methods(obj):
        """List all methods of a class or an instance."""
        if not (inspect.isclass(obj) or hasattr(obj, '__class__')):
            return "The object is not a class or an instance."
        return [method[0] for method in inspect.getmembers(obj, predicate=inspect.ismethod)]

    @staticmethod
    def list_attributes(obj):
        """List all attributes of an object."""
        return dir(obj)
    


inspector = Inspector()



# Signature
print(inspector.get_signature(plt.annotate))