
class A(object):
    #  def __init__(self):
    #     pass

    k = [1,2,3,5,4]
    i=0
    for i in range(len(k)):
        j = 0
        for j in range(i):
            if k[j] > k[j + 1]:
                k[j], k[j + 1] = k[j + 1], k[j]
            i += 1
        j +=1
    print k

    def z(self,a):
        return "z %d"%a

class B(A):
    pass


hh=B()
print hh.z
