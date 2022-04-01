import aprendiz

a1=aprendiz.Aprendiz("cristian","lopez")
a2=aprendiz.Aprendiz("yeily","cupaqui")
a1.mostrarAprendiz()
a2.mostrarAprendiz()

print("total %d",aprendiz.Aprendiz.total)

print(setattr(a1,"edad",8))
print(a1.edad)
a1.edad=18
print(hasattr(a1,"edad"))
print(a1.edad)
print(delattr(a1,"edad"))
print(hasattr(a1,"edad"))
a2.edad=28
print(hasattr(a2,"edad"))
print(a2.edad)
print(delattr(a2,"edad"))
print(hasattr(a1,"edad"))