
class Procedure:
    def __init__(self, name = "", params = {}):
        self._name = name
        self._params = params

class ProcedureResponse:
    def __init__(self, result_fields = {}):
        self._result_fields = result_fields