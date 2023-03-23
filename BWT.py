def rotation(x):
    """"Возвращает список всех смен/чередований исходной строки x"""
    x_rotat = x * 2
    return [x_rotat[i:i + len(x)] for i in range(0, len(x))]


def bwm(x):
    """"Возвращает отсортированный в лексичском порядке лист х"""
    return sorted(rotation(x))


def bwt(x):
    """"Возвращает строку отформатированную в bwt"""
    return ''.join(map(lambda x: x[-1], bwm(x)))

print(bwt("CGCTTNCACATTAGGAGAAAATATTGGCAA$"))
# print(rotation("$CGCTTNCACATTAGGAGAAAATATTGGCAA"))
print(bwt("$CGCTTNCACATTAGGAGAAAATATTGGCAA"))
