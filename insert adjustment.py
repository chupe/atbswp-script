#!/bin/env python3
# Created by atbswp (https://github.com/rmpr/atbswp)
# on 16 Nov 2020
import pyautogui
import time
pyautogui.FAILSAFE = False

rows = 24
fee = '.15'
y_adjustment = 0
y_adjustment_platform = 59

start_date = {
    'col': 7,
    'row': 3
}
start_date['col'] -= 1
start_date['row'] -= 1
calendar_field_loc = {
    'x': 1333,
    'y': 370 + y_adjustment_platform
}
date = {
    'x': calendar_field_loc['x'] + 37 * (start_date['col']),
    'y': calendar_field_loc['y'] + 110 + 30 * (start_date['row']),
    'col': start_date['col'],
    'row': start_date['row'],
    'seq': 0
}


def enter_next():

    def close_calendar():
        pyautogui.mouseDown(1445, 265, 'left')
        pyautogui.mouseUp(1445, 265, 'left')
        return

    def get_date_loc():
        global start_date
        global calendar_field_loc
        global date
        print('before modification date:', date)

        date['seq'] += 1

        calendar_root = {
            'x': calendar_field_loc['x'],
            'y': calendar_field_loc['y'] + 110,
        }

        if date['col'] > 6:
            date['col'] = 0
            date['row'] += 1

        date['y'] = calendar_root['y'] + 30 * date['row']

        if date['row'] > 6:
            return

        date['x'] = calendar_root['x'] + 37 * date['col']

        print('after modification date:', date)

        date['col'] += 1
        return date

    def enter_adjustment(date):
        global y_adjustment_platform

        total_field = {
            'x': 850,
            'y': 470 + y_adjustment_platform
        }
        matched_field = {
            'x': 1140,
            'y': 470 + y_adjustment_platform
        }
        paid_field = {
            'x': 1385,
            'y': 470 + y_adjustment_platform
        }
        revenue_field = {
            'x': 1590,
            'y': 470 + y_adjustment_platform
        }
        fee_field = {
            'x': 1770,
            'y': 470 + y_adjustment_platform
        }
        date_field_table = {
            'x': 115,
            'y': 337
        }
        total_field_table = {
            'x': 230,
            'y': 337
        }
        matched_field_table = {
            'x': 345,
            'y': 337
        }
        paid_field_table = {
            'x': 460,
            'y': 337
        }
        revenue_field_table = {
            'x': 555,
            'y': 337
        }

        global y_adjustment

        def click(field):
            pyautogui.mouseDown(field['x'], field['y'] + y_adjustment, 'left')
            pyautogui.mouseUp(field['x'], field['y'] + y_adjustment, 'left')
            print('click field:', field)
            return

        def copy():
            pyautogui.keyDown('ctrlleft')
            pyautogui.keyDown('c')
            pyautogui.keyUp('c')
            pyautogui.keyUp('ctrlleft')
            return

        def paste():
            pyautogui.keyDown('ctrlleft')
            pyautogui.keyDown('v')
            pyautogui.keyUp('v')
            pyautogui.keyUp('ctrlleft')
            return

        def enter_fee():
            global fee

            def split(word):
                return [char for char in word]

            for char in split(fee):
                pyautogui.keyDown(char)
                pyautogui.keyUp(char)
                pass

            return

        def get_table_value(field):
            global date
            table_field = field
            table_field['y'] = table_field['y'] + ((date['seq'] - 1) * 23)
            return table_field

        def get_field_location(field):
            global date
            table_field = field
            if date['seq'] > 1:
                table_field['y'] = table_field['y'] + 51
            return table_field

        def select_all():
            pyautogui.keyDown('ctrlleft')
            pyautogui.keyDown('a')
            pyautogui.keyUp('a')
            pyautogui.keyUp('ctrlleft')
            return

        def open_calendar():
            global calendar_field_loc

            if date['seq'] == 2:
                calendar_field_loc['y'] = calendar_field_loc['y'] + 51

            pyautogui.mouseDown(
                calendar_field_loc['x'], calendar_field_loc['y'] + y_adjustment, 'left')
            pyautogui.mouseUp(
                calendar_field_loc['x'], calendar_field_loc['y'] + y_adjustment, 'left')
            print('calendar field:', calendar_field_loc)
            return

        print('-----------------------------------------------')

        click(get_table_value(date_field_table))
        copy()
        open_calendar()
        # click(calendar_field_loc)
        select_all()
        paste()

        click(get_table_value(total_field_table))
        copy()
        click(get_field_location(total_field))
        paste()

        click(get_table_value(matched_field_table))
        copy()
        click(get_field_location(matched_field))
        paste()

        click(get_table_value(paid_field_table))
        copy()
        click(get_field_location(paid_field))
        paste()

        click(get_table_value(revenue_field_table))
        copy()
        click(get_field_location(revenue_field))
        paste()

        click(get_field_location(fee_field))
        enter_fee()

        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')
        time.sleep(2)

        print('finished')
        return

    def click(field):
        global y_adjustment

        pyautogui.mouseDown(field['x'], field['y'] + y_adjustment, 'left')
        pyautogui.mouseUp(field['x'], field['y'] + y_adjustment, 'left')
        print('click calendar:', field)
        return

    date = get_date_loc()
    enter_adjustment(date)
    return


for i in range(0, rows):
    enter_next()
