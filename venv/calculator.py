import PySimpleGUI as sg

input_num = sg.InputText("")
number_one = sg.Button("1")
number_two = sg.Button("2")
number_three = sg.Button("3")
plus = sg.Button("+")

number_four = sg.Button("4")
number_five = sg.Button("5")
number_six = sg.Button("6")
minus = sg.Button("-")

number_seven = sg.Button("7")
number_eight = sg.Button("8")
number_nine = sg.Button("9")
times = sg.Button("*")

divide = sg.Button("/")

window = sg.Window("Kalkalator", layout=[[input_num],
                                          [number_one, number_two, number_three, plus],
                                          [number_four, number_five, number_six, minus],
                                          [number_seven, number_eight, number_nine, divide],
                                          [times]
                                          ])
window.read()
window.close()
