class ui_helper():

    @staticmethod
    def layout_add(main_layout, layout, *args):
        main_layout.addLayout(layout, *args)
        print('rejilla')
                  

    @staticmethod
    def widget_add(container, widget_list):
        for widget in widget_list:
            container.addWidget(widget)

    @staticmethod
    def populate_menu(item, item_name, actions_dict):
        menu_item = self.menu.addMenu(item_name)
        for key, value in actions_dict.items():
            action = menu_item.addAction(key)
            action.triggered.connect(value)
    
    @staticmethod
    def add_buttons(self ,list):
        for item in range(len(list)):
            print(list[item].name)
            """
            button = QPushButton(list[item].name)
            button.clicked.connect(list[item].TextWriter.escrito)
            button.clicked.connect(lambda: self.text.show())
            self.my_condition_buttons.append(button)
            """

class EnoxDose:

    @staticmethod
    def drug_dose(weight, weight_table, dose_table):
        for index, bracket in enumerate(weight_table):
            if bracket[0] <= weight <= bracket[1]:
                dose = dose_table[index]
                print(dose)
                return(dose)

class IronDoseCalculator():
    
    @staticmethod
    def ganzoni(hb, peso):
        dose = max(500, int((((120 - hb) * peso * 0.24) + 500)))
        print(dose)
        return(dose)

    def iron_man(hb, peso, dose_table, weigh_table):
        
        for index, bracket in enumerate(weigh_table):
            if bracket[0] <= peso <= bracket[1]:
                dose = dose_table[index]
                return dose 

class TextWriter():
    @staticmethod
    def escrito(text_box, dictionary):
        texto = '\n'.join(key + ":\n" + value for key, value in dictionary.items())
        #texto = '\n'.join(key + ":\n" + value for key, value in dictionary)
        text_box.setPlainText(texto)
        for k, v in dictionary.items():
            if k == 'img':
                img = Image.open(v)
                img.show()
            if k == 'website':
                pagina_web = urllib.request.urlopen(v).read()
                text_box.setHtml(pagina_web)
            else:
                pass