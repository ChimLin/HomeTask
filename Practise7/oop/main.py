from Spec import *
man1 = Man("Иван",1990,40000)
man2 = Man("Петр",1992,70000)
man3 = Man("Алексей",1995,90000)

# man1.set("Иван",1990)
# man2.set("Петр",1992)
# man3.set("Алексей",1995)

men = [man1,man2,man3]
for man in men:
    man.show_info()

