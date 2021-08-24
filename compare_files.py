import filecmp

f1 = open("C:\\FoxQuilt\\Development\\foxcom-forms-backend\\src\\context\\mongodb.ts")
f2 = open("C:\\FoxQuilt\\Development\\foxcom-payment-backend\\src\\context\\mongodb.ts")
for line1 in f1:
    for line2 in f2:
        if line1 == line2:
            print(line1)