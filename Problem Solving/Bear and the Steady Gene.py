def steadyGene(gene):
    dic = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for i in gene:
        dic[i] += 1
    x = len(gene)
    factor = x / 4

    if dic['A'] == factor and dic['T'] == factor and dic['C'] ==factor and dic['G'] == factor:
        return 0

    upper = 0
    lower = 0
    minlen = x
    while upper < x and lower < x:
        while (dic['A'] > factor or dic['C'] > factor or dic['T'] > factor or dic['G'] > factor) and upper < x:
            dic[gene[upper]] -= 1
            upper += 1
            # print(dic,'Im dic in first while')
        while dic['A'] <= factor and dic['C'] <= factor and dic['T'] <= factor and dic['G'] <= factor:
            dic[gene[lower]] += 1
            lower += 1
            # print(dic, 'Im dic in second while')
        if upper - lower < minlen:
            minlen = upper - lower + 1
    return minlen





t= int(input())

s= input()
print(steadyGene(s))
