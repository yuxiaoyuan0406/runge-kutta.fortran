import numpy as np
import matplotlib.pyplot as plt

def read_dat_from_file(file_name):
    data = []
    with open(file_name) as file:
        lines = file.readlines()
        file.close()
    for line in lines:
        val = line.strip().split()
        data.append(float(val[0]))
    return data

# input_dat = open('test_input.dat')
# lines = input_dat.readlines()
# input_dat.close()

# index_raw = []
input_raw = read_dat_from_file('data.txt')

# for line in lines:
#     val = line.strip().split()
#     index_raw.append(int(val[0]))
#     input_raw.append(float(val[1]))
    
# output_dat = open('disp.dat')
# lines = output_dat.readlines()
# output_dat.close()

# output_raw_1 = []

# for line in lines:
#     val = line.strip().split()
#     output_raw_1.append(float(val[1]))

# output_dat = open('disp_2.dat')
# lines = output_dat.readlines()
# output_dat.close()

# output_raw_2 = []

# for line in lines:
#     val = line.strip().split()
#     output_raw_2.append(float(val[1]))

# output_dat = open('disp_4.dat')
# lines = output_dat.readlines()
# output_dat.close()

# output_raw_3 = []

# for line in lines:
#     val = line.strip().split()
#     output_raw_3.append(float(val[1]))

# output = np.array(read_dat_from_file('disp_9.dat'))
# other = np.array(read_dat_from_file('disp_other.txt'))

# t=np.linspace(0.,2.,int(2e6))
# std = 5.314e-12 * np.sin(2*np.pi*50*t)

# output = output[0:500000]
# other = other[0:500000]
# std = std[0:500000]

# diff = output-other
# diff = output-std
# diff2 = other-std

# diff=diff**2
# diff2=diff2**2

# sum1 = np.sum(diff)
# sum2 = np.sum(diff2)
# print(sum1)
# print(sum2)
# print((sum1-sum2)/sum1)



plt.figure()
plt.plot(input_raw, color='blue')
# plt.plot(output_raw_1, color='blue')
# plt.plot(output_raw_2, color='red')
# plt.plot(output_raw_3, color='red')

# plt.plot(output, color='blue')
# plt.plot(other, color='green')
# plt.plot(diff, color='red')
# plt.plot(diff2, color='purple')



plt.grid(True)
plt.show()