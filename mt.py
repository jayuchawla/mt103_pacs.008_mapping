from mt103 import MT103
with open("mt_sample.txt") as f:
    s = f.read()
#print(s)
mt103 = MT103(s)
print("basic header: {}, bank op code: {}, complete message: {}".format(
    mt103.basic_header,
    mt103.text.bank_operation_code,
    mt103
))

print(mt103)