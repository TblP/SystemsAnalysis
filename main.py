import PySimpleGUI as sg
from Solution import Solution_scipy, Solution_algo

sg.theme('BrownBlue')

TEXT = "Для производства двух видов изделий А и В используются три типа технологического оборудования.\n"\
"На производство единицы изделия А оборудования I типа используется 3, II типа – 4, оборудование III типа – 5 ч.\n"\
"На производство единицы продукции В соответственно 6, 3 и 2 ч.\n"\
"На производство всех изделий предприятие может представить оборудование I типа не более чем на 102,\n" \
"II типа – не более чем на 91 с, III типа – не более nчем на 105 ч.\n"\
"Прибыль от реализации единицы изделия А составляет 7 руб., а от изделия В 9 руб.\n"\
"Составить план производства изделий А и В, обеспечивающий максимальную прибыль от их реализации."\

col = [[sg.Text('Тип оборудования', text_color='white', background_color='#879BEC'),
        sg.Text('Затраты времени (станко - ч) на обработку одного \n изделия вида', text_color='white',
                background_color='#879BEC'),
        sg.Text('Общий кол-во \nрабочего \nвремени \nоборудования (ч)', text_color='white', background_color='#879BEC')],
       [sg.Text(f"{' ' * 45}A{' ' * 37}B{' ' * 12}", text_color='white', background_color='#879BEC')],

       [sg.Text('I', text_color='white', background_color='#95AAFF', size=(14, 1)),
        sg.Input('', background_color='#879BEC', size=(16, 2)),
        sg.Text(f"{' ' * 4}", background_color='#616EA4'),
        sg.Input('', background_color='#879BEC', size=(16, 2)),
        sg.Text(f"{' ' * 4}", background_color='#616EA4'),

        sg.Input('', background_color='#879BEC', size=(15, 2))],

       [sg.Text('II', text_color='white', background_color='#95AAFF', size=(14, 1)),
        sg.Input('', background_color='#879BEC', size=(16, 2)),
        sg.Text(f"{' ' * 4}", background_color='#616EA4'),
        sg.Input('', background_color='#879BEC', size=(16, 2)),
        sg.Text(f"{' ' * 4}", background_color='#616EA4'),

        sg.Input('', background_color='#879BEC', size=(15, 2))],

       [sg.Text('III', text_color='white', background_color='#95AAFF', size=(14, 1)),
        sg.Input('', background_color='#879BEC', size=(16, 2)),
        sg.Text(f"{' ' * 4}", background_color='#616EA4'),
        sg.Input('', background_color='#879BEC', size=(16, 2)),
        sg.Text(f"{' ' * 4}", background_color='#616EA4'),

        sg.Input('', background_color='#879BEC', size=(15, 2))],

       [sg.Text('Прибыль (руб.)', text_color='white', background_color='#95AAFF', size=(14, 1)),
        sg.Input('', background_color='#879BEC', size=(16, 2)),
        sg.Text(f"{' ' * 4}", background_color='#616EA4'),
        sg.Input('', background_color='#879BEC', size=(16, 2)),
        sg.Text(f"{' ' * 4}", background_color='#616EA4'),

        sg.Input('', background_color='#879BEC', size=(15, 2), readonly=True,
                 disabled_readonly_background_color='#879BEC')],
       ]

layout = [[sg.Text('Вариант 8', font='Any 18')],
          [sg.Text(TEXT)],
          [sg.Column(col, background_color='#616EA4')],
          [sg.Push()],
          [sg.Text("Выберите метод решения: ")],
          [sg.Push(),
           sg.Button("Scipy", size=(7, 2)), sg.Button("Algorithm", size=(7, 2)),
           sg.Push()],
          [sg.Push()],
          [sg.Button('Решить задачу'), sg.Button('Cancel')], ]

dispatch_dictionary = {'scipy': Solution_scipy, 'Algo': Solution_algo}

window = sg.Window('Window Title', layout)
temp = 0
func_to_call = None
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event in dispatch_dictionary:
        func_to_call = dispatch_dictionary[event]
        temp = 1
        print('#Debug#: Выбрано решение ', event)
    if event == 'Решить задачу':
        if all(list(values.values())[:18]) and temp:
            print("#Debug#: Решаем")
            result = func_to_call(list(values.values())[:12])
            sg.popup(result)
        else:
            sg.popup_ok("Не все значения введены или не выбран тип решения")
            print("#Debug#: Не все значения введены или не выбран тип решения")

window.close()
