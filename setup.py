from distutils.core import setup, Extension

setup(name='Drug',
      version='1.0',
      py_modules=['Main_GUI','medicine','medicine_conn','pharmacy','pharmacy_conn','Search','telegram','telegram_conn'],
      data_files=[('resource',['resource\\address_list.json','resource\\logo-gmail.png','resource\\medicine.png','resource\\medicine2.png',
                               'resource\\pharmacy.png','resource\\pharmacy2.png'
                               ,'resource\\search.png','resource\\search2.png','resource\\text.png'],)]
      )