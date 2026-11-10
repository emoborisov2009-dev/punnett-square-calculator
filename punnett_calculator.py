while True:

    q = input("Enter the allele names for individual 1: ")
    z = input("Enter the allele names for individual 2: ")

    if q.lower() == "exit" or z.lower() == "exit":
        print("Thank you for using the Punnett Square Calculator!")
        break

    if not q.isascii() or not z.isascii() or not q.isalpha() or not z.isalpha():
        print("Please use English letters only")
        continue

    if len(q) != 2 or len(z) != 2:
        print("Each individual must have exactly two alleles")
        continue

    if q[0].lower() != q[1].lower():
        print("The allele names do not match")
        continue

    if z[0].lower() != z[1].lower():
        print("The allele names do not match")
        continue

    if q[0].lower() != z[0].lower():
        print("The allele names must be the same for both individuals")
        continue

    if q[0].islower() and q[1].isupper():
        print("Write the dominant allele first")
        continue

    if z[0].islower() and z[1].isupper():
        print("Write the dominant allele first")
        continue

    phenotype = 0

    homozygous_dominant = 0
    heterozygous = 0
    homozygous_recessive = 0

    count_orders = 0

    for allele1 in q:
        for allele2 in z:

            count_orders += 1

            if allele1.isupper():
                order = allele1 + allele2
            else:
                order = allele2 + allele1

            if order[0].isupper():
                phenotype += 1

            if order.isupper():
                homozygous_dominant += 1

            elif order.islower():
                homozygous_recessive += 1

            else:
                heterozygous += 1

    print("\nCROSS SUMMARY")
    print("     ------------------------------")
    print("Parent 1: ",q)
    print("Parent 2: ",z)
    print()
    print("Possible offspring",count_orders)
    print()
    print("Dominant phenotype: ",phenotype)
    print("Recessive phenotype: ",count_orders - phenotype)
    print()
    print("Genotype distribution:")
    print()
    print("Homozygous dominant: ", homozygous_dominant)
    print("Heterozygous: ", heterozygous)
    print("Homozygous recessive: ", homozygous_recessive)


    print("\nPUNNETT SQUARE")
    print(f"Cross: {q} x {z}\n")

    print(f"       {z[0]}     {z[1]}")
    print("     ━━━━━━━━━━━")

    for allele1 in q:
        print(f"  {allele1}  ┃", end=" ")

        for allele2 in z:

            if allele1.isupper():
                offspring = allele1 + allele2
            else:
                offspring = allele2 + allele1

            print(f"{offspring:^5}", end=" ")

        print()

        print("     ━━━━━━━━━━━")

