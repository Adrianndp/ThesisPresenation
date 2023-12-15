from ThesisPresenation.main.logic.predefined_functions import PredefinedFunctions
import inspect


def get_predefined_functions():
    my_instance = PredefinedFunctions()
    all_functions_names = [
        method for method in dir(my_instance) if
        callable(getattr(my_instance, method)) and not method.startswith("__")
    ]
    all_functions = []
    for func_name in all_functions_names:
        func = getattr(my_instance, func_name)
        signature = inspect.signature(func)
        params_and_types = [(param.name, param.annotation) for param in signature.parameters.values()]
        params_str = ", ".join([f" {name} : {str(type_).replace('typing.', '')} " for name, type_ in params_and_types])
        function_str = f"{func_name}({params_str})"
        all_functions.append(function_str)
    return all_functions
