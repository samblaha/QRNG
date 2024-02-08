from qiskit import QuantumCircuit, Aer, execute
import numpy as np

def generate_random_number(max_val):
    n_qubits = int(np.ceil(np.log2(max_val)))  # Calculate the number of qubits needed
    circuit = QuantumCircuit(n_qubits, n_qubits)
    
    # Apply Hadamard gate to each qubit
    for qubit in range(n_qubits):
        circuit.h(qubit)
    
    # Measure each qubit
    circuit.measure(range(n_qubits), range(n_qubits))
    
    # Execute the circuit
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(circuit, simulator, shots=1)
    result = job.result()
    counts = result.get_counts(circuit)
    
    # Convert the measured binary string to a decimal number
    measured_bin = list(counts.keys())[0]  # Get the binary result
    measured_int = int(measured_bin, 2)  # Convert to integer
    
    # Ensure the result is within the specified range
    if measured_int < max_val:
        return measured_int
    else:
        # Optionally, handle the case where the number is out of range
        return generate_random_number(max_val)  # Recurse until valid

# Example usage
max_val = 1000  # Generate a random number between 0 and 9
random_number = generate_random_number(max_val)
print(f"Random Number: {random_number}")
