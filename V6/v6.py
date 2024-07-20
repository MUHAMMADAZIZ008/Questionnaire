from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QListWidget,
    QSpinBox,
    QComboBox,
    QFormLayout
)

class Questionnaire(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setGeometry(600, 300, 900, 700)
        # self.setFixedSize(750, 600)
        self.setStyleSheet("""background-color: #D6EFD8""")
        self.main_box = QVBoxLayout()
        self.box1 = QHBoxLayout()

        self.film_name = QLineEdit(self)
        self.filim_Lable_n = QLabel("Filim name:")
        self.box1.addWidget(self.filim_Lable_n)
        self.box1.addWidget(self.film_name)

        self.film_janir = QComboBox()
        self.film_janir_j = QLabel("Filim janir:")

        self.filim_year = QSpinBox(self)
        self.filim_year_y = QLabel("The year the film was produced:")

        self.filim_start = QLineEdit(self)
        self.filim_start_t = QLabel("Filim start time:")

        self.filim_search = QPushButton("Search", self)

        self.filim_show = QListWidget(self)
        self.filim_show_w = QLabel("Resault:")


        self.main_box.addLayout(self.filim_Lable_n, self.film_name)
        self.main_box.addRow(self.film_janir_j, self.film_janir)
        self.main_box.addRow(self.filim_year_y, self.filim_year)
        self.main_box.addRow(self.filim_start_t, self.filim_start)
        self.main_box.addRow(self.filim_search)
        self.main_box.addRow(self.filim_show_w, self.filim_show)
        self.setLayout(self.main_box)

        #stayle -->
        #film_name -->
        self.film_name.setFixedHeight(30)
        self.film_name.setStyleSheet("""

            font-size: 100px:
            background-color: #cac8eb;
            border: 0;
        """)
        self.film_name.setPlaceholderText("Filim Name")
        self.filim_Lable_n.setStyleSheet("""
            font-size: 30px;
            color: #1A5319;
            font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
                                                                      
        """)
        #film_name <--

        #filim_janr -->
        self.film_janir_j.setStyleSheet("""
            font-size: 30px;
            color: #1A5319;
            font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
        """)

        self.film_janir.setFixedHeight(40)
        self.film_janir.setStyleSheet("""
            font-size: 100px:
            background-color: #cac8eb;
            border: 0;
            color: 80AF81;
        """)
        self.film_janir.addItems(["Janr", "Militant", "Drama", "Comedy", "Melodrama", "Adventure", "Scary", "Fantastic", "Vital"])

        #filim_janr <--

        #filim_year -->
        self.filim_year_y.setStyleSheet("""
            color: #1A5319;
            font: bold;
            font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
        """)
        self.filim_year.setFixedSize(300, 40)
        self.filim_year.setMaximum(2024)
        self.filim_year.setMinimum(1895)

        self.filim_year.setStyleSheet("""
            font-size: 100px:
            background-color: #80AF81;
            border: 0;
            color: 80AF81;
        """)


        #filim_year <--


        #filim_start -->
        self.filim_start_t.setStyleSheet("""
            font-size: 30px;
            color: #1A5319;
            font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
        """)
        self.filim_start.setFixedSize(300, 40)
        self.filim_start.setPlaceholderText("00:00")

        self.filim_start.setStyleSheet("""
            QLineEdit{
                font-size: 100px:
                background-color: #508D4E;
                color: 80AF81;
                border: 0;
            }
            QLineEdit:focus {
                background-color: #80AF81;
                border: 1px solid #A0A0A0; 
            }
        """)
        #filim_start <--

        #filim_search -->
        self.filim_search.setFixedSize(200, 40)
        self.filim_search.setStyleSheet("""
            QPushButton{
                background-color: #508D4E;
                border: 0;
                color: #fff;
                font-sizi: 100px;
                font: bold;
                font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
                border-radius: 20px;
            }
            QPushButton:hover{
                background-color: #1A5319;
                view-timeline: inherit;
            }
                            
        """)
        #filim_search <--

        #filim_show -->
        self.filim_show.setFixedHeight(350)
        self.filim_show.setStyleSheet("""



            QListWidget {
                padding-left: 10px;
                background-color: #1A5319;
                border: 1px solid #CCC;
                border-radius: 10px;
            }
            QListWidget::item {
                padding: 5px;
                color: #fff;
                font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
            }
            QListWidget::item:selected {
                background-color: #A0A0A0; 
                color: white; 
            }
        """)
        

        self.filim_show_w.setStyleSheet("""
            font-size: 30px;
            color: #1A5319;
            font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
        """)


        #filim_show
        #stayle <---

        self.filim_search.clicked.connect(self.search_click)
    
        self.film_janir.currentTextChanged.connect(self.on_click)
    def on_click(self):
        self.text = self.film_janir.currentText()

    def search_click(self):
        if self.film_name.text() == "":
            self.film_name.setStyleSheet("""

                font-size: 100px:
                background-color: #cac8eb;
                border: 1px solid red;
                """)
        # if self.text == "Janr":
        #     self.film_janir.setStyleSheet("""

        #         font-size: 100px:
        #         background-color: #cac8eb;
        #         border: 1px solid red;
        #         color: 80AF81;
        #     """)
        if self.filim_start.text() == "":
            self.filim_start.setStyleSheet("""
                font-size: 100px:
                background-color: #cac8eb;
                border: 1px solid red;
                color: 80AF81;
            """)




        self.filim_show.clear()
        lst = []
        check_box = True
        with open("V6/cinema.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                date = line.split(",")
                date[-1]= date[-1][1:-1]
                date[1] = date[1][1:]
                date[2] = date[2][1:]
                lst.append(date)          
        for i in range(len(lst)):
            if self.film_name.text() in lst[i] and self.text in lst[i] and self.filim_year.text() in lst[i] and self.filim_start.text() in lst[i]:
                self.filim_show.addItem(f"{i+1} - Filim:")
                self.filim_show.addItem(f"Filim Name: {self.film_name.text()}")
                self.filim_show.addItem(f"Filim Janr: {self.text}")
                self.filim_show.addItem(f"The year the film was produced: {self.filim_year.text()}")
                self.filim_show.addItem(f"Filim start time: {self.filim_start.text()}")
                check_box = False
        if check_box:
            self.filim_show.addItem("No data found")

        # return text




app = QApplication([])

win = Questionnaire()
win.show()
app.exec_()