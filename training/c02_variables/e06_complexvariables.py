# Complex numbers have a real part and an imaginary part
# The imaginary part comes with a 'j'
num = 123 + 456j
print(type(num), end="\n\n")
print(dir(complex), end="\n\n")

# The real and imag fields could be used to obtain the number in each part
print("Real Part      : ", num.real)
print("Imaginary Part : ", num.imag, end="\n\n")

# Each part of the complex number are float
print("Real Part      : ", type(num.real))
print("Imaginary Part : ", type(num.imag), end="\n\n")
