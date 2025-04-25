# import qulacs
# from qulacs_core import QuantumStateGpu
#
# from tequila import TequilaException
# from tequila.simulators.simulator_qulacs import BackendCircuitQulacs, BackendExpectationValueQulacs
#
#
# class TequilaQulacsGpuException(TequilaException):
#     def __str__(self):
#         return "Error in qulacs gpu backend:" + self.message
#
#
# class BackendCircuitQulacsGpu(BackendCircuitQulacs):
#     quantum_state_class = QuantumStateGpu
#
#
# class BackendExpectationValueQulacsGpu(BackendExpectationValueQulacs):
#     BackendCircuitType = BackendCircuitQulacsGpu
#     pass

from tequila.simulators.simulator_base import BackendExpectationValue

class FQE(BackendExpectationValue):
    ExpValueType = None

    def __init__(self, expval, *args, **kwargs):
        self.HH = kwargs["FH"]
        self.wfn = kwargs["wfn"]
        self.UU = kwargs["FU"]
        self.vv = kwargs["vnames"]


    def __call__(self, variables, *args, **kwargs):
        variables = [variables[v] for v in self.vv]
        wfn = self.wfn
        for i, g in enumerate(self.UU):
            wfn = wfn.time_evolve(-0.5 * variables[i], g)
        energy = wfn.expectationValue(self.HH)
        return energy

    def extract_variables(self):
        return self.vv
