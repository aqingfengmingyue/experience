import numpy as np
from topsis import Topsis
import time


decision_matrix = np.array([
                            [0.73684211, 0.79166667, 0.03239623],
                            [0.63157895, 0.73076923, 0.02251314],
                            [0.57894737, 0.7037037,  0.01824300],
                            [0.31578947, 0.59375,    0.0115149 ],
                            [0.68421053, 0.76,       0.03377235],
                            [0.52631579, 0.67857143, 0.01949634],
                            [0.47368421, 0.65517241, 0.01792254],
                            [0.47368421, 0.65517241, 0.01831473],
                            [0.68421053, 0.76,       0.03745517],
                            [0.57894737, 0.7037037,  0.01705948],
                            [0.52631579, 0.67857143, 0.02621178],
                            [0.68421053, 0.76,       0.0332154 ],
                            [0.63157895, 0.73076923, 0.0224199 ],
                            [0.52631579, 0.67857143, 0.01500321],
                            [0.52631579, 0.67857143, 0.01308448],
                            [0.57894737, 0.7037037,  0.0357704 ],
                            [0.47368421, 0.65517241, 0.01399121],
                            [0.73684211, 0.79166667, 0.04234935],
                            [0.42105263, 0.63333333, 0.01635592],
                            [0.57894737, 0.7037037,  0.03244264],
                            ])
print(decision_matrix)
start_time = time.time()

weights = [1, 1, 1]
criteria = np.array([True, True, True])
t = Topsis(decision_matrix, weights, criteria, normalization=False)
t.calc()
un_nl = t.calc()
print(un_nl, '\n\n')
t = Topsis(decision_matrix, weights, criteria, normalization=True)
t.calc()
nl = t.calc()
print(nl, '\n\n')
un_nl_TOPSISI_array_keys = np.array(list(un_nl.keys()))
nl_TOPSISI_array_keys = np.array(list(nl.keys()))
un_nl_compare = np.column_stack((un_nl_TOPSISI_array_keys, nl_TOPSISI_array_keys))
print(un_nl_compare)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"代码运行时间: {elapsed_time} 秒")