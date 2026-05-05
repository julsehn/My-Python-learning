class Edat:
    def __init__ (self, edat):
        self.edat = edat
        self.dia = 0
        self.mes = 0
        self.any = 0000
        self.mesos = ["", "Gener", "Febrer", "Març", "Abril", "Maig", "Juny", "Juliol", "Agost", "Setembre", "Octubre", "Novembre", "Desembre"]
        

    def dia_de_naixement(self):
        return self.dia
    def mes_de_naixement(self):
        return self.mes
    def any_de_naixement(self):
        return self.any
    def data_naixement_str(self):
        return f"{self.dia} de {self.mesos[self.mes]} del {self.any}"
    def introduir_data_naixement(self, dia, mes, any):
        from datetime import date
        import calendar
        data_actual = date.today()
        
        while True:
            try:
                self.any = int(input("Introdueix l'any de naixement: "))
                if self.any < 0 or self.any > date.today().year:
                    print("Any no vàlid. Si us plau, introdueix un any vàlid.")
                    continue
                break
            except ValueError:
                print("Cal introduir un nombre enter vàlid. Torna-ho a provar.")
        
        while True:
            try:
                self.mes = int(input("Introdueix el mes de naixement (1-12): "))
                if self.mes < 1 or self.mes > 12:
                    print("Mes no vàlid. Si us plau, introdueix un mes entre 1 i 12.")
                    continue
                if self.mes > date.today().month and self.any == date.today().year:
                    print("No podeu neixer en el futur.")
                    continue
                break
            except ValueError:
                print("Cal introduir un nombre enter vàlid. Torna-ho a provar.")
        
        while True:
            try:
                self.dia = int(input("Introdueix el dia de naixement: "))
                if self.dia < 1 or self.dia > 31:
                    print("Dia no vàlid. Si us plau, introdueix un dia entre 1 i 31.")
                    continue
                if self.any == date.today().year and self.mes == date.today().month and self.dia > date.today().day:
                    print("No podeu neixer en el futur.")
                    continue
                if self.mes in [4, 6, 9, 11] and self.dia > 30:
                    print(f"El mes {self.mes} només té 30 dies. Si us plau, introdueix un dia vàlid.")
                    continue
                if self.mes in [1, 3, 5, 7, 8, 10, 12] and self.dia > 31:
                    print(f"El mes {self.mes} només té 31 dies. Si us plau, introdueix un dia vàlid.")
                    continue
                if self.mes == 2:
                    max_day = 29 if calendar.isleap(self.any) else 28
                    if self.dia > max_day:
                        print(f"Febrer {self.any} només té {max_day} dies. Si us plau, introdueix un dia vàlid.")
                        continue
                break
            except ValueError:
                print("Cal introduir un nombre enter vàlid. Torna-ho a provar.")

        data_naixement = date(self.any, self.mes, self.dia)
        anys = data_actual.year - data_naixement.year
        mesos = data_actual.month - data_naixement.month
        dies = data_actual.day - data_naixement.day
        
        if mesos < 0:
            anys -= 1
            mesos += 12
        if dies < 0:
            mesos -= 1
            if mesos < 0:
                anys -= 1
                mesos += 12
            prev_month = data_actual.month - 1 if data_actual.month > 1 else 12
            prev_year = data_actual.year if data_actual.month > 1 else data_actual.year - 1
            days_in_prev_month = calendar.monthrange(prev_year, prev_month)[1]
            dies += days_in_prev_month
        
        return anys, mesos, dies
    
if __name__ == "__main__":
    while True:
        persona = Edat(0)
        anys, mesos, dies = persona.introduir_data_naixement(0, 0, 0)
        print(f"Data de naixement: {persona.data_naixement_str()}")
        print(f"L'edat calculada és: {anys} anys, {mesos} mesos i {dies} dies.")
        
        resposta = input("Vols calcular una altra edat? (s/n): ").strip().lower()
        if resposta != 's':
            break