import ml_dtypes as mld 
import numpy as np

HEADER = '''
#include <vector>
#include <string>

namespace TEST_FP8_DATA {
'''

TAILER = '''
}; // END OF TEST_FP8_DATA
'''

def _generate_content(high_precision, low_precision, context = ''):
    input_str = f"const std::vector<float> {context}_INPUT = {{"
    golden_str = f"const std::vector<std::string> {context}_GOLDEN = {{"
    for i in range(high_precision.shape[1]):
        input_str += str(high_precision[0, i]) + ", "
        golden_str += '"' + str(low_precision[0, i]) + '", '
    input_str = input_str[:-2] + "};"
    golden_str = golden_str[:-2] + "};"
    
    return input_str + '\n\n' + golden_str

def generate_code(content, file_path = "float8_test_data.hpp"):
    with open(file_path, "w") as f:
        print(HEADER, file = f)
        print('\n' + content + '\n', file = f)
        print(TAILER, file = f)
    

def generate_fp8_e4m3_golden():
    key = np.random.uniform(low = -448, high = 448, size = (1, 1000)).astype(np.float32)
    value = key.astype(mld.float8_e4m3)
    content = _generate_content(key, value, "FP8_E4M3")
    generate_code(content)

if __name__ == "__main__":
    np.random.seed(1124)
    generate_fp8_e4m3_golden()